"""
Movie genre themed alien powers for Cosmic Encounter.
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
class ActionMovie(AlienPower):
    """ActionMovie - Power of Explosions. Non-stop thrills."""
    name: str = field(default="Action_Movie", init=False)
    description: str = field(default="+4 as offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Comedy(AlienPower):
    """Comedy - Power of Laughter. Find the humor."""
    name: str = field(default="Comedy", init=False)
    description: str = field(default="Random +1-5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 5)
        return base_total


@dataclass
class Drama(AlienPower):
    """Drama - Power of Emotion. Deep storytelling."""
    name: str = field(default="Drama", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class SciFi(AlienPower):
    """SciFi - Power of the Future. Technological wonder."""
    name: str = field(default="SciFi_Genre", init=False)
    description: str = field(default="+2 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + (ships * 2)


@dataclass
class Horror_Genre(AlienPower):
    """Horror_Genre - Power of Fear. Terrify your opponents."""
    name: str = field(default="Horror_Genre", init=False)
    description: str = field(default="+4 as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Romance(AlienPower):
    """Romance - Power of Love. Heartfelt connections."""
    name: str = field(default="Romance", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            # Count allied ships in encounter
            if side == Side.OFFENSE:
                allies = sum(1 for p in game.offense_ships if p != player.name and game.offense_ships.get(p, 0) > 0)
            else:
                allies = sum(1 for p in game.defense_ships if p != player.name and game.defense_ships.get(p, 0) > 0)
            return base_total + (allies * 2)
        return base_total


@dataclass
class Thriller(AlienPower):
    """Thriller - Power of Suspense. Edge of your seat."""
    name: str = field(default="Thriller", init=False)
    description: str = field(default="+3 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 3
        return base_total


@dataclass
class Documentary(AlienPower):
    """Documentary - Power of Truth. Facts and reality."""
    name: str = field(default="Documentary", init=False)
    description: str = field(default="+1 per turn (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(5, game.current_turn)
        return base_total


@dataclass
class Animation(AlienPower):
    """Animation - Power of Art. Drawn to life."""
    name: str = field(default="Animation", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = player.get_home_colony_count()
            return base_total + (home_colonies * 2)
        return base_total


@dataclass
class Western_Genre(AlienPower):
    """Western_Genre - Power of the Frontier. Wild west tales."""
    name: str = field(default="Western_Genre", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Musical(AlienPower):
    """Musical - Power of Song. Express through music."""
    name: str = field(default="Musical", init=False)
    description: str = field(default="+3 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if game.get_player_ally_count(player) > 0:
                return base_total + 3
        return base_total


@dataclass
class Fantasy_Genre(AlienPower):
    """Fantasy_Genre - Power of Magic. Mythical worlds."""
    name: str = field(default="Fantasy_Genre", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(player.hand)
        return base_total


@dataclass
class Mystery(AlienPower):
    """Mystery - Power of Clues. Solve the puzzle."""
    name: str = field(default="Mystery", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class WarFilm(AlienPower):
    """WarFilm - Power of Conflict. Battlefield drama."""
    name: str = field(default="War_Film", init=False)
    description: str = field(default="+3 per 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + (ships // 4) * 3


@dataclass
class Noir(AlienPower):
    """Noir - Power of Shadows. Dark and moody."""
    name: str = field(default="Noir", init=False)
    description: str = field(default="+5 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 5
        return base_total


# Register all movie genre powers
AlienRegistry.register(ActionMovie())
AlienRegistry.register(Comedy())
AlienRegistry.register(Drama())
AlienRegistry.register(SciFi())
AlienRegistry.register(Horror_Genre())
AlienRegistry.register(Romance())
AlienRegistry.register(Thriller())
AlienRegistry.register(Documentary())
AlienRegistry.register(Animation())
AlienRegistry.register(Western_Genre())
AlienRegistry.register(Musical())
AlienRegistry.register(Fantasy_Genre())
AlienRegistry.register(Mystery())
AlienRegistry.register(WarFilm())
AlienRegistry.register(Noir())
