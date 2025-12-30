"""
Special alien powers with unique mechanics for Cosmic Encounter.
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


# ========== Alternate Win Condition Powers ==========

@dataclass
class Masochist(AlienPower):
    """
    Masochist - Win by losing all ships.
    You win the game if all your ships are in the warp (instead of
    losing for having no colonies). You never lose your power.
    """
    name: str = field(default="Masochist", init=False)
    description: str = field(
        default="Win if all your ships are in the warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    has_alternate_win: bool = field(default=True, init=False)

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Win if all ships are in warp."""
        # Starting ships: 5 planets * 4 ships = 20
        total_starting_ships = 20
        return player.ships_in_warp >= total_starting_ships


@dataclass
class Genius(AlienPower):
    """
    Genius - Win by having 20+ cards in hand.
    You win the game if you have 20 or more cards in your hand.
    """
    name: str = field(default="Genius", init=False)
    description: str = field(
        default="Win if you have 20+ cards in hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    has_alternate_win: bool = field(default=True, init=False)

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Win if 20+ cards in hand."""
        return len(player.hand) >= 20


@dataclass
class TickTock(AlienPower):
    """
    Tick-Tock - Win after accumulating 10 tokens.
    Gain a token on defensive wins and successful deals.
    Win when you have 10 tokens.
    """
    name: str = field(default="Tick-Tock", init=False)
    description: str = field(
        default="Win at 10 tokens (gain on defense wins/deals).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    has_alternate_win: bool = field(default=True, init=False)

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Win at 10 tokens."""
        return player.tick_tock_tokens >= 10

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Gain token on defensive win."""
        if as_main_player and game.defense == player and player.power_active:
            player.tick_tock_tokens += 1

    def on_deal_success(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> None:
        """Gain token on successful deal."""
        if player.power_active:
            player.tick_tock_tokens += 1


# ========== Ship Manipulation Powers ==========

@dataclass
class Vacuum(AlienPower):
    """
    Vacuum - When you lose ships, another player loses ships too.
    Whenever you lose ships to the warp, you choose another player
    to lose the same number of ships to the warp.
    """
    name: str = field(default="Vacuum", init=False)
    description: str = field(
        default="When you lose ships, choose another to lose same.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        source: str
    ) -> int:
        """Choose another player to lose ships."""
        if not player.power_active or count == 0:
            return count

        # Target the leading player
        others = [p for p in game.players if p != player]
        if not others:
            return count

        target = max(others, key=lambda p: p.count_foreign_colonies(game.planets))

        # Remove ships from target
        removed = target.get_ships_from_colonies(count, game.planets, exclude_last_ship=False)
        target.send_ships_to_warp(removed)

        return count


@dataclass
class Void(AlienPower):
    """
    Void - Ships you defeat go to the void instead of warp.
    Ships lost to you in an encounter are removed from the game
    instead of going to the warp.
    """
    name: str = field(default="Void", init=False)
    description: str = field(
        default="Ships you defeat are removed from the game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Disease(AlienPower):
    """
    Disease - Eradicate colonies on planets you colonize.
    When you establish a colony on a planet, all other players'
    ships on that planet go to the warp.
    """
    name: str = field(default="Disease", init=False)
    description: str = field(
        default="Colonize: other players' ships go to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.OFFENSIVE_ALLY],
        init=False
    )

    def on_gain_colony(
        self,
        game: "Game",
        player: "Player",
        planet: Any
    ) -> None:
        """Eradicate other colonies."""
        if not player.power_active:
            return

        for colonizer_name in planet.colonizers():
            if colonizer_name != player.name:
                colonizer = game.get_player_by_name(colonizer_name)
                if colonizer:
                    ships = planet.clear_player(colonizer_name)
                    colonizer.send_ships_to_warp(ships)


# ========== Other Unique Powers ==========

@dataclass
class Oracle(AlienPower):
    """
    Oracle - See opponent's card before selecting yours.
    As offense, you may see the defense's encounter card before
    selecting your own.
    """
    name: str = field(default="Oracle", init=False)
    description: str = field(
        default="As offense, see defense's card before picking yours.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Calculator(AlienPower):
    """
    Calculator - Always know exact totals before cards are played.
    You always know the exact totals for both sides as if cards
    were already revealed.
    """
    name: str = field(default="Calculator", init=False)
    description: str = field(
        default="Know exact totals before cards are played.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Clone(AlienPower):
    """
    Clone - Retrieve encounter card instead of discarding.
    After an encounter, you may add your encounter card back to
    your hand instead of discarding it.
    """
    name: str = field(default="Clone", init=False)
    description: str = field(
        default="Keep your encounter card instead of discarding.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Sorcerer(AlienPower):
    """
    Sorcerer - Swap encounter cards before reveal.
    As a main player, after cards are selected but before reveal,
    you may swap your encounter card with your opponent's.
    """
    name: str = field(default="Sorcerer", init=False)
    description: str = field(
        default="Swap encounter cards before reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Spiff(AlienPower):
    """
    Spiff - Land ships on any planet after winning.
    When you win an encounter as offense, you may land your ships
    on any planet instead of the targeted planet.
    """
    name: str = field(default="Spiff", init=False)
    description: str = field(
        default="Win offense: land on any planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Remora(AlienPower):
    """
    Remora - Draw cards when others draw.
    Whenever any other player draws one or more cards from the deck,
    you also draw one card.
    """
    name: str = field(default="Remora", init=False)
    description: str = field(
        default="Draw 1 card whenever others draw cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Citadel(AlienPower):
    """
    Citadel - Defense ships count double on home planets.
    When you are the defense on one of your home planets, your
    ships count double.
    """
    name: str = field(default="Citadel", init=False)
    description: str = field(
        default="Defense on home: your ships count double.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Double defense ships on home planets."""
        if side != Side.DEFENSE or not player.power_active:
            return base_count

        # Check if defending home planet
        if game.defense_planet and game.defense_planet.owner == player:
            my_ships = game.defense_ships.get(player.name, 0)
            return base_count + my_ships  # Double by adding again

        return base_count


@dataclass
class Mite(AlienPower):
    """
    Mite - Force others to discard or forfeit.
    At the start of each encounter, each other player must either
    give you a card or forfeit the encounter.
    """
    name: str = field(default="Mite", init=False)
    description: str = field(
        default="Others give you a card or forfeit each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chosen(AlienPower):
    """
    Chosen - Destiny always points to leading player.
    When destiny would determine the defense, you may instead
    choose to encounter the player with the most foreign colonies.
    """
    name: str = field(default="Chosen", init=False)
    description: str = field(
        default="Choose to attack the leading player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )

    def on_destiny(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        destiny_player: "Player"
    ) -> Optional["Player"]:
        """Choose to attack the leader."""
        if not player.power_active or role != PlayerRole.OFFENSE:
            return None

        # Find player with most foreign colonies (not us)
        others = [p for p in game.players if p != player]
        if not others:
            return None

        leader = max(others, key=lambda p: p.count_foreign_colonies(game.planets))

        # Only redirect if leader is ahead
        if leader.count_foreign_colonies(game.planets) > player.count_foreign_colonies(game.planets):
            return leader

        return None


@dataclass
class Amoeba(AlienPower):
    """
    Amoeba - Add extra ships to encounter.
    As a main player, you may add up to 4 additional ships from
    your other colonies to the encounter.
    """
    name: str = field(default="Amoeba", init=False)
    description: str = field(
        default="Add up to 4 extra ships to encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Reincarnator(AlienPower):
    """
    Reincarnator - Get a new alien when losing power.
    When you would lose your alien power, you instead draw a new
    alien at random and become that alien.
    """
    name: str = field(default="Reincarnator", init=False)
    description: str = field(
        default="Get new random alien instead of losing power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Masochist())
AlienRegistry.register(Genius())
AlienRegistry.register(TickTock())
AlienRegistry.register(Vacuum())
AlienRegistry.register(Void())
AlienRegistry.register(Disease())
AlienRegistry.register(Oracle())
AlienRegistry.register(Calculator())
AlienRegistry.register(Clone())
AlienRegistry.register(Sorcerer())
AlienRegistry.register(Spiff())
AlienRegistry.register(Remora())
AlienRegistry.register(Citadel())
AlienRegistry.register(Mite())
AlienRegistry.register(Chosen())
AlienRegistry.register(Amoeba())
AlienRegistry.register(Reincarnator())
