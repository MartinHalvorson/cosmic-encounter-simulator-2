"""
Sky Powers - Aerial and atmospheric-themed aliens.
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
class Cloud(AlienPower):
    """Cloud - Obscuring mist. Hide your attack card value."""
    name: str = field(default="Cloud", init=False)
    description: str = field(default="Card value hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Storm(AlienPower):
    """Storm - Violent weather. All players discard after encounter."""
    name: str = field(default="Storm_Alt", init=False)
    description: str = field(default="Force everyone to discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wind(AlienPower):
    """Wind - Pushing force. Move opponent ships before encounter."""
    name: str = field(default="Wind_Alt", init=False)
    description: str = field(default="Relocate opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thunder(AlienPower):
    """Thunder - Booming voice. +4 on first encounter."""
    name: str = field(default="Thunder", init=False)
    description: str = field(default="+4 on first encounter each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Lightning(AlienPower):
    """Lightning - Instant strike. Win ties, opponent loses ship."""
    name: str = field(default="Lightning_Alt", init=False)
    description: str = field(default="Win ties and enemy loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Rainbow(AlienPower):
    """Rainbow - Multicolored. Use any flare as your own."""
    name: str = field(default="Rainbow", init=False)
    description: str = field(default="Use any flare as your own.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sunset(AlienPower):
    """Sunset - Fading light. +3 on second encounter of turn."""
    name: str = field(default="Sunset", init=False)
    description: str = field(default="+3 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 2:
            return total + 3
        return total


@dataclass
class Fog(AlienPower):
    """Fog - Dense cover. Opponent plays card blind."""
    name: str = field(default="Fog", init=False)
    description: str = field(default="Opponent selects card randomly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Haze(AlienPower):
    """Haze - Blurry vision. Opponent can't see ally counts."""
    name: str = field(default="Haze", init=False)
    description: str = field(default="Hide ally ship counts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Aurora(AlienPower):
    """Aurora - Northern lights. +2 for each color in your hand."""
    name: str = field(default="Aurora", init=False)
    description: str = field(default="+2 per card type in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Comet(AlienPower):
    """Comet - Blazing trail. +1 for each colony gained this game."""
    name: str = field(default="Comet", init=False)
    description: str = field(default="+1 per colony gained.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Meteor(AlienPower):
    """Meteor - Fiery impact. Destroy one colony when winning."""
    name: str = field(default="Meteor_Alt", init=False)
    description: str = field(default="Destroy enemy colony on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Star(AlienPower):
    """Star - Bright center. All allies get +1."""
    name: str = field(default="Star_Alt", init=False)
    description: str = field(default="All allies gain +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Moon(AlienPower):
    """Moon - Tidal influence. Move ships between your planets."""
    name: str = field(default="Moon_Alt", init=False)
    description: str = field(default="Freely move ships each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eclipse(AlienPower):
    """Eclipse - Dark shadow. Negate opponent's alien power."""
    name: str = field(default="Eclipse", init=False)
    description: str = field(default="Cancel opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Cloud())
AlienRegistry.register(Storm())
AlienRegistry.register(Wind())
AlienRegistry.register(Thunder())
AlienRegistry.register(Lightning())
AlienRegistry.register(Rainbow())
AlienRegistry.register(Sunset())
AlienRegistry.register(Fog())
AlienRegistry.register(Haze())
AlienRegistry.register(Aurora())
AlienRegistry.register(Comet())
AlienRegistry.register(Meteor())
AlienRegistry.register(Star())
AlienRegistry.register(Moon())
AlienRegistry.register(Eclipse())
