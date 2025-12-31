"""
Sport Powers - Athletic and competition-themed aliens.
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
class Wrestler(AlienPower):
    """Wrestler - Grappler. Win ties."""
    name: str = field(default="Wrestler", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boxer(AlienPower):
    """Boxer - Heavy hitter. +4 when attacking."""
    name: str = field(default="Boxer", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Sprinter(AlienPower):
    """Sprinter - Fast runner. +3 on first encounter."""
    name: str = field(default="Sprinter", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Goalie(AlienPower):
    """Goalie - Goal keeper. +4 when defending."""
    name: str = field(default="Goalie", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Marathoner(AlienPower):
    """Marathoner - Endurance runner. +1 per turn in game."""
    name: str = field(default="Marathoner", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swimmer(AlienPower):
    """Swimmer - Aquatic athlete. Ships escape to colonies."""
    name: str = field(default="Swimmer", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Archer(AlienPower):
    """Archer - Precise aim. See opponent's card."""
    name: str = field(default="Archer", init=False)
    description: str = field(default="View opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fencer(AlienPower):
    """Fencer - Blade master. Swap encounter cards."""
    name: str = field(default="Fencer", init=False)
    description: str = field(default="Swap cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gymnast(AlienPower):
    """Gymnast - Agile athlete. Switch sides after reveal."""
    name: str = field(default="Gymnast", init=False)
    description: str = field(default="Change sides after cards revealed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Weightlifter(AlienPower):
    """Weightlifter - Strong athlete. Ships count double."""
    name: str = field(default="Weightlifter", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coach(AlienPower):
    """Coach - Team leader. Allies gain +2."""
    name: str = field(default="Coach", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Referee(AlienPower):
    """Referee - Rule enforcer. Cancel one artifact per turn."""
    name: str = field(default="Referee", init=False)
    description: str = field(default="Cancel one artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Captain_Alt(AlienPower):
    """Captain Alt - Team captain. Force one ally to join."""
    name: str = field(default="Captain_Alt", init=False)
    description: str = field(default="Compel one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Champion_Alt(AlienPower):
    """Champion Alt - Winner. +3 when leading in colonies."""
    name: str = field(default="Champion_Alt2", init=False)
    description: str = field(default="+3 when leading.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rookie(AlienPower):
    """Rookie - Newcomer. +4 when behind in colonies."""
    name: str = field(default="Rookie", init=False)
    description: str = field(default="+4 when trailing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Wrestler())
AlienRegistry.register(Boxer())
AlienRegistry.register(Sprinter())
AlienRegistry.register(Goalie())
AlienRegistry.register(Marathoner())
AlienRegistry.register(Swimmer())
AlienRegistry.register(Archer())
AlienRegistry.register(Fencer())
AlienRegistry.register(Gymnast())
AlienRegistry.register(Weightlifter())
AlienRegistry.register(Coach())
AlienRegistry.register(Referee())
AlienRegistry.register(Captain_Alt())
AlienRegistry.register(Champion_Alt())
AlienRegistry.register(Rookie())
