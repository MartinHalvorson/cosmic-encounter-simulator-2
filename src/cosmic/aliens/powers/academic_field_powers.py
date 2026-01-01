"""
Academic Field themed alien powers for Cosmic Encounter.
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
class Anthropology(AlienPower):
    """Anthropology - Power of Culture."""
    name: str = field(default="Anthropology", init=False)
    description: str = field(default="+1 per unique player in game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Archaeology(AlienPower):
    """Archaeology - Power of the Past."""
    name: str = field(default="Archaeology", init=False)
    description: str = field(default="Retrieve cards from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Philosophy_Field(AlienPower):
    """Philosophy - Power of Thought."""
    name: str = field(default="Philosophy_Field", init=False)
    description: str = field(default="Consider all options before acting.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sociology_Field(AlienPower):
    """Sociology - Power of Society."""
    name: str = field(default="Sociology_Field", init=False)
    description: str = field(default="+2 when allied.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Psychology_Field(AlienPower):
    """Psychology - Power of Mind."""
    name: str = field(default="Psychology_Field", init=False)
    description: str = field(default="Predict opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Political_Science(AlienPower):
    """Political Science - Power of Governance."""
    name: str = field(default="Political_Science", init=False)
    description: str = field(default="Control alliance decisions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Linguistics_Field(AlienPower):
    """Linguistics - Power of Language."""
    name: str = field(default="Linguistics_Field", init=False)
    description: str = field(default="Communicate secretly with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Art_History(AlienPower):
    """Art History - Power of Aesthetics."""
    name: str = field(default="Art_History", init=False)
    description: str = field(default="+2 with high-value cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Musicology(AlienPower):
    """Musicology - Power of Harmony."""
    name: str = field(default="Musicology", init=False)
    description: str = field(default="+1 per allied player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Theology(AlienPower):
    """Theology - Power of Faith."""
    name: str = field(default="Theology", init=False)
    description: str = field(default="+3 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jurisprudence(AlienPower):
    """Jurisprudence - Power of Law."""
    name: str = field(default="Jurisprudence", init=False)
    description: str = field(default="Enforce encounter rules.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Diplomacy_Field(AlienPower):
    """Diplomacy - Power of Negotiation."""
    name: str = field(default="Diplomacy_Field", init=False)
    description: str = field(default="Negotiate cards gain +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Anthropology())
AlienRegistry.register(Archaeology())
AlienRegistry.register(Philosophy_Field())
AlienRegistry.register(Sociology_Field())
AlienRegistry.register(Psychology_Field())
AlienRegistry.register(Political_Science())
AlienRegistry.register(Linguistics_Field())
AlienRegistry.register(Art_History())
AlienRegistry.register(Musicology())
AlienRegistry.register(Theology())
AlienRegistry.register(Jurisprudence())
AlienRegistry.register(Diplomacy_Field())
