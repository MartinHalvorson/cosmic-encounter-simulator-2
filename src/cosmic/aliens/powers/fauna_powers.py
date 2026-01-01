"""
Fauna Powers - Animal-themed aliens.
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
class Bear(AlienPower):
    """Bear - Power of Strength. +4 on offense."""
    name: str = field(default="Bear", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Eagle(AlienPower):
    """Eagle - Power of Vision. See opponent's card."""
    name: str = field(default="Eagle", init=False)
    description: str = field(default="View opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wolf(AlienPower):
    """Wolf - Power of the Pack. +1 per ally."""
    name: str = field(default="Wolf", init=False)
    description: str = field(default="+1 per ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Turtle(AlienPower):
    """Turtle - Power of Defense. +6 when defending."""
    name: str = field(default="Turtle", init=False)
    description: str = field(default="+6 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 6
        return total


@dataclass
class Fox(AlienPower):
    """Fox - Power of Cunning. Swap cards after reveal."""
    name: str = field(default="Fox", init=False)
    description: str = field(default="May swap encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hawk(AlienPower):
    """Hawk - Power of the Strike. +5 first attack."""
    name: str = field(default="Hawk", init=False)
    description: str = field(default="+5 on first encounter each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Owl(AlienPower):
    """Owl - Power of Wisdom. See hand before planning."""
    name: str = field(default="Owl", init=False)
    description: str = field(default="View any player's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shark(AlienPower):
    """Shark - Power of Blood. +2 per ship in warp."""
    name: str = field(default="Shark", init=False)
    description: str = field(default="+2 per ship opponent has in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crow(AlienPower):
    """Crow - Power of Collection. Draw from discard."""
    name: str = field(default="Crow", init=False)
    description: str = field(default="Draw 1 card from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lion(AlienPower):
    """Lion - Power of Majesty. Win ties."""
    name: str = field(default="Lion", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Snake(AlienPower):
    """Snake - Power of Venom. Poison ships."""
    name: str = field(default="Snake", init=False)
    description: str = field(default="1 opponent ship goes to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rabbit(AlienPower):
    """Rabbit - Power of Speed. Extra encounter."""
    name: str = field(default="Rabbit", init=False)
    description: str = field(default="May take third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deer(AlienPower):
    """Deer - Power of Flight. Ships escape warp."""
    name: str = field(default="Deer", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Elephant(AlienPower):
    """Elephant - Power of Memory. Know all played cards."""
    name: str = field(default="Elephant", init=False)
    description: str = field(default="See discard pile at any time.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monkey(AlienPower):
    """Monkey - Power of Mimicry. Copy opponent's alien."""
    name: str = field(default="Monkey", init=False)
    description: str = field(default="Use opponent's power this encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Panther(AlienPower):
    """Panther - Power of Stealth. Hide card value."""
    name: str = field(default="Panther", init=False)
    description: str = field(default="Card stays hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rhino(AlienPower):
    """Rhino - Power of Charge. +3 when attacking with 4 ships."""
    name: str = field(default="Rhino", init=False)
    description: str = field(default="+3 when attacking with max ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bat(AlienPower):
    """Bat - Power of Night. +3 at low totals."""
    name: str = field(default="Bat", init=False)
    description: str = field(default="+3 if card value is under 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boar(AlienPower):
    """Boar - Power of Ferocity. Random +1 to +6."""
    name: str = field(default="Boar", init=False)
    description: str = field(default="Add random 1-6 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 6)
        return total


@dataclass
class Gorilla(AlienPower):
    """Gorilla - Power of Might. +5 constant."""
    name: str = field(default="Gorilla", init=False)
    description: str = field(default="+5 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


# Register all powers
FAUNA_POWERS = [
    Bear, Eagle, Wolf, Turtle, Fox, Hawk, Owl, Shark, Crow, Lion,
    Snake, Rabbit, Deer, Elephant, Monkey, Panther, Rhino, Bat, Boar, Gorilla,
]

for power_class in FAUNA_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
