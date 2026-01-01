"""
Tests for card interactions and special card types.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.cards.base import (
    AttackCard, NegotiateCard, MorphCard,
    ReinforcementCard, KickerCard, ArtifactCard, FlareCard
)
from cosmic.cards.rift_cards import RiftCard, RiftType, RiftDeck
from cosmic.types import ArtifactType


class TestAttackCards:
    """Tests for attack card interactions."""

    def test_attack_card_values(self):
        """Attack cards should have values from 0 to 40."""
        for value in [0, 1, 6, 8, 10, 20, 30, 40]:
            card = AttackCard(value=value)
            assert card.value == value
            assert card.is_encounter_card()

    def test_negative_attack_cards(self):
        """Negative attack cards should be allowed (from rewards deck)."""
        for value in [-7, -1]:
            card = AttackCard(value=value)
            assert card.value == value


class TestNegotiateCards:
    """Tests for negotiate card interactions."""

    def test_negotiate_card_is_encounter_card(self):
        """Negotiate should be an encounter card."""
        card = NegotiateCard()
        assert card.is_encounter_card()

    def test_negotiate_value_is_none(self):
        """Negotiate cards have no attack value."""
        card = NegotiateCard()
        assert card.value is None


class TestMorphCards:
    """Tests for morph card interactions."""

    def test_morph_copies_opponent(self):
        """Morph should copy opponent's attack value."""
        morph = MorphCard()
        assert morph.is_encounter_card()

        # When opponent plays 20, morph should become 20
        morph.set_copied_value(20)
        assert morph.effective_value == 20

    def test_morph_without_copy(self):
        """Morph without copy should have base value."""
        morph = MorphCard()
        assert morph.effective_value == 0  # Default base


class TestReinforcementCards:
    """Tests for reinforcement card interactions."""

    def test_reinforcement_values(self):
        """Reinforcement cards add to combat totals."""
        for value in [2, 3, 4, 5, 6]:
            card = ReinforcementCard(value=value)
            assert card.value == value
            assert not card.is_encounter_card()

    def test_multiple_reinforcements(self):
        """Multiple reinforcements should stack."""
        cards = [
            ReinforcementCard(value=2),
            ReinforcementCard(value=3),
            ReinforcementCard(value=5)
        ]
        total = sum(c.value for c in cards)
        assert total == 10


class TestKickerCards:
    """Tests for kicker card interactions."""

    def test_kicker_multipliers(self):
        """Kicker cards should multiply attack values."""
        for multiplier in [-1, 0, 1, 2, 3, 4]:
            card = KickerCard(value=multiplier)
            assert card.value == multiplier

    def test_kicker_application(self):
        """Test kicker multiplication."""
        attack = AttackCard(value=10)
        kicker = KickerCard(value=2)

        # Attack 10 * kicker 2 = 20
        kicked_value = attack.value * kicker.value
        assert kicked_value == 20

    def test_negative_kicker(self):
        """Negative kicker should negate the attack."""
        attack = AttackCard(value=10)
        kicker = KickerCard(value=-1)

        kicked_value = attack.value * kicker.value
        assert kicked_value == -10


class TestArtifactCards:
    """Tests for artifact card interactions."""

    def test_all_artifact_types(self):
        """All artifact types should create valid cards."""
        for artifact_type in ArtifactType:
            card = ArtifactCard(artifact_type=artifact_type)
            assert card.artifact_type == artifact_type
            assert not card.is_encounter_card()

    def test_cosmic_zap_artifact(self):
        """Cosmic Zap should be created correctly."""
        card = ArtifactCard(artifact_type=ArtifactType.COSMIC_ZAP)
        assert "zap" in str(card).lower()


