"""
Light Powers - Aliens with illumination and photon abilities.
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
class Beacon(AlienPower):
    """
    Beacon - Guide Light.
    Allies find way.
    """
    name: str = field(default="Beacon", init=False)
    description: str = field(default="Help allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blinder(AlienPower):
    """
    Blinder - Bright Flash.
    Opponent can't see.
    """
    name: str = field(default="Blinder", init=False)
    description: str = field(default="Blind opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bright(AlienPower):
    """
    Bright - Intense Light.
    +2 constant.
    """
    name: str = field(default="Bright", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 constant."""
        return total + 2


@dataclass
class Glow(AlienPower):
    """
    Glow - Soft Light.
    Reveal cards.
    """
    name: str = field(default="Glow", init=False)
    description: str = field(default="Reveal cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hologram(AlienPower):
    """
    Hologram - Light Image.
    Create phantom ships.
    """
    name: str = field(default="Hologram", init=False)
    description: str = field(default="Phantom ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Laser(AlienPower):
    """
    Laser - Focused Light.
    +4 attack bonus.
    """
    name: str = field(default="Laser", init=False)
    description: str = field(default="+4 attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking."""
        if side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Luminary(AlienPower):
    """
    Luminary - Shining Star.
    All see your power.
    """
    name: str = field(default="Luminary", init=False)
    description: str = field(default="Show power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Photon(AlienPower):
    """
    Photon - Light Particle.
    Move at light speed.
    """
    name: str = field(default="Photon", init=False)
    description: str = field(default="Fast move.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Prism(AlienPower):
    """
    Prism - Split Light.
    Multiple effects.
    """
    name: str = field(default="Prism", init=False)
    description: str = field(default="Multiple effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Radiant(AlienPower):
    """
    Radiant - Emit Light.
    +1 per ally.
    """
    name: str = field(default="Radiant", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reflector_Alt(AlienPower):
    """
    Reflector_Alt - Bounce Light.
    Return attack.
    """
    name: str = field(default="Reflector_Alt", init=False)
    description: str = field(default="Return attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shimmer(AlienPower):
    """
    Shimmer - Light Dance.
    Confuse opponent.
    """
    name: str = field(default="Shimmer", init=False)
    description: str = field(default="Confuse.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sparkle(AlienPower):
    """
    Sparkle - Tiny Lights.
    Distract opponent.
    """
    name: str = field(default="Sparkle", init=False)
    description: str = field(default="Distract.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spotlight(AlienPower):
    """
    Spotlight - Focus Light.
    Target one player.
    """
    name: str = field(default="Spotlight", init=False)
    description: str = field(default="Target one.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Beacon())
AlienRegistry.register(Blinder())
AlienRegistry.register(Bright())
AlienRegistry.register(Glow())
AlienRegistry.register(Hologram())
AlienRegistry.register(Laser())
AlienRegistry.register(Luminary())
AlienRegistry.register(Photon())
AlienRegistry.register(Prism())
AlienRegistry.register(Radiant())
AlienRegistry.register(Reflector_Alt())
AlienRegistry.register(Shimmer())
AlienRegistry.register(Sparkle())
AlienRegistry.register(Spotlight())
