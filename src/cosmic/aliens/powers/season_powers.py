"""
Season Powers - Season and time-of-year themed aliens.
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
class Spring(AlienPower):
    """Spring - New beginnings. Extra ship recovery."""
    name: str = field(default="Spring", init=False)
    description: str = field(default="Retrieve 2 extra ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Summer(AlienPower):
    """Summer - Peak power. +3 on offense."""
    name: str = field(default="Summer", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Autumn(AlienPower):
    """Autumn - Harvest time. Draw card on win."""
    name: str = field(default="Autumn", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Winter(AlienPower):
    """Winter - Cold defense. +3 on defense."""
    name: str = field(default="Winter", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Equinox(AlienPower):
    """Equinox - Perfect balance. +2 always."""
    name: str = field(default="Equinox", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Solstice(AlienPower):
    """Solstice - Extreme power. +5 or -2."""
    name: str = field(default="Solstice", init=False)
    description: str = field(default="+5 on first encounter, -2 otherwise.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            if game.encounter_number == 1:
                return total + 5
            return total - 2
        return total


@dataclass
class Monsoon(AlienPower):
    """Monsoon - Overwhelming force. +4 with 4 ships."""
    name: str = field(default="Monsoon", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drought(AlienPower):
    """Drought - Resource denial. -2 to opponent."""
    name: str = field(default="Drought", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harvest(AlienPower):
    """Harvest - Gather resources. +1 per card in hand."""
    name: str = field(default="Harvest", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Bloom(AlienPower):
    """Bloom - Growth explosion. +1 per home colony."""
    name: str = field(default="Bloom", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + home_count
        return total


@dataclass
class Frost(AlienPower):
    """Frost - Cold snap. Freeze opponent's allies."""
    name: str = field(default="Frost", init=False)
    description: str = field(default="Opponent allies don't count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thaw(AlienPower):
    """Thaw - Breaking free. Retrieve all ships from warp."""
    name: str = field(default="Thaw", init=False)
    description: str = field(default="Retrieve all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Renewal(AlienPower):
    """Renewal - Fresh start. Draw new hand."""
    name: str = field(default="Renewal", init=False)
    description: str = field(default="Discard hand, draw 8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dormancy(AlienPower):
    """Dormancy - Wait and recover. Ships return home."""
    name: str = field(default="Dormancy", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blossom(AlienPower):
    """Blossom - Full bloom. +3 with allies."""
    name: str = field(default="Blossom", init=False)
    description: str = field(default="+3 when you have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
SEASON_POWERS = [
    Spring, Summer, Autumn, Winter, Equinox, Solstice,
    Monsoon, Drought, Harvest, Bloom, Frost, Thaw,
    Renewal, Dormancy, Blossom,
]

for power_class in SEASON_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
