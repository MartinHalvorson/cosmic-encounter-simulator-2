"""
Language and Linguistics themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Translator(AlienPower):
    """Translator - Power of Understanding."""
    name: str = field(default="Translator", init=False)
    description: str = field(
        default="See opponent's intended card type before playing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Linguist(AlienPower):
    """Linguist - Power of Words."""
    name: str = field(default="Linguist", init=False)
    description: str = field(
        default="+1 for each different alien power in the game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Poet(AlienPower):
    """Poet - Power of Verse."""
    name: str = field(default="Poet", init=False)
    description: str = field(
        default="Win negotiations by default.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Orator(AlienPower):
    """Orator - Power of Speech."""
    name: str = field(default="Orator", init=False)
    description: str = field(
        default="Invite 2 extra allies each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scribe(AlienPower):
    """Scribe - Power of Records."""
    name: str = field(default="Scribe", init=False)
    description: str = field(
        default="Draw 1 card at the start of each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stutterer(AlienPower):
    """Stutterer - Power of Delay."""
    name: str = field(default="Stutterer", init=False)
    description: str = field(
        default="Opponent reveals card before you choose yours.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Whisperer(AlienPower):
    """Whisperer - Power of Secrets."""
    name: str = field(default="Whisperer", init=False)
    description: str = field(
        default="Look at any player's hand once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shouter(AlienPower):
    """Shouter - Power of Volume."""
    name: str = field(default="Shouter", init=False)
    description: str = field(
        default="+3 when you have more allies than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Narrator(AlienPower):
    """Narrator - Power of Story."""
    name: str = field(default="Narrator", init=False)
    description: str = field(
        default="Predict encounter outcome; if correct, draw 2 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Liar_Language(AlienPower):
    """Liar - Power of Falsehood."""
    name: str = field(default="Liar_Language", init=False)
    description: str = field(
        default="Announce false card value; if believed, use it.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Interpreter(AlienPower):
    """Interpreter - Power of Meaning."""
    name: str = field(default="Interpreter", init=False)
    description: str = field(
        default="Change negotiate to attack or vice versa.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Etymologist(AlienPower):
    """Etymologist - Power of Origins."""
    name: str = field(default="Etymologist", init=False)
    description: str = field(
        default="+2 for each home colony you still control.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Translator())
AlienRegistry.register(Linguist())
AlienRegistry.register(Poet())
AlienRegistry.register(Orator())
AlienRegistry.register(Scribe())
AlienRegistry.register(Stutterer())
AlienRegistry.register(Whisperer())
AlienRegistry.register(Shouter())
AlienRegistry.register(Narrator())
AlienRegistry.register(Liar_Language())
AlienRegistry.register(Interpreter())
AlienRegistry.register(Etymologist())
