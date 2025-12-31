"""
Dominion Powers - Aliens focused on control and territory.

These powers emphasize controlling planets, ships, and game flow.
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
class Admiral(AlienPower):
    """
    Admiral - Fleet Commander.
    Your ships count as 1.5 each (rounded down) in encounters.
    """
    name: str = field(default="Admiral", init=False)
    description: str = field(default="Ships count as 1.5 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        """Ships count as 1.5 each."""
        return int(count * 1.5)


@dataclass
class Baron(AlienPower):
    """
    Baron - Noble Ruler.
    When defending your home system, add +3 to your total.
    """
    name: str = field(default="Baron", init=False)
    description: str = field(default="Add +3 when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +3 when defending at home."""
        if side == Side.DEFENSE and game.defense == player:
            if game.defense_planet and game.defense_planet.owner == player:
                return total + 3
        return total


@dataclass
class Captain(AlienPower):
    """
    Captain - Ship Master.
    You may commit 5 ships instead of 4 to encounters.
    """
    name: str = field(default="Captain", init=False)
    description: str = field(default="Commit up to 5 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Despot(AlienPower):
    """
    Despot - Tyrant.
    When you win, opponent loses an additional ship to the warp.
    """
    name: str = field(default="Despot", init=False)
    description: str = field(default="Opponent loses extra ship on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Autocrat(AlienPower):
    """
    Autocrat - Supreme Ruler.
    Once per encounter, you may cancel an alliance invitation.
    """
    name: str = field(default="Autocrat", init=False)
    description: str = field(default="Cancel one alliance invitation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Governor(AlienPower):
    """
    Governor - Colony Manager.
    You start with 6 ships per home planet instead of 4.
    """
    name: str = field(default="Governor", init=False)
    description: str = field(default="Start with 6 ships per planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_game_start(self, game: "Game", player: "Player") -> None:
        """Add extra starting ships."""
        for planet in player.home_planets:
            planet.add_ships(player.name, 2)


@dataclass
class Herald(AlienPower):
    """
    Herald - Announcer.
    When you draw a destiny card, reveal it and then draw another.
    """
    name: str = field(default="Herald", init=False)
    description: str = field(default="Draw two destiny cards, choose one.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Imperator(AlienPower):
    """
    Imperator - Supreme Commander.
    Once per turn, you may force a player to ally with you.
    """
    name: str = field(default="Imperator", init=False)
    description: str = field(default="Force one player to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Monarch(AlienPower):
    """
    Monarch - Royal Ruler.
    You win ties (instead of defense winning ties).
    """
    name: str = field(default="Monarch", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lord(AlienPower):
    """
    Lord - Feudal Master.
    When you establish a colony, draw 1 card.
    """
    name: str = field(default="Lord", init=False)
    description: str = field(default="Draw card when colonizing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Marshal(AlienPower):
    """
    Marshal - Military Commander.
    Your attack cards get +2 value.
    """
    name: str = field(default="Marshal", init=False)
    description: str = field(default="Attack cards +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +2 to attack cards."""
        return total + 2


@dataclass
class Overseer(AlienPower):
    """
    Overseer - Supreme Master.
    When defending, you may look at attacker's hand.
    """
    name: str = field(default="Overseer", init=False)
    description: str = field(default="See attacker's hand when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Potentate(AlienPower):
    """
    Potentate - Powerful Ruler.
    Once per encounter, you may nullify one alien power use.
    """
    name: str = field(default="Potentate", init=False)
    description: str = field(default="Nullify one power use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Prince(AlienPower):
    """
    Prince - Royal Heir.
    When you lose ships to the warp, keep one.
    """
    name: str = field(default="Prince", init=False)
    description: str = field(default="Keep one ship when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Queen(AlienPower):
    """
    Queen - Royal Matriarch.
    Your negotiate cards are worth +3 in deals.
    """
    name: str = field(default="Queen", init=False)
    description: str = field(default="Better negotiate outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Regent(AlienPower):
    """
    Regent - Acting Ruler.
    When offense, your allies commit ships before defense invites.
    """
    name: str = field(default="Regent", init=False)
    description: str = field(default="Allies commit first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sovereign(AlienPower):
    """
    Sovereign - Absolute Ruler.
    You may have 6 foreign colonies to win (but need 5 still).
    """
    name: str = field(default="Sovereign", init=False)
    description: str = field(default="Extra colony flexibility.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sultan(AlienPower):
    """
    Sultan - Eastern Ruler.
    When you win, you may exchange one card with opponent.
    """
    name: str = field(default="Sultan", init=False)
    description: str = field(default="Exchange card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tsar(AlienPower):
    """
    Tsar - Imperial Ruler.
    Once per turn, you may retrieve 2 ships from the warp.
    """
    name: str = field(default="Tsar", init=False)
    description: str = field(default="Retrieve 2 ships per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Viceroy(AlienPower):
    """
    Viceroy - Deputy Ruler.
    When you are not a main player, add +1 to either side.
    """
    name: str = field(default="Viceroy", init=False)
    description: str = field(default="Add +1 when not main player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warden(AlienPower):
    """
    Warden - Keeper.
    Ships you send to warp return after 2 encounters.
    """
    name: str = field(default="Warden", init=False)
    description: str = field(default="Ships return from warp faster.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Admiral())
AlienRegistry.register(Baron())
AlienRegistry.register(Captain())
AlienRegistry.register(Despot())
AlienRegistry.register(Autocrat())
AlienRegistry.register(Governor())
AlienRegistry.register(Herald())
AlienRegistry.register(Imperator())
AlienRegistry.register(Monarch())
AlienRegistry.register(Lord())
AlienRegistry.register(Marshal())
AlienRegistry.register(Overseer())
AlienRegistry.register(Potentate())
AlienRegistry.register(Prince())
AlienRegistry.register(Queen())
AlienRegistry.register(Regent())
AlienRegistry.register(Sovereign())
AlienRegistry.register(Sultan())
AlienRegistry.register(Tsar())
AlienRegistry.register(Viceroy())
AlienRegistry.register(Warden())
