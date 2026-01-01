"""
Cooking Powers - Aliens with culinary and preparation abilities.
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
class Baker_Alt(AlienPower):
    """
    Baker_Alt - Make Bread.
    +1 per card.
    """
    name: str = field(default="Baker_Alt", init=False)
    description: str = field(default="+1 per card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brewer(AlienPower):
    """
    Brewer - Make Drinks.
    Combine effects.
    """
    name: str = field(default="Brewer", init=False)
    description: str = field(default="Combine effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chef_Alt(AlienPower):
    """
    Chef_Alt - Master Cook.
    +3 with ingredients.
    """
    name: str = field(default="Chef_Alt", init=False)
    description: str = field(default="+3 with cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 with cards."""
        return total + 3


@dataclass
class Grill(AlienPower):
    """
    Grill - Hot Cooking.
    Burn opponent cards.
    """
    name: str = field(default="Grill", init=False)
    description: str = field(default="Burn cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mixer(AlienPower):
    """
    Mixer - Blend Together.
    Combine totals.
    """
    name: str = field(default="Mixer", init=False)
    description: str = field(default="Blend totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Roaster(AlienPower):
    """
    Roaster - Slow Cook.
    +2 over time.
    """
    name: str = field(default="Roaster", init=False)
    description: str = field(default="+2 gradual.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seasoner(AlienPower):
    """
    Seasoner - Add Flavor.
    Enhance ally power.
    """
    name: str = field(default="Seasoner", init=False)
    description: str = field(default="Enhance ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Slicer(AlienPower):
    """
    Slicer - Cut Precise.
    Reduce opponent.
    """
    name: str = field(default="Slicer", init=False)
    description: str = field(default="Cut opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Steamer(AlienPower):
    """
    Steamer - Steam Cook.
    Slow steady bonus.
    """
    name: str = field(default="Steamer", init=False)
    description: str = field(default="Steady +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Taster(AlienPower):
    """
    Taster - Sample First.
    See opponent card.
    """
    name: str = field(default="Taster", init=False)
    description: str = field(default="See card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Baker_Alt())
AlienRegistry.register(Brewer())
AlienRegistry.register(Chef_Alt())
AlienRegistry.register(Grill())
AlienRegistry.register(Mixer())
AlienRegistry.register(Roaster())
AlienRegistry.register(Seasoner())
AlienRegistry.register(Slicer())
AlienRegistry.register(Steamer())
AlienRegistry.register(Taster())
