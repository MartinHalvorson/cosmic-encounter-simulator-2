"""
Nature Powers - Aliens themed around natural elements and creatures.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Avalanche(AlienPower):
    """
    Avalanche - Crushing Force.
    When you win, opponent's ships on adjacent planets go to warp.
    """
    name: str = field(default="Avalanche", init=False)
    description: str = field(default="Extra ships to warp on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blizzard(AlienPower):
    """
    Blizzard - Freezing Storm.
    Once per encounter, reduce opponent's total by 4.
    """
    name: str = field(default="Blizzard", init=False)
    description: str = field(default="Reduce opponent's total by 4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Earthquake(AlienPower):
    """
    Earthquake - Ground Shaker.
    When defending home system, add +5 to your total.
    """
    name: str = field(default="Earthquake", init=False)
    description: str = field(default="Add +5 when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when defending home."""
        if side == Side.DEFENSE and game.defense == player:
            if game.defense_planet and game.defense_planet.owner == player:
                return total + 5
        return total


@dataclass
class Flood(AlienPower):
    """
    Flood - Rising Waters.
    After losing, retrieve half your ships from warp.
    """
    name: str = field(default="Flood", init=False)
    description: str = field(default="Retrieve half ships after losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hurricane(AlienPower):
    """
    Hurricane - Destructive Wind.
    Once per turn, move 3 ships from any planet to any colony.
    """
    name: str = field(default="Hurricane", init=False)
    description: str = field(default="Move 3 ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lightning(AlienPower):
    """
    Lightning - Electric Strike.
    When you play an attack card 20+, add +3.
    """
    name: str = field(default="Lightning", init=False)
    description: str = field(default="Add +3 with attack 20+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Meteor(AlienPower):
    """
    Meteor - Space Rock.
    When attacking, your ships count double.
    """
    name: str = field(default="Meteor", init=False)
    description: str = field(default="Ships count double when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        """Double ships when attacking."""
        if side == Side.OFFENSE and game.offense == player:
            return count * 2
        return count


@dataclass
class Storm(AlienPower):
    """
    Storm - Tempest.
    Once per encounter, discard top 3 cards of cosmic deck.
    """
    name: str = field(default="Storm", init=False)
    description: str = field(default="Discard top 3 cosmic deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tide(AlienPower):
    """
    Tide - Ocean Current.
    Ships on foreign colonies count double for defense.
    """
    name: str = field(default="Tide", init=False)
    description: str = field(default="Foreign colony ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tornado(AlienPower):
    """
    Tornado - Spinning Destruction.
    When you lose, opponent also loses 2 ships.
    """
    name: str = field(default="Tornado", init=False)
    description: str = field(default="Opponent loses 2 ships when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tsunami(AlienPower):
    """
    Tsunami - Giant Wave.
    When winning by 10+, establish extra colony on any planet.
    """
    name: str = field(default="Tsunami", init=False)
    description: str = field(default="Extra colony on big wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Volcano(AlienPower):
    """
    Volcano - Eruption.
    Once per turn, destroy one ship on any planet (to warp).
    """
    name: str = field(default="Volcano", init=False)
    description: str = field(default="Destroy one ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Avalanche())
AlienRegistry.register(Blizzard())
AlienRegistry.register(Earthquake())
AlienRegistry.register(Flood())
AlienRegistry.register(Hurricane())
AlienRegistry.register(Lightning())
AlienRegistry.register(Meteor())
AlienRegistry.register(Storm())
AlienRegistry.register(Tide())
AlienRegistry.register(Tornado())
AlienRegistry.register(Tsunami())
AlienRegistry.register(Volcano())
