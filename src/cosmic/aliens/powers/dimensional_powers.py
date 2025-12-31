"""
Dimensional Powers - Aliens with reality-bending abilities.
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
class Bender(AlienPower):
    """
    Bender - Reality Bender.
    Swap two planets' ships.
    """
    name: str = field(default="Bender", init=False)
    description: str = field(default="Swap planet ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Dimension(AlienPower):
    """
    Dimension - Dimension Hopper.
    Your ships return to any colony on loss.
    """
    name: str = field(default="Dimension", init=False)
    description: str = field(default="Ships return anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Distorter(AlienPower):
    """
    Distorter - Space Distortion.
    Target any planet regardless of destiny.
    """
    name: str = field(default="Distorter", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Folder(AlienPower):
    """
    Folder - Space Folder.
    Colonies count as adjacent for ship movement.
    """
    name: str = field(default="Folder", init=False)
    description: str = field(default="Colonies adjacent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Merger(AlienPower):
    """
    Merger - Dimension Merger.
    Combine two of your encounter cards.
    """
    name: str = field(default="Merger", init=False)
    description: str = field(default="Combine two cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Multitude(AlienPower):
    """
    Multitude - Many Forms.
    Ships count as 1.5 (round up).
    """
    name: str = field(default="Multitude", init=False)
    description: str = field(default="Ships x1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Parallax(AlienPower):
    """
    Parallax - Parallel Self.
    Copy your previous encounter card.
    """
    name: str = field(default="Parallax", init=False)
    description: str = field(default="Copy previous card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Phaser(AlienPower):
    """
    Phaser - Phase Shift.
    Ships immune to warp this encounter.
    """
    name: str = field(default="Phaser", init=False)
    description: str = field(default="Ships can't go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Portal(AlienPower):
    """
    Portal - Gateway.
    Ships attack from any colony.
    """
    name: str = field(default="Portal", init=False)
    description: str = field(default="Attack from anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rift(AlienPower):
    """
    Rift - Space Tear.
    Ships lost go to different player's warp.
    """
    name: str = field(default="Rift", init=False)
    description: str = field(default="Redirect lost ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shifter(AlienPower):
    """
    Shifter - Reality Shift.
    Swap card values with opponent after reveal.
    """
    name: str = field(default="Shifter", init=False)
    description: str = field(default="Swap card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Splitter(AlienPower):
    """
    Splitter - Dimension Split.
    Attack two targets simultaneously.
    """
    name: str = field(default="Splitter", init=False)
    description: str = field(default="Attack two targets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Temporal(AlienPower):
    """
    Temporal - Time Control.
    Replay last encounter with same cards.
    """
    name: str = field(default="Temporal", init=False)
    description: str = field(default="Replay encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Transposer(AlienPower):
    """
    Transposer - Position Swap.
    Swap positions with opponent ship.
    """
    name: str = field(default="Transposer", init=False)
    description: str = field(default="Swap ship positions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Twister(AlienPower):
    """
    Twister - Reality Twist.
    Reverse attack and negotiate card meanings.
    """
    name: str = field(default="Twister", init=False)
    description: str = field(default="Reverse card meanings.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Unmaker(AlienPower):
    """
    Unmaker - Reality Unmaking.
    Cancel the encounter result.
    """
    name: str = field(default="Unmaker", init=False)
    description: str = field(default="Cancel encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Vortex(AlienPower):
    """
    Vortex - Dimensional Vortex.
    Pull ships from opponent colonies.
    """
    name: str = field(default="Vortex", init=False)
    description: str = field(default="Pull opposing ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Bender())
AlienRegistry.register(Dimension())
AlienRegistry.register(Distorter())
AlienRegistry.register(Folder())
AlienRegistry.register(Merger())
AlienRegistry.register(Multitude())
AlienRegistry.register(Parallax())
AlienRegistry.register(Phaser())
AlienRegistry.register(Portal())
AlienRegistry.register(Rift())
AlienRegistry.register(Shifter())
AlienRegistry.register(Splitter())
AlienRegistry.register(Temporal())
AlienRegistry.register(Transposer())
AlienRegistry.register(Twister())
AlienRegistry.register(Unmaker())
AlienRegistry.register(Vortex())
