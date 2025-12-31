"""
Communication Powers - Aliens with telepathy and signaling abilities.
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
class Announcer(AlienPower):
    """
    Announcer - Broadcast Intent.
    Force opponent to reveal card.
    """
    name: str = field(default="Announcer", init=False)
    description: str = field(default="Force reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Broadcaster(AlienPower):
    """
    Broadcaster - Wide Signal.
    All players see your card.
    """
    name: str = field(default="Broadcaster", init=False)
    description: str = field(default="Show your card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Caller(AlienPower):
    """
    Caller - Summon Aid.
    Force allies to join.
    """
    name: str = field(default="Caller", init=False)
    description: str = field(default="Force ally join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Channeler(AlienPower):
    """
    Channeler - Message Relay.
    Trade cards with ally.
    """
    name: str = field(default="Channeler", init=False)
    description: str = field(default="Trade with ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diplomat_Alt(AlienPower):
    """
    Diplomat_Alt - Negotiate.
    Convert attack to deal.
    """
    name: str = field(default="Diplomat_Alt", init=False)
    description: str = field(default="Force negotiation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Echo(AlienPower):
    """
    Echo - Repeat Signal.
    Use power twice.
    """
    name: str = field(default="Echo", init=False)
    description: str = field(default="Double power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Empath_Alt(AlienPower):
    """
    Empath_Alt - Feel Emotions.
    Know if opponent will negotiate.
    """
    name: str = field(default="Empath_Alt", init=False)
    description: str = field(default="Sense negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Herald(AlienPower):
    """
    Herald - Proclaim Victory.
    +2 for each ally.
    """
    name: str = field(default="Herald", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Interpreter(AlienPower):
    """
    Interpreter - Translate Intent.
    See opponent's hand.
    """
    name: str = field(default="Interpreter", init=False)
    description: str = field(default="See opponent hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Linguist(AlienPower):
    """
    Linguist - Speak All.
    Negotiate with anyone.
    """
    name: str = field(default="Linguist", init=False)
    description: str = field(default="Universal negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Messenger(AlienPower):
    """
    Messenger - Deliver News.
    Draw card when ally wins.
    """
    name: str = field(default="Messenger", init=False)
    description: str = field(default="Draw on ally win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mindlink(AlienPower):
    """
    Mindlink - Shared Thought.
    Know ally's card.
    """
    name: str = field(default="Mindlink", init=False)
    description: str = field(default="See ally card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Receiver(AlienPower):
    """
    Receiver - Get Signal.
    Draw extra when defending.
    """
    name: str = field(default="Receiver", init=False)
    description: str = field(default="Extra draw defend.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Signaler(AlienPower):
    """
    Signaler - Send Code.
    Allies get +1 each.
    """
    name: str = field(default="Signaler", init=False)
    description: str = field(default="Allies +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Telepath_Alt(AlienPower):
    """
    Telepath_Alt - Read Minds.
    See opponent's chosen card.
    """
    name: str = field(default="Telepath_Alt", init=False)
    description: str = field(default="See chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Transmitter(AlienPower):
    """
    Transmitter - Send Power.
    Give ally your bonus.
    """
    name: str = field(default="Transmitter", init=False)
    description: str = field(default="Share bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Announcer())
AlienRegistry.register(Broadcaster())
AlienRegistry.register(Caller())
AlienRegistry.register(Channeler())
AlienRegistry.register(Diplomat_Alt())
AlienRegistry.register(Echo())
AlienRegistry.register(Empath_Alt())
AlienRegistry.register(Herald())
AlienRegistry.register(Interpreter())
AlienRegistry.register(Linguist())
AlienRegistry.register(Messenger())
AlienRegistry.register(Mindlink())
AlienRegistry.register(Receiver())
AlienRegistry.register(Signaler())
AlienRegistry.register(Telepath_Alt())
AlienRegistry.register(Transmitter())
