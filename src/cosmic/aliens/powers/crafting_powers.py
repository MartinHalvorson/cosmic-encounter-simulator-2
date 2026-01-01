"""
Crafting themed alien powers for Cosmic Encounter.
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
class Blacksmith(AlienPower):
    """Blacksmith - Power of Forging."""
    name: str = field(default="Blacksmith", init=False)
    description: str = field(default="+2 when using attack cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Carpenter(AlienPower):
    """Carpenter - Power of Building."""
    name: str = field(default="Carpenter", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Weaver(AlienPower):
    """Weaver - Power of Connecting."""
    name: str = field(default="Weaver", init=False)
    description: str = field(default="Link allies for shared bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Potter(AlienPower):
    """Potter - Power of Shaping."""
    name: str = field(default="Potter", init=False)
    description: str = field(default="Reshape card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Glassblower(AlienPower):
    """Glassblower - Power of Clarity."""
    name: str = field(default="Glassblower", init=False)
    description: str = field(default="See all hidden information.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Leatherworker(AlienPower):
    """Leatherworker - Power of Durability."""
    name: str = field(default="Leatherworker", init=False)
    description: str = field(default="Ships survive one extra loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jeweler_Craft(AlienPower):
    """Jeweler - Power of Value."""
    name: str = field(default="Jeweler_Craft", init=False)
    description: str = field(default="Double card value once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tailor(AlienPower):
    """Tailor - Power of Fitting."""
    name: str = field(default="Tailor", init=False)
    description: str = field(default="Adjust ship count after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Brewer(AlienPower):
    """Brewer - Power of Mixture."""
    name: str = field(default="Brewer", init=False)
    description: str = field(default="Combine two card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sculptor(AlienPower):
    """Sculptor - Power of Form."""
    name: str = field(default="Sculptor", init=False)
    description: str = field(default="Create permanent bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Blacksmith())
AlienRegistry.register(Carpenter())
AlienRegistry.register(Weaver())
AlienRegistry.register(Potter())
AlienRegistry.register(Glassblower())
AlienRegistry.register(Leatherworker())
AlienRegistry.register(Jeweler_Craft())
AlienRegistry.register(Tailor())
AlienRegistry.register(Brewer())
AlienRegistry.register(Sculptor())
