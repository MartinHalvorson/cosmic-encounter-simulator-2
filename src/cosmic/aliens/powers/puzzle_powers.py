"""
Puzzle and game-themed alien powers for Cosmic Encounter.

Powers inspired by puzzles, games, and logical thinking.
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
class Jigsaw(AlienPower):
    """Jigsaw - Power of Pieces. Assemble strength."""
    name: str = field(default="Jigsaw", init=False)
    description: str = field(default="+1 per colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + colonies
        return base_total


@dataclass
class Crossword(AlienPower):
    """Crossword - Power of Intersection. Connect points."""
    name: str = field(default="Crossword", init=False)
    description: str = field(default="+2 per ally.", init=False)
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
        return base_total + (allies * 2)


@dataclass
class Sudoku(AlienPower):
    """Sudoku - Power of Numbers. Calculate advantage."""
    name: str = field(default="Sudoku", init=False)
    description: str = field(default="+3 with exactly 3 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships == 3:
            return base_total + 3
        return base_total


@dataclass
class Rubiks(AlienPower):
    """Rubiks - Power of Complexity. Twisted logic."""
    name: str = field(default="Rubiks", init=False)
    description: str = field(default="+2 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, game.current_turn * 2)
            return base_total + bonus
        return base_total


@dataclass
class Maze(AlienPower):
    """Maze - Power of Paths. Navigate complexity."""
    name: str = field(default="Maze", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Riddle(AlienPower):
    """Riddle - Power of Mystery. Confuse opponents."""
    name: str = field(default="Riddle", init=False)
    description: str = field(default="Opponent reveals card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chess_Puzzle(AlienPower):
    """Chess_Puzzle - Power of Strategy. Think ahead."""
    name: str = field(default="Chess_Puzzle", init=False)
    description: str = field(default="+3 when at more colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            if my_colonies > opp_colonies:
                return base_total + 3
        return base_total


@dataclass
class Domino(AlienPower):
    """Domino - Power of Chain. Consecutive strength."""
    name: str = field(default="Domino", init=False)
    description: str = field(default="+3 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 2:
            return base_total + 3
        return base_total


@dataclass
class Tetris(AlienPower):
    """Tetris - Power of Fitting. Efficient placement."""
    name: str = field(default="Tetris", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships == 4:
            return base_total + 4
        return base_total


@dataclass
class Trivia(AlienPower):
    """Trivia - Power of Knowledge. Information advantage."""
    name: str = field(default="Trivia", init=False)
    description: str = field(default="+1 per card more than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            diff = player.hand_size() - opponent.hand_size()
            if diff > 0:
                return base_total + diff
        return base_total


@dataclass
class Scrabble(AlienPower):
    """Scrabble - Power of Words. Spell out victory."""
    name: str = field(default="Scrabble", init=False)
    description: str = field(default="+2 per card in hand (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, player.hand_size() * 2)
            return base_total + bonus
        return base_total


@dataclass
class Mystery(AlienPower):
    """Mystery - Power of Unknown. Hidden strength."""
    name: str = field(default="Mystery", init=False)
    description: str = field(default="Card values +5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Logic(AlienPower):
    """Logic - Power of Reason. Clear thinking."""
    name: str = field(default="Logic", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Cipher(AlienPower):
    """Cipher - Power of Code. Hidden information."""
    name: str = field(default="Cipher", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all puzzle powers
PUZZLE_POWERS = [
    Jigsaw, Crossword, Sudoku, Rubiks, Maze,
    Riddle, Chess_Puzzle, Domino, Tetris, Trivia,
    Scrabble, Mystery, Logic, Cipher,
]

for power_class in PUZZLE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
