"""
Psychic Powers - Aliens with mental and telepathic abilities.
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
class Clairvoyant(AlienPower):
    """
    Clairvoyant - Future Sight.
    See the next 3 destiny cards at any time.
    """
    name: str = field(default="Clairvoyant", init=False)
    description: str = field(default="See next 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dominator(AlienPower):
    """
    Dominator - Mind Control.
    Once per encounter, take control of one opponent ally.
    """
    name: str = field(default="Dominator", init=False)
    description: str = field(default="Control opponent ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dreamer(AlienPower):
    """
    Dreamer - Dream Walker.
    When you lose, opponent doesn't gain colonies.
    """
    name: str = field(default="Dreamer", init=False)
    description: str = field(default="Attacker wins but no colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hypnotist(AlienPower):
    """
    Hypnotist - Hypnotic Gaze.
    Once per encounter, force opponent to commit max ships.
    """
    name: str = field(default="Hypnotist", init=False)
    description: str = field(default="Force max ship commitment.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Illusory_Alt(AlienPower):
    """
    Illusory_Alt - False Vision.
    Your encounter card appears as any value until reveal.
    """
    name: str = field(default="Illusory_Alt", init=False)
    description: str = field(default="Card appears as any value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mentalist(AlienPower):
    """
    Mentalist - Mental Force.
    Add +2 for each card in your hand.
    """
    name: str = field(default="Mentalist", init=False)
    description: str = field(default="+2 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Perceiver(AlienPower):
    """
    Perceiver - Enhanced Perception.
    Know the exact value of opponent's encounter card.
    """
    name: str = field(default="Perceiver", init=False)
    description: str = field(default="Know opponent's card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Projector(AlienPower):
    """
    Projector - Astral Projection.
    Your ships are never in danger when attacking.
    """
    name: str = field(default="Projector", init=False)
    description: str = field(default="Ships safe when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Psychic(AlienPower):
    """
    Psychic - Mental Powers.
    Once per encounter, swap encounter cards with opponent.
    """
    name: str = field(default="Psychic", init=False)
    description: str = field(default="Swap encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Reader(AlienPower):
    """
    Reader - Mind Reader.
    See all players' hands at start of encounter.
    """
    name: str = field(default="Reader", init=False)
    description: str = field(default="See all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seer(AlienPower):
    """
    Seer - Vision.
    Look at top 5 cards of cosmic deck.
    """
    name: str = field(default="Seer", init=False)
    description: str = field(default="See top 5 cosmic cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sender(AlienPower):
    """
    Sender - Telepathy.
    Give 1 card to an ally before encounter.
    """
    name: str = field(default="Sender", init=False)
    description: str = field(default="Give ally a card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Telepath(AlienPower):
    """
    Telepath - Mind Link.
    Opponent must play their highest or lowest card.
    """
    name: str = field(default="Telepath", init=False)
    description: str = field(default="Force opponent card choice.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Telekinetic(AlienPower):
    """
    Telekinetic - Mind Over Matter.
    Move ships between your colonies at will.
    """
    name: str = field(default="Telekinetic", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thoughter(AlienPower):
    """
    Thoughter - Thought Form.
    Once per game, replay your last encounter card.
    """
    name: str = field(default="Thoughter", init=False)
    description: str = field(default="Replay last card once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Visionary_Alt(AlienPower):
    """
    Visionary_Alt - Future Vision.
    See result before committing ships.
    """
    name: str = field(default="Visionary_Alt", init=False)
    description: str = field(default="See result before ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Warper(AlienPower):
    """
    Warper - Reality Warp.
    Once per encounter, change the target planet.
    """
    name: str = field(default="Warper", init=False)
    description: str = field(default="Change target planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Whisperer(AlienPower):
    """
    Whisperer - Subtle Influence.
    Allies join you secretly (not revealed until resolution).
    """
    name: str = field(default="Whisperer", init=False)
    description: str = field(default="Secret allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Clairvoyant())
AlienRegistry.register(Dominator())
AlienRegistry.register(Dreamer())
AlienRegistry.register(Hypnotist())
AlienRegistry.register(Illusory_Alt())
AlienRegistry.register(Mentalist())
AlienRegistry.register(Perceiver())
AlienRegistry.register(Projector())
AlienRegistry.register(Psychic())
AlienRegistry.register(Reader())
AlienRegistry.register(Seer())
AlienRegistry.register(Sender())
AlienRegistry.register(Telepath())
AlienRegistry.register(Telekinetic())
AlienRegistry.register(Thoughter())
AlienRegistry.register(Visionary_Alt())
AlienRegistry.register(Warper())
AlienRegistry.register(Whisperer())
