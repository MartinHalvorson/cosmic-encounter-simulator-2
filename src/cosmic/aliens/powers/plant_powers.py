"""
Plant Powers - Botanical and flora-themed aliens.
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
class TreeAlien(AlienPower):
    """Tree - Deep roots. +3 when defending home planets."""
    name: str = field(default="Tree", init=False)
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
class Vine(AlienPower):
    """Vine - Spreading growth. Place ship on adjacent colony."""
    name: str = field(default="Vine", init=False)
    description: str = field(default="Spread to adjacent colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flower(AlienPower):
    """Flower - Attractive bloom. Force one ally to join you."""
    name: str = field(default="Flower", init=False)
    description: str = field(default="Compel one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mushroom(AlienPower):
    """Mushroom - Spore spreader. Create colony when losing."""
    name: str = field(default="Mushroom", init=False)
    description: str = field(default="Spread colony when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cactus(AlienPower):
    """Cactus - Thorny defense. -2 to attacker's total."""
    name: str = field(default="Cactus", init=False)
    description: str = field(default="-2 to attacker.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Grass(AlienPower):
    """Grass - Resilient growth. Retrieve 1 ship each turn."""
    name: str = field(default="Grass", init=False)
    description: str = field(default="Retrieve 1 ship each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fern(AlienPower):
    """Fern - Ancient survivor. +2 always."""
    name: str = field(default="Fern", init=False)
    description: str = field(default="+2 to all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Moss(AlienPower):
    """Moss - Slow spreader. +1 per turn."""
    name: str = field(default="Moss", init=False)
    description: str = field(default="+1 per turn in game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bamboo(AlienPower):
    """Bamboo - Rapid growth. Double ships on first encounter."""
    name: str = field(default="Bamboo", init=False)
    description: str = field(default="Ships count double first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thorn(AlienPower):
    """Thorn - Painful touch. Opponent loses ship when attacking."""
    name: str = field(default="Thorn", init=False)
    description: str = field(default="Attackers lose 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pollen(AlienPower):
    """Pollen - Spreading influence. Allies gain +1 each."""
    name: str = field(default="Pollen", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seed(AlienPower):
    """Seed - Potential growth. Draw card when losing."""
    name: str = field(default="Seed", init=False)
    description: str = field(default="Draw card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Root(AlienPower):
    """Root - Underground network. Move ships freely."""
    name: str = field(default="Root", init=False)
    description: str = field(default="Freely relocate ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Leaf(AlienPower):
    """Leaf - Light gatherer. +1 per home colony."""
    name: str = field(default="Leaf", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + home_count
        return total


@dataclass
class Sprout(AlienPower):
    """Sprout - New growth. +3 when behind in colonies."""
    name: str = field(default="Sprout", init=False)
    description: str = field(default="+3 when trailing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(TreeAlien())
AlienRegistry.register(Vine())
AlienRegistry.register(Flower())
AlienRegistry.register(Mushroom())
AlienRegistry.register(Cactus())
AlienRegistry.register(Grass())
AlienRegistry.register(Fern())
AlienRegistry.register(Moss())
AlienRegistry.register(Bamboo())
AlienRegistry.register(Thorn())
AlienRegistry.register(Pollen())
AlienRegistry.register(Seed())
AlienRegistry.register(Root())
AlienRegistry.register(Leaf())
AlienRegistry.register(Sprout())
