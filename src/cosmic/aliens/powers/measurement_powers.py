"""
Measurement themed alien powers for Cosmic Encounter.
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
class Meter(AlienPower):
    """Meter - Power of Distance."""
    name: str = field(default="Meter", init=False)
    description: str = field(default="+1 for each planet between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gram(AlienPower):
    """Gram - Power of Weight."""
    name: str = field(default="Gram", init=False)
    description: str = field(default="Heavy cards (20+) count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Liter(AlienPower):
    """Liter - Power of Volume."""
    name: str = field(default="Liter", init=False)
    description: str = field(default="+2 for each ship over 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Second_Measure(AlienPower):
    """Second - Power of Time."""
    name: str = field(default="Second_Measure", init=False)
    description: str = field(default="Act twice per phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Degree_Measure(AlienPower):
    """Degree - Power of Angle."""
    name: str = field(default="Degree_Measure", init=False)
    description: str = field(default="Change encounter direction.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Volt(AlienPower):
    """Volt - Power of Energy."""
    name: str = field(default="Volt", init=False)
    description: str = field(default="+3 when using artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Watt(AlienPower):
    """Watt - Power of Output."""
    name: str = field(default="Watt", init=False)
    description: str = field(default="Power increases with each use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hertz(AlienPower):
    """Hertz - Power of Frequency."""
    name: str = field(default="Hertz", init=False)
    description: str = field(default="Use power every other turn at +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kelvin(AlienPower):
    """Kelvin - Power of Temperature."""
    name: str = field(default="Kelvin", init=False)
    description: str = field(default="Freeze opponent's power for one turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Pascal(AlienPower):
    """Pascal - Power of Pressure."""
    name: str = field(default="Pascal", init=False)
    description: str = field(default="Force opponent to play specific card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Meter())
AlienRegistry.register(Gram())
AlienRegistry.register(Liter())
AlienRegistry.register(Second_Measure())
AlienRegistry.register(Degree_Measure())
AlienRegistry.register(Volt())
AlienRegistry.register(Watt())
AlienRegistry.register(Hertz())
AlienRegistry.register(Kelvin())
AlienRegistry.register(Pascal())
