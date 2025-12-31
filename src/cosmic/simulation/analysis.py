"""
Simulation analysis tools for Cosmic Encounter.

Provides statistical analysis, power balance insights, and visualization-ready data.
"""

import json
import statistics
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from collections import defaultdict

from .cumulative_stats import CumulativeStats, AlienEloStats


@dataclass
class PowerBalanceReport:
    """Report on power balance across aliens."""
    overpowered: List[Tuple[str, float]]  # (name, win_rate) for OP aliens
    underpowered: List[Tuple[str, float]]  # (name, win_rate) for weak aliens
    balanced: List[str]  # names of balanced aliens
    average_win_rate: float
    median_win_rate: float
    standard_deviation: float
    win_rate_range: Tuple[float, float]  # (min, max)

    def to_markdown(self) -> str:
        """Generate markdown report."""
        lines = [
            "## Power Balance Report",
            "",
            f"**Average Win Rate:** {self.average_win_rate:.1f}%",
            f"**Median Win Rate:** {self.median_win_rate:.1f}%",
            f"**Standard Deviation:** {self.standard_deviation:.2f}%",
            f"**Win Rate Range:** {self.win_rate_range[0]:.1f}% - {self.win_rate_range[1]:.1f}%",
            "",
            "### Potentially Overpowered (Win Rate > Mean + 2σ)",
            "",
        ]

        if self.overpowered:
            lines.append("| Alien | Win Rate |")
            lines.append("|-------|----------|")
            for name, rate in self.overpowered[:10]:
                lines.append(f"| {name} | {rate:.1f}% |")
        else:
            lines.append("*None identified*")

        lines.extend([
            "",
            "### Potentially Underpowered (Win Rate < Mean - 2σ)",
            "",
        ])

        if self.underpowered:
            lines.append("| Alien | Win Rate |")
            lines.append("|-------|----------|")
            for name, rate in self.underpowered[:10]:
                lines.append(f"| {name} | {rate:.1f}% |")
        else:
            lines.append("*None identified*")

        return "\n".join(lines)


@dataclass
class GameLengthReport:
    """Report on game length statistics."""
    average_turns: float
    median_turns: float
    min_turns: int
    max_turns: int
    percentile_25: float
    percentile_75: float
    percentile_90: float

    def to_markdown(self) -> str:
        """Generate markdown report."""
        return f"""## Game Length Statistics

**Average Game Length:** {self.average_turns:.1f} turns
**Median Game Length:** {self.median_turns:.1f} turns
**Shortest Game:** {self.min_turns} turns
**Longest Game:** {self.max_turns} turns
**25th Percentile:** {self.percentile_25:.1f} turns
**75th Percentile:** {self.percentile_75:.1f} turns
**90th Percentile:** {self.percentile_90:.1f} turns
"""


@dataclass
class EloDistributionReport:
    """Report on ELO rating distribution."""
    average_elo: float
    median_elo: float
    std_dev: float
    min_elo: float
    max_elo: float
    elo_tiers: Dict[str, int]  # tier name -> count

    def to_markdown(self) -> str:
        """Generate markdown report."""
        lines = [
            "## ELO Distribution",
            "",
            f"**Average ELO:** {self.average_elo:.0f}",
            f"**Median ELO:** {self.median_elo:.0f}",
            f"**Standard Deviation:** {self.std_dev:.0f}",
            f"**Range:** {self.min_elo:.0f} - {self.max_elo:.0f}",
            "",
            "### Distribution by Tier",
            "",
            "| Tier | ELO Range | Count |",
            "|------|-----------|-------|",
        ]

        tier_order = ["S", "A", "B", "C", "D", "F"]
        for tier in tier_order:
            if tier in self.elo_tiers:
                count = self.elo_tiers[tier]
                ranges = {
                    "S": "1700+",
                    "A": "1600-1699",
                    "B": "1500-1599",
                    "C": "1400-1499",
                    "D": "1300-1399",
                    "F": "<1300"
                }
                lines.append(f"| {tier} | {ranges.get(tier, 'N/A')} | {count} |")

        return "\n".join(lines)


