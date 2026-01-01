"""
Speed Powers - Aliens with fast and agile abilities.
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
class Blitz(AlienPower):
    """
    Blitz - Lightning Attack.
    Extra encounter if you win quickly.
    """
    name: str = field(default="Blitz", init=False)
    description: str = field(default="Fast extra turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chaser(AlienPower):
    """
    Chaser - Pursue Target.
    Attack same player twice.
    """
    name: str = field(default="Chaser", init=False)
    description: str = field(default="Attack twice.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dasher(AlienPower):
    """
    Dasher - Quick Move.
    Ships move faster.
    """
    name: str = field(default="Dasher", init=False)
    description: str = field(default="Fast ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Express(AlienPower):
    """
    Express - Rapid Delivery.
    Ships arrive instantly.
    """
    name: str = field(default="Express", init=False)
    description: str = field(default="Instant arrival.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hasty(AlienPower):
    """
    Hasty - Rush Action.
    Act before opponent.
    """
    name: str = field(default="Hasty", init=False)
    description: str = field(default="Act first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quicken(AlienPower):
    """
    Quicken - Speed Up.
    +2 per ship committed.
    """
    name: str = field(default="Quicken", init=False)
    description: str = field(default="+2 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Racer(AlienPower):
    """
    Racer - Fast Mover.
    Move ships between planets.
    """
    name: str = field(default="Racer", init=False)
    description: str = field(default="Move ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rapid(AlienPower):
    """
    Rapid - Quick Strike.
    First strike advantage.
    """
    name: str = field(default="Rapid", init=False)
    description: str = field(default="First strike.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Runner(AlienPower):
    """
    Runner - Escape Speed.
    Ships escape to colonies.
    """
    name: str = field(default="Runner", init=False)
    description: str = field(default="Escape ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rusher(AlienPower):
    """
    Rusher - Rush Attack.
    Attack without warning.
    """
    name: str = field(default="Rusher", init=False)
    description: str = field(default="Surprise attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Speeder(AlienPower):
    """
    Speeder - High Speed.
    Skip phases.
    """
    name: str = field(default="Speeder", init=False)
    description: str = field(default="Skip phases.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sprint(AlienPower):
    """
    Sprint - Burst Speed.
    Extra action once per turn.
    """
    name: str = field(default="Sprint", init=False)
    description: str = field(default="Extra action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Streaker(AlienPower):
    """
    Streaker - Lightning Fast.
    Win ties.
    """
    name: str = field(default="Streaker", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swift(AlienPower):
    """
    Swift - Quick Response.
    React to opponent actions.
    """
    name: str = field(default="Swift", init=False)
    description: str = field(default="Quick react.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Velocity(AlienPower):
    """
    Velocity - Maximum Speed.
    +4 when attacking.
    """
    name: str = field(default="Velocity", init=False)
    description: str = field(default="+4 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking."""
        if side == Side.OFFENSE:
            return total + 4
        return total


# Register all powers
AlienRegistry.register(Blitz())
AlienRegistry.register(Chaser())
AlienRegistry.register(Dasher())
AlienRegistry.register(Express())
AlienRegistry.register(Hasty())
AlienRegistry.register(Quicken())
AlienRegistry.register(Racer())
AlienRegistry.register(Rapid())
AlienRegistry.register(Runner())
AlienRegistry.register(Rusher())
AlienRegistry.register(Speeder())
AlienRegistry.register(Sprint())
AlienRegistry.register(Streaker())
AlienRegistry.register(Swift())
AlienRegistry.register(Velocity())
