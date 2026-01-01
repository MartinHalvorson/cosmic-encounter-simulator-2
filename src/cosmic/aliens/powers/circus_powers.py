"""
Circus Powers for Cosmic Encounter.

Aliens inspired by circus performers and acts.
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
class Ringmaster(AlienPower):
    """Ringmaster - Power of Control. +2 per ally in encounter."""
    name: str = field(default="Ringmaster", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trapeze(AlienPower):
    """Trapeze - Power of Flying. Ships return home, not warp."""
    name: str = field(default="Trapeze", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Clown_Alt(AlienPower):
    """Clown_Alt - Power of Laughter. Opponent discards 1 card."""
    name: str = field(default="Clown_Alt", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lion_Tamer(AlienPower):
    """Lion_Tamer - Power of Bravery. +4 on offense."""
    name: str = field(default="Lion_Tamer", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Strongman(AlienPower):
    """Strongman - Power of Strength. Ships count as 2 each."""
    name: str = field(default="Strongman", init=False)
    description: str = field(default="Ships count as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Contortionist(AlienPower):
    """Contortionist - Power of Flexibility. May change card after reveal."""
    name: str = field(default="Contortionist", init=False)
    description: str = field(default="Change card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fire_Breather(AlienPower):
    """Fire_Breather - Power of Flame. +3 always."""
    name: str = field(default="Fire_Breather", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Sword_Swallower(AlienPower):
    """Sword_Swallower - Power of Daring. +5 but lose 1 ship after."""
    name: str = field(default="Sword_Swallower", init=False)
    description: str = field(default="+5, lose 1 ship after.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Knife_Thrower(AlienPower):
    """Knife_Thrower - Power of Precision. Win ties automatically."""
    name: str = field(default="Knife_Thrower", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magician_Alt(AlienPower):
    """Magician_Alt - Power of Tricks. See opponent's card before choosing."""
    name: str = field(default="Magician_Alt", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tightrope(AlienPower):
    """Tightrope - Power of Balance. +2 on defense."""
    name: str = field(default="Tightrope", init=False)
    description: str = field(default="+2 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Cannon_Ball(AlienPower):
    """Cannon_Ball - Power of Launch. +4 on first encounter."""
    name: str = field(default="Cannon_Ball", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 4
        return total


@dataclass
class Elephant_Act(AlienPower):
    """Elephant_Act - Power of Memory. Draw 1 card when winning."""
    name: str = field(default="Elephant_Act", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Unicycle(AlienPower):
    """Unicycle - Power of Solo. +3 when attacking alone."""
    name: str = field(default="Unicycle", init=False)
    description: str = field(default="+3 without allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Big_Top(AlienPower):
    """Big_Top - Power of Spectacle. All allies get +1."""
    name: str = field(default="Big_Top", init=False)
    description: str = field(default="Allies get +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all circus powers
AlienRegistry.register(Ringmaster())
AlienRegistry.register(Trapeze())
AlienRegistry.register(Clown_Alt())
AlienRegistry.register(Lion_Tamer())
AlienRegistry.register(Strongman())
AlienRegistry.register(Contortionist())
AlienRegistry.register(Fire_Breather())
AlienRegistry.register(Sword_Swallower())
AlienRegistry.register(Knife_Thrower())
AlienRegistry.register(Magician_Alt())
AlienRegistry.register(Tightrope())
AlienRegistry.register(Cannon_Ball())
AlienRegistry.register(Elephant_Act())
AlienRegistry.register(Unicycle())
AlienRegistry.register(Big_Top())
