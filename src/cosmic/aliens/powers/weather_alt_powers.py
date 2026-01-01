"""
Weather Alt Powers - Additional weather and climate-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Drought(AlienPower):
    """Drought - Water scarcity. Opponent draws fewer cards."""
    name: str = field(default="Drought", init=False)
    description: str = field(default="Reduce opponent's card draws.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deluge(AlienPower):
    """Deluge - Overwhelming flood. +5 on first encounter."""
    name: str = field(default="Deluge", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Sunshine(AlienPower):
    """Sunshine - Warming rays. +1 per ally."""
    name: str = field(default="Sunshine", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tempest_Alt(AlienPower):
    """Tempest Alt - Violent storm. +4 when attacking."""
    name: str = field(default="Tempest_Alt2", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Breeze_Alt(AlienPower):
    """Breeze Alt - Gentle wind. Move ships freely."""
    name: str = field(default="Breeze_Alt", init=False)
    description: str = field(default="Freely relocate ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sleet(AlienPower):
    """Sleet - Mixed precipitation. -2 to both sides."""
    name: str = field(default="Sleet", init=False)
    description: str = field(default="-2 to both totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dew(AlienPower):
    """Dew - Morning moisture. Draw card each turn."""
    name: str = field(default="Dew", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rainbow_Alt(AlienPower):
    """Rainbow Alt - Promise. Win encounter to draw 2 cards."""
    name: str = field(default="Rainbow_Alt", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Snowfall(AlienPower):
    """Snowfall - Blanketing snow. +3 when defending."""
    name: str = field(default="Snowfall", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Mist_Alt(AlienPower):
    """Mist Alt - Obscuring vapor. Hide encounter card."""
    name: str = field(default="Mist_Alt2", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thunder_Alt(AlienPower):
    """Thunder Alt - Booming sound. -3 to opponent."""
    name: str = field(default="Thunder_Alt", init=False)
    description: str = field(default="-3 to opponent's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Squall(AlienPower):
    """Squall - Sudden storm. Swap encounter cards."""
    name: str = field(default="Squall", init=False)
    description: str = field(default="Swap cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gust(AlienPower):
    """Gust - Strong wind. Move opponent ship to warp."""
    name: str = field(default="Gust", init=False)
    description: str = field(default="Send 1 enemy ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Climate(AlienPower):
    """Climate - Weather control. Choose encounter condition."""
    name: str = field(default="Climate", init=False)
    description: str = field(default="Set encounter conditions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Season(AlienPower):
    """Season - Changing times. +2 per turn in game."""
    name: str = field(default="Season", init=False)
    description: str = field(default="+2 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Drought())
AlienRegistry.register(Deluge())
AlienRegistry.register(Sunshine())
AlienRegistry.register(Tempest_Alt())
AlienRegistry.register(Breeze_Alt())
AlienRegistry.register(Sleet())
AlienRegistry.register(Dew())
AlienRegistry.register(Rainbow_Alt())
AlienRegistry.register(Snowfall())
AlienRegistry.register(Mist_Alt())
AlienRegistry.register(Thunder_Alt())
AlienRegistry.register(Squall())
AlienRegistry.register(Gust())
AlienRegistry.register(Climate())
AlienRegistry.register(Season())
