"""
Bonus Powers - Additional miscellaneous alien powers.
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
class Amplifier(AlienPower):
    """
    Amplifier - Power Boost.
    Your powers activate twice per encounter.
    """
    name: str = field(default="Amplifier", init=False)
    description: str = field(default="Powers activate twice.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Blocker(AlienPower):
    """
    Blocker - Power Block.
    Once per encounter, cancel an opponent power.
    """
    name: str = field(default="Blocker", init=False)
    description: str = field(default="Cancel opponent power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Climber(AlienPower):
    """
    Climber - Steady Progress.
    Gain +1 permanent bonus for each win.
    """
    name: str = field(default="Climber", init=False)
    description: str = field(default="+1 permanent per win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Equalizer(AlienPower):
    """
    Equalizer - Balance Power.
    Reduce all totals to the lower value.
    """
    name: str = field(default="Equalizer", init=False)
    description: str = field(default="Totals become equal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Finale(AlienPower):
    """
    Finale - Last Stand.
    When at 1 colony, +10 to all totals.
    """
    name: str = field(default="Finale", init=False)
    description: str = field(default="+10 at 1 colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gatherer(AlienPower):
    """
    Gatherer - Resource Collection.
    Draw 1 extra card at start of turn.
    """
    name: str = field(default="Gatherer", init=False)
    description: str = field(default="Draw extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Igniter(AlienPower):
    """
    Igniter - Spark Starter.
    When you attack, +3 to total.
    """
    name: str = field(default="Igniter", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 when attacking."""
        if side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Jumper(AlienPower):
    """
    Jumper - Quick Movement.
    Ships can launch from any colony.
    """
    name: str = field(default="Jumper", init=False)
    description: str = field(default="Launch from any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Amplifier())
AlienRegistry.register(Blocker())
AlienRegistry.register(Climber())
AlienRegistry.register(Equalizer())
AlienRegistry.register(Finale())
AlienRegistry.register(Gatherer())
AlienRegistry.register(Igniter())
AlienRegistry.register(Jumper())
