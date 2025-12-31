"""
Ocean Powers - Aquatic and marine-themed aliens.
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
class Kraken(AlienPower):
    """Kraken - Sea monster. Drag 2 opponent ships to warp."""
    name: str = field(default="Kraken", init=False)
    description: str = field(default="Send 2 enemy ships to warp when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Leviathan(AlienPower):
    """Leviathan - Deep dweller. +5 when defending home."""
    name: str = field(default="Leviathan", init=False)
    description: str = field(default="+5 when defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 5
        return total


@dataclass
class Octopus(AlienPower):
    """Octopus - Eight arms. Send 8 ships maximum to encounters."""
    name: str = field(default="Octopus", init=False)
    description: str = field(default="Can send up to 8 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Whale(AlienPower):
    """Whale - Massive presence. Ships count as 2 each."""
    name: str = field(default="Whale", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dolphin(AlienPower):
    """Dolphin - Playful intelligence. Choose to join winning side after reveal."""
    name: str = field(default="Dolphin", init=False)
    description: str = field(default="Switch sides after card reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jellyfish(AlienPower):
    """Jellyfish - Stinging touch. Opponent discards card when winning."""
    name: str = field(default="Jellyfish", init=False)
    description: str = field(default="Force discard even in victory.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Seahorse(AlienPower):
    """Seahorse - Protective parent. Move ships freely between colonies."""
    name: str = field(default="Seahorse", init=False)
    description: str = field(default="Freely relocate ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eel(AlienPower):
    """Eel - Electric shock. -3 to opponent's total."""
    name: str = field(default="Eel", init=False)
    description: str = field(default="-3 to opponent's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Coral(AlienPower):
    """Coral - Living structure. +1 for each planet you control."""
    name: str = field(default="Coral", init=False)
    description: str = field(default="+1 per planet controlled.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = len(player.foreign_colonies) + len([p for p in player.home_planets if player.name in p.ships])
            return total + colonies
        return total


@dataclass
class Siren(AlienPower):
    """Siren - Enchanting song. Force opponent to ally with you."""
    name: str = field(default="Siren", init=False)
    description: str = field(default="Force one player to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crab(AlienPower):
    """Crab - Hard shell. First 2 ships lost are saved."""
    name: str = field(default="Crab", init=False)
    description: str = field(default="Save first 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anglerfish(AlienPower):
    """Anglerfish - Luring light. Draw opponent to your home system."""
    name: str = field(default="Anglerfish", init=False)
    description: str = field(default="Choose which player attacks you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Starfish(AlienPower):
    """Starfish - Regeneration. Retrieve ship from warp each encounter."""
    name: str = field(default="Starfish", init=False)
    description: str = field(default="Retrieve 1 ship each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clam(AlienPower):
    """Clam - Pearl keeper. Keep discarded negotiate cards."""
    name: str = field(default="Clam", init=False)
    description: str = field(default="Keep negotiate cards after use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seal(AlienPower):
    """Seal - Slippery swimmer. Escape losing encounters."""
    name: str = field(default="Seal", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Kraken())
AlienRegistry.register(Leviathan())
AlienRegistry.register(Octopus())
AlienRegistry.register(Whale())
AlienRegistry.register(Dolphin())
AlienRegistry.register(Jellyfish())
AlienRegistry.register(Seahorse())
AlienRegistry.register(Eel())
AlienRegistry.register(Coral())
AlienRegistry.register(Siren())
AlienRegistry.register(Crab())
AlienRegistry.register(Anglerfish())
AlienRegistry.register(Starfish())
AlienRegistry.register(Clam())
AlienRegistry.register(Seal())
