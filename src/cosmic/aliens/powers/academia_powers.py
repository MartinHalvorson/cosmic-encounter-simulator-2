"""
Academia themed alien powers for Cosmic Encounter.

Powers themed around education, research, and academic pursuits.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# EDUCATORS
# ============================================================================

@dataclass
class Professor(AlienPower):
    """Professor - Power of Knowledge. Draw extra cards on win."""
    name: str = field(default="Professor", init=False)
    description: str = field(default="Draw 1 extra card when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lecturer(AlienPower):
    """Lecturer - Power of Teaching. Allies get +1 each."""
    name: str = field(default="Lecturer", init=False)
    description: str = field(default="Each ally gets +1 to their contribution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tutor(AlienPower):
    """Tutor - Power of Guidance. Help allies succeed."""
    name: str = field(default="Tutor", init=False)
    description: str = field(default="Allies may use your card value instead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dean(AlienPower):
    """Dean - Power of Administration. Control encounter flow."""
    name: str = field(default="Dean", init=False)
    description: str = field(default="Once per game, skip planning phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    used: bool = False


# ============================================================================
# RESEARCHERS
# ============================================================================

@dataclass
class Scientist(AlienPower):
    """Scientist - Power of Discovery. Look at more cards."""
    name: str = field(default="Scientist", init=False)
    description: str = field(default="See top 3 cards of deck when drawing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Researcher(AlienPower):
    """Researcher - Power of Study. Gain knowledge over time."""
    name: str = field(default="Researcher", init=False)
    description: str = field(default="+1 for each turn that has passed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class Analyst(AlienPower):
    """Analyst - Power of Data. Better predictions."""
    name: str = field(default="Analyst", init=False)
    description: str = field(default="See opponent's card before choosing yours.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Theorist(AlienPower):
    """Theorist - Power of Theory. Bonus for predictions."""
    name: str = field(default="Theorist", init=False)
    description: str = field(default="+4 if you correctly predict opponent's card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# STUDENTS
# ============================================================================

@dataclass
class Student(AlienPower):
    """Student - Power of Learning. Improve from losses."""
    name: str = field(default="Student", init=False)
    description: str = field(default="+2 for each loss this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    losses: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (self.losses * 2)
        return base_total


@dataclass
class Graduate(AlienPower):
    """Graduate - Power of Completion. Bonus late game."""
    name: str = field(default="Graduate", init=False)
    description: str = field(default="+5 after turn 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 10:
            return base_total + 5
        return base_total


@dataclass
class Freshman(AlienPower):
    """Freshman - Power of Beginnings. Strong early game."""
    name: str = field(default="Freshman", init=False)
    description: str = field(default="+4 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 4
        return base_total


@dataclass
class Dropout(AlienPower):
    """Dropout - Power of Quitting. Retreat safely."""
    name: str = field(default="Dropout", init=False)
    description: str = field(default="May retreat ships before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# DISCIPLINES
# ============================================================================

@dataclass
class Mathematician(AlienPower):
    """Mathematician - Power of Numbers. Precise calculations."""
    name: str = field(default="Mathematician", init=False)
    description: str = field(default="Know exact totals before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Historian(AlienPower):
    """Historian - Power of the Past. Use discarded cards."""
    name: str = field(default="Historian", init=False)
    description: str = field(default="May play card from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Philosopher(AlienPower):
    """Philosopher - Power of Thought. Contemplative advantage."""
    name: str = field(default="Philosopher", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Linguist(AlienPower):
    """Linguist - Power of Language. Better negotiations."""
    name: str = field(default="Linguist", init=False)
    description: str = field(default="Negotiations give double rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Librarian(AlienPower):
    """Librarian - Power of Archives. Access stored information."""
    name: str = field(default="Librarian", init=False)
    description: str = field(default="Look at any player's hand once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Biologist(AlienPower):
    """Biologist - Power of Life. Ships regenerate."""
    name: str = field(default="Biologist", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Physicist(AlienPower):
    """Physicist - Power of Forces. Manipulate ship counts."""
    name: str = field(default="Physicist", init=False)
    description: str = field(default="Move 1 ship between planets before encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chemist(AlienPower):
    """Chemist - Power of Reactions. Transform cards."""
    name: str = field(default="Chemist", init=False)
    description: str = field(default="Once per encounter, change card value by ±3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all academia powers
ACADEMIA_POWERS = [
    Professor, Lecturer, Tutor, Dean,
    Scientist, Researcher, Analyst, Theorist,
    Student, Graduate, Freshman, Dropout,
    Mathematician, Historian, Philosopher, Linguist,
    Librarian, Biologist, Physicist, Chemist,
]


# Auto-register all powers
for power_class in ACADEMIA_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
