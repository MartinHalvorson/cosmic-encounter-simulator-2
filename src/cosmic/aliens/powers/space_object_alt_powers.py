"""
Space Object Alternative themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Asteroid_Belt(AlienPower):
    """Asteroid Belt - Power of Defense."""
    name: str = field(default="Asteroid_Belt", init=False)
    description: str = field(default="+4 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Red_Giant(AlienPower):
    """Red Giant - Power of Size."""
    name: str = field(default="Red_Giant", init=False)
    description: str = field(default="+5 with most ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class White_Dwarf(AlienPower):
    """White Dwarf - Power of Density."""
    name: str = field(default="White_Dwarf", init=False)
    description: str = field(default="+6 with 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Neutron_Star(AlienPower):
    """Neutron Star - Power of Mass."""
    name: str = field(default="Neutron_Star", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Dark_Nebula(AlienPower):
    """Dark Nebula - Power of Concealment."""
    name: str = field(default="Dark_Nebula", init=False)
    description: str = field(default="Ships hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cosmic_Ray(AlienPower):
    """Cosmic Ray - Power of Penetration."""
    name: str = field(default="Cosmic_Ray", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Meteor_Shower(AlienPower):
    """Meteor Shower - Power of Bombardment."""
    name: str = field(default="Meteor_Shower", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Solar_Wind(AlienPower):
    """Solar Wind - Power of Push."""
    name: str = field(default="Solar_Wind", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Magnetar_Alt(AlienPower):
    """Magnetar - Power of Field."""
    name: str = field(default="Magnetar_Alt", init=False)
    description: str = field(default="Force ally join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Quasar_Alt(AlienPower):
    """Quasar - Power of Energy."""
    name: str = field(default="Quasar_Alt", init=False)
    description: str = field(default="+5 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gamma_Burst(AlienPower):
    """Gamma Burst - Power of Destruction."""
    name: str = field(default="Gamma_Burst", init=False)
    description: str = field(default="+6 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Event_Horizon(AlienPower):
    """Event Horizon - Power of Capture."""
    name: str = field(default="Event_Horizon", init=False)
    description: str = field(default="Trap ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
for alien_class in [
    Asteroid_Belt, Red_Giant, White_Dwarf, Neutron_Star, Dark_Nebula,
    Cosmic_Ray, Meteor_Shower, Solar_Wind, Magnetar_Alt, Quasar_Alt,
    Gamma_Burst, Event_Horizon,
]:
    AlienRegistry.register(alien_class())
