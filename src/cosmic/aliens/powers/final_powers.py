"""
Final Powers - Miscellaneous powers to reach 2000+.
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
class Winner(AlienPower):
    """Winner - Power of Victory. +4 always."""
    name: str = field(default="Winner", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Loser(AlienPower):
    """Loser - Power of Desperation. +8 when behind."""
    name: str = field(default="Loser", init=False)
    description: str = field(default="+8 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Average(AlienPower):
    """Average - Power of the Middle. +3 always."""
    name: str = field(default="Average", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Random_Alt(AlienPower):
    """Random_Alt - Power of Chaos. Random -3 to +7."""
    name: str = field(default="Random_Alt", init=False)
    description: str = field(default="Random -3 to +7.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return max(0, total + random.randint(-3, 7))
        return total


@dataclass
class Predictable(AlienPower):
    """Predictable - Power of Consistency. +2 always."""
    name: str = field(default="Predictable", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Chaos_Final(AlienPower):
    """Chaos_Final - Power of Entropy. Random +1 to +8."""
    name: str = field(default="Chaos_Final", init=False)
    description: str = field(default="Random +1 to +8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + random.randint(1, 8)
        return total


@dataclass
class Order_Final(AlienPower):
    """Order_Final - Power of Structure. +3 on defense."""
    name: str = field(default="Order_Final", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Balance_Final(AlienPower):
    """Balance_Final - Power of Equilibrium. Win ties."""
    name: str = field(default="Balance_Final", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Extremist_Final(AlienPower):
    """Extremist_Final - Power of Edges. +5 with high/low cards."""
    name: str = field(default="Extremist_Final", init=False)
    description: str = field(default="+5 when card under 5 or over 15.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Moderate(AlienPower):
    """Moderate - Power of Center. +4 with medium cards."""
    name: str = field(default="Moderate", init=False)
    description: str = field(default="+4 when card is 8-12.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Attacker_Final(AlienPower):
    """Attacker_Final - Power of Offense. +5 on offense."""
    name: str = field(default="Attacker_Final", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Defender_Final(AlienPower):
    """Defender_Final - Power of Defense. +5 on defense."""
    name: str = field(default="Defender_Final", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Neutral(AlienPower):
    """Neutral - Power of Impartiality. +2 always."""
    name: str = field(default="Neutral", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Positive(AlienPower):
    """Positive - Power of Optimism. +3 always."""
    name: str = field(default="Positive", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Negative(AlienPower):
    """Negative - Power of Pessimism. -2 to opponent."""
    name: str = field(default="Negative", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class First(AlienPower):
    """First - Power of Priority. +5 first encounter."""
    name: str = field(default="First", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Last(AlienPower):
    """Last - Power of Finale. +5 second encounter."""
    name: str = field(default="Last", init=False)
    description: str = field(default="+5 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Middle(AlienPower):
    """Middle - Power of Center. +3 always."""
    name: str = field(default="Middle", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Almighty(AlienPower):
    """Almighty - Power of Power. +6 constant."""
    name: str = field(default="Almighty", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Humble(AlienPower):
    """Humble - Power of Modesty. +5 with low cards."""
    name: str = field(default="Humble", init=False)
    description: str = field(default="+5 when card under 8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Proud(AlienPower):
    """Proud - Power of Pride. +4 when ahead."""
    name: str = field(default="Proud", init=False)
    description: str = field(default="+4 when ahead in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ally_Final(AlienPower):
    """Ally_Final - Power of Friendship. +2 per ally."""
    name: str = field(default="Ally_Final", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Solo(AlienPower):
    """Solo - Power of Independence. +6 when alone."""
    name: str = field(default="Solo", init=False)
    description: str = field(default="+6 when no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Team(AlienPower):
    """Team - Power of Cooperation. +1 per ally ship."""
    name: str = field(default="Team", init=False)
    description: str = field(default="+1 per allied ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
FINAL_POWERS = [
    Winner, Loser, Average, Random_Alt, Predictable, Chaos_Final, Order_Final,
    Balance_Final, Extremist_Final, Moderate, Attacker_Final, Defender_Final,
    Neutral, Positive, Negative, First, Last, Middle, Almighty, Humble, Proud,
    Ally_Final, Solo, Team,
]

for power_class in FINAL_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
