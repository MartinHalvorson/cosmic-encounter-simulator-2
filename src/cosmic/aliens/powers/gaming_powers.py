"""
Gaming and Competition themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Gamer(AlienPower):
    """
    Gamer - Power to Play.
    You may re-roll any card draw once per encounter.
    """
    name: str = field(default="Gamer", init=False)
    description: str = field(
        default="Re-draw any card once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Strategist(AlienPower):
    """
    Strategist - Power of Planning.
    +2 attack for each encounter you've won this game.
    """
    name: str = field(default="Strategist", init=False)
    description: str = field(
        default="+2 per encounter won this game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bluffer(AlienPower):
    """
    Bluffer - Power of Deception.
    You may play your encounter card face-down. Opponent must guess
    attack or negotiate. Wrong guess gives you +5.
    """
    name: str = field(default="Bluffer", init=False)
    description: str = field(
        default="Hidden card; wrong opponent guess = +5.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tactician(AlienPower):
    """
    Tactician - Power of Maneuver.
    After ships are committed, you may move 2 ships to any colony.
    """
    name: str = field(default="Tactician", init=False)
    description: str = field(
        default="After launch, move 2 ships to any colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Champion_Gaming(AlienPower):
    """
    Champion - Power of Victory.
    +4 when you have 4+ foreign colonies.
    """
    name: str = field(default="Champion_Gaming", init=False)
    description: str = field(
        default="+4 with 4+ foreign colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Champion bonus."""
        if not player.power_active:
            return base_total

        colonies = player.count_foreign_colonies(game.planets)
        if colonies >= 4:
            return base_total + 4
        return base_total


@dataclass
class Challenger(AlienPower):
    """
    Challenger - Power to Dare.
    You may challenge any player to a duel. Both commit 1 ship,
    highest card wins both ships.
    """
    name: str = field(default="Challenger", init=False)
    description: str = field(
        default="Challenge any player to 1-ship duel.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Underdog(AlienPower):
    """
    Underdog - Power of Persistence.
    +5 when you have the fewest colonies in the game.
    """
    name: str = field(default="Underdog", init=False)
    description: str = field(
        default="+5 when you have fewest colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Underdog bonus."""
        if not player.power_active:
            return base_total

        my_colonies = player.count_foreign_colonies(game.planets)
        min_colonies = min(p.count_foreign_colonies(game.planets) for p in game.players)

        if my_colonies == min_colonies:
            return base_total + 5
        return base_total


@dataclass
class Speedrunner(AlienPower):
    """
    Speedrunner - Power of Haste.
    Your encounters resolve 25% faster (game effect).
    +1 attack for each turn under 50.
    """
    name: str = field(default="Speedrunner", init=False)
    description: str = field(
        default="+1 per turn under 50.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Speed bonus."""
        if not player.power_active:
            return base_total

        turns_under = max(0, 50 - game.current_turn)
        return base_total + turns_under


@dataclass
class Rival(AlienPower):
    """
    Rival - Power of Competition.
    Choose a nemesis. +3 against that player.
    """
    name: str = field(default="Rival", init=False)
    description: str = field(
        default="Choose nemesis: +3 vs them.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Competitor(AlienPower):
    """
    Competitor - Power of Drive.
    Draw 1 card when you lose an encounter.
    """
    name: str = field(default="Competitor", init=False)
    description: str = field(
        default="Draw 1 card when losing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Draw on loss."""
        if not player.power_active:
            return

        card = game.cosmic_deck.draw()
        if card:
            player.add_card(card)


# Register all aliens
AlienRegistry.register(Gamer())
AlienRegistry.register(Strategist())
AlienRegistry.register(Bluffer())
AlienRegistry.register(Tactician())
AlienRegistry.register(Champion_Gaming())
AlienRegistry.register(Challenger())
AlienRegistry.register(Underdog())
AlienRegistry.register(Speedrunner())
AlienRegistry.register(Rival())
AlienRegistry.register(Competitor())
