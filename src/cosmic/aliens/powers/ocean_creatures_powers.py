"""
Ocean Creatures themed alien powers for Cosmic Encounter.

Powers based on marine life and deep sea creatures.
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
# SHARKS
# ============================================================================

@dataclass
class Great_White(AlienPower):
    """Great_White - Power of Apex. Top predator."""
    name: str = field(default="Great_White", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Hammerhead(AlienPower):
    """Hammerhead - Power of Perception. See all around."""
    name: str = field(default="Hammerhead", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tiger_Shark(AlienPower):
    """Tiger_Shark - Power of Ferocity. Aggressive hunter."""
    name: str = field(default="Tiger_Shark", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


# ============================================================================
# WHALES
# ============================================================================

@dataclass
class Blue_Whale(AlienPower):
    """Blue_Whale - Power of Size. Massive presence."""
    name: str = field(default="Blue_Whale", init=False)
    description: str = field(default="+2 per ship (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + min(10, ships * 2)


@dataclass
class Orca(AlienPower):
    """Orca - Power of Intelligence. Smart hunter."""
    name: str = field(default="Orca", init=False)
    description: str = field(default="+3 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 3)


@dataclass
class Humpback(AlienPower):
    """Humpback - Power of Song. Communication bonus."""
    name: str = field(default="Humpback", init=False)
    description: str = field(default="Invited allies must join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# DEEP SEA
# ============================================================================

@dataclass
class Anglerfish(AlienPower):
    """Anglerfish - Power of Lure. Attract enemies."""
    name: str = field(default="Anglerfish", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Giant_Squid(AlienPower):
    """Giant_Squid - Power of Tentacles. Multiple grabs."""
    name: str = field(default="Giant_Squid", init=False)
    description: str = field(default="+1 per card in hand (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, len(player.hand))
        return base_total


@dataclass
class Viperfish(AlienPower):
    """Viperfish - Power of Fangs. Deadly bite."""
    name: str = field(default="Viperfish", init=False)
    description: str = field(default="+5 when attacking with 1-2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active or side != Side.OFFENSE:
            return base_total
        ships = game.offense_ships.get(player.name, 0)
        if ships <= 2:
            return base_total + 5
        return base_total


# ============================================================================
# MOLLUSKS
# ============================================================================

@dataclass
class Nautilus(AlienPower):
    """Nautilus - Power of Shell. Protected defense."""
    name: str = field(default="Nautilus", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Octopus_OC(AlienPower):
    """Octopus_OC - Power of Escape. Ink and flee."""
    name: str = field(default="Octopus_OC", init=False)
    description: str = field(default="Lose only half ships on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cuttlefish(AlienPower):
    """Cuttlefish - Power of Camouflage. Hide your plans."""
    name: str = field(default="Cuttlefish", init=False)
    description: str = field(default="Opponent can't see your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CRUSTACEANS
# ============================================================================

@dataclass
class Lobster(AlienPower):
    """Lobster - Power of Claws. Crushing grip."""
    name: str = field(default="Lobster", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Mantis_Shrimp(AlienPower):
    """Mantis_Shrimp - Power of Punch. Lightning strike."""
    name: str = field(default="Mantis_Shrimp", init=False)
    description: str = field(default="+6 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hermit_Crab(AlienPower):
    """Hermit_Crab - Power of Home. Mobile defense."""
    name: str = field(default="Hermit_Crab", init=False)
    description: str = field(default="+3 when defending home colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


# Register all ocean creatures powers
OCEAN_CREATURES_POWERS = [
    Great_White, Hammerhead, Tiger_Shark,
    Blue_Whale, Orca, Humpback,
    Anglerfish, Giant_Squid, Viperfish,
    Nautilus, Octopus_OC, Cuttlefish,
    Lobster, Mantis_Shrimp, Hermit_Crab,
]


# Auto-register all powers
for power_class in OCEAN_CREATURES_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
