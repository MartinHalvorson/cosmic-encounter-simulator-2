"""
Territory Powers - Aliens with land control and territorial abilities.
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
class Border(AlienPower):
    """
    Border - Guard Border.
    +2 defending each planet.
    """
    name: str = field(default="Border", init=False)
    description: str = field(default="+2 per planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Claimer(AlienPower):
    """
    Claimer - Stake Claim.
    Extra colony on win.
    """
    name: str = field(default="Claimer", init=False)
    description: str = field(default="Extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Conqueror_Alt(AlienPower):
    """
    Conqueror_Alt - Take Land.
    Win ties as attacker.
    """
    name: str = field(default="Conqueror_Alt", init=False)
    description: str = field(default="Win ties attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Expander_Alt(AlienPower):
    """
    Expander_Alt - Grow Territory.
    Planets worth +1 each.
    """
    name: str = field(default="Expander_Alt", init=False)
    description: str = field(default="Planets +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Frontier(AlienPower):
    """
    Frontier - Push Frontier.
    Attack any system.
    """
    name: str = field(default="Frontier", init=False)
    description: str = field(default="Attack anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Homesteader(AlienPower):
    """
    Homesteader - Settle Land.
    Free colony when attacked.
    """
    name: str = field(default="Homesteader", init=False)
    description: str = field(default="Free colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Landlord(AlienPower):
    """
    Landlord - Own Land.
    Charge rent for colonies.
    """
    name: str = field(default="Landlord", init=False)
    description: str = field(default="Charge rent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mapper(AlienPower):
    """
    Mapper - Know Territory.
    See all planet locations.
    """
    name: str = field(default="Mapper", init=False)
    description: str = field(default="See all planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nomad_Alt(AlienPower):
    """
    Nomad_Alt - Roam Free.
    Move colonies freely.
    """
    name: str = field(default="Nomad_Alt", init=False)
    description: str = field(default="Move colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Occupier(AlienPower):
    """
    Occupier - Hold Ground.
    Resist removal.
    """
    name: str = field(default="Occupier", init=False)
    description: str = field(default="Resist removal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pioneer(AlienPower):
    """
    Pioneer - First Settler.
    +3 on empty planets.
    """
    name: str = field(default="Pioneer", init=False)
    description: str = field(default="+3 empty planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Settler_Alt(AlienPower):
    """
    Settler_Alt - Build Settlement.
    Double colony ships.
    """
    name: str = field(default="Settler_Alt", init=False)
    description: str = field(default="Double ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sovereign(AlienPower):
    """
    Sovereign - Rule Land.
    Own planets absolutely.
    """
    name: str = field(default="Sovereign", init=False)
    description: str = field(default="Absolute ownership.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Squatter(AlienPower):
    """
    Squatter - Occupy Free.
    Free colony anywhere.
    """
    name: str = field(default="Squatter", init=False)
    description: str = field(default="Free placement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Warden(AlienPower):
    """
    Warden - Guard Territory.
    Protect all colonies.
    """
    name: str = field(default="Warden", init=False)
    description: str = field(default="Protect colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Border())
AlienRegistry.register(Claimer())
AlienRegistry.register(Conqueror_Alt())
AlienRegistry.register(Expander_Alt())
AlienRegistry.register(Frontier())
AlienRegistry.register(Homesteader())
AlienRegistry.register(Landlord())
AlienRegistry.register(Mapper())
AlienRegistry.register(Nomad_Alt())
AlienRegistry.register(Occupier())
AlienRegistry.register(Pioneer())
AlienRegistry.register(Settler_Alt())
AlienRegistry.register(Sovereign())
AlienRegistry.register(Squatter())
AlienRegistry.register(Warden())
