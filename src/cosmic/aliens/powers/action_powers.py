"""
Action Powers - Verb/action-themed aliens.
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
class Striker(AlienPower):
    """Striker - Power of Hitting. +4 on attacks."""
    name: str = field(default="Striker", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Blocker(AlienPower):
    """Blocker - Power of Stopping. +4 on defense."""
    name: str = field(default="Blocker", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Runner(AlienPower):
    """Runner - Power of Speed. Extra encounter option."""
    name: str = field(default="Runner", init=False)
    description: str = field(default="May take third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Grabber(AlienPower):
    """Grabber - Power of Taking. Steal cards."""
    name: str = field(default="Grabber", init=False)
    description: str = field(default="Take 1 card from opponent on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jumper(AlienPower):
    """Jumper - Power of Leaping. Skip phases."""
    name: str = field(default="Jumper", init=False)
    description: str = field(default="Skip alliance phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pusher(AlienPower):
    """Pusher - Power of Force. Push ships around."""
    name: str = field(default="Pusher", init=False)
    description: str = field(default="Move opponent's ships between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Puller(AlienPower):
    """Puller - Power of Attraction. Draw allies."""
    name: str = field(default="Puller", init=False)
    description: str = field(default="Force one player to ally with you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flinger(AlienPower):
    """Flinger - Power of Throwing. Discard to damage."""
    name: str = field(default="Flinger", init=False)
    description: str = field(default="Discard card to send ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dodger(AlienPower):
    """Dodger - Power of Evasion. Avoid losses."""
    name: str = field(default="Dodger", init=False)
    description: str = field(default="Lose 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Breaker(AlienPower):
    """Breaker - Power of Destruction. Remove cards from game."""
    name: str = field(default="Breaker", init=False)
    description: str = field(default="Played cards removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Builder_Alt(AlienPower):
    """Builder_Alt - Power of Creation. Extra ships."""
    name: str = field(default="Builder_Alt", init=False)
    description: str = field(default="Add 1 ship to any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Keeper(AlienPower):
    """Keeper - Power of Holding. Keep cards."""
    name: str = field(default="Keeper", init=False)
    description: str = field(default="Never discard down.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Finder(AlienPower):
    """Finder - Power of Discovery. Search deck."""
    name: str = field(default="Finder", init=False)
    description: str = field(default="Search deck for specific card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Catcher(AlienPower):
    """Catcher - Power of Interception. Catch cards."""
    name: str = field(default="Catcher", init=False)
    description: str = field(default="Take discarded cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kicker(AlienPower):
    """Kicker - Power of the Boot. Remove from encounter."""
    name: str = field(default="Kicker", init=False)
    description: str = field(default="Remove 1 ally from opponent's side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Holder(AlienPower):
    """Holder - Power of Grip. Lock ships."""
    name: str = field(default="Holder", init=False)
    description: str = field(default="Ships on your planets cannot leave.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thrower(AlienPower):
    """Thrower - Power of Distance. Attack far planets."""
    name: str = field(default="Thrower", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dancer_Alt(AlienPower):
    """Dancer_Alt - Power of Grace. Escape encounters."""
    name: str = field(default="Dancer_Alt", init=False)
    description: str = field(default="Withdraw before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Climber(AlienPower):
    """Climber - Power of Ascent. +1 per turn."""
    name: str = field(default="Climber", init=False)
    description: str = field(default="+1 per turn number.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diver(AlienPower):
    """Diver - Power of Depth. Retrieve from warp."""
    name: str = field(default="Diver", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
ACTION_POWERS = [
    Striker, Blocker, Runner, Grabber, Jumper, Pusher, Puller, Flinger, Dodger, Breaker,
    Builder_Alt, Keeper, Finder, Catcher, Kicker, Holder, Thrower, Dancer_Alt, Climber, Diver,
]

for power_class in ACTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
