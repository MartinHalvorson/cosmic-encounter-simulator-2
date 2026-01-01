"""
Gravity Powers - Aliens with gravitational and mass abilities.
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
class Attractor(AlienPower):
    """
    Attractor - Pull In.
    Force ships to join.
    """
    name: str = field(default="Attractor", init=False)
    description: str = field(default="Force join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Compressor(AlienPower):
    """
    Compressor - Crush Down.
    -2 to opponent total.
    """
    name: str = field(default="Compressor", init=False)
    description: str = field(default="-2 opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dense(AlienPower):
    """
    Dense - Heavy Mass.
    Ships count as 2.
    """
    name: str = field(default="Dense", init=False)
    description: str = field(default="Ships x2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Floater(AlienPower):
    """
    Floater - Low Gravity.
    Avoid warp.
    """
    name: str = field(default="Floater", init=False)
    description: str = field(default="Avoid warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gravitic(AlienPower):
    """
    Gravitic - Control Gravity.
    Move any ships.
    """
    name: str = field(default="Gravitic", init=False)
    description: str = field(default="Move ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Heavy(AlienPower):
    """
    Heavy - Massive.
    +3 constant bonus.
    """
    name: str = field(default="Heavy", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 constant bonus."""
        return total + 3


@dataclass
class Levitator(AlienPower):
    """
    Levitator - Float Ships.
    Ships can't be lost.
    """
    name: str = field(default="Levitator", init=False)
    description: str = field(default="Protect ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lighter(AlienPower):
    """
    Lighter - Reduce Weight.
    Extra ships in encounter.
    """
    name: str = field(default="Lighter", init=False)
    description: str = field(default="Extra ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Orbit(AlienPower):
    """
    Orbit - Circle Around.
    Return after loss.
    """
    name: str = field(default="Orbit", init=False)
    description: str = field(default="Return on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Puller(AlienPower):
    """
    Puller - Gravity Well.
    Draw cards to you.
    """
    name: str = field(default="Puller", init=False)
    description: str = field(default="Draw cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pusher(AlienPower):
    """
    Pusher - Repel Force.
    Send ships away.
    """
    name: str = field(default="Pusher", init=False)
    description: str = field(default="Repel ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Singularity(AlienPower):
    """
    Singularity - Event Horizon.
    Destroy all ships.
    """
    name: str = field(default="Singularity", init=False)
    description: str = field(default="Destroy all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tidal(AlienPower):
    """
    Tidal - Gravity Waves.
    Shift ship positions.
    """
    name: str = field(default="Tidal", init=False)
    description: str = field(default="Shift ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Weightless(AlienPower):
    """
    Weightless - No Mass.
    Move freely.
    """
    name: str = field(default="Weightless", init=False)
    description: str = field(default="Free movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Attractor())
AlienRegistry.register(Compressor())
AlienRegistry.register(Dense())
AlienRegistry.register(Floater())
AlienRegistry.register(Gravitic())
AlienRegistry.register(Heavy())
AlienRegistry.register(Levitator())
AlienRegistry.register(Lighter())
AlienRegistry.register(Orbit())
AlienRegistry.register(Puller())
AlienRegistry.register(Pusher())
AlienRegistry.register(Singularity())
AlienRegistry.register(Tidal())
AlienRegistry.register(Weightless())
