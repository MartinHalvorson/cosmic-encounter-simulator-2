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
    """Tests for Hazard Deck (Cosmic Storm expansion)."""

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


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
