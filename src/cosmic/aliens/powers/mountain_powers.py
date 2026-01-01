"""
Mountain Powers for Cosmic Encounter.

Aliens inspired by mountains and highland themes.
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
class Summit(AlienPower):
    """Summit - Power of Height. +4 at 4 colonies."""
    name: str = field(default="Summit", init=False)
    description: str = field(default="+4 at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return total + 4
        return total


@dataclass
class Avalanche(AlienPower):
    """Avalanche - Power of Destruction. +5 but all lose 1 ship."""
    name: str = field(default="Avalanche", init=False)
    description: str = field(default="+5, all lose 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Cliff(AlienPower):
    """Cliff - Power of Edge. +4 on defense."""
    name: str = field(default="Cliff", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Peak(AlienPower):
    """Peak - Power of Vision. See top 3 deck cards."""
    name: str = field(default="Peak", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Valley(AlienPower):
    """Valley - Power of Shelter. Lose max 2 ships per encounter."""
    name: str = field(default="Valley", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glacier(AlienPower):
    """Glacier - Power of Cold. -2 to opponent's total."""
    name: str = field(default="Glacier", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Volcano_Alt(AlienPower):
    """Volcano_Alt - Power of Eruption. +4 on offense."""
    name: str = field(default="Volcano_Alt", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Cave_Alt(AlienPower):
    """Cave_Alt - Power of Hiding. Ships in warp count in combat."""
    name: str = field(default="Cave_Alt", init=False)
    description: str = field(default="Warp ships count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Boulder(AlienPower):
    """Boulder - Power of Mass. Ships count as 1.5 each."""
    name: str = field(default="Boulder", init=False)
    description: str = field(default="Ships count as 1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rockslide(AlienPower):
    """Rockslide - Power of Falling. Send 1 opponent ship to warp."""
    name: str = field(default="Rockslide", init=False)
    description: str = field(default="Send 1 ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Plateau(AlienPower):
    """Plateau - Power of Stability. +2 always."""
    name: str = field(default="Plateau", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Alpine(AlienPower):
    """Alpine - Power of Heights. +1 per colony you have."""
    name: str = field(default="Alpine", init=False)
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
class Ravine(AlienPower):
    """Ravine - Power of Depth. Win ties automatically."""
    name: str = field(default="Ravine", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Treeline(AlienPower):
    """Treeline - Power of Border. Draw 1 card at turn start."""
    name: str = field(default="Treeline", init=False)
    description: str = field(default="Draw 1 card at start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Snowcap(AlienPower):
    """Snowcap - Power of Ice. Opponent cannot invite allies."""
    name: str = field(default="Snowcap", init=False)
    description: str = field(default="Block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all mountain powers
AlienRegistry.register(Summit())
AlienRegistry.register(Avalanche())
AlienRegistry.register(Cliff())
AlienRegistry.register(Peak())
AlienRegistry.register(Valley())
AlienRegistry.register(Glacier())
AlienRegistry.register(Volcano_Alt())
AlienRegistry.register(Cave_Alt())
AlienRegistry.register(Boulder())
AlienRegistry.register(Rockslide())
AlienRegistry.register(Plateau())
AlienRegistry.register(Alpine())
AlienRegistry.register(Ravine())
AlienRegistry.register(Treeline())
AlienRegistry.register(Snowcap())
