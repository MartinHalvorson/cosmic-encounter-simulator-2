"""
Fairy Tale Powers for Cosmic Encounter.

Aliens inspired by fairy tale characters and themes.
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
class Big_Bad_Wolf(AlienPower):
    """Big_Bad_Wolf - Power of Huffing. +4 on offense."""
    name: str = field(default="Big_Bad_Wolf", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Red_Riding_Hood(AlienPower):
    """Red_Riding_Hood - Power of Journey. +3 when far from home."""
    name: str = field(default="Red_Riding_Hood", init=False)
    description: str = field(default="+3 attacking foreign systems.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Three_Pigs(AlienPower):
    """Three_Pigs - Power of Building. +4 on defense."""
    name: str = field(default="Three_Pigs", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Goldilocks(AlienPower):
    """Goldilocks - Power of Just Right. Win ties automatically."""
    name: str = field(default="Goldilocks", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rapunzel(AlienPower):
    """Rapunzel - Power of Hair. Ships return from warp each turn."""
    name: str = field(default="Rapunzel", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cinderella(AlienPower):
    """Cinderella - Power of Transformation. +3 every other turn."""
    name: str = field(default="Cinderella", init=False)
    description: str = field(default="+3 every other turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 3
        return total


@dataclass
class Snow_White(AlienPower):
    """Snow_White - Power of Allies. Allies get +2 each."""
    name: str = field(default="Snow_White", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Evil_Queen(AlienPower):
    """Evil_Queen - Power of Jealousy. -2 to opponent's total."""
    name: str = field(default="Evil_Queen", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Magic_Mirror(AlienPower):
    """Magic_Mirror - Power of Truth. See opponent's card before choosing."""
    name: str = field(default="Magic_Mirror", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sleeping_Beauty(AlienPower):
    """Sleeping_Beauty - Power of Sleep. Ships in warp count in combat."""
    name: str = field(default="Sleeping_Beauty", init=False)
    description: str = field(default="Warp ships count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pied_Piper(AlienPower):
    """Pied_Piper - Power of Music. Steal 1 opponent ship."""
    name: str = field(default="Pied_Piper", init=False)
    description: str = field(default="Steal opponent ship on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jack_Giant(AlienPower):
    """Jack_Giant - Power of Climbing. Draw 1 card when winning."""
    name: str = field(default="Jack_Giant", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hansel_Gretel(AlienPower):
    """Hansel_Gretel - Power of Trail. Ships return home, not warp."""
    name: str = field(default="Hansel_Gretel", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Rumpelstiltskin(AlienPower):
    """Rumpelstiltskin - Power of Names. Take 1 card from defeated opponent."""
    name: str = field(default="Rumpelstiltskin", init=False)
    description: str = field(default="Take card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Genie_Lamp(AlienPower):
    """Genie_Lamp - Power of Wishes. +3 in all encounters."""
    name: str = field(default="Genie_Lamp", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


# Register all fairy tale powers
AlienRegistry.register(Big_Bad_Wolf())
AlienRegistry.register(Red_Riding_Hood())
AlienRegistry.register(Three_Pigs())
AlienRegistry.register(Goldilocks())
AlienRegistry.register(Rapunzel())
AlienRegistry.register(Cinderella())
AlienRegistry.register(Snow_White())
AlienRegistry.register(Evil_Queen())
AlienRegistry.register(Magic_Mirror())
AlienRegistry.register(Sleeping_Beauty())
AlienRegistry.register(Pied_Piper())
AlienRegistry.register(Jack_Giant())
AlienRegistry.register(Hansel_Gretel())
AlienRegistry.register(Rumpelstiltskin())
AlienRegistry.register(Genie_Lamp())
