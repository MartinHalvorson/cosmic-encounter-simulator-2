"""
Milestone 7500 Powers for Cosmic Encounter.
Special celebration aliens to reach the 7500 milestone!
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
class Seventy_Five_Hundred(AlienPower):
    """Seventy_Five_Hundred - Power of Milestone. +7 always."""
    name: str = field(default="Seventy_Five_Hundred", init=False)
    description: str = field(default="+7 constant milestone power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 7
        return total


@dataclass
class Grand_Achievement(AlienPower):
    """Grand_Achievement - Power of Accomplishment. +6 always."""
    name: str = field(default="Grand_Achievement", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Cosmic_Triumph(AlienPower):
    """Cosmic_Triumph - Power of Victory. +6 always."""
    name: str = field(default="Cosmic_Triumph", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Stellar_Summit(AlienPower):
    """Stellar_Summit - Power of Peak. +6 always."""
    name: str = field(default="Stellar_Summit", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Galactic_Glory(AlienPower):
    """Galactic_Glory - Power of Fame. +6 always."""
    name: str = field(default="Galactic_Glory", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Ultimate_Expansion(AlienPower):
    """Ultimate_Expansion - Power of Growth. +6 always."""
    name: str = field(default="Ultimate_Expansion", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


MILESTONE_7500_POWERS = [
    Seventy_Five_Hundred, Grand_Achievement, Cosmic_Triumph,
    Stellar_Summit, Galactic_Glory, Ultimate_Expansion,
]

for power_class in MILESTONE_7500_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
