"""
Construction-themed alien powers for Cosmic Encounter.

Powers inspired by building and construction concepts.
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
class Bricklayer(AlienPower):
    """Bricklayer - Power of Foundation. Steady defense."""
    name: str = field(default="Bricklayer", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Crane_Operator(AlienPower):
    """Crane_Operator - Power of Lifting. Move resources."""
    name: str = field(default="Crane_Operator", init=False)
    description: str = field(default="Move 1 ship from warp before encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Demolisher(AlienPower):
    """Demolisher - Power of Destruction. Break defenses."""
    name: str = field(default="Demolisher", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Excavator(AlienPower):
    """Excavator - Power of Digging. Uncover secrets."""
    name: str = field(default="Excavator", init=False)
    description: str = field(default="Draw 1 card at start of encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scaffolder(AlienPower):
    """Scaffolder - Power of Support. Help allies."""
    name: str = field(default="Scaffolder", init=False)
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
class Welder(AlienPower):
    """Welder - Power of Joining. Strengthen bonds."""
    name: str = field(default="Welder", init=False)
    description: str = field(default="Ships count as +2.", init=False)
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
        return base_total + ships  # Extra +1 per ship


@dataclass
class Electrician(AlienPower):
    """Electrician - Power of Current. Energy flow."""
    name: str = field(default="Electrician", init=False)
    description: str = field(default="+2 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, player.hand_size() * 2)
            return base_total + bonus
        return base_total


@dataclass
class Plumber(AlienPower):
    """Plumber - Power of Flow. Resource management."""
    name: str = field(default="Plumber", init=False)
    description: str = field(default="Return 1 ship from warp on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Roofer(AlienPower):
    """Roofer - Power of Cover. Protect from above."""
    name: str = field(default="Roofer", init=False)
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
class Surveyor(AlienPower):
    """Surveyor - Power of Planning. Know the terrain."""
    name: str = field(default="Surveyor", init=False)
    description: str = field(default="+1 per colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + colonies
        return base_total


@dataclass
class Foreman(AlienPower):
    """Foreman - Power of Leadership. Direct workers."""
    name: str = field(default="Foreman", init=False)
    description: str = field(default="+2 per ship you have.", init=False)
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
class Concrete(AlienPower):
    """Concrete - Power of Solidity. Tough defense."""
    name: str = field(default="Concrete", init=False)
    description: str = field(default="+6 defense, -2 offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE:
            return base_total + 6
        elif side == Side.OFFENSE:
            return base_total - 2
        return base_total


@dataclass
class Steel(AlienPower):
    """Steel - Power of Strength. Unbreakable."""
    name: str = field(default="Steel", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Blueprint(AlienPower):
    """Blueprint - Power of Design. Plan ahead."""
    name: str = field(default="Blueprint", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all construction powers
CONSTRUCTION_POWERS = [
    Bricklayer, Crane_Operator, Demolisher, Excavator, Scaffolder,
    Welder, Electrician, Plumber, Roofer, Surveyor,
    Foreman, Concrete, Steel, Blueprint,
]

for power_class in CONSTRUCTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
