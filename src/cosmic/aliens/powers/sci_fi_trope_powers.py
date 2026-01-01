"""
Sci-Fi Trope themed alien powers for Cosmic Encounter.
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
class Cyborg_SF(AlienPower):
    """Cyborg - Power of Enhancement."""
    name: str = field(default="Cyborg_SF", init=False)
    description: str = field(default="+2 permanent bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clone_SF(AlienPower):
    """Clone - Power of Replication."""
    name: str = field(default="Clone_SF", init=False)
    description: str = field(default="Create copy ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hivemind(AlienPower):
    """Hivemind - Power of Unity."""
    name: str = field(default="Hivemind", init=False)
    description: str = field(default="+1 per ship you control.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Android_SF(AlienPower):
    """Android - Power of Logic."""
    name: str = field(default="Android_SF", init=False)
    description: str = field(default="Calculate exact outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class AI_SF(AlienPower):
    """AI - Power of Optimization."""
    name: str = field(default="AI_SF", init=False)
    description: str = field(default="Always play optimal card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hologram(AlienPower):
    """Hologram - Power of Illusion."""
    name: str = field(default="Hologram", init=False)
    description: str = field(default="Create fake ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class TimeLoop(AlienPower):
    """TimeLoop - Power of Repetition."""
    name: str = field(default="TimeLoop", init=False)
    description: str = field(default="Replay encounter on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Alien_SF(AlienPower):
    """Alien - Power of Otherness."""
    name: str = field(default="Alien_SF", init=False)
    description: str = field(default="Immune to human effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mutant(AlienPower):
    """Mutant - Power of Change."""
    name: str = field(default="Mutant", init=False)
    description: str = field(default="Random power each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Psychic_SF(AlienPower):
    """Psychic - Power of Mind."""
    name: str = field(default="Psychic_SF", init=False)
    description: str = field(default="See opponent's cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Galactic(AlienPower):
    """Galactic - Power of Space."""
    name: str = field(default="Galactic", init=False)
    description: str = field(default="+1 per system you control.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Terraform(AlienPower):
    """Terraform - Power of Shaping."""
    name: str = field(default="Terraform", init=False)
    description: str = field(default="Change planet properties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Cyborg_SF())
AlienRegistry.register(Clone_SF())
AlienRegistry.register(Hivemind())
AlienRegistry.register(Android_SF())
AlienRegistry.register(AI_SF())
AlienRegistry.register(Hologram())
AlienRegistry.register(TimeLoop())
AlienRegistry.register(Alien_SF())
AlienRegistry.register(Mutant())
AlienRegistry.register(Psychic_SF())
AlienRegistry.register(Galactic())
AlienRegistry.register(Terraform())
