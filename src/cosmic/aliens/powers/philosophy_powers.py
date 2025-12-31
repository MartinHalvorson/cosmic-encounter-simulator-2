"""
Philosophy Powers for Cosmic Encounter.

Aliens inspired by philosophical concepts and schools of thought.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Philosopher(AlienPower):
    """
    Philosopher - Power of Wisdom.
    Once per encounter, you may look at any player's hand.
    """
    name: str = "Philosopher"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Nihilist(AlienPower):
    """
    Nihilist - Power of Nothing.
    All attack cards played against you are reduced by 10.
    """
    name: str = "Nihilist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Stoic(AlienPower):
    """
    Stoic - Power of Acceptance.
    You cannot lose more than 2 ships per encounter.
    """
    name: str = "Stoic"
    timing: PowerTiming = PowerTiming.SHIPS_TO_WARP
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Existentialist(AlienPower):
    """
    Existentialist - Power of Choice.
    Before cards are revealed, you may switch your card with any card
    from your hand.
    """
    name: str = "Existentialist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Rationalist(AlienPower):
    """
    Rationalist - Power of Reason.
    Add +2 when you have more cards than your opponent.
    """
    name: str = "Rationalist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +2 if more cards than opponent."""
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if player.hand_size() > opponent.hand_size():
            return base_total + 2
        return base_total


@dataclass
class Empiricist(AlienPower):
    """
    Empiricist - Power of Experience.
    Gain +1 for each encounter you've won this game (max +10).
    """
    name: str = "Empiricist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Utilitarian(AlienPower):
    """
    Utilitarian - Power of the Greater Good.
    You may sacrifice an ally's ships instead of your own.
    """
    name: str = "Utilitarian"
    timing: PowerTiming = PowerTiming.SHIPS_TO_WARP
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Idealist(AlienPower):
    """
    Idealist - Power of Vision.
    You may play negotiate cards as attack 20.
    """
    name: str = "Idealist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Pragmatist(AlienPower):
    """
    Pragmatist - Power of What Works.
    You may change your card type after seeing opponent's card.
    """
    name: str = "Pragmatist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Determinist(AlienPower):
    """
    Determinist - Power of Fate.
    Once per game, you may declare you will win the encounter.
    If you do, you automatically win.
    """
    name: str = "Determinist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.OPTIONAL
    has_alternate_win: bool = False


@dataclass
class Skeptic(AlienPower):
    """
    Skeptic - Power of Doubt.
    Flare cards and artifacts have no effect when you are involved.
    """
    name: str = "Skeptic"
    timing: PowerTiming = PowerTiming.CONSTANT
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Relativist(AlienPower):
    """
    Relativist - Power of Perspective.
    Attack values are always compared relatively (difference from average).
    """
    name: str = "Relativist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Absolutist(AlienPower):
    """
    Absolutist - Power of Certainty.
    Your attack cards are worth exactly their printed value (immune to modifiers).
    """
    name: str = "Absolutist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Dualist(AlienPower):
    """
    Dualist - Power of Two.
    You may play two cards per encounter, using the higher value.
    """
    name: str = "Dualist"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Monist(AlienPower):
    """
    Monist - Power of Unity.
    All your ships count as one for combat but add +1 each.
    """
    name: str = "Monist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


# Register all philosophy powers
def register_philosophy_powers():
    from ..registry import AlienRegistry

    powers = [
        Philosopher(),
        Nihilist(),
        Stoic(),
        Existentialist(),
        Rationalist(),
        Empiricist(),
        Utilitarian(),
        Idealist(),
        Pragmatist(),
        Determinist(),
        Skeptic(),
        Relativist(),
        Absolutist(),
        Dualist(),
        Monist(),
    ]

    for power in powers:
        AlienRegistry.register(power)


# Auto-register on import
register_philosophy_powers()
