"""
Profession Powers for Cosmic Encounter.

Aliens inspired by various professions and jobs.
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
class Doctor_Profession(AlienPower):
    """Doctor_Profession - Power of Healing."""
    name: str = field(default="Doctor_Profession", init=False)
    description: str = field(default="Retrieve 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


@dataclass
class Lawyer_Profession(AlienPower):
    """Lawyer_Profession - Power of Argument."""
    name: str = field(default="Lawyer_Profession", init=False)
    description: str = field(default="+3 in negotiations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Teacher_Profession(AlienPower):
    """Teacher_Profession - Power of Knowledge."""
    name: str = field(default="Teacher_Profession", init=False)
    description: str = field(default="Draw 2 cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Engineer_Profession(AlienPower):
    """Engineer_Profession - Power of Building."""
    name: str = field(default="Engineer_Profession", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Pilot_Profession(AlienPower):
    """Pilot_Profession - Power of Flight."""
    name: str = field(default="Pilot_Profession", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chef_Profession(AlienPower):
    """Chef_Profession - Power of Creation."""
    name: str = field(default="Chef_Profession", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Artist_Profession(AlienPower):
    """Artist_Profession - Power of Creativity."""
    name: str = field(default="Artist_Profession", init=False)
    description: str = field(default="Change card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scientist_Profession(AlienPower):
    """Scientist_Profession - Power of Discovery."""
    name: str = field(default="Scientist_Profession", init=False)
    description: str = field(default="Draw extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Soldier_Profession(AlienPower):
    """Soldier_Profession - Power of Combat."""
    name: str = field(default="Soldier_Profession", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Farmer_Profession(AlienPower):
    """Farmer_Profession - Power of Growth."""
    name: str = field(default="Farmer_Profession", init=False)
    description: str = field(default="Gain ship each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


@dataclass
class Banker_Profession(AlienPower):
    """Banker_Profession - Power of Wealth."""
    name: str = field(default="Banker_Profession", init=False)
    description: str = field(default="+1 per card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Detective_Profession(AlienPower):
    """Detective_Profession - Power of Investigation."""
    name: str = field(default="Detective_Profession", init=False)
    description: str = field(default="See opponent hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Athlete_Profession(AlienPower):
    """Athlete_Profession - Power of Fitness."""
    name: str = field(default="Athlete_Profession", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Firefighter_Profession(AlienPower):
    """Firefighter_Profession - Power of Rescue."""
    name: str = field(default="Firefighter_Profession", init=False)
    description: str = field(default="Save ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(min(2, player.ships_in_warp))


# Register all aliens
for alien_class in [
    Doctor_Profession, Lawyer_Profession, Teacher_Profession, Engineer_Profession,
    Pilot_Profession, Chef_Profession, Artist_Profession, Scientist_Profession,
    Soldier_Profession, Farmer_Profession, Banker_Profession, Detective_Profession,
    Athlete_Profession, Firefighter_Profession,
]:
    AlienRegistry.register(alien_class())
