"""
Extreme Weather themed alien powers for Cosmic Encounter.
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
class Hurricane(AlienPower):
    """Hurricane - Power of Chaos."""
    name: str = field(default="Hurricane", init=False)
    description: str = field(
        default="Randomly redistribute ships after encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Blizzard(AlienPower):
    """Blizzard - Power of Cold."""
    name: str = field(default="Blizzard", init=False)
    description: str = field(
        default="Freeze opponent's ships: they can't ally next turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Heatwave(AlienPower):
    """Heatwave - Power of Heat."""
    name: str = field(default="Heatwave", init=False)
    description: str = field(
        default="+3 when playing attack cards 15 or higher.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tsunami(AlienPower):
    """Tsunami - Power of Waves."""
    name: str = field(default="Tsunami", init=False)
    description: str = field(
        default="When winning offense, sweep all ships off planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Earthquake(AlienPower):
    """Earthquake - Power of Tremors."""
    name: str = field(default="Earthquake", init=False)
    description: str = field(
        default="All planets lose 1 ship each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Drought(AlienPower):
    """Drought - Power of Scarcity."""
    name: str = field(default="Drought", init=False)
    description: str = field(
        default="Opponents draw 1 fewer card each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tornado(AlienPower):
    """Tornado - Power of Spinning."""
    name: str = field(default="Tornado", init=False)
    description: str = field(
        default="Swap positions of 2 ships after reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Avalanche(AlienPower):
    """Avalanche - Power of Momentum."""
    name: str = field(default="Avalanche", init=False)
    description: str = field(
        default="+1 for each ship over 4 in the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flood(AlienPower):
    """Flood - Power of Rising Waters."""
    name: str = field(default="Flood", init=False)
    description: str = field(
        default="Ships from warp return to any colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wildfire(AlienPower):
    """Wildfire - Power of Spreading."""
    name: str = field(default="Wildfire", init=False)
    description: str = field(
        default="When winning, also attack adjacent planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monsoon(AlienPower):
    """Monsoon - Power of Seasons."""
    name: str = field(default="Monsoon", init=False)
    description: str = field(
        default="+4 on turns divisible by 3.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sandstorm(AlienPower):
    """Sandstorm - Power of Obscuring."""
    name: str = field(default="Sandstorm", init=False)
    description: str = field(
        default="Prevent opponent from using reinforcements.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Hurricane())
AlienRegistry.register(Blizzard())
AlienRegistry.register(Heatwave())
AlienRegistry.register(Tsunami())
AlienRegistry.register(Earthquake())
AlienRegistry.register(Drought())
AlienRegistry.register(Tornado())
AlienRegistry.register(Avalanche())
AlienRegistry.register(Flood())
AlienRegistry.register(Wildfire())
AlienRegistry.register(Monsoon())
AlienRegistry.register(Sandstorm())
