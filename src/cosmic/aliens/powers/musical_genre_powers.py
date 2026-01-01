"""
Musical Genre themed alien powers for Cosmic Encounter.
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
class Jazz_Genre(AlienPower):
    """Jazz - Power of Improvisation."""
    name: str = field(default="Jazz_Genre", init=False)
    description: str = field(default="+3 when playing unexpected card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Blues_Genre(AlienPower):
    """Blues - Power of Sorrow."""
    name: str = field(default="Blues_Genre", init=False)
    description: str = field(default="+4 when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Classical_Genre(AlienPower):
    """Classical - Power of Refinement."""
    name: str = field(default="Classical_Genre", init=False)
    description: str = field(default="+2 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Metal_Genre(AlienPower):
    """Metal - Power of Aggression."""
    name: str = field(default="Metal_Genre", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Punk_Genre(AlienPower):
    """Punk - Power of Rebellion."""
    name: str = field(default="Punk_Genre", init=False)
    description: str = field(default="+3 attacking leader.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Country_Genre(AlienPower):
    """Country - Power of Home."""
    name: str = field(default="Country_Genre", init=False)
    description: str = field(default="+4 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Reggae_Genre(AlienPower):
    """Reggae - Power of Peace."""
    name: str = field(default="Reggae_Genre", init=False)
    description: str = field(default="+2 with no ships lost.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Folk_Genre(AlienPower):
    """Folk - Power of Tradition."""
    name: str = field(default="Folk_Genre", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Funk_Genre(AlienPower):
    """Funk - Power of Groove."""
    name: str = field(default="Funk_Genre", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Soul_Genre(AlienPower):
    """Soul - Power of Feeling."""
    name: str = field(default="Soul_Genre", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Techno_Genre(AlienPower):
    """Techno - Power of Rhythm."""
    name: str = field(default="Techno_Genre", init=False)
    description: str = field(default="+4 with most ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Grunge_Genre(AlienPower):
    """Grunge - Power of Angst."""
    name: str = field(default="Grunge_Genre", init=False)
    description: str = field(default="+5 when behind.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Jazz_Genre, Blues_Genre, Classical_Genre, Metal_Genre, Punk_Genre,
    Country_Genre, Reggae_Genre, Folk_Genre, Funk_Genre, Soul_Genre,
    Techno_Genre, Grunge_Genre,
]:
    AlienRegistry.register(alien_class())
