"""
Habitat Powers - Environment and habitat themed aliens.
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
class Forest(AlienPower):
    """Forest - Power of Woods. +3 on defense."""
    name: str = field(default="Forest", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Meadow(AlienPower):
    """Meadow - Power of Fields. +2 always."""
    name: str = field(default="Meadow", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Marsh(AlienPower):
    """Marsh - Power of Wetlands. -2 to attacker."""
    name: str = field(default="Marsh", init=False)
    description: str = field(default="Attacker gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Grove(AlienPower):
    """Grove - Power of Trees. Extra card draw."""
    name: str = field(default="Grove", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pond(AlienPower):
    """Pond - Power of Still Water. Retrieve ships."""
    name: str = field(default="Pond", init=False)
    description: str = field(default="Return 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reef_Alt(AlienPower):
    """Reef_Alt - Power of Coral. +3 on defense."""
    name: str = field(default="Reef_Alt", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Burrow(AlienPower):
    """Burrow - Power of Underground. Ships escape."""
    name: str = field(default="Burrow", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nest(AlienPower):
    """Nest - Power of Home. +4 defending home."""
    name: str = field(default="Nest", init=False)
    description: str = field(default="+4 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hive(AlienPower):
    """Hive - Power of Colony. +1 per ship."""
    name: str = field(default="Hive", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Den(AlienPower):
    """Den - Power of Shelter. +3 always."""
    name: str = field(default="Den", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Warren(AlienPower):
    """Warren - Power of Tunnels. Move ships freely."""
    name: str = field(default="Warren", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lair(AlienPower):
    """Lair - Power of the Hidden. Card stays hidden."""
    name: str = field(default="Lair", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Roost(AlienPower):
    """Roost - Power of Perching. +2 per ally."""
    name: str = field(default="Roost", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Aerie(AlienPower):
    """Aerie - Power of Heights. +4 on offense."""
    name: str = field(default="Aerie", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Canopy(AlienPower):
    """Canopy - Power of Cover. Reduce opponent damage."""
    name: str = field(default="Canopy", init=False)
    description: str = field(default="Lose 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
HABITAT_POWERS = [
    Forest, Meadow, Marsh, Grove, Pond, Reef_Alt, Burrow, Nest, Hive, Den,
    Warren, Lair, Roost, Aerie, Canopy,
]

for power_class in HABITAT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
