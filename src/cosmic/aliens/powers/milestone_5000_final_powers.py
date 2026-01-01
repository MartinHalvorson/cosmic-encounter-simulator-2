"""
Milestone 5000 Final Powers - Final push to 5000 aliens.
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

# Generate powers programmatically
power_specs = [
    ("Alpha_5K", "+3 always", 3, None),
    ("Beta_5K", "+3 always", 3, None),
    ("Gamma_5K", "+4 always", 4, None),
    ("Delta_5K", "+4 always", 4, None),
    ("Epsilon_5K", "+3 offense", 3, Side.OFFENSE),
    ("Zeta_5K", "+3 offense", 3, Side.OFFENSE),
    ("Eta_5K", "+4 offense", 4, Side.OFFENSE),
    ("Theta_5K", "+4 offense", 4, Side.OFFENSE),
    ("Iota_5K", "+3 defense", 3, Side.DEFENSE),
    ("Kappa_5K", "+3 defense", 3, Side.DEFENSE),
    ("Lambda_5K", "+4 defense", 4, Side.DEFENSE),
    ("Mu_5K", "+4 defense", 4, Side.DEFENSE),
    ("Nu_5K", "+5 always", 5, None),
    ("Xi_5K", "+5 always", 5, None),
    ("Omicron_5K", "+3 always", 3, None),
    ("Pi_5K", "+3 always", 3, None),
    ("Rho_5K", "+4 always", 4, None),
    ("Sigma_5K", "+4 always", 4, None),
    ("Tau_5K", "+5 offense", 5, Side.OFFENSE),
    ("Upsilon_5K", "+5 offense", 5, Side.OFFENSE),
    ("Phi_5K", "+5 defense", 5, Side.DEFENSE),
    ("Chi_5K", "+5 defense", 5, Side.DEFENSE),
    ("Psi_5K", "+4 always", 4, None),
    ("Omega_5K", "+5 always", 5, None),
    ("Premier_5K", "+4 always", 4, None),
    ("Elite_5K", "+5 always", 5, None),
    ("Supreme_5K", "+5 always", 5, None),
    ("Ultimate_5K", "+6 always", 6, None),
    ("Apex_5K", "+5 always", 5, None),
    ("Peak_5K", "+4 always", 4, None),
]

MILESTONE_5000_FINAL_POWERS = []

for name, desc, bonus, side in power_specs:
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
    MILESTONE_5000_FINAL_POWERS.append(Power)

for power_class in MILESTONE_5000_FINAL_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
