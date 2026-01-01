"""
Robot Powers for Cosmic Encounter.

Aliens inspired by robots, machines, and automation themes.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Assembly_Line(AlienPower):
    """Assembly_Line - Power of Production. Gain 1 ship at turn start."""
    name: str = field(default="Assembly_Line", init=False)
    description: str = field(default="Gain 1 ship at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Servitor(AlienPower):
    """Servitor - Power of Service. +1 for each ally ship in encounter."""
    name: str = field(default="Servitor", init=False)
    description: str = field(default="+1 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Automaton(AlienPower):
    """Automaton - Power of Repetition. Use same card twice in a row."""
    name: str = field(default="Automaton", init=False)
    description: str = field(default="Reuse last encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Processor(AlienPower):
    """Processor - Power of Calculation. Look at top 3 deck cards."""
    name: str = field(default="Processor", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drone_Bot(AlienPower):
    """Drone_Bot - Power of Swarm. Ships count as 1.5 each."""
    name: str = field(default="Drone_Bot", init=False)
    description: str = field(default="Ships count as 1.5 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Repair_Bot(AlienPower):
    """Repair_Bot - Power of Repair. Return 1 ship from warp each encounter."""
    name: str = field(default="Repair_Bot", init=False)
    description: str = field(default="Return 1 ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Battle_Bot(AlienPower):
    """Battle_Bot - Power of Combat. +3 in all encounters."""
    name: str = field(default="Battle_Bot", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Stealth_Bot(AlienPower):
    """Stealth_Bot - Power of Invisibility. Opponent reveals card first."""
    name: str = field(default="Stealth_Bot", init=False)
    description: str = field(default="Opponent reveals first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mining_Bot(AlienPower):
    """Mining_Bot - Power of Extraction. Draw 2 cards when winning on offense."""
    name: str = field(default="Mining_Bot", init=False)
    description: str = field(default="Draw 2 cards on offense win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scout_Bot(AlienPower):
    """Scout_Bot - Power of Reconnaissance. See opponent's hand."""
    name: str = field(default="Scout_Bot", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Guard_Bot(AlienPower):
    """Guard_Bot - Power of Protection. +4 on defense."""
    name: str = field(default="Guard_Bot", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Builder_Bot(AlienPower):
    """Builder_Bot - Power of Construction. Place 2 ships when establishing colony."""
    name: str = field(default="Builder_Bot", init=False)
    description: str = field(default="Place 2 ships on new colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Medic_Bot(AlienPower):
    """Medic_Bot - Power of Healing. Allies lose no ships in failed attacks."""
    name: str = field(default="Medic_Bot", init=False)
    description: str = field(default="Protect ally ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cargo_Bot(AlienPower):
    """Cargo_Bot - Power of Transport. May commit up to 6 ships."""
    name: str = field(default="Cargo_Bot", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mega_Bot(AlienPower):
    """Mega_Bot - Power of Size. Ships count as 2 each."""
    name: str = field(default="Mega_Bot", init=False)
    description: str = field(default="Ships count as 2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all robot powers
AlienRegistry.register(Assembly_Line())
AlienRegistry.register(Servitor())
AlienRegistry.register(Automaton())
AlienRegistry.register(Processor())
AlienRegistry.register(Drone_Bot())
AlienRegistry.register(Repair_Bot())
AlienRegistry.register(Battle_Bot())
AlienRegistry.register(Stealth_Bot())
AlienRegistry.register(Mining_Bot())
AlienRegistry.register(Scout_Bot())
AlienRegistry.register(Guard_Bot())
AlienRegistry.register(Builder_Bot())
AlienRegistry.register(Medic_Bot())
AlienRegistry.register(Cargo_Bot())
AlienRegistry.register(Mega_Bot())
