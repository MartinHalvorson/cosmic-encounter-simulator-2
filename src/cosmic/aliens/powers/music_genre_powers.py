"""
Music Genre Powers - Music genre themed aliens.
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
class Rock_Music(AlienPower):
    """Rock_Music - Electric power."""
    name: str = field(default="Rock_Music", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Jazz_Music(AlienPower):
    """Jazz_Music - Improvised soul."""
    name: str = field(default="Jazz_Music", init=False)
    description: str = field(default="+2 plus random +0-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + random.randint(0, 5)
        return total


@dataclass
class Classical_Music(AlienPower):
    """Classical_Music - Orchestral grand."""
    name: str = field(default="Classical_Music", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Blues_Music(AlienPower):
    """Blues_Music - Soulful roots."""
    name: str = field(default="Blues_Music", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Pop_Music(AlienPower):
    """Pop_Music - Catchy hook."""
    name: str = field(default="Pop_Music", init=False)
    description: str = field(default="+4 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count > 0:
            return total + 4
        return total


@dataclass
class Metal_Music(AlienPower):
    """Metal_Music - Heavy power."""
    name: str = field(default="Metal_Music", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 6
        return total


@dataclass
class Country_Music(AlienPower):
    """Country_Music - Rural heart."""
    name: str = field(default="Country_Music", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Hip_Hop_Music(AlienPower):
    """Hip_Hop_Music - Urban beat."""
    name: str = field(default="Hip_Hop_Music", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Reggae_Music(AlienPower):
    """Reggae_Music - Island rhythm."""
    name: str = field(default="Reggae_Music", init=False)
    description: str = field(default="+5 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 5
        return total


@dataclass
class Electronic_Music(AlienPower):
    """Electronic_Music - Synth wave."""
    name: str = field(default="Electronic_Music", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, game.current_turn)
        return total


@dataclass
class Folk_Music(AlienPower):
    """Folk_Music - Traditional roots."""
    name: str = field(default="Folk_Music", init=False)
    description: str = field(default="+5 with 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 5
        return total


@dataclass
class Punk_Music(AlienPower):
    """Punk_Music - Raw rebellion."""
    name: str = field(default="Punk_Music", init=False)
    description: str = field(default="+5 with 3 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return total + 5
        return total


@dataclass
class Soul_Music(AlienPower):
    """Soul_Music - Deep emotion."""
    name: str = field(default="Soul_Music", init=False)
    description: str = field(default="+5 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 5
        return total


@dataclass
class Funk_Music(AlienPower):
    """Funk_Music - Groove power."""
    name: str = field(default="Funk_Music", init=False)
    description: str = field(default="+2 per ally (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        return total + min(6, ally_count * 2)


@dataclass
class Opera_Music(AlienPower):
    """Opera_Music - Dramatic voice."""
    name: str = field(default="Opera_Music", init=False)
    description: str = field(default="+1 per card (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(7, len(player.hand))
        return total


MUSIC_GENRE_POWERS = [
    Rock_Music, Jazz_Music, Classical_Music, Blues_Music, Pop_Music,
    Metal_Music, Country_Music, Hip_Hop_Music, Reggae_Music, Electronic_Music,
    Folk_Music, Punk_Music, Soul_Music, Funk_Music, Opera_Music
]

for power_class in MUSIC_GENRE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
