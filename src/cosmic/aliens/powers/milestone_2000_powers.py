"""
Milestone 2000 alien powers - celebrating 2000 aliens!
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
class Millennium(AlienPower):
    """Millennium - Power of Thousands. +2 for every 1000 aliens in game."""
    name: str = field(default="Millennium", init=False)
    description: str = field(default="+2 bonus (celebrating 2000 aliens!).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class TwoThousand(AlienPower):
    """TwoThousand - Power of Celebration. +4 on your turn."""
    name: str = field(default="TwoThousand", init=False)
    description: str = field(default="+4 on offense (2000 aliens milestone!).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Infinite(AlienPower):
    """Infinite - Power of Endless. Ships return from warp each turn."""
    name: str = field(default="Infinite", init=False)
    description: str = field(default="Return 1 ship from warp at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boundless(AlienPower):
    """Boundless - Power of Limits. May commit up to 8 ships."""
    name: str = field(default="Boundless", init=False)
    description: str = field(default="May commit up to 8 ships to encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Vast(AlienPower):
    """Vast - Power of Scope. +1 per planet you occupy."""
    name: str = field(default="Vast", init=False)
    description: str = field(default="+1 for each planet you occupy.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            planets_occupied = sum(1 for p in game.planets if p.has_colony(player.name))
            return total + planets_occupied
        return total


@dataclass
class Cosmic_Milestone(AlienPower):
    """Cosmic_Milestone - Power of Achievement. Draw card when winning."""
    name: str = field(default="Cosmic_Milestone", init=False)
    description: str = field(default="Draw 1 card when winning an encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eternal_Cosmic(AlienPower):
    """Eternal_Cosmic - Power of Permanence. +3 on defense."""
    name: str = field(default="Eternal_Cosmic", init=False)
    description: str = field(default="+3 when on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Legendary_Milestone(AlienPower):
    """Legendary_Milestone - Power of Legends. +3 on offense."""
    name: str = field(default="Legendary_Milestone", init=False)
    description: str = field(default="+3 when on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Monumental(AlienPower):
    """Monumental - Power of Scale. Ships count as 2 each."""
    name: str = field(default="Monumental", init=False)
    description: str = field(default="Your ships each count as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Triumphant(AlienPower):
    """Triumphant - Power of Victory. +5 when at 4 foreign colonies."""
    name: str = field(default="Triumphant", init=False)
    description: str = field(default="+5 when at 4 foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return total + 5
        return total


@dataclass
class Epic_Milestone(AlienPower):
    """Epic_Milestone - Power of Saga. +2 per turn game has lasted."""
    name: str = field(default="Epic_Milestone", init=False)
    description: str = field(default="+2 per turn game has lasted.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (game.current_turn * 2)
        return total


# Register all milestone powers
AlienRegistry.register(Millennium())
AlienRegistry.register(TwoThousand())
AlienRegistry.register(Infinite())
AlienRegistry.register(Boundless())
AlienRegistry.register(Vast())
AlienRegistry.register(Cosmic_Milestone())
AlienRegistry.register(Eternal_Cosmic())
AlienRegistry.register(Legendary_Milestone())
AlienRegistry.register(Monumental())
AlienRegistry.register(Triumphant())
AlienRegistry.register(Epic_Milestone())
