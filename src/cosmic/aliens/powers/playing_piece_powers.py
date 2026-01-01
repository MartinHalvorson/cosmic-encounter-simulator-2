"""
Playing Piece themed alien powers for Cosmic Encounter.
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
class Dice_Piece(AlienPower):
    """Dice - Power of Randomness."""
    name: str = field(default="Dice_Piece", init=False)
    description: str = field(default="Random bonus 1-6 each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Token(AlienPower):
    """Token - Power of Representation."""
    name: str = field(default="Token", init=False)
    description: str = field(default="Create token ship copies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Meeple(AlienPower):
    """Meeple - Power of Workers."""
    name: str = field(default="Meeple", init=False)
    description: str = field(default="Ships generate resources each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Counter(AlienPower):
    """Counter - Power of Tracking."""
    name: str = field(default="Counter", init=False)
    description: str = field(default="Track wins: +1 per win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chip(AlienPower):
    """Chip - Power of Betting."""
    name: str = field(default="Chip", init=False)
    description: str = field(default="Bet cards on encounter outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spinner(AlienPower):
    """Spinner - Power of Fate."""
    name: str = field(default="Spinner", init=False)
    description: str = field(default="Spin for random effect each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hourglass(AlienPower):
    """Hourglass - Power of Time Limit."""
    name: str = field(default="Hourglass", init=False)
    description: str = field(default="Force quick resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tile(AlienPower):
    """Tile - Power of Placement."""
    name: str = field(default="Tile", init=False)
    description: str = field(default="Place bonus tiles on planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Standee(AlienPower):
    """Standee - Power of Standing."""
    name: str = field(default="Standee", init=False)
    description: str = field(default="Ships can't be moved involuntarily.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Miniature(AlienPower):
    """Miniature - Power of Detail."""
    name: str = field(default="Miniature", init=False)
    description: str = field(default="Ships count as fractional.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Dice_Piece())
AlienRegistry.register(Token())
AlienRegistry.register(Meeple())
AlienRegistry.register(Counter())
AlienRegistry.register(Chip())
AlienRegistry.register(Spinner())
AlienRegistry.register(Hourglass())
AlienRegistry.register(Tile())
AlienRegistry.register(Standee())
AlienRegistry.register(Miniature())
