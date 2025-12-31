"""
Tournament Mode for Cosmic Encounter Simulator.

Provides systematic, structured comparisons between alien powers through
various tournament formats:
- Round Robin: Every alien plays against every other
- Swiss: Efficient pairing based on performance
- Bracket: Elimination-style tournaments
- Monte Carlo: Statistical sampling for power estimation
"""

import random
import math
import json
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Any, Set
from collections import defaultdict
from pathlib import Path
from datetime import datetime

from ..game import Game
from ..types import GameConfig
from ..aliens import AlienRegistry


@dataclass
class TournamentAlien:
    """Tracks an alien's performance in a tournament."""
    name: str
    wins: int = 0
    losses: int = 0
    draws: int = 0
    games_played: int = 0
    points: float = 0.0
    opponents_faced: List[str] = field(default_factory=list)
    buchholz_score: float = 0.0  # Tie-breaker based on opponents' performance

    @property
    def win_rate(self) -> float:
        if self.games_played == 0:
            return 0.0
        return self.wins / self.games_played

    @property
    def game_points(self) -> float:
        """Standard tournament scoring: 1 for win, 0.5 for draw, 0 for loss."""
        return self.wins + (self.draws * 0.5)


@dataclass
class TournamentMatch:
    """A single match in the tournament."""
    round_num: int
    aliens: List[str]
    games_per_match: int
    results: Dict[str, int] = field(default_factory=dict)  # alien -> wins
    completed: bool = False


@dataclass
class TournamentRound:
    """A round of matches in the tournament."""
    round_num: int
    matches: List[TournamentMatch] = field(default_factory=list)
    completed: bool = False


@dataclass
class TournamentResults:
    """Complete results of a tournament."""
    format: str
    start_time: str
    end_time: str = ""
    aliens: Dict[str, TournamentAlien] = field(default_factory=dict)
    rounds: List[TournamentRound] = field(default_factory=list)
    total_games: int = 0

    def get_standings(self) -> List[TournamentAlien]:
        """Get aliens sorted by performance."""
        standings = list(self.aliens.values())
        # Sort by points, then wins, then win rate
        standings.sort(key=lambda a: (a.points, a.wins, a.win_rate), reverse=True)
        return standings

    def get_top_n(self, n: int) -> List[TournamentAlien]:
        """Get top N performers."""
        return self.get_standings()[:n]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "format": self.format,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "total_games": self.total_games,
            "standings": [
                {
                    "rank": i + 1,
                    "name": a.name,
                    "wins": a.wins,
                    "losses": a.losses,
                    "draws": a.draws,
                    "points": a.points,
                    "win_rate": round(a.win_rate * 100, 2),
                    "games": a.games_played
                }
                for i, a in enumerate(self.get_standings())
            ]
        }


