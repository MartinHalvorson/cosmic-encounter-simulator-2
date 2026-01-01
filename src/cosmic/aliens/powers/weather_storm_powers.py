"""
Weather Storm Powers for Cosmic Encounter.

Aliens inspired by storms and severe weather phenomena.
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
class Hurricane_Alt(AlienPower):
    """Hurricane_Alt - Power of Devastation. +5 but lose 1 ship after."""
    name: str = field(default="Hurricane_Alt", init=False)
    description: str = field(default="+5, lose 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Tornado_Alt(AlienPower):
    """Tornado_Alt - Power of Spinning. Scatter opponent ships to random colonies."""
    name: str = field(default="Tornado_Alt", init=False)
    description: str = field(default="Scatter opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Typhoon(AlienPower):
    """Typhoon - Power of Waves. +3 on offense."""
    name: str = field(default="Typhoon", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Cyclone(AlienPower):
    """Cyclone - Power of Rotation. Switch offense and defense cards after reveal."""
    name: str = field(default="Cyclone", init=False)
    description: str = field(default="Switch revealed cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Monsoon(AlienPower):
    """Monsoon - Power of Seasons. +4 every other encounter."""
    name: str = field(default="Monsoon", init=False)
    description: str = field(default="+4 every other encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thunderstorm(AlienPower):
    """Thunderstorm - Power of Thunder. +2 and opponent cannot invite allies."""
    name: str = field(default="Thunderstorm", init=False)
    description: str = field(default="+2, block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hailstorm(AlienPower):
    """Hailstorm - Power of Pelting. All ships lose 1 after encounter."""
    name: str = field(default="Hailstorm", init=False)
    description: str = field(default="All sides lose 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blizzard_Alt(AlienPower):
    """Blizzard_Alt - Power of Cold. -3 to opponent's total."""
    name: str = field(default="Blizzard_Alt", init=False)
    description: str = field(default="-3 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Squall(AlienPower):
    """Squall - Power of Gusts. Force opponent to commit fewer ships."""
    name: str = field(default="Squall", init=False)
    description: str = field(default="Opponent commits max 3 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tempest(AlienPower):
    """Tempest - Power of Fury. +4 when behind in colonies."""
    name: str = field(default="Tempest", init=False)
    description: str = field(default="+4 when behind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gale(AlienPower):
    """Gale - Power of Wind. Ships return home instead of warp."""
    name: str = field(default="Gale", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Downpour(AlienPower):
    """Downpour - Power of Rain. Draw 2 cards when losing."""
    name: str = field(default="Downpour", init=False)
    description: str = field(default="Draw 2 cards when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cloudburst(AlienPower):
    """Cloudburst - Power of Sudden Rain. +3 on first encounter."""
    name: str = field(default="Cloudburst", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Drizzle(AlienPower):
    """Drizzle - Power of Light Rain. +1 per turn game has lasted."""
    name: str = field(default="Drizzle", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


@dataclass
class Whirlwind(AlienPower):
    """Whirlwind - Power of Spinning. Randomly redistribute ally ships."""
    name: str = field(default="Whirlwind", init=False)
    description: str = field(default="Redistribute ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all weather storm powers
AlienRegistry.register(Hurricane_Alt())
AlienRegistry.register(Tornado_Alt())
AlienRegistry.register(Typhoon())
AlienRegistry.register(Cyclone())
AlienRegistry.register(Monsoon())
AlienRegistry.register(Thunderstorm())
AlienRegistry.register(Hailstorm())
AlienRegistry.register(Blizzard_Alt())
AlienRegistry.register(Squall())
AlienRegistry.register(Tempest())
AlienRegistry.register(Gale())
AlienRegistry.register(Downpour())
AlienRegistry.register(Cloudburst())
AlienRegistry.register(Drizzle())
AlienRegistry.register(Whirlwind())
