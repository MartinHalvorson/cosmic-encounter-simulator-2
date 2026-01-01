"""
Metal Powers - Metal and mineral-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Iron(AlienPower):
    """Iron - Hard metal. +3 when defending."""
    name: str = field(default="Iron", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Steel(AlienPower):
    """Steel - Strong alloy. +4 when defending home."""
    name: str = field(default="Steel", init=False)
    description: str = field(default="+4 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 4
        return total


@dataclass
class Gold(AlienPower):
    """Gold - Precious metal. +1 per card in hand."""
    name: str = field(default="Gold", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Silver(AlienPower):
    """Silver - Swift metal. +3 on first encounter."""
    name: str = field(default="Silver", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Copper(AlienPower):
    """Copper - Conductive metal. Allies gain +1 each."""
    name: str = field(default="Copper", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bronze(AlienPower):
    """Bronze - Ancient alloy. +2 always."""
    name: str = field(default="Bronze", init=False)
    description: str = field(default="+2 to all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Platinum(AlienPower):
    """Platinum - Rare metal. Win ties."""
    name: str = field(default="Platinum", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Titanium(AlienPower):
    """Titanium - Strongest metal. +5 when attacking."""
    name: str = field(default="Titanium", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Lead(AlienPower):
    """Lead - Heavy metal. Ships count double."""
    name: str = field(default="Lead", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nickel(AlienPower):
    """Nickel - Magnetic metal. Swap encounter cards."""
    name: str = field(default="Nickel", init=False)
    description: str = field(default="Swap cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Zinc(AlienPower):
    """Zinc - Protective metal. Prevent 2 ships from warp."""
    name: str = field(default="Zinc", init=False)
    description: str = field(default="Save 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Aluminum(AlienPower):
    """Aluminum - Light metal. Move ships freely."""
    name: str = field(default="Aluminum", init=False)
    description: str = field(default="Freely relocate ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tin(AlienPower):
    """Tin - Malleable metal. Draw card each turn."""
    name: str = field(default="Tin", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mercury(AlienPower):
    """Mercury - Liquid metal. Ships escape to colonies."""
    name: str = field(default="Mercury", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chromium(AlienPower):
    """Chromium - Shiny metal. See opponent's encounter card."""
    name: str = field(default="Chromium", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Iron())
AlienRegistry.register(Steel())
AlienRegistry.register(Gold())
AlienRegistry.register(Silver())
AlienRegistry.register(Copper())
AlienRegistry.register(Bronze())
AlienRegistry.register(Platinum())
AlienRegistry.register(Titanium())
AlienRegistry.register(Lead())
AlienRegistry.register(Nickel())
AlienRegistry.register(Zinc())
AlienRegistry.register(Aluminum())
AlienRegistry.register(Tin())
AlienRegistry.register(Mercury())
AlienRegistry.register(Chromium())
