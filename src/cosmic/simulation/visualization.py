"""
Visualization and Reporting Tools for Cosmic Encounter Simulator.

Provides text-based visualization and reporting capabilities:
- Game summary reports
- Alien performance charts
- Win rate distributions
- Tier breakdowns
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple
from collections import defaultdict
import math

from .cumulative_stats import CumulativeStats, AlienEloStats
from .power_analysis import PowerBalanceAnalyzer, PowerTier


@dataclass
class PerformanceChart:
    """ASCII bar chart for performance visualization."""

    @staticmethod
    def horizontal_bar(
        data: List[Tuple[str, float]],
        title: str = "",
        max_bar_width: int = 40,
        show_values: bool = True,
        value_format: str = "{:.1f}%"
    ) -> str:
        """
        Generate a horizontal bar chart.

        Args:
            data: List of (label, value) tuples
            title: Chart title
            max_bar_width: Maximum width of bars in characters
            show_values: Whether to show numeric values
            value_format: Format string for values
        """
        if not data:
            return "No data to display"

        lines = []

        if title:
            lines.append(title)
            lines.append("=" * len(title))
            lines.append("")

        # Find max value for scaling
        max_val = max(v for _, v in data) if data else 1
        min_val = min(v for _, v in data) if data else 0

        # Find max label length
        max_label = max(len(label) for label, _ in data) if data else 10

        for label, value in data:
            # Calculate bar length
            if max_val != min_val:
                bar_len = int((value - min_val) / (max_val - min_val) * max_bar_width)
            else:
                bar_len = max_bar_width // 2

            bar = "█" * bar_len

            # Format value
            val_str = value_format.format(value) if show_values else ""

            lines.append(f"{label:<{max_label}} | {bar} {val_str}")

        return "\n".join(lines)

    @staticmethod
    def distribution_histogram(
        values: List[float],
        title: str = "",
        bins: int = 10,
        width: int = 50
    ) -> str:
        """
        Generate a vertical histogram of value distribution.

        Args:
            values: List of numeric values
            title: Chart title
            bins: Number of bins
            width: Chart width
        """
        if not values:
            return "No data to display"

        lines = []

        if title:
            lines.append(title)
            lines.append("=" * len(title))
            lines.append("")

        # Calculate bin edges
        min_val = min(values)
        max_val = max(values)
        bin_width = (max_val - min_val) / bins if max_val != min_val else 1

        # Count values in each bin
        counts = [0] * bins
        for v in values:
            bin_idx = min(int((v - min_val) / bin_width), bins - 1)
            counts[bin_idx] += 1

        # Normalize counts
        max_count = max(counts) if counts else 1

        # Build histogram
        for i, count in enumerate(counts):
            bin_start = min_val + i * bin_width
            bin_end = bin_start + bin_width
            bar_len = int(count / max_count * width) if max_count > 0 else 0
            bar = "█" * bar_len

            lines.append(f"{bin_start:6.2f}-{bin_end:6.2f} | {bar} ({count})")

        return "\n".join(lines)


class GameAnalysisReport:
    """
    Generates comprehensive analysis reports for simulation results.
    """

    def __init__(self, stats: CumulativeStats):
        self.stats = stats
        self.analyzer = PowerBalanceAnalyzer(min_games=50)

    def generate_summary(self) -> str:
        """Generate a summary of simulation statistics."""
        lines = [
            "╔═══════════════════════════════════════════════════════════════════╗",
            "║           COSMIC ENCOUNTER SIMULATION SUMMARY                     ║",
            "╚═══════════════════════════════════════════════════════════════════╝",
            "",
            f"  Total Games Simulated: {self.stats.total_games:,}",
            f"  Unique Powers Tracked: {len(self.stats.alien_stats)}",
            "",
            "  Games by Player Count:",
        ]

        for players, count in sorted(self.stats.games_by_player_count.items()):
            pct = count / self.stats.total_games * 100 if self.stats.total_games else 0
            lines.append(f"    {players} players: {count:,} ({pct:.1f}%)")

        lines.append("")

        return "\n".join(lines)

    def generate_tier_breakdown(self) -> str:
        """Generate tier distribution breakdown."""
        report = self.analyzer.analyze(self.stats)

        lines = [
            "POWER TIER DISTRIBUTION",
            "─" * 50,
            "",
        ]

        tier_symbols = {
            PowerTier.S: "🟣 S-Tier (Elite)",
            PowerTier.A: "🔵 A-Tier (Strong)",
            PowerTier.B: "🟢 B-Tier (Good)",
            PowerTier.C: "🟡 C-Tier (Average)",
            PowerTier.D: "🔴 D-Tier (Below Avg)",
            PowerTier.F: "⚫ F-Tier (Weak)",
        }

        for tier in PowerTier:
            count = report.tier_counts.get(tier, 0)
            total = len(report.analyses)
            pct = count / total * 100 if total else 0

            bar_len = int(pct / 2)
            bar = "█" * bar_len

            lines.append(f"  {tier_symbols[tier]}")
            lines.append(f"    {bar} {count} powers ({pct:.1f}%)")
            lines.append("")

        return "\n".join(lines)

    def generate_top_performers(self, n: int = 20) -> str:
        """Generate top N performers report."""
        lines = [
            f"TOP {n} ALIEN POWERS",
            "─" * 60,
            "",
            f"{'Rank':>4} {'Power':<20} {'Win%':>8} {'ELO':>8} {'Games':>10}",
            "─" * 60,
        ]

        # Sort by win rate
        sorted_aliens = sorted(
            self.stats.alien_stats.values(),
            key=lambda x: x.win_rate,
            reverse=True
        )

        for i, alien in enumerate(sorted_aliens[:n], 1):
            wr = alien.win_rate * 100
            lines.append(
                f"{i:>4} {alien.name:<20} {wr:>7.1f}% {alien.elo_rating:>8.0f} {alien.games_played:>10,}"
            )

        return "\n".join(lines)

    def generate_bottom_performers(self, n: int = 10) -> str:
        """Generate bottom N performers report."""
        lines = [
            f"BOTTOM {n} ALIEN POWERS",
            "─" * 60,
            "",
            f"{'Rank':>4} {'Power':<20} {'Win%':>8} {'ELO':>8} {'Games':>10}",
            "─" * 60,
        ]

        # Sort by win rate ascending
        sorted_aliens = sorted(
            [a for a in self.stats.alien_stats.values() if a.games_played >= 50],
            key=lambda x: x.win_rate
        )

        for i, alien in enumerate(sorted_aliens[:n], 1):
            wr = alien.win_rate * 100
            lines.append(
                f"{i:>4} {alien.name:<20} {wr:>7.1f}% {alien.elo_rating:>8.0f} {alien.games_played:>10,}"
            )

        return "\n".join(lines)

    def generate_win_rate_distribution(self) -> str:
        """Generate win rate distribution chart."""
        win_rates = [
            a.win_rate * 100
            for a in self.stats.alien_stats.values()
            if a.games_played >= 50
        ]

        return PerformanceChart.distribution_histogram(
            win_rates,
            title="WIN RATE DISTRIBUTION (%)",
            bins=10,
            width=40
        )

    def generate_elo_distribution(self) -> str:
        """Generate ELO rating distribution chart."""
        elos = [
            a.elo_rating
            for a in self.stats.alien_stats.values()
            if a.games_played >= 50
        ]

        return PerformanceChart.distribution_histogram(
            elos,
            title="ELO RATING DISTRIBUTION",
            bins=10,
            width=40
        )

    def generate_full_report(self) -> str:
        """Generate complete analysis report."""
        sections = [
            self.generate_summary(),
            self.generate_tier_breakdown(),
            self.generate_top_performers(20),
            "",
            self.generate_bottom_performers(10),
            "",
            self.generate_win_rate_distribution(),
            "",
            self.generate_elo_distribution(),
        ]

        return "\n".join(sections)


class PowerComparisonReport:
    """
    Generate comparison reports between specific alien powers.
    """

    def __init__(self, stats: CumulativeStats):
        self.stats = stats

    def compare_powers(self, *power_names: str) -> str:
        """
        Generate a side-by-side comparison of specified powers.

        Args:
            *power_names: Names of powers to compare
        """
        lines = [
            "POWER COMPARISON",
            "═" * 70,
            "",
        ]

        # Get stats for each power
        powers = []
        for name in power_names:
            if name in self.stats.alien_stats:
                powers.append(self.stats.alien_stats[name])
            else:
                lines.append(f"  Warning: '{name}' not found in stats")

        if not powers:
            return "\n".join(lines + ["  No valid powers to compare"])

        # Header
        header = f"{'Metric':<20}"
        for p in powers:
            header += f" {p.name:>15}"
        lines.append(header)
        lines.append("─" * 70)

        # Games played
        row = f"{'Games Played':<20}"
        for p in powers:
            row += f" {p.games_played:>15,}"
        lines.append(row)

        # Win rate
        row = f"{'Win Rate':<20}"
        for p in powers:
            row += f" {p.win_rate * 100:>14.1f}%"
        lines.append(row)

        # Solo win rate
        row = f"{'Solo Win Rate':<20}"
        for p in powers:
            row += f" {p.solo_win_rate * 100:>14.1f}%"
        lines.append(row)

        # ELO rating
        row = f"{'ELO Rating':<20}"
        for p in powers:
            row += f" {p.elo_rating:>15.0f}"
        lines.append(row)

        lines.append("")

        # Winner declaration
        if len(powers) >= 2:
            best = max(powers, key=lambda p: p.win_rate)
            lines.append(f"  🏆 Best performer: {best.name} ({best.win_rate * 100:.1f}% win rate)")

        return "\n".join(lines)

    def generate_matchup_report(
        self,
        power_a: str,
        power_b: str
    ) -> str:
        """Generate detailed matchup report between two powers."""
        lines = [
            f"MATCHUP: {power_a} vs {power_b}",
            "═" * 50,
            "",
        ]

        a_stats = self.stats.alien_stats.get(power_a)
        b_stats = self.stats.alien_stats.get(power_b)

        if not a_stats:
            lines.append(f"  '{power_a}' not found in stats")
        if not b_stats:
            lines.append(f"  '{power_b}' not found in stats")

        if a_stats and b_stats:
            lines.extend([
                f"  {power_a:20} | {power_b:20}",
                "─" * 50,
                f"  Win Rate:   {a_stats.win_rate * 100:5.1f}%     | {b_stats.win_rate * 100:5.1f}%",
                f"  ELO:        {a_stats.elo_rating:5.0f}       | {b_stats.elo_rating:5.0f}",
                f"  Games:      {a_stats.games_played:5}       | {b_stats.games_played:5}",
                "",
            ])

            # Predict winner
            elo_diff = a_stats.elo_rating - b_stats.elo_rating
            win_prob = 1 / (1 + 10 ** (-elo_diff / 400))

            if elo_diff > 0:
                lines.append(f"  📊 {power_a} favored: {win_prob * 100:.1f}% expected win rate")
            else:
                lines.append(f"  📊 {power_b} favored: {(1 - win_prob) * 100:.1f}% expected win rate")

        return "\n".join(lines)


def generate_quick_report(stats_file: str = "cumulative_stats.json") -> str:
    """
    Quick function to generate a full analysis report.

    Args:
        stats_file: Path to cumulative stats JSON file

    Returns:
        Complete analysis report as string
    """
    from pathlib import Path

    stats = CumulativeStats.load(Path(stats_file))
    report_gen = GameAnalysisReport(stats)
    return report_gen.generate_full_report()


def compare_aliens(*alien_names: str, stats_file: str = "cumulative_stats.json") -> str:
    """
    Quick function to compare specific aliens.

    Args:
        *alien_names: Names of aliens to compare
        stats_file: Path to stats file

    Returns:
        Comparison report as string
    """
    from pathlib import Path

    stats = CumulativeStats.load(Path(stats_file))
    comparison = PowerComparisonReport(stats)
    return comparison.compare_powers(*alien_names)


if __name__ == "__main__":
    print(generate_quick_report())
