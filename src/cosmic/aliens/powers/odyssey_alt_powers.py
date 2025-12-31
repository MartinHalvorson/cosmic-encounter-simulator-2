"""
Cosmic Odyssey Alternate Timeline aliens.

These are alternate versions of existing aliens with different mechanics,
introduced in the Cosmic Odyssey expansion (2022).
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ==============================================================================
# COSMIC ODYSSEY ALTERNATE TIMELINE ALIENS (2022)
# ==============================================================================

@dataclass
class Brute_Alt(AlienPower):
    """
    Brute (Alternate) - Power to Overwhelm (Cosmic Odyssey).
    Alternate timeline version: Instead of raw strength, this Brute
    uses intimidation. Before cards are played, you may declare a
    minimum attack value. If your opponent plays below that value,
    you win automatically regardless of ships.
    """
    name: str = field(default="Brute_Alt", init=False)
    description: str = field(
        default="Declare minimum attack value; opponent playing lower loses automatically.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    declared_minimum: int = 0

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Declare minimum attack value."""
        if not player.power_active:
            return

        # AI: Declare a moderate minimum (around 10-15)
        import random
        self.declared_minimum = random.randint(8, 15)

    def check_intimidation_win(
        self,
        game: "Game",
        player: "Player",
        opponent_card_value: int
    ) -> bool:
        """Check if opponent is intimidated (played below minimum)."""
        if player.power_active and self.declared_minimum > 0:
            return opponent_card_value < self.declared_minimum
        return False


