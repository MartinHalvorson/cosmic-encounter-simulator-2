"""
Astronomical themed alien powers for Cosmic Encounter.
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
class Supernova_Astro(AlienPower):
    """Supernova - Power of Explosion."""
    name: str = field(default="Supernova_Astro", init=False)
    description: str = field(default="+8 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Neutron_Star(AlienPower):
    """Neutron Star - Power of Density."""
    name: str = field(default="Neutron_Star", init=False)
    description: str = field(default="+1 per ship on planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Red_Giant(AlienPower):
    """Red Giant - Power of Expansion."""
    name: str = field(default="Red_Giant", init=False)
    description: str = field(default="Expand to adjacent planets on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class White_Dwarf(AlienPower):
    """White Dwarf - Power of Fading."""
    name: str = field(default="White_Dwarf", init=False)
    description: str = field(default="+5 when low on ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Binary_Star(AlienPower):
    """Binary Star - Power of Pairs."""
    name: str = field(default="Binary_Star", init=False)
    description: str = field(default="+3 when playing matching cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quasar_Astro(AlienPower):
    """Quasar - Power of Distance."""
    name: str = field(default="Quasar_Astro", init=False)
    description: str = field(default="Attack from any distance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pulsar_Astro(AlienPower):
    """Pulsar - Power of Rhythm."""
    name: str = field(default="Pulsar_Astro", init=False)
    description: str = field(default="+4 every other turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magnetar(AlienPower):
    """Magnetar - Power of Attraction."""
    name: str = field(default="Magnetar", init=False)
    description: str = field(default="Pull ships from adjacent planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dark_Matter(AlienPower):
    """Dark Matter - Power of Invisibility."""
    name: str = field(default="Dark_Matter", init=False)
    description: str = field(default="Ships are hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dark_Energy(AlienPower):
    """Dark Energy - Power of Expansion."""
    name: str = field(default="Dark_Energy", init=False)
    description: str = field(default="Push opponent's ships away.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Black_Hole_Astro(AlienPower):
    """Black Hole - Power of Consumption."""
    name: str = field(default="Black_Hole_Astro", init=False)
    description: str = field(default="Pull cards from opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wormhole_Astro(AlienPower):
    """Wormhole - Power of Transport."""
    name: str = field(default="Wormhole_Astro", init=False)
    description: str = field(default="Teleport ships anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Supernova_Astro())
AlienRegistry.register(Neutron_Star())
AlienRegistry.register(Red_Giant())
AlienRegistry.register(White_Dwarf())
AlienRegistry.register(Binary_Star())
AlienRegistry.register(Quasar_Astro())
AlienRegistry.register(Pulsar_Astro())
AlienRegistry.register(Magnetar())
AlienRegistry.register(Dark_Matter())
AlienRegistry.register(Dark_Energy())
AlienRegistry.register(Black_Hole_Astro())
AlienRegistry.register(Wormhole_Astro())
