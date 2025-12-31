"""
Quantum Powers - Aliens with quantum physics and superposition abilities.
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
class Collapser(AlienPower):
    """
    Collapser - Wave Collapse.
    Force random outcome.
    """
    name: str = field(default="Collapser", init=False)
    description: str = field(default="Force random result.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Entangler_Alt(AlienPower):
    """
    Entangler_Alt - Quantum Link.
    Mirror opponent result.
    """
    name: str = field(default="Entangler_Alt", init=False)
    description: str = field(default="Mirror result.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Observer(AlienPower):
    """
    Observer - Quantum Observer.
    Viewing changes outcome.
    """
    name: str = field(default="Observer", init=False)
    description: str = field(default="See and change.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Particle(AlienPower):
    """
    Particle - Subatomic.
    Exist in multiple places.
    """
    name: str = field(default="Particle", init=False)
    description: str = field(default="Multiple locations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Probabilist(AlienPower):
    """
    Probabilist - Quantum Probability.
    +3 or -3 randomly.
    """
    name: str = field(default="Probabilist", init=False)
    description: str = field(default="+3 or -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 or -3 randomly."""
        return total + random.choice([3, -3])


@dataclass
class Quanta(AlienPower):
    """
    Quanta - Energy Packets.
    +1 per discrete step.
    """
    name: str = field(default="Quanta", init=False)
    description: str = field(default="+1 per step.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quantum(AlienPower):
    """
    Quantum - Superposition.
    Exist in both states.
    """
    name: str = field(default="Quantum", init=False)
    description: str = field(default="Both states.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Schrodinger(AlienPower):
    """
    Schrodinger - Uncertain State.
    Win and lose simultaneously.
    """
    name: str = field(default="Schrodinger", init=False)
    description: str = field(default="Win and lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Splitter(AlienPower):
    """
    Splitter - Split Reality.
    Create alternate outcome.
    """
    name: str = field(default="Splitter", init=False)
    description: str = field(default="Alternate outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Superposition(AlienPower):
    """
    Superposition - Multiple States.
    All possibilities active.
    """
    name: str = field(default="Superposition", init=False)
    description: str = field(default="All active.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Teleporter(AlienPower):
    """
    Teleporter - Quantum Jump.
    Move instantly.
    """
    name: str = field(default="Teleporter", init=False)
    description: str = field(default="Instant move.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tunneler(AlienPower):
    """
    Tunneler - Quantum Tunnel.
    Bypass defenses.
    """
    name: str = field(default="Tunneler", init=False)
    description: str = field(default="Bypass defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Uncertain(AlienPower):
    """
    Uncertain - Heisenberg.
    Position or momentum known.
    """
    name: str = field(default="Uncertain", init=False)
    description: str = field(default="One known.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wave(AlienPower):
    """
    Wave - Wave Function.
    Spread influence.
    """
    name: str = field(default="Wave", init=False)
    description: str = field(default="Spread effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Collapser())
AlienRegistry.register(Entangler_Alt())
AlienRegistry.register(Observer())
AlienRegistry.register(Particle())
AlienRegistry.register(Probabilist())
AlienRegistry.register(Quanta())
AlienRegistry.register(Quantum())
AlienRegistry.register(Schrodinger())
AlienRegistry.register(Splitter())
AlienRegistry.register(Superposition())
AlienRegistry.register(Teleporter())
AlienRegistry.register(Tunneler())
AlienRegistry.register(Uncertain())
AlienRegistry.register(Wave())
