"""
Musical Instrument Powers for Cosmic Encounter.

Aliens inspired by musical instruments.
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
class Guitar_Alt(AlienPower):
    """Guitar_Alt - Power of Strings. +3 always."""
    name: str = field(default="Guitar_Alt", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Drums_Alt(AlienPower):
    """Drums_Alt - Power of Rhythm. +4 on offense."""
    name: str = field(default="Drums_Alt", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Piano_Alt(AlienPower):
    """Piano_Alt - Power of Keys. +1 per card in hand."""
    name: str = field(default="Piano_Alt", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Violin_Alt(AlienPower):
    """Violin_Alt - Power of Harmony. Allies get +2 each."""
    name: str = field(default="Violin_Alt", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trumpet_Alt(AlienPower):
    """Trumpet_Alt - Power of Fanfare. +4 on first encounter."""
    name: str = field(default="Trumpet_Alt", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Flute_Alt(AlienPower):
    """Flute_Alt - Power of Wind. Draw 1 card at turn start."""
    name: str = field(default="Flute_Alt", init=False)
    description: str = field(default="Draw 1 card at start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saxophone(AlienPower):
    """Saxophone - Power of Jazz. See opponent's card before choosing."""
    name: str = field(default="Saxophone", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cello(AlienPower):
    """Cello - Power of Depth. +3 on defense."""
    name: str = field(default="Cello", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Harp_Alt(AlienPower):
    """Harp_Alt - Power of Grace. Win ties automatically."""
    name: str = field(default="Harp_Alt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Organ(AlienPower):
    """Organ - Power of Church. Ships return from warp each turn."""
    name: str = field(default="Organ", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bagpipe(AlienPower):
    """Bagpipe - Power of War. +2 and block opponent allies."""
    name: str = field(default="Bagpipe", init=False)
    description: str = field(default="+2, block allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Banjo(AlienPower):
    """Banjo - Power of Country. +2 per home colony."""
    name: str = field(default="Banjo", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Accordion(AlienPower):
    """Accordion - Power of Flexibility. May change card after reveal."""
    name: str = field(default="Accordion", init=False)
    description: str = field(default="Change card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tuba(AlienPower):
    """Tuba - Power of Bass. Ships count as 1.5 each."""
    name: str = field(default="Tuba", init=False)
    description: str = field(default="Ships count as 1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Xylophone(AlienPower):
    """Xylophone - Power of Notes. +1 per colony you have."""
    name: str = field(default="Xylophone", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return total + colonies
        return total


# Register all musical instrument powers
AlienRegistry.register(Guitar_Alt())
AlienRegistry.register(Drums_Alt())
AlienRegistry.register(Piano_Alt())
AlienRegistry.register(Violin_Alt())
AlienRegistry.register(Trumpet_Alt())
AlienRegistry.register(Flute_Alt())
AlienRegistry.register(Saxophone())
AlienRegistry.register(Cello())
AlienRegistry.register(Harp_Alt())
AlienRegistry.register(Organ())
AlienRegistry.register(Bagpipe())
AlienRegistry.register(Banjo())
AlienRegistry.register(Accordion())
AlienRegistry.register(Tuba())
AlienRegistry.register(Xylophone())
