"""
Arena and competition themed alien powers for Cosmic Encounter.

Powers inspired by competitive arenas and gladiatorial combat.
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
class Gladiator(AlienPower):
    """Gladiator - Power of Combat. Arena fighter."""
    name: str = field(default="Gladiator", init=False)
    description: str = field(default="+4 in one-on-one combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        # One-on-one: no allies on either side
        if side == Side.OFFENSE:
            my_allies = len([p for p in game.offense_ships if p != player.name])
            opp_allies = len([p for p in game.defense_ships if p != (game.defense.name if game.defense else "")])
        else:
            my_allies = len([p for p in game.defense_ships if p != player.name])
            opp_allies = len([p for p in game.offense_ships if p != (game.offense.name if game.offense else "")])
        if my_allies == 0 and opp_allies == 0:
            return base_total + 4
        return base_total


@dataclass
class Champion_Arena(AlienPower):
    """Champion_Arena - Power of Victory. Winner's bonus."""
    name: str = field(default="Champion_Arena", init=False)
    description: str = field(default="+3 at 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return base_total + 3
        return base_total


@dataclass
class Colosseum(AlienPower):
    """Colosseum - Power of Spectacle. Home advantage."""
    name: str = field(default="Colosseum", init=False)
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
class Contender(AlienPower):
    """Contender - Power of Challenge. Underdog strength."""
    name: str = field(default="Contender", init=False)
    description: str = field(default="+4 when behind in colonies.", init=False)
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
                return base_total + 4
        return base_total


@dataclass
class Fighter(AlienPower):
    """Fighter - Power of Brawl. Raw combat."""
    name: str = field(default="Fighter", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Duelist(AlienPower):
    """Duelist - Power of Honor. One-on-one specialist."""
    name: str = field(default="Duelist", init=False)
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
class Pit(AlienPower):
    """Pit - Power of the Depths. Trap enemies."""
    name: str = field(default="Pit", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Victor(AlienPower):
    """Victor - Power of Triumph. Snowball wins."""
    name: str = field(default="Victor", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brawler(AlienPower):
    """Brawler - Power of Chaos. Strength in disorder."""
    name: str = field(default="Brawler", init=False)
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
class Challenger(AlienPower):
    """Challenger - Power of Assault. Aggressive attacks."""
    name: str = field(default="Challenger", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Defender_Arena(AlienPower):
    """Defender_Arena - Power of Hold. Hold the line."""
    name: str = field(default="Defender_Arena", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Rival(AlienPower):
    """Rival - Power of Competition. Match opponents."""
    name: str = field(default="Rival", init=False)
    description: str = field(default="+1 per opponent ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            opp_ships = sum(game.defense_ships.values())
        else:
            opp_ships = sum(game.offense_ships.values())
        return base_total + opp_ships


@dataclass
class Underdog(AlienPower):
    """Underdog - Power of Surprise. Upset potential."""
    name: str = field(default="Underdog", init=False)
    description: str = field(default="+5 when outnumbered.", init=False)
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
            return base_total + 5
        return base_total


@dataclass
class Veteran(AlienPower):
    """Veteran - Power of Experience. Late game bonus."""
    name: str = field(default="Veteran", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn)
            return base_total + bonus
        return base_total


# Register all arena powers
ARENA_POWERS = [
    Gladiator, Champion_Arena, Colosseum, Contender, Fighter,
    Duelist, Pit, Victor, Brawler, Challenger,
    Defender_Arena, Rival, Underdog, Veteran,
]

for power_class in ARENA_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
