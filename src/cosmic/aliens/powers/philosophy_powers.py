"""
Philosophy Powers for Cosmic Encounter.

Aliens inspired by philosophical concepts and schools of thought.
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
class Philosopher(AlienPower):
    """
    Philosopher - Power to Question.
    Once per encounter, you may force a player to justify their action or lose 1 ship.
    """
    name: str = field(default="Philosopher", init=False)
    description: str = field(
        default="Force justification or opponent loses 1 ship.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stoic(AlienPower):
    """
    Stoic - Power of Acceptance.
    Losses do not affect your power. Your power remains active even with 3 home colonies lost.
    """
    name: str = field(default="Stoic", init=False)
    description: str = field(
        default="Power remains active regardless of home colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skeptic(AlienPower):
    """
    Skeptic - Power to Doubt.
    You may look at an opponent's encounter card before playing yours.
    """
    name: str = field(default="Skeptic", init=False)
    description: str = field(
        default="See opponent's encounter card first.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Nihilist(AlienPower):
    """
    Nihilist - Power of Nothingness.
    When you lose, you may send all ships on both sides to the warp.
    """
    name: str = field(default="Nihilist", init=False)
    description: str = field(
        default="When losing, send all ships to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Existentialist(AlienPower):
    """
    Existentialist - Power of Choice.
    Once per encounter, you may change your role (offense to ally, ally to not involved).
    """
    name: str = field(default="Existentialist", init=False)
    description: str = field(
        default="Change your encounter role once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rationalist(AlienPower):
    """
    Rationalist - Power of Logic.
    You always know the exact card value of the opponent before reveal.
    """
    name: str = field(default="Rationalist", init=False)
    description: str = field(
        default="Know opponent's card value before reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Empiricist(AlienPower):
    """
    Empiricist - Power of Experience.
    +1 for each encounter you've been in this game (max +6).
    """
    name: str = field(default="Empiricist", init=False)
    description: str = field(
        default="+1 per encounter participated in (max +6).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Idealist(AlienPower):
    """
    Idealist - Power of Vision.
    Your negotiate cards count as attack 10 when you choose.
    """
    name: str = field(default="Idealist", init=False)
    description: str = field(
        default="Negotiates can count as attack 10.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pragmatist(AlienPower):
    """
    Pragmatist - Power of Utility.
    After seeing the result, you may swap your card for one from your hand.
    """
    name: str = field(default="Pragmatist", init=False)
    description: str = field(
        default="Swap played card after seeing result.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Determinist(AlienPower):
    """
    Determinist - Power of Fate.
    Before destiny, you may declare the color that will be drawn.
    """
    name: str = field(default="Determinist", init=False)
    description: str = field(
        default="Predict and enforce destiny card color.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Utilitarianist(AlienPower):
    """
    Utilitarianist - Power of the Greatest Good.
    You may sacrifice 2 of your ships to save all ships on one side.
    """
    name: str = field(default="Utilitarianist", init=False)
    description: str = field(
        default="Sacrifice 2 ships to save all ships on one side.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dualist(AlienPower):
    """
    Dualist - Power of Two.
    You may play two encounter cards and use the higher value.
    """
    name: str = field(default="Dualist", init=False)
    description: str = field(
        default="Play 2 encounter cards, use higher.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monist(AlienPower):
    """
    Monist - Power of Unity.
    All your ships count as a single entity; either all survive or all go to warp.
    """
    name: str = field(default="Monist", init=False)
    description: str = field(
        default="Ships survive or die as one.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cynic(AlienPower):
    """
    Cynic - Power to Mock.
    Opponents cannot use artifacts when you are a main player.
    """
    name: str = field(default="Cynic", init=False)
    description: str = field(
        default="Block opponent artifacts when main player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dialectician(AlienPower):
    """
    Dialectician - Power of Synthesis.
    Average your encounter card with opponent's for your total.
    """
    name: str = field(default="Dialectician", init=False)
    description: str = field(
        default="Average your card with opponent's.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all philosophy powers
AlienRegistry.register(Philosopher())
AlienRegistry.register(Stoic())
AlienRegistry.register(Skeptic())
AlienRegistry.register(Nihilist())
AlienRegistry.register(Existentialist())
AlienRegistry.register(Rationalist())
AlienRegistry.register(Empiricist())
AlienRegistry.register(Idealist())
AlienRegistry.register(Pragmatist())
AlienRegistry.register(Determinist())
AlienRegistry.register(Utilitarianist())
AlienRegistry.register(Dualist())
AlienRegistry.register(Monist())
AlienRegistry.register(Cynic())
AlienRegistry.register(Dialectician())
