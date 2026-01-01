"""
Growth Powers - Aliens with expansion and multiplication abilities.
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
class Bloomer(AlienPower):
    """
    Bloomer - Rapid Growth.
    Gain ship per colony.
    """
    name: str = field(default="Bloomer", init=False)
    description: str = field(default="Ship per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Breeder(AlienPower):
    """
    Breeder - Multiply Ships.
    Double ships on win.
    """
    name: str = field(default="Breeder", init=False)
    description: str = field(default="Double on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Colonizer(AlienPower):
    """
    Colonizer - Rapid Expansion.
    Place extra colony on win.
    """
    name: str = field(default="Colonizer", init=False)
    description: str = field(default="Extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cultivator(AlienPower):
    """
    Cultivator - Grow Resources.
    Cards grow in value.
    """
    name: str = field(default="Cultivator", init=False)
    description: str = field(default="Cards grow.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Developer(AlienPower):
    """
    Developer - Build Up.
    Improve colonies over time.
    """
    name: str = field(default="Developer", init=False)
    description: str = field(default="Improve colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Doubler(AlienPower):
    """
    Doubler - Double Effect.
    Double ship count once.
    """
    name: str = field(default="Doubler", init=False)
    description: str = field(default="Double ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Evolver(AlienPower):
    """
    Evolver - Adapt and Grow.
    Gain abilities over time.
    """
    name: str = field(default="Evolver", init=False)
    description: str = field(default="Gain abilities.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Expander(AlienPower):
    """
    Expander - Spread Out.
    Extra ship from warp.
    """
    name: str = field(default="Expander", init=False)
    description: str = field(default="Extra from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flourisher(AlienPower):
    """
    Flourisher - Thrive.
    +1 per turn played.
    """
    name: str = field(default="Flourisher", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Grower(AlienPower):
    """
    Grower - Steady Growth.
    Gain card per encounter.
    """
    name: str = field(default="Grower", init=False)
    description: str = field(default="Card per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Harvester(AlienPower):
    """
    Harvester - Collect Resources.
    Take cards from wins.
    """
    name: str = field(default="Harvester", init=False)
    description: str = field(default="Cards from wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Multiplier(AlienPower):
    """
    Multiplier - Multiply Effect.
    Triple card effect once.
    """
    name: str = field(default="Multiplier", init=False)
    description: str = field(default="Triple effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Nurturer(AlienPower):
    """
    Nurturer - Care for Ships.
    Ships immune to half losses.
    """
    name: str = field(default="Nurturer", init=False)
    description: str = field(default="Half losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Propagator(AlienPower):
    """
    Propagator - Spread Wide.
    Place ships on multiple planets.
    """
    name: str = field(default="Propagator", init=False)
    description: str = field(default="Multiple planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Reproducer(AlienPower):
    """
    Reproducer - Create Ships.
    Gain ship per turn.
    """
    name: str = field(default="Reproducer", init=False)
    description: str = field(default="Ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scaler(AlienPower):
    """
    Scaler - Scale Up.
    Power grows with colonies.
    """
    name: str = field(default="Scaler", init=False)
    description: str = field(default="Scale with colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seedling(AlienPower):
    """
    Seedling - Plant Seeds.
    Place tokens on planets.
    """
    name: str = field(default="Seedling", init=False)
    description: str = field(default="Plant tokens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spreader(AlienPower):
    """
    Spreader - Extend Reach.
    Attack additional planets.
    """
    name: str = field(default="Spreader", init=False)
    description: str = field(default="Extra attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Bloomer())
AlienRegistry.register(Breeder())
AlienRegistry.register(Colonizer())
AlienRegistry.register(Cultivator())
AlienRegistry.register(Developer())
AlienRegistry.register(Doubler())
AlienRegistry.register(Evolver())
AlienRegistry.register(Expander())
AlienRegistry.register(Flourisher())
AlienRegistry.register(Grower())
AlienRegistry.register(Harvester())
AlienRegistry.register(Multiplier())
AlienRegistry.register(Nurturer())
AlienRegistry.register(Propagator())
AlienRegistry.register(Reproducer())
AlienRegistry.register(Scaler())
AlienRegistry.register(Seedling())
AlienRegistry.register(Spreader())
