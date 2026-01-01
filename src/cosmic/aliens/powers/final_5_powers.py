"""
Final 5 aliens to reach the 4000 milestone.
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
class FourThousand(AlienPower):
    """Four Thousand - Power of Completion."""
    name: str = field(default="FourThousand", init=False)
    description: str = field(default="+4 for milestone achievement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Finisher(AlienPower):
    """Finisher - Power of Ending."""
    name: str = field(default="Finisher", init=False)
    description: str = field(default="+5 on winning encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Completer(AlienPower):
    """Completer - Power of Finishing."""
    name: str = field(default="Completer", init=False)
    description: str = field(default="+3 when at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Achiever(AlienPower):
    """Achiever - Power of Goals."""
    name: str = field(default="Achiever", init=False)
    description: str = field(default="+2 for each milestone reached.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Culminator(AlienPower):
    """Culminator - Power of Climax."""
    name: str = field(default="Culminator", init=False)
    description: str = field(default="+6 on final colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(FourThousand())
AlienRegistry.register(Finisher())
AlienRegistry.register(Completer())
AlienRegistry.register(Achiever())
AlienRegistry.register(Culminator())
