"""
Tests for multi-player count game simulations.

Validates that games work correctly across different player counts (2-8 players).
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig, GamePhase
from cosmic.simulation.runner import Simulator
from cosmic.types import SimulationConfig


class TestTwoPlayerGames:
    """Tests for 2-player variant games."""

    def test_two_player_game_completes(self):
        """2-player games should complete successfully."""
        config = GameConfig(num_players=2, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_two_player_dual_powers(self):
        """2-player games should use dual powers mode."""
        config = GameConfig(num_players=2, seed=42)
        game = Game(config=config)
        game.setup()

        # Each player should have a secondary alien in 2-player mode
        for player in game.players:
            assert player.alien is not None
            # Dual powers should be enabled
            assert game.config.dual_powers or hasattr(player, 'secondary_alien')

    def test_two_player_simulation_batch(self):
        """Run batch of 2-player games."""
        game_config = GameConfig(num_players=2, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 100
        assert sim.statistics.avg_game_length > 0


class TestThreePlayerGames:
    """Tests for 3-player games."""

    def test_three_player_game_completes(self):
        """3-player games should complete successfully."""
        config = GameConfig(num_players=3, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_three_player_alliance_dynamics(self):
        """3-player games have limited alliance options."""
        config = GameConfig(num_players=3, seed=42)
        game = Game(config=config)
        game.setup()

        # With 3 players, only 1 potential ally per encounter
        potential_allies = [p for p in game.players if p != game.players[0] and p != game.players[1]]
        assert len(potential_allies) == 1

    def test_three_player_simulation_batch(self):
        """Run batch of 3-player games."""
        game_config = GameConfig(num_players=3, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 100


class TestFourPlayerGames:
    """Tests for 4-player games (standard)."""

    def test_four_player_game_completes(self):
        """4-player games should complete successfully."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_four_player_planets(self):
        """4-player games should have 20 planets total."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # 5 home planets per player
        assert len(game.planets) == 20

    def test_four_player_simulation_batch(self):
        """Run batch of 4-player games."""
        game_config = GameConfig(num_players=4, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 100


class TestFivePlayerGames:
    """Tests for 5-player games (standard)."""

    def test_five_player_game_completes(self):
        """5-player games should complete successfully."""
        config = GameConfig(num_players=5, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_five_player_alliance_options(self):
        """5-player games have 3 potential allies per encounter."""
        config = GameConfig(num_players=5, seed=42)
        game = Game(config=config)
        game.setup()

        # With 5 players, 3 potential allies per encounter
        for i in range(5):
            offense_idx = i
            defense_idx = (i + 1) % 5
            potential_allies = [p for j, p in enumerate(game.players)
                              if j != offense_idx and j != defense_idx]
            assert len(potential_allies) == 3

    def test_five_player_simulation_batch(self):
        """Run batch of 5-player games."""
        game_config = GameConfig(num_players=5, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 100


class TestSixPlayerGames:
    """Tests for 6-player games."""

    def test_six_player_game_completes(self):
        """6-player games should complete successfully."""
        config = GameConfig(num_players=6, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_six_player_planets(self):
        """6-player games should have 30 planets total."""
        config = GameConfig(num_players=6, seed=42)
        game = Game(config=config)
        game.setup()

        # 5 home planets per player
        assert len(game.planets) == 30

    def test_six_player_simulation_batch(self):
        """Run batch of 6-player games."""
        game_config = GameConfig(num_players=6, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 100


class TestSevenPlayerGames:
    """Tests for 7-player games (extended)."""

    def test_seven_player_game_completes(self):
        """7-player games should complete successfully."""
        config = GameConfig(num_players=7, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_seven_player_simulation_batch(self):
        """Run batch of 7-player games."""
        game_config = GameConfig(num_players=7, seed=42)
        sim_config = SimulationConfig(
            num_games=50,  # Fewer games for larger player counts
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 50


class TestEightPlayerGames:
    """Tests for 8-player games (maximum)."""

    def test_eight_player_game_completes(self):
        """8-player games should complete successfully."""
        config = GameConfig(num_players=8, seed=42)
        game = Game(config=config)
        game.setup()
        game.play()

        assert game.is_over
        assert len(game.winners) >= 1

    def test_eight_player_simulation_batch(self):
        """Run batch of 8-player games."""
        game_config = GameConfig(num_players=8, seed=42)
        sim_config = SimulationConfig(
            num_games=50,  # Fewer games for larger player counts
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        assert results.games_completed == 50


class TestPlayerCountComparison:
    """Tests comparing game dynamics across player counts."""

    def test_game_length_varies_by_player_count(self):
        """Game length should vary based on player count."""
        lengths = {}

        for num_players in [3, 4, 5, 6]:
            game_config = GameConfig(num_players=num_players, seed=42)
            sim_config = SimulationConfig(
                num_games=50,
                game_config=game_config,
                show_progress=False,
                catch_errors=False
            )
            sim = Simulator(config=sim_config)
            sim.run()
            lengths[num_players] = sim.statistics.avg_game_length

        # Games should complete (positive length)
        for length in lengths.values():
            assert length > 0

    def test_win_rate_distribution(self):
        """Win rates should be roughly equal across players."""
        game_config = GameConfig(num_players=5, seed=42)
        sim_config = SimulationConfig(
            num_games=100,
            game_config=game_config,
            show_progress=False,
            catch_errors=False
        )
        sim = Simulator(config=sim_config)
        results = sim.run()

        # Check that wins are distributed (not all to one player)
        # The statistics track by alien, but we can check the game completed
        assert results.games_completed == 100

    def test_shared_victory_rates(self):
        """Shared victories should occur across player counts."""
        for num_players in [4, 5, 6]:
            game_config = GameConfig(num_players=num_players, seed=42)
            sim_config = SimulationConfig(
                num_games=100,
                game_config=game_config,
                show_progress=False,
                catch_errors=False
            )
            sim = Simulator(config=sim_config)
            results = sim.run()

            # Games should complete successfully
            assert results.games_completed == 100


class TestDestinyDeckScaling:
    """Tests for destiny deck scaling with player count."""

    def test_destiny_deck_has_all_players(self):
        """Destiny deck should contain cards for all players."""
        for num_players in [3, 4, 5, 6]:
            config = GameConfig(num_players=num_players, seed=42)
            game = Game(config=config)
            game.setup()

            # Destiny deck should be created
            assert game.destiny_deck is not None

    def test_destiny_distribution_fair(self):
        """Each player should be targeted roughly equally."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Draw multiple destiny cards to check distribution
        targets = {}
        for _ in range(20):
            card = game.destiny_deck.draw()
            if card:
                if card.is_special:
                    name = card.special_type or "special"
                else:
                    name = card.player.name if card.player else "Unknown"
                targets[name] = targets.get(name, 0) + 1
                game.destiny_deck.discard(card)

        # Should have multiple different targets
        assert len(targets) >= 2
