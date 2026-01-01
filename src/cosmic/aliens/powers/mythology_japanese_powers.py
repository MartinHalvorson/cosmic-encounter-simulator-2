"""
Japanese Mythology themed alien powers for Cosmic Encounter.

Powers based on Japanese gods, spirits, and mythological concepts.
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
# KAMI (GODS)
# ============================================================================

@dataclass
class Amaterasu(AlienPower):
    """Amaterasu - Power of the Sun. Divine radiance."""
    name: str = field(default="Amaterasu", init=False)
    description: str = field(default="+5 on odd-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 5
        return base_total


@dataclass
class Tsukuyomi(AlienPower):
    """Tsukuyomi - Power of the Moon. Night strength."""
    name: str = field(default="Tsukuyomi", init=False)
    description: str = field(default="+5 on even-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 5
        return base_total


@dataclass
class Susanoo(AlienPower):
    """Susanoo - Power of Storms. Destructive force."""
    name: str = field(default="Susanoo", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 6
        return base_total


@dataclass
class Izanagi(AlienPower):
    """Izanagi - Power of Creation. Divine origin."""
    name: str = field(default="Izanagi", init=False)
    description: str = field(default="+1 per turn (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class Izanami(AlienPower):
    """Izanami - Power of Death. Underworld queen."""
    name: str = field(default="Izanami", init=False)
    description: str = field(default="Ships lost against you stay in warp longer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Inari(AlienPower):
    """Inari - Power of Prosperity. Agricultural blessing."""
    name: str = field(default="Inari", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Raijin(AlienPower):
    """Raijin - Power of Thunder. Lightning strikes."""
    name: str = field(default="Raijin", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Fujin(AlienPower):
    """Fujin - Power of Wind. Swift movement."""
    name: str = field(default="Fujin", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# YOKAI (SPIRITS)
# ============================================================================

@dataclass
class Kitsune(AlienPower):
    """Kitsune - Power of the Fox. Trickery and cunning."""
    name: str = field(default="Kitsune", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tanuki(AlienPower):
    """Tanuki - Power of Transformation. Shape-shifting bonus."""
    name: str = field(default="Tanuki", init=False)
    description: str = field(default="Random +2 to +6 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(2, 6)
        return base_total


@dataclass
class Tengu(AlienPower):
    """Tengu - Power of Martial Arts. Combat mastery."""
    name: str = field(default="Tengu", init=False)
    description: str = field(default="+3 per ship in encounter (max +9).", init=False)
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
        return base_total + min(9, ships * 3)


@dataclass
class Oni(AlienPower):
    """Oni - Power of Demons. Brutal strength."""
    name: str = field(default="Oni", init=False)
    description: str = field(default="+5 when attacking with 4+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active or side != Side.OFFENSE:
            return base_total
        ships = game.offense_ships.get(player.name, 0)
        if ships >= 4:
            return base_total + 5
        return base_total


@dataclass
class Kappa(AlienPower):
    """Kappa - Power of Water. Aquatic strength."""
    name: str = field(default="Kappa", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Yurei(AlienPower):
    """Yurei - Power of Ghosts. Ethereal presence."""
    name: str = field(default="Yurei", init=False)
    description: str = field(default="Ships can't be permanently destroyed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jorogumo(AlienPower):
    """Jorogumo - Power of the Spider. Trap and ensnare."""
    name: str = field(default="Jorogumo", init=False)
    description: str = field(default="Opponent's allies can't join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CULTURAL CONCEPTS
# ============================================================================

@dataclass
class Bushido(AlienPower):
    """Bushido - Power of Honor. Warrior's code."""
    name: str = field(default="Bushido", init=False)
    description: str = field(default="+3 in one-on-one combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Zen(AlienPower):
    """Zen - Power of Meditation. Inner peace."""
    name: str = field(default="Zen", init=False)
    description: str = field(default="+2 per foreign colony (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(8, colonies * 2)
        return base_total


@dataclass
class Origami(AlienPower):
    """Origami - Power of Folding. Transform cards."""
    name: str = field(default="Origami", init=False)
    description: str = field(default="Your card +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sakura(AlienPower):
    """Sakura - Power of Cherry Blossoms. Fleeting beauty."""
    name: str = field(default="Sakura", init=False)
    description: str = field(default="+6 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 6
        return base_total


@dataclass
class Torii(AlienPower):
    """Torii - Power of Gates. Sacred passage."""
    name: str = field(default="Torii", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all Japanese mythology powers
JAPANESE_MYTHOLOGY_POWERS = [
    Amaterasu, Tsukuyomi, Susanoo, Izanagi, Izanami, Inari, Raijin, Fujin,
    Kitsune, Tanuki, Tengu, Oni, Kappa, Yurei, Jorogumo,
    Bushido, Zen, Origami, Sakura, Torii,
]


# Auto-register all powers
for power_class in JAPANESE_MYTHOLOGY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
