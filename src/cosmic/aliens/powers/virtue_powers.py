"""
Virtue Powers - Moral virtue-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Kindness(AlienPower):
    """Kindness - Power of Generosity. Help others."""
    name: str = field(default="Kindness", init=False)
    description: str = field(default="Give 1 card to any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Valor(AlienPower):
    """Valor - Power of Bravery. +5 when outnumbered."""
    name: str = field(default="Valor", init=False)
    description: str = field(default="+5 when facing more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Honesty(AlienPower):
    """Honesty - Power of Truth. Cards visible."""
    name: str = field(default="Honesty", init=False)
    description: str = field(default="All play cards face-up.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Loyalty(AlienPower):
    """Loyalty - Power of Devotion. +2 per ally."""
    name: str = field(default="Loyalty", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Charity(AlienPower):
    """Charity - Power of Giving. Draw cards, give some away."""
    name: str = field(default="Charity", init=False)
    description: str = field(default="Draw 3, give 1 away.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diligence(AlienPower):
    """Diligence - Power of Hard Work. Extra encounters."""
    name: str = field(default="Diligence", init=False)
    description: str = field(default="Take third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Temperance(AlienPower):
    """Temperance - Power of Moderation. +3 with medium cards."""
    name: str = field(default="Temperance", init=False)
    description: str = field(default="+3 when card is 8-12.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fortitude(AlienPower):
    """Fortitude - Power of Endurance. +4 on defense."""
    name: str = field(default="Fortitude", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Prudence(AlienPower):
    """Prudence - Power of Wisdom. See opponent card."""
    name: str = field(default="Prudence", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Integrity(AlienPower):
    """Integrity - Power of Wholeness. +3 always."""
    name: str = field(default="Integrity", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Compassion(AlienPower):
    """Compassion - Power of Sympathy. Reduce opponent losses."""
    name: str = field(default="Compassion", init=False)
    description: str = field(default="Opponent loses 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Humbleness(AlienPower):
    """Humbleness - Power of Modesty. +5 with low cards."""
    name: str = field(default="Humbleness", init=False)
    description: str = field(default="+5 when card is under 6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gratitude(AlienPower):
    """Gratitude - Power of Thanks. Draw on loss."""
    name: str = field(default="Gratitude", init=False)
    description: str = field(default="Draw 2 cards when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sincerity(AlienPower):
    """Sincerity - Power of Genuineness. Negotiate bonus."""
    name: str = field(default="Sincerity", init=False)
    description: str = field(default="+3 cards when dealing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Responsibility(AlienPower):
    """Responsibility - Power of Duty. Extra defense."""
    name: str = field(default="Responsibility", init=False)
    description: str = field(default="+3 when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
VIRTUE_POWERS = [
    Kindness, Valor, Honesty, Loyalty, Charity, Diligence, Temperance, Fortitude,
    Prudence, Integrity, Compassion, Humbleness, Gratitude, Sincerity, Responsibility,
]

for power_class in VIRTUE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
