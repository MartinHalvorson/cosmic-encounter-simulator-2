"""
Natural Disaster themed alien powers for Cosmic Encounter.
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
class Earthquake_Disaster(AlienPower):
    """Earthquake - Power of Destruction."""
    name: str = field(default="Earthquake_Disaster", init=False)
    description: str = field(default="All ships on planet go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tsunami_Disaster(AlienPower):
    """Tsunami - Power of Waves."""
    name: str = field(default="Tsunami_Disaster", init=False)
    description: str = field(default="Push ships to adjacent planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tornado_Disaster(AlienPower):
    """Tornado - Power of Spinning."""
    name: str = field(default="Tornado_Disaster", init=False)
    description: str = field(default="Scatter opponent's ships randomly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hurricane_Disaster(AlienPower):
    """Hurricane - Power of Storms."""
    name: str = field(default="Hurricane_Disaster", init=False)
    description: str = field(default="+5 but lose 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wildfire_Disaster(AlienPower):
    """Wildfire - Power of Spreading."""
    name: str = field(default="Wildfire_Disaster", init=False)
    description: str = field(default="Damage spreads to adjacent planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Flood_Disaster(AlienPower):
    """Flood - Power of Rising Waters."""
    name: str = field(default="Flood_Disaster", init=False)
    description: str = field(default="Remove all low-value cards from play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Avalanche_Disaster(AlienPower):
    """Avalanche - Power of Momentum."""
    name: str = field(default="Avalanche_Disaster", init=False)
    description: str = field(default="+2 for each consecutive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drought_Disaster(AlienPower):
    """Drought - Power of Scarcity."""
    name: str = field(default="Drought_Disaster", init=False)
    description: str = field(default="Opponents draw 1 fewer card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sinkhole(AlienPower):
    """Sinkhole - Power of Swallowing."""
    name: str = field(default="Sinkhole", init=False)
    description: str = field(default="Ships fall into trap on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Heatwave(AlienPower):
    """Heatwave - Power of Heat."""
    name: str = field(default="Heatwave", init=False)
    description: str = field(default="+3 during summer turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blizzard_Disaster(AlienPower):
    """Blizzard - Power of Cold."""
    name: str = field(default="Blizzard_Disaster", init=False)
    description: str = field(default="Freeze one opponent's ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sandstorm(AlienPower):
    """Sandstorm - Power of Obscurity."""
    name: str = field(default="Sandstorm", init=False)
    description: str = field(default="Hide your ship count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Earthquake_Disaster())
AlienRegistry.register(Tsunami_Disaster())
AlienRegistry.register(Tornado_Disaster())
AlienRegistry.register(Hurricane_Disaster())
AlienRegistry.register(Wildfire_Disaster())
AlienRegistry.register(Flood_Disaster())
AlienRegistry.register(Avalanche_Disaster())
AlienRegistry.register(Drought_Disaster())
AlienRegistry.register(Sinkhole())
AlienRegistry.register(Heatwave())
AlienRegistry.register(Blizzard_Disaster())
AlienRegistry.register(Sandstorm())
