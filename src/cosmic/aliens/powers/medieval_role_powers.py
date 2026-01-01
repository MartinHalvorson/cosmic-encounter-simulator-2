"""
Medieval Role themed alien powers for Cosmic Encounter.
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
class Peasant(AlienPower):
    """Peasant - Power of Numbers."""
    name: str = field(default="Peasant", init=False)
    description: str = field(default="+1 per ship over 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Serf(AlienPower):
    """Serf - Power of Labor."""
    name: str = field(default="Serf", init=False)
    description: str = field(default="Extra card draw per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Squire_Med(AlienPower):
    """Squire - Power of Service."""
    name: str = field(default="Squire_Med", init=False)
    description: str = field(default="+2 when allied.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Knight_Med(AlienPower):
    """Knight - Power of Chivalry."""
    name: str = field(default="Knight_Med", init=False)
    description: str = field(default="+3 defending others.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Baron_Med(AlienPower):
    """Baron - Power of Land."""
    name: str = field(default="Baron_Med", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lord_Med(AlienPower):
    """Lord - Power of Command."""
    name: str = field(default="Lord_Med", init=False)
    description: str = field(default="Direct ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Duke_Med(AlienPower):
    """Duke - Power of Nobility."""
    name: str = field(default="Duke_Med", init=False)
    description: str = field(default="+2 per allied player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class King_Med(AlienPower):
    """King - Power of Rule."""
    name: str = field(default="King_Med", init=False)
    description: str = field(default="+4 with most colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bishop(AlienPower):
    """Bishop - Power of Faith."""
    name: str = field(default="Bishop", init=False)
    description: str = field(default="+3 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monk(AlienPower):
    """Monk - Power of Devotion."""
    name: str = field(default="Monk", init=False)
    description: str = field(default="Immune to ally effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Herald_Med(AlienPower):
    """Herald - Power of Announcement."""
    name: str = field(default="Herald_Med", init=False)
    description: str = field(default="Reveal opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jester(AlienPower):
    """Jester - Power of Chaos."""
    name: str = field(default="Jester", init=False)
    description: str = field(default="Random bonus 0-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Peasant())
AlienRegistry.register(Serf())
AlienRegistry.register(Squire_Med())
AlienRegistry.register(Knight_Med())
AlienRegistry.register(Baron_Med())
AlienRegistry.register(Lord_Med())
AlienRegistry.register(Duke_Med())
AlienRegistry.register(King_Med())
AlienRegistry.register(Bishop())
AlienRegistry.register(Monk())
AlienRegistry.register(Herald_Med())
AlienRegistry.register(Jester())
