"""
Time Travel Powers for Cosmic Encounter.

Aliens inspired by time travel and temporal manipulation themes.
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
class Chronologist(AlienPower):
    """Chronologist - Power of Timing. +1 per turn game has lasted."""
    name: str = field(default="Chronologist", init=False)
    description: str = field(default="+1 per game turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


@dataclass
class Paradox(AlienPower):
    """Paradox - Power of Contradiction. Win ties, lose non-ties."""
    name: str = field(default="Paradox", init=False)
    description: str = field(default="Win ties only.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Rewind(AlienPower):
    """Rewind - Power of Reversal. Redo the encounter once per turn."""
    name: str = field(default="Rewind", init=False)
    description: str = field(default="Redo encounter once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Fast_Forward(AlienPower):
    """Fast_Forward - Power of Speed. Take two encounters per turn."""
    name: str = field(default="Fast_Forward", init=False)
    description: str = field(default="Two encounters per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Time_Loop(AlienPower):
    """Time_Loop - Power of Repetition. Use same card twice in a row."""
    name: str = field(default="Time_Loop", init=False)
    description: str = field(default="Reuse encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Future_Sight(AlienPower):
    """Future_Sight - Power of Foresight. See opponent's card before choosing."""
    name: str = field(default="Future_Sight", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Past_Echo(AlienPower):
    """Past_Echo - Power of Memory. +2 for each encounter won previously."""
    name: str = field(default="Past_Echo", init=False)
    description: str = field(default="+2 per previous win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Temporal(AlienPower):
    """Temporal - Power of Time. +3 in all encounters."""
    name: str = field(default="Temporal", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Freeze_Frame(AlienPower):
    """Freeze_Frame - Power of Stasis. Opponent cannot invite allies."""
    name: str = field(default="Freeze_Frame", init=False)
    description: str = field(default="Block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Slow_Motion(AlienPower):
    """Slow_Motion - Power of Delay. -3 to opponent's total."""
    name: str = field(default="Slow_Motion", init=False)
    description: str = field(default="-3 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Time_Warp(AlienPower):
    """Time_Warp - Power of Distortion. Switch offense and defense cards."""
    name: str = field(default="Time_Warp", init=False)
    description: str = field(default="Switch revealed cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Age_Forward(AlienPower):
    """Age_Forward - Power of Aging. Opponent loses 1 ship before encounter."""
    name: str = field(default="Age_Forward", init=False)
    description: str = field(default="Opponent loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flashback(AlienPower):
    """Flashback - Power of Past. Retrieve card from discard pile."""
    name: str = field(default="Flashback", init=False)
    description: str = field(default="Retrieve discarded card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Eternity(AlienPower):
    """Eternity - Power of Forever. Ships return from warp immediately."""
    name: str = field(default="Eternity", init=False)
    description: str = field(default="Ships return from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Moment(AlienPower):
    """Moment - Power of Now. +5 on your turn only."""
    name: str = field(default="Moment", init=False)
    description: str = field(default="+5 on your turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


# Register all time travel powers
AlienRegistry.register(Chronologist())
AlienRegistry.register(Paradox())
AlienRegistry.register(Rewind())
AlienRegistry.register(Fast_Forward())
AlienRegistry.register(Time_Loop())
AlienRegistry.register(Future_Sight())
AlienRegistry.register(Past_Echo())
AlienRegistry.register(Temporal())
AlienRegistry.register(Freeze_Frame())
AlienRegistry.register(Slow_Motion())
AlienRegistry.register(Time_Warp())
AlienRegistry.register(Age_Forward())
AlienRegistry.register(Flashback())
AlienRegistry.register(Eternity())
AlienRegistry.register(Moment())
