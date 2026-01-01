"""
Additional Occupation themed alien powers for Cosmic Encounter.
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
class Accountant(AlienPower):
    """Accountant - Power of Numbers."""
    name: str = field(default="Accountant", init=False)
    description: str = field(default="Know exact card totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Librarian(AlienPower):
    """Librarian - Power of Knowledge."""
    name: str = field(default="Librarian", init=False)
    description: str = field(default="Draw specific card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Janitor(AlienPower):
    """Janitor - Power of Cleaning."""
    name: str = field(default="Janitor", init=False)
    description: str = field(default="Clear all cards from play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Secretary(AlienPower):
    """Secretary - Power of Organization."""
    name: str = field(default="Secretary", init=False)
    description: str = field(default="Rearrange hand before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Electrician(AlienPower):
    """Electrician - Power of Connection."""
    name: str = field(default="Electrician", init=False)
    description: str = field(default="Link planets for bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Plumber(AlienPower):
    """Plumber - Power of Flow."""
    name: str = field(default="Plumber", init=False)
    description: str = field(default="Ships flow between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mechanic(AlienPower):
    """Mechanic - Power of Repair."""
    name: str = field(default="Mechanic", init=False)
    description: str = field(default="Retrieve 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Veterinarian(AlienPower):
    """Veterinarian - Power of Healing."""
    name: str = field(default="Veterinarian", init=False)
    description: str = field(default="Heal damaged allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chef_Occ(AlienPower):
    """Chef - Power of Cooking."""
    name: str = field(default="Chef_Occ", init=False)
    description: str = field(default="Combine card effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Firefighter(AlienPower):
    """Firefighter - Power of Rescue."""
    name: str = field(default="Firefighter", init=False)
    description: str = field(default="Save ships from destruction.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Police_Officer(AlienPower):
    """Police Officer - Power of Law."""
    name: str = field(default="Police_Officer", init=False)
    description: str = field(default="Prevent power abuse.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Astronaut_Occ(AlienPower):
    """Astronaut - Power of Exploration."""
    name: str = field(default="Astronaut_Occ", init=False)
    description: str = field(default="+2 attacking far planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Accountant())
AlienRegistry.register(Librarian())
AlienRegistry.register(Janitor())
AlienRegistry.register(Secretary())
AlienRegistry.register(Electrician())
AlienRegistry.register(Plumber())
AlienRegistry.register(Mechanic())
AlienRegistry.register(Veterinarian())
AlienRegistry.register(Chef_Occ())
AlienRegistry.register(Firefighter())
AlienRegistry.register(Police_Officer())
AlienRegistry.register(Astronaut_Occ())
