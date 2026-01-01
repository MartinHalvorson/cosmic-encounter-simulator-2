"""
Final Push 5K Powers - Powers to reach 5000 milestone.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


# Batch 1 - Numbers
@dataclass
class Hundred(AlienPower):
    name: str = field(default="Hundred", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 2 if player.power_active else total

@dataclass
class Thousand(AlienPower):
    name: str = field(default="Thousand", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 3 if player.power_active else total

@dataclass
class Million(AlienPower):
    name: str = field(default="Million", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active else total

@dataclass
class Billion(AlienPower):
    name: str = field(default="Billion", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total

@dataclass
class Trillion(AlienPower):
    name: str = field(default="Trillion", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 6 if player.power_active else total

# Batch 2 - More concepts
@dataclass
class Infinity_5K(AlienPower):
    name: str = field(default="Infinity_5K", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total

@dataclass
class Zero_5K(AlienPower):
    name: str = field(default="Zero_5K", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 3 if player.power_active and side == Side.DEFENSE else total

@dataclass 
class Quadrillion(AlienPower):
    name: str = field(default="Quadrillion", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active and side == Side.OFFENSE else total

@dataclass
class Quintillion(AlienPower):
    name: str = field(default="Quintillion", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active and side == Side.OFFENSE else total

@dataclass
class Sextillion(AlienPower):
    name: str = field(default="Sextillion", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active else total

# Batch 3 - More types
@dataclass
class Googol(AlienPower):
    name: str = field(default="Googol", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total

@dataclass
class Googolplex(AlienPower):
    name: str = field(default="Googolplex", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 6 if player.power_active else total

@dataclass
class Myriad(AlienPower):
    name: str = field(default="Myriad", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 3 if player.power_active else total

@dataclass
class Countless(AlienPower):
    name: str = field(default="Countless", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active else total

@dataclass
class Immeasurable(AlienPower):
    name: str = field(default="Immeasurable", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total

@dataclass
class Incalculable(AlienPower):
    name: str = field(default="Incalculable", init=False)
    description: str = field(default="Random +3 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + random.randint(3, 6) if player.power_active else total

@dataclass
class Innumerable(AlienPower):
    name: str = field(default="Innumerable", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active else total

@dataclass
class Limitless_5K(AlienPower):
    name: str = field(default="Limitless_5K", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total

@dataclass
class Unbounded(AlienPower):
    name: str = field(default="Unbounded", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 4 if player.power_active else total

@dataclass
class Boundless_5K(AlienPower):
    name: str = field(default="Boundless_5K", init=False)
    description: str = field(default="+5 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 5 if player.power_active else total


# Register all
FINAL_PUSH_5K_POWERS = [
    Hundred, Thousand, Million, Billion, Trillion,
    Infinity_5K, Zero_5K, Quadrillion, Quintillion, Sextillion,
    Googol, Googolplex, Myriad, Countless, Immeasurable,
    Incalculable, Innumerable, Limitless_5K, Unbounded, Boundless_5K,
]

for power_class in FINAL_PUSH_5K_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
