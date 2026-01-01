"""
Gaming Concepts Powers for Cosmic Encounter.

Aliens inspired by video game and tabletop gaming concepts.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# RPG CONCEPTS
# ============================================================================

@dataclass
class LevelUp(AlienPower):
    """LevelUp - Power of Growth. +1 for each win."""
    name: str = field(default="LevelUp", init=False)
    description: str = field(default="+1 for each win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class ExperiencePoints(AlienPower):
    """ExperiencePoints - Power of Learning. +1 per encounter."""
    name: str = field(default="ExperiencePoints", init=False)
    description: str = field(default="+1 for each encounter this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class HealthBar(AlienPower):
    """HealthBar - Power of Vitality. Ships are resilient."""
    name: str = field(default="HealthBar", init=False)
    description: str = field(default="Save 1 ship from warp each loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Inventory(AlienPower):
    """Inventory - Power of Collection. Keep more cards."""
    name: str = field(default="Inventory", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Respawn(AlienPower):
    """Respawn - Power of Return. Ships come back from warp."""
    name: str = field(default="Respawn", init=False)
    description: str = field(default="Retrieve 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(min(2, player.ships_in_warp))


# ============================================================================
# STRATEGY CONCEPTS
# ============================================================================

@dataclass
class PowerUp(AlienPower):
    """PowerUp - Power of Enhancement. +4 once per turn."""
    name: str = field(default="PowerUp", init=False)
    description: str = field(default="+4 once per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class BossFight(AlienPower):
    """BossFight - Power of Challenge. +5 when outnumbered."""
    name: str = field(default="BossFight", init=False)
    description: str = field(default="+5 when opponent has more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Checkpoint(AlienPower):
    """Checkpoint - Power of Safety. Retry after loss."""
    name: str = field(default="Checkpoint", init=False)
    description: str = field(default="Redo encounter once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Combo(AlienPower):
    """Combo - Power of Chains. +2 for each consecutive win."""
    name: str = field(default="Combo", init=False)
    description: str = field(default="+2 per consecutive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class UltimateAbility(AlienPower):
    """UltimateAbility - Power of Finishers. +10 once per game."""
    name: str = field(default="UltimateAbility", init=False)
    description: str = field(default="+10 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ============================================================================
# MULTIPLAYER CONCEPTS
# ============================================================================

@dataclass
class TeamPlayer(AlienPower):
    """TeamPlayer - Power of Cooperation. +2 per ally."""
    name: str = field(default="TeamPlayer", init=False)
    description: str = field(default="+2 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class SoloPlayer(AlienPower):
    """SoloPlayer - Power of Independence. +4 with no allies."""
    name: str = field(default="SoloPlayer", init=False)
    description: str = field(default="+4 when no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        allies = len(game.offense_allies) if side == Side.OFFENSE else len(game.defense_allies)
        if allies == 0:
            return base_total + 4
        return base_total


@dataclass
class Leaderboard(AlienPower):
    """Leaderboard - Power of Competition. +2 per colony ahead."""
    name: str = field(default="Leaderboard", init=False)
    description: str = field(default="+2 per colony lead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Underdog(AlienPower):
    """Underdog - Power of Comeback. +3 when behind."""
    name: str = field(default="Underdog", init=False)
    description: str = field(default="+3 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class FreeForAll(AlienPower):
    """FreeForAll - Power of Chaos. Random target selection."""
    name: str = field(default="FreeForAll", init=False)
    description: str = field(default="Choose any attack target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# MECHANICS
# ============================================================================

@dataclass
class Tutorial(AlienPower):
    """Tutorial - Power of Guidance. +5 in first 3 turns."""
    name: str = field(default="Tutorial", init=False)
    description: str = field(default="+5 in first 3 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 3:
            return base_total + 5
        return base_total


@dataclass
class Endgame(AlienPower):
    """Endgame - Power of Finales. +5 after turn 10."""
    name: str = field(default="Endgame", init=False)
    description: str = field(default="+5 after turn 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 10:
            return base_total + 5
        return base_total


@dataclass
class Speedrun(AlienPower):
    """Speedrun - Power of Haste. Extra encounter on quick win."""
    name: str = field(default="Speedrun", init=False)
    description: str = field(default="Extra encounter on fast wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hardmode(AlienPower):
    """Hardmode - Power of Difficulty. Double rewards and risks."""
    name: str = field(default="Hardmode", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count * 2
        return base_count


@dataclass
class NewGamePlus(AlienPower):
    """NewGamePlus - Power of Mastery. Carry over bonuses."""
    name: str = field(default="NewGamePlus", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


# Register all aliens
for alien_class in [
    LevelUp, ExperiencePoints, HealthBar, Inventory, Respawn,
    PowerUp, BossFight, Checkpoint, Combo, UltimateAbility,
    TeamPlayer, SoloPlayer, Leaderboard, Underdog, FreeForAll,
    Tutorial, Endgame, Speedrun, Hardmode, NewGamePlus,
]:
    AlienRegistry.register(alien_class())
