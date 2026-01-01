"""
Card Game Powers for Cosmic Encounter.

Aliens inspired by card games and playing card themes.
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
class Ace(AlienPower):
    """Ace - Power of High. +5 when playing highest card in hand."""
    name: str = field(default="Ace", init=False)
    description: str = field(default="+5 with highest card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class King_Card(AlienPower):
    """King_Card - Power of Royalty. +4 on offense."""
    name: str = field(default="King_Card", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Queen_Card(AlienPower):
    """Queen_Card - Power of Grace. +3 on defense."""
    name: str = field(default="Queen_Card", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Jack_Card(AlienPower):
    """Jack_Card - Power of Tricks. May swap cards with opponent after reveal."""
    name: str = field(default="Jack_Card", init=False)
    description: str = field(default="Swap cards after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Joker_Card(AlienPower):
    """Joker_Card - Power of Wild. Copy opponent's card value."""
    name: str = field(default="Joker_Card", init=False)
    description: str = field(default="Copy opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dealer(AlienPower):
    """Dealer - Power of Cards. Draw 2 cards at turn start."""
    name: str = field(default="Dealer", init=False)
    description: str = field(default="Draw 2 cards at start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shuffler(AlienPower):
    """Shuffler - Power of Randomness. Opponent draws random card from hand."""
    name: str = field(default="Shuffler", init=False)
    description: str = field(default="Opponent plays random card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gambler_Card(AlienPower):
    """Gambler_Card - Power of Risk. +6 or -3 randomly."""
    name: str = field(default="Gambler_Card", init=False)
    description: str = field(default="+6 or -3 randomly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bluffer(AlienPower):
    """Bluffer - Power of Deception. Play cards face-down initially."""
    name: str = field(default="Bluffer", init=False)
    description: str = field(default="Hidden card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Counter(AlienPower):
    """Counter - Power of Counting. +1 per card in hand."""
    name: str = field(default="Counter", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Full_House(AlienPower):
    """Full_House - Power of Sets. +3 when at 3+ colonies."""
    name: str = field(default="Full_House", init=False)
    description: str = field(default="+3 at 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 3
        return total


@dataclass
class Flush(AlienPower):
    """Flush - Power of Suits. Win ties automatically."""
    name: str = field(default="Flush", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Straight(AlienPower):
    """Straight - Power of Sequence. +2 for each encounter this turn."""
    name: str = field(default="Straight", init=False)
    description: str = field(default="+2 per encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + (game.encounter_number * 2)
        return total


@dataclass
class Fold(AlienPower):
    """Fold - Power of Retreat. Withdraw without losing ships."""
    name: str = field(default="Fold", init=False)
    description: str = field(default="Retreat safely.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class All_In(AlienPower):
    """All_In - Power of Commitment. +4 when committing 4 ships."""
    name: str = field(default="All_In", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all card game powers
AlienRegistry.register(Ace())
AlienRegistry.register(King_Card())
AlienRegistry.register(Queen_Card())
AlienRegistry.register(Jack_Card())
AlienRegistry.register(Joker_Card())
AlienRegistry.register(Dealer())
AlienRegistry.register(Shuffler())
AlienRegistry.register(Gambler_Card())
AlienRegistry.register(Bluffer())
AlienRegistry.register(Counter())
AlienRegistry.register(Full_House())
AlienRegistry.register(Flush())
AlienRegistry.register(Straight())
AlienRegistry.register(Fold())
AlienRegistry.register(All_In())
