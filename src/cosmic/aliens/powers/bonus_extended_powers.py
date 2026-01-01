"""
Bonus Extended Powers - More bonus-themed aliens.
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
class Plus1(AlienPower):
    """Plus1 - Minimal Bonus. +1 always."""
    name: str = field(default="Plus1", init=False)
    description: str = field(default="+1 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 1
        return total


@dataclass
class Plus2(AlienPower):
    """Plus2 - Small Bonus. +2 always."""
    name: str = field(default="Plus2", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Plus3(AlienPower):
    """Plus3 - Medium Bonus. +3 always."""
    name: str = field(default="Plus3", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Plus4(AlienPower):
    """Plus4 - Good Bonus. +4 always."""
    name: str = field(default="Plus4", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Plus5(AlienPower):
    """Plus5 - Strong Bonus. +5 always."""
    name: str = field(default="Plus5", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class OffenseBoost(AlienPower):
    """OffenseBoost - Attack Power. +6 on offense."""
    name: str = field(default="OffenseBoost", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class DefenseBoost(AlienPower):
    """DefenseBoost - Defense Power. +6 on defense."""
    name: str = field(default="DefenseBoost", init=False)
    description: str = field(default="+6 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class AllyBoost(AlienPower):
    """AllyBoost - Team Power. +2 per ally."""
    name: str = field(default="AllyBoost", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class ShipBoost(AlienPower):
    """ShipBoost - Fleet Power. +2 per ship."""
    name: str = field(default="ShipBoost", init=False)
    description: str = field(default="+2 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class ColonyBoost(AlienPower):
    """ColonyBoost - Territory Power. +2 per colony."""
    name: str = field(default="ColonyBoost", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class CardBoost(AlienPower):
    """CardBoost - Hand Power. +1 per card."""
    name: str = field(default="CardBoost", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class WarpBoost(AlienPower):
    """WarpBoost - Warp Power. +1 per ship in warp."""
    name: str = field(default="WarpBoost", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class HomeBoost(AlienPower):
    """HomeBoost - Home Power. +2 per home colony."""
    name: str = field(default="HomeBoost", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class RandomBoost(AlienPower):
    """RandomBoost - Lucky Power. +1 to +8 random."""
    name: str = field(default="RandomBoost", init=False)
    description: str = field(default="Random +1 to +8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 8)
        return total


@dataclass
class ConditionalBoost(AlienPower):
    """ConditionalBoost - Situational Power. +5 when outnumbered."""
    name: str = field(default="ConditionalBoost", init=False)
    description: str = field(default="+5 when facing more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class UnderDogBoost(AlienPower):
    """UnderDogBoost - Comeback Power. +6 when behind."""
    name: str = field(default="UnderDogBoost", init=False)
    description: str = field(default="+6 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class LeaderBoost(AlienPower):
    """LeaderBoost - Domination Power. +4 when ahead."""
    name: str = field(default="LeaderBoost", init=False)
    description: str = field(default="+4 when ahead in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class TieBoost(AlienPower):
    """TieBoost - Balance Power. Win ties."""
    name: str = field(default="TieBoost", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class FirstBoost(AlienPower):
    """FirstBoost - Early Power. +5 first encounter."""
    name: str = field(default="FirstBoost", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
BONUS_EXTENDED_POWERS = [
    Plus1, Plus2, Plus3, Plus4, Plus5, OffenseBoost, DefenseBoost, AllyBoost, ShipBoost,
    ColonyBoost, CardBoost, WarpBoost, HomeBoost, RandomBoost, ConditionalBoost,
    UnderDogBoost, LeaderBoost, TieBoost, FirstBoost,
]

for power_class in BONUS_EXTENDED_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
