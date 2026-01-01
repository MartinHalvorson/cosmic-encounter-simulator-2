"""
Fictional Character themed alien powers for Cosmic Encounter.
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
class Hero_Char(AlienPower):
    """Hero - Power of Valor."""
    name: str = field(default="Hero_Char", init=False)
    description: str = field(default="+4 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Villain_Char(AlienPower):
    """Villain - Power of Scheme."""
    name: str = field(default="Villain_Char", init=False)
    description: str = field(default="See opponent's plans.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sidekick(AlienPower):
    """Sidekick - Power of Support."""
    name: str = field(default="Sidekick", init=False)
    description: str = field(default="+3 when allied.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mentor_Char(AlienPower):
    """Mentor - Power of Wisdom."""
    name: str = field(default="Mentor_Char", init=False)
    description: str = field(default="Give +2 to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Antihero(AlienPower):
    """Antihero - Power of Ambiguity."""
    name: str = field(default="Antihero", init=False)
    description: str = field(default="Switch sides mid-encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Trickster_Char(AlienPower):
    """Trickster - Power of Deception."""
    name: str = field(default="Trickster_Char", init=False)
    description: str = field(default="Bluff card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sage_Char(AlienPower):
    """Sage - Power of Knowledge."""
    name: str = field(default="Sage_Char", init=False)
    description: str = field(default="Know all card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warrior_Char(AlienPower):
    """Warrior - Power of Combat."""
    name: str = field(default="Warrior_Char", init=False)
    description: str = field(default="+2 in all battles.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mage_Char(AlienPower):
    """Mage - Power of Magic."""
    name: str = field(default="Mage_Char", init=False)
    description: str = field(default="Change card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rogue_Char(AlienPower):
    """Rogue - Power of Stealth."""
    name: str = field(default="Rogue_Char", init=False)
    description: str = field(default="Ships invisible until combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ranger_Char(AlienPower):
    """Ranger - Power of Tracking."""
    name: str = field(default="Ranger_Char", init=False)
    description: str = field(default="See destiny before drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Paladin_Char(AlienPower):
    """Paladin - Power of Justice."""
    name: str = field(default="Paladin_Char", init=False)
    description: str = field(default="+3 defending allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Hero_Char())
AlienRegistry.register(Villain_Char())
AlienRegistry.register(Sidekick())
AlienRegistry.register(Mentor_Char())
AlienRegistry.register(Antihero())
AlienRegistry.register(Trickster_Char())
AlienRegistry.register(Sage_Char())
AlienRegistry.register(Warrior_Char())
AlienRegistry.register(Mage_Char())
AlienRegistry.register(Rogue_Char())
AlienRegistry.register(Ranger_Char())
AlienRegistry.register(Paladin_Char())
