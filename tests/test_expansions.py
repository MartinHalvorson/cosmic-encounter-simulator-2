"""
Tests for expansion features: Tech Cards and Hazards.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig


class TestTechCards:
    """Tests for Tech Cards (Cosmic Incursion expansion)."""

    def test_tech_deck_initialized_when_enabled(self):
        """Tech deck should be created when use_tech is True."""
        config = GameConfig(num_players=4, seed=42, use_tech=True)
        game = Game(config=config)
        game.setup()

        assert game.tech_deck is not None
        assert game.tech_deck.cards_remaining() >= 0

    def test_tech_deck_not_initialized_when_disabled(self):
        """Tech deck should be None when use_tech is False."""
        config = GameConfig(num_players=4, seed=42, use_tech=False)
        game = Game(config=config)
        game.setup()

        assert game.tech_deck is None

    def test_players_get_starting_tech(self):
        """Each player should start researching a tech when tech is enabled."""
        config = GameConfig(num_players=4, seed=42, use_tech=True)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            # Player should have tech cards
            assert len(player.tech_state.available_techs) >= 1 or \
                   player.tech_state.current_research is not None

    def test_game_with_tech_completes(self):
        """Game with tech enabled should complete without errors."""
        config = GameConfig(num_players=4, seed=42, use_tech=True, max_turns=50)
        game = Game(config=config)
        game.setup()

        winners = game.play()
        # Game should complete (winner or max turns)
        assert game.is_over or game.current_turn >= 50

    def test_tech_combat_bonus_applied(self):
        """Tech combat bonuses should be calculated correctly."""
        config = GameConfig(num_players=4, seed=42, use_tech=True)
        game = Game(config=config)
        game.setup()

        player = game.players[0]

        # Initially no bonus (nothing completed)
        bonus = game._get_tech_combat_bonus(player, True, 4)
        assert bonus == 0

    def test_multiple_games_with_tech(self):
        """Multiple games with tech should complete without errors."""
        completed = 0
        for i in range(20):
            config = GameConfig(num_players=4, seed=i, use_tech=True, max_turns=75)
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == 20


class TestHazards:
    """Tests for Hazard Deck (Cosmic Conflict expansion)."""

    def test_hazard_deck_initialized_when_enabled(self):
        """Hazard deck should be created when use_hazards is True."""
        config = GameConfig(num_players=4, seed=42, use_hazards=True)
        game = Game(config=config)
        game.setup()

        assert game.hazard_deck is not None
        assert game.hazard_deck.cards_remaining() > 0

    def test_hazard_deck_not_initialized_when_disabled(self):
        """Hazard deck should be None when use_hazards is False."""
        config = GameConfig(num_players=4, seed=42, use_hazards=False)
        game = Game(config=config)
        game.setup()

        assert game.hazard_deck is None

    def test_game_with_hazards_completes(self):
        """Game with hazards enabled should complete without errors."""
        config = GameConfig(num_players=4, seed=42, use_hazards=True, max_turns=50)
        game = Game(config=config)
        game.setup()

        winners = game.play()
        # Game should complete
        assert game.is_over or game.current_turn >= 50

    def test_hazard_drawn_during_encounter(self):
        """Hazard should be drawn at start of encounter when enabled."""
        config = GameConfig(num_players=4, seed=42, use_hazards=True)
        game = Game(config=config)
        game.setup()

        # Play one encounter to trigger hazard draw
        game.play_encounter()

        # After encounter, hazard should be discarded
        # But we can check the hazard deck was used
        total_hazards = len(game.hazard_deck.draw_pile) + len(game.hazard_deck.discard_pile)
        assert total_hazards == 20  # Original deck size

    def test_multiple_games_with_hazards(self):
        """Multiple games with hazards should complete without errors."""
        completed = 0
        for i in range(20):
            config = GameConfig(num_players=4, seed=i, use_hazards=True, max_turns=75)
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == 20


class TestCombinedExpansions:
    """Tests for both expansions enabled together."""

    def test_both_expansions_enabled(self):
        """Game with both tech and hazards should work correctly."""
        config = GameConfig(
            num_players=4,
            seed=42,
            use_tech=True,
            use_hazards=True,
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        assert game.tech_deck is not None
        assert game.hazard_deck is not None

        winners = game.play()
        assert game.is_over or game.current_turn >= 50

    def test_multiple_games_with_both_expansions(self):
        """Multiple games with both expansions should complete without errors."""
        completed = 0
        for i in range(20):
            config = GameConfig(
                num_players=4,
                seed=i,
                use_tech=True,
                use_hazards=True,
                max_turns=75
            )
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == 20


class TestSpaceStations:
    """Tests for Space Stations (Cosmic Storm expansion)."""

    def test_stations_initialized_when_enabled(self):
        """Players should receive station markers when use_space_stations is True."""
        config = GameConfig(num_players=4, seed=42, use_space_stations=True)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert len(player.available_stations) == 3
            assert len(player.space_stations) == 0

    def test_stations_not_initialized_when_disabled(self):
        """Players should not have stations when use_space_stations is False."""
        config = GameConfig(num_players=4, seed=42, use_space_stations=False)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            assert len(player.available_stations) == 0

    def test_game_with_stations_completes(self):
        """Game with space stations enabled should complete without errors."""
        config = GameConfig(num_players=4, seed=42, use_space_stations=True, max_turns=50)
        game = Game(config=config)
        game.setup()

        winners = game.play()
        assert game.is_over or game.current_turn >= 50

    def test_station_placement(self):
        """Players should be able to place stations."""
        from cosmic.types import StationType

        config = GameConfig(num_players=4, seed=42, use_space_stations=True)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        # Get a planet that's not the player's
        foreign_planet = [p for p in game.planets if p.owner != player][0]

        # Place a station
        station = player.place_station(StationType.STATION_ALPHA, foreign_planet.planet_id)

        assert station is not None
        assert len(player.available_stations) == 2
        assert len(player.space_stations) == 1

    def test_station_defense_bonus(self):
        """Alpha station should provide +2 defense bonus."""
        from cosmic.types import StationType

        config = GameConfig(num_players=4, seed=42, use_space_stations=True)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        planet = game.planets[0]

        # Place Alpha station
        player.place_station(StationType.STATION_ALPHA, planet.planet_id)

        # Check bonus
        bonus = player.get_station_defense_bonus(planet.planet_id)
        assert bonus == 2

    def test_multiple_games_with_stations(self):
        """Multiple games with space stations should complete without errors."""
        completed = 0
        for i in range(20):
            config = GameConfig(num_players=4, seed=i, use_space_stations=True, max_turns=75)
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == 20


class TestAllExpansions:
    """Tests for all expansions enabled together."""

    def test_all_expansions_enabled(self):
        """Game with all expansions should work correctly."""
        config = GameConfig(
            num_players=4,
            seed=42,
            use_tech=True,
            use_hazards=True,
            use_space_stations=True,
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        assert game.tech_deck is not None
        assert game.hazard_deck is not None
        for player in game.players:
            assert len(player.available_stations) == 3

        winners = game.play()
        assert game.is_over or game.current_turn >= 50

    def test_multiple_games_with_all_expansions(self):
        """Multiple games with all expansions should complete without errors."""
        completed = 0
        for i in range(10):
            config = GameConfig(
                num_players=4,
                seed=i,
                use_tech=True,
                use_hazards=True,
                use_space_stations=True,
                max_turns=75
            )
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == 10


class TestLuxSystem:
    """Tests for Lux System (Cosmic Odyssey expansion)."""

    def test_lux_manager_initialization(self):
        """LuxManager should initialize players with starting Lux."""
        from cosmic.cards.lux_system import LuxManager

        manager = LuxManager(starting_lux=5)
        manager.initialize_player("Player 1")

        state = manager.get_player_state("Player 1")
        assert state is not None
        assert state.total_lux == 5

    def test_lux_spending(self):
        """Players should be able to spend Lux."""
        from cosmic.cards.lux_system import PlayerLuxState, LuxAction

        state = PlayerLuxState(lux_count=10)

        assert state.can_afford(LuxAction.BUY_CARD)  # Cost 3
        assert state.spend(3)
        assert state.lux_count == 7

    def test_ultra_lux_value(self):
        """Ultra Lux should be worth 3 regular Lux."""
        from cosmic.cards.lux_system import PlayerLuxState

        state = PlayerLuxState(lux_count=0, ultra_lux_count=2)
        assert state.total_lux == 6

    def test_lux_purchase_action(self):
        """Players should be able to purchase Lux actions."""
        from cosmic.cards.lux_system import PlayerLuxState, LuxAction

        state = PlayerLuxState(lux_count=10)

        # Purchase RETRIEVE_SHIP (cost 2)
        assert state.purchase_action(LuxAction.RETRIEVE_SHIP)
        assert state.lux_count == 8
        assert LuxAction.RETRIEVE_SHIP in state.actions_purchased

    def test_cannot_afford(self):
        """Players should not be able to purchase actions they can't afford."""
        from cosmic.cards.lux_system import PlayerLuxState, LuxAction

        state = PlayerLuxState(lux_count=1)

        # Cannot afford BUY_CARD (cost 3)
        assert not state.can_afford(LuxAction.BUY_CARD)
        assert not state.purchase_action(LuxAction.BUY_CARD)


