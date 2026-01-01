"""
Software development themed alien powers.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Debugger(AlienPower):
    """Debugger - Power of Fixing. Find and fix issues."""
    name: str = field(default="Debugger", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Compiler(AlienPower):
    """Compiler - Power of Translation. Convert code to action."""
    name: str = field(default="Compiler", init=False)
    description: str = field(default="+4 with 4+ cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 4:
            return total + 4
        return total


@dataclass
class Algorithm(AlienPower):
    """Algorithm - Power of Logic. Systematic approach."""
    name: str = field(default="Algorithm", init=False)
    description: str = field(default="+2 per colony (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + min(8, colonies * 2)
        return total


@dataclass
class Recursion(AlienPower):
    """Recursion - Power of Self-Reference. Calls itself."""
    name: str = field(default="Recursion", init=False)
    description: str = field(default="+1 that doubles each turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    bonus: int = 1

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            result = total + self.bonus
            self.bonus = min(8, self.bonus * 2)
            return result
        return total


@dataclass
class API(AlienPower):
    """API - Power of Interface. Connect systems."""
    name: str = field(default="API", init=False)
    description: str = field(default="+2 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        return total + ally_count * 2


@dataclass
class Database(AlienPower):
    """Database - Power of Storage. Massive data capacity."""
    name: str = field(default="Database", init=False)
    description: str = field(default="+5 with 6+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 6:
            return total + 5
        return total


@dataclass
class Encryption(AlienPower):
    """Encryption - Power of Secrecy. Hidden data."""
    name: str = field(default="Encryption", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Firewall(AlienPower):
    """Firewall - Power of Protection. Block threats."""
    name: str = field(default="Firewall", init=False)
    description: str = field(default="+5 when defending at home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.hyperspace_gate and game.hyperspace_gate.owner == player.name:
                return total + 5
        return total


@dataclass
class Open_Source(AlienPower):
    """Open_Source - Power of Sharing. Community driven."""
    name: str = field(default="Open_Source", init=False)
    description: str = field(default="+3 with 2+ allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count >= 2:
            return total + 3
        return total


@dataclass
class Refactor(AlienPower):
    """Refactor - Power of Improvement. Make code better."""
    name: str = field(default="Refactor", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Commit(AlienPower):
    """Commit - Power of Saving. Save your work."""
    name: str = field(default="Commit_Software", init=False)
    description: str = field(default="+2 plus +1 per win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    wins: int = 0

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + self.wins
        return total


@dataclass
class Microservice(AlienPower):
    """Microservice - Power of Modularity. Small focused units."""
    name: str = field(default="Microservice", init=False)
    description: str = field(default="+2 per ship (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return total + min(6, ships * 2)


@dataclass
class Container(AlienPower):
    """Container - Power of Isolation. Isolated environments."""
    name: str = field(default="Container_Software", init=False)
    description: str = field(default="+4 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 4
        return total


@dataclass
class Cloud(AlienPower):
    """Cloud - Power of Scalability. Scale infinitely."""
    name: str = field(default="Cloud_Software", init=False)
    description: str = field(default="+1 per card in hand (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(7, len(player.hand))
        return total


@dataclass
class Serverless(AlienPower):
    """Serverless - Power of Abstraction. No infrastructure needed."""
    name: str = field(default="Serverless", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


SOFTWARE_POWERS = [
    Debugger, Compiler, Algorithm, Recursion, API, Database, Encryption,
    Firewall, Open_Source, Refactor, Commit, Microservice, Container,
    Cloud, Serverless
]

for power_class in SOFTWARE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
