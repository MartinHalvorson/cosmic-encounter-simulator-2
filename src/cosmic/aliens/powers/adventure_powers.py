"""
Adventure themed alien powers for Cosmic Encounter.

Powers based on adventure, exploration, and heroic quests.
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
# ADVENTURER TYPES
# ============================================================================

@dataclass
class Explorer_Adv(AlienPower):
    """Explorer_Adv - Power of Discovery. Find new opportunities."""
    name: str = field(default="Explorer_Adv", init=False)
    description: str = field(default="+2 when attacking new planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 2
        return base_total


@dataclass
class Treasure_Hunter(AlienPower):
    """Treasure_Hunter - Power of Riches. Gain extra cards."""
    name: str = field(default="Treasure_Hunter", init=False)
    description: str = field(default="Draw 2 cards on successful attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pathfinder(AlienPower):
    """Pathfinder - Power of Guidance. Know the way."""
    name: str = field(default="Pathfinder", init=False)
    description: str = field(default="See destiny before it's drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ranger(AlienPower):
    """Ranger - Power of the Wild. Bonus in territory."""
    name: str = field(default="Ranger", init=False)
    description: str = field(default="+3 when defending your colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Cartographer(AlienPower):
    """Cartographer - Power of Mapping. Know the layout."""
    name: str = field(default="Cartographer", init=False)
    description: str = field(default="See all players' colony counts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Questor(AlienPower):
    """Questor - Power of Purpose. Goal-oriented bonus."""
    name: str = field(default="Questor", init=False)
    description: str = field(default="+2 per foreign colony (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(8, colonies * 2)
        return base_total


# ============================================================================
# DUNGEON DELVERS
# ============================================================================

@dataclass
class Delver(AlienPower):
    """Delver - Power of Depths. Bonus when outnumbered."""
    name: str = field(default="Delver", init=False)
    description: str = field(default="+4 when you have fewer ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            opp_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
        if my_ships < opp_ships:
            return base_total + 4
        return base_total


@dataclass
class Trapspringer(AlienPower):
    """Trapspringer - Power of Avoidance. Avoid penalties."""
    name: str = field(default="Trapspringer", init=False)
    description: str = field(default="Ignore opponent's first card effect.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lockpicker(AlienPower):
    """Lockpicker - Power of Access. Open any door."""
    name: str = field(default="Lockpicker", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Torchbearer(AlienPower):
    """Torchbearer - Power of Light. See through deception."""
    name: str = field(default="Torchbearer", init=False)
    description: str = field(default="See opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# EXPEDITION ROLES
# ============================================================================

@dataclass
class Guide(AlienPower):
    """Guide - Power of Leadership. Help allies."""
    name: str = field(default="Guide", init=False)
    description: str = field(default="Allied ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chronicler(AlienPower):
    """Chronicler - Power of Records. Learn from history."""
    name: str = field(default="Chronicler", init=False)
    description: str = field(default="+1 per encounter this game (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    encounters: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            self.encounters += 1
            return base_total + min(8, self.encounters)
        return base_total


@dataclass
class Survivalist(AlienPower):
    """Survivalist - Power of Endurance. Thrive in adversity."""
    name: str = field(default="Survivalist", init=False)
    description: str = field(default="+3 when you have 0-1 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies <= 1:
                return base_total + 3
        return base_total


@dataclass
class Mountaineer(AlienPower):
    """Mountaineer - Power of Climbing. Overcome obstacles."""
    name: str = field(default="Mountaineer", init=False)
    description: str = field(default="+2 per 3 turns passed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = (game.current_turn // 3) * 2
            return base_total + min(10, bonus)
        return base_total


@dataclass
class Scout_Adv(AlienPower):
    """Scout_Adv - Power of Reconnaissance. Information gathering."""
    name: str = field(default="Scout_Adv", init=False)
    description: str = field(default="Look at top 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Expedition_Leader(AlienPower):
    """Expedition_Leader - Power of Command. Lead the group."""
    name: str = field(default="Expedition_Leader", init=False)
    description: str = field(default="+1 per ally (max +5).", init=False)
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
        return base_total + min(5, allies)


# ============================================================================
# QUEST ITEMS
# ============================================================================

@dataclass
class Compass_Bearer(AlienPower):
    """Compass_Bearer - Power of Direction. Never lost."""
    name: str = field(default="Compass_Bearer", init=False)
    description: str = field(default="Always know optimal attack target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Map_Holder(AlienPower):
    """Map_Holder - Power of Knowledge. Know the territory."""
    name: str = field(default="Map_Holder", init=False)
    description: str = field(default="+2 for each foreign colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Key_Keeper(AlienPower):
    """Key_Keeper - Power of Access. Unlock potential."""
    name: str = field(default="Key_Keeper", init=False)
    description: str = field(default="Your cards get +1 value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all adventure powers
ADVENTURE_POWERS = [
    Explorer_Adv, Treasure_Hunter, Pathfinder, Ranger, Cartographer, Questor,
    Delver, Trapspringer, Lockpicker, Torchbearer,
    Guide, Chronicler, Survivalist, Mountaineer, Scout_Adv, Expedition_Leader,
    Compass_Bearer, Map_Holder, Key_Keeper,
]


# Auto-register all powers
for power_class in ADVENTURE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
