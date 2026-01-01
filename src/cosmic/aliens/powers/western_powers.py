"""
Western Powers for Cosmic Encounter.

Aliens inspired by Wild West themes.
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
class Gunslinger(AlienPower):
    """Gunslinger - Power of Quick Draw. +4 on first encounter."""
    name: str = field(default="Gunslinger", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Marshal(AlienPower):
    """Marshal - Power of Law. +3 on defense."""
    name: str = field(default="Marshal", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Outlaw(AlienPower):
    """Outlaw - Power of Crime. +3 on offense."""
    name: str = field(default="Outlaw", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Rancher(AlienPower):
    """Rancher - Power of Herding. +1 per colony you have."""
    name: str = field(default="Rancher", init=False)
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
class Prospector(AlienPower):
    """Prospector - Power of Mining. Draw 1 card when winning."""
    name: str = field(default="Prospector", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saloon_Keeper(AlienPower):
    """Saloon_Keeper - Power of Drinks. Opponent discards 1 card."""
    name: str = field(default="Saloon_Keeper", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bounty_Alt(AlienPower):
    """Bounty_Alt - Power of Hunting. +3 vs players with fewer colonies."""
    name: str = field(default="Bounty_Alt", init=False)
    description: str = field(default="+3 vs weaker players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stagecoach(AlienPower):
    """Stagecoach - Power of Transport. May commit up to 6 ships."""
    name: str = field(default="Stagecoach", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gold_Rush(AlienPower):
    """Gold_Rush - Power of Greed. Draw 2 cards on offense win."""
    name: str = field(default="Gold_Rush", init=False)
    description: str = field(default="Draw 2 cards on offense win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tumbleweed(AlienPower):
    """Tumbleweed - Power of Rolling. Ships return home, not warp."""
    name: str = field(default="Tumbleweed", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Lasso(AlienPower):
    """Lasso - Power of Capture. Take 1 ship from opponent's colony."""
    name: str = field(default="Lasso", init=False)
    description: str = field(default="Capture opponent ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frontier(AlienPower):
    """Frontier - Power of Expansion. +3 when establishing new colony."""
    name: str = field(default="Frontier", init=False)
    description: str = field(default="+3 for new colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Duel(AlienPower):
    """Duel - Power of Challenge. Win ties automatically."""
    name: str = field(default="Duel", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Posse(AlienPower):
    """Posse - Power of Group. Allies get +2 each."""
    name: str = field(default="Posse", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spurs(AlienPower):
    """Spurs - Power of Speed. +2 and take second encounter on win."""
    name: str = field(default="Spurs", init=False)
    description: str = field(default="+2 and second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


# Register all western powers
AlienRegistry.register(Gunslinger())
AlienRegistry.register(Marshal())
AlienRegistry.register(Outlaw())
AlienRegistry.register(Rancher())
AlienRegistry.register(Prospector())
AlienRegistry.register(Saloon_Keeper())
AlienRegistry.register(Bounty_Alt())
AlienRegistry.register(Stagecoach())
AlienRegistry.register(Gold_Rush())
AlienRegistry.register(Tumbleweed())
AlienRegistry.register(Lasso())
AlienRegistry.register(Frontier())
AlienRegistry.register(Duel())
AlienRegistry.register(Posse())
AlienRegistry.register(Spurs())
