"""
Hunting themed alien powers for Cosmic Encounter.
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
class Hunter_Hunt(AlienPower):
    """Hunter - Power of Pursuit."""
    name: str = field(default="Hunter_Hunt", init=False)
    description: str = field(default="+3 when targeting same player twice.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tracker(AlienPower):
    """Tracker - Power of Following."""
    name: str = field(default="Tracker", init=False)
    description: str = field(default="Know destiny card before drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trapper_Hunt(AlienPower):
    """Trapper - Power of Snares."""
    name: str = field(default="Trapper_Hunt", init=False)
    description: str = field(default="Place traps on planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Archer(AlienPower):
    """Archer - Power of Range."""
    name: str = field(default="Archer", init=False)
    description: str = field(default="Attack non-adjacent planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stalker_Hunt(AlienPower):
    """Stalker - Power of Patience."""
    name: str = field(default="Stalker_Hunt", init=False)
    description: str = field(default="+4 after waiting one turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Poacher(AlienPower):
    """Poacher - Power of Theft."""
    name: str = field(default="Poacher", init=False)
    description: str = field(default="Take one ship from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Falconer(AlienPower):
    """Falconer - Power of Scouts."""
    name: str = field(default="Falconer", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Houndmaster(AlienPower):
    """Houndmaster - Power of Pack."""
    name: str = field(default="Houndmaster", init=False)
    description: str = field(default="+1 per ship over 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gamekeeper(AlienPower):
    """Gamekeeper - Power of Protection."""
    name: str = field(default="Gamekeeper", init=False)
    description: str = field(default="Protect one planet from attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Marksman(AlienPower):
    """Marksman - Power of Precision."""
    name: str = field(default="Marksman", init=False)
    description: str = field(default="+5 when attacking with 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Hunter_Hunt())
AlienRegistry.register(Tracker())
AlienRegistry.register(Trapper_Hunt())
AlienRegistry.register(Archer())
AlienRegistry.register(Stalker_Hunt())
AlienRegistry.register(Poacher())
AlienRegistry.register(Falconer())
AlienRegistry.register(Houndmaster())
AlienRegistry.register(Gamekeeper())
AlienRegistry.register(Marksman())
