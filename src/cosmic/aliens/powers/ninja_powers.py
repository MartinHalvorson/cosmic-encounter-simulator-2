"""
Ninja Powers for Cosmic Encounter.

Aliens inspired by ninja and stealth combat themes.
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
class Shadow_Ninja(AlienPower):
    """Shadow_Ninja - Power of Shadows. +3 when fewer ships than opponent."""
    name: str = field(default="Shadow_Ninja", init=False)
    description: str = field(default="+3 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            my_ships = sum(game.offense_ships.values()) if side == Side.OFFENSE else sum(game.defense_ships.values())
            opp_ships = sum(game.defense_ships.values()) if side == Side.OFFENSE else sum(game.offense_ships.values())
            if my_ships < opp_ships:
                return total + 3
        return total


@dataclass
class Shuriken(AlienPower):
    """Shuriken - Power of Throwing. Send 1 opponent ship to warp before reveal."""
    name: str = field(default="Shuriken", init=False)
    description: str = field(default="Send 1 opponent ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Smoke_Bomb(AlienPower):
    """Smoke_Bomb - Power of Escape. Retreat from encounter without losing ships."""
    name: str = field(default="Smoke_Bomb", init=False)
    description: str = field(default="Retreat without losing ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Katana(AlienPower):
    """Katana - Power of the Blade. +4 on offense."""
    name: str = field(default="Katana", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Silent_Step(AlienPower):
    """Silent_Step - Power of Silence. Opponent cannot invite allies."""
    name: str = field(default="Silent_Step", init=False)
    description: str = field(default="Opponent cannot invite allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hidden_Blade(AlienPower):
    """Hidden_Blade - Power of Concealment. +2, opponent doesn't know your bonus."""
    name: str = field(default="Hidden_Blade", init=False)
    description: str = field(default="+2 hidden bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Poison_Dart(AlienPower):
    """Poison_Dart - Power of Venom. Winner loses 1 ship after encounter."""
    name: str = field(default="Poison_Dart", init=False)
    description: str = field(default="Winner loses 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wall_Climber(AlienPower):
    """Wall_Climber - Power of Agility. +1 for each planet you occupy."""
    name: str = field(default="Wall_Climber", init=False)
    description: str = field(default="+1 per planet occupied.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            planets = sum(1 for p in game.planets if p.has_colony(player.name))
            return total + planets
        return total


@dataclass
class Nunchaku(AlienPower):
    """Nunchaku - Power of Speed. Win ties automatically."""
    name: str = field(default="Nunchaku", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Disguise(AlienPower):
    """Disguise - Power of Deception. Copy opponent's power for encounter."""
    name: str = field(default="Disguise", init=False)
    description: str = field(default="Copy opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Grappling_Hook(AlienPower):
    """Grappling_Hook - Power of Reach. Attack any planet, not just drawn."""
    name: str = field(default="Grappling_Hook", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ambush(AlienPower):
    """Ambush - Power of Surprise. +5 on first encounter of your turn."""
    name: str = field(default="Ambush", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            # First encounter bonus
            if game.encounter_number == 1:
                return total + 5
        return total


@dataclass
class Vanish(AlienPower):
    """Vanish - Power of Disappearance. Ships return home instead of warp."""
    name: str = field(default="Vanish", init=False)
    description: str = field(default="Ships return home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Acrobat(AlienPower):
    """Acrobat - Power of Dodging. -2 to opponent's total."""
    name: str = field(default="Acrobat", init=False)
    description: str = field(default="-2 to opponent's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Master_Ninja(AlienPower):
    """Master_Ninja - Power of Mastery. +3 and win ties."""
    name: str = field(default="Master_Ninja", init=False)
    description: str = field(default="+3 and win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


# Register all ninja powers
AlienRegistry.register(Shadow_Ninja())
AlienRegistry.register(Shuriken())
AlienRegistry.register(Smoke_Bomb())
AlienRegistry.register(Katana())
AlienRegistry.register(Silent_Step())
AlienRegistry.register(Hidden_Blade())
AlienRegistry.register(Poison_Dart())
AlienRegistry.register(Wall_Climber())
AlienRegistry.register(Nunchaku())
AlienRegistry.register(Disguise())
AlienRegistry.register(Grappling_Hook())
AlienRegistry.register(Ambush())
AlienRegistry.register(Vanish())
AlienRegistry.register(Acrobat())
AlienRegistry.register(Master_Ninja())
