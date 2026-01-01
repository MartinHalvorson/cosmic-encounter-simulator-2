"""
Jewelry themed alien powers for Cosmic Encounter.
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
class Ring(AlienPower):
    """Ring - Power of Binding."""
    name: str = field(default="Ring", init=False)
    description: str = field(default="Lock one player's alliance choice.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Necklace(AlienPower):
    """Necklace - Power of Connection."""
    name: str = field(default="Necklace", init=False)
    description: str = field(default="+1 for each colony you share with another player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bracelet(AlienPower):
    """Bracelet - Power of Links."""
    name: str = field(default="Bracelet", init=False)
    description: str = field(default="Share victory with one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Earring(AlienPower):
    """Earring - Power of Listening."""
    name: str = field(default="Earring", init=False)
    description: str = field(default="Hear opponent's card choice before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crown_Jewelry(AlienPower):
    """Crown - Power of Royalty."""
    name: str = field(default="Crown_Jewelry", init=False)
    description: str = field(default="+3 when you have most colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tiara(AlienPower):
    """Tiara - Power of Grace."""
    name: str = field(default="Tiara", init=False)
    description: str = field(default="Avoid losing ships once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brooch(AlienPower):
    """Brooch - Power of Fastening."""
    name: str = field(default="Brooch", init=False)
    description: str = field(default="Lock cards in hand until end of encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pendant(AlienPower):
    """Pendant - Power of Memory."""
    name: str = field(default="Pendant", init=False)
    description: str = field(default="Recall one card from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Amulet(AlienPower):
    """Amulet - Power of Protection."""
    name: str = field(default="Amulet", init=False)
    description: str = field(default="Immune to artifact effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anklet(AlienPower):
    """Anklet - Power of Steps."""
    name: str = field(default="Anklet", init=False)
    description: str = field(default="Move ships one extra space.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Ring())
AlienRegistry.register(Necklace())
AlienRegistry.register(Bracelet())
AlienRegistry.register(Earring())
AlienRegistry.register(Crown_Jewelry())
AlienRegistry.register(Tiara())
AlienRegistry.register(Brooch())
AlienRegistry.register(Pendant())
AlienRegistry.register(Amulet())
AlienRegistry.register(Anklet())
