"""
Office and Workplace-themed alien powers.
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
class Boss_Office(AlienPower):
    """Boss - Power of Authority. +3 when you have most ships in encounter."""
    name: str = field(default="Boss_Office", init=False)
    description: str = field(default="+3 when you have most ships in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Secretary_Office(AlienPower):
    """Secretary - Power of Organization. Draw 2 cards, discard 1."""
    name: str = field(default="Secretary_Office", init=False)
    description: str = field(default="At turn start, draw 2 cards, discard 1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class CEO_Office(AlienPower):
    """CEO - Power of Leadership. +2 for each player on your side."""
    name: str = field(default="CEO_Office", init=False)
    description: str = field(default="+2 for each player on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Manager_Office(AlienPower):
    """Manager - Power of Delegation. Allies must commit max ships."""
    name: str = field(default="Manager_Office", init=False)
    description: str = field(default="Allies on your side must commit 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Intern_Office(AlienPower):
    """Intern - Power of Learning. +1 per encounter you've had this game."""
    name: str = field(default="Intern_Office", init=False)
    description: str = field(default="+1 per encounter you've had (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class HR_Office(AlienPower):
    """HR - Power of Relations. +2 when both sides have allies."""
    name: str = field(default="HR_Office", init=False)
    description: str = field(default="+2 when both sides have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Accountant_Office(AlienPower):
    """Accountant - Power of Numbers. +1 per card in hand."""
    name: str = field(default="Accountant_Office", init=False)
    description: str = field(default="+1 per card in your hand (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class IT_Office(AlienPower):
    """IT - Power of Tech. May look at top 3 cards of deck."""
    name: str = field(default="IT_Office", init=False)
    description: str = field(default="May look at top 3 cards of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Janitor_Office(AlienPower):
    """Janitor - Power of Cleanup. Return 1 ship from warp at encounter start."""
    name: str = field(default="Janitor_Office", init=False)
    description: str = field(default="Return 1 ship from warp at encounter start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Security_Office(AlienPower):
    """Security - Power of Protection. +4 when defending home planet."""
    name: str = field(default="Security_Office", init=False)
    description: str = field(default="+4 when defending a home planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Receptionist_Office(AlienPower):
    """Receptionist - Power of Welcome. Draw 1 card when ally joins your side."""
    name: str = field(default="Receptionist_Office", init=False)
    description: str = field(default="Draw 1 card when an ally joins your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Executive_Office(AlienPower):
    """Executive - Power of Decision. May veto one ally's joining."""
    name: str = field(default="Executive_Office", init=False)
    description: str = field(default="May veto one player's alliance offer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all office powers
AlienRegistry.register(Boss_Office())
AlienRegistry.register(Secretary_Office())
AlienRegistry.register(CEO_Office())
AlienRegistry.register(Manager_Office())
AlienRegistry.register(Intern_Office())
AlienRegistry.register(HR_Office())
AlienRegistry.register(Accountant_Office())
AlienRegistry.register(IT_Office())
AlienRegistry.register(Janitor_Office())
AlienRegistry.register(Security_Office())
AlienRegistry.register(Receptionist_Office())
AlienRegistry.register(Executive_Office())
