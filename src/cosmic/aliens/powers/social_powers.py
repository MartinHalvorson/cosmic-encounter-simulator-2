"""
Social Powers - Aliens with alliance and diplomatic abilities.
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
class Ambassador(AlienPower):
    """
    Ambassador - Diplomatic Envoy.
    Invite all players as allies every encounter.
    """
    name: str = field(default="Ambassador", init=False)
    description: str = field(default="Invite all as allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Betrayer(AlienPower):
    """
    Betrayer - Backstabber.
    Switch sides after alliances are committed.
    """
    name: str = field(default="Betrayer", init=False)
    description: str = field(default="Switch sides after allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Charmer(AlienPower):
    """
    Charmer - Irresistible.
    Invited allies must accept.
    """
    name: str = field(default="Charmer", init=False)
    description: str = field(default="Force ally acceptance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Coalition(AlienPower):
    """
    Coalition - Group Power.
    +2 for each ally on your side.
    """
    name: str = field(default="Coalition", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Consensus(AlienPower):
    """
    Consensus - Group Decision.
    Allies vote on encounter outcome.
    """
    name: str = field(default="Consensus", init=False)
    description: str = field(default="Allies vote.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Emissary(AlienPower):
    """
    Emissary - Peace Maker.
    Force negotiation once per turn.
    """
    name: str = field(default="Emissary", init=False)
    description: str = field(default="Force negotiation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Faction(AlienPower):
    """
    Faction - Alliance Builder.
    Ally ships count as double.
    """
    name: str = field(default="Faction", init=False)
    description: str = field(default="Ally ships x2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Friend(AlienPower):
    """
    Friend - Trusted Ally.
    Allies get +1 rewards each.
    """
    name: str = field(default="Friend", init=False)
    description: str = field(default="Allies +1 rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Influence(AlienPower):
    """
    Influence - Persuasion.
    Convert opponent ally to your side.
    """
    name: str = field(default="Influence", init=False)
    description: str = field(default="Convert ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Liaison(AlienPower):
    """
    Liaison - Connection.
    Draw card when ally joins.
    """
    name: str = field(default="Liaison", init=False)
    description: str = field(default="Draw per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mediator(AlienPower):
    """
    Mediator - Conflict Resolver.
    End encounter in deal automatically.
    """
    name: str = field(default="Mediator", init=False)
    description: str = field(default="Force deal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Peacekeeper(AlienPower):
    """
    Peacekeeper - No Violence.
    No ships lost this encounter.
    """
    name: str = field(default="Peacekeeper", init=False)
    description: str = field(default="No ships lost.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Politician(AlienPower):
    """
    Politician - Promise Maker.
    Make binding deals with opponents.
    """
    name: str = field(default="Politician", init=False)
    description: str = field(default="Binding deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Recruiter(AlienPower):
    """
    Recruiter - Force Allies.
    Opponent allies must decline.
    """
    name: str = field(default="Recruiter", init=False)
    description: str = field(default="Block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spokesman(AlienPower):
    """
    Spokesman - Voice.
    Speak for allies in negotiation.
    """
    name: str = field(default="Spokesman", init=False)
    description: str = field(default="Negotiate for allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Uniter(AlienPower):
    """
    Uniter - Bring Together.
    Win if all players ally with you.
    """
    name: str = field(default="Uniter", init=False)
    description: str = field(default="Win with all allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Ambassador())
AlienRegistry.register(Betrayer())
AlienRegistry.register(Charmer())
AlienRegistry.register(Coalition())
AlienRegistry.register(Consensus())
AlienRegistry.register(Emissary())
AlienRegistry.register(Faction())
AlienRegistry.register(Friend())
AlienRegistry.register(Influence())
AlienRegistry.register(Liaison())
AlienRegistry.register(Mediator())
AlienRegistry.register(Peacekeeper())
AlienRegistry.register(Politician())
AlienRegistry.register(Recruiter())
AlienRegistry.register(Spokesman())
AlienRegistry.register(Uniter())
