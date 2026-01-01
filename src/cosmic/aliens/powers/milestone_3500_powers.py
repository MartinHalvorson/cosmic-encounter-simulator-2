"""
Milestone 3500 themed alien powers for Cosmic Encounter.
Special celebration powers for reaching 3500 aliens.
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
class Milestone_Power(AlienPower):
    """Milestone - Power of Achievement."""
    name: str = field(default="Milestone_Power", init=False)
    description: str = field(default="+1 for each colony milestone reached.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Celebration_Power(AlienPower):
    """Celebration - Power of Victory."""
    name: str = field(default="Celebration_Power", init=False)
    description: str = field(default="All allies get +1 when you win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Achievement_Power(AlienPower):
    """Achievement - Power of Goals."""
    name: str = field(default="Achievement_Power", init=False)
    description: str = field(default="+2 for completing hidden objectives.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Landmark_Power(AlienPower):
    """Landmark - Power of Recognition."""
    name: str = field(default="Landmark_Power", init=False)
    description: str = field(default="Mark planets as landmarks for bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Record_Power(AlienPower):
    """Record - Power of History."""
    name: str = field(default="Record_Power", init=False)
    description: str = field(default="Track all encounters for future bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monument_Power(AlienPower):
    """Monument - Power of Memory."""
    name: str = field(default="Monument_Power", init=False)
    description: str = field(default="Build monuments for permanent +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Legacy_Power(AlienPower):
    """Legacy - Power of Continuation."""
    name: str = field(default="Legacy_Power", init=False)
    description: str = field(default="Pass bonuses to allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Triumph_Power(AlienPower):
    """Triumph - Power of Glory."""
    name: str = field(default="Triumph_Power", init=False)
    description: str = field(default="+5 on final colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Progress_Power(AlienPower):
    """Progress - Power of Advancement."""
    name: str = field(default="Progress_Power", init=False)
    description: str = field(default="+1 each turn (cumulative).", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pinnacle_Power(AlienPower):
    """Pinnacle - Power of Peak."""
    name: str = field(default="Pinnacle_Power", init=False)
    description: str = field(default="+6 when at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Milestone_Power())
AlienRegistry.register(Celebration_Power())
AlienRegistry.register(Achievement_Power())
AlienRegistry.register(Landmark_Power())
AlienRegistry.register(Record_Power())
AlienRegistry.register(Monument_Power())
AlienRegistry.register(Legacy_Power())
AlienRegistry.register(Triumph_Power())
AlienRegistry.register(Progress_Power())
AlienRegistry.register(Pinnacle_Power())
