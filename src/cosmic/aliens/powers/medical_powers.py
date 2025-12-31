"""
Medical Powers for Cosmic Encounter.

Aliens inspired by medical and healthcare concepts.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Surgeon(AlienPower):
    """
    Surgeon - Power to Operate.
    You may remove cards from opponent's hand before the encounter.
    """
    name: str = "Surgeon"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Healer_Power(AlienPower):
    """
    Healer - Power to Mend.
    At the end of each encounter, retrieve 1 ship from the warp.
    """
    name: str = "Healer_Power"
    timing: PowerTiming = PowerTiming.RESOLUTION
    power_type: PowerType = PowerType.MANDATORY

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        """Retrieve 1 ship from warp."""
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)
            player.return_ships_to_colonies(1, player.home_planets)


@dataclass
class Nurse(AlienPower):
    """
    Nurse - Power to Care.
    Allies who join your side retrieve 1 ship from the warp.
    """
    name: str = "Nurse"
    timing: PowerTiming = PowerTiming.ALLIANCE
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Paramedic(AlienPower):
    """
    Paramedic - Power of Emergency.
    Ships that would go to the warp are instead returned to colonies.
    """
    name: str = "Paramedic"
    timing: PowerTiming = PowerTiming.SHIPS_TO_WARP
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Pharmacist(AlienPower):
    """
    Pharmacist - Power to Prescribe.
    Once per encounter, you may give a card from your hand to any player.
    """
    name: str = "Pharmacist"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Psychiatrist(AlienPower):
    """
    Psychiatrist - Power of Mind.
    You may force opponent to play a specific card type.
    """
    name: str = "Psychiatrist"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Anesthesiologist(AlienPower):
    """
    Anesthesiologist - Power to Numb.
    Opponent's power is temporarily disabled during encounters with you.
    """
    name: str = "Anesthesiologist"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Pathologist(AlienPower):
    """
    Pathologist - Power to Analyze.
    Before the encounter, see the top 3 cards of the cosmic deck.
    """
    name: str = "Pathologist"
    timing: PowerTiming = PowerTiming.START_TURN
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Therapist(AlienPower):
    """
    Therapist - Power to Counsel.
    After a failed deal, you may propose a new deal.
    """
    name: str = "Therapist"
    timing: PowerTiming = PowerTiming.RESOLUTION
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Radiologist(AlienPower):
    """
    Radiologist - Power to See Through.
    You may see opponent's selected card before playing yours.
    """
    name: str = "Radiologist"
    timing: PowerTiming = PowerTiming.PLANNING
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Dentist(AlienPower):
    """
    Dentist - Power to Extract.
    When you win, remove 1 additional card from opponent's hand.
    """
    name: str = "Dentist"
    timing: PowerTiming = PowerTiming.WIN_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Veterinarian(AlienPower):
    """
    Veterinarian - Power of Creatures.
    Your ships from warp return to any colony, not just home.
    """
    name: str = "Veterinarian"
    timing: PowerTiming = PowerTiming.REGROUP
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Immunologist(AlienPower):
    """
    Immunologist - Power of Defense.
    The first time each encounter you would lose ships, lose 1 fewer.
    """
    name: str = "Immunologist"
    timing: PowerTiming = PowerTiming.SHIPS_TO_WARP
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Oncologist(AlienPower):
    """
    Oncologist - Power to Remove.
    Target one opponent's power; it is disabled for this encounter.
    """
    name: str = "Oncologist"
    timing: PowerTiming = PowerTiming.START_TURN
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Geneticist_Power(AlienPower):
    """
    Geneticist - Power to Modify.
    Once per game, swap your alien power with an opponent's.
    """
    name: str = "Geneticist_Power"
    timing: PowerTiming = PowerTiming.START_TURN
    power_type: PowerType = PowerType.OPTIONAL


# Register all medical powers
def register_medical_powers():
    from ..registry import AlienRegistry

    powers = [
        Surgeon(),
        Healer_Power(),
        Nurse(),
        Paramedic(),
        Pharmacist(),
        Psychiatrist(),
        Anesthesiologist(),
        Pathologist(),
        Therapist(),
        Radiologist(),
        Dentist(),
        Veterinarian(),
        Immunologist(),
        Oncologist(),
        Geneticist_Power(),
    ]

    for power in powers:
        AlienRegistry.register(power)


# Auto-register on import
register_medical_powers()
