"""
Chaos Powers - Aliens with unpredictable, random abilities.
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
class Anarchy(AlienPower):
    """
    Anarchy - Rule Breaker.
    Ignore one game rule per encounter.
    """
    name: str = field(default="Anarchy", init=False)
    description: str = field(default="Ignore one rule.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Chance(AlienPower):
    """
    Chance - Lucky Roll.
    50% chance to double your card value.
    """
    name: str = field(default="Chance", init=False)
    description: str = field(default="50% double card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chaos_Alt(AlienPower):
    """
    Chaos_Alt - Pure Chaos.
    Randomize all encounter results.
    """
    name: str = field(default="Chaos_Alt", init=False)
    description: str = field(default="Random results.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Confusion(AlienPower):
    """
    Confusion - Mind Chaos.
    Swap random cards between hands.
    """
    name: str = field(default="Confusion", init=False)
    description: str = field(default="Swap random cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Disorder(AlienPower):
    """
    Disorder - Shuffle Ships.
    Randomize ship positions.
    """
    name: str = field(default="Disorder", init=False)
    description: str = field(default="Shuffle ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Entropy(AlienPower):
    """
    Entropy - Decay Force.
    All cards lose 2 value this encounter.
    """
    name: str = field(default="Entropy", init=False)
    description: str = field(default="Cards -2 value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fortune(AlienPower):
    """
    Fortune - Good Luck.
    Win all coin flips and random effects.
    """
    name: str = field(default="Fortune", init=False)
    description: str = field(default="Win random effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Madness(AlienPower):
    """
    Madness - Insane Action.
    Take random extra action.
    """
    name: str = field(default="Madness", init=False)
    description: str = field(default="Random extra action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mayhem(AlienPower):
    """
    Mayhem - Total Chaos.
    All players reveal cards simultaneously.
    """
    name: str = field(default="Mayhem", init=False)
    description: str = field(default="Simultaneous reveals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Misfortune(AlienPower):
    """
    Misfortune - Bad Luck.
    Opponent's random effects fail.
    """
    name: str = field(default="Misfortune", init=False)
    description: str = field(default="Opponent bad luck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pandemonium(AlienPower):
    """
    Pandemonium - Wild Card.
    Use any card as any other card.
    """
    name: str = field(default="Pandemonium", init=False)
    description: str = field(default="Wild card use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Random(AlienPower):
    """
    Random - Pure Chance.
    Play random card from hand.
    """
    name: str = field(default="Random", init=False)
    description: str = field(default="Play random card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scrambler(AlienPower):
    """
    Scrambler - Mix It Up.
    Shuffle destiny deck.
    """
    name: str = field(default="Scrambler", init=False)
    description: str = field(default="Shuffle destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Turbulence(AlienPower):
    """
    Turbulence - Unstable Force.
    Card values fluctuate randomly.
    """
    name: str = field(default="Turbulence", init=False)
    description: str = field(default="Random card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Unpredictable(AlienPower):
    """
    Unpredictable - Unknown Action.
    Power effect varies each use.
    """
    name: str = field(default="Unpredictable", init=False)
    description: str = field(default="Variable effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wildcard(AlienPower):
    """
    Wildcard - Any Card.
    Play face-down card as any value.
    """
    name: str = field(default="Wildcard", init=False)
    description: str = field(default="Card as any value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Anarchy())
AlienRegistry.register(Chance())
AlienRegistry.register(Chaos_Alt())
AlienRegistry.register(Confusion())
AlienRegistry.register(Disorder())
AlienRegistry.register(Entropy())
AlienRegistry.register(Fortune())
AlienRegistry.register(Madness())
AlienRegistry.register(Mayhem())
AlienRegistry.register(Misfortune())
AlienRegistry.register(Pandemonium())
AlienRegistry.register(Random())
AlienRegistry.register(Scrambler())
AlienRegistry.register(Turbulence())
AlienRegistry.register(Unpredictable())
AlienRegistry.register(Wildcard())
