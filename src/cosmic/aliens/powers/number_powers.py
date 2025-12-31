"""
Number Powers - Number-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class One(AlienPower):
    """One - First number. +1 always."""
    name: str = field(default="One", init=False)
    description: str = field(default="+1 to all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 1
        return total


@dataclass
class Two(AlienPower):
    """Two - Double. Ships count double."""
    name: str = field(default="Two", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Three(AlienPower):
    """Three - Triple. +3 when attacking."""
    name: str = field(default="Three", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Four(AlienPower):
    """Four - Quadruple. +4 when defending."""
    name: str = field(default="Four", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Five(AlienPower):
    """Five - Quintuple. +5 on first encounter."""
    name: str = field(default="Five", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 5
        return total


@dataclass
class Six(AlienPower):
    """Six - Hex. -3 to opponent's total."""
    name: str = field(default="Six", init=False)
    description: str = field(default="-3 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Seven(AlienPower):
    """Seven - Lucky. Win ties."""
    name: str = field(default="Seven", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eight(AlienPower):
    """Eight - Octuple. Launch up to 8 ships."""
    name: str = field(default="Eight", init=False)
    description: str = field(default="Launch up to 8 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nine(AlienPower):
    """Nine - Near ten. +2 per home colony."""
    name: str = field(default="Nine", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + (home_count * 2)
        return total


@dataclass
class Ten(AlienPower):
    """Ten - Perfect score. +10 when ahead in colonies."""
    name: str = field(default="Ten", init=False)
    description: str = field(default="+10 when leading.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Zero(AlienPower):
    """Zero - Nothing. Opponent's kickers don't work."""
    name: str = field(default="Zero", init=False)
    description: str = field(default="Ignore opponent's kickers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dozen(AlienPower):
    """Dozen - Twelve. +1 per card in hand."""
    name: str = field(default="Dozen", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Hundred(AlienPower):
    """Hundred - Century. Draw 2 cards when winning."""
    name: str = field(default="Hundred", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Infinity(AlienPower):
    """Infinity - Endless. Retrieve all ships from warp."""
    name: str = field(default="Infinity", init=False)
    description: str = field(default="Retrieve all ships on turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Prime(AlienPower):
    """Prime - Special number. +1 per ship committed."""
    name: str = field(default="Prime", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(One())
AlienRegistry.register(Two())
AlienRegistry.register(Three())
AlienRegistry.register(Four())
AlienRegistry.register(Five())
AlienRegistry.register(Six())
AlienRegistry.register(Seven())
AlienRegistry.register(Eight())
AlienRegistry.register(Nine())
AlienRegistry.register(Ten())
AlienRegistry.register(Zero())
AlienRegistry.register(Dozen())
AlienRegistry.register(Hundred())
AlienRegistry.register(Infinity())
AlienRegistry.register(Prime())
