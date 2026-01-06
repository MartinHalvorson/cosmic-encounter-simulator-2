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
        # Single-pass categorization of encounter cards
        attack_cards, negotiate_cards, morph_cards = player.categorize_encounter_cards()
        if not attack_cards and not negotiate_cards and not morph_cards:
            raise ValueError(f"{player.name} has no encounter cards!")

        # Check for Tripler power
        if player.alien and player.alien.name == "Tripler" and player.power_active:
            return player.select_encounter_card_for_tripler()

        # Helper to get any encounter card (prefer attack, then negotiate, then morph)
        def any_encounter_card():
            if attack_cards:
                return attack_cards[0]
            elif negotiate_cards:
                return negotiate_cards[0]
            else:
                return morph_cards[0]

        if is_offense:
            # Offense: Play highest attack card
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)
            # Fallback to negotiate
            return any_encounter_card()
        else:
            # Defense: Play 3rd highest (save top 2 for offense)
            if attack_cards:
                # Sort and get 3rd highest (or lowest if fewer than 3)
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                idx = min(2, len(sorted_attacks) - 1)  # 0-indexed, so 3rd = index 2
                return sorted_attacks[idx]
            # Consider negotiate if we have weak hand or no attacks
            if negotiate_cards:
                if not attack_cards or max(c.value for c in attack_cards) < 10:
                    return negotiate_cards[0]
            return any_encounter_card()

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
        Invite allies based on strategic position.
        - Don't invite players close to winning unless necessary
        - Prefer players who are behind
        - Consider overall game state (who's leading)
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        invited = []

        # Get colony counts for all players
        colony_counts = {
            p.name: p.count_foreign_colonies(game.planets)
            for p in game.players
        }
        max_colonies = max(colony_counts.values())
        leader_count = sum(1 for c in colony_counts.values() if c == max_colonies)

        for ally in potential_allies:
            ally_colonies = colony_counts[ally.name]
            should_invite = False

            # Going for win (4 colonies) - be very selective
            if my_colonies == 4:
                # Only invite if they're well behind (won't share win)
                if ally_colonies <= 2:
                    # Low chance to invite - don't want shared victory
                    if self._rng.random() < 0.2:
                        should_invite = True
            # Close to winning (3 colonies)
            elif my_colonies == 3:
                # Don't invite players at 4 (they'd win)
                if ally_colonies < 4:
                    # Prefer players who won't share in the win
                    if ally_colonies < 3:
                        should_invite = True
                    elif self._rng.random() < 0.5:
                        should_invite = True
            else:
                # Earlier game - be more liberal
                # Don't help the leader unless we're also leading
                if ally_colonies == max_colonies and my_colonies < max_colonies:
                    should_invite = self._rng.random() < 0.3  # Sometimes still invite
                elif ally_colonies >= 4:
                    should_invite = False  # Never help someone at 4
                else:
                    should_invite = True

            if should_invite:
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
        - Don't help someone win (4+ colonies) unless we also win
        - Avoid kingmaking (helping others win when we can't)
        - Prefer offense (colony opportunity) but consider risk
        - Consider overall game state and who's leading
        """
        from ..types import Side

        if not invited_by_offense and not invited_by_defense:
            return None

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        # Get colony counts for all players to understand game state
        colony_counts = {
            p.name: p.count_foreign_colonies(game.planets)
            for p in game.players
        }
        max_colonies = max(colony_counts.values())

        # Calculate if joining would create a winner
        off_would_win = off_colonies >= 4
        def_would_win = def_colonies >= 4
        i_would_win = my_colonies >= 4

        # Kingmaking prevention: Don't help someone win if we can't share
        if invited_by_offense and off_would_win and not i_would_win:
            invited_by_offense = False
        if invited_by_defense and def_would_win and not i_would_win:
            invited_by_defense = False

        # If we can win by helping offense, definitely do it
        if invited_by_offense and i_would_win and off_colonies >= 4:
            return Side.OFFENSE

        # Evaluate offense vs defense options
        offense_value = 0
        defense_value = 0

        if invited_by_offense:
            # Value of joining offense: potential colony gain
            offense_value = 1.0  # Base value for colony opportunity

            # Reduce value if offense is leading (don't help leader unless we're close)
            if off_colonies == max_colonies and my_colonies < max_colonies - 1:
                offense_value *= 0.5

            # Increase value if we're close to winning
            if my_colonies >= 3:
                offense_value *= 1.5

            # Reduce value if offense would win and we wouldn't
            if off_would_win and my_colonies < 4:
                offense_value = 0

        if invited_by_defense:
            # Value of joining defense: prevent offense from winning/gaining
            defense_value = 0.5  # Lower base (no colony gain for us)

            # Increase value if offense would win and we don't want that
            if off_would_win and not i_would_win:
                defense_value = 2.0  # Very important to stop them

            # Increase value if offense is the leader
            if off_colonies == max_colonies and off_colonies > my_colonies:
                defense_value *= 1.5

            # Reduce value if defense is also close to winning
            if def_colonies >= 4 and my_colonies < 4:
                defense_value = 0

        # Make decision with some randomness for variety
        if offense_value <= 0 and defense_value <= 0:
            return None

        if offense_value > 0 and defense_value <= 0:
            return Side.OFFENSE

        if defense_value > 0 and offense_value <= 0:
            return Side.DEFENSE

        # Both options valid - choose based on values with some randomness
        if offense_value > defense_value * 1.5:
            return Side.OFFENSE
        elif defense_value > offense_value * 1.5:
            return Side.DEFENSE
        else:
            # Close values - slightly prefer offense for colony opportunity
            return Side.OFFENSE if self._rng.random() < 0.6 else Side.DEFENSE

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Select ships as ally based on stake in the outcome.
        - Send more if this encounter is important (close to winning)
        - Send fewer if just helping out
        """
        my_colonies = player.count_foreign_colonies(game.planets)

        # If we're at 4 colonies and offense wins, we win too - go all in
        if my_colonies >= 4:
            return min(4, max_ships)

        # If we're close (3 colonies), commit more
        if my_colonies == 3:
            return min(3, max_ships)

        # Default: commit 2 ships
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

        # Handle edge case: no home planets (should not happen normally)
        if not home_planets:
            # Fall back to any planet the defense has ships on
            all_planets = [p for p in game.planets if p.get_ships(defense.name) > 0]
            if all_planets:
                return all_planets[0]
            # Last resort: any planet
            if game.planets:
                return game.planets[0]
            return None

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
