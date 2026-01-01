"""
Sense Powers - Aliens based on the five senses and perception.
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
class Seer(AlienPower):
    """Seer - Enhanced sight. See opponent's card."""
    name: str = field(default="Seer", init=False)
    description: str = field(default="View opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Listener(AlienPower):
    """Listener - Acute hearing. Hear alliances forming."""
    name: str = field(default="Listener", init=False)
    description: str = field(default="Know ally counts before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Taster(AlienPower):
    """Taster - Refined taste. +2 on defense."""
    name: str = field(default="Taster", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Smeller(AlienPower):
    """Smeller - Keen scent. Detect negotiates."""
    name: str = field(default="Smeller", init=False)
    description: str = field(default="Know if opponent plays negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Toucher(AlienPower):
    """Toucher - Sensitive touch. +1 per ship committed."""
    name: str = field(default="Toucher", init=False)
    description: str = field(default="+1 per your ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blind(AlienPower):
    """Blind - No sight. Cards random but +4."""
    name: str = field(default="Blind", init=False)
    description: str = field(default="Random card but +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Deaf(AlienPower):
    """Deaf - Cannot hear. Immune to negotiates."""
    name: str = field(default="Deaf", init=False)
    description: str = field(default="Ignore negotiate cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sixth(AlienPower):
    """Sixth - Sixth sense. +3 when attacked."""
    name: str = field(default="Sixth", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Perceiver(AlienPower):
    """Perceiver - All senses. +1 per player."""
    name: str = field(default="Perceiver", init=False)
    description: str = field(default="+1 per player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(game.players)
        return total


@dataclass
class Feeler(AlienPower):
    """Feeler - Emotional sense. +2 with allies."""
    name: str = field(default="Feeler", init=False)
    description: str = field(default="+2 when you have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sensory(AlienPower):
    """Sensory - Full perception. See top deck card."""
    name: str = field(default="Sensory", init=False)
    description: str = field(default="View top destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Intuition(AlienPower):
    """Intuition - Gut feeling. Win ties."""
    name: str = field(default="Intuition", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Numb(AlienPower):
    """Numb - No feeling. Ships go home not warp."""
    name: str = field(default="Numb", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Awareness(AlienPower):
    """Awareness - Total awareness. Draw on win."""
    name: str = field(default="Awareness", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Synesthete(AlienPower):
    """Synesthete - Mixed senses. Random +1 to +5."""
    name: str = field(default="Synesthete", init=False)
    description: str = field(default="Random +1 to +5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 5)
        return total


# Register all powers
SENSE_POWERS = [
    Seer, Listener, Taster, Smeller, Toucher, Blind, Deaf,
    Sixth, Perceiver, Feeler, Sensory, Intuition, Numb,
    Awareness, Synesthete,
]

for power_class in SENSE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