class Tournament:
    """
    Base tournament class for running structured competitions.
    """

    def __init__(
        self,
        aliens: Optional[List[str]] = None,
        games_per_match: int = 50,
        player_count: int = 4,
        verbose: bool = True,
        seed: Optional[int] = None
    ):
        """
        Initialize tournament.

        Args:
            aliens: List of alien names to include (None = all aliens)
            games_per_match: Number of games per matchup
            player_count: Number of players per game
            verbose: Print progress
            seed: Random seed for reproducibility
        """
        self.games_per_match = games_per_match
        self.player_count = player_count
        self.verbose = verbose
        self.seed = seed
        self.rng = random.Random(seed)

        # Get aliens
        if aliens is None:
            self.aliens = [a.name for a in AlienRegistry.get_all()]
        else:
            # Validate aliens exist
            valid_aliens = []
            for name in aliens:
                if AlienRegistry.get(name):
                    valid_aliens.append(name)
                else:
                    if verbose:
                        print(f"Warning: Unknown alien '{name}', skipping")
            self.aliens = valid_aliens

        self.results = TournamentResults(
            format="base",
            start_time=datetime.now().isoformat()
        )

        # Initialize alien tracking
        for name in self.aliens:
            self.results.aliens[name] = TournamentAlien(name=name)

    def run_match(
        self,
        alien_a: str,
        alien_b: str,
        games: Optional[int] = None
    ) -> Tuple[int, int, int]:
        """
        Run a match between two aliens.

        Returns:
            Tuple of (a_wins, b_wins, draws)
        """
        games = games or self.games_per_match
        a_wins = 0
        b_wins = 0
        draws = 0

        for _ in range(games):
            config = GameConfig(
                num_players=self.player_count,
                required_aliens=[alien_a, alien_b],
                seed=self.rng.randint(0, 2**31) if self.seed else None
            )

            try:
                game = Game(config)
                game.setup()
                winners = game.play()

                winner_names = [p.alien.name for p in winners if p.alien]
                a_won = alien_a in winner_names
                b_won = alien_b in winner_names

                if a_won and b_won:
                    draws += 1
                elif a_won:
                    a_wins += 1
                elif b_won:
                    b_wins += 1
                # else: third party won, no points

            except Exception:
                continue

        self.results.total_games += games
        return a_wins, b_wins, draws

    def update_standings(
        self,
        alien_a: str,
        alien_b: str,
        a_wins: int,
        b_wins: int,
        draws: int
    ) -> None:
        """Update tournament standings after a match."""
        total = a_wins + b_wins + draws

        # Update alien A
        self.results.aliens[alien_a].wins += a_wins
        self.results.aliens[alien_a].losses += b_wins
        self.results.aliens[alien_a].draws += draws
        self.results.aliens[alien_a].games_played += total
        self.results.aliens[alien_a].points += a_wins + (draws * 0.5)
        self.results.aliens[alien_a].opponents_faced.append(alien_b)

        # Update alien B
        self.results.aliens[alien_b].wins += b_wins
        self.results.aliens[alien_b].losses += a_wins
        self.results.aliens[alien_b].draws += draws
        self.results.aliens[alien_b].games_played += total
        self.results.aliens[alien_b].points += b_wins + (draws * 0.5)
        self.results.aliens[alien_b].opponents_faced.append(alien_a)

    def calculate_buchholz(self) -> None:
        """Calculate Buchholz tie-breaker scores."""
        for alien in self.results.aliens.values():
            # Sum of opponents' points
            alien.buchholz_score = sum(
                self.results.aliens[opp].points
                for opp in alien.opponents_faced
                if opp in self.results.aliens
            )

    def _log(self, message: str) -> None:
        if self.verbose:
            print(message)


