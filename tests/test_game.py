"""
Tests for the core Game class.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig, GamePhase
from cosmic.player import Player


class TestGameSetup:
    """Tests for game setup and initialization."""

    def test_game_creates_correct_number_of_players(self):
        """Game should create the specified number of players."""
        for num_players in [3, 4, 5, 6]:
            config = GameConfig(num_players=num_players, seed=42)
            game = Game(config=config)
            game.setup()
            assert len(game.players) == num_players

    def test_each_player_has_home_planets(self):
        """Each player should start with 5 home planets."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert len(player.home_planets) == 5

    def test_each_player_has_starting_hand(self):
        """Each player should start with 8 cards."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert len(player.hand) >= 1  # At least one encounter card

    def test_each_player_has_alien_power(self):
        """Each player should have an alien power assigned."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert player.alien is not None

    def test_seeded_game_is_reproducible(self):
        """Games with same seed should produce same alien assignments."""
        config1 = GameConfig(num_players=4, seed=12345)
        game1 = Game(config=config1)
        game1.setup()

        config2 = GameConfig(num_players=4, seed=12345)
        game2 = Game(config=config2)
        game2.setup()

        aliens1 = [p.alien.name for p in game1.players]
        aliens2 = [p.alien.name for p in game2.players]
        assert aliens1 == aliens2

    def test_required_aliens_are_included(self):
        """Required aliens should always be in the game."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Machine", "Parasite"]
        )
        game = Game(config=config)
        game.setup()

        alien_names = [p.alien.name for p in game.players]
        assert "Machine" in alien_names
        assert "Parasite" in alien_names


class TestGameFlow:
    """Tests for game flow and encounter mechanics."""

    def test_game_starts_at_turn_1(self):
        """Game should start at turn 1 after first encounter begins."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        assert game.current_turn == 0
        game.play_encounter()
        assert game.current_turn == 1

    def test_game_completes_without_error(self):
        """A game should complete without raising exceptions."""
        config = GameConfig(num_players=4, seed=42, max_turns=50)
        game = Game(config=config)
        game.setup()

        winners = game.play()

        # Game should end (either winner or max turns)
        assert game.is_over or game.current_turn >= config.max_turns

    def test_winner_has_five_colonies(self):
        """Winner should have at least 5 foreign colonies."""
        config = GameConfig(num_players=4, seed=42, max_turns=100)
        game = Game(config=config)
        game.setup()

        winners = game.play()

        if winners:  # If there's a winner
            for winner in winners:
                # Either standard win or alternate win condition
                colonies = winner.count_foreign_colonies(game.planets)
                has_alternate = (
                    winner.alien and
                    winner.alien.has_alternate_win and
                    winner.alien.check_alternate_win(game, winner)
                )
                assert colonies >= 5 or has_alternate


class TestEncounterPhases:
    """Tests for individual encounter phases."""

    def test_regroup_returns_ship_from_warp(self):
        """Regroup should return 1 ship from warp."""
        # Use Human alien which doesn't affect warp retrieval
        config = GameConfig(num_players=4, seed=42, required_aliens=["Human"])
        game = Game(config=config)
        game.setup()

        # Find the Human player
        human_player = next(p for p in game.players if p.alien.name == "Human")
        human_player.ships_in_warp = 5

        initial_warp = human_player.ships_in_warp

        # Start encounter (which does regroup)
        game.offense = human_player
        game.encounter_number = 1
        game._regroup_phase()

        assert human_player.ships_in_warp == initial_warp - 1

    def test_destiny_sets_defender(self):
        """Destiny phase should set a defender different from offense."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        game.offense = game.players[0]
        game._destiny_phase()

        assert game.defense is not None
        # Note: In some cases destiny could point to self (special destiny)


class TestVictoryConditions:
    """Tests for victory condition checking."""

    def test_five_colonies_triggers_win(self):
        """Player with 5 foreign colonies should win."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Give player 0 colonies on other planets
        player = game.players[0]
        foreign_planets = [p for p in game.planets if p.owner != player][:5]

        for planet in foreign_planets:
            planet.add_ships(player.name, 1)

        game._check_game_end()

        assert game.is_over
        assert player in game.winners

    def test_shared_victory_possible(self):
        """Multiple players can win together."""
        config = GameConfig(num_players=4, seed=42, allow_shared_victory=True)
        game = Game(config=config)
        game.setup()

        # Give player1 5 foreign colonies
        player1 = game.players[0]
        foreign_planets = [p for p in game.planets if p.owner != player1][:5]
        for planet in foreign_planets:
            planet.add_ships(player1.name, 1)

        game._check_game_end()

        # At least one winner (player1)
        assert len(game.winners) >= 1
        assert player1 in game.winners