@dataclass
class Daredevil_Alt(AlienPower):
    """
    Daredevil (Alternate) - Power to Risk All (Cosmic Odyssey).
    Alternate timeline version: Instead of risky bets, this Daredevil
    can commit ALL ships from colonies to a single encounter, but if
    they lose, all those ships go to the warp.
    """
    name: str = field(default="Daredevil_Alt", init=False)
    description: str = field(
        default="May commit all ships to encounter; if lost, all go to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE], init=False
    )

    risked_all: bool = False

    def on_launch(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> int:
        """May commit all ships."""
        if not player.power_active or role != PlayerRole.OFFENSE:
            self.risked_all = False
            return 4  # Normal max

        # AI: Risk all if we have many colonies or are behind
        total_ships = player.total_ships_in_play(game.planets)
        if total_ships > 10:  # Only risk if we have plenty
            self.risked_all = True
            return total_ships

        self.risked_all = False
        return 4


@dataclass
class Demon_Alt(AlienPower):
    """
    Demon (Alternate) - Power to Possess (Cosmic Odyssey).
    Alternate timeline version: Instead of using opponent's hand,
    this Demon temporarily takes control of one opponent's alien power
    for the encounter, using it as their own.
    """
    name: str = field(default="Demon_Alt", init=False)
    description: str = field(
        default="Use one opponent's alien power instead of your own this encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    possessed_power: Optional[str] = None

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Choose a power to possess."""
        if not player.power_active:
            self.possessed_power = None
            return

        # AI: Choose the most useful power
        best_powers = ["Machine", "Virus", "Zombie", "Oracle"]

        for p in game.players:
            if p != player and p.alien and p.alien.name in best_powers:
                self.possessed_power = p.alien.name
                return

        # Default to any opponent's power
        for p in game.players:
            if p != player and p.alien:
                self.possessed_power = p.alien.name
                return


@dataclass
class Grumpus_Alt(AlienPower):
    """
    Grumpus (Alternate) - Power to Complain (Cosmic Odyssey).
    Alternate timeline version: Instead of benefiting from bad
    situations, this Grumpus spreads their negativity. Whenever
    you lose ships to warp, one ship from each other player also
    goes to the warp.
    """
    name: str = field(default="Grumpus_Alt", init=False)
    description: str = field(
        default="When your ships go to warp, each other player loses one ship too.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        reason: str
    ) -> int:
        """When Grumpus ships go to warp, others suffer too."""
        if not player.power_active:
            return count

        # Spread misery to all other players
        for p in game.players:
            if p != player and p.total_ships_in_play(game.planets) > 0:
                p.get_ships_from_colonies(1, game.planets, exclude_last_ship=True)
                p.send_ships_to_warp(1)

        return count


@dataclass
class Locust_Alt(AlienPower):
    """
    Locust (Alternate) - Power to Swarm (Cosmic Odyssey).
    Alternate timeline version: Instead of devouring planets, this
    Locust reproduces rapidly. At the start of each of your turns,
    add 1 ship to each planet where you have a colony.
    """
    name: str = field(default="Locust_Alt", init=False)
    description: str = field(
        default="At start of your turn, add 1 ship to each of your colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Add ships to all colonies."""
        if not player.power_active:
            return

        # Add 1 ship to each colony
        for planet in game.planets:
            if planet.has_colony(player.name):
                # Create new ship (from the cosmic pool)
                planet.add_ships(player.name, 1)


@dataclass
class Masochist_Alt(AlienPower):
    """
    Masochist (Alternate) - Power to Endure (Cosmic Odyssey).
    Alternate timeline version: Instead of enjoying losses, this
    Masochist grows stronger from damage. For each ship you have
    in the warp, add +1 to your encounter total.
    """
    name: str = field(default="Masochist_Alt", init=False)
    description: str = field(
        default="+1 to encounter total for each of your ships in the warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        total: int,
        side: Side
    ) -> int:
        """Add bonus based on ships in warp."""
        if player.power_active:
            return total + player.ships_in_warp
        return total


@dataclass
class Perfectionist_Alt(AlienPower):
    """
    Perfectionist (Alternate) - Power of Precision (Cosmic Odyssey).
    Alternate timeline version: Instead of demanding exact outcomes,
    this Perfectionist wins ties. Any encounter that ends in a tie
    is won by the Perfectionist.
    """
    name: str = field(default="Perfectionist_Alt", init=False)
    description: str = field(
        default="Automatically win all ties in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def resolve_tie(
        self,
        game: "Game",
        player: "Player",
        offense_total: int,
        defense_total: int
    ) -> Optional[str]:
        """Win ties."""
        if player.power_active and offense_total == defense_total:
            if player == game.offense:
                return "offense"
            elif player == game.defense:
                return "defense"
        return None


@dataclass
class Sadist_Alt(AlienPower):
    """
    Sadist (Alternate) - Power to Torment (Cosmic Odyssey).
    Alternate timeline version: Instead of winning when others suffer,
    this Sadist inflicts additional pain. When you win an encounter,
    the loser sends 1 additional ship to the warp.
    """
    name: str = field(default="Sadist_Alt", init=False)
    description: str = field(
        default="When you win, opponent loses 1 additional ship to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Inflict additional punishment on loser."""
        if not player.power_active:
            return

        loser = game.defense if as_offense else game.offense
        if loser and loser.total_ships_in_play(game.planets) > 0:
            loser.get_ships_from_colonies(1, game.planets, exclude_last_ship=True)
            loser.send_ships_to_warp(1)


@dataclass
class Schizoid_Alt(AlienPower):
    """
    Schizoid (Alternate) - Power to Split (Cosmic Odyssey).
    Alternate timeline version: Instead of changing reality, this
    Schizoid can play two encounter cards at once, choosing which
    one to use after seeing the opponent's card.
    """
    name: str = field(default="Schizoid_Alt", init=False)
    description: str = field(
        default="Play two encounter cards; choose which to use after seeing opponent's.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    second_card: Optional[Any] = None

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Play a second card face-down."""
        if not player.power_active:
            self.second_card = None
            return

        # Set aside a second card (AI picks lowest as backup)
        encounter_cards = player.get_encounter_cards()
        if len(encounter_cards) >= 2:
            # Keep the lowest as backup
            self.second_card = min(encounter_cards, key=lambda c: getattr(c, 'value', 0))


@dataclass
class Void_Alt(AlienPower):
    """
    Void (Alternate) - Power to Banish (Cosmic Odyssey).
    Alternate timeline version: Instead of permanently destroying ships,
    this Void can banish cards. Cards played against you are removed
    from the game instead of going to the discard pile.
    """
    name: str = field(default="Void_Alt", init=False)
    description: str = field(
        default="Cards played against you are removed from game, not discarded.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        """Remove opponent's card from game instead of discarding."""
        if not player.power_active:
            return

        # The opponent's card is voided (not added to discard)
        # This is handled in the game resolution by checking for this power


@dataclass
class Zombie_Alt(AlienPower):
    """
    Zombie (Alternate) - Power of Resurrection (Cosmic Odyssey).
    Alternate timeline version: Instead of ships never going to warp,
    this Zombie brings others back. Once per encounter, you may return
    up to 3 ships from ANY player's warp to their colonies.
    """
    name: str = field(default="Zombie_Alt", init=False)
    description: str = field(
        default="Once per encounter, return up to 3 ships from any player's warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    used_this_encounter: bool = False

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Reset usage tracking."""
        self.used_this_encounter = False

    def resurrect_ships(
        self,
        game: "Game",
        player: "Player",
        target: "Player",
        count: int
    ) -> int:
        """Return ships from target's warp to their colonies."""
        if not player.power_active or self.used_this_encounter:
            return 0

        self.used_this_encounter = True
        actual = min(count, 3, target.ships_in_warp)

        if actual > 0:
            target.retrieve_ships_from_warp(actual)
            target.return_ships_to_colonies(actual, target.home_planets)

        return actual


# ==============================================================================
# Register all Alternate Timeline aliens
# ==============================================================================

AlienRegistry.register(Brute_Alt())
AlienRegistry.register(Daredevil_Alt())
AlienRegistry.register(Demon_Alt())
AlienRegistry.register(Grumpus_Alt())
AlienRegistry.register(Locust_Alt())
AlienRegistry.register(Masochist_Alt())
AlienRegistry.register(Perfectionist_Alt())
AlienRegistry.register(Sadist_Alt())
AlienRegistry.register(Schizoid_Alt())
AlienRegistry.register(Void_Alt())
AlienRegistry.register(Zombie_Alt())
