"""
Head-to-Head Matchup Analysis for Cosmic Encounter.

Provides tools for analyzing how specific alien powers perform against each other,
identifying counters, synergies, and matchup advantages.
"""

import json
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any, Set
from collections import defaultdict
import math
from pathlib import Path

from ..game import Game
from ..types import GameConfig
from ..aliens import AlienRegistry


@dataclass
class MatchupResult:
    """Results for a specific alien vs alien matchup."""
    alien_a: str
    alien_b: str
    games_played: int = 0
    a_wins: int = 0
    b_wins: int = 0
    a_solo_wins: int = 0
    b_solo_wins: int = 0
    draws: int = 0  # Both win (shared victory)
    neither_wins: int = 0  # Third party wins

    @property
    def a_win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.a_wins / self.games_played

    @property
    def b_win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.b_wins / self.games_played

    @property
    def a_advantage(self) -> float:
        """Positive if A has advantage, negative if B has advantage."""
        if self.games_played == 0:
            return 0.0
        return self.a_win_rate - self.b_win_rate

    def to_dict(self) -> Dict[str, Any]:
        return {
            "alien_a": self.alien_a,
            "alien_b": self.alien_b,
            "games_played": self.games_played,
            "a_wins": self.a_wins,
            "b_wins": self.b_wins,
            "a_win_rate": round(self.a_win_rate * 100, 2),
            "b_win_rate": round(self.b_win_rate * 100, 2),
            "a_advantage": round(self.a_advantage * 100, 2),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatchupResult":
        return cls(
            alien_a=data["alien_a"],
            alien_b=data["alien_b"],
            games_played=data.get("games_played", 0),
            a_wins=data.get("a_wins", 0),
            b_wins=data.get("b_wins", 0),
            a_solo_wins=data.get("a_solo_wins", 0),
            b_solo_wins=data.get("b_solo_wins", 0),
            draws=data.get("draws", 0),
            neither_wins=data.get("neither_wins", 0),
        )


@dataclass
class MatchupMatrix:
    """Matrix of all matchup results between aliens."""
    matchups: Dict[Tuple[str, str], MatchupResult] = field(default_factory=dict)
    total_games: int = 0

    def get_matchup(self, alien_a: str, alien_b: str) -> MatchupResult:
        """Get matchup result, creating if needed. Always uses sorted order."""
        key = tuple(sorted([alien_a, alien_b]))
        if key not in self.matchups:
            self.matchups[key] = MatchupResult(alien_a=key[0], alien_b=key[1])
        return self.matchups[key]

    def record_game(
        self,
        aliens_in_game: List[str],
        winners: List[str],
        solo_win: bool
    ) -> None:
        """Record results of a game for all matchups present."""
        self.total_games += 1

        # Record matchup for each pair of aliens in the game
        for i, alien_a in enumerate(aliens_in_game):
            for alien_b in aliens_in_game[i+1:]:
                matchup = self.get_matchup(alien_a, alien_b)
                matchup.games_played += 1

                a_won = alien_a in winners
                b_won = alien_b in winners

                # Use the canonical order from the matchup
                if matchup.alien_a == alien_a:
                    if a_won and b_won:
                        matchup.draws += 1
                        matchup.a_wins += 1
                        matchup.b_wins += 1
                    elif a_won:
                        matchup.a_wins += 1
                        if solo_win:
                            matchup.a_solo_wins += 1
                    elif b_won:
                        matchup.b_wins += 1
                        if solo_win:
                            matchup.b_solo_wins += 1
                    else:
                        matchup.neither_wins += 1
                else:
                    # Aliens are swapped in this key
                    if a_won and b_won:
                        matchup.draws += 1
                        matchup.a_wins += 1
                        matchup.b_wins += 1
                    elif a_won:
                        matchup.b_wins += 1
                        if solo_win:
                            matchup.b_solo_wins += 1
                    elif b_won:
                        matchup.a_wins += 1
                        if solo_win:
                            matchup.a_solo_wins += 1
                    else:
                        matchup.neither_wins += 1

    def get_best_matchups(self, alien: str, top_n: int = 10) -> List[Tuple[str, float]]:
        """Get aliens that this alien performs best against."""
        results = []
        for key, matchup in self.matchups.items():
            if alien not in key:
                continue
            if matchup.games_played < 10:
                continue

            opponent = key[1] if key[0] == alien else key[0]
            if matchup.alien_a == alien:
                advantage = matchup.a_advantage
            else:
                advantage = -matchup.a_advantage
            results.append((opponent, advantage))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_n]

    def get_worst_matchups(self, alien: str, top_n: int = 10) -> List[Tuple[str, float]]:
        """Get aliens that counter this alien."""
        results = self.get_best_matchups(alien, top_n=1000)
        results.reverse()
        return results[:top_n]

    def get_counters(self, alien: str, min_advantage: float = 0.1) -> List[str]:
        """Get aliens that have significant advantage over this alien."""
        counters = []
        for opponent, advantage in self.get_worst_matchups(alien, top_n=50):
            if advantage < -min_advantage:
                counters.append(opponent)
        return counters

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total_games": self.total_games,
            "matchups": {
                f"{k[0]}_vs_{k[1]}": v.to_dict()
                for k, v in self.matchups.items()
            }
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MatchupMatrix":
        matrix = cls(total_games=data.get("total_games", 0))
        for key_str, matchup_data in data.get("matchups", {}).items():
            result = MatchupResult.from_dict(matchup_data)
            key = (result.alien_a, result.alien_b)
            matrix.matchups[key] = result
        return matrix


