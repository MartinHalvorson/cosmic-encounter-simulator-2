"""
State Powers - Physical and mental state themed aliens.
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
class Solid(AlienPower):
    """Solid - Power of Firmness. +4 on defense."""
    name: str = field(default="Solid", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Liquid(AlienPower):
    """Liquid - Power of Flow. Move ships freely."""
    name: str = field(default="Liquid", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gas(AlienPower):
    """Gas - Power of Expansion. +1 per colony."""
    name: str = field(default="Gas", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Frozen(AlienPower):
    """Frozen - Power of Stasis. Lock ships."""
    name: str = field(default="Frozen", init=False)
    description: str = field(default="Ships on your planets stay.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Burning(AlienPower):
    """Burning - Power of Fire. +5 on offense."""
    name: str = field(default="Burning", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Melting(AlienPower):
    """Melting - Power of Change. Transform cards."""
    name: str = field(default="Melting", init=False)
    description: str = field(default="Treat attack as negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Awake(AlienPower):
    """Awake - Power of Alertness. Extra encounters."""
    name: str = field(default="Awake", init=False)
    description: str = field(default="Take third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Asleep(AlienPower):
    """Asleep - Power of Rest. Retrieve ships."""
    name: str = field(default="Asleep", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Alive(AlienPower):
    """Alive - Power of Life. Ships avoid warp."""
    name: str = field(default="Alive", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dead(AlienPower):
    """Dead - Power of Death. Ships removed permanently."""
    name: str = field(default="Dead", init=False)
    description: str = field(default="Losing ships removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hungry(AlienPower):
    """Hungry - Power of Consumption. Take cards."""
    name: str = field(default="Hungry", init=False)
    description: str = field(default="Take 1 card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Full(AlienPower):
    """Full - Power of Satiation. No hand limit."""
    name: str = field(default="Full", init=False)
    description: str = field(default="Never discard down.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Strong(AlienPower):
    """Strong - Power of Strength. +4 always."""
    name: str = field(default="Strong", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Weak(AlienPower):
    """Weak - Power of Frailty. +6 with low cards."""
    name: str = field(default="Weak", init=False)
    description: str = field(default="+6 when card under 8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fast(AlienPower):
    """Fast - Power of Speed. +3 first encounter."""
    name: str = field(default="Fast", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Slow(AlienPower):
    """Slow - Power of Patience. +1 per turn."""
    name: str = field(default="Slow", init=False)
    description: str = field(default="+1 per turn number.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Visible(AlienPower):
    """Visible - Power of Clarity. All see cards."""
    name: str = field(default="Visible", init=False)
    description: str = field(default="All cards revealed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hidden(AlienPower):
    """Hidden - Power of Secrecy. Card stays hidden."""
    name: str = field(default="Hidden", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Angry(AlienPower):
    """Angry - Power of Rage. +5 on offense."""
    name: str = field(default="Angry", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Calm(AlienPower):
    """Calm - Power of Peace. Deal bonus."""
    name: str = field(default="Calm", init=False)
    description: str = field(default="+3 cards when negotiating.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
STATE_POWERS = [
    Solid, Liquid, Gas, Frozen, Burning, Melting, Awake, Asleep, Alive, Dead,
    Hungry, Full, Strong, Weak, Fast, Slow, Visible, Hidden, Angry, Calm,
]

for power_class in STATE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
