"""
Building Type themed alien powers for Cosmic Encounter.
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
class Skyscraper_Build(AlienPower):
    """Skyscraper - Power of Height."""
    name: str = field(default="Skyscraper_Build", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hospital(AlienPower):
    """Hospital - Power of Healing."""
    name: str = field(default="Hospital", init=False)
    description: str = field(default="Retrieve 1 ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class School(AlienPower):
    """School - Power of Learning."""
    name: str = field(default="School", init=False)
    description: str = field(default="+1 per turn played.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Factory_Build(AlienPower):
    """Factory - Power of Production."""
    name: str = field(default="Factory_Build", init=False)
    description: str = field(default="Create token ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Prison(AlienPower):
    """Prison - Power of Confinement."""
    name: str = field(default="Prison", init=False)
    description: str = field(default="Trap opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bank_Build(AlienPower):
    """Bank - Power of Savings."""
    name: str = field(default="Bank_Build", init=False)
    description: str = field(default="Store cards for later.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Church(AlienPower):
    """Church - Power of Faith."""
    name: str = field(default="Church", init=False)
    description: str = field(default="+3 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stadium(AlienPower):
    """Stadium - Power of Competition."""
    name: str = field(default="Stadium", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Museum(AlienPower):
    """Museum - Power of History."""
    name: str = field(default="Museum", init=False)
    description: str = field(default="Reuse played cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Library_Build(AlienPower):
    """Library - Power of Knowledge."""
    name: str = field(default="Library_Build", init=False)
    description: str = field(default="Draw extra cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lighthouse(AlienPower):
    """Lighthouse - Power of Guidance."""
    name: str = field(default="Lighthouse", init=False)
    description: str = field(default="Guide allies to you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Observatory(AlienPower):
    """Observatory - Power of Sight."""
    name: str = field(default="Observatory", init=False)
    description: str = field(default="See destiny before drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Skyscraper_Build())
AlienRegistry.register(Hospital())
AlienRegistry.register(School())
AlienRegistry.register(Factory_Build())
AlienRegistry.register(Prison())
AlienRegistry.register(Bank_Build())
AlienRegistry.register(Church())
AlienRegistry.register(Stadium())
AlienRegistry.register(Museum())
AlienRegistry.register(Library_Build())
AlienRegistry.register(Lighthouse())
AlienRegistry.register(Observatory())
