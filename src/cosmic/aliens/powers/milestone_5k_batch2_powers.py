"""
Milestone 5K Batch 2 Powers - Additional powers for 5000 milestone.
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

# Generate powers programmatically for batch 2
power_specs_batch2 = [
    ("Stellar_5K", "+4 always", 4, None),
    ("Lunar_5K", "+3 always", 3, None),
    ("Solar_5K", "+5 always", 5, None),
    ("Cosmic_5K", "+5 always", 5, None),
    ("Galactic_5K", "+4 always", 4, None),
    ("Nebular_5K", "+3 always", 3, None),
    ("Quasar_5K", "+5 offense", 5, Side.OFFENSE),
    ("Pulsar_5K", "+4 offense", 4, Side.OFFENSE),
    ("Nova_5K", "+5 offense", 5, Side.OFFENSE),
    ("Meteor_5K", "+4 offense", 4, Side.OFFENSE),
    ("Comet_5K", "+3 offense", 3, Side.OFFENSE),
    ("Asteroid_5K", "+3 defense", 3, Side.DEFENSE),
    ("Planet_5K", "+4 defense", 4, Side.DEFENSE),
    ("Moon_5K", "+3 defense", 3, Side.DEFENSE),
    ("Star_5K", "+5 defense", 5, Side.DEFENSE),
    ("Sun_5K", "+5 always", 5, None),
    ("Galaxy_5K", "+5 always", 5, None),
    ("Universe_5K", "+6 always", 6, None),
    ("Dimension_5K", "+4 always", 4, None),
    ("Reality_5K", "+4 always", 4, None),
    ("Existence_5K", "+5 always", 5, None),
    ("Eternity_5K", "+5 always", 5, None),
    ("Perpetual_5K", "+4 always", 4, None),
    ("Eternal_5K", "+5 always", 5, None),
    ("Infinite_5K", "+6 always", 6, None),
    ("Endless_5K", "+5 always", 5, None),
    ("Timeless_5K", "+4 always", 4, None),
    ("Ageless_5K", "+4 always", 4, None),
    ("Immortal_5K", "+5 always", 5, None),
    ("Divine_5K", "+5 always", 5, None),
]

MILESTONE_5K_BATCH2_POWERS = []

for name, desc, bonus, side in power_specs_batch2:
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
    MILESTONE_5K_BATCH2_POWERS.append(Power)

for power_class in MILESTONE_5K_BATCH2_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
