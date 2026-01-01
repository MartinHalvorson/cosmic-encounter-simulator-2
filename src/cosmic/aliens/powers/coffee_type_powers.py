"""
Coffee Type Powers for Cosmic Encounter.
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
class Espresso(AlienPower):
    """Espresso - Power of Strong. +5 on offense."""
    name: str = field(default="Espresso", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Cappuccino(AlienPower):
    """Cappuccino - Power of Foam. +4 always."""
    name: str = field(default="Cappuccino", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Latte(AlienPower):
    """Latte - Power of Milk. +4 always."""
    name: str = field(default="Latte", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Americano(AlienPower):
    """Americano - Power of Diluted. +3 always."""
    name: str = field(default="Americano", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Mocha(AlienPower):
    """Mocha - Power of Chocolate. +4 always."""
    name: str = field(default="Mocha", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Macchiato(AlienPower):
    """Macchiato - Power of Stained. +4 always."""
    name: str = field(default="Macchiato", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Ristretto(AlienPower):
    """Ristretto - Power of Short. +5 on offense."""
    name: str = field(default="Ristretto", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Lungo(AlienPower):
    """Lungo - Power of Long. +4 always."""
    name: str = field(default="Lungo", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Affogato(AlienPower):
    """Affogato - Power of Drowned. +4 always."""
    name: str = field(default="Affogato", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Cold_Brew(AlienPower):
    """Cold_Brew - Power of Cold. +4 always."""
    name: str = field(default="Cold_Brew", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Irish_Coffee(AlienPower):
    """Irish_Coffee - Power of Whiskey. +5 always."""
    name: str = field(default="Irish_Coffee", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Turkish_Coffee(AlienPower):
    """Turkish_Coffee - Power of Strong. +5 always."""
    name: str = field(default="Turkish_Coffee", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Frappe(AlienPower):
    """Frappe - Power of Frozen. +3 always."""
    name: str = field(default="Frappe", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Cortado(AlienPower):
    """Cortado - Power of Cut. +4 always."""
    name: str = field(default="Cortado", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


COFFEE_TYPE_POWERS = [
    Espresso, Cappuccino, Latte, Americano, Mocha,
    Macchiato, Ristretto, Lungo, Affogato, Cold_Brew,
    Irish_Coffee, Turkish_Coffee, Frappe, Cortado,
]

for power_class in COFFEE_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
