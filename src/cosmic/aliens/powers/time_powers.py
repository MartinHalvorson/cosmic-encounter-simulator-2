"""
Time Powers - Aliens with temporal abilities.
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
class Accelerator(AlienPower):
    """
    Accelerator - Speed Up.
    Take two encounters per turn.
    """
    name: str = field(default="Accelerator", init=False)
    description: str = field(default="Two encounters per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ancient(AlienPower):
    """
    Ancient - Elder Being.
    +1 per turn played.
    """
    name: str = field(default="Ancient", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clock(AlienPower):
    """
    Clock - Time Keeper.
    Know upcoming destiny cards.
    """
    name: str = field(default="Clock", init=False)
    description: str = field(default="See future destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Decayer(AlienPower):
    """
    Decayer - Time Decay.
    Opponent's high cards become lower.
    """
    name: str = field(default="Decayer", init=False)
    description: str = field(default="Decay opponent cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Eternity(AlienPower):
    """
    Eternity - Endless Time.
    Recover cards from discard pile.
    """
    name: str = field(default="Eternity", init=False)
    description: str = field(default="Recover discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Faster(AlienPower):
    """
    Faster - Quick Action.
    Act before opponent can respond.
    """
    name: str = field(default="Faster", init=False)
    description: str = field(default="Act before response.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hourglass(AlienPower):
    """
    Hourglass - Time Limit.
    End encounters faster.
    """
    name: str = field(default="Hourglass", init=False)
    description: str = field(default="Speed encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Moment(AlienPower):
    """
    Moment - Freeze Time.
    Cancel ally participation.
    """
    name: str = field(default="Moment", init=False)
    description: str = field(default="Cancel allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Past(AlienPower):
    """
    Past - Historic.
    Use cards from discard pile.
    """
    name: str = field(default="Past", init=False)
    description: str = field(default="Use discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pauser(AlienPower):
    """
    Pauser - Time Stop.
    Pause encounter for one round.
    """
    name: str = field(default="Pauser", init=False)
    description: str = field(default="Pause encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rewinder(AlienPower):
    """
    Rewinder - Time Rewind.
    Undo last action.
    """
    name: str = field(default="Rewinder", init=False)
    description: str = field(default="Undo action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Slowdown(AlienPower):
    """
    Slowdown - Slow Time.
    Opponent can't use powers this encounter.
    """
    name: str = field(default="Slowdown", init=False)
    description: str = field(default="Block opponent power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Timewarp(AlienPower):
    """
    Timewarp - Time Warp.
    Switch encounter order.
    """
    name: str = field(default="Timewarp", init=False)
    description: str = field(default="Switch order.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tomorrow(AlienPower):
    """
    Tomorrow - Future Self.
    Look at next cosmic cards.
    """
    name: str = field(default="Tomorrow", init=False)
    description: str = field(default="See future cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Yesterday(AlienPower):
    """
    Yesterday - Past Self.
    Replay previous encounter card.
    """
    name: str = field(default="Yesterday", init=False)
    description: str = field(default="Replay previous card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Accelerator())
AlienRegistry.register(Ancient())
AlienRegistry.register(Clock())
AlienRegistry.register(Decayer())
AlienRegistry.register(Eternity())
AlienRegistry.register(Faster())
AlienRegistry.register(Hourglass())
AlienRegistry.register(Moment())
AlienRegistry.register(Past())
AlienRegistry.register(Pauser())
AlienRegistry.register(Rewinder())
AlienRegistry.register(Slowdown())
AlienRegistry.register(Timewarp())
AlienRegistry.register(Tomorrow())
AlienRegistry.register(Yesterday())
