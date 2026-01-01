"""
Body and Physical themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Brain(AlienPower):
    """Brain - Power of Intellect."""
    name: str = field(default="Brain", init=False)
    description: str = field(
        default="Look at opponent's hand before selecting your card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Heart(AlienPower):
    """Heart - Power of Courage."""
    name: str = field(default="Heart", init=False)
    description: str = field(
        default="+3 when you have fewer colonies than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Muscle(AlienPower):
    """Muscle - Power of Strength."""
    name: str = field(default="Muscle", init=False)
    description: str = field(
        default="+1 for each ship you have in the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bone(AlienPower):
    """Bone - Power of Structure."""
    name: str = field(default="Bone", init=False)
    description: str = field(
        default="Ships return from warp to colonies instead of home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skin(AlienPower):
    """Skin - Power of Protection."""
    name: str = field(default="Skin", init=False)
    description: str = field(
        default="First ship lost each encounter goes to colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nerve(AlienPower):
    """Nerve - Power of Sensation."""
    name: str = field(default="Nerve", init=False)
    description: str = field(
        default="Know when opponent is bluffing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blood(AlienPower):
    """Blood - Power of Vitality."""
    name: str = field(default="Blood", init=False)
    description: str = field(
        default="Regain 1 ship from warp when you win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lung(AlienPower):
    """Lung - Power of Breath."""
    name: str = field(default="Lung", init=False)
    description: str = field(
        default="Draw 1 card at the start of each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Liver(AlienPower):
    """Liver - Power of Filtering."""
    name: str = field(default="Liver", init=False)
    description: str = field(
        default="Remove 1 card from opponent's hand at random.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stomach(AlienPower):
    """Stomach - Power of Digestion."""
    name: str = field(default="Stomach", init=False)
    description: str = field(
        default="Consume opponent's reinforcements.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spine(AlienPower):
    """Spine - Power of Support."""
    name: str = field(default="Spine", init=False)
    description: str = field(
        default="Allied ships count as +2 each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kidney(AlienPower):
    """Kidney - Power of Balance."""
    name: str = field(default="Kidney", init=False)
    description: str = field(
        default="Equalize ships on both sides before combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cell(AlienPower):
    """Cell - Power of Division."""
    name: str = field(default="Cell", init=False)
    description: str = field(
        default="Double your ships once per game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tissue(AlienPower):
    """Tissue - Power of Regeneration."""
    name: str = field(default="Tissue", init=False)
    description: str = field(
        default="Regain 2 ships from warp when you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Brain())
AlienRegistry.register(Heart())
AlienRegistry.register(Muscle())
AlienRegistry.register(Bone())
AlienRegistry.register(Skin())
AlienRegistry.register(Nerve())
AlienRegistry.register(Blood())
AlienRegistry.register(Lung())
AlienRegistry.register(Liver())
AlienRegistry.register(Stomach())
AlienRegistry.register(Spine())
AlienRegistry.register(Kidney())
AlienRegistry.register(Cell())
AlienRegistry.register(Tissue())