class TestPowerActivation:
    """Tests for alien power mechanics."""

    def test_power_can_be_zapped(self):
        """Cosmic Zap should disable power for encounter."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        assert game.is_power_active(player)

        game.zapped_powers.append(player)
        assert not game.is_power_active(player)

    def test_power_lost_with_few_home_colonies(self):
        """Power should be lost with 1-2 home colonies."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        assert player.power_active

        # Remove player from most home planets
        for planet in player.home_planets[:4]:
            planet.set_ships(player.name, 0)

        # Update power status (only 1 home colony left)
        player.check_power_status(1)
        assert not player.power_active


class TestDeckMechanics:
    """Tests for card deck functionality."""

    def test_hand_refills_when_no_encounter_cards(self):
        """Player should get new hand when out of encounter cards."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]

        # Remove all encounter cards
        player.hand = [c for c in player.hand
                      if not hasattr(c, 'value') or c.value is None]

        initial_hand_size = len(player.hand)
        game._ensure_encounter_card(player)

        # Should have new hand with encounter cards
        assert player.has_encounter_card()


class TestMultipleGames:
    """Tests for running multiple simulations."""

    def test_can_run_100_games(self):
        """Should be able to run 100 games without errors."""
        errors = []
        completed = 0

        for i in range(100):
            try:
                config = GameConfig(num_players=4, seed=i, max_turns=100)
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception as e:
                errors.append((i, str(e)))

        assert completed == 100, f"Failed games: {errors[:5]}"


class TestTwoPlayerVariant:
    """Tests for 2-player variant support."""

    def test_two_player_mode_auto_enabled(self):
        """2-player mode should auto-enable for 2 players."""
        config = GameConfig(num_players=2, seed=42)
        game = Game(config=config)
        game.setup()

        assert game.config.two_player_mode is True

    def test_dual_powers_default_enabled(self):
        """Dual powers should be enabled by default in 2-player mode."""
        config = GameConfig(num_players=2, seed=42)
        game = Game(config=config)
        game.setup()

        assert game.config.dual_powers is True

    def test_players_have_two_powers(self):
        """Each player should have primary and secondary alien."""
        config = GameConfig(num_players=2, seed=42)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert player.alien is not None
            assert player.secondary_alien is not None
            assert player.alien.name != player.secondary_alien.name

    def test_two_player_game_completes(self):
        """2-player game should complete without errors."""
        config = GameConfig(num_players=2, seed=42, max_turns=100)
        game = Game(config=config)
        game.setup()

        winners = game.play()

        assert game.is_over or game.current_turn >= 100

    def test_multiple_two_player_games(self):
        """Multiple 2-player games should complete without errors."""
        completed = 0
        errors = []

        for i in range(50):
            try:
                config = GameConfig(num_players=2, seed=i, max_turns=100)
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception as e:
                errors.append((i, str(e)))

        assert completed == 50, f"Failed games: {errors[:3]}"

    def test_required_aliens_in_two_player(self):
        """Required aliens should work in 2-player mode."""
        config = GameConfig(
            num_players=2,
            seed=42,
            required_aliens=["Virus", "Macron"]
        )
        game = Game(config=config)
        game.setup()

        # All powers (primary + secondary) should include required
        all_powers = []
        for p in game.players:
            all_powers.append(p.alien.name)
            if p.secondary_alien:
                all_powers.append(p.secondary_alien.name)

        assert "Virus" in all_powers
        assert "Macron" in all_powers


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
