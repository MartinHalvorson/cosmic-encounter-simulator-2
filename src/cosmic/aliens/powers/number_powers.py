"""Number themed alien powers."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class One(AlienPower):
    name: str = field(default="One", init=False)
    description: str = field(default="+1 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 1
        return base_total


@dataclass
class Two(AlienPower):
    name: str = field(default="Two", init=False)
    description: str = field(default="+2 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Three(AlienPower):
    name: str = field(default="Three", init=False)
    description: str = field(default="+3 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Four(AlienPower):
    name: str = field(default="Four", init=False)
    description: str = field(default="+4 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Five(AlienPower):
    name: str = field(default="Five", init=False)
    description: str = field(default="+5 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Six(AlienPower):
    name: str = field(default="Six", init=False)
    description: str = field(default="+6 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 6
        return base_total


@dataclass
class Seven(AlienPower):
    name: str = field(default="Seven", init=False)
    description: str = field(default="+7 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 7
        return base_total


@dataclass
class Eight(AlienPower):
    name: str = field(default="Eight", init=False)
    description: str = field(default="+8 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 8
        return base_total


@dataclass
class Nine(AlienPower):
    name: str = field(default="Nine", init=False)
    description: str = field(default="+9 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 9
        return base_total


@dataclass
class Ten(AlienPower):
    name: str = field(default="Ten", init=False)
    description: str = field(default="+10 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 10
        return base_total


@dataclass
class Zero(AlienPower):
    name: str = field(default="Zero", init=False)
    description: str = field(default="+0 but opponent -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dozen(AlienPower):
    name: str = field(default="Dozen", init=False)
    description: str = field(default="+12 but requires 4+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if side == Side.OFFENSE:
                ships = len(game.offense_ships) if hasattr(game, 'offense_ships') else 0
            else:
                ships = len(game.defense_ships) if hasattr(game, 'defense_ships') else 0
            if ships >= 4:
                return base_total + 12
        return base_total


@dataclass
class Hundred(AlienPower):
    name: str = field(default="Hundred", init=False)
    description: str = field(default="+10 but only in late game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn >= 10:
            return base_total + 10
        return base_total


@dataclass
class Prime(AlienPower):
    name: str = field(default="Prime", init=False)
    description: str = field(default="+5 on prime turns (2,3,5,7,11,13).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
            if game.current_turn in primes:
                return base_total + 5
        return base_total


@dataclass
class Fibonacci(AlienPower):
    name: str = field(default="Fibonacci", init=False)
    description: str = field(default="+fib(turn mod 8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            fib = [0, 1, 1, 2, 3, 5, 8, 13]
            idx = game.current_turn % 8
            return base_total + fib[idx]
        return base_total


NUMBER_POWERS = [
    One, Two, Three, Four, Five,
    Six, Seven, Eight, Nine, Ten,
    Zero, Dozen, Hundred, Prime, Fibonacci,
]

for power_class in NUMBER_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
