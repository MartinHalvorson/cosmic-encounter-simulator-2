"""
Strategy-themed alien powers.

These aliens are inspired by chess, military tactics, and game theory.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Grandmaster(AlienPower):
    """Grandmaster - Power of Planning. Look at top 3 deck cards before encounter."""
    name: str = field(default="Grandmaster", init=False)
    description: str = field(default="View top 3 deck cards before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tactician(AlienPower):
    """Tactician - Power of Tactics. +3 when you have more ships in encounter."""
    name: str = field(default="Tactician", init=False)
    description: str = field(default="+3 when you have more ships than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        my_ships = game.offense_ships.get(player.name, 0) if side == Side.OFFENSE else game.defense_ships.get(player.name, 0)
        opp_ships = sum(game.defense_ships.values()) if side == Side.OFFENSE else sum(game.offense_ships.values())
        if my_ships > opp_ships:
            return total + 3
        return total


@dataclass
class Flanker(AlienPower):
    """Flanker - Power of Flanking. +2 for each ally on your side."""
    name: str = field(default="Flanker", init=False)
    description: str = field(default="+2 for each ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        allies = game.offense_allies if side == Side.OFFENSE else game.defense_allies
        return total + (len(allies) * 2)


@dataclass
class Pawn(AlienPower):
    """Pawn - Power of Promotion. +10 when at 4 foreign colonies."""
    name: str = field(default="Pawn", init=False)
    description: str = field(default="+10 when at 4 foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        colonies = player.count_foreign_colonies(game.planets)
        if colonies >= 4:
            return total + 10
        return total


@dataclass
class Rook(AlienPower):
    """Rook - Power of Straight Lines. +4 when attacking home planets."""
    name: str = field(default="Rook", init=False)
    description: str = field(default="+4 when attacking opponent's home planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active or side != Side.OFFENSE:
            return total
        return total + 4


@dataclass
class Bishop(AlienPower):
    """Bishop - Power of Diagonals. +3 when defending."""
    name: str = field(default="Bishop", init=False)
    description: str = field(default="+3 when on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active or side != Side.DEFENSE:
            return total
        return total + 3


@dataclass
class Queen_Strategy(AlienPower):
    """Queen_Strategy - Power of Versatility. +2 on offense AND defense."""
    name: str = field(default="Queen_Strategy", init=False)
    description: str = field(default="+2 on both offense and defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Blitz(AlienPower):
    """Blitz - Power of Speed Attack. +5 on first encounter of turn."""
    name: str = field(default="Blitz", init=False)
    description: str = field(default="+5 on first encounter of your turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if player == game.offense and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Gambit(AlienPower):
    """Gambit - Power of Sacrifice. Discard cards for +3 each."""
    name: str = field(default="Gambit", init=False)
    description: str = field(default="Discard cards for +3 each (max 3).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Siege(AlienPower):
    """Siege - Power of Attrition. +1 for each turn game has lasted."""
    name: str = field(default="Siege", init=False)
    description: str = field(default="+1 for each turn the game has lasted.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


@dataclass
class Ambush(AlienPower):
    """Ambush - Power of Surprise. +6 when opponent has more ships."""
    name: str = field(default="Ambush", init=False)
    description: str = field(default="+6 when opponent has more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        my_ships = game.offense_ships.get(player.name, 0) if side == Side.OFFENSE else game.defense_ships.get(player.name, 0)
        opp_ships = sum(game.defense_ships.values()) if side == Side.OFFENSE else sum(game.offense_ships.values())
        if opp_ships > my_ships:
            return total + 6
        return total


@dataclass
class Bluff(AlienPower):
    """Bluff - Power of Deception. Random +0 to +8 bonus."""
    name: str = field(default="Bluff", init=False)
    description: str = field(default="Random +0 to +8 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 8)
        return total


@dataclass
class Counterattack(AlienPower):
    """Counterattack - Power to Counter. +5 when on defense."""
    name: str = field(default="Counterattack", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Fortress(AlienPower):
    """Fortress - Power of Entrenchment. +2 per home planet you control."""
    name: str = field(default="Fortress", init=False)
    description: str = field(default="+2 per home planet you control.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        home_controlled = sum(1 for p in player.home_planets if p.has_colony(player.name))
        return total + (home_controlled * 2)


@dataclass
class Retreat(AlienPower):
    """Retreat - Power to Escape. Ships return to colonies instead of warp on loss."""
    name: str = field(default="Retreat", init=False)
    description: str = field(default="Lost ships return to colonies, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sacrifice(AlienPower):
    """Sacrifice - Power of Trading. +4 but lose 2 ships to warp."""
    name: str = field(default="Sacrifice", init=False)
    description: str = field(default="+4 but lose 2 ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Encircle(AlienPower):
    """Encircle - Power of Surrounding. +3 if you have colonies in defender's system."""
    name: str = field(default="Encircle", init=False)
    description: str = field(default="+3 if you have colonies in defender's system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Formation(AlienPower):
    """Formation - Power of Order. +1 per ship you have in encounter."""
    name: str = field(default="Formation", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ship_dict = game.offense_ships if side == Side.OFFENSE else game.defense_ships
        my_ships = ship_dict.get(player.name, 0)
        return total + my_ships


@dataclass
class Pincer(AlienPower):
    """Pincer - Power of Two Fronts. +4 when allies on both sides."""
    name: str = field(default="Pincer", init=False)
    description: str = field(default="+4 when there are allies on both sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if game.offense_allies and game.defense_allies:
            return total + 4
        return total


@dataclass
class Feint(AlienPower):
    """Feint - Power of Misdirection. May change card after opponent reveals."""
    name: str = field(default="Feint", init=False)
    description: str = field(default="May change card after seeing opponent's.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all strategy powers
AlienRegistry.register(Grandmaster())
AlienRegistry.register(Tactician())
AlienRegistry.register(Flanker())
AlienRegistry.register(Pawn())
AlienRegistry.register(Rook())
AlienRegistry.register(Bishop())
AlienRegistry.register(Queen_Strategy())
AlienRegistry.register(Blitz())
AlienRegistry.register(Gambit())
AlienRegistry.register(Siege())
AlienRegistry.register(Ambush())
AlienRegistry.register(Bluff())
AlienRegistry.register(Counterattack())
AlienRegistry.register(Fortress())
AlienRegistry.register(Retreat())
AlienRegistry.register(Sacrifice())
AlienRegistry.register(Encircle())
AlienRegistry.register(Formation())
AlienRegistry.register(Pincer())
AlienRegistry.register(Feint())
