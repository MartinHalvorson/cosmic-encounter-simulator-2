"""
Milestone 5K Batch 3 Powers - Additional powers for 5000 milestone.
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

# Generate powers programmatically for batch 3
power_specs_batch3 = [
    ("Celestial_5K", "+5 always", 5, None),
    ("Heavenly_5K", "+4 always", 4, None),
    ("Sacred_5K", "+4 always", 4, None),
    ("Holy_5K", "+4 always", 4, None),
    ("Blessed_5K", "+3 always", 3, None),
    ("Virtuous_5K", "+3 always", 3, None),
    ("Noble_5K", "+4 always", 4, None),
    ("Royal_5K", "+5 always", 5, None),
    ("Majestic_5K", "+5 always", 5, None),
    ("Imperial_5K", "+5 always", 5, None),
    ("Sovereign_5K", "+4 always", 4, None),
    ("Regal_5K", "+4 always", 4, None),
    ("Kingly_5K", "+4 offense", 4, Side.OFFENSE),
    ("Queenly_5K", "+4 defense", 4, Side.DEFENSE),
    ("Princely_5K", "+3 always", 3, None),
    ("Lordly_5K", "+4 always", 4, None),
    ("Baronial_5K", "+3 always", 3, None),
    ("Ducal_5K", "+4 always", 4, None),
    ("Knightly_5K", "+4 offense", 4, Side.OFFENSE),
    ("Chivalrous_5K", "+3 defense", 3, Side.DEFENSE),
    ("Valiant_5K", "+4 offense", 4, Side.OFFENSE),
    ("Brave_5K", "+3 offense", 3, Side.OFFENSE),
    ("Courageous_5K", "+4 always", 4, None),
    ("Heroic_5K", "+5 always", 5, None),
    ("Legendary_5K", "+5 always", 5, None),
    ("Mythical_5K", "+5 always", 5, None),
    ("Fabled_5K", "+4 always", 4, None),
    ("Epic_5K", "+5 always", 5, None),
    ("Glorious_5K", "+5 always", 5, None),
    ("Triumphant_5K", "+5 offense", 5, Side.OFFENSE),
]

MILESTONE_5K_BATCH3_POWERS = []

for name, desc, bonus, side in power_specs_batch3:
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
    MILESTONE_5K_BATCH3_POWERS.append(Power)

for power_class in MILESTONE_5K_BATCH3_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
