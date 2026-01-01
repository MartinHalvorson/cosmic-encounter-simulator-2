"""
Age Powers - Aliens with age and life-stage abilities.
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
class Ancient_Alt(AlienPower):
    """
    Ancient_Alt - Very Old.
    +1 per turn played.
    """
    name: str = field(default="Ancient_Alt", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Child(AlienPower):
    """
    Child - Young One.
    Extra growth potential.
    """
    name: str = field(default="Child", init=False)
    description: str = field(default="Growth bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Elderly(AlienPower):
    """
    Elderly - Wise Old.
    See outcomes.
    """
    name: str = field(default="Elderly", init=False)
    description: str = field(default="See outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Infant(AlienPower):
    """
    Infant - Newborn.
    Protected by others.
    """
    name: str = field(default="Infant", init=False)
    description: str = field(default="Extra protection.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mature(AlienPower):
    """
    Mature - Full Grown.
    +3 constant.
    """
    name: str = field(default="Mature", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 constant bonus."""
        return total + 3


@dataclass
class Midlife(AlienPower):
    """
    Midlife - Peak Power.
    Balanced strength.
    """
    name: str = field(default="Midlife", init=False)
    description: str = field(default="+2 balanced.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Teen(AlienPower):
    """
    Teen - Growing Up.
    Risk for reward.
    """
    name: str = field(default="Teen", init=False)
    description: str = field(default="Risk reward.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Toddler(AlienPower):
    """
    Toddler - Little One.
    Random bonus 0-4.
    """
    name: str = field(default="Toddler", init=False)
    description: str = field(default="Random 0-4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add random 0-4."""
        return total + random.randint(0, 4)


@dataclass
class Young(AlienPower):
    """
    Young - Youthful.
    Extra energy.
    """
    name: str = field(default="Young", init=False)
    description: str = field(default="Extra actions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Ancient_Alt())
AlienRegistry.register(Child())
AlienRegistry.register(Elderly())
AlienRegistry.register(Infant())
AlienRegistry.register(Mature())
AlienRegistry.register(Midlife())
AlienRegistry.register(Teen())
AlienRegistry.register(Toddler())
AlienRegistry.register(Young())
