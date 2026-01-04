"""
Base card classes for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from abc import ABC, abstractmethod

from ..types import CardType, ArtifactType

if TYPE_CHECKING:
    from ..player import Player


class Card(ABC):
    """Base class for all cards."""

    @property
    @abstractmethod
    def card_type(self) -> CardType:
        pass

    @property
    def from_rewards_deck(self) -> bool:
        return getattr(self, '_from_rewards_deck', False)

    @from_rewards_deck.setter
    def from_rewards_deck(self, value: bool) -> None:
        self._from_rewards_deck = value

    @abstractmethod
    def __str__(self) -> str:
        pass

    def is_encounter_card(self) -> bool:
        """Returns True if this card can be played as an encounter card."""
        return self.card_type in (CardType.ATTACK, CardType.NEGOTIATE, CardType.MORPH)


class EncounterCard(Card):
    """Base class for encounter cards (Attack, Negotiate, Morph)."""
    pass


@dataclass
class AttackCard(EncounterCard):
    """An attack card with a numeric value."""
    value: int
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.ATTACK, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    def __str__(self) -> str:
        return f"Attack {self.value}"

    def mirrored_value(self) -> int:
        """Returns the value when Mirror alien power is used (digits reversed).

        Per FFG rules, attack cards are displayed as two digits (00-40).
        Mirror swaps the tens and ones digits:
        - 06 becomes 60
        - 12 becomes 21
        - 40 becomes 04
        """
        # Handle negative values (from rewards deck) - just swap digits of absolute value
        if self.value < 0:
            abs_val = abs(self.value)
            tens = abs_val // 10
            ones = abs_val % 10
            return -(ones * 10 + tens)
        # For values 0-9, treat as 0X where X is the value, so swap gives X0
        tens = self.value // 10
        ones = self.value % 10
        return ones * 10 + tens


@dataclass
class NegotiateCard(EncounterCard):
    """A negotiate card (value 0 for combat, but triggers deal phase)."""
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.NEGOTIATE, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    @property
    def value(self) -> int:
        return 0

    def __str__(self) -> str:
        return "Negotiate"


@dataclass
class MorphCard(EncounterCard):
    """A morph card that copies the opponent's card."""
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.MORPH, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    @property
    def value(self) -> int:
        # Value is determined by opponent's card during resolution
        return 0

    def __str__(self) -> str:
        return "Morph"


@dataclass
class ReinforcementCard(Card):
    """A reinforcement card that adds to encounter totals."""
    value: int
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.REINFORCEMENT, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    def __str__(self) -> str:
        return f"Reinforcement +{self.value}"


@dataclass
class KickerCard(Card):
    """A kicker card that multiplies encounter card value."""
    value: int  # Can be negative (like -1) or positive multiplier
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.KICKER, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    def __str__(self) -> str:
        if self.value < 0:
            return f"Kicker x{self.value}"
        return f"Kicker x{self.value}"


@dataclass
class ArtifactCard(Card):
    """An artifact card with a special effect."""
    artifact_type: ArtifactType
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.ARTIFACT, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    def __str__(self) -> str:
        name = self.artifact_type.value.replace("_", " ").title()
        return f"Artifact: {name}"


@dataclass
class FlareCard(Card):
    """A flare card associated with an alien power."""
    alien_name: str
    # Wild effect can be used by anyone, super effect only by the matching alien
    wild_effect: str = ""
    super_effect: str = ""
    _from_rewards_deck: bool = False
    _card_type: CardType = field(default=CardType.FLARE, init=False)

    @property
    def card_type(self) -> CardType:
        return self._card_type

    def __str__(self) -> str:
        return f"Flare: {self.alien_name}"
