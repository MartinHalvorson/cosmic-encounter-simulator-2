"""
Extended Sports themed alien powers for Cosmic Encounter.
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
class Quarterback(AlienPower):
    """Quarterback - Power of Leadership."""
    name: str = field(default="Quarterback", init=False)
    description: str = field(default="Choose which ally commits ships first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goalie(AlienPower):
    """Goalie - Power of Defense."""
    name: str = field(default="Goalie", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Striker(AlienPower):
    """Striker - Power of Offense."""
    name: str = field(default="Striker", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pitcher(AlienPower):
    """Pitcher - Power of Throws."""
    name: str = field(default="Pitcher", init=False)
    description: str = field(default="Discard to send 1 enemy ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Batter(AlienPower):
    """Batter - Power of Hits."""
    name: str = field(default="Batter", init=False)
    description: str = field(default="+3 for every 10 on your card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Referee(AlienPower):
    """Referee - Power of Rules."""
    name: str = field(default="Referee", init=False)
    description: str = field(default="Cancel one power use per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Coach(AlienPower):
    """Coach - Power of Strategy."""
    name: str = field(default="Coach", init=False)
    description: str = field(default="See opponent's top 2 cards before planning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sprinter(AlienPower):
    """Sprinter - Power of Speed."""
    name: str = field(default="Sprinter", init=False)
    description: str = field(default="Play card before opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Marathoner(AlienPower):
    """Marathoner - Power of Endurance."""
    name: str = field(default="Marathoner", init=False)
    description: str = field(default="+1 for each turn beyond 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swimmer(AlienPower):
    """Swimmer - Power of Flow."""
    name: str = field(default="Swimmer", init=False)
    description: str = field(default="Ships return from warp anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diver(AlienPower):
    """Diver - Power of Depth."""
    name: str = field(default="Diver", init=False)
    description: str = field(default="Draw from bottom of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boxer(AlienPower):
    """Boxer - Power of Punches."""
    name: str = field(default="Boxer", init=False)
    description: str = field(default="When winning, remove 2 extra ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Quarterback())
AlienRegistry.register(Goalie())
AlienRegistry.register(Striker())
AlienRegistry.register(Pitcher())
AlienRegistry.register(Batter())
AlienRegistry.register(Referee())
AlienRegistry.register(Coach())
AlienRegistry.register(Sprinter())
AlienRegistry.register(Marathoner())
AlienRegistry.register(Swimmer())
AlienRegistry.register(Diver())
AlienRegistry.register(Boxer())
