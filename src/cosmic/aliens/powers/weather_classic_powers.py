"""
Weather Classic Powers - Classic weather phenomena aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Sunny(AlienPower):
    """Sunny - Bright and clear. +2 always."""
    name: str = field(default="Sunny", init=False)
    description: str = field(default="+2 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Cloudy(AlienPower):
    """Cloudy - Obscured. Opponent can't see card."""
    name: str = field(default="Cloudy", init=False)
    description: str = field(default="Hide your encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rainy(AlienPower):
    """Rainy - Constant rain. -2 to opponent."""
    name: str = field(default="Rainy", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Windy(AlienPower):
    """Windy - Strong winds. Ships scatter home."""
    name: str = field(default="Windy", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Snowy(AlienPower):
    """Snowy - Cold blanket. +3 on defense."""
    name: str = field(default="Snowy", init=False)
    description: str = field(default="+3 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Foggy(AlienPower):
    """Foggy - Low visibility. Random outcome."""
    name: str = field(default="Foggy", init=False)
    description: str = field(default="Random +0 to +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 4)
        return total


@dataclass
class Stormy(AlienPower):
    """Stormy - Violent weather. +4 on offense."""
    name: str = field(default="Stormy", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Humid(AlienPower):
    """Humid - Heavy air. -1 to all."""
    name: str = field(default="Humid", init=False)
    description: str = field(default="-1 to both sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Freezing(AlienPower):
    """Freezing - Cold snap. Freeze opponent allies."""
    name: str = field(default="Freezing", init=False)
    description: str = field(default="Opponent allies don't count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hailing(AlienPower):
    """Hailing - Ice pellets. +3 first encounter."""
    name: str = field(default="Hailing", init=False)
    description: str = field(default="+3 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Drizzle(AlienPower):
    """Drizzle - Light rain. +1 constant."""
    name: str = field(default="Drizzle", init=False)
    description: str = field(default="+1 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 1
        return total


@dataclass
class Overcast(AlienPower):
    """Overcast - Gray skies. Draw on win."""
    name: str = field(default="Overcast", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Breezy(AlienPower):
    """Breezy - Light wind. Retrieve ship from warp."""
    name: str = field(default="Breezy", init=False)
    description: str = field(default="Retrieve 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Muggy(AlienPower):
    """Muggy - Thick air. +1 per card in hand."""
    name: str = field(default="Muggy", init=False)
    description: str = field(default="+1 per card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Clear(AlienPower):
    """Clear - Perfect visibility. Win ties."""
    name: str = field(default="Clear", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
WEATHER_CLASSIC_POWERS = [
    Sunny, Cloudy, Rainy, Windy, Snowy, Foggy, Stormy,
    Humid, Freezing, Hailing, Drizzle, Overcast, Breezy,
    Muggy, Clear,
]

for power_class in WEATHER_CLASSIC_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
