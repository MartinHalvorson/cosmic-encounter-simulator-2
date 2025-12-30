"""
Cumulative statistics tracking with ELO ratings for Cosmic Encounter simulations.

This module provides persistent statistics that accumulate across simulation runs,
including ELO rating calculations for comparing alien power strength.
"""

import json
import os
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path


@dataclass
class AlienEloStats:
    """Statistics and ELO rating for a single alien power."""
    name: str
    games_played: int = 0
    games_won: int = 0
    solo_wins: int = 0
    shared_wins: int = 0
    elo_rating: float = 1500.0  # Starting ELO
    peak_elo: float = 1500.0
    total_colonies_at_end: int = 0
    total_turns_played: int = 0

    # For ELO calculation tracking
    _elo_games: int = field(default=0, repr=False)

    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.games_won / self.games_played

    @property
    def win_rate_percent(self) -> float:
        return self.win_rate * 100

    @property
    def solo_win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.solo_wins / self.games_played

    @property
    def avg_colonies(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.total_colonies_at_end / self.games_played

    @property
    def avg_turns(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.total_turns_played / self.games_played

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "win_rate": round(self.win_rate * 100, 2),
            "solo_wins": self.solo_wins,
            "shared_wins": self.shared_wins,
            "elo_rating": round(self.elo_rating, 1),
            "peak_elo": round(self.peak_elo, 1),
            "avg_colonies": round(self.avg_colonies, 2),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AlienEloStats":
        return cls(
            name=data["name"],
            games_played=data.get("games_played", 0),
            games_won=data.get("games_won", 0),
            solo_wins=data.get("solo_wins", 0),
            shared_wins=data.get("shared_wins", 0),
            elo_rating=data.get("elo_rating", 1500.0),
            peak_elo=data.get("peak_elo", 1500.0),
            total_colonies_at_end=data.get("total_colonies_at_end", 0),
            total_turns_played=data.get("total_turns_played", 0),
        )


class EloCalculator:
    """Calculate ELO rating changes for multiplayer games."""

    def __init__(self, k_factor: float = 32.0, base_k: float = 400.0):
        self.k_factor = k_factor
        self.base_k = base_k

    def expected_score(self, player_elo: float, opponent_elo: float) -> float:
        """Calculate expected score against a single opponent."""
        return 1.0 / (1.0 + 10 ** ((opponent_elo - player_elo) / self.base_k))

    def calculate_multiplayer_changes(
        self,
        player_ratings: Dict[str, float],
        winner_names: List[str]
    ) -> Dict[str, float]:
        """
        Calculate ELO changes for a multiplayer game.

        Uses average expected score against all opponents.
        Winners get score 1.0, others get 0.0 (shared wins split the point).

        Args:
            player_ratings: Dict mapping player/alien name to current ELO
            winner_names: List of winning player/alien names

        Returns:
            Dict mapping player name to ELO change (delta)
        """
        players = list(player_ratings.keys())
        n = len(players)

        if n < 2:
            return {p: 0.0 for p in players}

        changes = {}

        for player in players:
            # Calculate expected score against average opponent
            player_elo = player_ratings[player]
            opponents = [p for p in players if p != player]

            # Expected score is average expected vs each opponent
            expected = sum(
                self.expected_score(player_elo, player_ratings[opp])
                for opp in opponents
            ) / len(opponents)

            # Actual score: 1 for solo win, 1/num_winners for shared, 0 for loss
            if player in winner_names:
                actual = 1.0 / len(winner_names)
            else:
                actual = 0.0

            # ELO change
            # Adjust K factor based on games played (higher K for new players)
            change = self.k_factor * (actual - expected)
            changes[player] = change

        return changes


@dataclass
class CumulativeStats:
    """
    Persistent cumulative statistics across simulation runs.

    Stores data in JSON format and supports ELO rating tracking.
    """
    # Per-alien statistics with ELO
    alien_stats: Dict[str, AlienEloStats] = field(default_factory=dict)

    # Overall statistics
    total_games: int = 0
    solo_victories: int = 0
    shared_victories: int = 0
    timeouts: int = 0
    errors: int = 0

    # Game length stats
    total_turns: int = 0
    min_game_length: int = 999999
    max_game_length: int = 0

    # Games by player count
    games_by_player_count: Dict[int, int] = field(default_factory=dict)

    # Metadata
    last_updated: str = ""
    simulation_runs: int = 0

    # ELO calculator
    _elo_calc: EloCalculator = field(default_factory=EloCalculator, repr=False)

    def record_game(
        self,
        alien_map: Dict[str, str],  # player_name -> alien_name
        winner_names: List[str],
        final_colonies: Dict[str, int],
        turn_count: int,
        num_players: int,
        timed_out: bool = False,
        errored: bool = False
    ) -> None:
        """Record a single game result."""
        self.total_games += 1
        self.total_turns += turn_count

        # Track game length
        if turn_count < self.min_game_length:
            self.min_game_length = turn_count
        if turn_count > self.max_game_length:
            self.max_game_length = turn_count

        # Track player count
        self.games_by_player_count[num_players] = (
            self.games_by_player_count.get(num_players, 0) + 1
        )

        if timed_out:
            self.timeouts += 1
        if errored:
            self.errors += 1
            return

        # Track victory type
        if len(winner_names) > 1:
            self.shared_victories += 1
        elif len(winner_names) == 1:
            self.solo_victories += 1

        # Get current ratings for ELO calculation
        player_ratings = {}
        for player_name, alien_name in alien_map.items():
            if alien_name not in self.alien_stats:
                self.alien_stats[alien_name] = AlienEloStats(name=alien_name)
            player_ratings[alien_name] = self.alien_stats[alien_name].elo_rating

        # Map winner player names to alien names
        winner_aliens = [alien_map[name] for name in winner_names if name in alien_map]

        # Calculate ELO changes
        elo_changes = self._elo_calc.calculate_multiplayer_changes(
            player_ratings, winner_aliens
        )

        # Update alien statistics
        for player_name, alien_name in alien_map.items():
            stats = self.alien_stats[alien_name]
            stats.games_played += 1
            stats.total_turns_played += turn_count
            stats.total_colonies_at_end += final_colonies.get(player_name, 0)

            # Update ELO
            if alien_name in elo_changes:
                stats.elo_rating += elo_changes[alien_name]
                if stats.elo_rating > stats.peak_elo:
                    stats.peak_elo = stats.elo_rating

            # Track wins
            if player_name in winner_names:
                stats.games_won += 1
                if len(winner_names) == 1:
                    stats.solo_wins += 1
                else:
                    stats.shared_wins += 1

        self.last_updated = datetime.now().isoformat()

    @property
    def avg_game_length(self) -> float:
        if self.total_games == 0:
            return 0.0
        return self.total_turns / self.total_games

    def get_rankings(self, by: str = "elo") -> List[AlienEloStats]:
        """
        Get alien powers ranked by a metric.

        Args:
            by: "elo", "win_rate", "games_played"
        """
        stats_list = list(self.alien_stats.values())

        if by == "elo":
            stats_list.sort(key=lambda s: s.elo_rating, reverse=True)
        elif by == "win_rate":
            stats_list.sort(key=lambda s: (s.win_rate, s.games_played), reverse=True)
        elif by == "games_played":
            stats_list.sort(key=lambda s: s.games_played, reverse=True)

        return stats_list

    def generate_readme_table(self, top_n: int = 30) -> str:
        """Generate a markdown table for the README."""
        rankings = self.get_rankings("elo")

        lines = [
            "| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |",
            "|------|-------|-----|----------|-------|-----------|--------|",
        ]

        for i, stats in enumerate(rankings[:top_n], 1):
            lines.append(
                f"| {i} | {stats.name} | {stats.elo_rating:.0f} | "
                f"{stats.win_rate_percent:.1f}% | {stats.games_played} | "
                f"{stats.solo_wins} | {stats.shared_wins} |"
            )

        if len(rankings) > top_n:
            lines.append(f"| ... | *{len(rankings) - top_n} more aliens* | ... | ... | ... | ... | ... |")

        return "\n".join(lines)

    def generate_summary(self) -> str:
        """Generate a text summary of cumulative statistics."""
        lines = [
            f"**Total Games Simulated:** {self.total_games:,}",
            f"**Solo Victories:** {self.solo_victories:,}",
            f"**Shared Victories:** {self.shared_victories:,}",
            f"**Average Game Length:** {self.avg_game_length:.1f} turns",
            f"**Last Updated:** {self.last_updated[:19] if self.last_updated else 'Never'}",
        ]
        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "total_games": self.total_games,
            "solo_victories": self.solo_victories,
            "shared_victories": self.shared_victories,
            "timeouts": self.timeouts,
            "errors": self.errors,
            "total_turns": self.total_turns,
            "min_game_length": self.min_game_length if self.min_game_length < 999999 else 0,
            "max_game_length": self.max_game_length,
            "games_by_player_count": self.games_by_player_count,
            "last_updated": self.last_updated,
            "simulation_runs": self.simulation_runs,
            "alien_stats": {
                name: stats.to_dict()
                for name, stats in self.alien_stats.items()
            }
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CumulativeStats":
        """Create from dictionary (JSON deserialization)."""
        stats = cls()
        stats.total_games = data.get("total_games", 0)
        stats.solo_victories = data.get("solo_victories", 0)
        stats.shared_victories = data.get("shared_victories", 0)
        stats.timeouts = data.get("timeouts", 0)
        stats.errors = data.get("errors", 0)
        stats.total_turns = data.get("total_turns", 0)
        stats.min_game_length = data.get("min_game_length", 999999) or 999999
        stats.max_game_length = data.get("max_game_length", 0)
        stats.games_by_player_count = {
            int(k): v for k, v in data.get("games_by_player_count", {}).items()
        }
        stats.last_updated = data.get("last_updated", "")
        stats.simulation_runs = data.get("simulation_runs", 0)

        # Restore alien stats
        for name, alien_data in data.get("alien_stats", {}).items():
            # Ensure all fields are present
            alien_data["name"] = name
            if "total_colonies_at_end" not in alien_data:
                alien_data["total_colonies_at_end"] = int(
                    alien_data.get("avg_colonies", 0) * alien_data.get("games_played", 0)
                )
            if "total_turns_played" not in alien_data:
                alien_data["total_turns_played"] = 0
            stats.alien_stats[name] = AlienEloStats.from_dict(alien_data)

        return stats

    def save(self, filepath: str = "cumulative_stats.json") -> None:
        """Save statistics to JSON file."""
        with open(filepath, "w") as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, filepath: str = "cumulative_stats.json") -> "CumulativeStats":
        """Load statistics from JSON file, or create new if not exists."""
        if os.path.exists(filepath):
            try:
                with open(filepath, "r") as f:
                    data = json.load(f)
                return cls.from_dict(data)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Warning: Could not load stats file, starting fresh: {e}")
        return cls()

    def merge(self, other: "CumulativeStats") -> None:
        """Merge another CumulativeStats into this one."""
        self.total_games += other.total_games
        self.solo_victories += other.solo_victories
        self.shared_victories += other.shared_victories
        self.timeouts += other.timeouts
        self.errors += other.errors
        self.total_turns += other.total_turns

        if other.min_game_length < self.min_game_length:
            self.min_game_length = other.min_game_length
        if other.max_game_length > self.max_game_length:
            self.max_game_length = other.max_game_length

        for count, games in other.games_by_player_count.items():
            self.games_by_player_count[count] = (
                self.games_by_player_count.get(count, 0) + games
            )

        # Merge alien stats - this is approximate for ELO
        for name, other_stats in other.alien_stats.items():
            if name not in self.alien_stats:
                self.alien_stats[name] = AlienEloStats(name=name)

            stats = self.alien_stats[name]
            total_games = stats.games_played + other_stats.games_played

            if total_games > 0:
                # Weighted average ELO
                stats.elo_rating = (
                    stats.elo_rating * stats.games_played +
                    other_stats.elo_rating * other_stats.games_played
                ) / total_games

            stats.games_played += other_stats.games_played
            stats.games_won += other_stats.games_won
            stats.solo_wins += other_stats.solo_wins
            stats.shared_wins += other_stats.shared_wins
            stats.total_colonies_at_end += other_stats.total_colonies_at_end
            stats.total_turns_played += other_stats.total_turns_played

            if other_stats.peak_elo > stats.peak_elo:
                stats.peak_elo = other_stats.peak_elo

        self.simulation_runs += 1
        self.last_updated = datetime.now().isoformat()
