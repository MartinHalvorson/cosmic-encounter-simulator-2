"""
Base AI strategy interface for Cosmic Encounter.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import Card, EncounterCard
    from ..types import Side


@dataclass
class AIStrategy(ABC):
    """
    Base class for AI strategies.

    Subclasses implement decision-making logic for various game situations.
    Each player can have a different AI strategy.
    """
    name: str = "BaseAI"

    # ========== Encounter Card Selection ==========

    @abstractmethod
    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Select an encounter card to play.

        Args:
            game: Current game state
            player: The player selecting a card
            is_offense: Whether the player is offense

        Returns:
            The encounter card to play
        """
        pass

    # ========== Ship Commitment ==========

    @abstractmethod
    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Select how many ships to commit to an encounter.

        Args:
            game: Current game state
            player: The player committing ships
            max_ships: Maximum ships allowed

        Returns:
            Number of ships to commit
        """
        pass

    # ========== Alliance Decisions ==========

    @abstractmethod
    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Decide which players to invite as allies.

        Args:
            game: Current game state
            player: The player inviting allies
            potential_allies: Players who can be invited
            as_offense: Whether inviting as offense or defense

        Returns:
            List of players to invite
        """
        pass

    @abstractmethod
    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """
        Decide whether to accept an alliance invitation.

        Args:
            game: Current game state
            player: The player deciding
            offense: The offensive player
            defense: The defensive player
            invited_by_offense: Whether invited by offense
            invited_by_defense: Whether invited by defense

        Returns:
            Side to join, or None to decline
        """
        pass

    @abstractmethod
    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Select how many ships to commit as an ally.
        """
        pass

    # ========== Target Selection ==========

    @abstractmethod
    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """
        Select which planet to attack on the defense's system.

        Args:
            game: Current game state
            player: The offensive player
            defense: The defensive player

        Returns:
            Planet to attack
        """
        pass

    # ========== Deal Negotiation ==========

    @abstractmethod
    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """
        Negotiate a deal when both players reveal negotiate cards.

        Args:
            game: Current game state
            player: The player negotiating
            opponent: The opposing player

        Returns:
            Deal terms, or None if deal fails
        """
        pass

    # ========== Power Usage ==========

    @abstractmethod
    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """
        Decide whether to use an optional alien power.

        Args:
            game: Current game state
            player: The player with the power
            context: Contextual information about the power use

        Returns:
            Whether to use the power
        """
        pass

    # ========== Second Encounter ==========

    @abstractmethod
    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """
        Decide whether to take a second encounter (after winning first).
        """
        pass

    # ========== Utility Methods ==========

    def get_hand_strength(self, player: "Player") -> float:
        """
        Evaluate the strength of a player's hand (0.0 to 1.0).
        """
        attack_cards = player.get_attack_cards()
        if not attack_cards:
            return 0.0

        max_value = max(c.value for c in attack_cards)
        avg_value = sum(c.value for c in attack_cards) / len(attack_cards)

        # Normalize to 0-1 range (40 is max attack value)
        return min(1.0, (max_value / 40 * 0.5) + (avg_value / 40 * 0.5))

    def evaluate_position(self, game: "Game", player: "Player") -> float:
        """
        Evaluate a player's overall position in the game (0.0 to 1.0).
        """
        colonies = player.count_foreign_colonies(game.planets)
        colony_score = colonies / 5.0  # 5 to win

        hand_score = self.get_hand_strength(player)

        ships_in_play = player.total_ships_in_play(game.planets)
        ship_score = min(1.0, ships_in_play / 20.0)

        return (colony_score * 0.5) + (hand_score * 0.3) + (ship_score * 0.2)
