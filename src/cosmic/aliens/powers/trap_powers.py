"""
Trap Powers - Aliens with ambush and snare abilities.
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
class Ambush(AlienPower):
    """
    Ambush - Surprise Attack.
    +4 when defending home.
    """
    name: str = field(default="Ambush", init=False)
    description: str = field(default="+4 home defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when defending home."""
        if side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Catcher(AlienPower):
    """
    Catcher - Catch Ships.
    Capture attacking ships.
    """
    name: str = field(default="Catcher", init=False)
    description: str = field(default="Capture ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Entangler(AlienPower):
    """
    Entangler - Trap in Web.
    Ships can't retreat.
    """
    name: str = field(default="Entangler", init=False)
    description: str = field(default="No retreat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lurer(AlienPower):
    """
    Lurer - Draw In.
    Force extra ships to attack.
    """
    name: str = field(default="Lurer", init=False)
    description: str = field(default="Force extra ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Miner(AlienPower):
    """
    Miner - Place Mines.
    Damage ships on planets.
    """
    name: str = field(default="Miner", init=False)
    description: str = field(default="Mine planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Netter(AlienPower):
    """
    Netter - Catch in Net.
    Hold ships for a turn.
    """
    name: str = field(default="Netter", init=False)
    description: str = field(default="Hold ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pitfall(AlienPower):
    """
    Pitfall - Hidden Trap.
    Ships fall to warp.
    """
    name: str = field(default="Pitfall", init=False)
    description: str = field(default="Warp trap.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quicksand(AlienPower):
    """
    Quicksand - Sink Slowly.
    Ships lose power over turns.
    """
    name: str = field(default="Quicksand", init=False)
    description: str = field(default="Gradual sink.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Snare(AlienPower):
    """
    Snare - Set Snare.
    Trap attacker for turn.
    """
    name: str = field(default="Snare", init=False)
    description: str = field(default="Trap attacker.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tangler(AlienPower):
    """
    Tangler - Tangle Up.
    -2 to tangled opponent.
    """
    name: str = field(default="Tangler", init=False)
    description: str = field(default="-2 opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trapper(AlienPower):
    """
    Trapper - Master Trapper.
    Set multiple traps.
    """
    name: str = field(default="Trapper", init=False)
    description: str = field(default="Multiple traps.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tripwire(AlienPower):
    """
    Tripwire - Set Wire.
    First ship lost.
    """
    name: str = field(default="Tripwire", init=False)
    description: str = field(default="Lose first ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Venus(AlienPower):
    """
    Venus - Flytrap.
    Lure and catch ships.
    """
    name: str = field(default="Venus", init=False)
    description: str = field(default="Lure and catch.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Web(AlienPower):
    """
    Web - Spin Web.
    Hold all ships.
    """
    name: str = field(default="Web", init=False)
    description: str = field(default="Hold all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ambush())
AlienRegistry.register(Catcher())
AlienRegistry.register(Entangler())
AlienRegistry.register(Lurer())
AlienRegistry.register(Miner())
AlienRegistry.register(Netter())
AlienRegistry.register(Pitfall())
AlienRegistry.register(Quicksand())
AlienRegistry.register(Snare())
AlienRegistry.register(Tangler())
AlienRegistry.register(Trapper())
AlienRegistry.register(Tripwire())
AlienRegistry.register(Venus())
AlienRegistry.register(Web())
