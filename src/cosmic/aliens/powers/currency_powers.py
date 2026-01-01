"""
Currency and Money themed alien powers for Cosmic Encounter.
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
class Dollar(AlienPower):
    """Dollar - Power of Commerce."""
    name: str = field(default="Dollar", init=False)
    description: str = field(default="Draw 1 card when you establish a colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Euro(AlienPower):
    """Euro - Power of Unity."""
    name: str = field(default="Euro", init=False)
    description: str = field(default="+1 for each ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Yen(AlienPower):
    """Yen - Power of Precision."""
    name: str = field(default="Yen", init=False)
    description: str = field(default="Know exact card value opponent plays.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pound(AlienPower):
    """Pound - Power of Weight."""
    name: str = field(default="Pound", init=False)
    description: str = field(default="+2 when you have more ships than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bitcoin(AlienPower):
    """Bitcoin - Power of Volatility."""
    name: str = field(default="Bitcoin", init=False)
    description: str = field(default="Random +/- 5 to your total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Gold(AlienPower):
    """Gold - Power of Value."""
    name: str = field(default="Gold", init=False)
    description: str = field(default="+3 when playing attack 20+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Silver(AlienPower):
    """Silver - Power of Second Place."""
    name: str = field(default="Silver", init=False)
    description: str = field(default="+2 when losing by 5 or less.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Coin(AlienPower):
    """Coin - Power of Chance."""
    name: str = field(default="Coin", init=False)
    description: str = field(default="Flip: heads +4, tails -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Banker(AlienPower):
    """Banker - Power of Interest."""
    name: str = field(default="Banker", init=False)
    description: str = field(default="Gain 1 card at the start of each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Treasure(AlienPower):
    """Treasure - Power of Riches."""
    name: str = field(default="Treasure", init=False)
    description: str = field(default="Draw 2 cards when winning as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Vault_Currency(AlienPower):
    """Vault - Power of Security."""
    name: str = field(default="Vault_Currency", init=False)
    description: str = field(default="Cards cannot be stolen from your hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wallet(AlienPower):
    """Wallet - Power of Storage."""
    name: str = field(default="Wallet", init=False)
    description: str = field(default="Hand limit increased to 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Dollar())
AlienRegistry.register(Euro())
AlienRegistry.register(Yen())
AlienRegistry.register(Pound())
AlienRegistry.register(Bitcoin())
AlienRegistry.register(Gold())
AlienRegistry.register(Silver())
AlienRegistry.register(Coin())
AlienRegistry.register(Banker())
AlienRegistry.register(Treasure())
AlienRegistry.register(Vault_Currency())
AlienRegistry.register(Wallet())
