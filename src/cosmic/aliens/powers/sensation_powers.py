"""
Sensation Powers for Cosmic Encounter.

Aliens inspired by the five senses and sensations.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Sight(AlienPower):
    """Sight - Power of Vision."""
    name: str = field(default="Sight", init=False)
    description: str = field(default="See opponent cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sound(AlienPower):
    """Sound - Power of Hearing."""
    name: str = field(default="Sound", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Touch_Sense(AlienPower):
    """Touch_Sense - Power of Feeling."""
    name: str = field(default="Touch_Sense", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Taste(AlienPower):
    """Taste - Power of Flavor."""
    name: str = field(default="Taste", init=False)
    description: str = field(default="Reject bad deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smell(AlienPower):
    """Smell - Power of Scent."""
    name: str = field(default="Smell", init=False)
    description: str = field(default="Detect traps.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warmth(AlienPower):
    """Warmth - Power of Heat."""
    name: str = field(default="Warmth", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Cold_Sense(AlienPower):
    """Cold_Sense - Power of Chill."""
    name: str = field(default="Cold_Sense", init=False)
    description: str = field(default="Slow opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pain(AlienPower):
    """Pain - Power of Hurt."""
    name: str = field(default="Pain", init=False)
    description: str = field(default="+5 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pleasure(AlienPower):
    """Pleasure - Power of Joy."""
    name: str = field(default="Pleasure", init=False)
    description: str = field(default="+3 when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Balance_Sense(AlienPower):
    """Balance_Sense - Power of Equilibrium."""
    name: str = field(default="Balance_Sense", init=False)
    description: str = field(default="Force tie outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hunger(AlienPower):
    """Hunger - Power of Appetite."""
    name: str = field(default="Hunger", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Thirst(AlienPower):
    """Thirst - Power of Need."""
    name: str = field(default="Thirst", init=False)
    description: str = field(default="Draw card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


# Register all aliens
for alien_class in [
    Sight, Sound, Touch_Sense, Taste, Smell,
    Warmth, Cold_Sense, Pain, Pleasure, Balance_Sense,
    Hunger, Thirst,
]:
    AlienRegistry.register(alien_class())
