"""
Career Powers - Job and profession themed aliens.
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
class Soldier(AlienPower):
    """Soldier - Power of Combat. +4 on offense."""
    name: str = field(default="Soldier", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Merchant(AlienPower):
    """Merchant - Power of Trade. Extra cards."""
    name: str = field(default="Merchant", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scholar(AlienPower):
    """Scholar - Power of Knowledge. See deck."""
    name: str = field(default="Scholar", init=False)
    description: str = field(default="Look at top 3 cards of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Farmer(AlienPower):
    """Farmer - Power of Growth. Extra ships."""
    name: str = field(default="Farmer", init=False)
    description: str = field(default="Add 1 ship to colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Miner(AlienPower):
    """Miner - Power of Extraction. Draw from bottom."""
    name: str = field(default="Miner", init=False)
    description: str = field(default="Draw from bottom of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blacksmith(AlienPower):
    """Blacksmith - Power of Crafting. +3 always."""
    name: str = field(default="Blacksmith", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Healer(AlienPower):
    """Healer - Power of Restoration. Retrieve ships."""
    name: str = field(default="Healer", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sailor(AlienPower):
    """Sailor - Power of Navigation. Choose destiny."""
    name: str = field(default="Sailor", init=False)
    description: str = field(default="Redraw destiny once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diplomat(AlienPower):
    """Diplomat - Power of Negotiation. Deal bonus."""
    name: str = field(default="Diplomat", init=False)
    description: str = field(default="+2 cards when dealing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Guard(AlienPower):
    """Guard - Power of Protection. +4 on defense."""
    name: str = field(default="Guard", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Scout(AlienPower):
    """Scout - Power of Reconnaissance. See opponent card."""
    name: str = field(default="Scout", init=False)
    description: str = field(default="View opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spy(AlienPower):
    """Spy - Power of Intel. See hidden cards."""
    name: str = field(default="Spy", init=False)
    description: str = field(default="See all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Assassin(AlienPower):
    """Assassin - Power of Elimination. Remove ships."""
    name: str = field(default="Assassin", init=False)
    description: str = field(default="1 ship goes to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Architect(AlienPower):
    """Architect - Power of Building. Extra colony."""
    name: str = field(default="Architect", init=False)
    description: str = field(default="Win grants extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Banker(AlienPower):
    """Banker - Power of Wealth. Accumulate cards."""
    name: str = field(default="Banker", init=False)
    description: str = field(default="No hand limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lawyer(AlienPower):
    """Lawyer - Power of Rules. Cancel power."""
    name: str = field(default="Lawyer", init=False)
    description: str = field(default="Zap opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Teacher(AlienPower):
    """Teacher - Power of Learning. Give bonus."""
    name: str = field(default="Teacher", init=False)
    description: str = field(default="+2 to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pilot(AlienPower):
    """Pilot - Power of Flight. Attack anywhere."""
    name: str = field(default="Pilot", init=False)
    description: str = field(default="Ignore destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Captain(AlienPower):
    """Captain - Power of Command. +1 per ship."""
    name: str = field(default="Captain", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Admiral(AlienPower):
    """Admiral - Power of Fleet. +2 per ship."""
    name: str = field(default="Admiral", init=False)
    description: str = field(default="+2 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
CAREER_POWERS = [
    Soldier, Merchant, Scholar, Farmer, Miner, Blacksmith, Healer, Sailor, Diplomat, Guard,
    Scout, Spy, Assassin, Architect, Banker, Lawyer, Teacher, Pilot, Captain, Admiral,
]

for power_class in CAREER_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
