"""
Board Game themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Monopoly(AlienPower):
    """Monopoly - Power of Ownership."""
    name: str = field(default="Monopoly", init=False)
    description: str = field(default="+2 for each planet you control alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Risk_Game(AlienPower):
    """Risk - Power of Territory."""
    name: str = field(default="Risk_Game", init=False)
    description: str = field(default="+1 for each adjacent controlled planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chess_Game(AlienPower):
    """Chess - Power of Strategy."""
    name: str = field(default="Chess_Game", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scrabble(AlienPower):
    """Scrabble - Power of Words."""
    name: str = field(default="Scrabble", init=False)
    description: str = field(default="+1 for each card type in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clue_Game(AlienPower):
    """Clue - Power of Deduction."""
    name: str = field(default="Clue_Game", init=False)
    description: str = field(default="Reveal one card from any hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Catan(AlienPower):
    """Catan - Power of Trade."""
    name: str = field(default="Catan", init=False)
    description: str = field(default="Trade cards before encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pandemic(AlienPower):
    """Pandemic - Power of Cooperation."""
    name: str = field(default="Pandemic", init=False)
    description: str = field(default="+2 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dominion_Game(AlienPower):
    """Dominion - Power of Building."""
    name: str = field(default="Dominion_Game", init=False)
    description: str = field(default="Draw extra card per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Poker_Game(AlienPower):
    """Poker - Power of Bluffing."""
    name: str = field(default="Poker_Game", init=False)
    description: str = field(default="Bluff card type once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Battleship(AlienPower):
    """Battleship - Power of Positioning."""
    name: str = field(default="Battleship", init=False)
    description: str = field(default="+3 when ships are hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Checkers(AlienPower):
    """Checkers - Power of Jumping."""
    name: str = field(default="Checkers", init=False)
    description: str = field(default="Skip over blocked planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Backgammon(AlienPower):
    """Backgammon - Power of Movement."""
    name: str = field(default="Backgammon", init=False)
    description: str = field(default="Move ships freely between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Monopoly())
AlienRegistry.register(Risk_Game())
AlienRegistry.register(Chess_Game())
AlienRegistry.register(Scrabble())
AlienRegistry.register(Clue_Game())
AlienRegistry.register(Catan())
AlienRegistry.register(Pandemic())
AlienRegistry.register(Dominion_Game())
AlienRegistry.register(Poker_Game())
AlienRegistry.register(Battleship())
AlienRegistry.register(Checkers())
AlienRegistry.register(Backgammon())
