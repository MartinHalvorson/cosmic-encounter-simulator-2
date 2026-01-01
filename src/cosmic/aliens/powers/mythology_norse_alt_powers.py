"""
Norse Mythology Alt Powers for Cosmic Encounter.

More aliens inspired by Norse gods and mythology.
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
class Odin_Alt(AlienPower):
    """Odin_Alt - Power of Wisdom. See opponent's hand."""
    name: str = field(default="Odin_Alt", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thor_Alt(AlienPower):
    """Thor_Alt - Power of Thunder. +4 on offense."""
    name: str = field(default="Thor_Alt", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Loki_Alt(AlienPower):
    """Loki_Alt - Power of Trickery. Swap cards after reveal."""
    name: str = field(default="Loki_Alt", init=False)
    description: str = field(default="Swap cards after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Freya_Alt(AlienPower):
    """Freya_Alt - Power of Love. Allies get +2 each."""
    name: str = field(default="Freya_Alt", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Heimdall_Alt(AlienPower):
    """Heimdall_Alt - Power of Vigilance. +3 on defense."""
    name: str = field(default="Heimdall_Alt", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Tyr_Alt(AlienPower):
    """Tyr_Alt - Power of War. +3 always."""
    name: str = field(default="Tyr_Alt", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Baldur_Alt(AlienPower):
    """Baldur_Alt - Power of Light. Immune to negative modifiers."""
    name: str = field(default="Baldur_Alt", init=False)
    description: str = field(default="Immune to penalties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Frigg(AlienPower):
    """Frigg - Power of Foresight. See top 3 deck cards."""
    name: str = field(default="Frigg", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skadi(AlienPower):
    """Skadi - Power of Winter. -2 to opponent's total."""
    name: str = field(default="Skadi", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bragi(AlienPower):
    """Bragi - Power of Poetry. Draw 1 card when winning."""
    name: str = field(default="Bragi", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hel(AlienPower):
    """Hel - Power of Death. Ships in warp count in combat."""
    name: str = field(default="Hel", init=False)
    description: str = field(default="Warp ships count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fenrir(AlienPower):
    """Fenrir - Power of Destruction. +5 but lose 2 ships after."""
    name: str = field(default="Fenrir", init=False)
    description: str = field(default="+5, lose 2 ships after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Jormungandr(AlienPower):
    """Jormungandr - Power of Serpent. Win ties automatically."""
    name: str = field(default="Jormungandr", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Valkyrie_Alt(AlienPower):
    """Valkyrie_Alt - Power of Choosers. Ships return from warp each turn."""
    name: str = field(default="Valkyrie_Alt", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Norns(AlienPower):
    """Norns - Power of Fate. Manipulate destiny deck."""
    name: str = field(default="Norns", init=False)
    description: str = field(default="Choose destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all Norse mythology alt powers
AlienRegistry.register(Odin_Alt())
AlienRegistry.register(Thor_Alt())
AlienRegistry.register(Loki_Alt())
AlienRegistry.register(Freya_Alt())
AlienRegistry.register(Heimdall_Alt())
AlienRegistry.register(Tyr_Alt())
AlienRegistry.register(Baldur_Alt())
AlienRegistry.register(Frigg())
AlienRegistry.register(Skadi())
AlienRegistry.register(Bragi())
AlienRegistry.register(Hel())
AlienRegistry.register(Fenrir())
AlienRegistry.register(Jormungandr())
AlienRegistry.register(Valkyrie_Alt())
AlienRegistry.register(Norns())
