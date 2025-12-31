"""
Spirit Powers - Ethereal and supernatural aliens.
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
class Ghost(AlienPower):
    """Ghost - Incorporeal. Ships can't be targeted by artifacts."""
    name: str = field(default="Ghost", init=False)
    description: str = field(default="Ships immune to artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wraith(AlienPower):
    """Wraith - Death touch. Win ties; opponent loses extra ship."""
    name: str = field(default="Wraith", init=False)
    description: str = field(default="Win ties; extra ship loss for opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Specter(AlienPower):
    """Specter - Haunting presence. -2 to opponent's total."""
    name: str = field(default="Specter", init=False)
    description: str = field(default="-2 to opponent's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Poltergeist(AlienPower):
    """Poltergeist - Mischief maker. Swap 2 destiny cards."""
    name: str = field(default="Poltergeist", init=False)
    description: str = field(default="Swap destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shade(AlienPower):
    """Shade - Shadow form. Ships return to colonies instead of warp."""
    name: str = field(default="Shade", init=False)
    description: str = field(default="Ships return home instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spirit(AlienPower):
    """Spirit - Ancestral guidance. +1 for each ship in warp."""
    name: str = field(default="Spirit", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + player.ships_in_warp
        return total


@dataclass
class Banshee(AlienPower):
    """Banshee - Death wail. When losing, opponent discards 2 cards."""
    name: str = field(default="Banshee", init=False)
    description: str = field(default="Opponent discards 2 cards when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Revenant(AlienPower):
    """Revenant - Undying spirit. Retrieve 2 ships from warp each turn."""
    name: str = field(default="Revenant", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Apparition(AlienPower):
    """Apparition - Sudden appearance. Join any encounter as ally."""
    name: str = field(default="Apparition", init=False)
    description: str = field(default="Join any encounter without invitation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Soul(AlienPower):
    """Soul - Inner strength. Double compensation received."""
    name: str = field(default="Soul", init=False)
    description: str = field(default="Double compensation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ethereal(AlienPower):
    """Ethereal - Phase shift. Ignore kickers played against you."""
    name: str = field(default="Ethereal", init=False)
    description: str = field(default="Ignore opponent kickers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Haunt(AlienPower):
    """Haunt - Persistent presence. Stay on planet even when losing."""
    name: str = field(default="Haunt", init=False)
    description: str = field(default="Keep 1 ship on planet when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Eidolon(AlienPower):
    """Eidolon - Perfect copy. Use opponent's alien power."""
    name: str = field(default="Eidolon", init=False)
    description: str = field(default="Copy opponent's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Phantom(AlienPower):
    """Phantom - Unseen force. Ships count double when hidden."""
    name: str = field(default="Phantom_Alt", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ghostly(AlienPower):
    """Ghostly - Intangible. Negotiate cards are worth +2."""
    name: str = field(default="Ghostly", init=False)
    description: str = field(default="Negotiate cards worth +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Ghost())
AlienRegistry.register(Wraith())
AlienRegistry.register(Specter())
AlienRegistry.register(Poltergeist())
AlienRegistry.register(Shade())
AlienRegistry.register(Spirit())
AlienRegistry.register(Banshee())
AlienRegistry.register(Revenant())
AlienRegistry.register(Apparition())
AlienRegistry.register(Soul())
AlienRegistry.register(Ethereal())
AlienRegistry.register(Haunt())
AlienRegistry.register(Eidolon())
AlienRegistry.register(Phantom())
AlienRegistry.register(Ghostly())
