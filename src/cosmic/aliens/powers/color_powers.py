"""
Color Powers - Aliens with chromatic and color-based abilities.
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
class Azure(AlienPower):
    """
    Azure - Blue Power.
    +2 defense.
    """
    name: str = field(default="Azure", init=False)
    description: str = field(default="+2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 when defending."""
        if side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Crimson(AlienPower):
    """
    Crimson - Red Power.
    +3 attack.
    """
    name: str = field(default="Crimson", init=False)
    description: str = field(default="+3 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 when attacking."""
        if side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Emerald(AlienPower):
    """
    Emerald - Green Power.
    +1 per ally.
    """
    name: str = field(default="Emerald", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Golden(AlienPower):
    """
    Golden - Gold Power.
    +4 constant.
    """
    name: str = field(default="Golden", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 constant bonus."""
        return total + 4


@dataclass
class Ivory(AlienPower):
    """
    Ivory - White Power.
    See all cards.
    """
    name: str = field(default="Ivory", init=False)
    description: str = field(default="See all cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Obsidian(AlienPower):
    """
    Obsidian - Black Power.
    Hide information.
    """
    name: str = field(default="Obsidian", init=False)
    description: str = field(default="Hide info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scarlet(AlienPower):
    """
    Scarlet - Deep Red.
    Extra attack power.
    """
    name: str = field(default="Scarlet", init=False)
    description: str = field(default="Extra attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Silver(AlienPower):
    """
    Silver - Silver Power.
    +2 constant.
    """
    name: str = field(default="Silver", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 constant bonus."""
        return total + 2


@dataclass
class Violet(AlienPower):
    """
    Violet - Purple Power.
    Mix ally powers.
    """
    name: str = field(default="Violet", init=False)
    description: str = field(default="Mix powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Azure())
AlienRegistry.register(Crimson())
AlienRegistry.register(Emerald())
AlienRegistry.register(Golden())
AlienRegistry.register(Ivory())
AlienRegistry.register(Obsidian())
AlienRegistry.register(Scarlet())
AlienRegistry.register(Silver())
AlienRegistry.register(Violet())
