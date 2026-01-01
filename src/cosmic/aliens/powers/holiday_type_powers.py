"""
Holiday Type Powers for Cosmic Encounter.
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
class Christmas_Holiday(AlienPower):
    """Christmas_Holiday - Power of Gift. +5 always"""
    name: str = field(default="Christmas_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Halloween_Holiday(AlienPower):
    """Halloween_Holiday - Power of Spooky. +5 always"""
    name: str = field(default="Halloween_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Easter_Holiday(AlienPower):
    """Easter_Holiday - Power of Egg. +5 always"""
    name: str = field(default="Easter_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Thanksgiving_Holiday(AlienPower):
    """Thanksgiving_Holiday - Power of Feast. +5 always"""
    name: str = field(default="Thanksgiving_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class New_Year_Holiday(AlienPower):
    """New_Year_Holiday - Power of Celebrate. +5 always"""
    name: str = field(default="New_Year_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Valentine_Holiday(AlienPower):
    """Valentine_Holiday - Power of Love. +5 always"""
    name: str = field(default="Valentine_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Independence_Day_Holiday(AlienPower):
    """Independence_Day_Holiday - Power of Freedom. +5 always"""
    name: str = field(default="Independence_Day_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Diwali_Holiday(AlienPower):
    """Diwali_Holiday - Power of Light. +5 always"""
    name: str = field(default="Diwali_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Hanukkah_Holiday(AlienPower):
    """Hanukkah_Holiday - Power of Candle. +5 always"""
    name: str = field(default="Hanukkah_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Lunar_New_Year_Holiday(AlienPower):
    """Lunar_New_Year_Holiday - Power of Dragon. +5 always"""
    name: str = field(default="Lunar_New_Year_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Mardi_Gras_Holiday(AlienPower):
    """Mardi_Gras_Holiday - Power of Party. +5 always"""
    name: str = field(default="Mardi_Gras_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class St_Patrick_Holiday(AlienPower):
    """St_Patrick_Holiday - Power of Green. +4 always"""
    name: str = field(default="St_Patrick_Holiday", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Cinco_De_Mayo_Holiday(AlienPower):
    """Cinco_De_Mayo_Holiday - Power of Fiesta. +5 always"""
    name: str = field(default="Cinco_De_Mayo_Holiday", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Carnival_Holiday(AlienPower):
    """Carnival_Holiday - Power of Dance. +6 always"""
    name: str = field(default="Carnival_Holiday", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


HOLIDAY_TYPE_POWERS = [
    Christmas_Holiday, Halloween_Holiday, Easter_Holiday, Thanksgiving_Holiday, New_Year_Holiday, Valentine_Holiday, Independence_Day_Holiday,
    Diwali_Holiday, Hanukkah_Holiday, Lunar_New_Year_Holiday, Mardi_Gras_Holiday, St_Patrick_Holiday, Cinco_De_Mayo_Holiday, Carnival_Holiday,
]

for power_class in HOLIDAY_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
