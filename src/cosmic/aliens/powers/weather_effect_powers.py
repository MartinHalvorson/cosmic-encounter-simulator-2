"""
Weather Effect themed alien powers for Cosmic Encounter.
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
class Drizzle(AlienPower):
    """Drizzle - Power of Persistence."""
    name: str = field(default="Drizzle", init=False)
    description: str = field(default="+1 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 1
        return base_total


@dataclass
class Downpour(AlienPower):
    """Downpour - Power of Deluge."""
    name: str = field(default="Downpour", init=False)
    description: str = field(default="+5 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sleet(AlienPower):
    """Sleet - Power of Mixed."""
    name: str = field(default="Sleet", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Gale_Weather(AlienPower):
    """Gale - Power of Force."""
    name: str = field(default="Gale_Weather", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Squall(AlienPower):
    """Squall - Power of Suddenness."""
    name: str = field(default="Squall", init=False)
    description: str = field(default="+6 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tempest_Weather(AlienPower):
    """Tempest - Power of Storm."""
    name: str = field(default="Tempest_Weather", init=False)
    description: str = field(default="+5 with 4+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mist_Weather(AlienPower):
    """Mist - Power of Concealment."""
    name: str = field(default="Mist_Weather", init=False)
    description: str = field(default="Ships unseen until reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Overcast(AlienPower):
    """Overcast - Power of Gloom."""
    name: str = field(default="Overcast", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Whiteout(AlienPower):
    """Whiteout - Power of Blindness."""
    name: str = field(default="Whiteout", init=False)
    description: str = field(default="Opponent plays blind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sunshine_Weather(AlienPower):
    """Sunshine - Power of Clarity."""
    name: str = field(default="Sunshine_Weather", init=False)
    description: str = field(default="+3 with high card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Humidity(AlienPower):
    """Humidity - Power of Oppression."""
    name: str = field(default="Humidity", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rainbow_Weather(AlienPower):
    """Rainbow - Power of Hope."""
    name: str = field(default="Rainbow_Weather", init=False)
    description: str = field(default="+4 after loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Drizzle, Downpour, Sleet, Gale_Weather, Squall, Tempest_Weather,
    Mist_Weather, Overcast, Whiteout, Sunshine_Weather, Humidity, Rainbow_Weather,
]:
    AlienRegistry.register(alien_class())
