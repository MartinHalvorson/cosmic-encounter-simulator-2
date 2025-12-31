"""
Beast Powers - Animal and creature-themed aliens.
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
class Wolf(AlienPower):
    """Wolf - Pack hunter. +1 for each ally ship."""
    name: str = field(default="Wolf", init=False)
    description: str = field(default="+1 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bear(AlienPower):
    """Bear - Powerful defender. +4 when defending."""
    name: str = field(default="Bear", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Eagle(AlienPower):
    """Eagle - Swift attacker. +3 when attacking."""
    name: str = field(default="Eagle", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Lion(AlienPower):
    """Lion - King of beasts. Win ties."""
    name: str = field(default="Lion", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Serpent(AlienPower):
    """Serpent - Venomous strike. Opponent loses extra ship on loss."""
    name: str = field(default="Serpent", init=False)
    description: str = field(default="Opponent loses extra ship when you win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spider(AlienPower):
    """Spider - Web spinner. Trap opponent's allies."""
    name: str = field(default="Spider", init=False)
    description: str = field(default="Opponent allies lose 1 ship each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shark(AlienPower):
    """Shark - Blood frenzy. +2 for each ship opponent lost this turn."""
    name: str = field(default="Shark", init=False)
    description: str = field(default="+2 per ship opponent lost this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hawk(AlienPower):
    """Hawk - Keen sight. See opponent's encounter card."""
    name: str = field(default="Hawk", init=False)
    description: str = field(default="See opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Raven(AlienPower):
    """Raven - Collector. Take opponent's discarded encounter card."""
    name: str = field(default="Raven", init=False)
    description: str = field(default="Take opponent's discarded card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crow(AlienPower):
    """Crow - Scavenger. Draw card when ships go to warp."""
    name: str = field(default="Crow", init=False)
    description: str = field(default="Draw card when any ships warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fox(AlienPower):
    """Fox - Cunning. Switch encounter cards after selection."""
    name: str = field(default="Fox", init=False)
    description: str = field(default="Switch cards after selection.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Owl(AlienPower):
    """Owl - Wise observer. Know destiny before it's drawn."""
    name: str = field(default="Owl", init=False)
    description: str = field(default="See next destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Turtle(AlienPower):
    """Turtle - Protective shell. Prevent 2 ships from going to warp."""
    name: str = field(default="Turtle", init=False)
    description: str = field(default="Save 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rhino(AlienPower):
    """Rhino - Charging beast. +5 on first encounter of turn."""
    name: str = field(default="Rhino", init=False)
    description: str = field(default="+5 on first encounter each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Scorpion(AlienPower):
    """Scorpion - Deadly sting. When losing, opponent loses same ships."""
    name: str = field(default="Scorpion", init=False)
    description: str = field(default="Opponent mirrors your ship losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Wolf())
AlienRegistry.register(Bear())
AlienRegistry.register(Eagle())
AlienRegistry.register(Lion())
AlienRegistry.register(Serpent())
AlienRegistry.register(Spider())
AlienRegistry.register(Shark())
AlienRegistry.register(Hawk())
AlienRegistry.register(Raven())
AlienRegistry.register(Crow())
AlienRegistry.register(Fox())
AlienRegistry.register(Owl())
AlienRegistry.register(Turtle())
AlienRegistry.register(Rhino())
AlienRegistry.register(Scorpion())
