"""
Milestone 4500 themed alien powers for Cosmic Encounter.
Special celebration powers for reaching 4500 aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class FourFiveHundred(AlienPower):
    """4500 - Power of Milestone."""
    name: str = field(default="FourFiveHundred", init=False)
    description: str = field(default="+4 for reaching milestone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Massive(AlienPower):
    """Massive - Power of Scale."""
    name: str = field(default="Massive", init=False)
    description: str = field(default="+1 per 10 total ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Enormous(AlienPower):
    """Enormous - Power of Size."""
    name: str = field(default="Enormous", init=False)
    description: str = field(default="+5 when largest player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tremendous(AlienPower):
    """Tremendous - Power of Impact."""
    name: str = field(default="Tremendous", init=False)
    description: str = field(default="+3 and opponent loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monumental(AlienPower):
    """Monumental - Power of Memory."""
    name: str = field(default="Monumental", init=False)
    description: str = field(default="+2 per win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Majestic(AlienPower):
    """Majestic - Power of Glory."""
    name: str = field(default="Majestic", init=False)
    description: str = field(default="+4 when attacking leader.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Awesome(AlienPower):
    """Awesome - Power of Wonder."""
    name: str = field(default="Awesome", init=False)
    description: str = field(default="Allies get +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spectacular(AlienPower):
    """Spectacular - Power of Display."""
    name: str = field(default="Spectacular", init=False)
    description: str = field(default="Reveal hand for +3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stunning(AlienPower):
    """Stunning - Power of Shock."""
    name: str = field(default="Stunning", init=False)
    description: str = field(default="Freeze opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Incredible(AlienPower):
    """Incredible - Power of Belief."""
    name: str = field(default="Incredible", init=False)
    description: str = field(default="+6 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Phenomenal(AlienPower):
    """Phenomenal - Power of Excellence."""
    name: str = field(default="Phenomenal", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Extraordinary(AlienPower):
    """Extraordinary - Power of Rarity."""
    name: str = field(default="Extraordinary", init=False)
    description: str = field(default="Double card bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Remarkable(AlienPower):
    """Remarkable - Power of Notice."""
    name: str = field(default="Remarkable", init=False)
    description: str = field(default="+2 when targeted.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Outstanding(AlienPower):
    """Outstanding - Power of Excellence."""
    name: str = field(default="Outstanding", init=False)
    description: str = field(default="+4 on final colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Impressive(AlienPower):
    """Impressive - Power of Awe."""
    name: str = field(default="Impressive", init=False)
    description: str = field(default="Draw extra card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wonderful(AlienPower):
    """Wonderful - Power of Joy."""
    name: str = field(default="Wonderful", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fantastic(AlienPower):
    """Fantastic - Power of Fantasy."""
    name: str = field(default="Fantastic", init=False)
    description: str = field(default="Use any card as attack 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Marvelous(AlienPower):
    """Marvelous - Power of Marvel."""
    name: str = field(default="Marvelous", init=False)
    description: str = field(default="+5 first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Superb(AlienPower):
    """Superb - Power of Quality."""
    name: str = field(default="Superb", init=False)
    description: str = field(default="+2 with high cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Excellent(AlienPower):
    """Excellent - Power of Perfection."""
    name: str = field(default="Excellent", init=False)
    description: str = field(default="Reroll destiny once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Terrific(AlienPower):
    """Terrific - Power of Impact."""
    name: str = field(default="Terrific", init=False)
    description: str = field(default="+3 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(FourFiveHundred())
AlienRegistry.register(Massive())
AlienRegistry.register(Enormous())
AlienRegistry.register(Tremendous())
AlienRegistry.register(Monumental())
AlienRegistry.register(Majestic())
AlienRegistry.register(Awesome())
AlienRegistry.register(Spectacular())
AlienRegistry.register(Stunning())
AlienRegistry.register(Incredible())
AlienRegistry.register(Phenomenal())
AlienRegistry.register(Extraordinary())
AlienRegistry.register(Remarkable())
AlienRegistry.register(Outstanding())
AlienRegistry.register(Impressive())
AlienRegistry.register(Wonderful())
AlienRegistry.register(Fantastic())
AlienRegistry.register(Marvelous())
AlienRegistry.register(Superb())
AlienRegistry.register(Excellent())
AlienRegistry.register(Terrific())
