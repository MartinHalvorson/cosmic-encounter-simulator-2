"""
Forest Powers for Cosmic Encounter.

Aliens inspired by forests, trees, and woodland themes.
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
class Oak(AlienPower):
    """Oak - Power of Strength. +3 on defense."""
    name: str = field(default="Oak", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Willow(AlienPower):
    """Willow - Power of Flexibility. May change card after reveal."""
    name: str = field(default="Willow", init=False)
    description: str = field(default="Change card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pine(AlienPower):
    """Pine - Power of Persistence. +1 for each encounter this turn."""
    name: str = field(default="Pine", init=False)
    description: str = field(default="+1 per encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.encounter_number
        return total


@dataclass
class Birch(AlienPower):
    """Birch - Power of Renewal. Draw 1 card at turn start."""
    name: str = field(default="Birch", init=False)
    description: str = field(default="Draw 1 card at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Maple(AlienPower):
    """Maple - Power of Seasons. +4 every other turn."""
    name: str = field(default="Maple", init=False)
    description: str = field(default="+4 every other turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 4
        return total


@dataclass
class Redwood(AlienPower):
    """Redwood - Power of Height. +2 for each home colony."""
    name: str = field(default="Redwood", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ash_Tree(AlienPower):
    """Ash_Tree - Power of Rebirth. Ships return from warp faster."""
    name: str = field(default="Ash_Tree", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cedar(AlienPower):
    """Cedar - Power of Preservation. Cards not discarded when used."""
    name: str = field(default="Cedar", init=False)
    description: str = field(default="Keep cards after use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sequoia(AlienPower):
    """Sequoia - Power of Ancients. +5 in late game (turn 10+)."""
    name: str = field(default="Sequoia", init=False)
    description: str = field(default="+5 after turn 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn >= 10:
            return total + 5
        return total


@dataclass
class Elm(AlienPower):
    """Elm - Power of Shelter. Defend allies - they lose fewer ships."""
    name: str = field(default="Elm", init=False)
    description: str = field(default="Protect ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Banyan(AlienPower):
    """Banyan - Power of Roots. +1 for each colony you have."""
    name: str = field(default="Banyan", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return total + colonies
        return total


@dataclass
class Baobab(AlienPower):
    """Baobab - Power of Storage. Hold up to 10 cards."""
    name: str = field(default="Baobab", init=False)
    description: str = field(default="10 card hand limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mangrove(AlienPower):
    """Mangrove - Power of Networks. Allies gain +1 each."""
    name: str = field(default="Mangrove", init=False)
    description: str = field(default="Allies get +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cypress(AlienPower):
    """Cypress - Power of Swamps. +3 when at 2 or fewer colonies."""
    name: str = field(default="Cypress", init=False)
    description: str = field(default="+3 when struggling.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies <= 2:
                return total + 3
        return total


@dataclass
class Yew(AlienPower):
    """Yew - Power of Longevity. Cannot lose more than 2 ships per encounter."""
    name: str = field(default="Yew", init=False)
    description: str = field(default="Lose max 2 ships per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all forest powers
AlienRegistry.register(Oak())
AlienRegistry.register(Willow())
AlienRegistry.register(Pine())
AlienRegistry.register(Birch())
AlienRegistry.register(Maple())
AlienRegistry.register(Redwood())
AlienRegistry.register(Ash_Tree())
AlienRegistry.register(Cedar())
AlienRegistry.register(Sequoia())
AlienRegistry.register(Elm())
AlienRegistry.register(Banyan())
AlienRegistry.register(Baobab())
AlienRegistry.register(Mangrove())
AlienRegistry.register(Cypress())
AlienRegistry.register(Yew())
