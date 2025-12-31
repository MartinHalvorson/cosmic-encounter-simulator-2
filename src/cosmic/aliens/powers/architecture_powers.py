"""
Architecture Powers for Cosmic Encounter.

Aliens inspired by architectural concepts and building structures.
"""

from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Architect_Power(AlienPower):
    """
    Architect - Power to Design.
    Before each encounter, you may rearrange up to 3 ships among your colonies.
    """
    name: str = "Architect_Power"
    timing: PowerTiming = PowerTiming.START_TURN
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Builder(AlienPower):
    """
    Builder - Power to Construct.
    When you establish a new colony, draw 2 cards.
    """
    name: str = "Builder"
    timing: PowerTiming = PowerTiming.WIN_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Demolisher(AlienPower):
    """
    Demolisher - Power to Destroy.
    When you win as offense, remove 1 additional ship from the planet.
    """
    name: str = "Demolisher"
    timing: PowerTiming = PowerTiming.WIN_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Foundation(AlienPower):
    """
    Foundation - Power of Stability.
    Your home colonies cannot have fewer than 2 ships removed at once.
    """
    name: str = "Foundation"
    timing: PowerTiming = PowerTiming.SHIPS_TO_WARP
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Skyscraper(AlienPower):
    """
    Skyscraper - Power to Rise.
    Add +1 for each colony you have (max +5).
    """
    name: str = "Skyscraper"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +1 per colony."""
        if not player.power_active:
            return base_total
        colonies = player.count_foreign_colonies(game.planets)
        home_colonies = sum(1 for p in game.planets if p.owner == player and p.has_colony(player.name))
        total_colonies = colonies + home_colonies
        return base_total + min(5, total_colonies)


@dataclass
class Pillar(AlienPower):
    """
    Pillar - Power to Support.
    Allied ships count double toward your side's total.
    """
    name: str = "Pillar"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Bridge(AlienPower):
    """
    Bridge - Power to Connect.
    You may invite one additional ally beyond the normal limit.
    """
    name: str = "Bridge"
    timing: PowerTiming = PowerTiming.ALLIANCE
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Tower(AlienPower):
    """
    Tower - Power of Defense.
    Add +4 when defending your home planets.
    """
    name: str = "Tower"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +4 defending home."""
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE and game.defense_planet:
            if game.defense_planet.owner == player:
                return base_total + 4
        return base_total


@dataclass
class Vault(AlienPower):
    """
    Vault - Power to Secure.
    Cards cannot be taken from your hand by other powers.
    """
    name: str = "Vault"
    timing: PowerTiming = PowerTiming.CONSTANT
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Dome(AlienPower):
    """
    Dome - Power to Cover.
    Your allies are protected from losing ships when you win.
    """
    name: str = "Dome"
    timing: PowerTiming = PowerTiming.WIN_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Fortress(AlienPower):
    """
    Fortress - Power to Fortify.
    You may commit up to 6 ships when defending (instead of 4).
    """
    name: str = "Fortress"
    timing: PowerTiming = PowerTiming.LAUNCH
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Monument(AlienPower):
    """
    Monument - Power to Commemorate.
    Gain 1 token each time you win an encounter. Each token is worth +1.
    """
    name: str = "Monument"
    timing: PowerTiming = PowerTiming.WIN_ENCOUNTER
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Rampart(AlienPower):
    """
    Rampart - Power to Wall.
    Opponents need 4 additional ships to successfully invade your home planets.
    """
    name: str = "Rampart"
    timing: PowerTiming = PowerTiming.REVEAL
    power_type: PowerType = PowerType.MANDATORY


@dataclass
class Spire(AlienPower):
    """
    Spire - Power to Reach.
    You may attack any planet in the game, ignoring destiny.
    """
    name: str = "Spire"
    timing: PowerTiming = PowerTiming.DESTINY
    power_type: PowerType = PowerType.OPTIONAL


@dataclass
class Ruins(AlienPower):
    """
    Ruins - Power of the Past.
    When you lose a colony, you may immediately attack it again.
    """
    name: str = "Ruins"
    timing: PowerTiming = PowerTiming.LOSE_ENCOUNTER
    power_type: PowerType = PowerType.OPTIONAL


# Register all architecture powers
def register_architecture_powers():
    from ..registry import AlienRegistry

    powers = [
        Architect_Power(),
        Builder(),
        Demolisher(),
        Foundation(),
        Skyscraper(),
        Pillar(),
        Bridge(),
        Tower(),
        Vault(),
        Dome(),
        Fortress(),
        Monument(),
        Rampart(),
        Spire(),
        Ruins(),
    ]

    for power in powers:
        AlienRegistry.register(power)


# Auto-register on import
register_architecture_powers()
