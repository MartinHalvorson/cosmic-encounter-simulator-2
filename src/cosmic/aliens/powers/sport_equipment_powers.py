"""
Sport Equipment themed alien powers for Cosmic Encounter.
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
class Ball_Sport(AlienPower):
    """Ball - Power of Bouncing."""
    name: str = field(default="Ball_Sport", init=False)
    description: str = field(default="Ships return to colonies instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bat_Sport(AlienPower):
    """Bat - Power of Hitting."""
    name: str = field(default="Bat_Sport", init=False)
    description: str = field(default="+4 when playing attack 20+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goal(AlienPower):
    """Goal - Power of Scoring."""
    name: str = field(default="Goal", init=False)
    description: str = field(default="Win gives +1 colony marker.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Net_Sport(AlienPower):
    """Net - Power of Catching."""
    name: str = field(default="Net_Sport", init=False)
    description: str = field(default="Capture one enemy ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Racket(AlienPower):
    """Racket - Power of Returning."""
    name: str = field(default="Racket", init=False)
    description: str = field(default="Return opponent's attack card to hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Whistle(AlienPower):
    """Whistle - Power of Stopping."""
    name: str = field(default="Whistle", init=False)
    description: str = field(default="Stop encounter and force redraw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Trophy(AlienPower):
    """Trophy - Power of Achievement."""
    name: str = field(default="Trophy", init=False)
    description: str = field(default="+2 for each win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Medal(AlienPower):
    """Medal - Power of Honor."""
    name: str = field(default="Medal", init=False)
    description: str = field(default="+3 when defending successfully.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Puck(AlienPower):
    """Puck - Power of Sliding."""
    name: str = field(default="Puck", init=False)
    description: str = field(default="Ships slide to adjacent planets on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Helmet_Sport(AlienPower):
    """Helmet - Power of Protection."""
    name: str = field(default="Helmet_Sport", init=False)
    description: str = field(default="First ship each encounter is protected.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Ball_Sport())
AlienRegistry.register(Bat_Sport())
AlienRegistry.register(Goal())
AlienRegistry.register(Net_Sport())
AlienRegistry.register(Racket())
AlienRegistry.register(Whistle())
AlienRegistry.register(Trophy())
AlienRegistry.register(Medal())
AlienRegistry.register(Puck())
AlienRegistry.register(Helmet_Sport())
