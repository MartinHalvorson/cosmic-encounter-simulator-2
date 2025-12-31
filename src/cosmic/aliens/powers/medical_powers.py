"""
Medical Powers for Cosmic Encounter.

Aliens inspired by medical and healthcare concepts.
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
class Surgeon(AlienPower):
    """
    Surgeon - Power to Operate.
    Once per encounter, remove exactly 1 ship from any colony to save it from warp.
    """
    name: str = field(default="Surgeon", init=False)
    description: str = field(
        default="Remove 1 ship from colony to save from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nurse(AlienPower):
    """
    Nurse - Power to Care.
    At start of each turn, return 1 ship from warp to any of your colonies.
    """
    name: str = field(default="Nurse", init=False)
    description: str = field(
        default="Return 1 ship from warp at start of turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Doctor(AlienPower):
    """
    Doctor - Power to Heal.
    After each encounter, return up to 2 ships from warp.
    """
    name: str = field(default="Doctor", init=False)
    description: str = field(
        default="Return up to 2 ships from warp after encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pharmacist(AlienPower):
    """
    Pharmacist - Power to Prescribe.
    You may give 1 card to another player to gain +2 in the current encounter.
    """
    name: str = field(default="Pharmacist", init=False)
    description: str = field(
        default="Give card to player for +2.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Paramedic(AlienPower):
    """
    Paramedic - Power of Emergency.
    When any player would lose all their ships, save 1 ship to any colony.
    """
    name: str = field(default="Paramedic", init=False)
    description: str = field(
        default="Save 1 ship when player loses all.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anesthesiologist(AlienPower):
    """
    Anesthesiologist - Power to Numb.
    Opponent's reinforcements have no effect when you are main player.
    """
    name: str = field(default="Anesthesiologist", init=False)
    description: str = field(
        default="Block opponent reinforcements as main player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pathologist(AlienPower):
    """
    Pathologist - Power to Diagnose.
    Look at any player's hand at the start of your turn.
    """
    name: str = field(default="Pathologist", init=False)
    description: str = field(
        default="View one player's hand at start of turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Therapist(AlienPower):
    """
    Therapist - Power to Counsel.
    You may make any player discard 1 card and draw 1 card.
    """
    name: str = field(default="Therapist", init=False)
    description: str = field(
        default="Force player to swap 1 card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Immunologist(AlienPower):
    """
    Immunologist - Power of Immunity.
    You are immune to zap cards (Cosmic Zap, etc.).
    """
    name: str = field(default="Immunologist", init=False)
    description: str = field(
        default="Immune to zap cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cardiologist(AlienPower):
    """
    Cardiologist - Power of the Heart.
    When you play negotiate, draw 2 cards regardless of deal outcome.
    """
    name: str = field(default="Cardiologist", init=False)
    description: str = field(
        default="Draw 2 cards when playing negotiate.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Oncologist(AlienPower):
    """
    Oncologist - Power to Remove.
    Once per encounter, permanently remove 1 card from the game.
    """
    name: str = field(default="Oncologist", init=False)
    description: str = field(
        default="Remove 1 card from game per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dentist(AlienPower):
    """
    Dentist - Power to Extract.
    After winning, take 1 random card from the loser's hand.
    """
    name: str = field(default="Dentist", init=False)
    description: str = field(
        default="Take 1 random card from loser after winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Optometrist(AlienPower):
    """
    Optometrist - Power to See.
    You may look at the top 3 cards of the cosmic deck at any time.
    """
    name: str = field(default="Optometrist", init=False)
    description: str = field(
        default="View top 3 cosmic deck cards anytime.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Psychiatrist(AlienPower):
    """
    Psychiatrist - Power to Analyze.
    Once per encounter, force a main player to reveal their chosen card.
    """
    name: str = field(default="Psychiatrist", init=False)
    description: str = field(
        default="Force main player to reveal card early.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Geneticist(AlienPower):
    """
    Geneticist - Power to Mutate.
    Once per game, copy another player's alien power for one encounter.
    """
    name: str = field(default="Geneticist", init=False)
    description: str = field(
        default="Copy another alien's power once per game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all medical powers
AlienRegistry.register(Surgeon())
AlienRegistry.register(Nurse())
AlienRegistry.register(Doctor())
AlienRegistry.register(Pharmacist())
AlienRegistry.register(Paramedic())
AlienRegistry.register(Anesthesiologist())
AlienRegistry.register(Pathologist())
AlienRegistry.register(Therapist())
AlienRegistry.register(Immunologist())
AlienRegistry.register(Cardiologist())
AlienRegistry.register(Oncologist())
AlienRegistry.register(Dentist())
AlienRegistry.register(Optometrist())
AlienRegistry.register(Psychiatrist())
AlienRegistry.register(Geneticist())
