"""
Extended Music themed alien powers for Cosmic Encounter.
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
class Piano(AlienPower):
    """Piano - Power of Keys."""
    name: str = field(default="Piano", init=False)
    description: str = field(default="Play two cards, use higher value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Guitar(AlienPower):
    """Guitar - Power of Strings."""
    name: str = field(default="Guitar", init=False)
    description: str = field(default="+2 for each card in hand over 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drums(AlienPower):
    """Drums - Power of Rhythm."""
    name: str = field(default="Drums", init=False)
    description: str = field(default="+3 on every other encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Violin(AlienPower):
    """Violin - Power of Precision."""
    name: str = field(default="Violin", init=False)
    description: str = field(default="Adjust your total by exactly +/- 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trumpet(AlienPower):
    """Trumpet - Power of Fanfare."""
    name: str = field(default="Trumpet", init=False)
    description: str = field(default="Announce card value; if opponent believed, +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flute(AlienPower):
    """Flute - Power of Charm."""
    name: str = field(default="Flute", init=False)
    description: str = field(default="Lure one enemy ally to your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harp(AlienPower):
    """Harp - Power of Serenity."""
    name: str = field(default="Harp", init=False)
    description: str = field(default="Prevent combat once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Bass(AlienPower):
    """Bass - Power of Depth."""
    name: str = field(default="Bass", init=False)
    description: str = field(default="+1 for each ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saxophone(AlienPower):
    """Saxophone - Power of Jazz."""
    name: str = field(default="Saxophone", init=False)
    description: str = field(default="Random card from opponent's hand instead of your own.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Cello(AlienPower):
    """Cello - Power of Resonance."""
    name: str = field(default="Cello", init=False)
    description: str = field(default="Copy ally's bonus to yourself.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Opera(AlienPower):
    """Opera - Power of Drama."""
    name: str = field(default="Opera", init=False)
    description: str = field(default="+5 when you have exactly 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Symphony(AlienPower):
    """Symphony - Power of Unity."""
    name: str = field(default="Symphony", init=False)
    description: str = field(default="+1 for each different player in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Piano())
AlienRegistry.register(Guitar())
AlienRegistry.register(Drums())
AlienRegistry.register(Violin())
AlienRegistry.register(Trumpet())
AlienRegistry.register(Flute())
AlienRegistry.register(Harp())
AlienRegistry.register(Bass())
AlienRegistry.register(Saxophone())
AlienRegistry.register(Cello())
AlienRegistry.register(Opera())
AlienRegistry.register(Symphony())
