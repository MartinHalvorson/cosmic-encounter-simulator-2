"""
Tactical AI - Makes decisions based on win probability calculations and threat assessment.

This AI focuses on:
- Calculating expected win probabilities for each decision
- Assessing opponent threat levels
- Optimizing for highest expected value plays
- Resource management (ships, cards, power uses)
"""

import random
import math
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, TYPE_CHECKING

from .base import AIStrategy

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import EncounterCard, AttackCard, Card
    from ..types import Side


# Expected win rates by card value (based on typical distributions)
CARD_WIN_RATES = {
    1: 0.10, 2: 0.12, 3: 0.15, 4: 0.18, 5: 0.22,
    6: 0.28, 7: 0.35, 8: 0.42, 9: 0.48, 10: 0.52,
    11: 0.55, 12: 0.58, 13: 0.62, 14: 0.65, 15: 0.68,
    16: 0.72, 17: 0.78, 18: 0.82, 19: 0.88, 20: 0.92,
    23: 0.95, 30: 0.97, 40: 0.99
}


@dataclass
class TacticalAI(AIStrategy):
    """
    AI that calculates expected values and win probabilities.

    Makes decisions to maximize expected game-winning probability,
    not just individual encounter wins.
    """
    name: str = field(default="TacticalAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    # Risk tolerance (0 = very conservative, 1 = very aggressive)
    risk_tolerance: float = 0.5

    # Track game state for adaptive decisions
    _turn_count: int = 0
    _wins_this_game: int = 0
    _losses_this_game: int = 0

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Select card based on expected win probability and game state.
        """
        cards = player.get_encounter_cards()
        if not cards:
            # Player needs a new hand - raise error to trigger redraw
            raise ValueError(f"{player.name} has no encounter cards!")

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        # Fallback if no standard cards (e.g., only morphs)
        if not attack_cards and not negotiate_cards:
            return cards[0]

        # Get game state
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if is_offense else game.offense
        opp_colonies = opponent.count_foreign_colonies(game.planets) if opponent else 0

        # Calculate win pressure (how badly do we need to win?)
        win_pressure = self._calculate_win_pressure(my_colonies, opp_colonies, game)

        # If close to winning or opponent close, adjust strategy
        if my_colonies >= 4:
            # Go aggressive to close out
            return self._select_aggressive_card(attack_cards, negotiate_cards)
        elif opp_colonies >= 4:
            # Need to stop them - high risk plays
            return self._select_high_risk_card(attack_cards, negotiate_cards)

        # Normal play: optimize expected value
        return self._select_optimal_card(
            player, attack_cards, negotiate_cards, is_offense, game, win_pressure
        )

    def _calculate_win_pressure(
        self,
        my_colonies: int,
        opp_colonies: int,
        game: "Game"
    ) -> float:
        """
        Calculate how urgent it is to win (0.0 to 1.0).

        Higher values mean more pressure to win now.
        """
        # Base pressure from colony counts
        my_progress = my_colonies / 5.0
        opp_progress = opp_colonies / 5.0

        # Pressure increases if opponent is ahead
        relative_position = opp_progress - my_progress

        # Late game increases pressure
        turn_pressure = min(1.0, game.current_turn / 50)

        # Combine factors
        pressure = 0.3 + (relative_position * 0.4) + (turn_pressure * 0.3)
        return max(0.0, min(1.0, pressure))

    def _select_aggressive_card(
        self,
        attack_cards: List["AttackCard"],
        negotiate_cards: List
    ) -> Optional["EncounterCard"]:
        """Select highest attack card to close out the game."""
        if attack_cards:
            return max(attack_cards, key=lambda c: c.value)
        if negotiate_cards:
            return negotiate_cards[0]
        return None

    def _select_high_risk_card(
        self,
        attack_cards: List["AttackCard"],
        negotiate_cards: List
    ) -> Optional["EncounterCard"]:
        """Select high-value card to stop opponent from winning."""
        if attack_cards:
            # Use highest card to maximize win chance
            return max(attack_cards, key=lambda c: c.value)
        if negotiate_cards:
            return negotiate_cards[0]
        return None

    def _select_optimal_card(
        self,
        player: "Player",
        attack_cards: List["AttackCard"],
        negotiate_cards: List,
        is_offense: bool,
        game: "Game",
        win_pressure: float
    ) -> Optional["EncounterCard"]:
        """
        Select card that maximizes expected game value.

        Considers:
        - Win probability of each card
        - Value of winning vs losing
        - Future card availability
        """
        if not attack_cards:
            if negotiate_cards:
                return negotiate_cards[0]
            return None

        # Estimate opponent's likely card value
        opp_expected_value = self._estimate_opponent_card(game, is_offense)

        # Calculate expected value for each card
        best_card = None
        best_ev = float('-inf')

        for card in attack_cards:
            # Win probability
            win_prob = self._calculate_win_probability(
                card.value, opp_expected_value, game, is_offense
            )

            # Value of winning (adjusted for game state)
            win_value = 1.0 + win_pressure * 0.5

            # Cost of losing (also adjusted)
            lose_cost = 0.5 + win_pressure * 0.3

            # Card conservation value (save high cards for later)
            conservation_value = self._calculate_conservation_value(
                card.value, player.hand, game
            )

            # Expected value
            ev = (win_prob * win_value) - ((1 - win_prob) * lose_cost) + conservation_value

            if ev > best_ev:
                best_ev = ev
                best_card = card

        # Consider negotiate if EV of attack is low
        if negotiate_cards and best_ev < 0.3:
            # Negotiate might be better
            if self._rng.random() < 0.3:  # 30% chance to negotiate
                return negotiate_cards[0]

        return best_card if best_card else attack_cards[0]

    def _estimate_opponent_card(
        self,
        game: "Game",
        is_offense: bool
    ) -> float:
        """Estimate opponent's likely card value."""
        opponent = game.defense if is_offense else game.offense
        opp_hand_size = opponent.hand_size() if opponent else 8

        # Larger hands tend to have higher average best cards
        # Expected best attack in hand of size N ≈ 10 + 2*sqrt(N)
        expected_best = min(20, 10 + 2 * math.sqrt(opp_hand_size))

        # Assume they'll play slightly below their best
        return expected_best * 0.85

    def _calculate_win_probability(
        self,
        my_card: int,
        opp_expected: float,
        game: "Game",
        is_offense: bool
    ) -> float:
        """Calculate probability of winning with this card."""
        # Get ship counts
        if is_offense:
            my_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4
            opp_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
        else:
            my_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
            opp_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4

        # Calculate totals
        my_total = my_card + my_ships
        opp_total = opp_expected + opp_ships

        # Win probability (sigmoid function of difference)
        diff = my_total - opp_total
        win_prob = 1 / (1 + math.exp(-diff / 5))

        return win_prob

    def _calculate_conservation_value(
        self,
        card_value: int,
        hand: List["Card"],
        game: "Game"
    ) -> float:
        """
        Calculate value of conserving this card for later.

        High cards should be saved early game, used late game.
        """
        # Late game progress
        late_game_factor = min(1.0, game.current_turn / 30)

        # Card rarity (high cards are more valuable to save)
        rarity = card_value / 20.0

        # Early game: penalize using high cards
        # Late game: encourage using high cards
        conservation = (rarity - 0.5) * (0.5 - late_game_factor) * 0.2

        return conservation

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Select ships based on win probability optimization.
        """
        # Get available ships
        available = min(max_ships, player.total_ships_in_play(game.planets))
        if available <= 0:
            return 0

        my_colonies = player.count_foreign_colonies(game.planets)

        # Close to winning: commit max
        if my_colonies >= 4:
            return available

        # Calculate optimal ship count
        # More ships = higher win chance but more risk
        # Balance risk vs reward

        # Base on hand strength
        hand_strength = self.get_hand_strength(player)

        if hand_strength > 0.7:
            # Strong hand: commit more
            return min(available, 4)
        elif hand_strength > 0.4:
            # Medium hand: moderate
            return min(available, 3)
        else:
            # Weak hand: conserve
            return min(available, 2)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Invite allies based on threat assessment and expected benefit.
        """
        if not potential_allies:
            return []

        invited = []
        my_colonies = player.count_foreign_colonies(game.planets)

        for ally in potential_allies:
            ally_colonies = ally.count_foreign_colonies(game.planets)

            # Don't help players close to winning
            if ally_colonies >= 4 and my_colonies < 4:
                continue

            # Evaluate ally value
            ally_value = self._evaluate_ally_value(game, player, ally, as_offense)

            # Invite if value is positive
            if ally_value > 0.2:
                invited.append(ally)

        return invited[:2]  # Limit invitations

    def _evaluate_ally_value(
        self,
        game: "Game",
        player: "Player",
        ally: "Player",
        as_offense: bool
    ) -> float:
        """Evaluate how valuable an ally would be."""
        value = 0.0

        # Ships they might commit (estimate based on ships in play)
        ally_ships = min(4, ally.total_ships_in_play(game.planets))
        value += ally_ships * 0.1

        # Their power's usefulness
        if ally.alien and ally.power_active:
            power_name = ally.alien.name
            # Combat-boosting allies are more valuable
            if power_name in {"Human", "Warrior", "Virus", "Macron"}:
                value += 0.3

        # Negative: they'll benefit from the win
        ally_colonies = ally.count_foreign_colonies(game.planets)
        if ally_colonies >= 3:
            value -= 0.2  # They're already doing well

        return value

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
        Decide alliance based on expected value of joining each side.
        """
        from ..types import Side

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        # Calculate join value for each side
        offense_value = 0.0
        defense_value = 0.0

        if invited_by_offense:
            # Offensive ally gets colony if win
            colony_value = 1.0 if my_colonies < 4 else 0.3
            offense_value = self._estimate_side_win_prob(game, True) * colony_value

            # Penalty for helping leader
            if off_colonies >= 4:
                offense_value -= 0.5

        if invited_by_defense:
            # Defensive ally gets cards/ships if win
            reward_value = 0.4
            defense_value = self._estimate_side_win_prob(game, False) * reward_value

            # Penalty for helping leader
            if def_colonies >= 4:
                defense_value -= 0.3

        # Choose best option
        if offense_value > defense_value and offense_value > 0.15:
            return Side.OFFENSE
        elif defense_value > 0.1:
            return Side.DEFENSE
        return None

    def _estimate_side_win_prob(
        self,
        game: "Game",
        offense_side: bool
    ) -> float:
        """Estimate probability that a side will win the encounter."""
        # Base 50/50
        prob = 0.5

        # Adjust for ship counts
        off_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4
        def_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4

        ship_diff = off_ships - def_ships
        prob += ship_diff * 0.03  # Each ship ≈ 3% difference

        # Adjust for hand sizes
        if game.offense and game.defense:
            off_hand = game.offense.hand_size()
            def_hand = game.defense.hand_size()
            hand_diff = off_hand - def_hand
            prob += hand_diff * 0.02  # Each card ≈ 2% difference

        if offense_side:
            return max(0.1, min(0.9, prob))
        else:
            return max(0.1, min(0.9, 1 - prob))

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Select ships to commit as ally."""
        available = min(max_ships, player.total_ships_in_play(game.planets))

        # Commit moderate amount (1-2)
        return min(available, 2)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """
        Select planet to attack based on:
        - Defensive ship count
        - Strategic value
        - Win probability
        """
        defense_planets = [p for p in game.planets if p.owner == defense]

        if not defense_planets:
            # Attack any available planet
            all_planets = [p for p in game.planets if p.owner != player]
            return all_planets[0] if all_planets else game.planets[0]

        # Evaluate each planet
        best_planet = None
        best_value = float('-inf')

        for planet in defense_planets:
            # Ships defending
            def_ships = planet.get_ships(defense.name)

            # Value: lower defense = easier win
            value = 10 - def_ships

            # Bonus for establishing new colony
            if not planet.has_colony(player.name):
                value += 2

            if value > best_value:
                best_value = value
                best_planet = planet

        return best_planet or defense_planets[0]

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Negotiate based on relative positions."""
        my_colonies = player.count_foreign_colonies(game.planets)
        opp_colonies = opponent.count_foreign_colonies(game.planets)

        # Default: simple card trade
        deal = {
            "type": "card_trade",
            "my_cards": 1,
            "their_cards": 1
        }

        # If I'm behind, try for colonies
        if my_colonies < opp_colonies - 1:
            deal = {
                "type": "colony_exchange",
                "give_colony": False,
                "receive_colony": True
            }

        return deal

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power if expected value is positive."""
        my_colonies = player.count_foreign_colonies(game.planets)

        # More aggressive power use when close to winning
        threshold = 0.3 if my_colonies >= 3 else 0.5

        return self._rng.random() > threshold

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter if close to winning and have good hand."""
        my_colonies = player.count_foreign_colonies(game.planets)
        hand_strength = self.get_hand_strength(player)

        # Yes if close to winning with decent hand
        if my_colonies >= 4 and hand_strength > 0.3:
            return True

        # Yes if strong hand and not too far behind
        if my_colonies >= 3 and hand_strength > 0.5:
            return True

        return False
