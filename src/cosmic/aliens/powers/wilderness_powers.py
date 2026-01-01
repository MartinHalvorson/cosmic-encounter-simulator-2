"""
Wilderness Powers for Cosmic Encounter.

Aliens inspired by wild environments and outdoor concepts.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# TERRAIN
# ============================================================================

@dataclass
class Wilderness(AlienPower):
    """Wilderness - Power of the Wild. +3 defending home."""
    name: str = field(default="Wilderness", init=False)
    description: str = field(default="+3 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet in player.home_planets:
                return base_total + 3
        return base_total


@dataclass
class Frontier(AlienPower):
    """Frontier - Power of Exploration. +2 attacking new planets."""
    name: str = field(default="Frontier", init=False)
    description: str = field(default="+2 attacking new planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if game.defense_planet and not game.defense_planet.has_colony(player.name):
                return base_total + 2
        return base_total


@dataclass
class Outback(AlienPower):
    """Outback - Power of Survival. Ships return from warp faster."""
    name: str = field(default="Outback", init=False)
    description: str = field(default="Retrieve 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(min(2, player.ships_in_warp))


@dataclass
class Savanna(AlienPower):
    """Savanna - Power of the Plains. Ships move freely."""
    name: str = field(default="Savanna", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rainforest(AlienPower):
    """Rainforest - Power of Abundance. Draw extra card."""
    name: str = field(default="Rainforest", init=False)
    description: str = field(default="Draw 1 extra card per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


# ============================================================================
# WILDLIFE ENCOUNTERS
# ============================================================================

@dataclass
class Tracker(AlienPower):
    """Tracker - Power of Pursuit. Know opponent's card."""
    name: str = field(default="Tracker", init=False)
    description: str = field(default="See opponent's chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trapper(AlienPower):
    """Trapper - Power of Snares. Catch opponent ships."""
    name: str = field(default="Trapper", init=False)
    description: str = field(default="Opponent loses extra ship on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ranger(AlienPower):
    """Ranger - Power of Protection. +2 in all combats."""
    name: str = field(default="Ranger", init=False)
    description: str = field(default="+2 in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Pathfinder(AlienPower):
    """Pathfinder - Power of Discovery. Attack any planet."""
    name: str = field(default="Pathfinder", init=False)
    description: str = field(default="Choose attack target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Survivalist(AlienPower):
    """Survivalist - Power of Endurance. +1 per ship in warp."""
    name: str = field(default="Survivalist", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + player.ships_in_warp
        return base_total


# ============================================================================
# NATURAL PHENOMENA
# ============================================================================

@dataclass
class Geyser(AlienPower):
    """Geyser - Power of Eruption. Random +0 to +8."""
    name: str = field(default="Geyser", init=False)
    description: str = field(default="Random bonus 0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hotspring(AlienPower):
    """Hotspring - Power of Healing. Retrieve ships on win."""
    name: str = field(default="Hotspring", init=False)
    description: str = field(default="Retrieve 2 ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        if player.power_active and player.ships_in_warp >= 2:
            player.retrieve_ships_from_warp(2)


@dataclass
class Quicksand(AlienPower):
    """Quicksand - Power of Trapping. Slow opponent's ships."""
    name: str = field(default="Quicksand", init=False)
    description: str = field(default="Opponent can't use all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oasis(AlienPower):
    """Oasis - Power of Refuge. Safe haven for ships."""
    name: str = field(default="Oasis", init=False)
    description: str = field(default="Ships saved from warp go to colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rapids(AlienPower):
    """Rapids - Power of Speed. Extra encounter on win."""
    name: str = field(default="Rapids", init=False)
    description: str = field(default="Extra encounter after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CAMPING
# ============================================================================

@dataclass
class Campfire(AlienPower):
    """Campfire - Power of Gathering. Allies get +1."""
    name: str = field(default="Campfire", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tent(AlienPower):
    """Tent - Power of Shelter. Ships protected on defense."""
    name: str = field(default="Tent", init=False)
    description: str = field(default="Ships stay on loss when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Compass(AlienPower):
    """Compass - Power of Direction. See destiny before drawn."""
    name: str = field(default="Compass", init=False)
    description: str = field(default="Preview destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Backpack(AlienPower):
    """Backpack - Power of Storage. Hold extra cards."""
    name: str = field(default="Backpack", init=False)
    description: str = field(default="No hand limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lantern(AlienPower):
    """Lantern - Power of Light. See hidden cards."""
    name: str = field(default="Lantern", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
for alien_class in [
    Wilderness, Frontier, Outback, Savanna, Rainforest,
    Tracker, Trapper, Ranger, Pathfinder, Survivalist,
    Geyser, Hotspring, Quicksand, Oasis, Rapids,
    Campfire, Tent, Compass, Backpack, Lantern,
]:
    AlienRegistry.register(alien_class())