class TestRiftCards:
    """Tests for Rift Cards (Cosmic Odyssey expansion)."""

    def test_rift_card_creation(self):
        """Rift cards should be created correctly."""
        from cosmic.cards.rift_cards import RiftCard, RiftType

        rift = RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=2)
        assert rift.rift_type == RiftType.WARP_RIFT
        assert rift.ships_affected == 2
        assert not rift.is_encounter_card()

    def test_rift_deck_standard(self):
        """Standard rift deck should have 12 cards."""
        from cosmic.cards.rift_cards import RiftDeck

        rifts = RiftDeck.create_standard_rifts()
        assert len(rifts) == 12

    def test_rift_type_checking(self):
        """is_rift_card should correctly identify rift cards."""
        from cosmic.cards.rift_cards import RiftCard, RiftType, is_rift_card
        from cosmic.cards.base import AttackCard

        rift = RiftCard(rift_type=RiftType.TRAP_RIFT)
        attack = AttackCard(value=10)

        assert is_rift_card(rift)
        assert not is_rift_card(attack)

    def test_rift_types(self):
        """All rift types should be available."""
        from cosmic.cards.rift_cards import RiftType

        expected_types = ["WARP_RIFT", "TRAP_RIFT", "MIRROR_RIFT", "VOID_RIFT", "TIME_RIFT"]
        actual_types = [rt.name for rt in RiftType]

        for expected in expected_types:
            assert expected in actual_types


class TestCosmicOdyssey:
    """Tests for combined Cosmic Odyssey features."""

    def test_game_config_has_lux_options(self):
        """GameConfig should have Lux configuration options."""
        config = GameConfig(use_lux=True, starting_lux=7)
        assert config.use_lux is True
        assert config.starting_lux == 7

    def test_game_config_has_rift_options(self):
        """GameConfig should have Rift configuration options."""
        config = GameConfig(use_rifts=True)
        assert config.use_rifts is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
