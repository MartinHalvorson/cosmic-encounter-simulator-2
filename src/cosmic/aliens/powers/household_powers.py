"""
Household items themed alien powers for Cosmic Encounter.
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
class Broom(AlienPower):
    """Broom - Power of Sweeping."""
    name: str = field(default="Broom", init=False)
    description: str = field(default="Clear all ships from one planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mop(AlienPower):
    """Mop - Power of Cleaning."""
    name: str = field(default="Mop", init=False)
    description: str = field(default="Remove one card type from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vacuum(AlienPower):
    """Vacuum - Power of Suction."""
    name: str = field(default="Vacuum", init=False)
    description: str = field(default="Take cards from opponent's discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lamp(AlienPower):
    """Lamp - Power of Illumination."""
    name: str = field(default="Lamp", init=False)
    description: str = field(default="Reveal opponent's hand once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Clock_Household(AlienPower):
    """Clock - Power of Timing."""
    name: str = field(default="Clock_Household", init=False)
    description: str = field(default="End encounter immediately.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mirror_Household(AlienPower):
    """Mirror - Power of Reflection."""
    name: str = field(default="Mirror_Household", init=False)
    description: str = field(default="Copy opponent's attack card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pillow(AlienPower):
    """Pillow - Power of Comfort."""
    name: str = field(default="Pillow", init=False)
    description: str = field(default="Ships survive one extra loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blanket(AlienPower):
    """Blanket - Power of Coverage."""
    name: str = field(default="Blanket", init=False)
    description: str = field(default="Protect all ships on one planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Candle(AlienPower):
    """Candle - Power of Light."""
    name: str = field(default="Candle", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Vase(AlienPower):
    """Vase - Power of Fragility."""
    name: str = field(default="Vase", init=False)
    description: str = field(default="+5 but lose power if you lose encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Broom())
AlienRegistry.register(Mop())
AlienRegistry.register(Vacuum())
AlienRegistry.register(Lamp())
AlienRegistry.register(Clock_Household())
AlienRegistry.register(Mirror_Household())
AlienRegistry.register(Pillow())
AlienRegistry.register(Blanket())
AlienRegistry.register(Candle())
AlienRegistry.register(Vase())
