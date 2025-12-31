"""
Sin Powers - Seven deadly sins themed aliens.
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
class Greed(AlienPower):
    """Greed - Power of Want. Extra cards."""
    name: str = field(default="Greed", init=False)
    description: str = field(default="Draw 2 extra cards each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wrath(AlienPower):
    """Wrath - Power of Anger. +5 on offense."""
    name: str = field(default="Wrath", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Envy(AlienPower):
    """Envy - Power of Jealousy. Copy opponent power."""
    name: str = field(default="Envy", init=False)
    description: str = field(default="Use opponent's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Sloth(AlienPower):
    """Sloth - Power of Laziness. Skip requirements."""
    name: str = field(default="Sloth", init=False)
    description: str = field(default="Commit 0 ships and still count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gluttony(AlienPower):
    """Gluttony - Power of Excess. Never discard down."""
    name: str = field(default="Gluttony", init=False)
    description: str = field(default="No hand limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lust(AlienPower):
    """Lust - Power of Desire. Compel allies."""
    name: str = field(default="Lust", init=False)
    description: str = field(default="Force 1 player to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pride_Alt(AlienPower):
    """Pride_Alt - Power of Ego. +4 when ahead."""
    name: str = field(default="Pride_Alt", init=False)
    description: str = field(default="+4 when ahead in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Avarice(AlienPower):
    """Avarice - Power of Hoarding. Steal cards."""
    name: str = field(default="Avarice", init=False)
    description: str = field(default="Take 1 card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vanity(AlienPower):
    """Vanity - Power of Self-Love. Win ties."""
    name: str = field(default="Vanity", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Malice(AlienPower):
    """Malice - Power of Ill-Will. -3 to opponent."""
    name: str = field(default="Malice", init=False)
    description: str = field(default="Opponent gets -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cruelty(AlienPower):
    """Cruelty - Power of Harm. Extra damage."""
    name: str = field(default="Cruelty", init=False)
    description: str = field(default="Opponent loses extra ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spite(AlienPower):
    """Spite - Power of Resentment. Damage on loss."""
    name: str = field(default="Spite", init=False)
    description: str = field(default="Winner loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deceit(AlienPower):
    """Deceit - Power of Lies. Fake card value."""
    name: str = field(default="Deceit", init=False)
    description: str = field(default="Announce false value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Treachery(AlienPower):
    """Treachery - Power of Betrayal. Switch sides."""
    name: str = field(default="Treachery", init=False)
    description: str = field(default="Switch ally to other side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Cowardice(AlienPower):
    """Cowardice - Power of Retreat. Escape losses."""
    name: str = field(default="Cowardice", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
SIN_POWERS = [
    Greed, Wrath, Envy, Sloth, Gluttony, Lust, Pride_Alt, Avarice, Vanity, Malice,
    Cruelty, Spite, Deceit, Treachery, Cowardice,
]

for power_class in SIN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
