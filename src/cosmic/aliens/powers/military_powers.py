"""
Military Powers - Aliens with warfare and tactical abilities.
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
class Airborne(AlienPower):
    """
    Airborne - Sky Assault.
    You may attack planets with no defending ships directly.
    """
    name: str = field(default="Airborne", init=False)
    description: str = field(default="Attack empty planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Artillery(AlienPower):
    """
    Artillery - Long Range Fire.
    Add +4 to your total when attacking.
    """
    name: str = field(default="Artillery", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +4 when attacking."""
        if side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Battalion(AlienPower):
    """
    Battalion - Large Force.
    You may commit up to 6 ships instead of 4.
    """
    name: str = field(default="Battalion", init=False)
    description: str = field(default="Commit 6 ships max.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blockade(AlienPower):
    """
    Blockade - Naval Block.
    Opponent cannot retrieve ships from warp this encounter.
    """
    name: str = field(default="Blockade", init=False)
    description: str = field(default="Block warp retrieval.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bunker(AlienPower):
    """
    Bunker - Fortified Position.
    When defending, -5 to opponent's total.
    """
    name: str = field(default="Bunker", init=False)
    description: str = field(default="-5 to attacker's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Commando(AlienPower):
    """
    Commando - Elite Strike.
    When attacking with 1 ship, +10 to total.
    """
    name: str = field(default="Commando", init=False)
    description: str = field(default="+10 with 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Conscript(AlienPower):
    """
    Conscript - Forced Service.
    Allies must join with at least 2 ships.
    """
    name: str = field(default="Conscript", init=False)
    description: str = field(default="Allies commit 2+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Corps(AlienPower):
    """
    Corps - Military Body.
    When you win, retrieve 2 ships from warp.
    """
    name: str = field(default="Corps", init=False)
    description: str = field(default="Retrieve 2 ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Division(AlienPower):
    """
    Division - Split Force.
    Split your ships between two planets when attacking.
    """
    name: str = field(default="Division", init=False)
    description: str = field(default="Attack two planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Draft(AlienPower):
    """
    Draft - Force Recruitment.
    Once per turn, take a ship from any player's warp.
    """
    name: str = field(default="Draft", init=False)
    description: str = field(default="Take ship from any warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flanker(AlienPower):
    """
    Flanker - Side Attack.
    Ignore defensive ally ships in totals.
    """
    name: str = field(default="Flanker", init=False)
    description: str = field(default="Ignore defensive allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Garrison(AlienPower):
    """
    Garrison - Stationed Force.
    Home planets each have +2 defensive bonus.
    """
    name: str = field(default="Garrison", init=False)
    description: str = field(default="+2 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Infantry(AlienPower):
    """
    Infantry - Ground Force.
    Each ship counts as 1.5 (round up).
    """
    name: str = field(default="Infantry", init=False)
    description: str = field(default="Ships count as 1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Marine(AlienPower):
    """
    Marine - Amphibious.
    Win ties when attacking.
    """
    name: str = field(default="Marine", init=False)
    description: str = field(default="Win ties as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Militia(AlienPower):
    """
    Militia - Local Defense.
    When defending, all your colonies send 1 reinforcement.
    """
    name: str = field(default="Militia", init=False)
    description: str = field(default="Colonies reinforce defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ordnance(AlienPower):
    """
    Ordnance - Heavy Weapons.
    When you win by 10+, opponent loses all ships.
    """
    name: str = field(default="Ordnance", init=False)
    description: str = field(default="Big wins destroy all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Outpost(AlienPower):
    """
    Outpost - Forward Base.
    Your foreign colonies can launch attacks.
    """
    name: str = field(default="Outpost", init=False)
    description: str = field(default="Launch from foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Patrol(AlienPower):
    """
    Patrol - Watch Guard.
    See opponent's encounter card before planning.
    """
    name: str = field(default="Patrol", init=False)
    description: str = field(default="See opponent's card early.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Platoon(AlienPower):
    """
    Platoon - Combat Unit.
    Allies on your side get +1 per ship.
    """
    name: str = field(default="Platoon", init=False)
    description: str = field(default="Ally ships +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Recon(AlienPower):
    """
    Recon - Scout Mission.
    Before destiny, look at top 3 cards and choose one.
    """
    name: str = field(default="Recon", init=False)
    description: str = field(default="Choose destiny from top 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Regiment(AlienPower):
    """
    Regiment - Organized Force.
    When you commit 4 ships, +5 to total.
    """
    name: str = field(default="Regiment", init=False)
    description: str = field(default="+5 with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Siege(AlienPower):
    """
    Siege - Extended Attack.
    If attack fails, keep ships for next encounter.
    """
    name: str = field(default="Siege", init=False)
    description: str = field(default="Keep ships after failed attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sniper(AlienPower):
    """
    Sniper - Precision Strike.
    Before reveal, remove 1 opposing ship.
    """
    name: str = field(default="Sniper", init=False)
    description: str = field(default="Remove 1 ship before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Squadron(AlienPower):
    """
    Squadron - Air Unit.
    May attack two planets on same player.
    """
    name: str = field(default="Squadron", init=False)
    description: str = field(default="Attack two planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tank(AlienPower):
    """
    Tank - Armored Unit.
    First 2 ships lost return to colonies instead.
    """
    name: str = field(default="Tank", init=False)
    description: str = field(default="2 ships return on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trench(AlienPower):
    """
    Trench - Defensive Position.
    When defending, win ties.
    """
    name: str = field(default="Trench", init=False)
    description: str = field(default="Win ties as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Airborne())
AlienRegistry.register(Artillery())
AlienRegistry.register(Battalion())
AlienRegistry.register(Blockade())
AlienRegistry.register(Bunker())
AlienRegistry.register(Commando())
AlienRegistry.register(Conscript())
AlienRegistry.register(Corps())
AlienRegistry.register(Division())
AlienRegistry.register(Draft())
AlienRegistry.register(Flanker())
AlienRegistry.register(Garrison())
AlienRegistry.register(Infantry())
AlienRegistry.register(Marine())
AlienRegistry.register(Militia())
AlienRegistry.register(Ordnance())
AlienRegistry.register(Outpost())
AlienRegistry.register(Patrol())
AlienRegistry.register(Platoon())
AlienRegistry.register(Recon())
AlienRegistry.register(Regiment())
AlienRegistry.register(Siege())
AlienRegistry.register(Sniper())
AlienRegistry.register(Squadron())
AlienRegistry.register(Tank())
AlienRegistry.register(Trench())
