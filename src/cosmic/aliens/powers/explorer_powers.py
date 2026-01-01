"""
Explorer-themed alien powers for Cosmic Encounter.

Powers inspired by exploration and discovery.
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
class Pioneer(AlienPower):
    """Pioneer - Power of First. Bonus on new territory."""
    name: str = field(default="Pioneer", init=False)
    description: str = field(default="+4 attacking planets you have no colony on.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if game.defense_planet and not game.defense_planet.has_colony(player.name):
                return base_total + 4
        return base_total


@dataclass
class Navigator(AlienPower):
    """Navigator - Power of Direction. Find the way."""
    name: str = field(default="Navigator", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Cartographer(AlienPower):
    """Cartographer - Power of Maps. Know the terrain."""
    name: str = field(default="Cartographer", init=False)
    description: str = field(default="+1 per planet you have ships on.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            occupied = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + occupied
        return base_total


@dataclass
class Pathfinder(AlienPower):
    """Pathfinder - Power of Trail. Find new routes."""
    name: str = field(default="Pathfinder", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Trailblazer(AlienPower):
    """Trailblazer - Power of Opening. Create new paths."""
    name: str = field(default="Trailblazer", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 5
        return base_total


@dataclass
class Surveyor_Explorer(AlienPower):
    """Surveyor_Explorer - Power of Study. Analyze terrain."""
    name: str = field(default="Surveyor_Explorer", init=False)
    description: str = field(default="+3 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 3
        return base_total


@dataclass
class Adventurer(AlienPower):
    """Adventurer - Power of Risk. Bold moves."""
    name: str = field(default="Adventurer", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
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
            return base_total + 4
        return base_total


@dataclass
class Nomad_Explorer(AlienPower):
    """Nomad_Explorer - Power of Wandering. Never stay still."""
    name: str = field(default="Nomad_Explorer", init=False)
    description: str = field(default="+2 offense, +2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Expedition(AlienPower):
    """Expedition - Power of Team. Group exploration."""
    name: str = field(default="Expedition", init=False)
    description: str = field(default="+2 per ally.", init=False)
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
        return base_total + (allies * 2)


@dataclass
class Archaeologist(AlienPower):
    """Archaeologist - Power of Digging. Uncover secrets."""
    name: str = field(default="Archaeologist", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mountaineer(AlienPower):
    """Mountaineer - Power of Climbing. Overcome obstacles."""
    name: str = field(default="Mountaineer", init=False)
    description: str = field(default="+3 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            if my_colonies < opp_colonies:
                return base_total + 3
        return base_total


@dataclass
class Diver(AlienPower):
    """Diver - Power of Depths. Explore deep."""
    name: str = field(default="Diver", init=False)
    description: str = field(default="+4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Astronaut(AlienPower):
    """Astronaut - Power of Space. Cosmic exploration."""
    name: str = field(default="Astronaut", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Prospector(AlienPower):
    """Prospector - Power of Resources. Find treasure."""
    name: str = field(default="Prospector", init=False)
    description: str = field(default="+1 per card in hand (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(5, player.hand_size())
            return base_total + bonus
        return base_total


# Register all explorer powers
EXPLORER_POWERS = [
    Pioneer, Navigator, Cartographer, Pathfinder, Trailblazer,
    Surveyor_Explorer, Adventurer, Nomad_Explorer, Expedition, Archaeologist,
    Mountaineer, Diver, Astronaut, Prospector,
]

for power_class in EXPLORER_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
