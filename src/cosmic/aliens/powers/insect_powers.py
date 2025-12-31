"""
Insect Powers - Bug and arthropod-themed aliens.
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
class Ant(AlienPower):
    """Ant - Colony strength. +1 per ship in encounter."""
    name: str = field(default="Ant", init=False)
    description: str = field(default="+1 per ship committed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bee(AlienPower):
    """Bee - Hive mind. All ships count double."""
    name: str = field(default="Bee", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Butterfly(AlienPower):
    """Butterfly - Transformation. Change card type after reveal."""
    name: str = field(default="Butterfly", init=False)
    description: str = field(default="Switch attack/negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Beetle(AlienPower):
    """Beetle - Hard shell. Prevent first 2 ships from warp."""
    name: str = field(default="Beetle", init=False)
    description: str = field(default="Save 2 ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wasp(AlienPower):
    """Wasp - Aggressive stinger. +3 when attacking."""
    name: str = field(default="Wasp", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Moth(AlienPower):
    """Moth - Drawn to light. Join any encounter as ally."""
    name: str = field(default="Moth", init=False)
    description: str = field(default="Join any encounter uninvited.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fly(AlienPower):
    """Fly - Quick escape. Ships return home instead of warp."""
    name: str = field(default="Fly", init=False)
    description: str = field(default="Ships escape to colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mosquito(AlienPower):
    """Mosquito - Blood drain. Draw card from opponent."""
    name: str = field(default="Mosquito", init=False)
    description: str = field(default="Take card from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Firefly(AlienPower):
    """Firefly - Glowing signal. Reveal opponent's card."""
    name: str = field(default="Firefly", init=False)
    description: str = field(default="See opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Locust_Alt(AlienPower):
    """Locust Alt - Swarm destruction. Remove opponent's cards."""
    name: str = field(default="Locust_Alt", init=False)
    description: str = field(default="Opponent discards after win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Caterpillar(AlienPower):
    """Caterpillar - Slow growth. +2 per turn."""
    name: str = field(default="Caterpillar", init=False)
    description: str = field(default="+2 each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dragonfly(AlienPower):
    """Dragonfly - Swift hunter. +4 when attacking."""
    name: str = field(default="Dragonfly", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Cricket(AlienPower):
    """Cricket - Lucky song. Redraw destiny once."""
    name: str = field(default="Cricket", init=False)
    description: str = field(default="Redraw destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Grasshopper(AlienPower):
    """Grasshopper - Great leaper. Attack any planet."""
    name: str = field(default="Grasshopper", init=False)
    description: str = field(default="Ignore destiny target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mantis(AlienPower):
    """Mantis - Patient hunter. Win ties."""
    name: str = field(default="Mantis", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Ant())
AlienRegistry.register(Bee())
AlienRegistry.register(Butterfly())
AlienRegistry.register(Beetle())
AlienRegistry.register(Wasp())
AlienRegistry.register(Moth())
AlienRegistry.register(Fly())
AlienRegistry.register(Mosquito())
AlienRegistry.register(Firefly())
AlienRegistry.register(Locust_Alt())
AlienRegistry.register(Caterpillar())
AlienRegistry.register(Dragonfly())
AlienRegistry.register(Cricket())
AlienRegistry.register(Grasshopper())
AlienRegistry.register(Mantis())
