"""
Player Count Analysis for Cosmic Encounter.

Analyzes how game dynamics change across different player counts.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import time

from ..types import GameConfig, SimulationConfig
from ..game import Game
from .runner import Simulator
from .stats import Statistics


@dataclass
class PlayerCountStats:
    """Statistics for a specific player count."""
    player_count: int
    games_played: int = 0
    avg_game_length: float = 0.0
    min_game_length: int = 999
    max_game_length: int = 0
    solo_victories: int = 0
    shared_victories: int = 0
    avg_allies_per_encounter: float = 0.0
    offense_win_rate: float = 0.0
    games_per_second: float = 0.0

    @property
    def shared_victory_rate(self) -> float:
        """Percentage of games ending in shared victory."""
        total = self.solo_victories + self.shared_victories
        if total == 0:
            return 0.0
        return self.shared_victories / total * 100

    @property
    def solo_victory_rate(self) -> float:
        """Percentage of games ending in solo victory."""
        return 100 - self.shared_victory_rate


@dataclass
class PlayerCountAnalysis:
    """Complete analysis across all player counts."""
    stats_by_count: Dict[int, PlayerCountStats] = field(default_factory=dict)
    top_aliens_by_count: Dict[int, List[Tuple[str, float]]] = field(default_factory=dict)
    total_games: int = 0
    total_time: float = 0.0

    def to_markdown(self) -> str:
        """Generate markdown report."""
        lines = [
            "# Player Count Analysis Report",
            "",
            f"**Total Games:** {self.total_games:,}",
            f"**Total Time:** {self.total_time:.1f}s",
            "",
            "## Game Dynamics by Player Count",
            "",
            "| Players | Games | Avg Length | Solo Win % | Shared Win % | Speed |",
            "|---------|-------|------------|------------|--------------|-------|",
        ]

        for count in sorted(self.stats_by_count.keys()):
            stats = self.stats_by_count[count]
            lines.append(
                f"| {count} | {stats.games_played} | {stats.avg_game_length:.1f} | "
                f"{stats.solo_victory_rate:.1f}% | {stats.shared_victory_rate:.1f}% | "
                f"{stats.games_per_second:.0f}/s |"
            )

        lines.extend([
            "",
            "## Key Observations",
            "",
        ])

        # Add observations
        if len(self.stats_by_count) >= 2:
            counts = sorted(self.stats_by_count.keys())
            min_count = counts[0]
            max_count = counts[-1]

            min_stats = self.stats_by_count[min_count]
            max_stats = self.stats_by_count[max_count]

            lines.append(f"- **Game Length:** {min_count}-player games average "
                        f"{min_stats.avg_game_length:.1f} turns vs "
                        f"{max_stats.avg_game_length:.1f} turns for {max_count}-player games")

            # Note: The relationship between player count and shared victories depends on game dynamics
            if min_stats.shared_victory_rate > max_stats.shared_victory_rate:
                lines.append(f"- **Shared Victories:** More common with fewer players "
                            f"({min_stats.shared_victory_rate:.1f}% with {min_count} players vs "
                            f"{max_stats.shared_victory_rate:.1f}% with {max_count} players)")
            else:
                lines.append(f"- **Shared Victories:** More common with more players "
                            f"({max_stats.shared_victory_rate:.1f}% with {max_count} players vs "
                            f"{min_stats.shared_victory_rate:.1f}% with {min_count} players)")

            lines.append(f"- **Simulation Speed:** {min_count}-player games run at "
                        f"{min_stats.games_per_second:.0f} games/sec vs "
                        f"{max_stats.games_per_second:.0f} games/sec for {max_count}-player games")

        return "\n".join(lines)


class PlayerCountAnalyzer:
    """
    Analyzes game dynamics across different player counts.
    """

    def __init__(
        self,
        games_per_count: int = 1000,
        player_counts: Optional[List[int]] = None,
        seed: Optional[int] = None
    ):
        self.games_per_count = games_per_count
        self.player_counts = player_counts or [2, 3, 4, 5, 6, 7, 8]
        self.seed = seed

    def run_analysis(self, show_progress: bool = True) -> PlayerCountAnalysis:
        """Run the full player count analysis."""
        analysis = PlayerCountAnalysis()
        start_time = time.time()

        for count in self.player_counts:
            if show_progress:
                print(f"Analyzing {count}-player games...")

            stats = self._analyze_player_count(count, show_progress)
            analysis.stats_by_count[count] = stats
            analysis.total_games += stats.games_played

        analysis.total_time = time.time() - start_time
        return analysis

    def _analyze_player_count(
        self,
        player_count: int,
        show_progress: bool
    ) -> PlayerCountStats:
        """Analyze games with a specific player count."""
        game_config = GameConfig(
            num_players=player_count,
            seed=self.seed
        )
        sim_config = SimulationConfig(
            num_games=self.games_per_count,
            game_config=game_config,
            show_progress=False,
            catch_errors=True
        )

        start = time.time()
        sim = Simulator(config=sim_config)
        results = sim.run()
        elapsed = time.time() - start

        stats = PlayerCountStats(
            player_count=player_count,
            games_played=results.games_completed,
            avg_game_length=sim.statistics.avg_game_length,
            games_per_second=results.games_completed / elapsed if elapsed > 0 else 0
        )

        # Count solo vs shared victories from alien stats
        total_wins = 0
        solo_wins = 0
        for alien_stats in sim.statistics.alien_stats.values():
            solo_wins += alien_stats.solo_wins
            total_wins += alien_stats.games_won

        stats.solo_victories = solo_wins
        stats.shared_victories = max(0, total_wins - solo_wins)

        return stats

    def quick_compare(
        self,
        counts: List[int] = [3, 4, 5, 6],
        games: int = 500
    ) -> str:
        """Quick comparison of select player counts."""
        old_games = self.games_per_count
        old_counts = self.player_counts

        self.games_per_count = games
        self.player_counts = counts

        analysis = self.run_analysis(show_progress=True)

        self.games_per_count = old_games
        self.player_counts = old_counts

        return analysis.to_markdown()


def run_player_count_analysis(
    games_per_count: int = 1000,
    player_counts: Optional[List[int]] = None
) -> PlayerCountAnalysis:
    """Run a complete player count analysis."""
    analyzer = PlayerCountAnalyzer(
        games_per_count=games_per_count,
        player_counts=player_counts
    )
    return analyzer.run_analysis()


def compare_player_counts(
    counts: List[int] = [3, 4, 5, 6],
    games: int = 500
) -> str:
    """Quick comparison of player counts."""
    analyzer = PlayerCountAnalyzer()
    return analyzer.quick_compare(counts, games)
