"""
Celestial Powers - Space and astronomy themed aliens.
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
class Star(AlienPower):
    """Star - Power of Light. +3 always."""
    name: str = field(default="Star", init=False)
    description: str = field(default="+3 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Moon(AlienPower):
    """Moon - Power of Phases. Alternating bonus."""
    name: str = field(default="Moon", init=False)
    description: str = field(default="+4 on odd turns, +2 on even.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sun(AlienPower):
    """Sun - Power of Energy. +5 on offense."""
    name: str = field(default="Sun", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Comet(AlienPower):
    """Comet - Power of Speed. Extra encounter."""
    name: str = field(default="Comet", init=False)
    description: str = field(default="Take third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Asteroid(AlienPower):
    """Asteroid - Power of Impact. Damage on arrival."""
    name: str = field(default="Asteroid", init=False)
    description: str = field(default="1 defending ship goes to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nebula(AlienPower):
    """Nebula - Power of Mystery. Hide card."""
    name: str = field(default="Nebula", init=False)
    description: str = field(default="Card stays hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Galaxy(AlienPower):
    """Galaxy - Power of Vastness. +1 per colony."""
    name: str = field(default="Galaxy", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blackhole(AlienPower):
    """Blackhole - Power of Consumption. Ships vanish."""
    name: str = field(default="Blackhole", init=False)
    description: str = field(default="Losing ships removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Supernova(AlienPower):
    """Supernova - Power of Explosion. Once per game big effect."""
    name: str = field(default="Supernova", init=False)
    description: str = field(default="Once per game: +15 to total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Pulsar(AlienPower):
    """Pulsar - Power of Rhythm. Regular bonuses."""
    name: str = field(default="Pulsar", init=False)
    description: str = field(default="+3 every third encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quasar(AlienPower):
    """Quasar - Power of Brightness. +4 constant."""
    name: str = field(default="Quasar", init=False)
    description: str = field(default="+4 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Saturn(AlienPower):
    """Saturn - Power of Rings. Circular defense."""
    name: str = field(default="Saturn", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Jupiter(AlienPower):
    """Jupiter - Power of Size. +2 per ship."""
    name: str = field(default="Jupiter", init=False)
    description: str = field(default="+2 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mars(AlienPower):
    """Mars - Power of War. +4 on offense."""
    name: str = field(default="Mars", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Venus(AlienPower):
    """Venus - Power of Beauty. Attract allies."""
    name: str = field(default="Venus", init=False)
    description: str = field(default="One extra ally joins you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mercury(AlienPower):
    """Mercury - Power of Speed. Act first."""
    name: str = field(default="Mercury", init=False)
    description: str = field(default="Play card before opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Neptune(AlienPower):
    """Neptune - Power of Depths. Retrieve ships."""
    name: str = field(default="Neptune", init=False)
    description: str = field(default="Return 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pluto(AlienPower):
    """Pluto - Power of Distance. Ignore ally penalties."""
    name: str = field(default="Pluto", init=False)
    description: str = field(default="Allies always welcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Meteor(AlienPower):
    """Meteor - Power of Falling. Random +2 to +8."""
    name: str = field(default="Meteor", init=False)
    description: str = field(default="Random +2 to +8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(2, 8)
        return total


@dataclass
class Eclipse(AlienPower):
    """Eclipse - Power of Shadow. -3 to opponent."""
    name: str = field(default="Eclipse", init=False)
    description: str = field(default="Opponent gets -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
CELESTIAL_POWERS = [
    Star, Moon, Sun, Comet, Asteroid, Nebula, Galaxy, Blackhole, Supernova, Pulsar,
    Quasar, Saturn, Jupiter, Mars, Venus, Mercury, Neptune, Pluto, Meteor, Eclipse,
]

for power_class in CELESTIAL_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
