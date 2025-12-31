"""
Cosmic Entity Powers - Aliens representing cosmic forces and entities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Celestial(AlienPower):
    """
    Celestial - Star Being.
    +1 for each colony you have.
    """
    name: str = field(default="Celestial", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cosmic_Entity(AlienPower):
    """
    Cosmic_Entity - Universe Force.
    Once per game, win any encounter.
    """
    name: str = field(default="Cosmic_Entity", init=False)
    description: str = field(default="Auto-win once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Deity(AlienPower):
    """
    Deity - God Power.
    Change any die roll or random result.
    """
    name: str = field(default="Deity", init=False)
    description: str = field(default="Control random.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Eternal(AlienPower):
    """
    Eternal - Undying.
    Ships never go to warp.
    """
    name: str = field(default="Eternal", init=False)
    description: str = field(default="Ships immune to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Fate(AlienPower):
    """
    Fate - Destiny Control.
    Choose destiny instead of drawing.
    """
    name: str = field(default="Fate", init=False)
    description: str = field(default="Choose destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Infinite(AlienPower):
    """
    Infinite - Endless Power.
    Draw 2 cards per turn.
    """
    name: str = field(default="Infinite", init=False)
    description: str = field(default="Draw 2 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Omniscient(AlienPower):
    """
    Omniscient - All Knowing.
    See all cards and hands.
    """
    name: str = field(default="Omniscient", init=False)
    description: str = field(default="See all cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Primal(AlienPower):
    """
    Primal - First Force.
    Win ties automatically.
    """
    name: str = field(default="Primal", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Primordial(AlienPower):
    """
    Primordial - Ancient Force.
    Power cannot be canceled.
    """
    name: str = field(default="Primordial", init=False)
    description: str = field(default="Uncancelable power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Transcendent(AlienPower):
    """
    Transcendent - Beyond Normal.
    Play cards from discard.
    """
    name: str = field(default="Transcendent", init=False)
    description: str = field(default="Play from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Universal(AlienPower):
    """
    Universal - Everywhere.
    Ally in all encounters.
    """
    name: str = field(default="Universal", init=False)
    description: str = field(default="Ally everywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Void_Entity(AlienPower):
    """
    Void_Entity - Nothingness.
    Remove cards from game.
    """
    name: str = field(default="Void_Entity", init=False)
    description: str = field(default="Remove cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Celestial())
AlienRegistry.register(Cosmic_Entity())
AlienRegistry.register(Deity())
AlienRegistry.register(Eternal())
AlienRegistry.register(Fate())
AlienRegistry.register(Infinite())
AlienRegistry.register(Omniscient())
AlienRegistry.register(Primal())
AlienRegistry.register(Primordial())
AlienRegistry.register(Transcendent())
AlienRegistry.register(Universal())
AlienRegistry.register(Void_Entity())
