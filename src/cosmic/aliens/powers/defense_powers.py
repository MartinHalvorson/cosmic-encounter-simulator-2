"""
Defense Powers - Aliens with strong defensive abilities.
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
class Absorb(AlienPower):
    """
    Absorb - Take Hits.
    Reduce damage taken.
    """
    name: str = field(default="Absorb", init=False)
    description: str = field(default="Reduce damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Barrier(AlienPower):
    """
    Barrier - Block Attack.
    +5 when defending.
    """
    name: str = field(default="Barrier", init=False)
    description: str = field(default="+5 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when defending."""
        if side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Blocker_Alt(AlienPower):
    """
    Blocker_Alt - Stop Attacks.
    Cancel one attack per turn.
    """
    name: str = field(default="Blocker_Alt", init=False)
    description: str = field(default="Cancel attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bouncer(AlienPower):
    """
    Bouncer - Reflect Attack.
    Send attacker to warp.
    """
    name: str = field(default="Bouncer", init=False)
    description: str = field(default="Reflect to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Buffer(AlienPower):
    """
    Buffer - Protection Layer.
    First 3 ships immune.
    """
    name: str = field(default="Buffer", init=False)
    description: str = field(default="3 ships immune.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Defender(AlienPower):
    """
    Defender - Strong Defense.
    +3 defending home.
    """
    name: str = field(default="Defender", init=False)
    description: str = field(default="+3 home defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Deflect(AlienPower):
    """
    Deflect - Turn Away.
    Redirect attack to ally.
    """
    name: str = field(default="Deflect", init=False)
    description: str = field(default="Redirect attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Endurer(AlienPower):
    """
    Endurer - Last Long.
    Ships return after 2 turns.
    """
    name: str = field(default="Endurer", init=False)
    description: str = field(default="Ships return.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fortifier(AlienPower):
    """
    Fortifier - Build Walls.
    +2 per colony.
    """
    name: str = field(default="Fortifier", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Guard(AlienPower):
    """
    Guard - Protect Allies.
    Take hits for allies.
    """
    name: str = field(default="Guard", init=False)
    description: str = field(default="Protect allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hardener(AlienPower):
    """
    Hardener - Tough Exterior.
    Reduce all damage by 2.
    """
    name: str = field(default="Hardener", init=False)
    description: str = field(default="-2 damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Immunizer(AlienPower):
    """
    Immunizer - Immunity.
    Immune to one power.
    """
    name: str = field(default="Immunizer", init=False)
    description: str = field(default="Power immunity.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Parry(AlienPower):
    """
    Parry - Block Strike.
    Negate attack bonus.
    """
    name: str = field(default="Parry", init=False)
    description: str = field(default="Negate bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Protector(AlienPower):
    """
    Protector - Shield Others.
    Allies gain +2.
    """
    name: str = field(default="Protector", init=False)
    description: str = field(default="Allies +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reflector(AlienPower):
    """
    Reflector - Mirror Damage.
    Return damage to attacker.
    """
    name: str = field(default="Reflector", init=False)
    description: str = field(default="Mirror damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Resistor(AlienPower):
    """
    Resistor - Resist Effects.
    Immune to card effects.
    """
    name: str = field(default="Resistor", init=False)
    description: str = field(default="Effect immunity.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shielder(AlienPower):
    """
    Shielder - Energy Shield.
    Block first attack.
    """
    name: str = field(default="Shielder", init=False)
    description: str = field(default="Block first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stopper(AlienPower):
    """
    Stopper - Stop Advance.
    Prevent colony gain.
    """
    name: str = field(default="Stopper", init=False)
    description: str = field(default="Block colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wall(AlienPower):
    """
    Wall - Solid Defense.
    Win ties defending.
    """
    name: str = field(default="Wall", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Absorb())
AlienRegistry.register(Barrier())
AlienRegistry.register(Blocker_Alt())
AlienRegistry.register(Bouncer())
AlienRegistry.register(Buffer())
AlienRegistry.register(Defender())
AlienRegistry.register(Deflect())
AlienRegistry.register(Endurer())
AlienRegistry.register(Fortifier())
AlienRegistry.register(Guard())
AlienRegistry.register(Hardener())
AlienRegistry.register(Immunizer())
AlienRegistry.register(Parry())
AlienRegistry.register(Protector())
AlienRegistry.register(Reflector())
AlienRegistry.register(Resistor())
AlienRegistry.register(Shielder())
AlienRegistry.register(Stopper())
AlienRegistry.register(Wall())
