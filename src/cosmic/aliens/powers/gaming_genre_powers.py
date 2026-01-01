"""
Gaming Genre themed alien powers for Cosmic Encounter.
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
class Roguelike(AlienPower):
    """Roguelike - Power of Permadeath."""
    name: str = field(default="Roguelike", init=False)
    description: str = field(default="+5 but ships don't return from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class RPG_Genre(AlienPower):
    """RPG - Power of Leveling."""
    name: str = field(default="RPG_Genre", init=False)
    description: str = field(default="+1 for each win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class FPS(AlienPower):
    """FPS - Power of Reflexes."""
    name: str = field(default="FPS", init=False)
    description: str = field(default="+3 when attacking first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class RTS(AlienPower):
    """RTS - Power of Multitasking."""
    name: str = field(default="RTS", init=False)
    description: str = field(default="Take actions on multiple planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class MOBA(AlienPower):
    """MOBA - Power of Teams."""
    name: str = field(default="MOBA", init=False)
    description: str = field(default="+1 per ally in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Puzzle_Genre(AlienPower):
    """Puzzle - Power of Solutions."""
    name: str = field(default="Puzzle_Genre", init=False)
    description: str = field(default="Predict exact outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stealth_Genre(AlienPower):
    """Stealth - Power of Hiding."""
    name: str = field(default="Stealth_Genre", init=False)
    description: str = field(default="Ships are invisible.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Simulation(AlienPower):
    """Simulation - Power of Modeling."""
    name: str = field(default="Simulation", init=False)
    description: str = field(default="Preview encounter outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Racing_Genre(AlienPower):
    """Racing - Power of Speed."""
    name: str = field(default="Racing_Genre", init=False)
    description: str = field(default="+3 when first to act.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fighting_Genre(AlienPower):
    """Fighting - Power of Combat."""
    name: str = field(default="Fighting_Genre", init=False)
    description: str = field(default="+2 in 1v1 encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Horror_Genre(AlienPower):
    """Horror - Power of Fear."""
    name: str = field(default="Horror_Genre", init=False)
    description: str = field(default="Opponent loses 1 ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Survival_Genre(AlienPower):
    """Survival - Power of Endurance."""
    name: str = field(default="Survival_Genre", init=False)
    description: str = field(default="Ships survive longer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Roguelike())
AlienRegistry.register(RPG_Genre())
AlienRegistry.register(FPS())
AlienRegistry.register(RTS())
AlienRegistry.register(MOBA())
AlienRegistry.register(Puzzle_Genre())
AlienRegistry.register(Stealth_Genre())
AlienRegistry.register(Simulation())
AlienRegistry.register(Racing_Genre())
AlienRegistry.register(Fighting_Genre())
AlienRegistry.register(Horror_Genre())
AlienRegistry.register(Survival_Genre())
