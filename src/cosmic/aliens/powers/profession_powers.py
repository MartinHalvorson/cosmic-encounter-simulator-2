"""
Profession Powers - Job and career-themed aliens.
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
class Banker(AlienPower):
    """Banker - Financial expert. +1 per card in hand."""
    name: str = field(default="Banker", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Lawyer(AlienPower):
    """Lawyer - Legal expert. Negotiate cards can't fail."""
    name: str = field(default="Lawyer", init=False)
    description: str = field(default="Negotiate deals always succeed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Doctor(AlienPower):
    """Doctor - Healer. Retrieve 2 ships from warp after encounters."""
    name: str = field(default="Doctor_Alt", init=False)
    description: str = field(default="Retrieve 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Teacher(AlienPower):
    """Teacher - Knowledge sharer. Allies draw 1 card each."""
    name: str = field(default="Teacher", init=False)
    description: str = field(default="Allies draw cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Engineer(AlienPower):
    """Engineer - Builder. +2 defending home planets."""
    name: str = field(default="Engineer_Alt", init=False)
    description: str = field(default="+2 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 2
        return total


@dataclass
class Architect(AlienPower):
    """Architect - Designer. Build colony on empty planet for free."""
    name: str = field(default="Architect", init=False)
    description: str = field(default="Free colony on empty planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scientist(AlienPower):
    """Scientist - Researcher. Look at top 3 deck cards."""
    name: str = field(default="Scientist_Alt", init=False)
    description: str = field(default="View top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pilot(AlienPower):
    """Pilot - Ship commander. Launch up to 6 ships."""
    name: str = field(default="Pilot", init=False)
    description: str = field(default="Launch up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Merchant(AlienPower):
    """Merchant - Trader. Trade cards before encounters."""
    name: str = field(default="Merchant_Alt", init=False)
    description: str = field(default="Trade cards freely.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Artist(AlienPower):
    """Artist - Creative soul. Create new card from discards."""
    name: str = field(default="Artist", init=False)
    description: str = field(default="Reclaim discarded card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Judge(AlienPower):
    """Judge - Arbiter. Win all ties."""
    name: str = field(default="Judge", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Farmer(AlienPower):
    """Farmer - Grower. +1 per home colony."""
    name: str = field(default="Farmer", init=False)
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
class Miner(AlienPower):
    """Miner - Digger. Draw extra card each turn."""
    name: str = field(default="Miner_Alt", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chef(AlienPower):
    """Chef - Creator. Combine two attack cards."""
    name: str = field(default="Chef", init=False)
    description: str = field(default="Play two attack cards summed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Detective(AlienPower):
    """Detective - Investigator. See opponent's entire hand."""
    name: str = field(default="Detective", init=False)
    description: str = field(default="View opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Banker())
AlienRegistry.register(Lawyer())
AlienRegistry.register(Doctor())
AlienRegistry.register(Teacher())
AlienRegistry.register(Engineer())
AlienRegistry.register(Architect())
AlienRegistry.register(Scientist())
AlienRegistry.register(Pilot())
AlienRegistry.register(Merchant())
AlienRegistry.register(Artist())
AlienRegistry.register(Judge())
AlienRegistry.register(Farmer())
AlienRegistry.register(Miner())
AlienRegistry.register(Chef())
AlienRegistry.register(Detective())
