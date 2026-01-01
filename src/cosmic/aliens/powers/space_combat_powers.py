"""
Space Combat Powers for Cosmic Encounter.

Aliens inspired by space warfare and combat.
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
class Laser_Cannon(AlienPower):
    """Laser_Cannon - Power of Precision. +4 on offense."""
    name: str = field(default="Laser_Cannon", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Shield_Generator(AlienPower):
    """Shield_Generator - Power of Defense. +4 on defense."""
    name: str = field(default="Shield_Generator", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Ion_Beam(AlienPower):
    """Ion_Beam - Power of Disruption. -2 to opponent's total."""
    name: str = field(default="Ion_Beam", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Plasma_Torpedo(AlienPower):
    """Plasma_Torpedo - Power of Impact. +5 on first encounter."""
    name: str = field(default="Plasma_Torpedo", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Missile_Battery(AlienPower):
    """Missile_Battery - Power of Volleys. +3 always."""
    name: str = field(default="Missile_Battery", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Cloaking_Device(AlienPower):
    """Cloaking_Device - Power of Invisibility. Ships return home, not warp."""
    name: str = field(default="Cloaking_Device", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tractor_Beam(AlienPower):
    """Tractor_Beam - Power of Pulling. +2 per ally ship."""
    name: str = field(default="Tractor_Beam", init=False)
    description: str = field(default="+2 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Point_Defense(AlienPower):
    """Point_Defense - Power of Interception. +3 on defense."""
    name: str = field(default="Point_Defense", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Railgun(AlienPower):
    """Railgun - Power of Kinetics. +5 on offense."""
    name: str = field(default="Railgun", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class EMP(AlienPower):
    """EMP - Power of Shutdown. Opponent cannot use power."""
    name: str = field(default="EMP", init=False)
    description: str = field(default="Block opponent power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dreadnought(AlienPower):
    """Dreadnought - Power of Size. Ships count as 2 each."""
    name: str = field(default="Dreadnought", init=False)
    description: str = field(default="Ships count as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fighter_Squadron(AlienPower):
    """Fighter_Squadron - Power of Swarm. +1 per ship in encounter."""
    name: str = field(default="Fighter_Squadron", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Battlecruiser(AlienPower):
    """Battlecruiser - Power of War. +4 always."""
    name: str = field(default="Battlecruiser", init=False)
    description: str = field(default="+4 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Carrier(AlienPower):
    """Carrier - Power of Transport. May commit up to 6 ships."""
    name: str = field(default="Carrier", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Frigate(AlienPower):
    """Frigate - Power of Speed. Win ties automatically."""
    name: str = field(default="Frigate", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all space combat powers
AlienRegistry.register(Laser_Cannon())
AlienRegistry.register(Shield_Generator())
AlienRegistry.register(Ion_Beam())
AlienRegistry.register(Plasma_Torpedo())
AlienRegistry.register(Missile_Battery())
AlienRegistry.register(Cloaking_Device())
AlienRegistry.register(Tractor_Beam())
AlienRegistry.register(Point_Defense())
AlienRegistry.register(Railgun())
AlienRegistry.register(EMP())
AlienRegistry.register(Dreadnought())
AlienRegistry.register(Fighter_Squadron())
AlienRegistry.register(Battlecruiser())
AlienRegistry.register(Carrier())
AlienRegistry.register(Frigate())
