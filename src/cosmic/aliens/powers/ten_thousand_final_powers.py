"""
10000 Final Powers for Cosmic Encounter.
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
class Final_10K_Victory_A(AlienPower):
    """Final_10K_Victory_A - Power of Win. +5 always"""
    name: str = field(default="Final_10K_Victory_A", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_B(AlienPower):
    """Final_10K_Victory_B - Power of Triumph. +5 always"""
    name: str = field(default="Final_10K_Victory_B", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_C(AlienPower):
    """Final_10K_Victory_C - Power of Glory. +5 always"""
    name: str = field(default="Final_10K_Victory_C", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_D(AlienPower):
    """Final_10K_Victory_D - Power of Honor. +5 always"""
    name: str = field(default="Final_10K_Victory_D", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_E(AlienPower):
    """Final_10K_Victory_E - Power of Success. +5 always"""
    name: str = field(default="Final_10K_Victory_E", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_F(AlienPower):
    """Final_10K_Victory_F - Power of Achievement. +5 always"""
    name: str = field(default="Final_10K_Victory_F", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_G(AlienPower):
    """Final_10K_Victory_G - Power of Milestone. +5 always"""
    name: str = field(default="Final_10K_Victory_G", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_H(AlienPower):
    """Final_10K_Victory_H - Power of Complete. +5 always"""
    name: str = field(default="Final_10K_Victory_H", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_I(AlienPower):
    """Final_10K_Victory_I - Power of Done. +5 always"""
    name: str = field(default="Final_10K_Victory_I", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_J(AlienPower):
    """Final_10K_Victory_J - Power of Finish. +5 always"""
    name: str = field(default="Final_10K_Victory_J", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_K(AlienPower):
    """Final_10K_Victory_K - Power of End. +5 always"""
    name: str = field(default="Final_10K_Victory_K", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Final_10K_Victory_L(AlienPower):
    """Final_10K_Victory_L - Power of Goal. +4 always"""
    name: str = field(default="Final_10K_Victory_L", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Final_10K_Victory_M(AlienPower):
    """Final_10K_Victory_M - Power of Target. +5 always"""
    name: str = field(default="Final_10K_Victory_M", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ten_Thousand_Ultimate_Victory(AlienPower):
    """Ten_Thousand_Ultimate_Victory - Power of Ultimate. +6 always"""
    name: str = field(default="Ten_Thousand_Ultimate_Victory", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


TEN_THOUSAND_FINAL_POWERS = [
    Final_10K_Victory_A, Final_10K_Victory_B, Final_10K_Victory_C, Final_10K_Victory_D, Final_10K_Victory_E, Final_10K_Victory_F, Final_10K_Victory_G,
    Final_10K_Victory_H, Final_10K_Victory_I, Final_10K_Victory_J, Final_10K_Victory_K, Final_10K_Victory_L, Final_10K_Victory_M, Ten_Thousand_Ultimate_Victory,
]

for power_class in TEN_THOUSAND_FINAL_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
