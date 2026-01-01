"""
Pattern Powers - Pattern and design themed aliens.
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
class Spiral(AlienPower):
    """Spiral - Power of Rotation. +1 cumulative per encounter."""
    name: str = field(default="Spiral", init=False)
    description: str = field(default="+1 per encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stripe(AlienPower):
    """Stripe - Power of Alternation. +4 on odd turns."""
    name: str = field(default="Stripe", init=False)
    description: str = field(default="+4 on odd turn numbers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Checker(AlienPower):
    """Checker - Power of Grid. +3 with even cards."""
    name: str = field(default="Checker", init=False)
    description: str = field(default="+3 when card is even.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dot(AlienPower):
    """Dot - Power of Points. +1 per ship."""
    name: str = field(default="Dot", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wave_Alt(AlienPower):
    """Wave_Alt - Power of Oscillation. Random +2 to +6."""
    name: str = field(default="Wave_Alt", init=False)
    description: str = field(default="Random +2 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(2, 6)
        return total


@dataclass
class Fractal(AlienPower):
    """Fractal - Power of Recursion. +2 per colony."""
    name: str = field(default="Fractal", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mosaic(AlienPower):
    """Mosaic - Power of Combination. +1 per ally."""
    name: str = field(default="Mosaic", init=False)
    description: str = field(default="+1 per ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Zigzag(AlienPower):
    """Zigzag - Power of Unpredictability. +4 or -2."""
    name: str = field(default="Zigzag", init=False)
    description: str = field(default="+4 or -2 (random).", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (4 if random.random() > 0.5 else -2)
        return total


@dataclass
class Grid(AlienPower):
    """Grid - Power of Structure. +3 on defense."""
    name: str = field(default="Grid", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Radial(AlienPower):
    """Radial - Power of Expansion. +4 on offense."""
    name: str = field(default="Radial", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Symmetry(AlienPower):
    """Symmetry - Power of Balance. Win ties."""
    name: str = field(default="Symmetry", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Asymmetry(AlienPower):
    """Asymmetry - Power of Imbalance. -2 to opponent."""
    name: str = field(default="Asymmetry", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tessellation(AlienPower):
    """Tessellation - Power of Tiling. +2 per home colony."""
    name: str = field(default="Tessellation", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lattice(AlienPower):
    """Lattice - Power of Connection. +3 constant."""
    name: str = field(default="Lattice", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Weave(AlienPower):
    """Weave - Power of Interlock. Cards work together."""
    name: str = field(default="Weave", init=False)
    description: str = field(default="+5 when playing 10-15.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
PATTERN_POWERS = [
    Spiral, Stripe, Checker, Dot, Wave_Alt, Fractal, Mosaic, Zigzag, Grid, Radial,
    Symmetry, Asymmetry, Tessellation, Lattice, Weave,
]

for power_class in PATTERN_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
