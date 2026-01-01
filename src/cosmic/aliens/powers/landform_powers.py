"""
Landform themed alien powers for Cosmic Encounter.
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
class Peninsula(AlienPower):
    """Peninsula - Power of Extension."""
    name: str = field(default="Peninsula", init=False)
    description: str = field(default="Extend encounter to adjacent system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Plateau(AlienPower):
    """Plateau - Power of Stability."""
    name: str = field(default="Plateau", init=False)
    description: str = field(default="Card values lock at +10 max.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Canyon(AlienPower):
    """Canyon - Power of Depth."""
    name: str = field(default="Canyon", init=False)
    description: str = field(default="Low cards (under 10) count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mesa(AlienPower):
    """Mesa - Power of Flatness."""
    name: str = field(default="Mesa", init=False)
    description: str = field(default="All attack cards treated as 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fjord(AlienPower):
    """Fjord - Power of Inlet."""
    name: str = field(default="Fjord", init=False)
    description: str = field(default="Draw ships into encounter from adjacent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Delta(AlienPower):
    """Delta - Power of Branching."""
    name: str = field(default="Delta", init=False)
    description: str = field(default="Split ships between two planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Atoll(AlienPower):
    """Atoll - Power of the Ring."""
    name: str = field(default="Atoll", init=False)
    description: str = field(default="Protect planet with ship barrier.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Geyser(AlienPower):
    """Geyser - Power of Eruption."""
    name: str = field(default="Geyser", init=False)
    description: str = field(default="Periodically boost: +5 every 3rd encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ravine(AlienPower):
    """Ravine - Power of Splitting."""
    name: str = field(default="Ravine", init=False)
    description: str = field(default="Divide opponent's ships between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dune(AlienPower):
    """Dune - Power of Shifting."""
    name: str = field(default="Dune", init=False)
    description: str = field(default="Move colonies between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oasis_Land(AlienPower):
    """Oasis - Power of Refuge."""
    name: str = field(default="Oasis_Land", init=False)
    description: str = field(default="Ships can retreat here safely.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Basin(AlienPower):
    """Basin - Power of Collection."""
    name: str = field(default="Basin", init=False)
    description: str = field(default="Collect all discarded cards at round end.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Peninsula())
AlienRegistry.register(Plateau())
AlienRegistry.register(Canyon())
AlienRegistry.register(Mesa())
AlienRegistry.register(Fjord())
AlienRegistry.register(Delta())
AlienRegistry.register(Atoll())
AlienRegistry.register(Geyser())
AlienRegistry.register(Ravine())
AlienRegistry.register(Dune())
AlienRegistry.register(Oasis_Land())
AlienRegistry.register(Basin())
