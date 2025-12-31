"""
Shape Powers - Geometric shape-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Circle(AlienPower):
    """Circle - Complete shape. Win ties."""
    name: str = field(default="Circle", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Square(AlienPower):
    """Square - Solid shape. +4 when defending."""
    name: str = field(default="Square", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Triangle(AlienPower):
    """Triangle - Pointed shape. +3 when attacking."""
    name: str = field(default="Triangle", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Pentagon(AlienPower):
    """Pentagon - Five-sided. +1 per ship committed."""
    name: str = field(default="Pentagon", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hexagon(AlienPower):
    """Hexagon - Six-sided. +2 per home colony."""
    name: str = field(default="Hexagon", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + (home_count * 2)
        return total


@dataclass
class Octagon(AlienPower):
    """Octagon - Eight-sided. Launch up to 8 ships."""
    name: str = field(default="Octagon", init=False)
    description: str = field(default="Launch up to 8 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Star_Shape(AlienPower):
    """Star Shape - Pointed form. +5 on first encounter."""
    name: str = field(default="StarShape", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Diamond_Shape(AlienPower):
    """Diamond Shape - Precious form. +1 per card in hand."""
    name: str = field(default="DiamondShape", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Pyramid(AlienPower):
    """Pyramid - Ancient form. +3 defending home."""
    name: str = field(default="Pyramid", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 3
        return total


@dataclass
class Sphere(AlienPower):
    """Sphere - Perfect 3D form. Ships count double."""
    name: str = field(default="Sphere", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cube(AlienPower):
    """Cube - Solid 3D form. Prevent 2 ships from warp."""
    name: str = field(default="Cube", init=False)
    description: str = field(default="Save 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cylinder(AlienPower):
    """Cylinder - Rolling form. Move ships freely."""
    name: str = field(default="Cylinder", init=False)
    description: str = field(default="Freely relocate ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cone(AlienPower):
    """Cone - Pointed 3D form. -2 to opponent's total."""
    name: str = field(default="Cone", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spiral(AlienPower):
    """Spiral - Winding form. Swap encounter cards."""
    name: str = field(default="Spiral", init=False)
    description: str = field(default="Swap cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Arrow(AlienPower):
    """Arrow - Pointing form. Ignore destiny, attack any player."""
    name: str = field(default="Arrow", init=False)
    description: str = field(default="Choose attack target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Circle())
AlienRegistry.register(Square())
AlienRegistry.register(Triangle())
AlienRegistry.register(Pentagon())
AlienRegistry.register(Hexagon())
AlienRegistry.register(Octagon())
AlienRegistry.register(Star_Shape())
AlienRegistry.register(Diamond_Shape())
AlienRegistry.register(Pyramid())
AlienRegistry.register(Sphere())
AlienRegistry.register(Cube())
AlienRegistry.register(Cylinder())
AlienRegistry.register(Cone())
AlienRegistry.register(Spiral())
AlienRegistry.register(Arrow())
