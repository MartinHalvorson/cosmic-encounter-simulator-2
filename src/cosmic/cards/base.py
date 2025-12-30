"""
Base card classes for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from abc import ABC, abstractmethod

from ..types import CardType, ArtifactType

if TYPE_CHECKING:
    from ..player import Player


@dataclass
class Card(ABC):
    """Base class for all cards."""
    card_type: CardType
    from_rewards_deck: bool = False

    @abstractmethod
    def __str__(self) -> str:
        pass

    def is_encounter_card(self) -> bool:
        """Returns True if this card can be played as an encounter card."""
        return self.card_type in (CardType.ATTACK, CardType.NEGOTIATE, CardType.MORPH)


@dataclass
class EncounterCard(Card):
    """Base class for encounter cards (Attack, Negotiate, Morph)."""
    pass


@dataclass
class AttackCard(EncounterCard):
    """An attack card with a numeric value."""
    value: int
    card_type: CardType = field(default=CardType.ATTACK, init=False)

    def __str__(self) -> str:
        return f"Attack {self.value}"

    def mirrored_value(self) -> int:
        """Returns the value when Mirror alien power is used (digits reversed)."""
        if self.value < 10:
            return self.value * 10
        tens = self.value // 10
        ones = self.value % 10
        return ones * 10 + tens


@dataclass
class NegotiateCard(EncounterCard):
    """A negotiate card (value 0 for combat, but triggers deal phase)."""
    card_type: CardType = field(default=CardType.NEGOTIATE, init=False)

    @property
    def value(self) -> int:
        return 0

    def __str__(self) -> str:
        return "Negotiate"


@dataclass
class MorphCard(EncounterCard):
    """A morph card that copies the opponent's card."""
    card_type: CardType = field(default=CardType.MORPH, init=False)

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
    card_type: CardType = field(default=CardType.REINFORCEMENT, init=False)

    def __str__(self) -> str:
        return f"Reinforcement +{self.value}"


@dataclass
class KickerCard(Card):
    """A kicker card that multiplies encounter card value."""
    value: int  # Can be negative (like -1) or positive multiplier
    card_type: CardType = field(default=CardType.KICKER, init=False)

    def __str__(self) -> str:
        if self.value < 0:
            return f"Kicker x{self.value}"
        return f"Kicker x{self.value}"


@dataclass
class ArtifactCard(Card):
    """An artifact card with a special effect."""
    artifact_type: ArtifactType
    card_type: CardType = field(default=CardType.ARTIFACT, init=False)

    def __str__(self) -> str:
        name = self.artifact_type.value.replace("_", " ").title()
        return f"Artifact: {name}"


@dataclass
class FlareCard(Card):
    """A flare card associated with an alien power."""
    alien_name: str
    card_type: CardType = field(default=CardType.FLARE, init=False)
    # Wild effect can be used by anyone, super effect only by the matching alien
    wild_effect: str = ""
    super_effect: str = ""

    def __str__(self) -> str:
        return f"Flare: {self.alien_name}"
