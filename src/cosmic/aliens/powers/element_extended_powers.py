"""
Element Extended Powers - More elemental themed aliens.
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
class Plasma(AlienPower):
    """Plasma - Power of Ionization. +4 on offense."""
    name: str = field(default="Plasma", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Magma(AlienPower):
    """Magma - Power of Heat. Destroy ships."""
    name: str = field(default="Magma", init=False)
    description: str = field(default="1 ship removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dust(AlienPower):
    """Dust - Power of Particles. +1 per ship in warp."""
    name: str = field(default="Dust", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Steam(AlienPower):
    """Steam - Power of Pressure. +3 always."""
    name: str = field(default="Steam", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Frost(AlienPower):
    """Frost - Power of Cold. Slow opponent."""
    name: str = field(default="Frost", init=False)
    description: str = field(default="Opponent commits 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ember(AlienPower):
    """Ember - Power of Smoldering. +2 constant."""
    name: str = field(default="Ember", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Mist(AlienPower):
    """Mist - Power of Obscurity. Hide card."""
    name: str = field(default="Mist", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spark(AlienPower):
    """Spark - Power of Ignition. Random bonus."""
    name: str = field(default="Spark", init=False)
    description: str = field(default="Random +1 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 6)
        return total


@dataclass
class Ash(AlienPower):
    """Ash - Power of Remains. Return from discard."""
    name: str = field(default="Ash", init=False)
    description: str = field(default="Draw from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Vapor(AlienPower):
    """Vapor - Power of Escape. Ships avoid warp."""
    name: str = field(default="Vapor", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mud(AlienPower):
    """Mud - Power of Slowing. -2 to opponent."""
    name: str = field(default="Mud", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Crystal(AlienPower):
    """Crystal - Power of Clarity. See all cards."""
    name: str = field(default="Crystal", init=False)
    description: str = field(default="See all hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smoke(AlienPower):
    """Smoke - Power of Confusion. -1 per ally."""
    name: str = field(default="Smoke", init=False)
    description: str = field(default="Opponent -1 per their ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Acid(AlienPower):
    """Acid - Power of Corrosion. Reduce cards."""
    name: str = field(default="Acid", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Slime(AlienPower):
    """Slime - Power of Stickiness. Lock ships."""
    name: str = field(default="Slime", init=False)
    description: str = field(default="Ships on your planets stay.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tar(AlienPower):
    """Tar - Power of Trapping. Slow movement."""
    name: str = field(default="Tar", init=False)
    description: str = field(default="Attacker commits 1 fewer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ooze(AlienPower):
    """Ooze - Power of Spreading. +1 per colony."""
    name: str = field(default="Ooze", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Goo(AlienPower):
    """Goo - Power of Adhesion. Hold cards."""
    name: str = field(default="Goo", init=False)
    description: str = field(default="Never discard down.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sludge(AlienPower):
    """Sludge - Power of Pollution. -3 to all opponents."""
    name: str = field(default="Sludge", init=False)
    description: str = field(default="All opponents -1 in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oil(AlienPower):
    """Oil - Power of Slipperiness. Escape encounters."""
    name: str = field(default="Oil", init=False)
    description: str = field(default="Withdraw before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
ELEMENT_EXTENDED_POWERS = [
    Plasma, Magma, Dust, Steam, Frost, Ember, Mist, Spark, Ash, Vapor,
    Mud, Crystal, Smoke, Acid, Slime, Tar, Ooze, Goo, Sludge, Oil,
]

for power_class in ELEMENT_EXTENDED_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
