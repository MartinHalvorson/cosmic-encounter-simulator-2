"""
Milestone 7000 Powers for Cosmic Encounter.
Special aliens to commemorate the 7000 alien milestone.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Seven_Thousand(AlienPower):
    """Seven_Thousand - Power of Milestone. +7 always."""
    name: str = field(default="Seven_Thousand", init=False)
    description: str = field(default="+7 constant milestone power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 7
        return total


@dataclass
class Cosmic_Champion(AlienPower):
    """Cosmic_Champion - Power of Victory. +6 always."""
    name: str = field(default="Cosmic_Champion", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Galactic_Legend(AlienPower):
    """Galactic_Legend - Power of Legend. +6 always."""
    name: str = field(default="Galactic_Legend", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Universe_Master(AlienPower):
    """Universe_Master - Power of Mastery. +6 always."""
    name: str = field(default="Universe_Master", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Stellar_Conqueror(AlienPower):
    """Stellar_Conqueror - Power of Conquest. +6 on offense."""
    name: str = field(default="Stellar_Conqueror", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Infinity_Guardian(AlienPower):
    """Infinity_Guardian - Power of Infinity. +6 on defense."""
    name: str = field(default="Infinity_Guardian", init=False)
    description: str = field(default="+6 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


MILESTONE_7000_POWERS = [
    Seven_Thousand, Cosmic_Champion, Galactic_Legend,
    Universe_Master, Stellar_Conqueror, Infinity_Guardian,
]

for power_class in MILESTONE_7000_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