@dataclass
class MatchupAnalyzer:
    """
    Analyzes head-to-head matchups between alien powers.
    """
    matrix: MatchupMatrix = field(default_factory=MatchupMatrix)
    data_file: Optional[Path] = None

    def __post_init__(self):
        if self.data_file and self.data_file.exists():
            self.load()

    def run_matchup_simulation(
        self,
        alien_a: str,
        alien_b: str,
        num_games: int = 1000,
        player_count: int = 4,
        show_progress: bool = True
    ) -> MatchupResult:
        """
        Run simulations specifically for two aliens to get matchup data.

        Places both aliens in every game and fills remaining slots randomly.
        """
        from .runner import Simulator
        from ..types import SimulationConfig

        # Verify aliens exist
        registry = AlienRegistry
        if not registry.get(alien_a):
            raise ValueError(f"Unknown alien: {alien_a}")
        if not registry.get(alien_b):
            raise ValueError(f"Unknown alien: {alien_b}")

        matchup = self.matrix.get_matchup(alien_a, alien_b)

        for i in range(num_games):
            if show_progress and (i + 1) % 100 == 0:
                print(f"  Matchup simulation: {i + 1}/{num_games}")

            # Create game with both aliens guaranteed
            config = GameConfig(
                num_players=player_count,
                required_aliens=[alien_a, alien_b]
            )

            try:
                game = Game(config)
                game.setup()
                winners = game.play()  # Returns list of winning players

                # Get results
                winner_aliens = [p.alien.name for p in winners if p.alien]
                aliens_in_game = [p.alien.name for p in game.players if p.alien]
                solo_win = len(winners) == 1

                # Record result
                self.matrix.record_game(aliens_in_game, winner_aliens, solo_win)

            except Exception as e:
                # Skip failed games
                continue

        if self.data_file:
            self.save()

        return self.matrix.get_matchup(alien_a, alien_b)

    def run_full_matrix_simulation(
        self,
        aliens: Optional[List[str]] = None,
        games_per_matchup: int = 100,
        player_count: int = 4,
        show_progress: bool = True
    ) -> None:
        """
        Run simulations for all alien pairs.

        Warning: This can take a very long time for many aliens.
        """
        if aliens is None:
            aliens = [a.name for a in AlienRegistry.get_all()]

        total_pairs = len(aliens) * (len(aliens) - 1) // 2
        pair_num = 0

        for i, alien_a in enumerate(aliens):
            for alien_b in aliens[i+1:]:
                pair_num += 1
                if show_progress:
                    print(f"Matchup {pair_num}/{total_pairs}: {alien_a} vs {alien_b}")

                self.run_matchup_simulation(
                    alien_a, alien_b,
                    num_games=games_per_matchup,
                    player_count=player_count,
                    show_progress=False
                )

    def run_targeted_analysis(
        self,
        target_aliens: List[str],
        games_per_matchup: int = 500,
        player_count: int = 4
    ) -> Dict[str, Dict[str, Any]]:
        """
        Run detailed matchup analysis for specific aliens.

        Returns analysis of how each target performs against all others.
        """
        all_aliens = [a.name for a in AlienRegistry.get_all()]
        results = {}

        for target in target_aliens:
            print(f"\nAnalyzing {target}...")
            target_results = {
                "best_matchups": [],
                "worst_matchups": [],
                "counters": [],
                "countered_by": [],
            }

            for opponent in all_aliens:
                if opponent == target:
                    continue

                self.run_matchup_simulation(
                    target, opponent,
                    num_games=games_per_matchup,
                    player_count=player_count,
                    show_progress=False
                )

            target_results["best_matchups"] = self.matrix.get_best_matchups(target, 10)
            target_results["worst_matchups"] = self.matrix.get_worst_matchups(target, 10)
            target_results["counters"] = self.matrix.get_counters(target)

            results[target] = target_results

        return results

    def generate_report(
        self,
        alien: str,
        min_games: int = 50
    ) -> str:
        """Generate a text report for a specific alien's matchups."""
        lines = [
            f"=== Matchup Report: {alien} ===",
            "",
        ]

        # Best matchups
        lines.append("Top Favorable Matchups:")
        for opponent, advantage in self.matrix.get_best_matchups(alien, 10):
            matchup = self.matrix.get_matchup(alien, opponent)
            if matchup.games_played < min_games:
                continue
            lines.append(
                f"  vs {opponent}: +{advantage*100:.1f}% advantage "
                f"({matchup.games_played} games)"
            )

        lines.append("")
        lines.append("Worst Matchups (Counters):")
        for opponent, advantage in self.matrix.get_worst_matchups(alien, 10):
            matchup = self.matrix.get_matchup(alien, opponent)
            if matchup.games_played < min_games:
                continue
            lines.append(
                f"  vs {opponent}: {advantage*100:.1f}% advantage "
                f"({matchup.games_played} games)"
            )

        return "\n".join(lines)

    def save(self, filepath: Optional[Path] = None) -> None:
        """Save matchup data to JSON file."""
        path = filepath or self.data_file
        if path is None:
            raise ValueError("No filepath specified")

        with open(path, 'w') as f:
            json.dump(self.matrix.to_dict(), f, indent=2)

    def load(self, filepath: Optional[Path] = None) -> None:
        """Load matchup data from JSON file."""
        path = filepath or self.data_file
        if path is None or not path.exists():
            return

        with open(path, 'r') as f:
            data = json.load(f)
            self.matrix = MatchupMatrix.from_dict(data)


def run_quick_matchup(
    alien_a: str,
    alien_b: str,
    games: int = 1000
) -> MatchupResult:
    """
    Quick function to run matchup analysis between two aliens.

    Example:
        result = run_quick_matchup("Machine", "Virus", 1000)
        print(f"Machine win rate: {result.a_win_rate:.1%}")
    """
    analyzer = MatchupAnalyzer()
    return analyzer.run_matchup_simulation(alien_a, alien_b, games)


def find_counters(
    alien: str,
    games_per_matchup: int = 200,
    top_n: int = 10
) -> List[Tuple[str, float]]:
    """
    Find the best counters to a specific alien.

    Example:
        counters = find_counters("Machine", 200)
        for counter, advantage in counters:
            print(f"{counter}: {advantage:.1%} advantage")
    """
    analyzer = MatchupAnalyzer()
    all_aliens = [a.name for a in AlienRegistry.get_all()]

    print(f"Finding counters to {alien}...")
    for opponent in all_aliens:
        if opponent == alien:
            continue
        analyzer.run_matchup_simulation(
            alien, opponent,
            num_games=games_per_matchup,
            show_progress=False
        )

    return analyzer.matrix.get_worst_matchups(alien, top_n)
