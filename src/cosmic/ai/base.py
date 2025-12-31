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

    # ========== Reinforcement Cards ==========

    def select_reinforcement_cards(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool,
        current_total: int,
        opponent_total: int
    ) -> List["Card"]:
        """
        Select reinforcement cards to play after encounter cards are revealed.

        Args:
            game: Current game state
            player: The player selecting reinforcements
            is_offense: Whether the player is offense
            current_total: Player's current combat total
            opponent_total: Opponent's current combat total

        Returns:
            List of reinforcement cards to play (can be empty)
        """
        # Default: play reinforcements if losing
        from ..cards.base import ReinforcementCard
        reinforcements = [c for c in player.hand if isinstance(c, ReinforcementCard)]

        if not reinforcements:
            return []

        # If winning, don't play reinforcements
        if current_total > opponent_total:
            return []

        # If losing, play reinforcements to try to win
        cards_to_play = []
        deficit = opponent_total - current_total + 1  # Need to beat, not just tie (unless Yin)

        # Sort by value ascending to use smallest cards first
        reinforcements.sort(key=lambda c: c.value)

        total_boost = 0
        for card in reinforcements:
            if total_boost < deficit:
                cards_to_play.append(card)
                total_boost += card.value
            else:
                break

        return cards_to_play

    # ========== Kicker Cards ==========

    def select_kicker_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool,
        attack_value: int,
        opponent_total: int
    ) -> Optional["Card"]:
        """
        Select a kicker card to play with the encounter card.

        Kicker cards multiply the attack card value:
        - x-1 (negative) turns attack into negative
        - x0 makes attack 0
        - x1 has no effect (don't play)
        - x2, x3, x4 multiply attack value

        Args:
            game: Current game state
            player: The player selecting a kicker
            is_offense: Whether the player is offense
            attack_value: The attack card value being played
            opponent_total: Estimated opponent total

        Returns:
            KickerCard to play, or None
        """
        from ..cards.base import KickerCard

        kickers = [c for c in player.hand if isinstance(c, KickerCard)]
        if not kickers:
            return None

        # Only play kickers if we have a decent attack card
        if attack_value < 6:
            return None

        # Sort by multiplier value (highest first)
        kickers.sort(key=lambda c: c.value, reverse=True)

        # Calculate if a kicker would help
        my_ships = 4  # Approximate
        my_total = attack_value + my_ships

        for kicker in kickers:
            # Don't play x0 or x1 kickers
            if kicker.value <= 1:
                continue

            # Calculate new total with kicker
            new_attack = attack_value * kicker.value
            new_total = new_attack + my_ships

            # Only play if it would likely help win
            if new_total > opponent_total + 5:  # Margin for safety
                return kicker

        return None

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

    # ========== Defensive Ally Rewards ==========

    def choose_ally_reward(
        self,
        game: "Game",
        player: "Player",
        ships_committed: int
    ) -> str:
        """
        Choose reward type when winning as a defensive ally.

        Per rules: For each ship committed, defensive allies can either:
        - Draw one card from the rewards deck, OR
        - Retrieve one ship from the warp

        Args:
            game: Current game state
            player: The allied player
            ships_committed: Number of ships the ally committed

        Returns:
            "cards" or "ships" indicating the reward type
        """
        # Default: prefer cards if hand is weak, ships if warp is full
        if player.ships_in_warp >= 5 and len(player.hand) >= 6:
            return "ships"
        elif len(player.hand) < 4:
            return "cards"
        elif player.ships_in_warp >= 3:
            return "ships"
        else:
            return "cards"

    # ========== Artifact Usage ==========

    def should_use_artifact(
        self,
        game: "Game",
        player: "Player",
        artifact_type: str,
        context: Dict[str, Any]
    ) -> bool:
        """
        Decide whether to use an artifact card.

        Args:
            game: Current game state
            player: Player with the artifact
            artifact_type: Type of artifact (e.g., "cosmic_zap", "force_field")
            context: Context about when/why artifact might be used

        Returns:
            True if should use the artifact
        """
        from ..types import ArtifactType

        # Default logic for common artifacts
        if artifact_type == ArtifactType.COSMIC_ZAP.value:
            # Use to stop dangerous power usage
            target = context.get("target_player")
            if target and target.alien:
                # Zap strong powers like Machine, Parasite
                if target.alien.name in ["Machine", "Parasite", "Virus", "Void"]:
                    return True
            return False

        elif artifact_type == ArtifactType.MOBIUS_TUBES.value:
            # Use if we have many ships in warp
            return player.ships_in_warp >= 4

        elif artifact_type == ArtifactType.FORCE_FIELD.value:
            # Use if we're about to lose badly as defense
            if context.get("is_defense") and context.get("likely_to_lose"):
                return True
            return False

        elif artifact_type == ArtifactType.CARD_ZAP.value:
            # Zap high attack cards
            target_card = context.get("target_card")
            if target_card and hasattr(target_card, 'value') and target_card.value >= 20:
                return True
            return False

        elif artifact_type == ArtifactType.IONIC_GAS.value:
            # Use if opponents have many allies
            opponent_allies = context.get("opponent_ally_count", 0)
            return opponent_allies >= 2

        elif artifact_type == ArtifactType.PLAGUE.value:
            # Use against player with many ships on one planet
            return False  # Rarely worth it in simulation

        # Default: don't use
        return False

    def select_artifact_to_play(
        self,
        game: "Game",
        player: "Player",
        phase: str,
        context: Dict[str, Any]
    ) -> Optional["Card"]:
        """
        Select an artifact card to play (if any) during the current phase.

        Returns:
            The artifact card to play, or None
        """
        from ..cards.base import ArtifactCard

        # Get artifact cards in hand
        artifacts = [c for c in player.hand if isinstance(c, ArtifactCard)]
        if not artifacts:
            return None

        # Check each artifact to see if we should use it
        for artifact in artifacts:
            if self.should_use_artifact(game, player, artifact.artifact_type.value, context):
                return artifact

        return None

    # ========== Flare Usage ==========

    def select_flare_to_play(
        self,
        game: "Game",
        player: "Player",
        phase: str,
        context: Dict[str, Any]
    ) -> Optional["Card"]:
        """
        Select a flare card to play (if any) during the current phase.

        Flares have Wild effects (usable by anyone) and Super effects
        (only usable by the matching alien).

        Args:
            game: Current game state
            player: Player with flare cards
            phase: Current phase name
            context: Context for flare decision

        Returns:
            The flare card to play, or None
        """
        from ..cards.base import FlareCard

        # Get flare cards in hand
        flares = [c for c in player.hand if isinstance(c, FlareCard)]
        if not flares:
            return None

        my_colonies = player.count_foreign_colonies(game.planets)
        is_main_player = player in (game.offense, game.defense)

        for flare in flares:
            # Check if we can use Super (matching alien)
            can_use_super = (
                player.alien and
                player.alien.name == flare.alien_name and
                player.power_active
            )

            # Combat-boosting flares during reveal
            if phase == "reveal" and is_main_player:
                combat_flares = {"Human", "Warrior", "Macron", "Virus", "Tripler"}
                if flare.alien_name in combat_flares:
                    # Use if we need the boost or are close to winning
                    if my_colonies >= 3 or context.get("need_boost", False):
                        return flare

            # Ship recovery flares during regroup
            if phase == "regroup":
                recovery_flares = {"Zombie", "Healer", "Phantom", "Horde"}
                if flare.alien_name in recovery_flares:
                    if player.ships_in_warp >= 4:
                        return flare

            # Offensive flares at start of encounter
            if phase == "destiny":
                extra_encounter_flares = {"Machine", "Chronos"}
                if flare.alien_name in extra_encounter_flares:
                    if can_use_super and my_colonies >= 3:
                        return flare

            # Super flares are worth using more aggressively
            if can_use_super:
                # Use Super if close to winning
                if my_colonies >= 4:
                    return flare
                # Or if in trouble
                if player.ships_in_warp >= 6:
                    return flare

        return None

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
