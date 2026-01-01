"""
Texture and Material themed alien powers for Cosmic Encounter.
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
class Smooth(AlienPower):
    """Smooth - Power of Frictionless."""
    name: str = field(default="Smooth", init=False)
    description: str = field(
        default="Ships slide to adjacent colonies when losing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rough(AlienPower):
    """Rough - Power of Friction."""
    name: str = field(default="Rough", init=False)
    description: str = field(
        default="Ships attacking you need +2 to win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Silky(AlienPower):
    """Silky - Power of Elegance."""
    name: str = field(default="Silky", init=False)
    description: str = field(
        default="All deals you make give you 1 extra card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spiky(AlienPower):
    """Spiky - Power of Points."""
    name: str = field(default="Spiky", init=False)
    description: str = field(
        default="When attacked, attacker loses 1 ship before combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fuzzy(AlienPower):
    """Fuzzy - Power of Softness."""
    name: str = field(default="Fuzzy", init=False)
    description: str = field(
        default="Allies joining your side don't lose ships if you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crystalline(AlienPower):
    """Crystalline - Power of Clarity."""
    name: str = field(default="Crystalline", init=False)
    description: str = field(
        default="All hands are revealed during encounters you're in.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Spongy(AlienPower):
    """Spongy - Power of Absorption."""
    name: str = field(default="Spongy", init=False)
    description: str = field(
        default="Absorb reinforcement effects directed at opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Metallic(AlienPower):
    """Metallic - Power of Hardness."""
    name: str = field(default="Metallic", init=False)
    description: str = field(
        default="+2 to combat when defending.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE], init=False
    )


@dataclass
class Gooey(AlienPower):
    """Gooey - Power of Stickiness."""
    name: str = field(default="Gooey", init=False)
    description: str = field(
        default="Ships that attack you can't leave for 1 turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Grainy(AlienPower):
    """Grainy - Power of Particles."""
    name: str = field(default="Grainy", init=False)
    description: str = field(
        default="Split ships among multiple targets when attacking.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Smooth())
AlienRegistry.register(Rough())
AlienRegistry.register(Silky())
AlienRegistry.register(Spiky())
AlienRegistry.register(Fuzzy())
AlienRegistry.register(Crystalline())
AlienRegistry.register(Spongy())
AlienRegistry.register(Metallic())
AlienRegistry.register(Gooey())
AlienRegistry.register(Grainy())
