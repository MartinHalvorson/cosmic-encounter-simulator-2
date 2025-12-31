"""
Transformation Powers - Aliens with shapeshifting and metamorphosis abilities.
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
class Adapter(AlienPower):
    """
    Adapter - Quick Change.
    Copy opponent's card value.
    """
    name: str = field(default="Adapter", init=False)
    description: str = field(default="Copy card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chameleon(AlienPower):
    """
    Chameleon - Blend In.
    Use another player's power.
    """
    name: str = field(default="Chameleon", init=False)
    description: str = field(default="Use other power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Evolver_Alt(AlienPower):
    """
    Evolver_Alt - Rapid Evolution.
    Gain abilities over time.
    """
    name: str = field(default="Evolver_Alt", init=False)
    description: str = field(default="Gain abilities.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Metamorph(AlienPower):
    """
    Metamorph - Complete Change.
    Become any alien for encounter.
    """
    name: str = field(default="Metamorph", init=False)
    description: str = field(default="Become any alien.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mimic_Alt(AlienPower):
    """
    Mimic_Alt - Perfect Copy.
    Duplicate opponent's last action.
    """
    name: str = field(default="Mimic_Alt", init=False)
    description: str = field(default="Copy last action.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Morpher(AlienPower):
    """
    Morpher - Shape Shift.
    Change ship count after commit.
    """
    name: str = field(default="Morpher", init=False)
    description: str = field(default="Change ship count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mutant(AlienPower):
    """
    Mutant - Random Evolution.
    Gain random bonus each encounter.
    """
    name: str = field(default="Mutant", init=False)
    description: str = field(default="Random bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add random bonus 0-6."""
        return total + random.randint(0, 6)


@dataclass
class Phoenix(AlienPower):
    """
    Phoenix - Rebirth.
    Return from warp as different power.
    """
    name: str = field(default="Phoenix", init=False)
    description: str = field(default="Rebirth power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Polymorph(AlienPower):
    """
    Polymorph - Many Forms.
    Choose power at start of turn.
    """
    name: str = field(default="Polymorph", init=False)
    description: str = field(default="Choose power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Reconstructor(AlienPower):
    """
    Reconstructor - Rebuild Self.
    Heal ships after battle.
    """
    name: str = field(default="Reconstructor", init=False)
    description: str = field(default="Heal ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reformer(AlienPower):
    """
    Reformer - Change Structure.
    Swap attack for negotiate.
    """
    name: str = field(default="Reformer", init=False)
    description: str = field(default="Swap card type.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shifter(AlienPower):
    """
    Shifter - Phase Shift.
    Move between dimensions.
    """
    name: str = field(default="Shifter", init=False)
    description: str = field(default="Phase shift.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Skinwalker(AlienPower):
    """
    Skinwalker - Steal Form.
    Take opponent's identity.
    """
    name: str = field(default="Skinwalker", init=False)
    description: str = field(default="Steal identity.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Transformer(AlienPower):
    """
    Transformer - Vehicle Mode.
    +4 when attacking, -2 defending.
    """
    name: str = field(default="Transformer", init=False)
    description: str = field(default="+4 attack/-2 defend.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking, -2 defending."""
        if side == Side.OFFENSE:
            return total + 4
        else:
            return total - 2


@dataclass
class Transmuter(AlienPower):
    """
    Transmuter - Change Matter.
    Convert cards to different type.
    """
    name: str = field(default="Transmuter", init=False)
    description: str = field(default="Convert cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Werewolf(AlienPower):
    """
    Werewolf - Beast Mode.
    Double attack on odd turns.
    """
    name: str = field(default="Werewolf", init=False)
    description: str = field(default="Double odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Adapter())
AlienRegistry.register(Chameleon())
AlienRegistry.register(Evolver_Alt())
AlienRegistry.register(Metamorph())
AlienRegistry.register(Mimic_Alt())
AlienRegistry.register(Morpher())
AlienRegistry.register(Mutant())
AlienRegistry.register(Phoenix())
AlienRegistry.register(Polymorph())
AlienRegistry.register(Reconstructor())
AlienRegistry.register(Reformer())
AlienRegistry.register(Shifter())
AlienRegistry.register(Skinwalker())
AlienRegistry.register(Transformer())
AlienRegistry.register(Transmuter())
AlienRegistry.register(Werewolf())
