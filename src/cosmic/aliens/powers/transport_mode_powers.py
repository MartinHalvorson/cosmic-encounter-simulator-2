"""
Transport Mode themed alien powers for Cosmic Encounter.
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
class Bicycle(AlienPower):
    """Bicycle - Power of Simplicity."""
    name: str = field(default="Bicycle", init=False)
    description: str = field(default="+2 with low card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Motorcycle(AlienPower):
    """Motorcycle - Power of Speed."""
    name: str = field(default="Motorcycle", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Car_Transport(AlienPower):
    """Car - Power of Mobility."""
    name: str = field(default="Car_Transport", init=False)
    description: str = field(default="Move 2 ships per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bus(AlienPower):
    """Bus - Power of Capacity."""
    name: str = field(default="Bus", init=False)
    description: str = field(default="Send 5 ships instead of 4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Truck(AlienPower):
    """Truck - Power of Hauling."""
    name: str = field(default="Truck", init=False)
    description: str = field(default="Carry extra cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Helicopter(AlienPower):
    """Helicopter - Power of Hover."""
    name: str = field(default="Helicopter", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Airplane(AlienPower):
    """Airplane - Power of Flight."""
    name: str = field(default="Airplane", init=False)
    description: str = field(default="+2 to distant attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boat(AlienPower):
    """Boat - Power of Sailing."""
    name: str = field(default="Boat", init=False)
    description: str = field(default="Move through blocked paths.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Submarine_Trans(AlienPower):
    """Submarine - Power of Stealth."""
    name: str = field(default="Submarine_Trans", init=False)
    description: str = field(default="Ships hidden until combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rocket_Trans(AlienPower):
    """Rocket - Power of Launch."""
    name: str = field(default="Rocket_Trans", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skateboard(AlienPower):
    """Skateboard - Power of Tricks."""
    name: str = field(default="Skateboard", init=False)
    description: str = field(default="Random +0-5 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Teleporter_Trans(AlienPower):
    """Teleporter - Power of Instant Travel."""
    name: str = field(default="Teleporter_Trans", init=False)
    description: str = field(default="Ships appear anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Bicycle())
AlienRegistry.register(Motorcycle())
AlienRegistry.register(Car_Transport())
AlienRegistry.register(Bus())
AlienRegistry.register(Truck())
AlienRegistry.register(Helicopter())
AlienRegistry.register(Airplane())
AlienRegistry.register(Boat())
AlienRegistry.register(Submarine_Trans())
AlienRegistry.register(Rocket_Trans())
AlienRegistry.register(Skateboard())
AlienRegistry.register(Teleporter_Trans())
