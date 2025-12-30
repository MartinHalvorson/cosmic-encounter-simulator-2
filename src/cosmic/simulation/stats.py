"""
Statistics collection and analysis for Cosmic Encounter simulations.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
import json
import csv
from io import StringIO


@dataclass
class AlienStats:
    """Statistics for a single alien power."""
    name: str
    games_played: int = 0
    games_won: int = 0
    shared_wins: int = 0
    solo_wins: int = 0
    alternate_wins: int = 0
    total_turns: int = 0
    total_colonies_at_end: int = 0

    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.games_won / self.games_played

    @property
    def solo_win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.solo_wins / self.games_played

    @property
    def avg_turns_per_game(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.total_turns / self.games_played

    @property
    def avg_colonies(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.total_colonies_at_end / self.games_played

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "win_rate": round(self.win_rate * 100, 2),
            "solo_wins": self.solo_wins,
            "shared_wins": self.shared_wins,
            "alternate_wins": self.alternate_wins,
            "avg_colonies": round(self.avg_colonies, 2),
        }


@dataclass
class Statistics:
    """
    Comprehensive statistics for simulation runs.
    """
    # Per-alien statistics
    alien_stats: Dict[str, AlienStats] = field(default_factory=dict)

    # Per-player-count statistics
    games_by_player_count: Dict[int, int] = field(default_factory=dict)
    wins_by_player_count: Dict[int, Dict[str, int]] = field(default_factory=dict)

    # Game length statistics
    turn_counts: List[int] = field(default_factory=list)
    shared_victory_count: int = 0
    solo_victory_count: int = 0
    timeout_count: int = 0
    error_count: int = 0

    # Total games
    total_games: int = 0

    def record_game(
        self,
        num_players: int,
        winners: List[str],
        alien_map: Dict[str, str],
        turn_count: int,
        final_colonies: Dict[str, int],
        alternate_win: bool = False,
        timed_out: bool = False,
        errored: bool = False
    ) -> None:
        """
        Record statistics from a completed game.

        Args:
            num_players: Number of players in the game
            winners: List of winning player names
            alien_map: Mapping of player name to alien power name
            turn_count: Number of turns the game lasted
            final_colonies: Mapping of player name to final colony count
            alternate_win: Whether the win was via alternate condition
            timed_out: Whether the game timed out
            errored: Whether the game had an error
        """
        self.total_games += 1
        self.turn_counts.append(turn_count)

        # Track player count
        self.games_by_player_count[num_players] = (
            self.games_by_player_count.get(num_players, 0) + 1
        )

        if num_players not in self.wins_by_player_count:
            self.wins_by_player_count[num_players] = {}

        # Track timeouts/errors
        if timed_out:
            self.timeout_count += 1
        if errored:
            self.error_count += 1
            return

        # Track shared vs solo victories
        if len(winners) > 1:
            self.shared_victory_count += 1
        elif len(winners) == 1:
            self.solo_victory_count += 1

        # Update alien statistics
        for player_name, alien_name in alien_map.items():
            if alien_name not in self.alien_stats:
                self.alien_stats[alien_name] = AlienStats(name=alien_name)

            stats = self.alien_stats[alien_name]
            stats.games_played += 1
            stats.total_turns += turn_count
            stats.total_colonies_at_end += final_colonies.get(player_name, 0)

            if player_name in winners:
                stats.games_won += 1

                # Track win by player count
                wins_dict = self.wins_by_player_count[num_players]
                wins_dict[alien_name] = wins_dict.get(alien_name, 0) + 1

                if len(winners) == 1:
                    stats.solo_wins += 1
                else:
                    stats.shared_wins += 1

                if alternate_win:
                    stats.alternate_wins += 1

    @property
    def avg_game_length(self) -> float:
        if not self.turn_counts:
            return 0.0
        return sum(self.turn_counts) / len(self.turn_counts)

    @property
    def min_game_length(self) -> int:
        return min(self.turn_counts) if self.turn_counts else 0

    @property
    def max_game_length(self) -> int:
        return max(self.turn_counts) if self.turn_counts else 0

    def get_rankings(self, by: str = "win_rate") -> List[AlienStats]:
        """
        Get alien powers ranked by a metric.

        Args:
            by: Metric to rank by ("win_rate", "games_played", "solo_win_rate")

        Returns:
            List of AlienStats sorted by the metric (descending)
        """
        stats_list = list(self.alien_stats.values())

        if by == "win_rate":
            stats_list.sort(key=lambda s: s.win_rate, reverse=True)
        elif by == "solo_win_rate":
            stats_list.sort(key=lambda s: s.solo_win_rate, reverse=True)
        elif by == "games_played":
            stats_list.sort(key=lambda s: s.games_played, reverse=True)

        return stats_list

    def get_win_rates_by_player_count(self, alien_name: str) -> Dict[int, float]:
        """Get win rates for an alien across different player counts."""
        result = {}

        for player_count, wins_dict in self.wins_by_player_count.items():
            total_games = self.games_by_player_count.get(player_count, 0)
            if total_games > 0:
                wins = wins_dict.get(alien_name, 0)
                # Adjust for number of players
                # Expected win rate = 1 / num_players
                result[player_count] = wins / total_games

        return result

    def summary(self) -> str:
        """Generate a text summary of statistics."""
        lines = [
            "=" * 60,
            "COSMIC ENCOUNTER SIMULATION RESULTS",
            "=" * 60,
            "",
            f"Total Games: {self.total_games}",
            f"Solo Victories: {self.solo_victory_count}",
            f"Shared Victories: {self.shared_victory_count}",
            f"Timeouts: {self.timeout_count}",
            f"Errors: {self.error_count}",
            "",
            f"Average Game Length: {self.avg_game_length:.1f} turns",
            f"Shortest Game: {self.min_game_length} turns",
            f"Longest Game: {self.max_game_length} turns",
            "",
            "-" * 60,
            "ALIEN POWER WIN RATES",
            "-" * 60,
        ]

        # Rank by win rate
        rankings = self.get_rankings("win_rate")
        for i, stats in enumerate(rankings, 1):
            lines.append(
                f"{i:3}. {stats.name:20} {stats.win_rate*100:5.1f}% "
                f"({stats.games_won}/{stats.games_played})"
            )

        lines.append("")
        lines.append("=" * 60)

        return "\n".join(lines)

    def to_csv(self) -> str:
        """Export statistics to CSV format."""
        output = StringIO()
        writer = csv.writer(output)

        # Header
        writer.writerow([
            "Alien", "Games Played", "Games Won", "Win Rate %",
            "Solo Wins", "Shared Wins", "Alternate Wins",
            "Avg Colonies"
        ])

        # Data
        for stats in self.get_rankings("win_rate"):
            writer.writerow([
                stats.name,
                stats.games_played,
                stats.games_won,
                round(stats.win_rate * 100, 2),
                stats.solo_wins,
                stats.shared_wins,
                stats.alternate_wins,
                round(stats.avg_colonies, 2),
            ])

        return output.getvalue()

    def to_json(self) -> str:
        """Export statistics to JSON format."""
        data = {
            "summary": {
                "total_games": self.total_games,
                "solo_victories": self.solo_victory_count,
                "shared_victories": self.shared_victory_count,
                "timeouts": self.timeout_count,
                "errors": self.error_count,
                "avg_game_length": round(self.avg_game_length, 2),
            },
            "alien_stats": [
                stats.to_dict()
                for stats in self.get_rankings("win_rate")
            ],
            "games_by_player_count": self.games_by_player_count,
        }
        return json.dumps(data, indent=2)

    def save_csv(self, filepath: str) -> None:
        """Save statistics to a CSV file."""
        with open(filepath, "w") as f:
            f.write(self.to_csv())

    def save_json(self, filepath: str) -> None:
        """Save statistics to a JSON file."""
        with open(filepath, "w") as f:
            f.write(self.to_json())
