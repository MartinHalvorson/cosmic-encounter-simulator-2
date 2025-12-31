"""
Energy Powers - Aliens with energy manipulation abilities.
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
class Absorber(AlienPower):
    """
    Absorber - Energy Drain.
    Steal +2 from opponent's total.
    """
    name: str = field(default="Absorber", init=False)
    description: str = field(default="Steal +2 from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Amplify(AlienPower):
    """
    Amplify - Power Amplifier.
    Double your card value.
    """
    name: str = field(default="Amplify", init=False)
    description: str = field(default="Double card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Battery(AlienPower):
    """
    Battery - Stored Power.
    Store +1 per turn, release when needed.
    """
    name: str = field(default="Battery", init=False)
    description: str = field(default="Store power bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bolt(AlienPower):
    """
    Bolt - Energy Bolt.
    +5 when attacking.
    """
    name: str = field(default="Bolt", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when attacking."""
        if side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Capacitor(AlienPower):
    """
    Capacitor - Energy Storage.
    Once per game, double your total.
    """
    name: str = field(default="Capacitor", init=False)
    description: str = field(default="Double total once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Charger(AlienPower):
    """
    Charger - Energy Charge.
    +2 per ally ship.
    """
    name: str = field(default="Charger", init=False)
    description: str = field(default="+2 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Conductor_Alt(AlienPower):
    """
    Conductor_Alt - Energy Flow.
    Transfer power between ships.
    """
    name: str = field(default="Conductor_Alt", init=False)
    description: str = field(default="Transfer power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Core(AlienPower):
    """
    Core - Power Core.
    +4 to all totals.
    """
    name: str = field(default="Core", init=False)
    description: str = field(default="+4 to all totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 to total."""
        return total + 4


@dataclass
class Discharge(AlienPower):
    """
    Discharge - Power Release.
    Send opponent ships to warp.
    """
    name: str = field(default="Discharge", init=False)
    description: str = field(default="Send ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dynamo(AlienPower):
    """
    Dynamo - Power Generator.
    Draw extra card per encounter.
    """
    name: str = field(default="Dynamo", init=False)
    description: str = field(default="Draw extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fission(AlienPower):
    """
    Fission - Split Power.
    Split ships between two encounters.
    """
    name: str = field(default="Fission", init=False)
    description: str = field(default="Split encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fusion(AlienPower):
    """
    Fusion - Combine Power.
    Combine ally totals.
    """
    name: str = field(default="Fusion", init=False)
    description: str = field(default="Combine ally power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Overload(AlienPower):
    """
    Overload - Power Surge.
    Risk all for massive bonus.
    """
    name: str = field(default="Overload", init=False)
    description: str = field(default="All or nothing bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Plasma(AlienPower):
    """
    Plasma - Hot Energy.
    Destroy opponent ships on win.
    """
    name: str = field(default="Plasma", init=False)
    description: str = field(default="Destroy ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Pulse(AlienPower):
    """
    Pulse - Energy Wave.
    Remove ally ships from both sides.
    """
    name: str = field(default="Pulse", init=False)
    description: str = field(default="Remove all allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Reactor(AlienPower):
    """
    Reactor - Power Plant.
    Generate +1 per home colony.
    """
    name: str = field(default="Reactor", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Resonator(AlienPower):
    """
    Resonator - Energy Echo.
    Copy opponent's card value.
    """
    name: str = field(default="Resonator", init=False)
    description: str = field(default="Copy opponent card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shock(AlienPower):
    """
    Shock - Electric Shock.
    Stun opponent for 1 turn.
    """
    name: str = field(default="Shock", init=False)
    description: str = field(default="Stun opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Absorber())
AlienRegistry.register(Amplify())
AlienRegistry.register(Battery())
AlienRegistry.register(Bolt())
AlienRegistry.register(Capacitor())
AlienRegistry.register(Charger())
AlienRegistry.register(Conductor_Alt())
AlienRegistry.register(Core())
AlienRegistry.register(Discharge())
AlienRegistry.register(Dynamo())
AlienRegistry.register(Fission())
AlienRegistry.register(Fusion())
AlienRegistry.register(Overload())
AlienRegistry.register(Plasma())
AlienRegistry.register(Pulse())
AlienRegistry.register(Reactor())
AlienRegistry.register(Resonator())
AlienRegistry.register(Shock())