class RoundRobinTournament(Tournament):
    """
    Round Robin tournament where every alien plays every other alien.

    Good for comprehensive analysis but O(n²) complexity.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.results.format = "round_robin"

    def run(self) -> TournamentResults:
        """Run the round robin tournament."""
        n = len(self.aliens)
        total_matches = n * (n - 1) // 2
        match_num = 0

        self._log(f"Starting Round Robin Tournament with {n} aliens")
        self._log(f"Total matches: {total_matches}")
        self._log(f"Games per match: {self.games_per_match}")
        self._log(f"Total games: {total_matches * self.games_per_match}")
        self._log("")

        for i, alien_a in enumerate(self.aliens):
            for alien_b in self.aliens[i+1:]:
                match_num += 1

                if self.verbose and match_num % 100 == 0:
                    self._log(f"Match {match_num}/{total_matches}: {alien_a} vs {alien_b}")

                a_wins, b_wins, draws = self.run_match(alien_a, alien_b)
                self.update_standings(alien_a, alien_b, a_wins, b_wins, draws)

        self.calculate_buchholz()
        self.results.end_time = datetime.now().isoformat()

        self._log("")
        self._log("Tournament Complete!")
        self._log(f"Total games: {self.results.total_games}")

        return self.results


class SwissTournament(Tournament):
    """
    Swiss-style tournament with efficient pairing based on performance.

    More efficient than round robin while still providing good rankings.
    Number of rounds typically log2(n) for n participants.
    """

    def __init__(
        self,
        *args,
        num_rounds: Optional[int] = None,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.results.format = "swiss"

        # Default rounds: ceil(log2(n))
        if num_rounds is None:
            self.num_rounds = max(1, math.ceil(math.log2(len(self.aliens))))
        else:
            self.num_rounds = num_rounds

    def run(self) -> TournamentResults:
        """Run the Swiss tournament."""
        n = len(self.aliens)

        self._log(f"Starting Swiss Tournament with {n} aliens")
        self._log(f"Rounds: {self.num_rounds}")
        self._log(f"Games per match: {self.games_per_match}")
        self._log("")

        for round_num in range(1, self.num_rounds + 1):
            self._log(f"=== Round {round_num}/{self.num_rounds} ===")

            # Get pairings for this round
            pairings = self._get_swiss_pairings(round_num)

            round_obj = TournamentRound(round_num=round_num)

            for alien_a, alien_b in pairings:
                a_wins, b_wins, draws = self.run_match(alien_a, alien_b)
                self.update_standings(alien_a, alien_b, a_wins, b_wins, draws)

                match = TournamentMatch(
                    round_num=round_num,
                    aliens=[alien_a, alien_b],
                    games_per_match=self.games_per_match,
                    results={alien_a: a_wins, alien_b: b_wins},
                    completed=True
                )
                round_obj.matches.append(match)

            round_obj.completed = True
            self.results.rounds.append(round_obj)

            # Print round standings
            if self.verbose:
                standings = self.results.get_standings()[:5]
                self._log("Top 5 after this round:")
                for i, alien in enumerate(standings, 1):
                    self._log(f"  {i}. {alien.name}: {alien.points:.1f} pts ({alien.win_rate*100:.1f}%)")
                self._log("")

        self.calculate_buchholz()
        self.results.end_time = datetime.now().isoformat()

        return self.results

    def _get_swiss_pairings(self, round_num: int) -> List[Tuple[str, str]]:
        """Generate Swiss pairings for a round."""
        # Get current standings
        standings = self.results.get_standings()

        # Track which aliens have been paired
        paired = set()
        pairings = []

        # Group by points (Swiss style)
        point_groups = defaultdict(list)
        for alien in standings:
            point_groups[alien.points].append(alien.name)

        # Sort point groups
        sorted_points = sorted(point_groups.keys(), reverse=True)

        # Pair within point groups
        unpaired = []
        for points in sorted_points:
            group = point_groups[points] + unpaired
            unpaired = []

            # Shuffle to randomize within group
            self.rng.shuffle(group)

            while len(group) >= 2:
                alien_a = group.pop(0)

                # Find opponent who hasn't played this alien
                opponent_found = False
                for i, alien_b in enumerate(group):
                    a_data = self.results.aliens[alien_a]
                    if alien_b not in a_data.opponents_faced:
                        pairings.append((alien_a, alien_b))
                        group.pop(i)
                        opponent_found = True
                        break

                if not opponent_found and group:
                    # Fallback: just pair with first available
                    alien_b = group.pop(0)
                    pairings.append((alien_a, alien_b))

            if group:
                unpaired.extend(group)

        return pairings


class MonteCarloEstimator:
    """
    Monte Carlo power estimation through random sampling.

    Estimates true power strength with confidence intervals
    using fewer games than exhaustive simulation.
    """

    def __init__(
        self,
        samples_per_alien: int = 500,
        player_count: int = 4,
        confidence_level: float = 0.95,
        verbose: bool = True
    ):
        self.samples_per_alien = samples_per_alien
        self.player_count = player_count
        self.confidence_level = confidence_level
        self.verbose = verbose
        self.z_score = 1.96  # For 95% CI

    def estimate_power(self, alien_name: str) -> Dict[str, Any]:
        """
        Estimate an alien's power through Monte Carlo sampling.

        Returns dictionary with:
        - estimated_win_rate: Point estimate
        - confidence_interval: (low, high) tuple
        - standard_error: SE of the estimate
        - games_played: Actual samples taken
        """
        if not AlienRegistry.get(alien_name):
            raise ValueError(f"Unknown alien: {alien_name}")

        wins = 0
        games = 0

        if self.verbose:
            print(f"Estimating power of {alien_name}...")

        for i in range(self.samples_per_alien):
            config = GameConfig(
                num_players=self.player_count,
                required_aliens=[alien_name]
            )

            try:
                game = Game(config)
                game.setup()
                winners = game.play()

                if any(p.alien and p.alien.name == alien_name for p in winners):
                    wins += 1
                games += 1

            except Exception:
                continue

        if games == 0:
            return {
                "alien": alien_name,
                "estimated_win_rate": 0.0,
                "confidence_interval": (0.0, 0.0),
                "standard_error": 0.0,
                "games_played": 0
            }

        # Calculate estimates
        p_hat = wins / games
        se = math.sqrt(p_hat * (1 - p_hat) / games)
        margin = self.z_score * se

        ci_low = max(0, p_hat - margin)
        ci_high = min(1, p_hat + margin)

        return {
            "alien": alien_name,
            "estimated_win_rate": p_hat,
            "confidence_interval": (ci_low, ci_high),
            "standard_error": se,
            "games_played": games
        }

    def estimate_all(
        self,
        aliens: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Estimate power for multiple aliens."""
        if aliens is None:
            aliens = [a.name for a in AlienRegistry.get_all()]

        results = []
        for i, alien in enumerate(aliens):
            if self.verbose:
                print(f"[{i+1}/{len(aliens)}] ", end="")

            result = self.estimate_power(alien)
            results.append(result)

        # Sort by estimated win rate
        results.sort(key=lambda x: x["estimated_win_rate"], reverse=True)
        return results

    def generate_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate a text report from estimation results."""
        lines = [
            "=" * 70,
            "MONTE CARLO POWER ESTIMATION REPORT",
            "=" * 70,
            "",
            f"Samples per alien: {self.samples_per_alien}",
            f"Player count: {self.player_count}",
            f"Confidence level: {self.confidence_level*100:.0f}%",
            f"Expected win rate: {100/self.player_count:.1f}%",
            "",
            "RANKINGS",
            "-" * 60,
        ]

        for i, r in enumerate(results, 1):
            ci = r["confidence_interval"]
            lines.append(
                f"{i:3}. {r['alien']:20} | "
                f"WR: {r['estimated_win_rate']*100:5.1f}% | "
                f"CI: [{ci[0]*100:4.1f}%, {ci[1]*100:4.1f}%]"
            )

        return "\n".join(lines)


class SynergyMatrix:
    """
    Analyzes synergies and counters between alien powers.

    A synergy exists when two aliens perform better together (as allies)
    than their individual performance would predict.

    A counter exists when one alien significantly outperforms another
    in head-to-head matchups.
    """

    def __init__(
        self,
        games_per_matchup: int = 100,
        player_count: int = 4,
        verbose: bool = True
    ):
        self.games_per_matchup = games_per_matchup
        self.player_count = player_count
        self.verbose = verbose

        # Synergy matrix: (alien_a, alien_b) -> synergy_score
        self.synergies: Dict[Tuple[str, str], float] = {}

        # Counter matrix: (alien_a, alien_b) -> a's advantage over b
        self.counters: Dict[Tuple[str, str], float] = {}

        # Individual win rates for reference
        self.base_rates: Dict[str, float] = {}

    def calculate_synergy(
        self,
        alien_a: str,
        alien_b: str
    ) -> float:
        """
        Calculate synergy score between two aliens.

        Synergy is positive when they perform better together than expected.
        """
        # Run games where both are on the same team (allies)
        ally_wins = 0
        games = 0

        for _ in range(self.games_per_matchup):
            config = GameConfig(
                num_players=self.player_count,
                required_aliens=[alien_a, alien_b]
            )

            try:
                game = Game(config)
                game.setup()
                winners = game.play()

                winner_names = [p.alien.name for p in winners if p.alien]
                a_won = alien_a in winner_names
                b_won = alien_b in winner_names

                # Count as synergy win if both won
                if a_won and b_won:
                    ally_wins += 2
                elif a_won or b_won:
                    ally_wins += 1

                games += 1

            except Exception:
                continue

        if games == 0:
            return 0.0

        # Expected: 2 * (1/player_count) wins if independent
        expected = 2.0 / self.player_count
        actual = ally_wins / games

        # Synergy score: how much better than expected
        synergy = (actual - expected) / expected if expected > 0 else 0

        key = tuple(sorted([alien_a, alien_b]))
        self.synergies[key] = synergy

        return synergy

    def calculate_counter(
        self,
        alien_a: str,
        alien_b: str
    ) -> float:
        """
        Calculate how much alien_a counters alien_b.

        Positive = A counters B, Negative = B counters A.
        """
        a_wins = 0
        b_wins = 0
        games = 0

        for _ in range(self.games_per_matchup):
            config = GameConfig(
                num_players=self.player_count,
                required_aliens=[alien_a, alien_b]
            )

            try:
                game = Game(config)
                game.setup()
                winners = game.play()

                winner_names = [p.alien.name for p in winners if p.alien]

                if alien_a in winner_names:
                    a_wins += 1
                if alien_b in winner_names:
                    b_wins += 1

                games += 1

            except Exception:
                continue

        if games == 0:
            return 0.0

        a_rate = a_wins / games
        b_rate = b_wins / games

        counter_score = a_rate - b_rate
        self.counters[(alien_a, alien_b)] = counter_score

        return counter_score

    def build_matrix(
        self,
        aliens: Optional[List[str]] = None,
        mode: str = "counter"  # "synergy", "counter", or "both"
    ) -> None:
        """Build the full synergy/counter matrix."""
        if aliens is None:
            aliens = [a.name for a in AlienRegistry.get_all()][:50]  # Limit for performance

        n = len(aliens)
        total = n * (n - 1) // 2
        count = 0

        if self.verbose:
            print(f"Building {mode} matrix for {n} aliens ({total} matchups)")

        for i, alien_a in enumerate(aliens):
            for alien_b in aliens[i+1:]:
                count += 1

                if self.verbose and count % 50 == 0:
                    print(f"  Progress: {count}/{total}")

                if mode in ["counter", "both"]:
                    self.calculate_counter(alien_a, alien_b)

                if mode in ["synergy", "both"]:
                    self.calculate_synergy(alien_a, alien_b)

    def get_best_partners(self, alien: str, top_n: int = 10) -> List[Tuple[str, float]]:
        """Get aliens that synergize best with this alien."""
        partners = []
        for key, score in self.synergies.items():
            if alien in key:
                partner = key[1] if key[0] == alien else key[0]
                partners.append((partner, score))

        partners.sort(key=lambda x: x[1], reverse=True)
        return partners[:top_n]

    def get_counters(self, alien: str, top_n: int = 10) -> List[Tuple[str, float]]:
        """Get aliens that counter this alien."""
        counters = []
        for (a, b), score in self.counters.items():
            if alien == b:  # Looking for aliens that beat this one
                counters.append((a, score))
            elif alien == a:
                counters.append((b, -score))

        counters.sort(key=lambda x: x[1], reverse=True)
        return counters[:top_n]

    def get_countered_by(self, alien: str, top_n: int = 10) -> List[Tuple[str, float]]:
        """Get aliens that this alien counters."""
        return [(name, -score) for name, score in self.get_counters(alien, top_n)]

    def generate_report(self, aliens: Optional[List[str]] = None) -> str:
        """Generate a text report of the synergy/counter analysis."""
        lines = [
            "=" * 70,
            "SYNERGY & COUNTER MATRIX REPORT",
            "=" * 70,
            "",
        ]

        # Top synergies
        all_synergies = sorted(self.synergies.items(), key=lambda x: x[1], reverse=True)
        lines.extend([
            "TOP 20 SYNERGIES (work well together)",
            "-" * 50,
        ])
        for (a, b), score in all_synergies[:20]:
            lines.append(f"  {a:15} + {b:15} = +{score*100:5.1f}%")

        lines.append("")

        # Top counters
        all_counters = sorted(self.counters.items(), key=lambda x: abs(x[1]), reverse=True)
        lines.extend([
            "TOP 20 COUNTERS (A beats B)",
            "-" * 50,
        ])
        for (a, b), score in all_counters[:20]:
            if score > 0:
                lines.append(f"  {a:15} > {b:15} = +{score*100:5.1f}%")
            else:
                lines.append(f"  {b:15} > {a:15} = +{abs(score)*100:5.1f}%")

        return "\n".join(lines)

    def to_dict(self) -> Dict[str, Any]:
        """Export matrix data."""
        return {
            "synergies": {
                f"{k[0]}_{k[1]}": v for k, v in self.synergies.items()
            },
            "counters": {
                f"{k[0]}_vs_{k[1]}": v for k, v in self.counters.items()
            }
        }

    def save(self, filepath: str) -> None:
        """Save matrix to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)


