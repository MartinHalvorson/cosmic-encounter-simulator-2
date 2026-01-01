"""
Gaming Alternative Powers for Cosmic Encounter.

More aliens inspired by games, puzzles, and entertainment.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Poker(AlienPower):
    """
    Poker - Power to Bluff.
    You may play any card face-down; if opponent guesses wrong type, you win.
    """
    name: str = field(default="Poker", init=False)
    description: str = field(
        default="Win if opponent guesses wrong card type.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chess(AlienPower):
    """
    Chess - Power to Plan.
    You may see opponent's card before playing yours.
    """
    name: str = field(default="Chess", init=False)
    description: str = field(
        default="See opponent's card before playing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Dominoes(AlienPower):
    """
    Dominoes - Power of Chain.
    When you win, you may immediately attack an adjacent planet.
    """
    name: str = field(default="Dominoes", init=False)
    description: str = field(
        default="Attack adjacent planet after winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Checkers(AlienPower):
    """
    Checkers - Power to Jump.
    Your ships may jump over opponent ships during launch.
    """
    name: str = field(default="Checkers", init=False)
    description: str = field(
        default="Jump over opponent ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monopolist_Game(AlienPower):
    """
    Monopolist_Game - Power to Own.
    +2 for each planet you control exclusively.
    """
    name: str = field(default="Monopolist_Game", init=False)
    description: str = field(
        default="+2 per exclusive planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scrabble(AlienPower):
    """
    Scrabble - Power of Words.
    Your hand size limit is increased by 3.
    """
    name: str = field(default="Scrabble", init=False)
    description: str = field(
        default="Hand size +3.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Roulette(AlienPower):
    """
    Roulette - Power of Spin.
    Once per encounter, roll a die; add the result to your total.
    """
    name: str = field(default="Roulette", init=False)
    description: str = field(
        default="Add random 1-6 to total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blackjack(AlienPower):
    """
    Blackjack - Power of 21.
    If your total is exactly 21, you automatically win.
    """
    name: str = field(default="Blackjack", init=False)
    description: str = field(
        default="Win automatically if total is 21.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Puzzle(AlienPower):
    """
    Puzzle - Power to Solve.
    +3 when you have fewer cards than opponent.
    """
    name: str = field(default="Puzzle", init=False)
    description: str = field(
        default="+3 with fewer cards than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trivia(AlienPower):
    """
    Trivia - Power to Know.
    At start of turn, look at any player's hand.
    """
    name: str = field(default="Trivia", init=False)
    description: str = field(
        default="View one player's hand each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Arcade_Game(AlienPower):
    """
    Arcade_Game - Power to Score.
    Gain +1 for each encounter you've won this game.
    """
    name: str = field(default="Arcade_Game", init=False)
    description: str = field(
        default="+1 per past win (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pinball(AlienPower):
    """
    Pinball - Power to Bounce.
    Ships sent to warp bounce back to any of your colonies.
    """
    name: str = field(default="Pinball", init=False)
    description: str = field(
        default="Ships bounce back from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tetris(AlienPower):
    """
    Tetris - Power to Fit.
    You may stack up to 6 ships on any planet (instead of 4).
    """
    name: str = field(default="Tetris", init=False)
    description: str = field(
        default="Stack up to 6 ships per planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crossword(AlienPower):
    """
    Crossword - Power to Intersect.
    +2 for each other player you share a planet with.
    """
    name: str = field(default="Crossword", init=False)
    description: str = field(
        default="+2 per shared planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mahjong(AlienPower):
    """
    Mahjong - Power of Matching.
    When you play an attack card, draw another card of same value if you have one.
    """
    name: str = field(default="Mahjong", init=False)
    description: str = field(
        default="Matching attack card draws extra.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all gaming alt powers
AlienRegistry.register(Poker())
AlienRegistry.register(Chess())
AlienRegistry.register(Dominoes())
AlienRegistry.register(Checkers())
AlienRegistry.register(Monopolist_Game())
AlienRegistry.register(Scrabble())
AlienRegistry.register(Roulette())
AlienRegistry.register(Blackjack())
AlienRegistry.register(Puzzle())
AlienRegistry.register(Trivia())
AlienRegistry.register(Arcade_Game())
AlienRegistry.register(Pinball())
AlienRegistry.register(Tetris())
AlienRegistry.register(Crossword())
AlienRegistry.register(Mahjong())
