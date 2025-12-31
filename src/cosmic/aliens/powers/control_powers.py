"""
Control Powers - Aliens with domination and manipulation abilities.
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
class Authority(AlienPower):
    """
    Authority - Command Power.
    Force opponent actions.
    """
    name: str = field(default="Authority", init=False)
    description: str = field(default="Force actions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Binder(AlienPower):
    """
    Binder - Lock Powers.
    Prevent power usage.
    """
    name: str = field(default="Binder", init=False)
    description: str = field(default="Lock powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Commander_Alt(AlienPower):
    """
    Commander_Alt - Lead Forces.
    Direct ally movements.
    """
    name: str = field(default="Commander_Alt", init=False)
    description: str = field(default="Direct allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Compeller(AlienPower):
    """
    Compeller - Force Compliance.
    Make opponent play specific card.
    """
    name: str = field(default="Compeller", init=False)
    description: str = field(default="Force card play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Controller(AlienPower):
    """
    Controller - Total Control.
    Manipulate game flow.
    """
    name: str = field(default="Controller", init=False)
    description: str = field(default="Control flow.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Director(AlienPower):
    """
    Director - Stage Manager.
    Choose encounter order.
    """
    name: str = field(default="Director", init=False)
    description: str = field(default="Set order.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Enslaver(AlienPower):
    """
    Enslaver - Take Control.
    Control opponent ships.
    """
    name: str = field(default="Enslaver", init=False)
    description: str = field(default="Control ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Handler(AlienPower):
    """
    Handler - Manage Others.
    Redirect opponent attacks.
    """
    name: str = field(default="Handler", init=False)
    description: str = field(default="Redirect attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Manipulator(AlienPower):
    """
    Manipulator - Subtle Control.
    Change encounter results.
    """
    name: str = field(default="Manipulator", init=False)
    description: str = field(default="Change results.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Master_Alt(AlienPower):
    """
    Master_Alt - Supreme Control.
    Override any decision.
    """
    name: str = field(default="Master_Alt", init=False)
    description: str = field(default="Override decisions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Oppressor(AlienPower):
    """
    Oppressor - Crush Opposition.
    Weaken opponent powers.
    """
    name: str = field(default="Oppressor", init=False)
    description: str = field(default="Weaken powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Overruler(AlienPower):
    """
    Overruler - Veto Power.
    Cancel opponent actions.
    """
    name: str = field(default="Overruler", init=False)
    description: str = field(default="Cancel actions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Puppeteer(AlienPower):
    """
    Puppeteer - Control Strings.
    Move opponent ships.
    """
    name: str = field(default="Puppeteer", init=False)
    description: str = field(default="Move opponent ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ruler_Alt(AlienPower):
    """
    Ruler_Alt - Kingdom Builder.
    +2 per home colony.
    """
    name: str = field(default="Ruler_Alt", init=False)
    description: str = field(default="+2 per home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Subjugator(AlienPower):
    """
    Subjugator - Force Submission.
    Convert opponents to allies.
    """
    name: str = field(default="Subjugator", init=False)
    description: str = field(default="Convert opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Suppressor(AlienPower):
    """
    Suppressor - Power Shutdown.
    Disable all powers this encounter.
    """
    name: str = field(default="Suppressor", init=False)
    description: str = field(default="Disable powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Taskmaster(AlienPower):
    """
    Taskmaster - Drive Workers.
    Force ship commitments.
    """
    name: str = field(default="Taskmaster", init=False)
    description: str = field(default="Force commitments.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Authority())
AlienRegistry.register(Binder())
AlienRegistry.register(Commander_Alt())
AlienRegistry.register(Compeller())
AlienRegistry.register(Controller())
AlienRegistry.register(Director())
AlienRegistry.register(Enslaver())
AlienRegistry.register(Handler())
AlienRegistry.register(Manipulator())
AlienRegistry.register(Master_Alt())
AlienRegistry.register(Oppressor())
AlienRegistry.register(Overruler())
AlienRegistry.register(Puppeteer())
AlienRegistry.register(Ruler_Alt())
AlienRegistry.register(Subjugator())
AlienRegistry.register(Suppressor())
AlienRegistry.register(Taskmaster())
