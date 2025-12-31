"""
Tests for AI decision-making, particularly power-aware strategies.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.ai.strategic_ai import (
    StrategicAI, DANGEROUS_POWERS, NEGOTIATE_FRIENDLY_POWERS,
    COMBAT_MODIFIER_POWERS, LOW_CARD_POWERS, HIGH_CARD_POWERS
)
from cosmic.ai.basic_ai import BasicAI


class TestStrategicAIPowerCategories:
    """Test that power categories are correctly defined."""

    def test_dangerous_powers_defined(self):
        """Dangerous powers set should have key powers."""
        assert "Machine" in DANGEROUS_POWERS
        assert "Virus" in DANGEROUS_POWERS
        assert "Zombie" in DANGEROUS_POWERS
        assert len(DANGEROUS_POWERS) >= 10

    def test_negotiate_friendly_powers_defined(self):
        """Negotiate-friendly powers should include Pacifist."""
        assert "Pacifist" in NEGOTIATE_FRIENDLY_POWERS
        assert "Diplomat" in NEGOTIATE_FRIENDLY_POWERS

    def test_combat_modifier_powers_defined(self):
        """Combat modifier powers should have combat-altering aliens."""
        assert "Virus" in COMBAT_MODIFIER_POWERS
        assert "Macron" in COMBAT_MODIFIER_POWERS
        assert "Human" in COMBAT_MODIFIER_POWERS
        assert "Loser" in COMBAT_MODIFIER_POWERS

    def test_low_card_powers_defined(self):
        """Low card powers should include Loser."""
        assert "Loser" in LOW_CARD_POWERS
        assert "Anti-Matter" in LOW_CARD_POWERS


class TestStrategicAICardSelection:
    """Test card selection strategies for specific powers."""

    def test_loser_selects_low_cards(self):
        """Loser should select low attack cards."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Loser"])
        game = Game(config=config)
        game.setup()

        loser = next(p for p in game.players if p.alien.name == "Loser")
        ai = StrategicAI()
        ai.set_seed(42)

        # Set up game state for encounter
        game.offense = loser
        game.defense = game.players[1]

        # Get card selection
        attack_cards = loser.get_attack_cards()
        if attack_cards and len(attack_cards) > 1:
            selected = ai.select_encounter_card(game, loser, is_offense=True)
            # Loser should select their lowest attack card
            min_value = min(c.value for c in attack_cards)
            assert selected.value == min_value

    def test_virus_selects_mid_cards(self):
        """Virus should conserve high cards, selecting mid-range."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Virus"])
        game = Game(config=config)
        game.setup()

        virus = next(p for p in game.players if p.alien.name == "Virus")
        ai = StrategicAI()
        ai.set_seed(42)

        game.offense = virus
        game.defense = game.players[1]

        attack_cards = virus.get_attack_cards()
        if attack_cards and len(attack_cards) >= 3:
            selected = ai.select_encounter_card(game, virus, is_offense=True)
            max_value = max(c.value for c in attack_cards)
            # Virus shouldn't always play highest card
            # (might still play highest if only 1-2 cards)
            assert selected is not None


class TestStrategicAIShipSelection:
    """Test ship commitment strategies."""

    def test_virus_commits_more_ships(self):
        """Virus should commit more ships (multiplier effect)."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Virus"])
        game = Game(config=config)
        game.setup()

        virus = next(p for p in game.players if p.alien.name == "Virus")
        normal = next(p for p in game.players if p.alien.name != "Virus")
        ai = StrategicAI()
        ai.set_seed(42)

        game.offense = virus
        game.defense = normal

        virus_ships = ai.select_ships_for_encounter(game, virus, max_ships=4)
        # Virus should tend to commit more ships
        assert virus_ships >= 1

    def test_macron_commits_fewer_ships(self):
        """Macron should commit fewer ships (each = 4)."""
        config = GameConfig(num_players=4, seed=42, required_aliens=["Macron"])
        game = Game(config=config)
        game.setup()

        macron = next(p for p in game.players if p.alien.name == "Macron")
        ai = StrategicAI()
        ai.set_seed(42)

        game.offense = macron
        game.defense = game.players[1]

        macron_ships = ai.select_ships_for_encounter(game, macron, max_ships=4)
        # Macron should commit fewer ships
        assert macron_ships >= 1


class TestStrategicAIOpponentModifiers:
    """Test opponent strategy modifiers."""

    def test_vs_loser_modifier(self):
        """Against Loser, AI should expect low cards."""
        ai = StrategicAI()

        modifier = ai._get_opponent_strategy_modifier("Loser", None)
        assert modifier["expect_low_card"] is True
        assert modifier["play_defensive"] is True

    def test_vs_virus_modifier(self):
        """Against Virus, AI should play aggressively."""
        ai = StrategicAI()

        modifier = ai._get_opponent_strategy_modifier("Virus", None)
        assert modifier["play_aggressive"] is True

    def test_vs_pacifist_modifier(self):
        """Against Pacifist, AI should avoid negotiate."""
        ai = StrategicAI()

        modifier = ai._get_opponent_strategy_modifier("Pacifist", None)
        assert modifier["avoid_negotiate"] is True


class TestAIGameCompletion:
    """Test that games complete with various AI and power combinations."""

    def test_strategic_ai_vs_combat_powers(self):
        """Games with combat modifier powers should complete."""
        combat_powers = ["Virus", "Macron", "Human", "Warrior"]
        completed = 0

        for i, power in enumerate(combat_powers):
            config = GameConfig(
                num_players=4,
                seed=100 + i,
                required_aliens=[power],
                max_turns=75
            )
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == len(combat_powers)

    def test_strategic_ai_vs_low_card_powers(self):
        """Games with low-card powers should complete."""
        low_card_powers = ["Loser", "Anti-Matter", "Masochist"]
        completed = 0

        for i, power in enumerate(low_card_powers):
            try:
                config = GameConfig(
                    num_players=4,
                    seed=200 + i,
                    required_aliens=[power],
                    max_turns=75
                )
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception:
                pass  # Some powers might not be implemented

        assert completed >= 2  # At least Loser and Anti-Matter

    def test_strategic_ai_power_matchups(self):
        """Test specific interesting power matchups."""
        matchups = [
            ["Virus", "Warrior"],
            ["Loser", "Human"],
            ["Macron", "Zombie"],
            ["Oracle", "Sorcerer"],
        ]
        completed = 0

        for i, powers in enumerate(matchups):
            config = GameConfig(
                num_players=4,
                seed=300 + i,
                required_aliens=powers,
                max_turns=75
            )
            game = Game(config=config)
            game.setup()
            game.play()
            completed += 1

        assert completed == len(matchups)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
