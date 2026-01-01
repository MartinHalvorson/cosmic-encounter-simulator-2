"""
School Subject themed alien powers for Cosmic Encounter.
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
class History(AlienPower):
    """History - Power of the Past."""
    name: str = field(default="History", init=False)
    description: str = field(default="Replay last encounter outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Geography(AlienPower):
    """Geography - Power of Location."""
    name: str = field(default="Geography", init=False)
    description: str = field(default="Choose which planet destiny points to.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Literature(AlienPower):
    """Literature - Power of Stories."""
    name: str = field(default="Literature", init=False)
    description: str = field(default="Narrate outcome: +3 or -3 to total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Art_Subject(AlienPower):
    """Art - Power of Creation."""
    name: str = field(default="Art_Subject", init=False)
    description: str = field(default="Create a temporary card once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Music_Subject(AlienPower):
    """Music - Power of Harmony."""
    name: str = field(default="Music_Subject", init=False)
    description: str = field(default="+2 for each ally you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Physical_Education(AlienPower):
    """Physical Education - Power of Fitness."""
    name: str = field(default="Physical_Education", init=False)
    description: str = field(default="Ships count as +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Economics(AlienPower):
    """Economics - Power of Trade."""
    name: str = field(default="Economics", init=False)
    description: str = field(default="Trade cards with any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Psychology(AlienPower):
    """Psychology - Power of Mind."""
    name: str = field(default="Psychology", init=False)
    description: str = field(default="Predict opponent's card; if right, +5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sociology(AlienPower):
    """Sociology - Power of Groups."""
    name: str = field(default="Sociology", init=False)
    description: str = field(default="+1 for each other player with colonies on same system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Linguistics(AlienPower):
    """Linguistics - Power of Words."""
    name: str = field(default="Linguistics", init=False)
    description: str = field(default="Negotiate cards have +2 effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Computer_Science(AlienPower):
    """Computer Science - Power of Logic."""
    name: str = field(default="Computer_Science", init=False)
    description: str = field(default="Calculate exact winning card needed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drama_Subject(AlienPower):
    """Drama - Power of Performance."""
    name: str = field(default="Drama_Subject", init=False)
    description: str = field(default="Bluff card type once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(History())
AlienRegistry.register(Geography())
AlienRegistry.register(Literature())
AlienRegistry.register(Art_Subject())
AlienRegistry.register(Music_Subject())
AlienRegistry.register(Physical_Education())
AlienRegistry.register(Economics())
AlienRegistry.register(Psychology())
AlienRegistry.register(Sociology())
AlienRegistry.register(Linguistics())
AlienRegistry.register(Computer_Science())
AlienRegistry.register(Drama_Subject())
