"""
Gemstone Powers for Cosmic Encounter.

Aliens inspired by precious gems and crystals.
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
class Diamond_Alt(AlienPower):
    """Diamond_Alt - Power of Hardness. +4 on defense."""
    name: str = field(default="Diamond_Alt", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Ruby_Alt(AlienPower):
    """Ruby_Alt - Power of Fire. +3 on offense."""
    name: str = field(default="Ruby_Alt", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Sapphire_Alt(AlienPower):
    """Sapphire_Alt - Power of Wisdom. See opponent's card before choosing."""
    name: str = field(default="Sapphire_Alt", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Emerald_Alt(AlienPower):
    """Emerald_Alt - Power of Growth. +1 per colony you have."""
    name: str = field(default="Emerald_Alt", init=False)
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
class Amethyst_Alt(AlienPower):
    """Amethyst_Alt - Power of Calm. Win ties automatically."""
    name: str = field(default="Amethyst_Alt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Topaz(AlienPower):
    """Topaz - Power of Energy. +2 to all totals."""
    name: str = field(default="Topaz", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Opal(AlienPower):
    """Opal - Power of Color. Copy opponent's power for encounter."""
    name: str = field(default="Opal", init=False)
    description: str = field(default="Copy opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Pearl_Alt(AlienPower):
    """Pearl_Alt - Power of Purity. Cannot be targeted by opponent powers."""
    name: str = field(default="Pearl_Alt", init=False)
    description: str = field(default="Immune to opponent powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Onyx(AlienPower):
    """Onyx - Power of Darkness. -2 to opponent's total."""
    name: str = field(default="Onyx", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Garnet(AlienPower):
    """Garnet - Power of Protection. Lose max 2 ships per encounter."""
    name: str = field(default="Garnet", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Turquoise(AlienPower):
    """Turquoise - Power of Healing. Return 1 ship from warp each turn."""
    name: str = field(default="Turquoise", init=False)
    description: str = field(default="Return 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jade(AlienPower):
    """Jade - Power of Fortune. Draw 1 card when winning."""
    name: str = field(default="Jade", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quartz(AlienPower):
    """Quartz - Power of Clarity. See top 3 deck cards."""
    name: str = field(default="Quartz", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Obsidian(AlienPower):
    """Obsidian - Power of Sharpness. +4 on first encounter of turn."""
    name: str = field(default="Obsidian", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Moonstone(AlienPower):
    """Moonstone - Power of Night. +3 every other turn."""
    name: str = field(default="Moonstone", init=False)
    description: str = field(default="+3 every other turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 3
        return total


# Register all gemstone powers
AlienRegistry.register(Diamond_Alt())
AlienRegistry.register(Ruby_Alt())
AlienRegistry.register(Sapphire_Alt())
AlienRegistry.register(Emerald_Alt())
AlienRegistry.register(Amethyst_Alt())
AlienRegistry.register(Topaz())
AlienRegistry.register(Opal())
AlienRegistry.register(Pearl_Alt())
AlienRegistry.register(Onyx())
AlienRegistry.register(Garnet())
AlienRegistry.register(Turquoise())
AlienRegistry.register(Jade())
AlienRegistry.register(Quartz())
AlienRegistry.register(Obsidian())
AlienRegistry.register(Moonstone())
