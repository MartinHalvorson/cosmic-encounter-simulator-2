"""
Sports Powers for Cosmic Encounter.

Aliens inspired by various sports and athletic activities.
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
# TEAM SPORTS
# ============================================================================

@dataclass
class Quarterback(AlienPower):
    """Quarterback - Power of the Pass. Send ships to allies."""
    name: str = field(default="Quarterback", init=False)
    description: str = field(default="Send ships to help allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goalkeeper(AlienPower):
    """Goalkeeper - Power of Blocking. +5 when defending."""
    name: str = field(default="Goalkeeper", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Pitcher(AlienPower):
    """Pitcher - Power of Throwing. +3 when attacking."""
    name: str = field(default="Pitcher", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Catcher(AlienPower):
    """Catcher - Power of Receiving. Take cards from opponents."""
    name: str = field(default="Catcher", init=False)
    description: str = field(default="Take 1 random card from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class PointGuard(AlienPower):
    """PointGuard - Power of Assists. Allies get +2."""
    name: str = field(default="PointGuard", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# INDIVIDUAL SPORTS
# ============================================================================

@dataclass
class Sprinter(AlienPower):
    """Sprinter - Power of Speed. Extra encounter on fast wins."""
    name: str = field(default="Sprinter", init=False)
    description: str = field(default="Extra encounter on quick wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Marathon(AlienPower):
    """Marathon - Power of Endurance. +1 for each encounter this turn."""
    name: str = field(default="Marathon", init=False)
    description: str = field(default="+1 per encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            encounter_count = getattr(game.logger, 'encounter_count', 0) if hasattr(game, 'logger') else 0
            return base_total + encounter_count
        return base_total


@dataclass
class Swimmer(AlienPower):
    """Swimmer - Power of Fluidity. Ships return from warp faster."""
    name: str = field(default="Swimmer", init=False)
    description: str = field(default="Retrieve 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(min(2, player.ships_in_warp))


@dataclass
class Gymnast(AlienPower):
    """Gymnast - Power of Flexibility. Change card after reveal."""
    name: str = field(default="Gymnast", init=False)
    description: str = field(default="Swap card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Archer_Sport(AlienPower):
    """Archer - Power of Precision. Win ties."""
    name: str = field(default="Archer_Sport", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# COMBAT SPORTS
# ============================================================================

@dataclass
class Boxer(AlienPower):
    """Boxer - Power of Striking. +4 on attack, -2 on defense."""
    name: str = field(default="Boxer", init=False)
    description: str = field(default="+4 attack, -2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 4
        return base_total - 2


@dataclass
class Wrestler(AlienPower):
    """Wrestler - Power of Grappling. Opponent's allies can't help."""
    name: str = field(default="Wrestler", init=False)
    description: str = field(default="Block opponent's allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fencer(AlienPower):
    """Fencer - Power of Precision. +2 for each card in hand."""
    name: str = field(default="Fencer", init=False)
    description: str = field(default="+1 per 3 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (len(player.hand) // 3)
        return base_total


@dataclass
class MartialArtist(AlienPower):
    """MartialArtist - Power of Discipline. Ships worth double."""
    name: str = field(default="MartialArtist", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count * 2
        return base_count


@dataclass
class Judoka(AlienPower):
    """Judoka - Power of Redirection. Use opponent's strength."""
    name: str = field(default="Judoka", init=False)
    description: str = field(default="Use opponent's ships as bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# WINTER SPORTS
# ============================================================================

@dataclass
class Skier(AlienPower):
    """Skier - Power of Descent. +3 when attacking downhill."""
    name: str = field(default="Skier", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skater(AlienPower):
    """Skater - Power of Grace. Move ships freely between colonies."""
    name: str = field(default="Skater", init=False)
    description: str = field(default="Free ship movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Snowboarder(AlienPower):
    """Snowboarder - Power of Style. Draw card when winning with style."""
    name: str = field(default="Snowboarder", init=False)
    description: str = field(default="Draw 1 card on big wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Curler(AlienPower):
    """Curler - Power of Strategy. See opponent's card before playing."""
    name: str = field(default="Curler", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bobsledder(AlienPower):
    """Bobsledder - Power of Teamwork. +1 for each ally."""
    name: str = field(default="Bobsledder", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Quarterback, Goalkeeper, Pitcher, Catcher, PointGuard,
    Sprinter, Marathon, Swimmer, Gymnast, Archer_Sport,
    Boxer, Wrestler, Fencer, MartialArtist, Judoka,
    Skier, Skater, Snowboarder, Curler, Bobsledder,
]:
    AlienRegistry.register(alien_class())
