"""
Time of Day themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Dawn_Time(AlienPower):
    """Dawn - Power of Beginnings."""
    name: str = field(default="Dawn_Time", init=False)
    description: str = field(default="+4 on first encounter of game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Morning(AlienPower):
    """Morning - Power of Freshness."""
    name: str = field(default="Morning", init=False)
    description: str = field(default="Draw extra card at start of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Noon(AlienPower):
    """Noon - Power of Peak."""
    name: str = field(default="Noon", init=False)
    description: str = field(default="+3 when at exactly 3 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Afternoon(AlienPower):
    """Afternoon - Power of Routine."""
    name: str = field(default="Afternoon", init=False)
    description: str = field(default="+2 on consecutive wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dusk_Time(AlienPower):
    """Dusk - Power of Transition."""
    name: str = field(default="Dusk_Time", init=False)
    description: str = field(default="Switch offense/defense roles once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Evening(AlienPower):
    """Evening - Power of Winding Down."""
    name: str = field(default="Evening", init=False)
    description: str = field(default="Force encounter to end in draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Night(AlienPower):
    """Night - Power of Darkness."""
    name: str = field(default="Night", init=False)
    description: str = field(default="Cards played face-down until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Midnight_Time(AlienPower):
    """Midnight - Power of Witching Hour."""
    name: str = field(default="Midnight_Time", init=False)
    description: str = field(default="+5 when you have 0 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Twilight_Time(AlienPower):
    """Twilight - Power of In-Between."""
    name: str = field(default="Twilight_Time", init=False)
    description: str = field(default="Choose to use offense or defense power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sunrise(AlienPower):
    """Sunrise - Power of Hope."""
    name: str = field(default="Sunrise", init=False)
    description: str = field(default="Retrieve 2 ships from warp after losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Dawn_Time())
AlienRegistry.register(Morning())
AlienRegistry.register(Noon())
AlienRegistry.register(Afternoon())
AlienRegistry.register(Dusk_Time())
AlienRegistry.register(Evening())
AlienRegistry.register(Night())
AlienRegistry.register(Midnight_Time())
AlienRegistry.register(Twilight_Time())
AlienRegistry.register(Sunrise())
