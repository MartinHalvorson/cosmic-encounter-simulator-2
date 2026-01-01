"""
Furniture themed alien powers for Cosmic Encounter.
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
class Chair(AlienPower):
    """Chair - Power of Rest."""
    name: str = field(default="Chair", init=False)
    description: str = field(default="Retrieve 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Table(AlienPower):
    """Table - Power of Gathering."""
    name: str = field(default="Table", init=False)
    description: str = field(default="All allies on your side get +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bed(AlienPower):
    """Bed - Power of Comfort."""
    name: str = field(default="Bed", init=False)
    description: str = field(default="+3 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sofa(AlienPower):
    """Sofa - Power of Relaxation."""
    name: str = field(default="Sofa", init=False)
    description: str = field(default="May skip encounter to draw 2 cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Desk(AlienPower):
    """Desk - Power of Work."""
    name: str = field(default="Desk", init=False)
    description: str = field(default="Look at top 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bookshelf(AlienPower):
    """Bookshelf - Power of Knowledge."""
    name: str = field(default="Bookshelf", init=False)
    description: str = field(default="Draw 1 extra card at start of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cabinet(AlienPower):
    """Cabinet - Power of Storage."""
    name: str = field(default="Cabinet", init=False)
    description: str = field(default="Set aside 1 card; retrieve it later.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lamp(AlienPower):
    """Lamp - Power of Light."""
    name: str = field(default="Lamp", init=False)
    description: str = field(default="See opponent's card before playing yours.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Clock_Furniture(AlienPower):
    """Clock - Power of Time."""
    name: str = field(default="Clock_Furniture", init=False)
    description: str = field(default="+1 for each turn passed (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mirror_Furniture(AlienPower):
    """Mirror - Power of Reflection."""
    name: str = field(default="Mirror_Furniture", init=False)
    description: str = field(default="Copy opponent's card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Chair())
AlienRegistry.register(Table())
AlienRegistry.register(Bed())
AlienRegistry.register(Sofa())
AlienRegistry.register(Desk())
AlienRegistry.register(Bookshelf())
AlienRegistry.register(Cabinet())
AlienRegistry.register(Lamp())
AlienRegistry.register(Clock_Furniture())
AlienRegistry.register(Mirror_Furniture())
