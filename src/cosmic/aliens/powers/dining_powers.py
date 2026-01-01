"""
Dining themed alien powers for Cosmic Encounter.
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
class Fork_Dining(AlienPower):
    """Fork - Power of Choice."""
    name: str = field(default="Fork_Dining", init=False)
    description: str = field(default="Choose between two revealed cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Knife_Dining(AlienPower):
    """Knife - Power of Cutting."""
    name: str = field(default="Knife_Dining", init=False)
    description: str = field(default="Cut opponent's total in half.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Spoon_Dining(AlienPower):
    """Spoon - Power of Scooping."""
    name: str = field(default="Spoon_Dining", init=False)
    description: str = field(default="Scoop cards from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Plate(AlienPower):
    """Plate - Power of Serving."""
    name: str = field(default="Plate", init=False)
    description: str = field(default="Serve cards to other players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cup_Dining(AlienPower):
    """Cup - Power of Holding."""
    name: str = field(default="Cup_Dining", init=False)
    description: str = field(default="Hold one card in reserve.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Napkin(AlienPower):
    """Napkin - Power of Cleaning."""
    name: str = field(default="Napkin", init=False)
    description: str = field(default="Clean up after messy encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Menu(AlienPower):
    """Menu - Power of Options."""
    name: str = field(default="Menu", init=False)
    description: str = field(default="Offer opponent choice of outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Table_Dining(AlienPower):
    """Table - Power of Gathering."""
    name: str = field(default="Table_Dining", init=False)
    description: str = field(default="All players at table get +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chopsticks(AlienPower):
    """Chopsticks - Power of Precision."""
    name: str = field(default="Chopsticks", init=False)
    description: str = field(default="Pick exact card from deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tray(AlienPower):
    """Tray - Power of Carrying."""
    name: str = field(default="Tray", init=False)
    description: str = field(default="Carry multiple cards between phases.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Fork_Dining())
AlienRegistry.register(Knife_Dining())
AlienRegistry.register(Spoon_Dining())
AlienRegistry.register(Plate())
AlienRegistry.register(Cup_Dining())
AlienRegistry.register(Napkin())
AlienRegistry.register(Menu())
AlienRegistry.register(Table_Dining())
AlienRegistry.register(Chopsticks())
AlienRegistry.register(Tray())
