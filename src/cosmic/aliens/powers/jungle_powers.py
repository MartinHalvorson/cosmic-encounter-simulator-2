"""
Jungle-themed alien powers for Cosmic Encounter.

Powers inspired by jungle environments and wildlife.
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
class Canopy(AlienPower):
    """Canopy - Power of Cover. Forest ceiling."""
    name: str = field(default="Canopy", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Panther(AlienPower):
    """Panther - Power of Stealth. Silent hunter."""
    name: str = field(default="Panther", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Gorilla(AlienPower):
    """Gorilla - Power of Strength. Jungle ape."""
    name: str = field(default="Gorilla", init=False)
    description: str = field(default="+4 offense, +4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Anaconda(AlienPower):
    """Anaconda - Power of Constriction. Giant serpent."""
    name: str = field(default="Anaconda", init=False)
    description: str = field(default="+5 with 1-2 ships.", init=False)
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
            return base_total + 5
        return base_total


@dataclass
class Piranha(AlienPower):
    """Piranha - Power of Swarm. Deadly fish."""
    name: str = field(default="Piranha", init=False)
    description: str = field(default="+2 per ship.", init=False)
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
        return base_total + (ships * 2)


@dataclass
class Toucan_Jungle(AlienPower):
    """Toucan_Jungle - Power of Color. Bright bird."""
    name: str = field(default="Toucan_Jungle", init=False)
    description: str = field(default="+3 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 3)


@dataclass
class Liana(AlienPower):
    """Liana - Power of Vine. Jungle rope."""
    name: str = field(default="Liana", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 5
        return base_total


@dataclass
class Tribe(AlienPower):
    """Tribe - Power of Community. Jungle people."""
    name: str = field(default="Tribe", init=False)
    description: str = field(default="+5 with 4 ships.", init=False)
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
        if ships >= 4:
            return base_total + 5
        return base_total


@dataclass
class Treehouse(AlienPower):
    """Treehouse - Power of Elevation. Jungle dwelling."""
    name: str = field(default="Treehouse", init=False)
    description: str = field(default="+5 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 5
        return base_total


@dataclass
class Monsoon(AlienPower):
    """Monsoon - Power of Rain. Seasonal storm."""
    name: str = field(default="Monsoon", init=False)
    description: str = field(default="+1 per turn (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(7, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Quicksand(AlienPower):
    """Quicksand - Power of Trap. Sinking sand."""
    name: str = field(default="Quicksand", init=False)
    description: str = field(default="+3 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (player.ships_in_warp * 3)
        return base_total


@dataclass
class Orchid_Jungle(AlienPower):
    """Orchid_Jungle - Power of Beauty. Rare flower."""
    name: str = field(default="Orchid_Jungle", init=False)
    description: str = field(default="+1 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, player.hand_size())
            return base_total + bonus
        return base_total


@dataclass
class Jaguar_Jungle(AlienPower):
    """Jaguar_Jungle - Power of Predator. Top hunter."""
    name: str = field(default="Jaguar_Jungle", init=False)
    description: str = field(default="+5 with no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        if allies == 0:
            return base_total + 5
        return base_total


@dataclass
class Undergrowth(AlienPower):
    """Undergrowth - Power of Hiding. Jungle floor."""
    name: str = field(default="Undergrowth", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + (colonies * 2)
        return base_total


# Register all jungle powers
JUNGLE_POWERS = [
    Canopy, Panther, Gorilla, Anaconda, Piranha,
    Toucan_Jungle, Liana, Tribe, Treehouse, Monsoon,
    Quicksand, Orchid_Jungle, Jaguar_Jungle, Undergrowth,
]

for power_class in JUNGLE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
