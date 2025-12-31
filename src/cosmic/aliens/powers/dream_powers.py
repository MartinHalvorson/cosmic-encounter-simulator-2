"""
Dream Powers - Dream and sleep themed aliens.
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
class Dreamer(AlienPower):
    """Dreamer - Dream visions. See opponent's card."""
    name: str = field(default="Dreamer", init=False)
    description: str = field(default="View opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sleeper(AlienPower):
    """Sleeper - Deep sleep. Ships return home."""
    name: str = field(default="Sleeper", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nightmare(AlienPower):
    """Nightmare - Terrifying. -3 to opponent."""
    name: str = field(default="Nightmare", init=False)
    description: str = field(default="-3 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lucid(AlienPower):
    """Lucid - Control dreams. Choose card effect."""
    name: str = field(default="Lucid", init=False)
    description: str = field(default="Card acts as +10 or negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Insomniac(AlienPower):
    """Insomniac - Never sleep. Extra encounter."""
    name: str = field(default="Insomniac", init=False)
    description: str = field(default="May have third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sleepwalker(AlienPower):
    """Sleepwalker - Move while sleeping. Random bonus."""
    name: str = field(default="Sleepwalker", init=False)
    description: str = field(default="Random +0 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 6)
        return total


@dataclass
class Daydreamer(AlienPower):
    """Daydreamer - Pleasant thoughts. +2 always."""
    name: str = field(default="Daydreamer", init=False)
    description: str = field(default="+2 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Awakener(AlienPower):
    """Awakener - Wake others. Retrieve ships from warp."""
    name: str = field(default="Awakener", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Napper(AlienPower):
    """Napper - Quick sleep. +3 on defense."""
    name: str = field(default="Napper", init=False)
    description: str = field(default="+3 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Reverie(AlienPower):
    """Reverie - Pleasant dream. Draw on win."""
    name: str = field(default="Reverie", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Phantasm(AlienPower):
    """Phantasm - Dream illusion. +4 on first encounter."""
    name: str = field(default="Phantasm", init=False)
    description: str = field(default="+4 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Slumber(AlienPower):
    """Slumber - Deep rest. +1 per home colony."""
    name: str = field(default="Slumber", init=False)
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
class Vision(AlienPower):
    """Vision - Prophetic dream. See destiny."""
    name: str = field(default="Vision", init=False)
    description: str = field(default="View top destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hypnos(AlienPower):
    """Hypnos - God of sleep. +3 on offense."""
    name: str = field(default="Hypnos", init=False)
    description: str = field(default="+3 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Morpheus(AlienPower):
    """Morpheus - Dream shaper. Win ties."""
    name: str = field(default="Morpheus", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
DREAM_POWERS = [
    Dreamer, Sleeper, Nightmare, Lucid, Insomniac, Sleepwalker,
    Daydreamer, Awakener, Napper, Reverie, Phantasm, Slumber,
    Vision, Hypnos, Morpheus,
]

for power_class in DREAM_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
