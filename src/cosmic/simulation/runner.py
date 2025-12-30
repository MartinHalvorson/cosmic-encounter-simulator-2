"""
Simulation runner for Cosmic Encounter.
"""

import time
import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Callable
from concurrent.futures import ThreadPoolExecutor, as_completed

from ..game import Game
from ..types import GameConfig, SimulationConfig
from ..aliens import AlienRegistry
from .stats import Statistics


@dataclass
class SimulationResult:
    """Result of a simulation run."""
    statistics: Statistics
    total_time: float
    games_completed: int
    games_per_second: float

    def summary(self) -> str:
        """Get a text summary of the simulation."""
        lines = [
            self.statistics.summary(),
            "",
            f"Simulation completed in {self.total_time:.2f} seconds",
            f"Games completed: {self.games_completed}",
            f"Speed: {self.games_per_second:.1f} games/second",
        ]
        return "\n".join(lines)


@dataclass
class Simulator:
    """
    Runs simulations of Cosmic Encounter games.
    """
    config: SimulationConfig = field(default_factory=SimulationConfig)
    statistics: Statistics = field(default_factory=Statistics)
    _rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if self.config.game_config.seed is not None:
            self._rng.seed(self.config.game_config.seed)

    def run(
        self,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> SimulationResult:
        """
        Run the simulation.

        Args:
            progress_callback: Optional callback(completed, total) for progress

        Returns:
            SimulationResult with statistics
        """
        start_time = time.time()
        games_completed = 0
        errors = 0

        for i in range(self.config.num_games):
            try:
                self._run_single_game()
                games_completed += 1
            except Exception as e:
                if self.config.catch_errors:
                    errors += 1
                    if self.config.log_errors:
                        print(f"Game {i} error: {e}")
                else:
                    raise

            # Progress reporting
            if self.config.show_progress:
                if (i + 1) % self.config.progress_interval == 0:
                    elapsed = time.time() - start_time
                    rate = (i + 1) / elapsed if elapsed > 0 else 0
                    print(f"Progress: {i + 1}/{self.config.num_games} ({rate:.1f} games/s)")

            if progress_callback:
                progress_callback(i + 1, self.config.num_games)

        total_time = time.time() - start_time
        games_per_second = games_completed / total_time if total_time > 0 else 0

        return SimulationResult(
            statistics=self.statistics,
            total_time=total_time,
            games_completed=games_completed,
            games_per_second=games_per_second,
        )

    def _run_single_game(self) -> None:
        """Run a single game and record statistics."""
        # Create game config
        game_config = GameConfig(
            num_players=self.config.game_config.num_players,
            colonies_to_win=self.config.game_config.colonies_to_win,
            max_turns=self.config.game_config.max_turns,
            seed=self._rng.randint(0, 2**31),
        )

        game = Game(config=game_config)

        # Select powers
        powers = None
        if self.config.powers_to_test:
            powers = self._rng.sample(
                self.config.powers_to_test,
                min(len(self.config.powers_to_test), game_config.num_players)
            )

        # Setup and play game
        game.setup(powers=powers)
        winners = game.play()

        # Record statistics
        winner_names = [w.name for w in winners]
        alien_map = {p.name: p.alien_name for p in game.players}
        final_colonies = {
            p.name: p.count_foreign_colonies(game.planets)
            for p in game.players
        }

        # Check for alternate wins
        alternate_win = any(
            w.alien and w.alien.has_alternate_win
            for w in winners
        )

        self.statistics.record_game(
            num_players=game_config.num_players,
            winners=winner_names,
            alien_map=alien_map,
            turn_count=game.current_turn,
            final_colonies=final_colonies,
            alternate_win=alternate_win,
            timed_out=game.current_turn >= game_config.max_turns,
        )

    def run_with_varying_players(
        self,
        player_counts: List[int],
        games_per_count: int
    ) -> SimulationResult:
        """
        Run simulations with varying player counts.

        Args:
            player_counts: List of player counts to test
            games_per_count: Number of games per player count

        Returns:
            Combined SimulationResult
        """
        start_time = time.time()
        total_games = len(player_counts) * games_per_count
        games_completed = 0

        for count in player_counts:
            print(f"\nRunning {games_per_count} games with {count} players...")

            self.config.game_config.num_players = count

            for i in range(games_per_count):
                try:
                    self._run_single_game()
                    games_completed += 1
                except Exception as e:
                    if self.config.catch_errors:
                        if self.config.log_errors:
                            print(f"Error: {e}")
                    else:
                        raise

                if self.config.show_progress:
                    if (i + 1) % self.config.progress_interval == 0:
                        print(f"  Progress: {i + 1}/{games_per_count}")

        total_time = time.time() - start_time
        games_per_second = games_completed / total_time if total_time > 0 else 0

        return SimulationResult(
            statistics=self.statistics,
            total_time=total_time,
            games_completed=games_completed,
            games_per_second=games_per_second,
        )

    def run_power_comparison(
        self,
        powers_to_compare: List[str],
        games_per_power: int
    ) -> SimulationResult:
        """
        Run simulations comparing specific alien powers.
        Each power is tested in games_per_power games.

        Args:
            powers_to_compare: List of alien power names to compare
            games_per_power: Number of games each power should play

        Returns:
            SimulationResult with comparison data
        """
        start_time = time.time()
        games_completed = 0

        # Get all available powers
        all_powers = AlienRegistry.get_names()

        for target_power in powers_to_compare:
            if target_power not in all_powers:
                print(f"Warning: Power '{target_power}' not found")
                continue

            print(f"\nTesting {target_power}...")

            for i in range(games_per_power):
                try:
                    # Ensure target power is in the game
                    num_players = self.config.game_config.num_players
                    other_powers = [p for p in all_powers if p != target_power]
                    selected_others = self._rng.sample(
                        other_powers,
                        min(len(other_powers), num_players - 1)
                    )
                    powers = [target_power] + selected_others

                    game_config = GameConfig(
                        num_players=num_players,
                        seed=self._rng.randint(0, 2**31),
                    )
                    game = Game(config=game_config)
                    game.setup(powers=powers)
                    winners = game.play()

                    # Record stats
                    winner_names = [w.name for w in winners]
                    alien_map = {p.name: p.alien_name for p in game.players}
                    final_colonies = {
                        p.name: p.count_foreign_colonies(game.planets)
                        for p in game.players
                    }

                    self.statistics.record_game(
                        num_players=num_players,
                        winners=winner_names,
                        alien_map=alien_map,
                        turn_count=game.current_turn,
                        final_colonies=final_colonies,
                    )
                    games_completed += 1

                except Exception as e:
                    if self.config.catch_errors:
                        if self.config.log_errors:
                            print(f"Error: {e}")
                    else:
                        raise

                if self.config.show_progress:
                    if (i + 1) % self.config.progress_interval == 0:
                        print(f"  Progress: {i + 1}/{games_per_power}")

        total_time = time.time() - start_time
        games_per_second = games_completed / total_time if total_time > 0 else 0

        return SimulationResult(
            statistics=self.statistics,
            total_time=total_time,
            games_completed=games_completed,
            games_per_second=games_per_second,
        )


def run_quick_simulation(
    num_games: int = 100,
    num_players: int = 5,
    show_progress: bool = True
) -> SimulationResult:
    """
    Run a quick simulation with default settings.

    Args:
        num_games: Number of games to simulate
        num_players: Players per game
        show_progress: Whether to show progress

    Returns:
        SimulationResult
    """
    config = SimulationConfig(
        num_games=num_games,
        game_config=GameConfig(num_players=num_players),
        show_progress=show_progress,
        progress_interval=max(1, num_games // 10),
    )

    simulator = Simulator(config=config)
    return simulator.run()
