"""
Amphibian Type Powers for Cosmic Encounter.
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
class Frog_Amphibian(AlienPower):
    """Frog_Amphibian - Power of Leap. +5 always"""
    name: str = field(default="Frog_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Toad_Amphibian(AlienPower):
    """Toad_Amphibian - Power of Wart. +5 always"""
    name: str = field(default="Toad_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Salamander_Amphibian(AlienPower):
    """Salamander_Amphibian - Power of Fire. +5 always"""
    name: str = field(default="Salamander_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Newt_Amphibian(AlienPower):
    """Newt_Amphibian - Power of Regenerate. +5 on defense"""
    name: str = field(default="Newt_Amphibian", init=False)
    description: str = field(default="+5 on defense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Axolotl_Amphibian(AlienPower):
    """Axolotl_Amphibian - Power of Forever. +5 always"""
    name: str = field(default="Axolotl_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Caecilian_Amphibian(AlienPower):
    """Caecilian_Amphibian - Power of Burrow. +5 always"""
    name: str = field(default="Caecilian_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Treefrog_Amphibian(AlienPower):
    """Treefrog_Amphibian - Power of Climb. +5 always"""
    name: str = field(default="Treefrog_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Poison_Dart_Amphibian(AlienPower):
    """Poison_Dart_Amphibian - Power of Toxic. +5 on offense"""
    name: str = field(default="Poison_Dart_Amphibian", init=False)
    description: str = field(default="+5 on offense", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Bullfrog_Amphibian(AlienPower):
    """Bullfrog_Amphibian - Power of Deep. +5 always"""
    name: str = field(default="Bullfrog_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Spring_Peeper_Amphibian(AlienPower):
    """Spring_Peeper_Amphibian - Power of Song. +5 always"""
    name: str = field(default="Spring_Peeper_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Glass_Frog_Amphibian(AlienPower):
    """Glass_Frog_Amphibian - Power of Clear. +5 always"""
    name: str = field(default="Glass_Frog_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Mudpuppy_Amphibian(AlienPower):
    """Mudpuppy_Amphibian - Power of Gills. +4 always"""
    name: str = field(default="Mudpuppy_Amphibian", init=False)
    description: str = field(default="+4 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Hellbender_Amphibian(AlienPower):
    """Hellbender_Amphibian - Power of Large. +5 always"""
    name: str = field(default="Hellbender_Amphibian", init=False)
    description: str = field(default="+5 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Golden_Frog_Amphibian(AlienPower):
    """Golden_Frog_Amphibian - Power of Rare. +6 always"""
    name: str = field(default="Golden_Frog_Amphibian", init=False)
    description: str = field(default="+6 always", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


AMPHIBIAN_TYPE_POWERS = [
    Frog_Amphibian, Toad_Amphibian, Salamander_Amphibian, Newt_Amphibian, Axolotl_Amphibian, Caecilian_Amphibian, Treefrog_Amphibian,
    Poison_Dart_Amphibian, Bullfrog_Amphibian, Spring_Peeper_Amphibian, Glass_Frog_Amphibian, Mudpuppy_Amphibian, Hellbender_Amphibian, Golden_Frog_Amphibian,
]

for power_class in AMPHIBIAN_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
