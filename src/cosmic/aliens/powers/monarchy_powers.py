"""
Monarchy-themed alien powers for Cosmic Encounter.

Powers inspired by royal courts and monarchies.
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
class Monarch(AlienPower):
    """Monarch - Power of Rule. Supreme authority."""
    name: str = field(default="Monarch", init=False)
    description: str = field(default="+4 offense, +4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Courtier(AlienPower):
    """Courtier - Power of Favor. Royal connections."""
    name: str = field(default="Courtier", init=False)
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
class Throne(AlienPower):
    """Throne - Power of Authority. Command from above."""
    name: str = field(default="Throne", init=False)
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
class Crown(AlienPower):
    """Crown - Power of Sovereignty. Royal might."""
    name: str = field(default="Crown", init=False)
    description: str = field(default="+5 at 4+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return base_total + 5
        return base_total


@dataclass
class Scepter(AlienPower):
    """Scepter - Power of Command. Direct authority."""
    name: str = field(default="Scepter", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Regent(AlienPower):
    """Regent - Power of Stewardship. Temporary rule."""
    name: str = field(default="Regent", init=False)
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
class Heir(AlienPower):
    """Heir - Power of Succession. Rising power."""
    name: str = field(default="Heir", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Noble(AlienPower):
    """Noble - Power of Status. High station."""
    name: str = field(default="Noble", init=False)
    description: str = field(default="+3 with no ships in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and player.ships_in_warp == 0:
            return base_total + 3
        return base_total


@dataclass
class Vassal(AlienPower):
    """Vassal - Power of Loyalty. Sworn service."""
    name: str = field(default="Vassal", init=False)
    description: str = field(default="+2 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ally_ships = sum(v for k, v in game.offense_ships.items() if k != player.name)
        else:
            ally_ships = sum(v for k, v in game.defense_ships.items() if k != player.name)
        return base_total + (ally_ships * 2)


@dataclass
class Chamberlain(AlienPower):
    """Chamberlain - Power of Protocol. Manage affairs."""
    name: str = field(default="Chamberlain", init=False)
    description: str = field(default="Allies commit +1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chancellor(AlienPower):
    """Chancellor - Power of Counsel. Wise advice."""
    name: str = field(default="Chancellor", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Steward(AlienPower):
    """Steward - Power of Management. Resource care."""
    name: str = field(default="Steward", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dynasty(AlienPower):
    """Dynasty - Power of Legacy. Enduring rule."""
    name: str = field(default="Dynasty", init=False)
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
class Realm(AlienPower):
    """Realm - Power of Domain. Control territory."""
    name: str = field(default="Realm", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


# Register all monarchy powers
MONARCHY_POWERS = [
    Monarch, Courtier, Throne, Crown, Scepter,
    Regent, Heir, Noble, Vassal, Chamberlain,
    Chancellor, Steward, Dynasty, Realm,
]

for power_class in MONARCHY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
