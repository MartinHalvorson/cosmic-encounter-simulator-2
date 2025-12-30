"""
Basic AI strategy - makes reasonable heuristic-based decisions.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, TYPE_CHECKING

from .base import AIStrategy

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import EncounterCard
    from ..types import Side


@dataclass
class BasicAI(AIStrategy):
    """
    AI that makes reasonable decisions based on simple heuristics.
    """
    name: str = field(default="BasicAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Select encounter card based on position.
        - Offense: Play high cards to win
        - Defense: Play mid-range cards (save best for offense)
        """
        cards = player.get_encounter_cards()
        if not cards:
            raise ValueError(f"{player.name} has no encounter cards!")

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        # Check for Tripler power
        if player.alien and player.alien.name == "Tripler" and player.power_active:
            return player.select_encounter_card_for_tripler()

        if is_offense:
            # Offense: Play highest attack card
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)
            # Fallback to negotiate
            return cards[0]
        else:
            # Defense: Play 3rd highest (save top 2 for offense)
            best = player.select_nth_highest_attack(3)
            if best:
                return best
            # Consider negotiate if we have weak hand
            if negotiate_cards and attack_cards:
                max_attack = max(c.value for c in attack_cards)
                if max_attack < 10:
                    return negotiate_cards[0]
            return cards[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Select ships based on hand strength.
        Strong hand -> commit fewer ships (save for later)
        Weak hand -> commit more ships
        """
        hand_strength = self.get_hand_strength(player)

        # Always commit at least 1, prefer 3-4
        if hand_strength > 0.6:
            return min(3, max_ships)  # Save ships if strong hand
        else:
            return min(4, max_ships)  # Commit more if weak

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Invite allies based on their position.
        - Don't invite players close to winning
        - Prefer players who are behind
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        invited = []

        for ally in potential_allies:
            ally_colonies = ally.count_foreign_colonies(game.planets)

            # Going for win (4 colonies) - be selective
            if my_colonies == 4:
                # Only invite if they're well behind
                if ally_colonies <= 2 and self._rng.random() < 0.3:
                    invited.append(ally)
            else:
                # Invite players with equal or fewer colonies
                if ally_colonies <= my_colonies:
                    invited.append(ally)

        return invited

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
        Join based on strategic considerations:
        - Don't help someone win (4+ colonies)
        - Prefer offense (colony opportunity)
        - Consider own position
        """
        from ..types import Side

        if not invited_by_offense and not invited_by_defense:
            return None

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        # Don't help someone win unless we're also close
        if invited_by_offense and off_colonies >= 4 and my_colonies < 4:
            invited_by_offense = False
        if invited_by_defense and def_colonies >= 4 and my_colonies < 4:
            invited_by_defense = False

        # If only one option, take it (if reasonable)
        if invited_by_offense and not invited_by_defense:
            return Side.OFFENSE
        if invited_by_defense and not invited_by_offense:
            return Side.DEFENSE

        # Both invited - prefer offense for colony chance
        if invited_by_offense and invited_by_defense:
            # Join defense if offense is about to win
            if off_colonies >= 4:
                return Side.DEFENSE
            return Side.OFFENSE

        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Select ships as ally - usually 2."""
        return min(2, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """
        Select planet to attack:
        - Prefer planets we don't have colonies on
        - Prefer planets with fewer defender ships
        """
        home_planets = [p for p in game.planets if p.owner == defense]

        # Filter to planets we don't already have colonies on
        valid = [p for p in home_planets if not p.has_colony(player.name)]
        if not valid:
            valid = home_planets

        # Sort by defender ship count (prefer fewer)
        valid.sort(key=lambda p: p.get_ships(defense.name))

        return valid[0] if valid else home_planets[0]

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """
        Negotiate a deal - usually succeed with colony swap.
        Fail if we're winning and opponent would benefit more.
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        opp_colonies = opponent.count_foreign_colonies(game.planets)

        # If we're ahead, sometimes fail deal
        if my_colonies > opp_colonies and self._rng.random() < 0.3:
            return None

        # Colony swap deal
        return {"type": "colony_swap", "cards": 0}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """
        Use power if it seems beneficial.
        Delegate to alien's own should_use if available.
        """
        if player.alien:
            return player.alien.should_use(game, player, context)
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """
        Take second encounter if:
        - We have encounter cards
        - Not too close to winning (respect shared victory potential)
        """
        if not player.has_encounter_card():
            return False

        colonies = player.count_foreign_colonies(game.planets)

        # At 4 colonies, always go for win
        if colonies == 4:
            return True

        # At 3 colonies, usually want it
        if colonies == 3:
            return True

        # Otherwise, take it most of the time
        return self._rng.random() < 0.8

    def set_seed(self, seed: int) -> None:
        """Set random seed for reproducibility."""
        self._rng.seed(seed)
