"""
Weather Phenomena themed alien powers for Cosmic Encounter.
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
class Aurora_Weather(AlienPower):
    """Aurora - Power of Display."""
    name: str = field(default="Aurora_Weather", init=False)
    description: str = field(default="Reveal all hidden information briefly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fog_Weather(AlienPower):
    """Fog - Power of Obscurity."""
    name: str = field(default="Fog_Weather", init=False)
    description: str = field(default="Ship counts hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Haze(AlienPower):
    """Haze - Power of Confusion."""
    name: str = field(default="Haze", init=False)
    description: str = field(default="Opponent must guess your card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Drizzle(AlienPower):
    """Drizzle - Power of Persistence."""
    name: str = field(default="Drizzle", init=False)
    description: str = field(default="+1 that stacks each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Downpour(AlienPower):
    """Downpour - Power of Flooding."""
    name: str = field(default="Downpour", init=False)
    description: str = field(default="Flood planet: all ships go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Rainbow_Weather(AlienPower):
    """Rainbow - Power of Promise."""
    name: str = field(default="Rainbow_Weather", init=False)
    description: str = field(default="Gain benefit of any ally's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frost_Weather(AlienPower):
    """Frost - Power of Chill."""
    name: str = field(default="Frost_Weather", init=False)
    description: str = field(default="Slow one player's next action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sleet(AlienPower):
    """Sleet - Power of Mixture."""
    name: str = field(default="Sleet", init=False)
    description: str = field(default="Combine two card values into one.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hail_Weather(AlienPower):
    """Hail - Power of Pelting."""
    name: str = field(default="Hail_Weather", init=False)
    description: str = field(default="Deal 1 ship loss to each player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Breeze(AlienPower):
    """Breeze - Power of Gentle Push."""
    name: str = field(default="Breeze", init=False)
    description: str = field(default="Move one ship from any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Aurora_Weather())
AlienRegistry.register(Fog_Weather())
AlienRegistry.register(Haze())
AlienRegistry.register(Drizzle())
AlienRegistry.register(Downpour())
AlienRegistry.register(Rainbow_Weather())
AlienRegistry.register(Frost_Weather())
AlienRegistry.register(Sleet())
AlienRegistry.register(Hail_Weather())
AlienRegistry.register(Breeze())
