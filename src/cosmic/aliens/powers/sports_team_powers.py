"""
Sports Team Powers for Cosmic Encounter.

Aliens inspired by team sports and athletic themes.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Quarterback(AlienPower):
    """Quarterback - Power of Leadership. +2 per ally in encounter."""
    name: str = field(default="Quarterback", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goalkeeper(AlienPower):
    """Goalkeeper - Power of Blocking. +4 on defense."""
    name: str = field(default="Goalkeeper", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Striker(AlienPower):
    """Striker - Power of Scoring. +4 on offense."""
    name: str = field(default="Striker", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Pitcher(AlienPower):
    """Pitcher - Power of Throwing. Send 1 opponent ship to warp."""
    name: str = field(default="Pitcher", init=False)
    description: str = field(default="Send 1 ship to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Batter(AlienPower):
    """Batter - Power of Hitting. +3 always."""
    name: str = field(default="Batter", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Center(AlienPower):
    """Center - Power of Height. Ships count as 1.5 each."""
    name: str = field(default="Center", init=False)
    description: str = field(default="Ships count as 1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Point_Guard(AlienPower):
    """Point_Guard - Power of Passing. Allies get +1 each."""
    name: str = field(default="Point_Guard", init=False)
    description: str = field(default="Allies get +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Defenseman(AlienPower):
    """Defenseman - Power of Defense. +3 on defense."""
    name: str = field(default="Defenseman", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Midfielder(AlienPower):
    """Midfielder - Power of Balance. +2 always."""
    name: str = field(default="Midfielder", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Catcher(AlienPower):
    """Catcher - Power of Catching. Draw 1 card when winning on defense."""
    name: str = field(default="Catcher", init=False)
    description: str = field(default="Draw 1 card on defense win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coach(AlienPower):
    """Coach - Power of Strategy. See opponent's card before choosing."""
    name: str = field(default="Coach", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Referee(AlienPower):
    """Referee - Power of Rules. Win ties automatically."""
    name: str = field(default="Referee", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cheerleader(AlienPower):
    """Cheerleader - Power of Support. Allies get +2 each."""
    name: str = field(default="Cheerleader", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Captain(AlienPower):
    """Captain - Power of Leadership. +1 per ship in encounter."""
    name: str = field(default="Captain", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class MVP(AlienPower):
    """MVP - Power of Excellence. +4 when at 3+ colonies."""
    name: str = field(default="MVP", init=False)
    description: str = field(default="+4 at 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 4
        return total


# Register all sports team powers
AlienRegistry.register(Quarterback())
AlienRegistry.register(Goalkeeper())
AlienRegistry.register(Striker())
AlienRegistry.register(Pitcher())
AlienRegistry.register(Batter())
AlienRegistry.register(Center())
AlienRegistry.register(Point_Guard())
AlienRegistry.register(Defenseman())
AlienRegistry.register(Midfielder())
AlienRegistry.register(Catcher())
AlienRegistry.register(Coach())
AlienRegistry.register(Referee())
AlienRegistry.register(Cheerleader())
AlienRegistry.register(Captain())
AlienRegistry.register(MVP())
