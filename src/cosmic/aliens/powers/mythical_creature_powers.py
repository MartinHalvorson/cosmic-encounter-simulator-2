"""
Mythical Creature Powers for Cosmic Encounter.

Aliens inspired by mythical creatures and beings.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Unicorn_Myth(AlienPower):
    """Unicorn_Myth - Power of Purity."""
    name: str = field(default="Unicorn_Myth", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Griffin_Myth(AlienPower):
    """Griffin_Myth - Power of Guardian."""
    name: str = field(default="Griffin_Myth", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Manticore(AlienPower):
    """Manticore - Power of Terror."""
    name: str = field(default="Manticore", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Pegasus_Myth(AlienPower):
    """Pegasus_Myth - Power of Flight."""
    name: str = field(default="Pegasus_Myth", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Basilisk_Myth(AlienPower):
    """Basilisk_Myth - Power of Gaze."""
    name: str = field(default="Basilisk_Myth", init=False)
    description: str = field(default="Petrify opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Chimera_Myth(AlienPower):
    """Chimera_Myth - Power of Hybrid."""
    name: str = field(default="Chimera_Myth", init=False)
    description: str = field(default="Random +3 to +6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(3, 6)
        return base_total


@dataclass
class Hydra_Myth(AlienPower):
    """Hydra_Myth - Power of Regeneration."""
    name: str = field(default="Hydra_Myth", init=False)
    description: str = field(default="Retrieve all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(player.ships_in_warp)


@dataclass
class Cerberus_Myth(AlienPower):
    """Cerberus_Myth - Power of Guarding."""
    name: str = field(default="Cerberus_Myth", init=False)
    description: str = field(default="+6 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 6
        return base_total


@dataclass
class Centaur_Myth(AlienPower):
    """Centaur_Myth - Power of Wisdom."""
    name: str = field(default="Centaur_Myth", init=False)
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
class Minotaur_Myth(AlienPower):
    """Minotaur_Myth - Power of Maze."""
    name: str = field(default="Minotaur_Myth", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Siren_Myth(AlienPower):
    """Siren_Myth - Power of Song."""
    name: str = field(default="Siren_Myth", init=False)
    description: str = field(default="Lure opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kitsune(AlienPower):
    """Kitsune - Power of Fox."""
    name: str = field(default="Kitsune", init=False)
    description: str = field(default="Trick opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
for alien_class in [
    Unicorn_Myth, Griffin_Myth, Manticore, Pegasus_Myth, Basilisk_Myth,
    Chimera_Myth, Hydra_Myth, Cerberus_Myth, Centaur_Myth, Minotaur_Myth,
    Siren_Myth, Kitsune,
]:
    AlienRegistry.register(alien_class())
