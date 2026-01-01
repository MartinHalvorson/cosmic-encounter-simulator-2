"""
Egyptian Mythology themed alien powers for Cosmic Encounter.
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
class Ra_Egyptian(AlienPower):
    """Ra - Power of the Sun."""
    name: str = field(default="Ra_Egyptian", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Osiris(AlienPower):
    """Osiris - Power of Rebirth."""
    name: str = field(default="Osiris", init=False)
    description: str = field(default="Retrieve 2 ships from warp on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Isis_Egyptian(AlienPower):
    """Isis - Power of Magic."""
    name: str = field(default="Isis_Egyptian", init=False)
    description: str = field(default="Copy any ally's power once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Anubis(AlienPower):
    """Anubis - Power of Judgment."""
    name: str = field(default="Anubis", init=False)
    description: str = field(default="Win ties automatically.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Horus_Egyptian(AlienPower):
    """Horus - Power of Vengeance."""
    name: str = field(default="Horus_Egyptian", init=False)
    description: str = field(default="+4 against player who attacked you last.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Set_Egyptian(AlienPower):
    """Set - Power of Chaos."""
    name: str = field(default="Set_Egyptian", init=False)
    description: str = field(default="Randomize card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Thoth(AlienPower):
    """Thoth - Power of Wisdom."""
    name: str = field(default="Thoth", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bastet(AlienPower):
    """Bastet - Power of Protection."""
    name: str = field(default="Bastet", init=False)
    description: str = field(default="+3 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sekhmet(AlienPower):
    """Sekhmet - Power of War."""
    name: str = field(default="Sekhmet", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sobek(AlienPower):
    """Sobek - Power of the River."""
    name: str = field(default="Sobek", init=False)
    description: str = field(default="Ships flow to adjacent colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ptah(AlienPower):
    """Ptah - Power of Creation."""
    name: str = field(default="Ptah", init=False)
    description: str = field(default="Create token ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Maat(AlienPower):
    """Maat - Power of Truth."""
    name: str = field(default="Maat", init=False)
    description: str = field(default="Force honest negotiations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ra_Egyptian())
AlienRegistry.register(Osiris())
AlienRegistry.register(Isis_Egyptian())
AlienRegistry.register(Anubis())
AlienRegistry.register(Horus_Egyptian())
AlienRegistry.register(Set_Egyptian())
AlienRegistry.register(Thoth())
AlienRegistry.register(Bastet())
AlienRegistry.register(Sekhmet())
AlienRegistry.register(Sobek())
AlienRegistry.register(Ptah())
AlienRegistry.register(Maat())
