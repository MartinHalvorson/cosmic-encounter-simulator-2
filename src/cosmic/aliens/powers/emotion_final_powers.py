"""
Emotion Final Powers for Cosmic Encounter.

Additional emotion-themed aliens.
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
class Determination(AlienPower):
    """Determination - Power of Will. +4 always."""
    name: str = field(default="Determination", init=False)
    description: str = field(default="+4 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Confidence(AlienPower):
    """Confidence - Power of Belief. +3 on offense."""
    name: str = field(default="Confidence", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Anxiety_Alt(AlienPower):
    """Anxiety_Alt - Power of Worry. See opponent's card before choosing."""
    name: str = field(default="Anxiety_Alt", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Excitement(AlienPower):
    """Excitement - Power of Energy. +4 on first encounter."""
    name: str = field(default="Excitement", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Contentment(AlienPower):
    """Contentment - Power of Peace. +2 always."""
    name: str = field(default="Contentment", init=False)
    description: str = field(default="+2 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Frustration(AlienPower):
    """Frustration - Power of Struggle. +4 when behind."""
    name: str = field(default="Frustration", init=False)
    description: str = field(default="+4 when behind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gratitude(AlienPower):
    """Gratitude - Power of Thanks. Allies get +2 each."""
    name: str = field(default="Gratitude", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Surprise_Alt(AlienPower):
    """Surprise_Alt - Power of Shock. +3 on first encounter."""
    name: str = field(default="Surprise_Alt", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Admiration(AlienPower):
    """Admiration - Power of Respect. +2 per ally ship."""
    name: str = field(default="Admiration", init=False)
    description: str = field(default="+2 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sympathy(AlienPower):
    """Sympathy - Power of Understanding. Draw 1 card when losing."""
    name: str = field(default="Sympathy", init=False)
    description: str = field(default="Draw 1 card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nostalgia_Alt(AlienPower):
    """Nostalgia_Alt - Power of Past. +1 per turn game has lasted."""
    name: str = field(default="Nostalgia_Alt", init=False)
    description: str = field(default="+1 per game turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


@dataclass
class Anticipation_Alt(AlienPower):
    """Anticipation_Alt - Power of Waiting. +3 on defense."""
    name: str = field(default="Anticipation_Alt", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Serenity_Alt(AlienPower):
    """Serenity_Alt - Power of Calm. Win ties automatically."""
    name: str = field(default="Serenity_Alt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Loneliness(AlienPower):
    """Loneliness - Power of Solitude. +4 when attacking alone."""
    name: str = field(default="Loneliness", init=False)
    description: str = field(default="+4 without allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Enthusiasm(AlienPower):
    """Enthusiasm - Power of Zeal. +3 always."""
    name: str = field(default="Enthusiasm", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


# Register all emotion final powers
AlienRegistry.register(Determination())
AlienRegistry.register(Confidence())
AlienRegistry.register(Anxiety_Alt())
AlienRegistry.register(Excitement())
AlienRegistry.register(Contentment())
AlienRegistry.register(Frustration())
AlienRegistry.register(Gratitude())
AlienRegistry.register(Surprise_Alt())
AlienRegistry.register(Admiration())
AlienRegistry.register(Sympathy())
AlienRegistry.register(Nostalgia_Alt())
AlienRegistry.register(Anticipation_Alt())
AlienRegistry.register(Serenity_Alt())
AlienRegistry.register(Loneliness())
AlienRegistry.register(Enthusiasm())
