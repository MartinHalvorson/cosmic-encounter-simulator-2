"""
Statistics collection and analysis for Cosmic Encounter simulations.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple, Any
import json
import csv
import math
from io import StringIO


def wilson_score_interval(wins: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    """
    Calculate Wilson score interval for a proportion.

    This is more accurate than normal approximation for proportions,
    especially with small sample sizes or extreme proportions.

    Args:
        wins: Number of successes
        n: Total trials
        z: Z-score for confidence level (1.96 = 95%, 2.58 = 99%)

    Returns:
        Tuple of (lower_bound, upper_bound) for the confidence interval
    """
    if n == 0:
        return (0.0, 0.0)

    p = wins / n
    denominator = 1 + z * z / n

    centre_adjusted_probability = p + z * z / (2 * n)
    adjusted_standard_deviation = math.sqrt((p * (1 - p) + z * z / (4 * n)) / n)

    lower = (centre_adjusted_probability - z * adjusted_standard_deviation) / denominator
    upper = (centre_adjusted_probability + z * adjusted_standard_deviation) / denominator

    return (max(0.0, lower), min(1.0, upper))


def standard_error(p: float, n: int) -> float:
    """Calculate standard error for a proportion."""
    if n == 0:
        return 0.0
    return math.sqrt(p * (1 - p) / n)


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
    # Power activation tracking
    total_power_activations: int = 0
    total_encounters_as_main: int = 0  # Opportunities to use power
    # Encounter statistics
    encounters_as_offense: int = 0
    encounters_as_defense: int = 0
    encounters_won_as_offense: int = 0
    encounters_won_as_defense: int = 0
    encounters_with_deal: int = 0  # Times a deal was made
    encounters_with_allies: int = 0  # Times allies joined

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

    @property
    def power_activation_rate(self) -> float:
        """Rate of power activations per encounter as main player."""
        if self.total_encounters_as_main == 0:
            return 0.0
        return self.total_power_activations / self.total_encounters_as_main

    @property
    def avg_activations_per_game(self) -> float:
        """Average number of power activations per game."""
        if self.games_played == 0:
            return 0.0
        return self.total_power_activations / self.games_played

    @property
    def offense_encounter_win_rate(self) -> float:
        """Win rate when playing as offense."""
        if self.encounters_as_offense == 0:
            return 0.0
        return self.encounters_won_as_offense / self.encounters_as_offense

    @property
    def defense_encounter_win_rate(self) -> float:
        """Win rate when playing as defense."""
        if self.encounters_as_defense == 0:
            return 0.0
        return self.encounters_won_as_defense / self.encounters_as_defense

    @property
    def deal_rate(self) -> float:
        """Rate of deals made (as percentage of encounters as main player)."""
        total_encounters = self.encounters_as_offense + self.encounters_as_defense
        if total_encounters == 0:
            return 0.0
        return self.encounters_with_deal / total_encounters

    def confidence_interval(self, confidence: float = 0.95) -> Tuple[float, float]:
        """
        Calculate confidence interval for win rate using Wilson score interval.

        Args:
            confidence: Confidence level (0.95 = 95%)

        Returns:
            Tuple of (lower_bound, upper_bound) as proportions (0-1)
        """
        # Map confidence level to z-score
        z_scores = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}
        z = z_scores.get(confidence, 1.96)
        return wilson_score_interval(self.games_won, self.games_played, z)

    def margin_of_error(self) -> float:
        """Calculate margin of error for 95% confidence interval."""
        ci = self.confidence_interval()
        return (ci[1] - ci[0]) / 2

    def is_significantly_different(
        self,
        expected_rate: float,
        confidence: float = 0.95
    ) -> Tuple[bool, str]:
        """
        Test if win rate is significantly different from expected.

        Args:
            expected_rate: Expected win rate (e.g., 0.2 for 5 players)
            confidence: Confidence level for the test

        Returns:
            Tuple of (is_significant, direction) where direction is
            "above", "below", or "neutral"
        """
        ci = self.confidence_interval(confidence)

        if expected_rate < ci[0]:
            return (True, "above")
        elif expected_rate > ci[1]:
            return (True, "below")
        else:
            return (False, "neutral")

    def power_rating(self, expected_rate: float) -> float:
        """
        Calculate a power rating relative to expected win rate.

        Rating > 1.0 means alien wins more than expected
        Rating < 1.0 means alien wins less than expected
        Rating = 1.0 means alien wins at expected rate

        Args:
            expected_rate: Expected win rate (e.g., 0.2 for 5 players)

        Returns:
            Power rating as a multiplier
        """
        if expected_rate == 0 or self.games_played == 0:
            return 1.0
        return self.win_rate / expected_rate

    def to_dict(self, expected_rate: float = 0.2) -> Dict[str, Any]:
        """Convert to dictionary with statistical info.

        Args:
            expected_rate: Expected win rate for comparison (default 0.2 for 5 players)
        """
        ci = self.confidence_interval()
        is_sig, direction = self.is_significantly_different(expected_rate)

        return {
            "name": self.name,
            "games_played": self.games_played,
            "games_won": self.games_won,
            "win_rate": round(self.win_rate * 100, 2),
            "win_rate_ci_lower": round(ci[0] * 100, 2),
            "win_rate_ci_upper": round(ci[1] * 100, 2),
            "margin_of_error": round(self.margin_of_error() * 100, 2),
            "power_rating": round(self.power_rating(expected_rate), 3),
            "significantly_different": is_sig,
            "direction": direction,
            "solo_wins": self.solo_wins,
            "shared_wins": self.shared_wins,
            "alternate_wins": self.alternate_wins,
            "avg_colonies": round(self.avg_colonies, 2),
            "total_power_activations": self.total_power_activations,
            "avg_activations_per_game": round(self.avg_activations_per_game, 2),
            "power_activation_rate": round(self.power_activation_rate * 100, 1),
            # Encounter statistics
            "encounters_as_offense": self.encounters_as_offense,
            "encounters_as_defense": self.encounters_as_defense,
            "offense_win_rate": round(self.offense_encounter_win_rate * 100, 1),
            "defense_win_rate": round(self.defense_encounter_win_rate * 100, 1),
            "deal_rate": round(self.deal_rate * 100, 1),
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

    def preallocate_aliens(self, alien_names: List[str]) -> None:
        """
        Pre-allocate AlienStats for a list of alien names.

        This avoids dictionary lookup + conditional allocation on every game,
        improving performance when running many simulations.

        Args:
            alien_names: List of alien names to pre-allocate stats for
        """
        for name in alien_names:
            if name not in self.alien_stats:
                self.alien_stats[name] = AlienStats(name=name)

    def record_game(
        self,
        num_players: int,
        winners: List[str],
        alien_map: Dict[str, str],
        turn_count: int,
        final_colonies: Dict[str, int],
        alternate_win: bool = False,
        timed_out: bool = False,
        errored: bool = False,
        power_activations: Optional[Dict[str, int]] = None,
        encounters_as_main: Optional[Dict[str, int]] = None,
        encounter_stats: Optional[Dict[str, Dict[str, int]]] = None
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
            power_activations: Mapping of player name to power activation count
            encounters_as_main: Mapping of player name to encounters as main player
            encounter_stats: Per-player encounter statistics (offense/defense/wins/deals)
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

            # Track power activations if provided
            if power_activations and player_name in power_activations:
                stats.total_power_activations += power_activations[player_name]
            if encounters_as_main and player_name in encounters_as_main:
                stats.total_encounters_as_main += encounters_as_main[player_name]

            # Track encounter statistics if provided
            if encounter_stats and player_name in encounter_stats:
                player_enc = encounter_stats[player_name]
                stats.encounters_as_offense += player_enc.get("as_offense", 0)
                stats.encounters_as_defense += player_enc.get("as_defense", 0)
                stats.encounters_won_as_offense += player_enc.get("won_as_offense", 0)
                stats.encounters_won_as_defense += player_enc.get("won_as_defense", 0)
                stats.encounters_with_deal += player_enc.get("deals", 0)
                stats.encounters_with_allies += player_enc.get("with_allies", 0)

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

    @property
    def most_common_player_count(self) -> int:
        """Get the most common number of players across all games."""
        if not self.games_by_player_count:
            return 5  # Default
        return max(self.games_by_player_count, key=self.games_by_player_count.get)

    @property
    def expected_win_rate(self) -> float:
        """Get expected win rate based on most common player count."""
        return 1.0 / self.most_common_player_count

    def get_significantly_strong(self, min_games: int = 100) -> List[AlienStats]:
        """Get aliens that are statistically significantly stronger than expected."""
        expected = self.expected_win_rate
        return [
            stats for stats in self.alien_stats.values()
            if stats.games_played >= min_games and
               stats.is_significantly_different(expected)[0] and
               stats.is_significantly_different(expected)[1] == "above"
        ]

    def get_significantly_weak(self, min_games: int = 100) -> List[AlienStats]:
        """Get aliens that are statistically significantly weaker than expected."""
        expected = self.expected_win_rate
        return [
            stats for stats in self.alien_stats.values()
            if stats.games_played >= min_games and
               stats.is_significantly_different(expected)[0] and
               stats.is_significantly_different(expected)[1] == "below"
        ]

    def get_balanced(self, min_games: int = 100) -> List[AlienStats]:
        """Get aliens whose win rate is not significantly different from expected."""
        expected = self.expected_win_rate
        return [
            stats for stats in self.alien_stats.values()
            if stats.games_played >= min_games and
               not stats.is_significantly_different(expected)[0]
        ]

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

    def summary(self, show_significance: bool = True) -> str:
        """Generate a text summary of statistics with statistical significance.

        Args:
            show_significance: Whether to show statistical significance indicators
        """
        expected = self.expected_win_rate
        player_count = self.most_common_player_count

        lines = [
            "=" * 70,
            "COSMIC ENCOUNTER SIMULATION RESULTS",
            "=" * 70,
            "",
            f"Total Games: {self.total_games:,}",
            f"Most Common Player Count: {player_count} (expected win rate: {expected*100:.1f}%)",
            f"Solo Victories: {self.solo_victory_count:,}",
            f"Shared Victories: {self.shared_victory_count:,}",
            f"Timeouts: {self.timeout_count:,}",
            f"Errors: {self.error_count:,}",
            "",
            f"Average Game Length: {self.avg_game_length:.1f} turns",
            f"Shortest Game: {self.min_game_length} turns",
            f"Longest Game: {self.max_game_length} turns",
            "",
        ]

        if show_significance and self.total_games >= 100:
            strong = self.get_significantly_strong()
            weak = self.get_significantly_weak()
            balanced = self.get_balanced()

            lines.extend([
                "-" * 70,
                "STATISTICAL SIGNIFICANCE (95% confidence)",
                "-" * 70,
                f"Significantly STRONGER than expected: {len(strong)} aliens",
                f"Significantly WEAKER than expected: {len(weak)} aliens",
                f"Balanced (not significantly different): {len(balanced)} aliens",
                "",
            ])

        lines.extend([
            "-" * 70,
            "ALIEN POWER WIN RATES (with 95% CI)",
            "-" * 70,
        ])

        if show_significance:
            lines.append(
                f"{'Rank':>4} {'Alien':20} {'Win%':>6} {'95% CI':^15} {'Rating':>6} {'Sig':>4}"
            )
            lines.append("-" * 70)

        # Rank by win rate
        rankings = self.get_rankings("win_rate")
        for i, stats in enumerate(rankings, 1):
            if show_significance and stats.games_played >= 30:
                ci = stats.confidence_interval()
                is_sig, direction = stats.is_significantly_different(expected)
                rating = stats.power_rating(expected)

                # Significance indicator
                if is_sig:
                    sig = "+" if direction == "above" else "-"
                else:
                    sig = "="

                lines.append(
                    f"{i:3}. {stats.name:20} {stats.win_rate*100:5.1f}% "
                    f"[{ci[0]*100:4.1f}-{ci[1]*100:4.1f}%] "
                    f"{rating:5.2f}x {sig:>3}"
                )
            else:
                lines.append(
                    f"{i:3}. {stats.name:20} {stats.win_rate*100:5.1f}% "
                    f"({stats.games_won}/{stats.games_played})"
                )

        lines.append("")
        lines.append("Legend: + = significantly above expected, - = below, = = balanced")
        lines.append("=" * 70)

        return "\n".join(lines)

    def to_csv(self) -> str:
        """Export statistics to CSV format with statistical significance data."""
        output = StringIO()
        writer = csv.writer(output)
        expected = self.expected_win_rate

        # Header
        writer.writerow([
            "Alien", "Games Played", "Games Won", "Win Rate %",
            "CI Lower %", "CI Upper %", "Margin of Error %",
            "Power Rating", "Significantly Different", "Direction",
            "Solo Wins", "Shared Wins", "Alternate Wins", "Avg Colonies"
        ])

        # Data
        for stats in self.get_rankings("win_rate"):
            ci = stats.confidence_interval()
            is_sig, direction = stats.is_significantly_different(expected)
            writer.writerow([
                stats.name,
                stats.games_played,
                stats.games_won,
                round(stats.win_rate * 100, 2),
                round(ci[0] * 100, 2),
                round(ci[1] * 100, 2),
                round(stats.margin_of_error() * 100, 2),
                round(stats.power_rating(expected), 3),
                is_sig,
                direction,
                stats.solo_wins,
                stats.shared_wins,
                stats.alternate_wins,
                round(stats.avg_colonies, 2),
            ])

        return output.getvalue()

    def to_json(self) -> str:
        """Export statistics to JSON format with statistical significance data."""
        expected = self.expected_win_rate
        strong = self.get_significantly_strong()
        weak = self.get_significantly_weak()
        balanced = self.get_balanced()

        data = {
            "summary": {
                "total_games": self.total_games,
                "solo_victories": self.solo_victory_count,
                "shared_victories": self.shared_victory_count,
                "timeouts": self.timeout_count,
                "errors": self.error_count,
                "avg_game_length": round(self.avg_game_length, 2),
                "most_common_player_count": self.most_common_player_count,
                "expected_win_rate": round(expected * 100, 2),
            },
            "statistical_significance": {
                "significantly_strong_count": len(strong),
                "significantly_weak_count": len(weak),
                "balanced_count": len(balanced),
                "significantly_strong": [s.name for s in strong],
                "significantly_weak": [s.name for s in weak],
            },
            "alien_stats": [
                stats.to_dict(expected)
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
