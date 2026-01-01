"""
Game Mechanics themed alien powers for Cosmic Encounter.

Powers based on board game and video game mechanics.
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
# BOARD GAME MECHANICS
# ============================================================================

@dataclass
class Dice_Roll(AlienPower):
    """Dice_Roll - Power of Chance. Random outcomes."""
    name: str = field(default="Dice_Roll", init=False)
    description: str = field(default="Random +1 to +6 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 6)
        return base_total


@dataclass
class Turn_Order(AlienPower):
    """Turn_Order - Power of Sequence. First strike."""
    name: str = field(default="Turn_Order", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Victory_Point(AlienPower):
    """Victory_Point - Power of Scoring. Goal-oriented."""
    name: str = field(default="Victory_Point", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Draw_Card(AlienPower):
    """Draw_Card - Power of Resources. Card advantage."""
    name: str = field(default="Draw_Card", init=False)
    description: str = field(default="Draw 1 card after any encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mulligan(AlienPower):
    """Mulligan - Power of Retry. Second chance."""
    name: str = field(default="Mulligan", init=False)
    description: str = field(default="Redraw your card once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Critical_Hit(AlienPower):
    """Critical_Hit - Power of Lucky Strike. Massive damage."""
    name: str = field(default="Critical_Hit", init=False)
    description: str = field(default="20% chance of +10 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and random.random() < 0.2:
            return base_total + 10
        return base_total


@dataclass
class Level_Up(AlienPower):
    """Level_Up - Power of Growth. Increasing strength."""
    name: str = field(default="Level_Up", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Power_Up(AlienPower):
    """Power_Up - Power of Enhancement. Boost abilities."""
    name: str = field(default="Power_Up", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


# ============================================================================
# VIDEO GAME MECHANICS
# ============================================================================

@dataclass
class Respawn(AlienPower):
    """Respawn - Power of Return. Come back to life."""
    name: str = field(default="Respawn", init=False)
    description: str = field(default="Retrieve 3 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Health_Bar(AlienPower):
    """Health_Bar - Power of Endurance. Stay alive."""
    name: str = field(default="Health_Bar", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Combo(AlienPower):
    """Combo - Power of Chains. Building attacks."""
    name: str = field(default="Combo", init=False)
    description: str = field(default="+2 per consecutive win (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    wins: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, self.wins * 2)
        return base_total


@dataclass
class Boss_Fight(AlienPower):
    """Boss_Fight - Power of Challenge. Difficult opponent."""
    name: str = field(default="Boss_Fight", init=False)
    description: str = field(default="+6 with 4+ ships.", init=False)
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
        if ships >= 4:
            return base_total + 6
        return base_total


@dataclass
class Save_Point(AlienPower):
    """Save_Point - Power of Preservation. Protect progress."""
    name: str = field(default="Save_Point", init=False)
    description: str = field(default="Lose only half ships on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Speedrun(AlienPower):
    """Speedrun - Power of Speed. Fast victory."""
    name: str = field(default="Speedrun", init=False)
    description: str = field(default="+5 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 5
        return base_total


# ============================================================================
# STRATEGY MECHANICS
# ============================================================================

@dataclass
class Flanking(AlienPower):
    """Flanking - Power of Position. Tactical bonus."""
    name: str = field(default="Flanking", init=False)
    description: str = field(default="+3 with allies.", init=False)
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
        if allies > 0:
            return base_total + 3
        return base_total


@dataclass
class Ambush(AlienPower):
    """Ambush - Power of Surprise. Unexpected attack."""
    name: str = field(default="Ambush", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Fortify(AlienPower):
    """Fortify - Power of Defense. Strong position."""
    name: str = field(default="Fortify", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Resource_Pool(AlienPower):
    """Resource_Pool - Power of Accumulation. Build resources."""
    name: str = field(default="Resource_Pool", init=False)
    description: str = field(default="+1 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(6, len(player.hand))
        return base_total


# Register all game mechanics powers
GAME_MECHANICS_POWERS = [
    Dice_Roll, Turn_Order, Victory_Point, Draw_Card, Mulligan, Critical_Hit, Level_Up, Power_Up,
    Respawn, Health_Bar, Combo, Boss_Fight, Save_Point, Speedrun,
    Flanking, Ambush, Fortify, Resource_Pool,
]


# Auto-register all powers
for power_class in GAME_MECHANICS_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
