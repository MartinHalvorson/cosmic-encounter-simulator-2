"""
Artifact Powers - Aliens with item and object abilities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Armorer(AlienPower):
    """
    Armorer - Craft Weapons.
    +2 from equipment.
    """
    name: str = field(default="Armorer", init=False)
    description: str = field(default="+2 equipment.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Collector_Alt(AlienPower):
    """
    Collector_Alt - Gather Items.
    Draw extra artifacts.
    """
    name: str = field(default="Collector_Alt", init=False)
    description: str = field(default="Extra artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crafter(AlienPower):
    """
    Crafter - Make Items.
    Create artifact cards.
    """
    name: str = field(default="Crafter", init=False)
    description: str = field(default="Create artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Enchanter(AlienPower):
    """
    Enchanter - Imbue Power.
    Boost artifact effects.
    """
    name: str = field(default="Enchanter", init=False)
    description: str = field(default="Boost artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Finder(AlienPower):
    """
    Finder - Locate Items.
    Search deck for artifact.
    """
    name: str = field(default="Finder", init=False)
    description: str = field(default="Search artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jeweler(AlienPower):
    """
    Jeweler - Precious Items.
    Artifacts worth more.
    """
    name: str = field(default="Jeweler", init=False)
    description: str = field(default="Better artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Keeper_Alt(AlienPower):
    """
    Keeper_Alt - Hold Items.
    Artifacts can't be stolen.
    """
    name: str = field(default="Keeper_Alt", init=False)
    description: str = field(default="Protect artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Looter(AlienPower):
    """
    Looter - Take Items.
    Steal artifact on win.
    """
    name: str = field(default="Looter", init=False)
    description: str = field(default="Steal artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Salvager(AlienPower):
    """
    Salvager - Reclaim Items.
    Retrieve discarded artifacts.
    """
    name: str = field(default="Salvager", init=False)
    description: str = field(default="Reclaim discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smith(AlienPower):
    """
    Smith - Forge Weapons.
    +3 with equipment.
    """
    name: str = field(default="Smith", init=False)
    description: str = field(default="+3 equipped.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 with equipment."""
        return total + 3


@dataclass
class Supplier(AlienPower):
    """
    Supplier - Provide Items.
    Give artifacts to allies.
    """
    name: str = field(default="Supplier", init=False)
    description: str = field(default="Give to allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wielder(AlienPower):
    """
    Wielder - Use Items.
    Double artifact effect.
    """
    name: str = field(default="Wielder", init=False)
    description: str = field(default="Double effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Curator(AlienPower):
    """
    Curator - Manage Collection.
    +1 per artifact held.
    """
    name: str = field(default="Curator", init=False)
    description: str = field(default="+1 per artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tinker(AlienPower):
    """
    Tinker - Modify Items.
    Change artifact effect.
    """
    name: str = field(default="Tinker", init=False)
    description: str = field(default="Modify effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Armorer())
AlienRegistry.register(Collector_Alt())
AlienRegistry.register(Crafter())
AlienRegistry.register(Enchanter())
AlienRegistry.register(Finder())
AlienRegistry.register(Jeweler())
AlienRegistry.register(Keeper_Alt())
AlienRegistry.register(Looter())
AlienRegistry.register(Salvager())
AlienRegistry.register(Smith())
AlienRegistry.register(Supplier())
AlienRegistry.register(Wielder())
AlienRegistry.register(Curator())
AlienRegistry.register(Tinker())
