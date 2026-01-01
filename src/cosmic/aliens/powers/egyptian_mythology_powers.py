"""
Egyptian mythology themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Ra(AlienPower):
    """Ra - Power of the Sun. Supreme solar deity."""
    name: str = field(default="Ra", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Osiris(AlienPower):
    """Osiris - Power of Resurrection. King of the dead."""
    name: str = field(default="Osiris", init=False)
    description: str = field(default="Retrieve 3 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Isis(AlienPower):
    """Isis - Power of Magic. Divine sorceress."""
    name: str = field(default="Isis", init=False)
    description: str = field(default="Copy any power once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Horus(AlienPower):
    """Horus - Power of the Sky. Falcon god."""
    name: str = field(default="Horus", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Set(AlienPower):
    """Set - Power of Chaos. Storm lord."""
    name: str = field(default="Set", init=False)
    description: str = field(default="Random +0-10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(0, 10)
        return base_total


@dataclass
class Anubis(AlienPower):
    """Anubis - Power of the Dead. Jackal guide."""
    name: str = field(default="Anubis", init=False)
    description: str = field(default="Control warp order.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thoth(AlienPower):
    """Thoth - Power of Knowledge. Divine scribe."""
    name: str = field(default="Thoth", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bastet(AlienPower):
    """Bastet - Power of Cats. Feline protector."""
    name: str = field(default="Bastet", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Sekhmet(AlienPower):
    """Sekhmet - Power of War. Lioness destroyer."""
    name: str = field(default="Sekhmet", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 6
        return base_total


@dataclass
class Hathor(AlienPower):
    """Hathor - Power of Joy. Celestial cow."""
    name: str = field(default="Hathor", init=False)
    description: str = field(default="+3 and draw card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Ptah(AlienPower):
    """Ptah - Power of Creation. Divine craftsman."""
    name: str = field(default="Ptah", init=False)
    description: str = field(default="+2 per ship (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + min(8, ships * 2)


@dataclass
class Sobek(AlienPower):
    """Sobek - Power of Crocodiles. Fierce guardian."""
    name: str = field(default="Sobek", init=False)
    description: str = field(default="+5 in water planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Khnum(AlienPower):
    """Khnum - Power of the River. Ram creator."""
    name: str = field(default="Khnum", init=False)
    description: str = field(default="+2 per colony (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nut(AlienPower):
    """Nut - Power of the Sky. Celestial body."""
    name: str = field(default="Nut", init=False)
    description: str = field(default="+3 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Geb(AlienPower):
    """Geb - Power of Earth. Ground father."""
    name: str = field(default="Geb", init=False)
    description: str = field(default="+4 when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Nephthys(AlienPower):
    """Nephthys - Power of Night. Lady of the house."""
    name: str = field(default="Nephthys", init=False)
    description: str = field(default="+3 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 3
        return base_total


@dataclass
class Maat(AlienPower):
    """Maat - Power of Truth. Divine order."""
    name: str = field(default="Maat", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Aten(AlienPower):
    """Aten - Power of the Disk. Solar emanation."""
    name: str = field(default="Aten", init=False)
    description: str = field(default="+4 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 4
        return base_total


@dataclass
class Khepri(AlienPower):
    """Khepri - Power of Dawn. Scarab god."""
    name: str = field(default="Khepri", init=False)
    description: str = field(default="Retrieve 2 ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


EGYPTIAN_MYTHOLOGY_POWERS = [
    Ra, Osiris, Isis, Horus, Set, Anubis, Thoth, Bastet, Sekhmet, Hathor,
    Ptah, Sobek, Khnum, Nut, Geb, Nephthys, Maat, Aten, Khepri,
]

for power_class in EGYPTIAN_MYTHOLOGY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
