"""
Survival Powers - Aliens with defensive and survivability abilities.
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
class Armor(AlienPower):
    """
    Armor - Protected.
    First 2 ships immune to warp.
    """
    name: str = field(default="Armor", init=False)
    description: str = field(default="2 ships immune.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cockroach(AlienPower):
    """
    Cockroach - Survivor.
    Always keep at least 1 ship per colony.
    """
    name: str = field(default="Cockroach", init=False)
    description: str = field(default="1 ship survives.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Escape(AlienPower):
    """
    Escape - Quick Exit.
    Ships return to colonies instead of warp.
    """
    name: str = field(default="Escape", init=False)
    description: str = field(default="Ships return home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Evade(AlienPower):
    """
    Evade - Dodge Attack.
    50% chance to avoid ship loss.
    """
    name: str = field(default="Evade", init=False)
    description: str = field(default="50% avoid loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fortress_Alt(AlienPower):
    """
    Fortress_Alt - Strong Defense.
    +5 when defending home planets.
    """
    name: str = field(default="Fortress_Alt", init=False)
    description: str = field(default="+5 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hide(AlienPower):
    """
    Hide - Concealment.
    Opponent doesn't know your ships.
    """
    name: str = field(default="Hide", init=False)
    description: str = field(default="Hidden ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Persist(AlienPower):
    """
    Persist - Never Give Up.
    Retry failed encounter once.
    """
    name: str = field(default="Persist", init=False)
    description: str = field(default="Retry once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Recover(AlienPower):
    """
    Recover - Quick Heal.
    Retrieve 1 ship after each encounter.
    """
    name: str = field(default="Recover", init=False)
    description: str = field(default="Retrieve 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Regenerator(AlienPower):
    """
    Regenerator - Regrow.
    Return all ships from warp on your turn.
    """
    name: str = field(default="Regenerator", init=False)
    description: str = field(default="All ships return.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Resilient(AlienPower):
    """
    Resilient - Bounce Back.
    Draw card when losing ships.
    """
    name: str = field(default="Resilient", init=False)
    description: str = field(default="Draw on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Runaway(AlienPower):
    """
    Runaway - Flee Battle.
    Cancel encounter, ships return.
    """
    name: str = field(default="Runaway", init=False)
    description: str = field(default="Flee encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shelter(AlienPower):
    """
    Shelter - Safe Haven.
    Ships go to home colony not warp.
    """
    name: str = field(default="Shelter", init=False)
    description: str = field(default="Ships go home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shield_Alt(AlienPower):
    """
    Shield_Alt - Deflection.
    Reduce damage by 2.
    """
    name: str = field(default="Shield_Alt", init=False)
    description: str = field(default="Reduce loss by 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Survivor_Alt(AlienPower):
    """
    Survivor_Alt - Last One Standing.
    Gain power when near elimination.
    """
    name: str = field(default="Survivor_Alt", init=False)
    description: str = field(default="Power at low ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tenacious(AlienPower):
    """
    Tenacious - Hold On.
    Keep 1 colony even if all ships lost.
    """
    name: str = field(default="Tenacious", init=False)
    description: str = field(default="Keep 1 colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Armor())
AlienRegistry.register(Cockroach())
AlienRegistry.register(Escape())
AlienRegistry.register(Evade())
AlienRegistry.register(Fortress_Alt())
AlienRegistry.register(Hide())
AlienRegistry.register(Persist())
AlienRegistry.register(Recover())
AlienRegistry.register(Regenerator())
AlienRegistry.register(Resilient())
AlienRegistry.register(Runaway())
AlienRegistry.register(Shelter())
AlienRegistry.register(Shield_Alt())
AlienRegistry.register(Survivor_Alt())
AlienRegistry.register(Tenacious())