def run_quick_tournament(
    aliens: Optional[List[str]] = None,
    format: str = "swiss",
    games_per_match: int = 50,
    **kwargs
) -> TournamentResults:
    """
    Quick function to run a tournament.

    Args:
        aliens: List of aliens (None = sample of 32)
        format: "swiss" or "round_robin"
        games_per_match: Games per matchup

    Returns:
        TournamentResults object
    """
    if aliens is None:
        all_aliens = [a.name for a in AlienRegistry.get_all()]
        aliens = random.sample(all_aliens, min(32, len(all_aliens)))

    if format == "swiss":
        tournament = SwissTournament(
            aliens=aliens,
            games_per_match=games_per_match,
            **kwargs
        )
    else:
        tournament = RoundRobinTournament(
            aliens=aliens,
            games_per_match=games_per_match,
            **kwargs
        )

    return tournament.run()


def run_monte_carlo_analysis(
    aliens: Optional[List[str]] = None,
    samples: int = 500
) -> List[Dict[str, Any]]:
    """
    Run Monte Carlo power estimation.

    Args:
        aliens: List of aliens (None = all)
        samples: Games per alien

    Returns:
        List of estimation results
    """
    estimator = MonteCarloEstimator(samples_per_alien=samples)
    results = estimator.estimate_all(aliens)
    print(estimator.generate_report(results))
    return results


if __name__ == "__main__":
    # Example: Run a quick Swiss tournament
    print("Running Swiss Tournament...")
    results = run_quick_tournament(format="swiss", games_per_match=30)

    print("\nFinal Standings:")
    for i, alien in enumerate(results.get_standings()[:20], 1):
        print(f"{i:2}. {alien.name:20} | {alien.points:5.1f} pts | WR: {alien.win_rate*100:5.1f}%")
