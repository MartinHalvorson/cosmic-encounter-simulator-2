"""
Fantasy Race themed alien powers for Cosmic Encounter.
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
class Elf_Fantasy(AlienPower):
    """Elf - Power of Precision."""
    name: str = field(default="Elf_Fantasy", init=False)
    description: str = field(default="+2 when playing attack cards under 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dwarf_Fantasy(AlienPower):
    """Dwarf - Power of Endurance."""
    name: str = field(default="Dwarf_Fantasy", init=False)
    description: str = field(default="+3 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Orc_Fantasy(AlienPower):
    """Orc - Power of Aggression."""
    name: str = field(default="Orc_Fantasy", init=False)
    description: str = field(default="+4 when attacking with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Troll_Fantasy(AlienPower):
    """Troll - Power of Regeneration."""
    name: str = field(default="Troll_Fantasy", init=False)
    description: str = field(default="Retrieve 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goblin_Fantasy(AlienPower):
    """Goblin - Power of Swarming."""
    name: str = field(default="Goblin_Fantasy", init=False)
    description: str = field(default="+1 for each of your ships in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fairy(AlienPower):
    """Fairy - Power of Mischief."""
    name: str = field(default="Fairy", init=False)
    description: str = field(default="Swap one ally between sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gnome(AlienPower):
    """Gnome - Power of Tinkering."""
    name: str = field(default="Gnome", init=False)
    description: str = field(default="Modify artifact effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ogre(AlienPower):
    """Ogre - Power of Brute Force."""
    name: str = field(default="Ogre", init=False)
    description: str = field(default="+6 but can only send 2 ships max.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sprite(AlienPower):
    """Sprite - Power of Speed."""
    name: str = field(default="Sprite", init=False)
    description: str = field(default="Take two encounters per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Halfling(AlienPower):
    """Halfling - Power of Luck."""
    name: str = field(default="Halfling", init=False)
    description: str = field(default="Reroll destiny once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Centaur(AlienPower):
    """Centaur - Power of Cavalry."""
    name: str = field(default="Centaur", init=False)
    description: str = field(default="Ships count double when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Minotaur(AlienPower):
    """Minotaur - Power of the Maze."""
    name: str = field(default="Minotaur", init=False)
    description: str = field(default="Opponent must discard to attack you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Elf_Fantasy())
AlienRegistry.register(Dwarf_Fantasy())
AlienRegistry.register(Orc_Fantasy())
AlienRegistry.register(Troll_Fantasy())
AlienRegistry.register(Goblin_Fantasy())
AlienRegistry.register(Fairy())
AlienRegistry.register(Gnome())
AlienRegistry.register(Ogre())
AlienRegistry.register(Sprite())
AlienRegistry.register(Halfling())
AlienRegistry.register(Centaur())
AlienRegistry.register(Minotaur())
