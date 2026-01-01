"""
Military Rank themed alien powers for Cosmic Encounter.

Powers based on military ranks and command structures.
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
# ENLISTED RANKS
# ============================================================================

@dataclass
class Private(AlienPower):
    """Private - Power of Humility. Underdog bonus."""
    name: str = field(default="Private", init=False)
    description: str = field(default="+3 when you have fewest colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Corporal(AlienPower):
    """Corporal - Power of Team. Small group bonus."""
    name: str = field(default="Corporal", init=False)
    description: str = field(default="+2 with exactly 2 ships.", init=False)
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
        if ships == 2:
            return base_total + 2
        return base_total


@dataclass
class Sergeant(AlienPower):
    """Sergeant - Power of Discipline. Consistent bonus."""
    name: str = field(default="Sergeant", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Staff_Sergeant(AlienPower):
    """Staff_Sergeant - Power of Experience. Veteran bonus."""
    name: str = field(default="Staff_Sergeant", init=False)
    description: str = field(default="+1 per 2 turns (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = game.current_turn // 2
            return base_total + min(5, bonus)
        return base_total


# ============================================================================
# NCO RANKS
# ============================================================================

@dataclass
class Warrant_Officer(AlienPower):
    """Warrant_Officer - Power of Expertise. Technical bonus."""
    name: str = field(default="Warrant_Officer", init=False)
    description: str = field(default="+3 if your card is 10 or higher.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Master_Sergeant(AlienPower):
    """Master_Sergeant - Power of Mastery. Peak performance."""
    name: str = field(default="Master_Sergeant", init=False)
    description: str = field(default="+4 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class First_Sergeant(AlienPower):
    """First_Sergeant - Power of Primacy. Lead from front."""
    name: str = field(default="First_Sergeant", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Sergeant_Major(AlienPower):
    """Sergeant_Major - Power of Senior NCO. Command presence."""
    name: str = field(default="Sergeant_Major", init=False)
    description: str = field(default="+1 per allied ship (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# OFFICER RANKS
# ============================================================================

@dataclass
class Lieutenant(AlienPower):
    """Lieutenant - Power of Junior Officer. Fresh leadership."""
    name: str = field(default="Lieutenant", init=False)
    description: str = field(default="+4 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 4
        return base_total


@dataclass
class Captain_Rank(AlienPower):
    """Captain_Rank - Power of Company. Unit command."""
    name: str = field(default="Captain_Rank", init=False)
    description: str = field(default="+1 per ship in encounter (max +4).", init=False)
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
        return base_total + min(4, ships)


@dataclass
class Major(AlienPower):
    """Major - Power of Battalion. Larger unit command."""
    name: str = field(default="Major", init=False)
    description: str = field(default="+3 with 3+ ships.", init=False)
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
        if ships >= 3:
            return base_total + 3
        return base_total


@dataclass
class Colonel(AlienPower):
    """Colonel - Power of Regiment. Strong command."""
    name: str = field(default="Colonel", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


# ============================================================================
# FLAG OFFICER RANKS
# ============================================================================

@dataclass
class Brigadier(AlienPower):
    """Brigadier - Power of Brigade. Division command."""
    name: str = field(default="Brigadier", init=False)
    description: str = field(default="+2 per foreign colony (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(6, colonies * 2)
        return base_total


@dataclass
class Major_General(AlienPower):
    """Major_General - Power of Division. High command."""
    name: str = field(default="Major_General", init=False)
    description: str = field(default="+5 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    used: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and not self.used:
            if random.random() < 0.3:
                self.used = True
                return base_total + 5
        return base_total


@dataclass
class Lieutenant_General(AlienPower):
    """Lieutenant_General - Power of Corps. Strategic command."""
    name: str = field(default="Lieutenant_General", init=False)
    description: str = field(default="+4 after turn 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 10:
            return base_total + 4
        return base_total


@dataclass
class General_Rank(AlienPower):
    """General_Rank - Power of Army. Supreme command."""
    name: str = field(default="General_Rank", init=False)
    description: str = field(default="+5 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Field_Marshal(AlienPower):
    """Field_Marshal - Power of Theater. War command."""
    name: str = field(default="Field_Marshal", init=False)
    description: str = field(default="+6 in late game (turn 15+).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn >= 15:
            return base_total + 6
        return base_total


@dataclass
class Supreme_Commander(AlienPower):
    """Supreme_Commander - Power of Supreme. Absolute command."""
    name: str = field(default="Supreme_Commander", init=False)
    description: str = field(default="+3 and +1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        bonus = 3
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + bonus + allies


# Register all military rank powers
MILITARY_RANK_POWERS = [
    Private, Corporal, Sergeant, Staff_Sergeant,
    Warrant_Officer, Master_Sergeant, First_Sergeant, Sergeant_Major,
    Lieutenant, Captain_Rank, Major, Colonel,
    Brigadier, Major_General, Lieutenant_General, General_Rank,
    Field_Marshal, Supreme_Commander,
]


# Auto-register all powers
for power_class in MILITARY_RANK_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
