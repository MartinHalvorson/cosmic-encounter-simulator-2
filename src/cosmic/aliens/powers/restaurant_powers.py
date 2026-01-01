"""
Restaurant themed alien powers for Cosmic Encounter.

Powers based on restaurant types, dining experiences, and food service.
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
# RESTAURANT TYPES
# ============================================================================

@dataclass
class Fine_Dining(AlienPower):
    """Fine_Dining - Power of Excellence. Premium experience."""
    name: str = field(default="Fine_Dining", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Fast_Food(AlienPower):
    """Fast_Food - Power of Speed. Quick service."""
    name: str = field(default="Fast_Food", init=False)
    description: str = field(default="+3 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Buffet(AlienPower):
    """Buffet - Power of Plenty. All you can eat."""
    name: str = field(default="Buffet", init=False)
    description: str = field(default="+1 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, len(player.hand))
        return base_total


@dataclass
class Diner(AlienPower):
    """Diner - Power of Comfort. Classic experience."""
    name: str = field(default="Diner", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Food_Truck(AlienPower):
    """Food_Truck - Power of Mobility. Go anywhere."""
    name: str = field(default="Food_Truck", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cafe(AlienPower):
    """Cafe - Power of Relaxation. Social bonus."""
    name: str = field(default="Cafe", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 2)


# ============================================================================
# RESTAURANT ROLES
# ============================================================================

@dataclass
class Chef_Rest(AlienPower):
    """Chef_Rest - Power of Creation. Master of the kitchen."""
    name: str = field(default="Chef_Rest", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Waiter(AlienPower):
    """Waiter - Power of Service. Help others."""
    name: str = field(default="Waiter", init=False)
    description: str = field(default="Allies draw 1 card each on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bartender(AlienPower):
    """Bartender - Power of Mixing. Combine effects."""
    name: str = field(default="Bartender", init=False)
    description: str = field(default="Random +2 to +5 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(2, 5)
        return base_total


@dataclass
class Manager(AlienPower):
    """Manager - Power of Control. Oversee operations."""
    name: str = field(default="Manager_Rest", init=False)
    description: str = field(default="+2 per foreign colony (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(6, colonies * 2)
        return base_total


@dataclass
class Host(AlienPower):
    """Host - Power of Welcome. Greet guests."""
    name: str = field(default="Host_Rest", init=False)
    description: str = field(default="Invited allies must join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CUISINE STYLES
# ============================================================================

@dataclass
class Italian(AlienPower):
    """Italian - Power of Tradition. Classic bonus."""
    name: str = field(default="Italian", init=False)
    description: str = field(default="+3 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Mexican(AlienPower):
    """Mexican - Power of Spice. Fiery bonus."""
    name: str = field(default="Mexican", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Chinese_Food(AlienPower):
    """Chinese_Food - Power of Balance. Yin and yang."""
    name: str = field(default="Chinese_Food", init=False)
    description: str = field(default="+2 on odd turns, +3 on even.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if game.current_turn % 2 == 1:
                return base_total + 2
            else:
                return base_total + 3
        return base_total


@dataclass
class Japanese(AlienPower):
    """Japanese - Power of Precision. Careful execution."""
    name: str = field(default="Japanese_Food", init=False)
    description: str = field(default="+4 if your card is 10+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class French(AlienPower):
    """French - Power of Refinement. Sophisticated bonus."""
    name: str = field(default="French_Food", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, game.current_turn)
        return base_total


# Register all restaurant powers
RESTAURANT_POWERS = [
    Fine_Dining, Fast_Food, Buffet, Diner, Food_Truck, Cafe,
    Chef_Rest, Waiter, Bartender, Manager, Host,
    Italian, Mexican, Chinese_Food, Japanese, French,
]


# Auto-register all powers
for power_class in RESTAURANT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
