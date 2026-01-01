"""
Lovecraftian/Cosmic horror themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Cthulhu(AlienPower):
    """Cthulhu - Dreaming god. +6 always."""
    name: str = field(default="Cthulhu", init=False)
    description: str = field(default="+6 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Nyarlathotep(AlienPower):
    """Nyarlathotep - Crawling chaos. Random +0-10."""
    name: str = field(default="Nyarlathotep", init=False)
    description: str = field(default="Random +0-10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(0, 10)
        return total


@dataclass
class Azathoth(AlienPower):
    """Azathoth - Blind idiot god. -4 to everyone."""
    name: str = field(default="Azathoth", init=False)
    description: str = field(default="-4 to all sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Yog_Sothoth(AlienPower):
    """Yog_Sothoth - Gate and key. See all cards."""
    name: str = field(default="Yog_Sothoth", init=False)
    description: str = field(default="View all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shub_Niggurath(AlienPower):
    """Shub_Niggurath - Black goat. Retrieve 4 ships."""
    name: str = field(default="Shub_Niggurath", init=False)
    description: str = field(default="Retrieve 4 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dagon(AlienPower):
    """Dagon - Deep one lord. +5 defending."""
    name: str = field(default="Dagon", init=False)
    description: str = field(default="+5 defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Hastur(AlienPower):
    """Hastur - The unspeakable. +5 attacking."""
    name: str = field(default="Hastur", init=False)
    description: str = field(default="+5 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Deep_One(AlienPower):
    """Deep_One - Ocean dweller. +3 always."""
    name: str = field(default="Deep_One", init=False)
    description: str = field(default="+3 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Shoggoth(AlienPower):
    """Shoggoth - Shapeless horror. Copy power."""
    name: str = field(default="Shoggoth", init=False)
    description: str = field(default="Copy opponent power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mi_Go(AlienPower):
    """Mi_Go - Fungi from Yuggoth. +4 first encounter."""
    name: str = field(default="Mi_Go", init=False)
    description: str = field(default="+4 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Elder_Thing(AlienPower):
    """Elder_Thing - Ancient builder. +2 per home colony."""
    name: str = field(default="Elder_Thing", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Star_Spawn(AlienPower):
    """Star_Spawn - Cthulhu's kin. +4 defending home."""
    name: str = field(default="Star_Spawn", init=False)
    description: str = field(default="+4 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flying_Polyp(AlienPower):
    """Flying_Polyp - Wind creature. Ships go home."""
    name: str = field(default="Flying_Polyp", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nightgaunt(AlienPower):
    """Nightgaunt - Dream carrier. Win ties."""
    name: str = field(default="Nightgaunt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ghoul(AlienPower):
    """Ghoul - Corpse eater. +1 per card."""
    name: str = field(default="Ghoul_Cosmic", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


# Register all powers
LOVECRAFT_POWERS = [
    Cthulhu, Nyarlathotep, Azathoth, Yog_Sothoth, Shub_Niggurath,
    Dagon, Hastur, Deep_One, Shoggoth, Mi_Go, Elder_Thing,
    Star_Spawn, Flying_Polyp, Nightgaunt, Ghoul,
]

for power_class in LOVECRAFT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
