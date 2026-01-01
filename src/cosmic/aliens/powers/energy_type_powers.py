"""
Energy Type themed alien powers for Cosmic Encounter.
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
class Solar_Energy(AlienPower):
    """Solar Energy - Power of Light."""
    name: str = field(default="Solar_Energy", init=False)
    description: str = field(default="+3 during day turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wind_Energy(AlienPower):
    """Wind Energy - Power of Gust."""
    name: str = field(default="Wind_Energy", init=False)
    description: str = field(default="Push ships between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hydro_Energy(AlienPower):
    """Hydro Energy - Power of Water."""
    name: str = field(default="Hydro_Energy", init=False)
    description: str = field(default="+1 per flowing connection.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nuclear_Energy(AlienPower):
    """Nuclear Energy - Power of Fission."""
    name: str = field(default="Nuclear_Energy", init=False)
    description: str = field(default="+6 but all ships go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Geothermal(AlienPower):
    """Geothermal - Power of Earth Heat."""
    name: str = field(default="Geothermal", init=False)
    description: str = field(default="+2 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kinetic_Energy(AlienPower):
    """Kinetic Energy - Power of Motion."""
    name: str = field(default="Kinetic_Energy", init=False)
    description: str = field(default="+1 per ship moved.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Potential_Energy(AlienPower):
    """Potential Energy - Power of Storage."""
    name: str = field(default="Potential_Energy", init=False)
    description: str = field(default="Store bonus for later.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chemical_Energy(AlienPower):
    """Chemical Energy - Power of Reaction."""
    name: str = field(default="Chemical_Energy", init=False)
    description: str = field(default="Combine cards for effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Electrical_Energy(AlienPower):
    """Electrical Energy - Power of Shock."""
    name: str = field(default="Electrical_Energy", init=False)
    description: str = field(default="+4 on surprise attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thermal_Energy(AlienPower):
    """Thermal Energy - Power of Heat."""
    name: str = field(default="Thermal_Energy", init=False)
    description: str = field(default="+2 after consecutive wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magnetic_Energy(AlienPower):
    """Magnetic Energy - Power of Attraction."""
    name: str = field(default="Magnetic_Energy", init=False)
    description: str = field(default="Pull allies to your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Radiant_Energy(AlienPower):
    """Radiant Energy - Power of Glow."""
    name: str = field(default="Radiant_Energy", init=False)
    description: str = field(default="Reveal all hidden info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Solar_Energy())
AlienRegistry.register(Wind_Energy())
AlienRegistry.register(Hydro_Energy())
AlienRegistry.register(Nuclear_Energy())
AlienRegistry.register(Geothermal())
AlienRegistry.register(Kinetic_Energy())
AlienRegistry.register(Potential_Energy())
AlienRegistry.register(Chemical_Energy())
AlienRegistry.register(Electrical_Energy())
AlienRegistry.register(Thermal_Energy())
AlienRegistry.register(Magnetic_Energy())
AlienRegistry.register(Radiant_Energy())
