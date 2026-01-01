"""
Motion Powers - Movement and motion themed aliens.
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
class Mover(AlienPower):
    """Mover - Power of Motion. Move ships freely."""
    name: str = field(default="Mover", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sprinter(AlienPower):
    """Sprinter - Power of Speed. +4 first encounter."""
    name: str = field(default="Sprinter", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jogger(AlienPower):
    """Jogger - Power of Steady. +2 always."""
    name: str = field(default="Jogger", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Crawler(AlienPower):
    """Crawler - Power of Persistence. +1 per turn."""
    name: str = field(default="Crawler", init=False)
    description: str = field(default="+1 per turn number.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Leaper(AlienPower):
    """Leaper - Power of Jumping. Skip phases."""
    name: str = field(default="Leaper", init=False)
    description: str = field(default="Skip alliance phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Glider(AlienPower):
    """Glider - Power of Soaring. Ships avoid warp."""
    name: str = field(default="Glider", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Slider(AlienPower):
    """Slider - Power of Gliding. Move after win."""
    name: str = field(default="Slider", init=False)
    description: str = field(default="Move 2 ships after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Roller(AlienPower):
    """Roller - Power of Rolling. Random bonus."""
    name: str = field(default="Roller", init=False)
    description: str = field(default="Random +1 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 6)
        return total


@dataclass
class Spinner(AlienPower):
    """Spinner - Power of Rotation. +3 on defense."""
    name: str = field(default="Spinner", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Swinger(AlienPower):
    """Swinger - Power of Oscillation. +4 or -2."""
    name: str = field(default="Swinger", init=False)
    description: str = field(default="+4 or -2 (random).", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (4 if random.random() > 0.5 else -2)
        return total


@dataclass
class Bouncer(AlienPower):
    """Bouncer - Power of Rebound. +2 on loss."""
    name: str = field(default="Bouncer", init=False)
    description: str = field(default="Draw 2 cards when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Floater_Alt(AlienPower):
    """Floater_Alt - Power of Buoyancy. Ships escape."""
    name: str = field(default="Floater_Alt", init=False)
    description: str = field(default="Retrieve 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drifter(AlienPower):
    """Drifter - Power of Wandering. Ignore destiny."""
    name: str = field(default="Drifter", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Charger(AlienPower):
    """Charger - Power of Rush. +5 with max ships."""
    name: str = field(default="Charger", init=False)
    description: str = field(default="+5 when committing 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Retreater(AlienPower):
    """Retreater - Power of Withdrawal. Escape encounters."""
    name: str = field(default="Retreater", init=False)
    description: str = field(default="Withdraw before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
MOTION_POWERS = [
    Mover, Sprinter, Jogger, Crawler, Leaper, Glider, Slider, Roller, Spinner, Swinger,
    Bouncer, Floater_Alt, Drifter, Charger, Retreater,
]

for power_class in MOTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
