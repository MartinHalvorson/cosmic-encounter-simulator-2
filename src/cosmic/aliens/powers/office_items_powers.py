"""
Office and Stationery themed alien powers for Cosmic Encounter.
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
class Pen(AlienPower):
    """Pen - Power of Writing."""
    name: str = field(default="Pen", init=False)
    description: str = field(default="Mark an opponent: +2 vs them all game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pencil(AlienPower):
    """Pencil - Power of Erasure."""
    name: str = field(default="Pencil", init=False)
    description: str = field(default="Cancel one reinforcement card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Paper(AlienPower):
    """Paper - Power of Records."""
    name: str = field(default="Paper", init=False)
    description: str = field(default="See all cards played this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stapler(AlienPower):
    """Stapler - Power of Binding."""
    name: str = field(default="Stapler", init=False)
    description: str = field(default="Lock one player's ships in place.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Calculator(AlienPower):
    """Calculator - Power of Precision."""
    name: str = field(default="Calculator", init=False)
    description: str = field(default="Know exact total before playing card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eraser(AlienPower):
    """Eraser - Power of Removal."""
    name: str = field(default="Eraser", init=False)
    description: str = field(default="Remove one card from the game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Folder(AlienPower):
    """Folder - Power of Organization."""
    name: str = field(default="Folder", init=False)
    description: str = field(default="Arrange top 3 cards of cosmic deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Notebook(AlienPower):
    """Notebook - Power of Notes."""
    name: str = field(default="Notebook", init=False)
    description: str = field(default="Draw 1 extra card when drawing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clipboard(AlienPower):
    """Clipboard - Power of Lists."""
    name: str = field(default="Clipboard", init=False)
    description: str = field(default="+1 for each completed encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stamp(AlienPower):
    """Stamp - Power of Approval."""
    name: str = field(default="Stamp", init=False)
    description: str = field(default="Approve or deny ally participation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Pen())
AlienRegistry.register(Pencil())
AlienRegistry.register(Paper())
AlienRegistry.register(Stapler())
AlienRegistry.register(Calculator())
AlienRegistry.register(Eraser())
AlienRegistry.register(Folder())
AlienRegistry.register(Notebook())
AlienRegistry.register(Clipboard())
AlienRegistry.register(Stamp())
