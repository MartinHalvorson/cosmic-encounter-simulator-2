"""
Eyewear Type Powers for Cosmic Encounter.
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
class Monocle_Eyewear(AlienPower):
    """Monocle_Eyewear - Power of Classic. +5 always."""
    name: str = field(default="Monocle_Eyewear", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Spectacles_Eyewear(AlienPower):
    """Spectacles_Eyewear - Power of Clear. +4 always."""
    name: str = field(default="Spectacles_Eyewear", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Sunglasses_Eyewear(AlienPower):
    """Sunglasses_Eyewear - Power of Shade. +5 always."""
    name: str = field(default="Sunglasses_Eyewear", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Goggles_Eyewear(AlienPower):
    """Goggles_Eyewear - Power of Protect. +5 on defense."""
    name: str = field(default="Goggles_Eyewear", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class VR_Headset_Eyewear(AlienPower):
    """VR_Headset_Eyewear - Power of Virtual. +6 always."""
    name: str = field(default="VR_Headset_Eyewear", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Night_Vision_Eyewear(AlienPower):
    """Night_Vision_Eyewear - Power of Dark. +5 always."""
    name: str = field(default="Night_Vision_Eyewear", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Aviator_Eyewear(AlienPower):
    """Aviator_Eyewear - Power of Flight. +5 on offense."""
    name: str = field(default="Aviator_Eyewear", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Lorgnette_Eyewear(AlienPower):
    """Lorgnette_Eyewear - Power of Elegant. +5 always."""
    name: str = field(default="Lorgnette_Eyewear", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Pince_Nez_Eyewear(AlienPower):
    """Pince_Nez_Eyewear - Power of Pinch. +4 always."""
    name: str = field(default="Pince_Nez_Eyewear", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Telescope_Eyewear(AlienPower):
    """Telescope_Eyewear - Power of Distant. +6 always."""
    name: str = field(default="Telescope_Eyewear", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Binocular_Eyewear(AlienPower):
    """Binocular_Eyewear - Power of Scout. +5 on offense."""
    name: str = field(default="Binocular_Eyewear", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Reading_Glasses_Eyewear(AlienPower):
    """Reading_Glasses_Eyewear - Power of Study. +4 always."""
    name: str = field(default="Reading_Glasses_Eyewear", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Safety_Glasses_Eyewear(AlienPower):
    """Safety_Glasses_Eyewear - Power of Shield. +5 on defense."""
    name: str = field(default="Safety_Glasses_Eyewear", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Contact_Lens_Eyewear(AlienPower):
    """Contact_Lens_Eyewear - Power of Invisible. +5 always."""
    name: str = field(default="Contact_Lens_Eyewear", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


EYEWEAR_TYPE_POWERS = [
    Monocle_Eyewear, Spectacles_Eyewear, Sunglasses_Eyewear, Goggles_Eyewear, VR_Headset_Eyewear,
    Night_Vision_Eyewear, Aviator_Eyewear, Lorgnette_Eyewear, Pince_Nez_Eyewear, Telescope_Eyewear,
    Binocular_Eyewear, Reading_Glasses_Eyewear, Safety_Glasses_Eyewear, Contact_Lens_Eyewear,
]

for power_class in EYEWEAR_TYPE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
