"""
Science Powers - Scientific and research-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Physicist(AlienPower):
    """Physicist - Energy expert. +3 when attacking."""
    name: str = field(default="Physicist", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Chemist(AlienPower):
    """Chemist - Reaction expert. Combine two attack cards."""
    name: str = field(default="Chemist", init=False)
    description: str = field(default="Play two attack cards summed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Biologist(AlienPower):
    """Biologist - Life expert. +1 per ship in encounter."""
    name: str = field(default="Biologist", init=False)
    description: str = field(default="+1 per ship committed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Astronomer(AlienPower):
    """Astronomer - Star watcher. See next 3 destiny cards."""
    name: str = field(default="Astronomer", init=False)
    description: str = field(default="View top 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mathematician(AlienPower):
    """Mathematician - Number expert. Double attack card value."""
    name: str = field(default="Mathematician", init=False)
    description: str = field(default="Double encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Geologist(AlienPower):
    """Geologist - Earth expert. +2 per home colony."""
    name: str = field(default="Geologist", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + (home_count * 2)
        return total


@dataclass
class Historian(AlienPower):
    """Historian - Past expert. +1 per turn in game."""
    name: str = field(default="Historian", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Geneticist(AlienPower):
    """Geneticist - DNA expert. Copy opponent's power."""
    name: str = field(default="Geneticist", init=False)
    description: str = field(default="Use opponent's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Economist(AlienPower):
    """Economist - Value expert. +1 per card in hand."""
    name: str = field(default="Economist", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + len(player.hand)
        return total


@dataclass
class Psychologist(AlienPower):
    """Psychologist - Mind expert. See opponent's encounter card."""
    name: str = field(default="Psychologist", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Researcher(AlienPower):
    """Researcher - Knowledge seeker. Draw 2 cards when winning."""
    name: str = field(default="Researcher", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Inventor(AlienPower):
    """Inventor - Creator. Make new encounter cards."""
    name: str = field(default="Inventor", init=False)
    description: str = field(default="Create custom encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Theorist(AlienPower):
    """Theorist - Hypothesis maker. +3 when defending."""
    name: str = field(default="Theorist", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Analyst(AlienPower):
    """Analyst - Data expert. View opponent's hand."""
    name: str = field(default="Analyst_Alt", init=False)
    description: str = field(default="See opponent's entire hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scholar(AlienPower):
    """Scholar - Learned one. Win ties."""
    name: str = field(default="Scholar", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Physicist())
AlienRegistry.register(Chemist())
AlienRegistry.register(Biologist())
AlienRegistry.register(Astronomer())
AlienRegistry.register(Mathematician())
AlienRegistry.register(Geologist())
AlienRegistry.register(Historian())
AlienRegistry.register(Geneticist())
AlienRegistry.register(Economist())
AlienRegistry.register(Psychologist())
AlienRegistry.register(Researcher())
AlienRegistry.register(Inventor())
AlienRegistry.register(Theorist())
AlienRegistry.register(Analyst())
AlienRegistry.register(Scholar())
