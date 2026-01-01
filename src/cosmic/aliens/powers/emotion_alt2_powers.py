"""
Additional Emotion themed alien powers for Cosmic Encounter.
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
class Ecstasy(AlienPower):
    """Ecstasy - Power of Bliss."""
    name: str = field(default="Ecstasy", init=False)
    description: str = field(default="+4 when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Melancholy(AlienPower):
    """Melancholy - Power of Sadness."""
    name: str = field(default="Melancholy", init=False)
    description: str = field(default="+3 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Euphoria(AlienPower):
    """Euphoria - Power of Elation."""
    name: str = field(default="Euphoria", init=False)
    description: str = field(default="+2 per ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dread(AlienPower):
    """Dread - Power of Fear."""
    name: str = field(default="Dread", init=False)
    description: str = field(default="Opponent loses 1 ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Serenity(AlienPower):
    """Serenity - Power of Calm."""
    name: str = field(default="Serenity", init=False)
    description: str = field(default="Prevent all power uses once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Fury(AlienPower):
    """Fury - Power of Wrath."""
    name: str = field(default="Fury", init=False)
    description: str = field(default="+6 but lose 2 ships after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nostalgia(AlienPower):
    """Nostalgia - Power of the Past."""
    name: str = field(default="Nostalgia", init=False)
    description: str = field(default="Replay last encounter outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Longing(AlienPower):
    """Longing - Power of Desire."""
    name: str = field(default="Longing", init=False)
    description: str = field(default="Take one card from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Contempt(AlienPower):
    """Contempt - Power of Disdain."""
    name: str = field(default="Contempt", init=False)
    description: str = field(default="+2 against weaker opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Compassion(AlienPower):
    """Compassion - Power of Mercy."""
    name: str = field(default="Compassion", init=False)
    description: str = field(default="Save opponent's ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Apathy(AlienPower):
    """Apathy - Power of Indifference."""
    name: str = field(default="Apathy", init=False)
    description: str = field(default="Immune to all effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jealousy(AlienPower):
    """Jealousy - Power of Envy."""
    name: str = field(default="Jealousy", init=False)
    description: str = field(default="Copy leader's bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ecstasy())
AlienRegistry.register(Melancholy())
AlienRegistry.register(Euphoria())
AlienRegistry.register(Dread())
AlienRegistry.register(Serenity())
AlienRegistry.register(Fury())
AlienRegistry.register(Nostalgia())
AlienRegistry.register(Longing())
AlienRegistry.register(Contempt())
AlienRegistry.register(Compassion())
AlienRegistry.register(Apathy())
AlienRegistry.register(Jealousy())
