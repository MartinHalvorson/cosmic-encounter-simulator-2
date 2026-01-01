"""
Gambling Powers - Aliens with risk and chance abilities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class AllIn(AlienPower):
    """
    AllIn - Risk Everything.
    Double or nothing.
    """
    name: str = field(default="AllIn", init=False)
    description: str = field(default="Double or nothing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Bettor(AlienPower):
    """
    Bettor - Make Bets.
    Wager on outcomes.
    """
    name: str = field(default="Bettor", init=False)
    description: str = field(default="Wager outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bluffer_Alt(AlienPower):
    """
    Bluffer_Alt - Fake Hand.
    Pretend higher card.
    """
    name: str = field(default="Bluffer_Alt", init=False)
    description: str = field(default="Fake high.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cardsharp(AlienPower):
    """
    Cardsharp - Skilled Player.
    +3 card bonus.
    """
    name: str = field(default="Cardsharp", init=False)
    description: str = field(default="+3 card bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 card bonus."""
        return total + 3


@dataclass
class Casino(AlienPower):
    """
    Casino - House Advantage.
    Win ties.
    """
    name: str = field(default="Casino", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dealer_Alt(AlienPower):
    """
    Dealer_Alt - Deal Cards.
    Control card flow.
    """
    name: str = field(default="Dealer_Alt", init=False)
    description: str = field(default="Control cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Diceroller(AlienPower):
    """
    Diceroller - Roll Dice.
    Random 1-6 bonus.
    """
    name: str = field(default="Diceroller", init=False)
    description: str = field(default="Random 1-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add random 1-6."""
        return total + random.randint(1, 6)


@dataclass
class Gambler_Alt(AlienPower):
    """
    Gambler_Alt - Take Chances.
    Risk for reward.
    """
    name: str = field(default="Gambler_Alt", init=False)
    description: str = field(default="Risk reward.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Highroller(AlienPower):
    """
    Highroller - Big Stakes.
    +5 when ahead.
    """
    name: str = field(default="Highroller", init=False)
    description: str = field(default="+5 when ahead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jackpot(AlienPower):
    """
    Jackpot - Big Win.
    Rare huge bonus.
    """
    name: str = field(default="Jackpot", init=False)
    description: str = field(default="Rare +10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """10% chance of +10 bonus."""
        if random.random() < 0.1:
            return total + 10
        return total


@dataclass
class Pokerface(AlienPower):
    """
    Pokerface - Hide Intent.
    Opponents can't see.
    """
    name: str = field(default="Pokerface", init=False)
    description: str = field(default="Hide info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shuffler(AlienPower):
    """
    Shuffler - Mix Cards.
    Randomize hands.
    """
    name: str = field(default="Shuffler", init=False)
    description: str = field(default="Randomize.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(AllIn())
AlienRegistry.register(Bettor())
AlienRegistry.register(Bluffer_Alt())
AlienRegistry.register(Cardsharp())
AlienRegistry.register(Casino())
AlienRegistry.register(Dealer_Alt())
AlienRegistry.register(Diceroller())
AlienRegistry.register(Gambler_Alt())
AlienRegistry.register(Highroller())
AlienRegistry.register(Jackpot())
AlienRegistry.register(Pokerface())
AlienRegistry.register(Shuffler())
