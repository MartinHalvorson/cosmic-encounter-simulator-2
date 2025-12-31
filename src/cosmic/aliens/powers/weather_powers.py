"""
Weather Powers - Aliens with climate and atmospheric abilities.
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
class Blizzard(AlienPower):
    """
    Blizzard - Freeze All.
    Slow opponent's ships.
    """
    name: str = field(default="Blizzard", init=False)
    description: str = field(default="Slow ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Clouder(AlienPower):
    """
    Clouder - Cover Field.
    Hide encounter cards.
    """
    name: str = field(default="Clouder", init=False)
    description: str = field(default="Hide cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cyclone(AlienPower):
    """
    Cyclone - Scatter Ships.
    Redistribute ships randomly.
    """
    name: str = field(default="Cyclone", init=False)
    description: str = field(default="Scatter ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Drought(AlienPower):
    """
    Drought - Dry Up.
    Opponent loses cards.
    """
    name: str = field(default="Drought", init=False)
    description: str = field(default="Opponent loses cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fogger(AlienPower):
    """
    Fogger - Create Fog.
    Cards played face down.
    """
    name: str = field(default="Fogger", init=False)
    description: str = field(default="Face down cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Frost(AlienPower):
    """
    Frost - Freeze Ships.
    One ship can't move.
    """
    name: str = field(default="Frost", init=False)
    description: str = field(default="Freeze ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hail(AlienPower):
    """
    Hail - Damage All.
    All sides lose 1 ship.
    """
    name: str = field(default="Hail", init=False)
    description: str = field(default="All lose 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hurricane(AlienPower):
    """
    Hurricane - Massive Force.
    +5 or -5 randomly.
    """
    name: str = field(default="Hurricane", init=False)
    description: str = field(default="+5 or -5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 or -5 randomly."""
        return total + random.choice([5, -5])


@dataclass
class Lightning(AlienPower):
    """
    Lightning - Strike Fast.
    Instant kill one ship.
    """
    name: str = field(default="Lightning", init=False)
    description: str = field(default="Kill one ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monsoon(AlienPower):
    """
    Monsoon - Flood Zone.
    Extra encounter after rain.
    """
    name: str = field(default="Monsoon", init=False)
    description: str = field(default="Extra encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rainbow(AlienPower):
    """
    Rainbow - Good Fortune.
    Draw card after win.
    """
    name: str = field(default="Rainbow", init=False)
    description: str = field(default="Draw on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stormer(AlienPower):
    """
    Stormer - Create Storm.
    -2 to all opponents.
    """
    name: str = field(default="Stormer", init=False)
    description: str = field(default="-2 opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sunshine(AlienPower):
    """
    Sunshine - Bright Light.
    Reveal hidden cards.
    """
    name: str = field(default="Sunshine", init=False)
    description: str = field(default="Reveal hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thunder(AlienPower):
    """
    Thunder - Loud Boom.
    Cancel artifacts.
    """
    name: str = field(default="Thunder", init=False)
    description: str = field(default="Cancel artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tornado(AlienPower):
    """
    Tornado - Spin Attack.
    Move opponent ships.
    """
    name: str = field(default="Tornado", init=False)
    description: str = field(default="Move opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wind(AlienPower):
    """
    Wind - Push Away.
    Prevent one ally.
    """
    name: str = field(default="Wind", init=False)
    description: str = field(default="Block one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Blizzard())
AlienRegistry.register(Clouder())
AlienRegistry.register(Cyclone())
AlienRegistry.register(Drought())
AlienRegistry.register(Fogger())
AlienRegistry.register(Frost())
AlienRegistry.register(Hail())
AlienRegistry.register(Hurricane())
AlienRegistry.register(Lightning())
AlienRegistry.register(Monsoon())
AlienRegistry.register(Rainbow())
AlienRegistry.register(Stormer())
AlienRegistry.register(Sunshine())
AlienRegistry.register(Thunder())
AlienRegistry.register(Tornado())
AlienRegistry.register(Wind())
