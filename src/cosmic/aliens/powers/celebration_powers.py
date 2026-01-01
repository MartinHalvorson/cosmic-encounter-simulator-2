"""
Celebration Powers - Aliens with festive and holiday abilities.
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
class Caroler(AlienPower):
    """
    Caroler - Sing Songs.
    Ally bonus +1.
    """
    name: str = field(default="Caroler", init=False)
    description: str = field(default="Ally +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Celebrant(AlienPower):
    """
    Celebrant - Party Time.
    +2 on wins.
    """
    name: str = field(default="Celebrant", init=False)
    description: str = field(default="+2 on wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cupid(AlienPower):
    """
    Cupid - Love Arrow.
    Force alliance.
    """
    name: str = field(default="Cupid", init=False)
    description: str = field(default="Force ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Elf(AlienPower):
    """
    Elf - Helper.
    +1 per ally.
    """
    name: str = field(default="Elf", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Firework(AlienPower):
    """
    Firework - Big Bang.
    +4 once per game.
    """
    name: str = field(default="Firework", init=False)
    description: str = field(default="+4 once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class GiftGiver(AlienPower):
    """
    GiftGiver - Share Presents.
    Give cards for bonus.
    """
    name: str = field(default="GiftGiver", init=False)
    description: str = field(default="Give for bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Leprechaun(AlienPower):
    """
    Leprechaun - Lucky Charm.
    +2 random bonus.
    """
    name: str = field(default="Leprechaun", init=False)
    description: str = field(default="+2 luck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 luck bonus."""
        return total + 2


@dataclass
class PartyHost(AlienPower):
    """
    PartyHost - Throw Party.
    All join encounter.
    """
    name: str = field(default="PartyHost", init=False)
    description: str = field(default="All join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pilgrim(AlienPower):
    """
    Pilgrim - Long Journey.
    +1 per colony.
    """
    name: str = field(default="Pilgrim", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Santa(AlienPower):
    """
    Santa - Give Gifts.
    All get cards.
    """
    name: str = field(default="Santa", init=False)
    description: str = field(default="All get cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Caroler())
AlienRegistry.register(Celebrant())
AlienRegistry.register(Cupid())
AlienRegistry.register(Elf())
AlienRegistry.register(Firework())
AlienRegistry.register(GiftGiver())
AlienRegistry.register(Leprechaun())
AlienRegistry.register(PartyHost())
AlienRegistry.register(Pilgrim())
AlienRegistry.register(Santa())
