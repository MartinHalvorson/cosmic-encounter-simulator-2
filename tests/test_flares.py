"""
Tests for flare card mechanics.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.cards.flare_deck import FlareDeck, FLARE_EFFECTS


class TestFlareDeck:
    """Tests for flare deck initialization and card creation."""

    def test_flare_deck_creates_cards_for_aliens(self):
        """Flare deck should create cards for specified aliens."""
        deck = FlareDeck()
        alien_names = ["Machine", "Virus", "Zombie"]
        flares = deck.create_flares_for_game(alien_names)

        assert len(flares) == 3
        assert all(f.alien_name in alien_names for f in flares)

    def test_flare_cards_have_wild_and_super_effects(self):
        """Each flare should have wild and super effects."""
        deck = FlareDeck()
        flares = deck.create_flares_for_game(["Machine", "Human"])

        for flare in flares:
            assert flare.wild_effect is not None
            assert flare.super_effect is not None
            assert "Wild" in flare.wild_effect
            assert "Super" in flare.super_effect

    def test_flare_effects_defined_for_key_aliens(self):
        """FLARE_EFFECTS should have definitions for key aliens."""
        key_aliens = ["Machine", "Virus", "Zombie", "Human", "Warrior"]
        for alien in key_aliens:
            assert alien in FLARE_EFFECTS
            assert "wild" in FLARE_EFFECTS[alien]
            assert "super" in FLARE_EFFECTS[alien]


class TestFlareGameIntegration:
    """Tests for flare integration in games."""

    def test_flares_added_to_cosmic_deck(self):
        """Flares should be added to cosmic deck when use_flares is True."""
        config = GameConfig(num_players=4, seed=42, use_flares=True)
        game = Game(config=config)
        game.setup()

        # Check that cosmic deck has flare cards
        has_flares = any(
            hasattr(card, 'alien_name')
            for card in game.cosmic_deck.draw_pile + game.cosmic_deck.discard_pile
        )
        # Flares get shuffled into hands too
        for player in game.players:
            has_flares = has_flares or any(
                hasattr(card, 'alien_name') for card in player.hand
            )

        assert has_flares

    def test_game_with_flares_completes(self):
        """Game with flares enabled should complete without errors."""
        config = GameConfig(num_players=4, seed=42, use_flares=True, max_turns=75)
        game = Game(config=config)
        game.setup()

        winners = game.play()
        assert game.is_over or game.current_turn >= 75

    def test_multiple_games_with_flares(self):
        """Multiple games with flares should complete without errors."""
        completed = 0
        errors = []

        for i in range(50):
            try:
                config = GameConfig(num_players=4, seed=i, use_flares=True, max_turns=100)
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception as e:
                errors.append((i, str(e)))

        assert completed == 50, f"Failed games: {errors[:3]}"


class TestFlareEffects:
    """Tests for specific flare effect mechanics."""

    def test_human_flare_wild_adds_bonus(self):
        """Human wild flare should add +3 to total."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Human"])
        game = Game(config=config)
        game.setup()

        context = {"flare_bonus": 0}
        from cosmic.cards.base import FlareCard
        flare = FlareCard(alien_name="Human", wild_effect="test", super_effect="test")

        game._apply_flare_wild(game.players[0], flare, context)
        assert context["flare_bonus"] == 3

    def test_human_flare_super_adds_bonus(self):
        """Human super flare should add +6 to total."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Human"])
        game = Game(config=config)
        game.setup()

        human = next(p for p in game.players if p.alien.name == "Human")
        context = {"flare_bonus": 0}
        from cosmic.cards.base import FlareCard
        flare = FlareCard(alien_name="Human", wild_effect="test", super_effect="test")

        game._apply_flare_super(human, flare, context)
        assert context["flare_bonus"] == 6

    def test_macron_flare_sets_ship_multiplier(self):
        """Macron flare should set ship multiplier."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Macron"])
        game = Game(config=config)
        game.setup()

        context = {"flare_ship_multiplier": 1}
        from cosmic.cards.base import FlareCard
        flare = FlareCard(alien_name="Macron", wild_effect="test", super_effect="test")

        game._apply_flare_wild(game.players[0], flare, context)
        assert context["flare_ship_multiplier"] == 2

        macron = next(p for p in game.players if p.alien.name == "Macron")
        context = {"flare_ship_multiplier": 1}
        game._apply_flare_super(macron, flare, context)
        assert context["flare_ship_multiplier"] == 5

    def test_warrior_flare_uses_warp_ships(self):
        """Warrior flare should add bonus based on ships in warp."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Warrior"])
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        player.ships_in_warp = 5

        context = {"flare_bonus": 0}
        from cosmic.cards.base import FlareCard
        flare = FlareCard(alien_name="Warrior", wild_effect="test", super_effect="test")

        game._apply_flare_wild(player, flare, context)
        assert context["flare_bonus"] == 5  # +1 per ship

        warrior = next(p for p in game.players if p.alien.name == "Warrior")
        warrior.ships_in_warp = 5
        context = {"flare_bonus": 0}
        game._apply_flare_super(warrior, flare, context)
        assert context["flare_bonus"] == 10  # +2 per ship


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
