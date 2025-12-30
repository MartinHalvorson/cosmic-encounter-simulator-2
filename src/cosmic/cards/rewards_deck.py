"""
The Rewards Deck - drawn as rewards for defensive allies.
"""

import random
from typing import List
from dataclasses import dataclass, field

from .base import (
    Card, AttackCard, NegotiateCard,
    ReinforcementCard, ArtifactCard, KickerCard
)
from ..types import ArtifactType


@dataclass
class RewardsDeck:
    """
    The rewards deck contains special cards for defensive ally rewards.
    Generally has stronger cards than the cosmic deck.
    """
    draw_pile: List[Card] = field(default_factory=list)
    discard_pile: List[Card] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def __post_init__(self):
        if not self.draw_pile:
            self._initialize_deck()
            self.shuffle()

    def _initialize_deck(self) -> None:
        """Create the rewards deck."""
        cards: List[Card] = []

        # Attack cards - generally higher values, includes negative
        attack_values = [-7, -1, 10, 12, 14, 16, 18, 20, 23]
        for value in attack_values:
            cards.append(AttackCard(value=value, _from_rewards_deck=True))

        # Negotiate cards (can be special negotiates in expansions)
        for _ in range(4):
            cards.append(NegotiateCard(_from_rewards_deck=True))

        # Reinforcement cards - higher values
        reinforcement_values = [4, 4, 6, 6]
        for value in reinforcement_values:
            cards.append(ReinforcementCard(value=value, _from_rewards_deck=True))

        # Kicker cards
        kicker_values = [-1, 0, 1, 2, 2, 3, 4]
        for value in kicker_values:
            cards.append(KickerCard(value=value, _from_rewards_deck=True))

        # Artifacts (powerful ones)
        reward_artifacts = [
            ArtifactType.COSMIC_ZAP,
            ArtifactType.CARD_ZAP,
            ArtifactType.OMNI_ZAP,
            ArtifactType.SOLAR_WIND,
            ArtifactType.REBIRTH,
            ArtifactType.SHIP_ZAP,
            ArtifactType.HAND_ZAP,
            ArtifactType.SPACE_JUNK,
            ArtifactType.VICTORY_BOON,
        ]
        for artifact_type in reward_artifacts:
            cards.append(ArtifactCard(
                artifact_type=artifact_type,
                _from_rewards_deck=True
            ))

        self.draw_pile = cards

    def shuffle(self) -> None:
        """Shuffle the draw pile."""
        self._rng.shuffle(self.draw_pile)

    def draw(self) -> Card:
        """Draw a card from the deck, reshuffling discard if needed."""
        if not self.draw_pile:
            self._reshuffle_discard()

        if not self.draw_pile:
            # If deck is completely empty, regenerate it
            # This can happen if all cards are in player hands
            self._initialize_deck()
            self.shuffle()

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
        if not self.discard_pile:
            return
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        self.shuffle()

    def cards_remaining(self) -> int:
        """Number of cards in draw pile."""
        return len(self.draw_pile)

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator for reproducibility."""
        self._rng = rng
