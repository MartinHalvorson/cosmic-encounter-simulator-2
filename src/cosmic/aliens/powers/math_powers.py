"""
Math Powers - Aliens with numerical and calculation abilities.
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
class Adder(AlienPower):
    """
    Adder - Sum Values.
    +2 to total.
    """
    name: str = field(default="Adder", init=False)
    description: str = field(default="+2 total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 to total."""
        return total + 2


@dataclass
class Calculator(AlienPower):
    """
    Calculator - Compute Odds.
    Know win probability.
    """
    name: str = field(default="Calculator", init=False)
    description: str = field(default="Know odds.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Divider(AlienPower):
    """
    Divider - Split Values.
    Halve opponent total.
    """
    name: str = field(default="Divider", init=False)
    description: str = field(default="Halve opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Equalizer(AlienPower):
    """
    Equalizer - Make Equal.
    Set totals same.
    """
    name: str = field(default="Equalizer", init=False)
    description: str = field(default="Equal totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Exponential(AlienPower):
    """
    Exponential - Grow Fast.
    Double bonus each turn.
    """
    name: str = field(default="Exponential", init=False)
    description: str = field(default="Double bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Factorial(AlienPower):
    """
    Factorial - Massive Growth.
    +1, +2, +3 per turn.
    """
    name: str = field(default="Factorial", init=False)
    description: str = field(default="Growing bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Maximizer(AlienPower):
    """
    Maximizer - Find Maximum.
    Use highest card.
    """
    name: str = field(default="Maximizer", init=False)
    description: str = field(default="Use highest.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Minimizer(AlienPower):
    """
    Minimizer - Find Minimum.
    Opponent uses lowest.
    """
    name: str = field(default="Minimizer", init=False)
    description: str = field(default="Force lowest.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Multiplier_Alt(AlienPower):
    """
    Multiplier_Alt - Increase Values.
    Double ship count.
    """
    name: str = field(default="Multiplier_Alt", init=False)
    description: str = field(default="Double ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Negator(AlienPower):
    """
    Negator - Reverse Sign.
    Flip bonus/penalty.
    """
    name: str = field(default="Negator", init=False)
    description: str = field(default="Flip sign.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Prime(AlienPower):
    """
    Prime - Prime Number.
    +3 on prime totals.
    """
    name: str = field(default="Prime", init=False)
    description: str = field(default="+3 on prime.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Statistician(AlienPower):
    """
    Statistician - Know Averages.
    Predict outcomes.
    """
    name: str = field(default="Statistician", init=False)
    description: str = field(default="Predict outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Subtractor(AlienPower):
    """
    Subtractor - Reduce Values.
    -2 to opponent.
    """
    name: str = field(default="Subtractor", init=False)
    description: str = field(default="-2 opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Adder())
AlienRegistry.register(Calculator())
AlienRegistry.register(Divider())
AlienRegistry.register(Equalizer())
AlienRegistry.register(Exponential())
AlienRegistry.register(Factorial())
AlienRegistry.register(Maximizer())
AlienRegistry.register(Minimizer())
AlienRegistry.register(Multiplier_Alt())
AlienRegistry.register(Negator())
AlienRegistry.register(Prime())
AlienRegistry.register(Statistician())
AlienRegistry.register(Subtractor())
