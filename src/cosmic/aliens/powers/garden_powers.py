"""
Garden and flora themed alien powers for Cosmic Encounter.

Powers inspired by plants, gardens, and horticulture.
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
class Gardener(AlienPower):
    """Gardener - Power of Cultivation. Grow resources."""
    name: str = field(default="Gardener", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Orchid(AlienPower):
    """Orchid - Power of Beauty. Elegant presence."""
    name: str = field(default="Orchid", init=False)
    description: str = field(default="+3 with 1-2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships in (1, 2):
            return base_total + 3
        return base_total


@dataclass
class Sunflower(AlienPower):
    """Sunflower - Power of Light. Bright presence."""
    name: str = field(default="Sunflower", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Cactus(AlienPower):
    """Cactus - Power of Thorns. Painful defense."""
    name: str = field(default="Cactus", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Vine_Garden(AlienPower):
    """Vine_Garden - Power of Spreading. Grow outward."""
    name: str = field(default="Vine_Garden", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Rose(AlienPower):
    """Rose - Power of Thorn. Beauty with defense."""
    name: str = field(default="Rose", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Bamboo(AlienPower):
    """Bamboo - Power of Growth. Rapid expansion."""
    name: str = field(default="Bamboo", init=False)
    description: str = field(default="Return 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lotus(AlienPower):
    """Lotus - Power of Purity. Clean strength."""
    name: str = field(default="Lotus", init=False)
    description: str = field(default="+4 with no ships in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and player.ships_in_warp == 0:
            return base_total + 4
        return base_total


@dataclass
class Moss(AlienPower):
    """Moss - Power of Covering. Spread slowly."""
    name: str = field(default="Moss", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + ships


@dataclass
class Fern(AlienPower):
    """Fern - Power of Shade. Survive in shadow."""
    name: str = field(default="Fern", init=False)
    description: str = field(default="+3 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            opp_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
        if opp_ships > my_ships:
            return base_total + 3
        return base_total


@dataclass
class Tulip(AlienPower):
    """Tulip - Power of Spring. Seasonal strength."""
    name: str = field(default="Tulip", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 4
        return base_total


@dataclass
class Dandelion(AlienPower):
    """Dandelion - Power of Scattering. Spread seeds."""
    name: str = field(default="Dandelion", init=False)
    description: str = field(default="Lose only 1 ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bonsai(AlienPower):
    """Bonsai - Power of Patience. Slow perfection."""
    name: str = field(default="Bonsai", init=False)
    description: str = field(default="+2 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn * 2)
            return base_total + bonus
        return base_total


@dataclass
class Hedge(AlienPower):
    """Hedge - Power of Barrier. Living wall."""
    name: str = field(default="Hedge", init=False)
    description: str = field(default="+4 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 4
        return base_total


# Register all garden powers
GARDEN_POWERS = [
    Gardener, Orchid, Sunflower, Cactus, Vine_Garden,
    Rose, Bamboo, Lotus, Moss, Fern,
    Tulip, Dandelion, Bonsai, Hedge,
]

for power_class in GARDEN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
