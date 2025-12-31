"""
Deception Powers - Aliens with trickery and illusion abilities.
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
class Bluffer(AlienPower):
    """
    Bluffer - Fake Strength.
    Claim any card value.
    """
    name: str = field(default="Bluffer", init=False)
    description: str = field(default="Claim card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Charlatan(AlienPower):
    """
    Charlatan - False Power.
    Pretend to have power.
    """
    name: str = field(default="Charlatan", init=False)
    description: str = field(default="Fake power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Cheater_Alt(AlienPower):
    """
    Cheater_Alt - Bend Rules.
    Play extra card secretly.
    """
    name: str = field(default="Cheater_Alt", init=False)
    description: str = field(default="Play extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Conman(AlienPower):
    """
    Conman - Scam Deal.
    Take extra in deals.
    """
    name: str = field(default="Conman", init=False)
    description: str = field(default="Extra from deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Deceiver(AlienPower):
    """
    Deceiver - Lie Freely.
    Opponent's card shows wrong.
    """
    name: str = field(default="Deceiver", init=False)
    description: str = field(default="Wrong card shown.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Faker(AlienPower):
    """
    Faker - False Attack.
    Swap attack target.
    """
    name: str = field(default="Faker", init=False)
    description: str = field(default="Swap target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Forger(AlienPower):
    """
    Forger - Fake Card.
    Play card as different value.
    """
    name: str = field(default="Forger", init=False)
    description: str = field(default="Fake value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fraud(AlienPower):
    """
    Fraud - Total Fake.
    Win with negotiate vs attack.
    """
    name: str = field(default="Fraud", init=False)
    description: str = field(default="Negotiate wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hoaxer(AlienPower):
    """
    Hoaxer - Fake Event.
    Cancel opponent's artifact.
    """
    name: str = field(default="Hoaxer", init=False)
    description: str = field(default="Cancel artifact.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Illusionist(AlienPower):
    """
    Illusionist - Create Illusion.
    Add phantom ships.
    """
    name: str = field(default="Illusionist", init=False)
    description: str = field(default="Phantom ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Impostor(AlienPower):
    """
    Impostor - Steal Identity.
    Use opponent's power once.
    """
    name: str = field(default="Impostor", init=False)
    description: str = field(default="Use opponent power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Liar(AlienPower):
    """
    Liar - Constant Lies.
    +3 when bluffing.
    """
    name: str = field(default="Liar", init=False)
    description: str = field(default="+3 bluff bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 when bluffing (random 50% chance)."""
        if random.random() < 0.5:
            return total + 3
        return total


@dataclass
class Pretender_Alt(AlienPower):
    """
    Pretender_Alt - Act Weak.
    Win when appearing to lose.
    """
    name: str = field(default="Pretender_Alt", init=False)
    description: str = field(default="Win appearing weak.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Schemer(AlienPower):
    """
    Schemer - Plot Ahead.
    Set traps for opponent.
    """
    name: str = field(default="Schemer", init=False)
    description: str = field(default="Set traps.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Trickster(AlienPower):
    """
    Trickster - Play Tricks.
    Swap cards after reveal.
    """
    name: str = field(default="Trickster", init=False)
    description: str = field(default="Swap after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Weasel(AlienPower):
    """
    Weasel - Sneaky Escape.
    Avoid loss consequences.
    """
    name: str = field(default="Weasel", init=False)
    description: str = field(default="Avoid loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Bluffer())
AlienRegistry.register(Charlatan())
AlienRegistry.register(Cheater_Alt())
AlienRegistry.register(Conman())
AlienRegistry.register(Deceiver())
AlienRegistry.register(Faker())
AlienRegistry.register(Forger())
AlienRegistry.register(Fraud())
AlienRegistry.register(Hoaxer())
AlienRegistry.register(Illusionist())
AlienRegistry.register(Impostor())
AlienRegistry.register(Liar())
AlienRegistry.register(Pretender_Alt())
AlienRegistry.register(Schemer())
AlienRegistry.register(Trickster())
AlienRegistry.register(Weasel())
