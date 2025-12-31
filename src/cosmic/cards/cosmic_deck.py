"""
The Cosmic Deck - main draw pile for the game.
"""

import random
from typing import List, Optional
from dataclasses import dataclass, field

from .base import (
    Card, AttackCard, NegotiateCard, MorphCard,
    ReinforcementCard, ArtifactCard, FlareCard
)
from ..types import ArtifactType


@dataclass
class CosmicDeck:
    """
    The main cosmic deck containing attack cards, negotiates,
    reinforcements, and artifacts.
    """
    draw_pile: List[Card] = field(default_factory=list)
    discard_pile: List[Card] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if not self.draw_pile:
            self._initialize_deck()
            self.shuffle()

    def _initialize_deck(self) -> None:
        """Create the standard cosmic deck."""
        cards: List[Card] = []

        # Attack cards - standard distribution
        # Low cards (useful for Loser, but weak normally)
        attack_values = [
            0,  # x1 (Morph-like value)
            1,  # x1
            4, 4, 4, 4,  # x4
            5,  # x1
            6, 6, 6, 6, 6, 6, 6,  # x7
            7,  # x1
            8, 8, 8, 8, 8, 8, 8,  # x7
            9,  # x1
            10, 10, 10, 10,  # x4
            11,  # x1
            12, 12,  # x2
            13,  # x1
            14, 14,  # x2
            15,  # x1
            20, 20,  # x2
            23,  # x1
            30,  # x1
            40,  # x1
        ]

        for value in attack_values:
            cards.append(AttackCard(value=value))

        # Negotiate cards - 15 total
        for _ in range(15):
            cards.append(NegotiateCard())

        # Morph cards - 1 in base game (optional, adding 2)
        cards.append(MorphCard())
        cards.append(MorphCard())

        # Reinforcement cards
        reinforcement_values = [2, 2, 3, 3, 3, 5]
        for value in reinforcement_values:
            cards.append(ReinforcementCard(value=value))

        # Artifact cards
        artifact_counts = {
            ArtifactType.COSMIC_ZAP: 2,
            ArtifactType.CARD_ZAP: 2,
            ArtifactType.MOBIUS_TUBES: 2,
            ArtifactType.EMOTION_CONTROL: 1,
            ArtifactType.FORCE_FIELD: 1,
            ArtifactType.QUASH: 1,
            ArtifactType.IONIC_GAS: 1,
            ArtifactType.PLAGUE: 1,
        }

        for artifact_type, count in artifact_counts.items():
            for _ in range(count):
                cards.append(ArtifactCard(artifact_type=artifact_type))

        self.draw_pile = cards

    def shuffle(self) -> None:
        """Shuffle the draw pile."""
        self._rng.shuffle(self.draw_pile)

    def draw(self) -> Card:
        """Draw a card from the deck, reshuffling discard if needed."""
        if not self.draw_pile:
            self._reshuffle_discard()

        if not self.draw_pile:
            raise RuntimeError("No cards available in cosmic deck!")

        return self.draw_pile.pop()

    def draw_multiple(self, count: int) -> List[Card]:
        """Draw multiple cards."""
        return [self.draw() for _ in range(count)]

    def discard(self, card: Card) -> None:
        """Add a card to the discard pile."""
        self.discard_pile.append(card)

    def discard_multiple(self, cards: List[Card]) -> None:
        """Discard multiple cards."""
        self.discard_pile.extend(cards)

    def _reshuffle_discard(self) -> None:
        """Shuffle the discard pile back into the draw pile."""
        if self.discard_pile:
            self.draw_pile = self.discard_pile
            self.discard_pile = []
            self.shuffle()
        elif not self.draw_pile:
            # Emergency: both piles empty, regenerate basic cards
            # This can happen in edge cases with certain power combinations
            basic_cards = []
            for value in [6, 6, 8, 8, 10, 12, 14]:
                basic_cards.append(AttackCard(value=value))
            for _ in range(3):
                basic_cards.append(NegotiateCard())
            self.draw_pile = basic_cards
            self.shuffle()

    def peek(self, count: int = 1) -> List[Card]:
        """Look at the top cards without drawing them."""
        # Ensure we have enough cards
        while len(self.draw_pile) < count and self.discard_pile:
            self._reshuffle_discard()
        return self.draw_pile[-count:] if self.draw_pile else []

    def cards_remaining(self) -> int:
        """Number of cards in draw pile."""
        return len(self.draw_pile)

    def total_cards(self) -> int:
        """Total cards in deck (draw + discard)."""
        return len(self.draw_pile) + len(self.discard_pile)

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator for reproducibility."""
        self._rng = rng

    def add_flares(self, flares: List[FlareCard]) -> None:
        """Add flare cards to the deck and reshuffle."""
        self.draw_pile.extend(flares)
        self.shuffle()
