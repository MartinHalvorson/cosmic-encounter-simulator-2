"""
Predator Powers - Aliens with hunting and stalking abilities.
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
class Apex(AlienPower):
    """
    Apex - Top Predator.
    +5 vs weaker opponent.
    """
    name: str = field(default="Apex", init=False)
    description: str = field(default="+5 vs weak.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Devourer(AlienPower):
    """
    Devourer - Consume Enemy.
    Take opponent's cards.
    """
    name: str = field(default="Devourer", init=False)
    description: str = field(default="Take cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Feral(AlienPower):
    """
    Feral - Wild Attack.
    Random +0 to +8.
    """
    name: str = field(default="Feral", init=False)
    description: str = field(default="Random +0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add random 0-8 bonus."""
        return total + random.randint(0, 8)


@dataclass
class Hunter_Alt(AlienPower):
    """
    Hunter_Alt - Track Prey.
    Choose attack target.
    """
    name: str = field(default="Hunter_Alt", init=False)
    description: str = field(default="Choose target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lurker_Alt(AlienPower):
    """
    Lurker_Alt - Wait in Shadows.
    Attack from hiding.
    """
    name: str = field(default="Lurker_Alt", init=False)
    description: str = field(default="Hidden attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pouncer(AlienPower):
    """
    Pouncer - Quick Strike.
    First hit bonus.
    """
    name: str = field(default="Pouncer", init=False)
    description: str = field(default="First strike.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Predator_Alt(AlienPower):
    """
    Predator_Alt - Born Killer.
    +4 when attacking.
    """
    name: str = field(default="Predator_Alt", init=False)
    description: str = field(default="+4 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking."""
        if side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Prowler(AlienPower):
    """
    Prowler - Stalk Target.
    Know opponent's card.
    """
    name: str = field(default="Prowler", init=False)
    description: str = field(default="See card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Savage(AlienPower):
    """
    Savage - Brutal Attack.
    Extra ship damage.
    """
    name: str = field(default="Savage", init=False)
    description: str = field(default="Extra damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scavenger_Alt(AlienPower):
    """
    Scavenger_Alt - Pick Remains.
    Take from warp.
    """
    name: str = field(default="Scavenger_Alt", init=False)
    description: str = field(default="Take from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stalker(AlienPower):
    """
    Stalker - Follow Prey.
    Attack same player again.
    """
    name: str = field(default="Stalker", init=False)
    description: str = field(default="Attack again.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Swarm_Alt(AlienPower):
    """
    Swarm_Alt - Attack in Numbers.
    +1 per ally ship.
    """
    name: str = field(default="Swarm_Alt", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Viper(AlienPower):
    """
    Viper - Poison Strike.
    Opponent loses card.
    """
    name: str = field(default="Viper", init=False)
    description: str = field(default="Poison card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Apex())
AlienRegistry.register(Devourer())
AlienRegistry.register(Feral())
AlienRegistry.register(Hunter_Alt())
AlienRegistry.register(Lurker_Alt())
AlienRegistry.register(Pouncer())
AlienRegistry.register(Predator_Alt())
AlienRegistry.register(Prowler())
AlienRegistry.register(Savage())
AlienRegistry.register(Scavenger_Alt())
AlienRegistry.register(Stalker())
AlienRegistry.register(Swarm_Alt())
AlienRegistry.register(Viper())
