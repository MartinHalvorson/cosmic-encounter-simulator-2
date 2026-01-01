"""
Milestone 5K Batch 4 Powers - Additional powers for 5000 milestone.
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

# Generate powers programmatically for batch 4
power_specs_batch4 = [
    ("Victorious_5K", "+5 offense", 5, Side.OFFENSE),
    ("Winning_5K", "+4 offense", 4, Side.OFFENSE),
    ("Champion_5K", "+5 always", 5, None),
    ("Conqueror_5K", "+5 offense", 5, Side.OFFENSE),
    ("Vanquisher_5K", "+4 offense", 4, Side.OFFENSE),
    ("Defender_5K", "+5 defense", 5, Side.DEFENSE),
    ("Protector_5K", "+4 defense", 4, Side.DEFENSE),
    ("Guardian_5K", "+4 defense", 4, Side.DEFENSE),
    ("Sentinel_5K", "+4 defense", 4, Side.DEFENSE),
    ("Warden_5K", "+3 defense", 3, Side.DEFENSE),
    ("Keeper_5K", "+3 always", 3, None),
    ("Watcher_5K", "+3 always", 3, None),
    ("Observer_5K", "+2 always", 2, None),
    ("Scout_5K", "+3 offense", 3, Side.OFFENSE),
    ("Ranger_5K", "+4 always", 4, None),
    ("Hunter_5K", "+4 offense", 4, Side.OFFENSE),
    ("Tracker_5K", "+3 always", 3, None),
    ("Pathfinder_5K", "+4 offense", 4, Side.OFFENSE),
    ("Explorer_5K", "+3 always", 3, None),
    ("Pioneer_5K", "+4 always", 4, None),
    ("Trailblazer_5K", "+4 offense", 4, Side.OFFENSE),
    ("Vanguard_5K", "+5 offense", 5, Side.OFFENSE),
    ("Forerunner_5K", "+4 always", 4, None),
    ("Harbinger_5K", "+4 always", 4, None),
    ("Herald_5K", "+3 always", 3, None),
    ("Envoy_5K", "+3 always", 3, None),
    ("Ambassador_5K", "+4 always", 4, None),
    ("Diplomat_5K", "+3 always", 3, None),
    ("Negotiator_5K", "+3 always", 3, None),
    ("Mediator_5K", "+3 always", 3, None),
]

MILESTONE_5K_BATCH4_POWERS = []

for name, desc, bonus, side in power_specs_batch4:
    @dataclass
    class Power(AlienPower):
        name: str = field(default=name, init=False)
        description: str = field(default=desc, init=False)
        timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
        power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
        category: PowerCategory = field(default=PowerCategory.GREEN if bonus <= 4 else PowerCategory.YELLOW, init=False)
        _bonus: int = field(default=bonus, init=False)
        _side: Side = field(default=side, init=False)

        def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
            if not player.power_active:
                return total
            if self._side is None or side == self._side:
                return total + self._bonus
            return total

    Power.__name__ = name
    Power.__qualname__ = name
    MILESTONE_5K_BATCH4_POWERS.append(Power)

for power_class in MILESTONE_5K_BATCH4_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
