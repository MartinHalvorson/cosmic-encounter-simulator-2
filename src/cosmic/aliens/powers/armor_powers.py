"""
Armor Powers for Cosmic Encounter.

Aliens themed around armor and protective gear.
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
class Plate_Armor(AlienPower):
    """Plate_Armor - Power of Protection. +4 on defense."""
    name: str = field(default="Plate_Armor", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Chain_Mail(AlienPower):
    """Chain_Mail - Power of Links. +3 always."""
    name: str = field(default="Chain_Mail", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Leather_Armor(AlienPower):
    """Leather_Armor - Power of Flexibility. +2 always."""
    name: str = field(default="Leather_Armor", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Scale_Mail(AlienPower):
    """Scale_Mail - Power of Scales. +3 on defense."""
    name: str = field(default="Scale_Mail", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Helmet(AlienPower):
    """Helmet - Power of Headgear. +2 on defense."""
    name: str = field(default="Helmet", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Shield_Armor(AlienPower):
    """Shield_Armor - Power of Blocking. +3 on defense."""
    name: str = field(default="Shield_Armor", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Gauntlet(AlienPower):
    """Gauntlet - Power of Fists. +2 on offense."""
    name: str = field(default="Gauntlet", init=False)
    description: str = field(default="+2 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 2
        return total


@dataclass
class Breastplate(AlienPower):
    """Breastplate - Power of Chest. +4 always."""
    name: str = field(default="Breastplate", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Greaves(AlienPower):
    """Greaves - Power of Legs. +2 always."""
    name: str = field(default="Greaves", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Pauldron(AlienPower):
    """Pauldron - Power of Shoulders. +2 always."""
    name: str = field(default="Pauldron", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Vambrace(AlienPower):
    """Vambrace - Power of Arms. +2 always."""
    name: str = field(default="Vambrace", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Cuirass(AlienPower):
    """Cuirass - Power of Torso. +3 always."""
    name: str = field(default="Cuirass", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Buckler(AlienPower):
    """Buckler - Power of Small Shield. +2 on defense."""
    name: str = field(default="Buckler", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Hauberk(AlienPower):
    """Hauberk - Power of Mail. +3 always."""
    name: str = field(default="Hauberk", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Gorget(AlienPower):
    """Gorget - Power of Throat. Ships survive on loss."""
    name: str = field(default="Gorget", init=False)
    description: str = field(default="Lose 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


ARMOR_POWERS = [
    Plate_Armor, Chain_Mail, Leather_Armor, Scale_Mail, Helmet,
    Shield_Armor, Gauntlet, Breastplate, Greaves, Pauldron,
    Vambrace, Cuirass, Buckler, Hauberk, Gorget,
]

for power_class in ARMOR_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
