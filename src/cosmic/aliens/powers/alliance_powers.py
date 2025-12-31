"""
Alliance Powers - Aliens with teamwork and cooperation abilities.
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
class Ally(AlienPower):
    """
    Ally - True Friend.
    Always accept alliance invites.
    """
    name: str = field(default="Ally", init=False)
    description: str = field(default="Accept all invites.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bonder(AlienPower):
    """
    Bonder - Create Bond.
    Ally ships count double.
    """
    name: str = field(default="Bonder", init=False)
    description: str = field(default="Double ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brotherhood(AlienPower):
    """
    Brotherhood - United Front.
    Allies share rewards.
    """
    name: str = field(default="Brotherhood", init=False)
    description: str = field(default="Share rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Captain(AlienPower):
    """
    Captain - Lead Team.
    Command ally ships.
    """
    name: str = field(default="Captain", init=False)
    description: str = field(default="Command allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coalition(AlienPower):
    """
    Coalition - Group Power.
    +1 per ally in game.
    """
    name: str = field(default="Coalition", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Collaborator(AlienPower):
    """
    Collaborator - Work Together.
    Share cards with ally.
    """
    name: str = field(default="Collaborator", init=False)
    description: str = field(default="Share cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Comrade(AlienPower):
    """
    Comrade - Close Ally.
    Draw when ally draws.
    """
    name: str = field(default="Comrade", init=False)
    description: str = field(default="Copy ally draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Federation(AlienPower):
    """
    Federation - United Planets.
    Win shared with allies.
    """
    name: str = field(default="Federation", init=False)
    description: str = field(default="Shared victory.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Friend(AlienPower):
    """
    Friend - Make Friends.
    Force player to ally.
    """
    name: str = field(default="Friend", init=False)
    description: str = field(default="Force alliance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Helper(AlienPower):
    """
    Helper - Aid Others.
    Ally gets +2.
    """
    name: str = field(default="Helper", init=False)
    description: str = field(default="Ally +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Leader(AlienPower):
    """
    Leader - Inspire.
    All allies +1.
    """
    name: str = field(default="Leader", init=False)
    description: str = field(default="All allies +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Partner(AlienPower):
    """
    Partner - Joint Venture.
    Share colony with ally.
    """
    name: str = field(default="Partner", init=False)
    description: str = field(default="Share colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Recruiter(AlienPower):
    """
    Recruiter - Gather Allies.
    Invite extra allies.
    """
    name: str = field(default="Recruiter", init=False)
    description: str = field(default="Extra invites.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Supporter(AlienPower):
    """
    Supporter - Back Up.
    Ally ships immune to warp.
    """
    name: str = field(default="Supporter", init=False)
    description: str = field(default="Ally ship immunity.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Teammate(AlienPower):
    """
    Teammate - Team Player.
    +3 when you have allies.
    """
    name: str = field(default="Teammate", init=False)
    description: str = field(default="+3 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Unifier(AlienPower):
    """
    Unifier - Unite All.
    Force all to ally.
    """
    name: str = field(default="Unifier", init=False)
    description: str = field(default="Universal alliance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Ally())
AlienRegistry.register(Bonder())
AlienRegistry.register(Brotherhood())
AlienRegistry.register(Captain())
AlienRegistry.register(Coalition())
AlienRegistry.register(Collaborator())
AlienRegistry.register(Comrade())
AlienRegistry.register(Federation())
AlienRegistry.register(Friend())
AlienRegistry.register(Helper())
AlienRegistry.register(Leader())
AlienRegistry.register(Partner())
AlienRegistry.register(Recruiter())
AlienRegistry.register(Supporter())
AlienRegistry.register(Teammate())
AlienRegistry.register(Unifier())
