"""
Kitchen and Appliance themed alien powers for Cosmic Encounter.
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
class Oven(AlienPower):
    """Oven - Power of Cooking."""
    name: str = field(default="Oven", init=False)
    description: str = field(default="Transform negotiate into attack 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Refrigerator(AlienPower):
    """Refrigerator - Power of Preservation."""
    name: str = field(default="Refrigerator", init=False)
    description: str = field(default="Keep cards after failed negotiation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Microwave(AlienPower):
    """Microwave - Power of Speed."""
    name: str = field(default="Microwave", init=False)
    description: str = field(default="+3 when encounter ends in 1 round.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blender(AlienPower):
    """Blender - Power of Mixing."""
    name: str = field(default="Blender", init=False)
    description: str = field(default="Combine two low cards into one high.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Toaster(AlienPower):
    """Toaster - Power of Transformation."""
    name: str = field(default="Toaster", init=False)
    description: str = field(default="Flip card value (40 becomes 00, etc).", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dishwasher(AlienPower):
    """Dishwasher - Power of Cleaning."""
    name: str = field(default="Dishwasher", init=False)
    description: str = field(default="Shuffle discard into deck once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kettle(AlienPower):
    """Kettle - Power of Heating."""
    name: str = field(default="Kettle", init=False)
    description: str = field(default="+2 when you play first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Grinder(AlienPower):
    """Grinder - Power of Reduction."""
    name: str = field(default="Grinder", init=False)
    description: str = field(default="Reduce opponent's card by 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pan(AlienPower):
    """Pan - Power of Sizzle."""
    name: str = field(default="Pan", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pot(AlienPower):
    """Pot - Power of Simmering."""
    name: str = field(default="Pot", init=False)
    description: str = field(default="+1 each turn you don't use power (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Oven())
AlienRegistry.register(Refrigerator())
AlienRegistry.register(Microwave())
AlienRegistry.register(Blender())
AlienRegistry.register(Toaster())
AlienRegistry.register(Dishwasher())
AlienRegistry.register(Kettle())
AlienRegistry.register(Grinder())
AlienRegistry.register(Pan())
AlienRegistry.register(Pot())
