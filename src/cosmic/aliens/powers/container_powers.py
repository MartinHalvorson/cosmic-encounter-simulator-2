"""
Container themed alien powers for Cosmic Encounter.
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
class Box(AlienPower):
    """Box - Power of Storage."""
    name: str = field(default="Box", init=False)
    description: str = field(default="Store one card outside hand for later.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bag(AlienPower):
    """Bag - Power of Carrying."""
    name: str = field(default="Bag", init=False)
    description: str = field(default="Hand limit increased by 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jar(AlienPower):
    """Jar - Power of Preservation."""
    name: str = field(default="Jar", init=False)
    description: str = field(default="Protect one card from being discarded.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bottle(AlienPower):
    """Bottle - Power of Messages."""
    name: str = field(default="Bottle", init=False)
    description: str = field(default="Send card to any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Basket(AlienPower):
    """Basket - Power of Collection."""
    name: str = field(default="Basket", init=False)
    description: str = field(default="Collect discarded cards once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Barrel(AlienPower):
    """Barrel - Power of Bulk."""
    name: str = field(default="Barrel", init=False)
    description: str = field(default="Draw 3 cards, keep 1, discard 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chest(AlienPower):
    """Chest - Power of Treasure."""
    name: str = field(default="Chest", init=False)
    description: str = field(default="Double card value once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Bucket(AlienPower):
    """Bucket - Power of Gathering."""
    name: str = field(default="Bucket", init=False)
    description: str = field(default="Gather all ships from warp at once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Crate(AlienPower):
    """Crate - Power of Shipping."""
    name: str = field(default="Crate", init=False)
    description: str = field(default="Move cards between players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Trunk(AlienPower):
    """Trunk - Power of Secrets."""
    name: str = field(default="Trunk", init=False)
    description: str = field(default="Hide your hand from all players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Box())
AlienRegistry.register(Bag())
AlienRegistry.register(Jar())
AlienRegistry.register(Bottle())
AlienRegistry.register(Basket())
AlienRegistry.register(Barrel())
AlienRegistry.register(Chest())
AlienRegistry.register(Bucket())
AlienRegistry.register(Crate())
AlienRegistry.register(Trunk())
