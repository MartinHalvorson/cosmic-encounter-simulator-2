"""
Memory Powers - Aliens with recollection and knowledge abilities.
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
class Amnesiac(AlienPower):
    """
    Amnesiac - Forget Past.
    Reset encounter.
    """
    name: str = field(default="Amnesiac", init=False)
    description: str = field(default="Reset encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Archivist(AlienPower):
    """
    Archivist - Store Knowledge.
    Keep cards used.
    """
    name: str = field(default="Archivist", init=False)
    description: str = field(default="Keep used cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Deja(AlienPower):
    """
    Deja - Repeat Past.
    Replay last card.
    """
    name: str = field(default="Deja", init=False)
    description: str = field(default="Replay card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Eraser(AlienPower):
    """
    Eraser - Remove Memory.
    Cancel recent action.
    """
    name: str = field(default="Eraser", init=False)
    description: str = field(default="Cancel action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flashback(AlienPower):
    """
    Flashback - Return to Past.
    Undo last phase.
    """
    name: str = field(default="Flashback", init=False)
    description: str = field(default="Undo phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Historian_Alt(AlienPower):
    """
    Historian_Alt - Record Events.
    +1 per past encounter.
    """
    name: str = field(default="Historian_Alt", init=False)
    description: str = field(default="+1 per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Memorizer(AlienPower):
    """
    Memorizer - Perfect Memory.
    Know all hands.
    """
    name: str = field(default="Memorizer", init=False)
    description: str = field(default="Know all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nostalgic(AlienPower):
    """
    Nostalgic - Love Past.
    Retrieve discards.
    """
    name: str = field(default="Nostalgic", init=False)
    description: str = field(default="Retrieve discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Recall(AlienPower):
    """
    Recall - Remember.
    Use discarded card.
    """
    name: str = field(default="Recall", init=False)
    description: str = field(default="Use discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Recorder(AlienPower):
    """
    Recorder - Track All.
    See all past moves.
    """
    name: str = field(default="Recorder", init=False)
    description: str = field(default="See history.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reminiscer(AlienPower):
    """
    Reminiscer - Think Back.
    Bonus from past wins.
    """
    name: str = field(default="Reminiscer", init=False)
    description: str = field(default="Past win bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scribe(AlienPower):
    """
    Scribe - Write Down.
    +2 per recorded event.
    """
    name: str = field(default="Scribe", init=False)
    description: str = field(default="+2 per event.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Amnesiac())
AlienRegistry.register(Archivist())
AlienRegistry.register(Deja())
AlienRegistry.register(Eraser())
AlienRegistry.register(Flashback())
AlienRegistry.register(Historian_Alt())
AlienRegistry.register(Memorizer())
AlienRegistry.register(Nostalgic())
AlienRegistry.register(Recall())
AlienRegistry.register(Recorder())
AlienRegistry.register(Reminiscer())
AlienRegistry.register(Scribe())
