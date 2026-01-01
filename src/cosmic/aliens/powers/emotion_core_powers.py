"""
Emotion Core Powers - Core emotion themed aliens.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Joy_Core(AlienPower):
    """Joy_Core - Pure happiness. +4 always."""
    name: str = field(default="Joy_Core", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Sadness_Core(AlienPower):
    """Sadness_Core - Deep sorrow. +4 on defense."""
    name: str = field(default="Sadness_Core", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Anger_Core(AlienPower):
    """Anger_Core - Burning rage. +5 on offense."""
    name: str = field(default="Anger_Core", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Fear_Core(AlienPower):
    """Fear_Core - Primal terror. +4 on defense."""
    name: str = field(default="Fear_Core", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Surprise_Core(AlienPower):
    """Surprise_Core - Unexpected. Random +2 to +6."""
    name: str = field(default="Surprise_Core", init=False)
    description: str = field(default="Random +2 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(2, 6)
        return total


@dataclass
class Disgust_Core(AlienPower):
    """Disgust_Core - Revulsion. -2 to opponent."""
    name: str = field(default="Disgust_Core", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Contempt_Core(AlienPower):
    """Contempt_Core - Disdain. +3 always."""
    name: str = field(default="Contempt_Core", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Trust_Core(AlienPower):
    """Trust_Core - Faith. +2 per ally."""
    name: str = field(default="Trust_Core", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anticipation_Core(AlienPower):
    """Anticipation_Core - Expectation. +5 first encounter."""
    name: str = field(default="Anticipation_Core", init=False)
    description: str = field(default="+5 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Love_Core(AlienPower):
    """Love_Core - Deep affection. +3 per ally."""
    name: str = field(default="Love_Core", init=False)
    description: str = field(default="+3 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hate_Core(AlienPower):
    """Hate_Core - Intense loathing. +5 on offense."""
    name: str = field(default="Hate_Core", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Hope_Core(AlienPower):
    """Hope_Core - Optimism. Return 1 ship from warp."""
    name: str = field(default="Hope_Core", init=False)
    description: str = field(default="Return 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Despair_Core(AlienPower):
    """Despair_Core - Hopelessness. +6 when behind."""
    name: str = field(default="Despair_Core", init=False)
    description: str = field(default="+6 when behind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pride_Core(AlienPower):
    """Pride_Core - Self-worth. +4 when ahead."""
    name: str = field(default="Pride_Core", init=False)
    description: str = field(default="+4 when ahead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shame_Core(AlienPower):
    """Shame_Core - Self-conscious. +3 on defense."""
    name: str = field(default="Shame_Core", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


# Register all powers
EMOTION_CORE_POWERS = [
    Joy_Core, Sadness_Core, Anger_Core, Fear_Core, Surprise_Core,
    Disgust_Core, Contempt_Core, Trust_Core, Anticipation_Core, Love_Core,
    Hate_Core, Hope_Core, Despair_Core, Pride_Core, Shame_Core,
]

for power_class in EMOTION_CORE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