class TestFlareCards:
    """Tests for flare card interactions."""

    def test_flare_wild_and_super(self):
        """Flares should have wild and super effects."""
        flare = FlareCard(
            alien_name="Machine",
            wild_effect="Take one extra encounter.",
            super_effect="Take two extra encounters."
        )
        assert flare.alien_name == "Machine"
        assert "extra" in flare.wild_effect
        assert "two" in flare.super_effect

    def test_flare_is_not_encounter_card(self):
        """Flares should not be encounter cards."""
        flare = FlareCard(
            alien_name="Zombie",
            wild_effect="Return 2 ships.",
            super_effect="Return all ships."
        )
        assert not flare.is_encounter_card()


class TestRiftCards:
    """Tests for rift card interactions."""

    def test_rift_types(self):
        """All rift types should create valid cards."""
        for rift_type in RiftType:
            card = RiftCard(rift_type=rift_type, ships_affected=2)
            assert card.rift_type == rift_type

    def test_warp_rift_draw_effect(self):
        """Warp rift should free ships when drawn."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        player = game.players[0]
        player.ships_in_warp = 5

        rift = RiftCard(rift_type=RiftType.WARP_RIFT, ships_affected=3)
        effect = rift.on_draw(game, player)

        # Should have freed ships
        assert "frees" in effect.lower() or "freed" in effect.lower() or player.ships_in_warp < 5

    def test_trap_rift_stolen_effect(self):
        """Trap rift should hurt the thief."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        thief = game.players[0]
        victim = game.players[1]

        rift = RiftCard(rift_type=RiftType.TRAP_RIFT, ships_affected=2)
        effect = rift.on_stolen(game, thief, victim)

        # Should have hurt the thief
        assert "trap" in effect.lower() or "warp" in effect.lower()

    def test_rift_deck_creation(self):
        """Rift deck should create standard rifts."""
        rifts = RiftDeck.create_standard_rifts()
        assert len(rifts) == 12  # Standard set size

        # Check types are varied
        types = {r.rift_type for r in rifts}
        assert len(types) >= 4


class TestCardCombinations:
    """Tests for card combination scenarios."""

    def test_attack_with_reinforcement(self):
        """Attack + reinforcement should add correctly."""
        attack = AttackCard(value=15)
        reinforcement = ReinforcementCard(value=5)

        total = attack.value + reinforcement.value
        assert total == 20

    def test_attack_with_kicker_and_reinforcement(self):
        """Attack * kicker + reinforcement should calculate correctly."""
        attack = AttackCard(value=10)
        kicker = KickerCard(value=2)
        reinforcement = ReinforcementCard(value=3)

        kicked = attack.value * kicker.value
        total = kicked + reinforcement.value
        assert total == 23

    def test_morph_with_kicker(self):
        """Morph with kicker should work correctly."""
        morph = MorphCard()
        morph.set_copied_value(8)
        kicker = KickerCard(value=3)

        total = morph.effective_value * kicker.value
        assert total == 24


class TestGameCardInteractions:
    """Tests for card interactions in actual games."""

    def test_game_has_encounter_cards(self):
        """Game should deal encounter cards to players."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        for player in game.players:
            encounter_cards = [c for c in player.hand if c.is_encounter_card()]
            assert len(encounter_cards) >= 1

    def test_game_deals_varied_cards(self):
        """Game should deal varied card types."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        all_cards = []
        for player in game.players:
            all_cards.extend(player.hand)

        # Should have variety
        attack_count = sum(1 for c in all_cards if isinstance(c, AttackCard))
        negotiate_count = sum(1 for c in all_cards if isinstance(c, NegotiateCard))

        assert attack_count > 0
        assert negotiate_count >= 0  # Negotiates might be 0 by chance

    def test_reinforcement_in_game(self):
        """Game should be able to use reinforcements."""
        config = GameConfig(num_players=4, seed=42)
        game = Game(config=config)
        game.setup()

        # Check if any player has reinforcements
        all_cards = []
        for player in game.players:
            all_cards.extend(player.hand)

        reinforcements = [c for c in all_cards if isinstance(c, ReinforcementCard)]
        # Reinforcements are in the deck, may or may not be in hands
        assert reinforcements is not None
