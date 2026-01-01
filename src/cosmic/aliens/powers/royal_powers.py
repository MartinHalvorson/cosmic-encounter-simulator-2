"""
Royal Powers - Nobility and leadership-themed aliens.
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
class King(AlienPower):
    """King - Royal authority. +4 when you have most colonies."""
    name: str = field(default="King", init=False)
    description: str = field(default="+4 when leading in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Duke(AlienPower):
    """Duke - Noble commander. Allies get +1 each."""
    name: str = field(default="Duke", init=False)
    description: str = field(default="Each ally adds +1 extra.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Count(AlienPower):
    """Count - Territory holder. +2 per home colony defended."""
    name: str = field(default="Count", init=False)
    description: str = field(default="+2 per home colony when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Earl(AlienPower):
    """Earl - Border lord. +3 when attacking adjacent system."""
    name: str = field(default="Earl", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Marquis(AlienPower):
    """Marquis - Border defender. +4 defending borders."""
    name: str = field(default="Marquis", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Viscount(AlienPower):
    """Viscount - Deputy ruler. Take card from ally after winning."""
    name: str = field(default="Viscount", init=False)
    description: str = field(default="Take card from ally when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Knight(AlienPower):
    """Knight - Honorable warrior. +2 when attacking alone."""
    name: str = field(default="Knight", init=False)
    description: str = field(default="+2 when attacking without allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Princess(AlienPower):
    """Princess - Royal presence. Opponents can't refuse your deals."""
    name: str = field(default="Princess", init=False)
    description: str = field(default="Deals can't be refused.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Heir(AlienPower):
    """Heir - Next in line. Inherit defeated opponent's card."""
    name: str = field(default="Heir", init=False)
    description: str = field(default="Take defeated opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Noble(AlienPower):
    """Noble - High status. Win ties against non-nobles."""
    name: str = field(default="Noble", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Squire(AlienPower):
    """Squire - Knight's aide. Draw card when ally wins."""
    name: str = field(default="Squire", init=False)
    description: str = field(default="Draw card when ally wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Page(AlienPower):
    """Page - Messenger. See opponent's hand before alliances."""
    name: str = field(default="Page", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Courtier(AlienPower):
    """Courtier - Political operator. Switch sides after alliances."""
    name: str = field(default="Courtier", init=False)
    description: str = field(default="Switch sides after alliances formed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Herald(AlienPower):
    """Herald - Royal announcer. Reveal destiny and choose target."""
    name: str = field(default="Herald_Alt", init=False)
    description: str = field(default="Choose destiny target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Steward(AlienPower):
    """Steward - Estate manager. +1 per home colony you have."""
    name: str = field(default="Steward", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + home_count
        return total


# Register all powers
AlienRegistry.register(King())
AlienRegistry.register(Duke())
AlienRegistry.register(Count())
AlienRegistry.register(Earl())
AlienRegistry.register(Marquis())
AlienRegistry.register(Viscount())
AlienRegistry.register(Knight())
AlienRegistry.register(Princess())
AlienRegistry.register(Heir())
AlienRegistry.register(Noble())
AlienRegistry.register(Squire())
AlienRegistry.register(Page())
AlienRegistry.register(Courtier())
AlienRegistry.register(Herald())
AlienRegistry.register(Steward())
