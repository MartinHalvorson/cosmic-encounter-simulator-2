"""
9500 Last A Powers for Cosmic Encounter.
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
class Push_Final_One_95(AlienPower):
    """Push_Final_One_95 - Power of One. +5 always"""
    name: str = field(default="Push_Final_One_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Two_95(AlienPower):
    """Push_Final_Two_95 - Power of Two. +5 always"""
    name: str = field(default="Push_Final_Two_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Three_95(AlienPower):
    """Push_Final_Three_95 - Power of Three. +5 always"""
    name: str = field(default="Push_Final_Three_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Four_95(AlienPower):
    """Push_Final_Four_95 - Power of Four. +5 always"""
    name: str = field(default="Push_Final_Four_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Five_95(AlienPower):
    """Push_Final_Five_95 - Power of Five. +5 always"""
    name: str = field(default="Push_Final_Five_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Six_95(AlienPower):
    """Push_Final_Six_95 - Power of Six. +5 always"""
    name: str = field(default="Push_Final_Six_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Seven_95(AlienPower):
    """Push_Final_Seven_95 - Power of Seven. +5 always"""
    name: str = field(default="Push_Final_Seven_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Eight_95(AlienPower):
    """Push_Final_Eight_95 - Power of Eight. +5 always"""
    name: str = field(default="Push_Final_Eight_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Nine_95(AlienPower):
    """Push_Final_Nine_95 - Power of Nine. +5 always"""
    name: str = field(default="Push_Final_Nine_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Ten_95(AlienPower):
    """Push_Final_Ten_95 - Power of Ten. +5 always"""
    name: str = field(default="Push_Final_Ten_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Eleven_95(AlienPower):
    """Push_Final_Eleven_95 - Power of Eleven. +5 always"""
    name: str = field(default="Push_Final_Eleven_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Twelve_95(AlienPower):
    """Push_Final_Twelve_95 - Power of Twelve. +4 always"""
    name: str = field(default="Push_Final_Twelve_95", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Push_Final_Thirteen_95(AlienPower):
    """Push_Final_Thirteen_95 - Power of Thirteen. +5 always"""
    name: str = field(default="Push_Final_Thirteen_95", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Push_Final_Fourteen_95(AlienPower):
    """Push_Final_Fourteen_95 - Power of Fourteen. +6 always"""
    name: str = field(default="Push_Final_Fourteen_95", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


NINE_FIVE_LAST_PUSH_A_POWERS = [
    Push_Final_One_95, Push_Final_Two_95, Push_Final_Three_95, Push_Final_Four_95, Push_Final_Five_95, Push_Final_Six_95, Push_Final_Seven_95,
    Push_Final_Eight_95, Push_Final_Nine_95, Push_Final_Ten_95, Push_Final_Eleven_95, Push_Final_Twelve_95, Push_Final_Thirteen_95, Push_Final_Fourteen_95,
]

for power_class in NINE_FIVE_LAST_PUSH_A_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
