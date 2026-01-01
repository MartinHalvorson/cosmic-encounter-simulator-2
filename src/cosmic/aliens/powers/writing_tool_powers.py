"""
Writing Tool themed alien powers for Cosmic Encounter.
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
class Quill(AlienPower):
    """Quill - Power of Signing."""
    name: str = field(default="Quill", init=False)
    description: str = field(default="Sign deals that can't be broken.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ink(AlienPower):
    """Ink - Power of Permanence."""
    name: str = field(default="Ink", init=False)
    description: str = field(default="Mark cards as unusable by others.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scroll(AlienPower):
    """Scroll - Power of Records."""
    name: str = field(default="Scroll", init=False)
    description: str = field(default="Know all cards played this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Typewriter(AlienPower):
    """Typewriter - Power of Precision."""
    name: str = field(default="Typewriter", init=False)
    description: str = field(default="Card values cannot be modified.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chalk(AlienPower):
    """Chalk - Power of Temporary."""
    name: str = field(default="Chalk", init=False)
    description: str = field(default="Create temporary +3 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Marker(AlienPower):
    """Marker - Power of Highlighting."""
    name: str = field(default="Marker", init=False)
    description: str = field(default="Mark one player for +2 against them.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crayon(AlienPower):
    """Crayon - Power of Color."""
    name: str = field(default="Crayon", init=False)
    description: str = field(default="Change card type once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stylus(AlienPower):
    """Stylus - Power of Touch."""
    name: str = field(default="Stylus", init=False)
    description: str = field(default="Modify one card value by +/-2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brush(AlienPower):
    """Brush - Power of Strokes."""
    name: str = field(default="Brush", init=False)
    description: str = field(default="Paint ships into different colors.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tablet(AlienPower):
    """Tablet - Power of Display."""
    name: str = field(default="Tablet", init=False)
    description: str = field(default="Show top 3 deck cards to all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Quill())
AlienRegistry.register(Ink())
AlienRegistry.register(Scroll())
AlienRegistry.register(Typewriter())
AlienRegistry.register(Chalk())
AlienRegistry.register(Marker())
AlienRegistry.register(Crayon())
AlienRegistry.register(Stylus())
AlienRegistry.register(Brush())
AlienRegistry.register(Tablet())
