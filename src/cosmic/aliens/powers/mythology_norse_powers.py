"""
Norse Mythology themed alien powers for Cosmic Encounter.

Powers based on Norse gods, creatures, and mythological concepts.
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


# ============================================================================
# NORSE GODS
# ============================================================================

@dataclass
class Odin(AlienPower):
    """Odin - Power of Wisdom. See opponent's cards."""
    name: str = field(default="Odin", init=False)
    description: str = field(default="See opponent's hand before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thor(AlienPower):
    """Thor - Power of Thunder. Devastating attacks."""
    name: str = field(default="Thor", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 6
        return base_total


@dataclass
class Loki(AlienPower):
    """Loki - Power of Trickery. Swap encounter cards."""
    name: str = field(default="Loki", init=False)
    description: str = field(default="After reveal, may swap both encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Freya(AlienPower):
    """Freya - Power of Love. Attract allies."""
    name: str = field(default="Freya", init=False)
    description: str = field(default="Invited allies must join your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tyr(AlienPower):
    """Tyr - Power of War. Combat specialist."""
    name: str = field(default="Tyr", init=False)
    description: str = field(default="+4 in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Heimdall(AlienPower):
    """Heimdall - Power of Vigilance. See all threats."""
    name: str = field(default="Heimdall", init=False)
    description: str = field(default="See destiny cards before they're drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Frigg(AlienPower):
    """Frigg - Power of Fate. Manipulate destiny."""
    name: str = field(default="Frigg", init=False)
    description: str = field(default="Redraw destiny once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Baldur(AlienPower):
    """Baldur - Power of Light. Protected from harm."""
    name: str = field(default="Baldur", init=False)
    description: str = field(default="Lose only half ships on loss (rounded up).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# NORSE CREATURES
# ============================================================================

@dataclass
class Fenrir(AlienPower):
    """Fenrir - Power of the Wolf. Devour enemies."""
    name: str = field(default="Fenrir", init=False)
    description: str = field(default="Opponent loses extra ship on your win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jormungandr(AlienPower):
    """Jormungandr - Power of the Serpent. Encircle enemies."""
    name: str = field(default="Jormungandr", init=False)
    description: str = field(default="+2 per ship opponent has.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            opp_ships = sum(game.defense_ships.values())
        else:
            opp_ships = sum(game.offense_ships.values())
        return base_total + (opp_ships * 2)


@dataclass
class Sleipnir(AlienPower):
    """Sleipnir - Power of Speed. Fast movement."""
    name: str = field(default="Sleipnir", init=False)
    description: str = field(default="May attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Valkyrie(AlienPower):
    """Valkyrie - Power of the Chosen. Retrieve the fallen."""
    name: str = field(default="Valkyrie", init=False)
    description: str = field(default="Retrieve 2 ships from warp after any encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Draugr(AlienPower):
    """Draugr - Power of the Undead. Ships return from warp."""
    name: str = field(default="Draugr", init=False)
    description: str = field(default="Ships in warp return to colonies after 1 turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nidhogg(AlienPower):
    """Nidhogg - Power of Destruction. Consume resources."""
    name: str = field(default="Nidhogg", init=False)
    description: str = field(default="Opponent discards 1 card when you attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Raven(AlienPower):
    """Raven - Power of Scouting. Gather information."""
    name: str = field(default="Raven", init=False)
    description: str = field(default="See top 3 cards of any deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# NORSE CONCEPTS
# ============================================================================

@dataclass
class Ragnarok(AlienPower):
    """Ragnarok - Power of Doom. End-game destruction."""
    name: str = field(default="Ragnarok", init=False)
    description: str = field(default="After turn 15, all players lose 1 ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Yggdrasil(AlienPower):
    """Yggdrasil - Power of Connection. Link all colonies."""
    name: str = field(default="Yggdrasil", init=False)
    description: str = field(default="Ships can move between your colonies freely.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Valhalla(AlienPower):
    """Valhalla - Power of Glory. Reward for battle."""
    name: str = field(default="Valhalla", init=False)
    description: str = field(default="Draw 1 card for each ship lost in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bifrost(AlienPower):
    """Bifrost - Power of the Bridge. Connect realms."""
    name: str = field(default="Bifrost", init=False)
    description: str = field(default="Attack any player's colony as if adjacent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rune(AlienPower):
    """Rune - Power of Magic. Inscribe power."""
    name: str = field(default="Rune", init=False)
    description: str = field(default="Mark a planet. +3 when attacking/defending it.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mead(AlienPower):
    """Mead - Power of Inspiration. Boost allies."""
    name: str = field(default="Mead", init=False)
    description: str = field(default="Allied ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mjolnir(AlienPower):
    """Mjolnir - Power of the Hammer. Return to sender."""
    name: str = field(default="Mjolnir", init=False)
    description: str = field(default="Your encounter card returns to hand after use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all Norse mythology powers
NORSE_MYTHOLOGY_POWERS = [
    Odin, Thor, Loki, Freya, Tyr, Heimdall, Frigg, Baldur,
    Fenrir, Jormungandr, Sleipnir, Valkyrie, Draugr, Nidhogg, Raven,
    Ragnarok, Yggdrasil, Valhalla, Bifrost, Rune, Mead, Mjolnir,
]


# Auto-register all powers
for power_class in NORSE_MYTHOLOGY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
