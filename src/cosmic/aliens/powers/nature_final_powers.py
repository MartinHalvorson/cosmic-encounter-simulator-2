"""
Final Nature themed alien powers for Cosmic Encounter.
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
class River_Nature(AlienPower):
    """River - Power of Flow."""
    name: str = field(default="River_Nature", init=False)
    description: str = field(default="Ships move to adjacent colonies when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mountain_Nature(AlienPower):
    """Mountain - Power of Height."""
    name: str = field(default="Mountain_Nature", init=False)
    description: str = field(default="+4 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Forest_Nature(AlienPower):
    """Forest - Power of Concealment."""
    name: str = field(default="Forest_Nature", init=False)
    description: str = field(default="Your ship count is hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Desert_Nature(AlienPower):
    """Desert - Power of Scarcity."""
    name: str = field(default="Desert_Nature", init=False)
    description: str = field(default="Opponents draw 1 fewer card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Valley(AlienPower):
    """Valley - Power of Gathering."""
    name: str = field(default="Valley", init=False)
    description: str = field(default="Invite 2 extra allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Volcano_Nature(AlienPower):
    """Volcano - Power of Eruption."""
    name: str = field(default="Volcano_Nature", init=False)
    description: str = field(default="When losing, all ships on planet go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Waterfall(AlienPower):
    """Waterfall - Power of Cascade."""
    name: str = field(default="Waterfall", init=False)
    description: str = field(default="Cards played cascade to next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cave_Nature(AlienPower):
    """Cave - Power of Shelter."""
    name: str = field(default="Cave_Nature", init=False)
    description: str = field(default="Ships survive one extra loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cliff(AlienPower):
    """Cliff - Power of Edges."""
    name: str = field(default="Cliff", init=False)
    description: str = field(default="+3 when winning by exactly 1-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swamp(AlienPower):
    """Swamp - Power of Trapping."""
    name: str = field(default="Swamp", init=False)
    description: str = field(default="Opponent's ships can't retreat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Island_Nature(AlienPower):
    """Island - Power of Isolation."""
    name: str = field(default="Island_Nature", init=False)
    description: str = field(default="Home planets can't be invaded for 2 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Glacier(AlienPower):
    """Glacier - Power of Slowness."""
    name: str = field(default="Glacier", init=False)
    description: str = field(default="Slow but inevitable: +1 each turn (no max).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(River_Nature())
AlienRegistry.register(Mountain_Nature())
AlienRegistry.register(Forest_Nature())
AlienRegistry.register(Desert_Nature())
AlienRegistry.register(Valley())
AlienRegistry.register(Volcano_Nature())
AlienRegistry.register(Waterfall())
AlienRegistry.register(Cave_Nature())
AlienRegistry.register(Cliff())
AlienRegistry.register(Swamp())
AlienRegistry.register(Island_Nature())
AlienRegistry.register(Glacier())
