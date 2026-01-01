"""
Reaction Powers - Chemical and emotional reaction themed aliens.
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
class Explosive(AlienPower):
    """Explosive - Power of Explosion. +5 on offense."""
    name: str = field(default="Explosive", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Inert(AlienPower):
    """Inert - Power of Stability. +4 on defense."""
    name: str = field(default="Inert", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Catalytic(AlienPower):
    """Catalytic - Power of Catalysis. +2 per ally."""
    name: str = field(default="Catalytic", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Reactive(AlienPower):
    """Reactive - Power of Reaction. +3 always."""
    name: str = field(default="Reactive", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Volatile(AlienPower):
    """Volatile - Power of Instability. Random +/- 5."""
    name: str = field(default="Volatile", init=False)
    description: str = field(default="Random -5 to +5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return max(0, total + random.randint(-5, 5))
        return total


@dataclass
class Stable_Alt(AlienPower):
    """Stable_Alt - Power of Stability. +4 always."""
    name: str = field(default="Stable_Alt", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Corrosive(AlienPower):
    """Corrosive - Power of Corrosion. -3 to opponent."""
    name: str = field(default="Corrosive", init=False)
    description: str = field(default="Opponent gets -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Neutralizing(AlienPower):
    """Neutralizing - Power of Neutralization. -2 to attacker."""
    name: str = field(default="Neutralizing", init=False)
    description: str = field(default="Attacker gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Oxidizing(AlienPower):
    """Oxidizing - Power of Oxidation. +4 on offense."""
    name: str = field(default="Oxidizing", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Reducing(AlienPower):
    """Reducing - Power of Reduction. Lose 1 fewer ship."""
    name: str = field(default="Reducing", init=False)
    description: str = field(default="Lose 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Binding(AlienPower):
    """Binding - Power of Bonds. +1 per ship."""
    name: str = field(default="Binding", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dissolving(AlienPower):
    """Dissolving - Power of Dissolution. See opponent card."""
    name: str = field(default="Dissolving", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Precipitating(AlienPower):
    """Precipitating - Power of Precipitation. Extra card draw."""
    name: str = field(default="Precipitating", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Combusting(AlienPower):
    """Combusting - Power of Combustion. +6 always."""
    name: str = field(default="Combusting", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Synthesizing(AlienPower):
    """Synthesizing - Power of Synthesis. +3 with allies."""
    name: str = field(default="Synthesizing", init=False)
    description: str = field(default="+3 when you have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
REACTION_POWERS = [
    Explosive, Inert, Catalytic, Reactive, Volatile, Stable_Alt, Corrosive,
    Neutralizing, Oxidizing, Reducing, Binding, Dissolving, Precipitating,
    Combusting, Synthesizing,
]

for power_class in REACTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
