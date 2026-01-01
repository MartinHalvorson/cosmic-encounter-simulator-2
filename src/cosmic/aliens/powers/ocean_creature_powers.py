"""
Ocean Creature Powers for Cosmic Encounter.

Aliens inspired by sea creatures and marine life.
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
class Shark_Alt(AlienPower):
    """Shark_Alt - Power of Hunting. +3 against wounded opponents."""
    name: str = field(default="Shark_Alt", init=False)
    description: str = field(default="+3 vs opponents with ships in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Whale_Alt(AlienPower):
    """Whale_Alt - Power of Size. Ships count as 2."""
    name: str = field(default="Whale_Alt", init=False)
    description: str = field(default="Ships count as 2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Octopus_Alt(AlienPower):
    """Octopus_Alt - Power of Arms. May commit from multiple colonies."""
    name: str = field(default="Octopus_Alt", init=False)
    description: str = field(default="Commit from any colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jellyfish_Alt(AlienPower):
    """Jellyfish_Alt - Power of Stinging. Attacker loses 1 ship after encounter."""
    name: str = field(default="Jellyfish_Alt", init=False)
    description: str = field(default="Attacker loses 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dolphin_Alt(AlienPower):
    """Dolphin_Alt - Power of Intelligence. See opponent's card before choosing."""
    name: str = field(default="Dolphin_Alt", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Seahorse_Alt(AlienPower):
    """Seahorse_Alt - Power of Grace. Win ties automatically."""
    name: str = field(default="Seahorse_Alt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crab_Alt(AlienPower):
    """Crab_Alt - Power of Armor. +2 on defense."""
    name: str = field(default="Crab_Alt", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Lobster(AlienPower):
    """Lobster - Power of Claws. +3 on offense."""
    name: str = field(default="Lobster", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Squid(AlienPower):
    """Squid - Power of Ink. Force opponent to discard 1 card."""
    name: str = field(default="Squid", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Starfish(AlienPower):
    """Starfish - Power of Regeneration. Return 1 ship from warp each encounter."""
    name: str = field(default="Starfish", init=False)
    description: str = field(default="Return 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Urchin(AlienPower):
    """Urchin - Power of Spines. Attackers lose 1 ship when attacking you."""
    name: str = field(default="Urchin", init=False)
    description: str = field(default="Attackers lose 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Anglerfish(AlienPower):
    """Anglerfish - Power of Lure. Draw opponent into your home system."""
    name: str = field(default="Anglerfish", init=False)
    description: str = field(default="Lure opponent to your system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Manta(AlienPower):
    """Manta - Power of Gliding. +2 and may retreat without losing ships."""
    name: str = field(default="Manta", init=False)
    description: str = field(default="+2 and safe retreat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Clam(AlienPower):
    """Clam - Power of Shells. Cannot lose more than 2 ships per encounter."""
    name: str = field(default="Clam", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Barracuda(AlienPower):
    """Barracuda - Power of Speed. +4 on first encounter of turn."""
    name: str = field(default="Barracuda", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


# Register all ocean creature powers
AlienRegistry.register(Shark_Alt())
AlienRegistry.register(Whale_Alt())
AlienRegistry.register(Octopus_Alt())
AlienRegistry.register(Jellyfish_Alt())
AlienRegistry.register(Dolphin_Alt())
AlienRegistry.register(Seahorse_Alt())
AlienRegistry.register(Crab_Alt())
AlienRegistry.register(Lobster())
AlienRegistry.register(Squid())
AlienRegistry.register(Starfish())
AlienRegistry.register(Urchin())
AlienRegistry.register(Anglerfish())
AlienRegistry.register(Manta())
AlienRegistry.register(Clam())
AlienRegistry.register(Barracuda())
