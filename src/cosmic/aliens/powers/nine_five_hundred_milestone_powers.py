"""
9500 Milestone Powers for Cosmic Encounter.
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
class Ninety_Five_Hundred_Alpha(AlienPower):
    """Ninety_Five_Hundred_Alpha - Power of Alpha. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Alpha", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Beta(AlienPower):
    """Ninety_Five_Hundred_Beta - Power of Beta. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Beta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Gamma(AlienPower):
    """Ninety_Five_Hundred_Gamma - Power of Gamma. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Gamma", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Delta(AlienPower):
    """Ninety_Five_Hundred_Delta - Power of Delta. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Delta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Epsilon(AlienPower):
    """Ninety_Five_Hundred_Epsilon - Power of Epsilon. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Epsilon", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Zeta(AlienPower):
    """Ninety_Five_Hundred_Zeta - Power of Zeta. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Zeta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Eta(AlienPower):
    """Ninety_Five_Hundred_Eta - Power of Eta. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Eta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Theta(AlienPower):
    """Ninety_Five_Hundred_Theta - Power of Theta. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Theta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Iota(AlienPower):
    """Ninety_Five_Hundred_Iota - Power of Iota. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Iota", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Kappa(AlienPower):
    """Ninety_Five_Hundred_Kappa - Power of Kappa. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Kappa", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Lambda(AlienPower):
    """Ninety_Five_Hundred_Lambda - Power of Lambda. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Lambda", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Mu(AlienPower):
    """Ninety_Five_Hundred_Mu - Power of Mu. +4 always"""
    name: str = field(default="Ninety_Five_Hundred_Mu", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Ninety_Five_Hundred_Nu(AlienPower):
    """Ninety_Five_Hundred_Nu - Power of Nu. +5 always"""
    name: str = field(default="Ninety_Five_Hundred_Nu", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Ninety_Five_Hundred_Victory(AlienPower):
    """Ninety_Five_Hundred_Victory - Power of Win. +6 always"""
    name: str = field(default="Ninety_Five_Hundred_Victory", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


NINE_FIVE_HUNDRED_MILESTONE_POWERS = [
    Ninety_Five_Hundred_Alpha, Ninety_Five_Hundred_Beta, Ninety_Five_Hundred_Gamma, Ninety_Five_Hundred_Delta, Ninety_Five_Hundred_Epsilon, Ninety_Five_Hundred_Zeta, Ninety_Five_Hundred_Eta,
    Ninety_Five_Hundred_Theta, Ninety_Five_Hundred_Iota, Ninety_Five_Hundred_Kappa, Ninety_Five_Hundred_Lambda, Ninety_Five_Hundred_Mu, Ninety_Five_Hundred_Nu, Ninety_Five_Hundred_Victory,
]

for power_class in NINE_FIVE_HUNDRED_MILESTONE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
