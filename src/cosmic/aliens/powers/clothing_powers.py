"""
Clothing themed alien powers for Cosmic Encounter.
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
class Shirt(AlienPower):
    """Shirt - Power of Covering."""
    name: str = field(default="Shirt", init=False)
    description: str = field(default="First ship lost each turn is protected.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pants(AlienPower):
    """Pants - Power of Movement."""
    name: str = field(default="Pants", init=False)
    description: str = field(default="Move 2 ships between colonies each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hat(AlienPower):
    """Hat - Power of Authority."""
    name: str = field(default="Hat", init=False)
    description: str = field(default="+2 when you are the offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shoes(AlienPower):
    """Shoes - Power of Speed."""
    name: str = field(default="Shoes", init=False)
    description: str = field(default="Ships commit before opponent's.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gloves(AlienPower):
    """Gloves - Power of Grip."""
    name: str = field(default="Gloves", init=False)
    description: str = field(default="Cards can't be taken from your hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jacket(AlienPower):
    """Jacket - Power of Protection."""
    name: str = field(default="Jacket", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scarf(AlienPower):
    """Scarf - Power of Warmth."""
    name: str = field(default="Scarf", init=False)
    description: str = field(default="Retrieve 1 ship from warp each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Belt(AlienPower):
    """Belt - Power of Holding."""
    name: str = field(default="Belt", init=False)
    description: str = field(default="Keep cards after negotiation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Socks(AlienPower):
    """Socks - Power of Comfort."""
    name: str = field(default="Socks", init=False)
    description: str = field(default="Ships survive one extra loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tie(AlienPower):
    """Tie - Power of Business."""
    name: str = field(default="Tie", init=False)
    description: str = field(default="Draw 1 card when you win a deal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dress(AlienPower):
    """Dress - Power of Elegance."""
    name: str = field(default="Dress", init=False)
    description: str = field(default="+2 for each ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cape(AlienPower):
    """Cape - Power of Drama."""
    name: str = field(default="Cape", init=False)
    description: str = field(default="+5 when you play your highest card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Shirt())
AlienRegistry.register(Pants())
AlienRegistry.register(Hat())
AlienRegistry.register(Shoes())
AlienRegistry.register(Gloves())
AlienRegistry.register(Jacket())
AlienRegistry.register(Scarf())
AlienRegistry.register(Belt())
AlienRegistry.register(Socks())
AlienRegistry.register(Tie())
AlienRegistry.register(Dress())
AlienRegistry.register(Cape())
