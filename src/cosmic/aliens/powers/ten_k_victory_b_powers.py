"""
10K Victory B Powers for Cosmic Encounter.
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
class Triumph_10K_Alpha(AlienPower):
    """Triumph_10K_Alpha - Power of Alpha. +5 always"""
    name: str = field(default="Triumph_10K_Alpha", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Beta(AlienPower):
    """Triumph_10K_Beta - Power of Beta. +5 always"""
    name: str = field(default="Triumph_10K_Beta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Gamma(AlienPower):
    """Triumph_10K_Gamma - Power of Gamma. +5 always"""
    name: str = field(default="Triumph_10K_Gamma", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Delta(AlienPower):
    """Triumph_10K_Delta - Power of Delta. +5 always"""
    name: str = field(default="Triumph_10K_Delta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Epsilon(AlienPower):
    """Triumph_10K_Epsilon - Power of Epsilon. +5 always"""
    name: str = field(default="Triumph_10K_Epsilon", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Zeta(AlienPower):
    """Triumph_10K_Zeta - Power of Zeta. +5 always"""
    name: str = field(default="Triumph_10K_Zeta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Eta(AlienPower):
    """Triumph_10K_Eta - Power of Eta. +5 always"""
    name: str = field(default="Triumph_10K_Eta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Theta(AlienPower):
    """Triumph_10K_Theta - Power of Theta. +5 always"""
    name: str = field(default="Triumph_10K_Theta", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Iota(AlienPower):
    """Triumph_10K_Iota - Power of Iota. +5 always"""
    name: str = field(default="Triumph_10K_Iota", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Kappa(AlienPower):
    """Triumph_10K_Kappa - Power of Kappa. +5 always"""
    name: str = field(default="Triumph_10K_Kappa", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Lambda(AlienPower):
    """Triumph_10K_Lambda - Power of Lambda. +5 always"""
    name: str = field(default="Triumph_10K_Lambda", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Mu(AlienPower):
    """Triumph_10K_Mu - Power of Mu. +4 always"""
    name: str = field(default="Triumph_10K_Mu", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Triumph_10K_Nu(AlienPower):
    """Triumph_10K_Nu - Power of Nu. +5 always"""
    name: str = field(default="Triumph_10K_Nu", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Triumph_10K_Xi(AlienPower):
    """Triumph_10K_Xi - Power of Xi. +6 always"""
    name: str = field(default="Triumph_10K_Xi", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


TEN_K_VICTORY_B_POWERS = [
    Triumph_10K_Alpha, Triumph_10K_Beta, Triumph_10K_Gamma, Triumph_10K_Delta, Triumph_10K_Epsilon, Triumph_10K_Zeta, Triumph_10K_Eta,
    Triumph_10K_Theta, Triumph_10K_Iota, Triumph_10K_Kappa, Triumph_10K_Lambda, Triumph_10K_Mu, Triumph_10K_Nu, Triumph_10K_Xi,
]

for power_class in TEN_K_VICTORY_B_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
