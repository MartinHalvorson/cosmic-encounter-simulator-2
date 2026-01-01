"""
Architecture Style Powers for Cosmic Encounter.

Aliens inspired by architectural styles and buildings.
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
class Gothic(AlienPower):
    """Gothic - Power of Spires. +4 on defense."""
    name: str = field(default="Gothic", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Baroque(AlienPower):
    """Baroque - Power of Ornament. +1 per ally in encounter."""
    name: str = field(default="Baroque", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Minimalist(AlienPower):
    """Minimalist - Power of Simplicity. +3 when attacking alone."""
    name: str = field(default="Minimalist", init=False)
    description: str = field(default="+3 without allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Art_Deco(AlienPower):
    """Art_Deco - Power of Style. +2 always."""
    name: str = field(default="Art_Deco", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Brutalist(AlienPower):
    """Brutalist - Power of Concrete. Ships count as 2 each."""
    name: str = field(default="Brutalist", init=False)
    description: str = field(default="Ships count as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Renaissance(AlienPower):
    """Renaissance - Power of Rebirth. Return 2 ships from warp each turn."""
    name: str = field(default="Renaissance", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Modernist(AlienPower):
    """Modernist - Power of Function. Win ties automatically."""
    name: str = field(default="Modernist", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Classical(AlienPower):
    """Classical - Power of Columns. +3 always."""
    name: str = field(default="Classical", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Victorian(AlienPower):
    """Victorian - Power of Elegance. Draw 1 card when winning."""
    name: str = field(default="Victorian", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Industrial(AlienPower):
    """Industrial - Power of Factory. +1 per ship in encounter."""
    name: str = field(default="Industrial", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Colonial_Style(AlienPower):
    """Colonial_Style - Power of Settlement. +1 per colony you have."""
    name: str = field(default="Colonial_Style", init=False)
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
class Futurist(AlienPower):
    """Futurist - Power of Tomorrow. +4 on offense."""
    name: str = field(default="Futurist", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Neoclassical(AlienPower):
    """Neoclassical - Power of Revival. Retrieve card from discard."""
    name: str = field(default="Neoclassical", init=False)
    description: str = field(default="Retrieve discarded card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deconstructivist(AlienPower):
    """Deconstructivist - Power of Chaos. Swap cards after reveal."""
    name: str = field(default="Deconstructivist", init=False)
    description: str = field(default="Swap cards after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Organic_Arch(AlienPower):
    """Organic_Arch - Power of Nature. Lose max 2 ships per encounter."""
    name: str = field(default="Organic_Arch", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all architecture style powers
AlienRegistry.register(Gothic())
AlienRegistry.register(Baroque())
AlienRegistry.register(Minimalist())
AlienRegistry.register(Art_Deco())
AlienRegistry.register(Brutalist())
AlienRegistry.register(Renaissance())
AlienRegistry.register(Modernist())
AlienRegistry.register(Classical())
AlienRegistry.register(Victorian())
AlienRegistry.register(Industrial())
AlienRegistry.register(Colonial_Style())
AlienRegistry.register(Futurist())
AlienRegistry.register(Neoclassical())
AlienRegistry.register(Deconstructivist())
AlienRegistry.register(Organic_Arch())