class SimulationAnalyzer:
    """
    Analyzes cumulative simulation statistics.

    Provides various reports and insights from the accumulated game data.
    """

    def __init__(self, stats: CumulativeStats):
        self.stats = stats

    def get_power_balance_report(
        self,
        min_games: int = 100
    ) -> PowerBalanceReport:
        """
        Analyze power balance across all aliens.

        Args:
            min_games: Minimum games played to include in analysis

        Returns:
            PowerBalanceReport with balance insights
        """
        # Filter aliens with enough games
        eligible = [
            s for s in self.stats.alien_stats.values()
            if s.games_played >= min_games
        ]

        if len(eligible) < 5:
            return PowerBalanceReport(
                overpowered=[],
                underpowered=[],
                balanced=[],
                average_win_rate=0.0,
                median_win_rate=0.0,
                standard_deviation=0.0,
                win_rate_range=(0.0, 0.0)
            )

        win_rates = [s.win_rate_percent for s in eligible]

        avg = statistics.mean(win_rates)
        median = statistics.median(win_rates)
        std_dev = statistics.stdev(win_rates) if len(win_rates) > 1 else 0.0
        min_rate = min(win_rates)
        max_rate = max(win_rates)

        # Identify outliers (2 standard deviations from mean)
        high_threshold = avg + (2 * std_dev)
        low_threshold = avg - (2 * std_dev)

        overpowered = [
            (s.name, s.win_rate_percent)
            for s in eligible
            if s.win_rate_percent > high_threshold
        ]
        overpowered.sort(key=lambda x: x[1], reverse=True)

        underpowered = [
            (s.name, s.win_rate_percent)
            for s in eligible
            if s.win_rate_percent < low_threshold
        ]
        underpowered.sort(key=lambda x: x[1])

        balanced = [
            s.name
            for s in eligible
            if low_threshold <= s.win_rate_percent <= high_threshold
        ]

        return PowerBalanceReport(
            overpowered=overpowered,
            underpowered=underpowered,
            balanced=balanced,
            average_win_rate=avg,
            median_win_rate=median,
            standard_deviation=std_dev,
            win_rate_range=(min_rate, max_rate)
        )

    def get_game_length_report(self) -> GameLengthReport:
        """
        Analyze game length statistics.

        Note: This uses average data since we don't store individual game lengths.
        """
        avg = self.stats.avg_game_length
        min_len = self.stats.min_game_length if self.stats.min_game_length < 999999 else 0
        max_len = self.stats.max_game_length

        return GameLengthReport(
            average_turns=avg,
            median_turns=avg,  # Approximate with average
            min_turns=min_len,
            max_turns=max_len,
            percentile_25=avg * 0.7,  # Estimate
            percentile_75=avg * 1.3,
            percentile_90=avg * 1.5
        )

    def get_elo_distribution_report(
        self,
        min_games: int = 50
    ) -> EloDistributionReport:
        """
        Analyze ELO rating distribution.

        Args:
            min_games: Minimum games to include alien in analysis
        """
        eligible = [
            s for s in self.stats.alien_stats.values()
            if s.games_played >= min_games
        ]

        if not eligible:
            return EloDistributionReport(
                average_elo=1500.0,
                median_elo=1500.0,
                std_dev=0.0,
                min_elo=1500.0,
                max_elo=1500.0,
                elo_tiers={}
            )

        elos = [s.elo_rating for s in eligible]

        # Calculate tier distribution
        tiers = {"S": 0, "A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for elo in elos:
            if elo >= 1700:
                tiers["S"] += 1
            elif elo >= 1600:
                tiers["A"] += 1
            elif elo >= 1500:
                tiers["B"] += 1
            elif elo >= 1400:
                tiers["C"] += 1
            elif elo >= 1300:
                tiers["D"] += 1
            else:
                tiers["F"] += 1

        return EloDistributionReport(
            average_elo=statistics.mean(elos),
            median_elo=statistics.median(elos),
            std_dev=statistics.stdev(elos) if len(elos) > 1 else 0.0,
            min_elo=min(elos),
            max_elo=max(elos),
            elo_tiers=tiers
        )

    def get_top_aliens(
        self,
        by: str = "elo",
        n: int = 20,
        min_games: int = 100
    ) -> List[AlienEloStats]:
        """
        Get top N aliens by a specified metric.

        Args:
            by: "elo", "win_rate", or "games_played"
            n: Number of aliens to return
            min_games: Minimum games played to include
        """
        eligible = [
            s for s in self.stats.alien_stats.values()
            if s.games_played >= min_games
        ]

        if by == "elo":
            eligible.sort(key=lambda s: s.elo_rating, reverse=True)
        elif by == "win_rate":
            eligible.sort(key=lambda s: s.win_rate, reverse=True)
        elif by == "games_played":
            eligible.sort(key=lambda s: s.games_played, reverse=True)

        return eligible[:n]

    def get_bottom_aliens(
        self,
        by: str = "elo",
        n: int = 20,
        min_games: int = 100
    ) -> List[AlienEloStats]:
        """
        Get bottom N aliens by a specified metric.

        Args:
            by: "elo", "win_rate"
            n: Number of aliens to return
            min_games: Minimum games played to include
        """
        eligible = [
            s for s in self.stats.alien_stats.values()
            if s.games_played >= min_games
        ]

        if by == "elo":
            eligible.sort(key=lambda s: s.elo_rating)
        elif by == "win_rate":
            eligible.sort(key=lambda s: s.win_rate)

        return eligible[:n]

    def find_alien_stats(self, name: str) -> Optional[AlienEloStats]:
        """Get stats for a specific alien."""
        return self.stats.alien_stats.get(name)

    def compare_aliens(
        self,
        alien1: str,
        alien2: str
    ) -> Dict[str, Any]:
        """
        Compare two aliens head to head.

        Returns dict with comparison metrics.
        """
        stats1 = self.find_alien_stats(alien1)
        stats2 = self.find_alien_stats(alien2)

        if not stats1 or not stats2:
            return {"error": "One or both aliens not found"}

        return {
            "alien1": {
                "name": alien1,
                "elo": stats1.elo_rating,
                "win_rate": stats1.win_rate_percent,
                "games": stats1.games_played
            },
            "alien2": {
                "name": alien2,
                "elo": stats2.elo_rating,
                "win_rate": stats2.win_rate_percent,
                "games": stats2.games_played
            },
            "elo_difference": stats1.elo_rating - stats2.elo_rating,
            "win_rate_difference": stats1.win_rate_percent - stats2.win_rate_percent,
            "expected_win_rate": self._calculate_expected_win_rate(
                stats1.elo_rating, stats2.elo_rating
            )
        }

    def _calculate_expected_win_rate(
        self,
        elo1: float,
        elo2: float
    ) -> float:
        """Calculate expected win rate for player 1 against player 2."""
        exponent = (elo2 - elo1) / 400
        return 1.0 / (1.0 + 10 ** exponent)

    def generate_full_report(self, min_games: int = 100) -> str:
        """Generate a comprehensive markdown report."""
        lines = [
            "# Cosmic Encounter Simulation Analysis Report",
            "",
            f"**Total Games Simulated:** {self.stats.total_games:,}",
            f"**Unique Aliens Tracked:** {len(self.stats.alien_stats)}",
            f"**Last Updated:** {self.stats.last_updated[:19] if self.stats.last_updated else 'Never'}",
            "",
        ]

        # Game length
        game_report = self.get_game_length_report()
        lines.append(game_report.to_markdown())
        lines.append("")

        # Victory distribution
        total_victories = self.stats.solo_victories + self.stats.shared_victories
        if total_victories > 0:
            solo_pct = self.stats.solo_victories / total_victories * 100
            shared_pct = self.stats.shared_victories / total_victories * 100
            lines.extend([
                "## Victory Distribution",
                "",
                f"**Solo Victories:** {self.stats.solo_victories:,} ({solo_pct:.1f}%)",
                f"**Shared Victories:** {self.stats.shared_victories:,} ({shared_pct:.1f}%)",
                "",
            ])

        # ELO distribution
        elo_report = self.get_elo_distribution_report(min_games)
        lines.append(elo_report.to_markdown())
        lines.append("")

        # Power balance
        balance_report = self.get_power_balance_report(min_games)
        lines.append(balance_report.to_markdown())
        lines.append("")

        # Top aliens
        top = self.get_top_aliens("elo", 15, min_games)
        if top:
            lines.extend([
                "## Top 15 Aliens by ELO",
                "",
                "| Rank | Alien | ELO | Win Rate | Games |",
                "|------|-------|-----|----------|-------|",
            ])
            for i, s in enumerate(top, 1):
                lines.append(f"| {i} | {s.name} | {s.elo_rating:.0f} | {s.win_rate_percent:.1f}% | {s.games_played} |")
            lines.append("")

        # Bottom aliens
        bottom = self.get_bottom_aliens("elo", 10, min_games)
        if bottom:
            lines.extend([
                "## Bottom 10 Aliens by ELO",
                "",
                "| Rank | Alien | ELO | Win Rate | Games |",
                "|------|-------|-----|----------|-------|",
            ])
            for i, s in enumerate(bottom, 1):
                lines.append(f"| {i} | {s.name} | {s.elo_rating:.0f} | {s.win_rate_percent:.1f}% | {s.games_played} |")
            lines.append("")

        return "\n".join(lines)

    def export_to_json(self, filepath: str) -> None:
        """Export analysis data to JSON for external tools."""
        data = {
            "summary": {
                "total_games": self.stats.total_games,
                "unique_aliens": len(self.stats.alien_stats),
                "avg_game_length": self.stats.avg_game_length,
                "solo_victories": self.stats.solo_victories,
                "shared_victories": self.stats.shared_victories,
            },
            "aliens": [
                {
                    "name": s.name,
                    "elo": s.elo_rating,
                    "win_rate": s.win_rate,
                    "games_played": s.games_played,
                    "solo_wins": s.solo_wins,
                    "shared_wins": s.shared_wins,
                    "avg_colonies": s.avg_colonies,
                }
                for s in self.stats.alien_stats.values()
            ]
        }

        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)


def analyze_stats_file(
    filepath: str = "cumulative_stats.json",
    min_games: int = 100
) -> SimulationAnalyzer:
    """
    Load stats from file and create analyzer.

    Args:
        filepath: Path to cumulative stats JSON file
        min_games: Minimum games for aliens to be included in analysis

    Returns:
        SimulationAnalyzer instance
    """
    stats = CumulativeStats.load(filepath)
    return SimulationAnalyzer(stats)
