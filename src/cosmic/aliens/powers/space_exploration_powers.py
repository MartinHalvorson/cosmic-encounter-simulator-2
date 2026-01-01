"""
Space Exploration Powers for Cosmic Encounter.

Aliens inspired by space exploration and astronaut themes.
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
class Astronaut(AlienPower):
    """Astronaut - Power of Exploration. +2 when attacking new planets."""
    name: str = field(default="Astronaut", init=False)
    description: str = field(default="+2 for new colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cosmonaut(AlienPower):
    """Cosmonaut - Power of Pioneering. +3 on offense."""
    name: str = field(default="Cosmonaut", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Rocket_Ship(AlienPower):
    """Rocket_Ship - Power of Launch. May commit up to 6 ships."""
    name: str = field(default="Rocket_Ship", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Space_Station(AlienPower):
    """Space_Station - Power of Orbit. +3 on defense."""
    name: str = field(default="Space_Station", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Mission_Control(AlienPower):
    """Mission_Control - Power of Command. See opponent's card before choosing."""
    name: str = field(default="Mission_Control", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lunar_Base(AlienPower):
    """Lunar_Base - Power of Moon. +1 per home colony."""
    name: str = field(default="Lunar_Base", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mars_Colony(AlienPower):
    """Mars_Colony - Power of Settlement. +1 per foreign colony."""
    name: str = field(default="Mars_Colony", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + colonies
        return total


@dataclass
class Probe(AlienPower):
    """Probe - Power of Discovery. See top 3 deck cards."""
    name: str = field(default="Probe", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Satellite(AlienPower):
    """Satellite - Power of Surveillance. Know opponent's hand size."""
    name: str = field(default="Satellite", init=False)
    description: str = field(default="See opponent hand size.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Telescope(AlienPower):
    """Telescope - Power of Vision. Attack any planet."""
    name: str = field(default="Telescope", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deep_Space(AlienPower):
    """Deep_Space - Power of Distance. +2 always."""
    name: str = field(default="Deep_Space", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Warp_Drive(AlienPower):
    """Warp_Drive - Power of Speed. Take second encounter on win."""
    name: str = field(default="Warp_Drive", init=False)
    description: str = field(default="Second encounter on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cryo_Sleep(AlienPower):
    """Cryo_Sleep - Power of Stasis. Ships in warp return each turn."""
    name: str = field(default="Cryo_Sleep", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Zero_Gravity(AlienPower):
    """Zero_Gravity - Power of Weightlessness. Win ties automatically."""
    name: str = field(default="Zero_Gravity", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Escape_Pod(AlienPower):
    """Escape_Pod - Power of Survival. Lose max 2 ships per encounter."""
    name: str = field(default="Escape_Pod", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all space exploration powers
AlienRegistry.register(Astronaut())
AlienRegistry.register(Cosmonaut())
AlienRegistry.register(Rocket_Ship())
AlienRegistry.register(Space_Station())
AlienRegistry.register(Mission_Control())
AlienRegistry.register(Lunar_Base())
AlienRegistry.register(Mars_Colony())
AlienRegistry.register(Probe())
AlienRegistry.register(Satellite())
AlienRegistry.register(Telescope())
AlienRegistry.register(Deep_Space())
AlienRegistry.register(Warp_Drive())
AlienRegistry.register(Cryo_Sleep())
AlienRegistry.register(Zero_Gravity())
AlienRegistry.register(Escape_Pod())
