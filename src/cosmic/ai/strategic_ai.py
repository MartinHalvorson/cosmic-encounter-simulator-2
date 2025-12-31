"""
Strategic AI - makes sophisticated decisions based on game state analysis.

This AI considers:
- Opponent modeling and behavior patterns
- Power synergies and interactions
- Card counting and probability estimation
- Dynamic aggression based on game state
- Risk assessment for various choices
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Set, TYPE_CHECKING

from .base import AIStrategy

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import EncounterCard, AttackCard, Card
    from ..types import Side


# Powers that are dangerous to let win
DANGEROUS_POWERS = {
    "Machine", "Virus", "Void", "Parasite", "Loser", "Masochist",
    "Zombie", "Oracle", "Tick-Tock", "Chosen", "Chronos"
}

# Powers that synergize well with negotiation
NEGOTIATE_FRIENDLY_POWERS = {
    "Pacifist", "Diplomat", "Trader", "Philanthropist", "Empath"
}

# Powers that benefit from high attack cards
HIGH_CARD_POWERS = {
    "Human", "Warrior", "Calculator", "Grudge", "Shadow"
}

# Powers that benefit from low cards
LOW_CARD_POWERS = {
    "Loser", "Anti-Matter", "Underdog"
}


@dataclass
class StrategicAI(AIStrategy):
    """
    Advanced AI that considers multiple factors and opponent modeling.

    Features:
    - Tracks observed opponent behavior
    - Adjusts strategy based on alien powers in play
    - Considers card probability and expected values
    - Dynamic aggression levels based on game state
    """
    name: str = field(default="StrategicAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    # Opponent modeling - track aggression levels
    _opponent_aggression: Dict[str, float] = field(default_factory=dict)

    # Track high cards we've seen played (rough card counting)
    _high_cards_seen: int = 0
    _cards_seen_total: int = 0

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Sophisticated card selection based on:
        - Estimated opponent hand strength
        - Ship counts on both sides
        - Power interactions and synergies
        - Win proximity for both players
        - Threat assessment of opponent's power
        """
        cards = player.get_encounter_cards()
        if not cards:
            raise ValueError(f"{player.name} has no encounter cards!")

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()
        morph_cards = [c for c in cards if hasattr(c, 'card_type') and c.card_type.value == 'morph']

        # Get opponent info
        opponent = game.defense if is_offense else game.offense
        opp_hand_size = opponent.hand_size()
        opp_alien = opponent.alien.name if opponent.alien and opponent.power_active else None

        # Handle special powers - expanded alien-specific strategies
        if player.alien and player.power_active:
            alien_name = player.alien.name
            card = self._select_card_for_power(
                alien_name, attack_cards, negotiate_cards, morph_cards, game, player
            )
            if card:
                return card

        # Calculate ship advantage
        if is_offense:
            my_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4
            opp_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
        else:
            my_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
            opp_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4

        ship_advantage = my_ships - opp_ships

        # Adjust strategy based on opponent's power
        strategy_modifier = self._get_opponent_strategy_modifier(opp_alien, opponent)

        if is_offense:
            return self._select_offense_card(
                player, attack_cards, negotiate_cards,
                ship_advantage, opp_hand_size, game,
                strategy_modifier
            )
        else:
            return self._select_defense_card(
                player, attack_cards, negotiate_cards,
                ship_advantage, opp_hand_size, game,
                strategy_modifier
            )

    def _select_card_for_power(
        self,
        alien_name: str,
        attack_cards: List["AttackCard"],
        negotiate_cards: List,
        morph_cards: List,
        game: "Game",
        player: "Player"
    ) -> Optional["EncounterCard"]:
        """Select card based on player's alien power."""

        if alien_name == "Tripler":
            return player.select_encounter_card_for_tripler()

        if alien_name == "Pacifist" and negotiate_cards:
            return negotiate_cards[0]

        if alien_name == "Loser":
            if attack_cards:
                return min(attack_cards, key=lambda c: c.value)

        if alien_name == "Anti-Matter":
            # Anti-Matter reverses totals, so low cards win
            if attack_cards:
                return min(attack_cards, key=lambda c: c.value)

        if alien_name == "Virus":
            # Virus multiplies ships, so ship count matters more than card
            # Play mid-range cards to conserve high ones
            if attack_cards and len(attack_cards) > 2:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value)
                return sorted_attacks[len(sorted_attacks) // 2]

        if alien_name == "Human":
            # Human gets +4, can play slightly lower cards
            if attack_cards:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                # Second highest is often sufficient
                return sorted_attacks[min(1, len(sorted_attacks) - 1)]

        if alien_name == "Macron":
            # Macron ships count as 4 each, card value less important
            if attack_cards and len(attack_cards) > 1:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                return sorted_attacks[min(1, len(sorted_attacks) - 1)]

        if alien_name == "Calculator":
            # Calculator uses hand size as value - any attack works
            if attack_cards:
                # Play lowest attack to preserve options
                return min(attack_cards, key=lambda c: c.value)

        if alien_name == "Gambler":
            # Gambler can swap cards after seeing opponent's
            # Play conservatively
            if attack_cards:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                return sorted_attacks[min(1, len(sorted_attacks) - 1)]

        if alien_name == "Trader" and negotiate_cards:
            # Trader benefits from negotiate plays
            if self._rng.random() < 0.4:
                return negotiate_cards[0]

        if alien_name == "Sorcerer":
            # Sorcerer swaps cards after reveal - play low
            if attack_cards:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value)
                return sorted_attacks[0]

        if alien_name == "Clone":
            # Clone can replay cards - go for high card plays
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        if alien_name == "Oracle":
            # Oracle sees opponent's card first - no special selection needed
            # Will be handled in game logic
            pass

        if alien_name == "Mirror":
            # Mirror reverses digits - 14 becomes 41
            if attack_cards:
                def mirror_value(card):
                    v = card.value
                    if v >= 10:
                        return int(str(v)[::-1])
                    return v
                return max(attack_cards, key=mirror_value)

        # Use morph if we have one and no great attacks
        if morph_cards and attack_cards:
            best_attack = max(c.value for c in attack_cards)
            if best_attack < 10:
                return morph_cards[0]

        return None

    def _get_opponent_strategy_modifier(
        self,
        opp_alien: Optional[str],
        opponent: "Player"
    ) -> Dict[str, Any]:
        """Get strategy modifications based on opponent's power."""
        modifier = {
            "avoid_negotiate": False,
            "play_aggressive": False,
            "play_defensive": False,
            "expect_low_card": False,
            "expect_high_card": False
        }

        if not opp_alien:
            return modifier

        if opp_alien == "Loser":
            modifier["expect_low_card"] = True
            modifier["play_defensive"] = True  # Low card often beats us

        if opp_alien == "Anti-Matter":
            modifier["expect_low_card"] = True

        if opp_alien in {"Virus", "Macron", "Human"}:
            modifier["play_aggressive"] = True  # Need high cards

        if opp_alien == "Sorcerer":
            # They'll swap if they're losing - play mid cards
            modifier["play_defensive"] = True

        if opp_alien in NEGOTIATE_FRIENDLY_POWERS:
            modifier["avoid_negotiate"] = True  # They benefit from deals

        return modifier

    def _select_offense_card(
        self,
        player: "Player",
        attacks: List["AttackCard"],
        negotiates: List,
        ship_advantage: int,
        opp_hand_size: int,
        game: "Game",
        modifier: Dict[str, Any] = None
    ) -> "EncounterCard":
        """Select card as offense with strategic considerations."""
        modifier = modifier or {}
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense

        # Calculate threat level of opponent
        opp_colonies = opponent.count_foreign_colonies(game.planets)
        opponent_near_win = opp_colonies >= 4

        # Going for win - play best card
        if my_colonies >= 4:
            if attacks:
                return max(attacks, key=lambda c: c.value)

        # Opponent near win - block aggressively
        if opponent_near_win and attacks:
            # Play high to prevent their colony
            return max(attacks, key=lambda c: c.value)

        # Adjust for expected opponent strategy
        if modifier.get("expect_low_card"):
            # Against Loser/Anti-Matter, our high cards are devalued
            # Play mid-range to not waste high cards
            if attacks and len(attacks) > 2:
                sorted_attacks = sorted(attacks, key=lambda c: c.value)
                return sorted_attacks[len(sorted_attacks) // 2]

        if modifier.get("play_aggressive"):
            # Need high cards against Virus/Macron/Human
            if attacks:
                return max(attacks, key=lambda c: c.value)

        # Have ship advantage - can play lower card
        if ship_advantage >= 3 and attacks:
            # Play a mid-range card
            sorted_attacks = sorted(attacks, key=lambda c: c.value, reverse=True)
            idx = min(1, len(sorted_attacks) - 1)  # Second highest
            return sorted_attacks[idx]

        # Ship disadvantage - need high card or negotiate
        if ship_advantage <= -3:
            # Consider negotiate if opponent likely has high cards
            avoid_negotiate = modifier.get("avoid_negotiate", False)
            if negotiates and opp_hand_size >= 4 and attacks and not avoid_negotiate:
                best_attack = max(c.value for c in attacks)
                if best_attack < 12:  # Our best isn't great
                    return negotiates[0]

        # Default: play highest attack
        if attacks:
            return max(attacks, key=lambda c: c.value)

        return negotiates[0] if negotiates else player.get_encounter_cards()[0]

    def _select_defense_card(
        self,
        player: "Player",
        attacks: List["AttackCard"],
        negotiates: List,
        ship_advantage: int,
        opp_hand_size: int,
        game: "Game",
        modifier: Dict[str, Any] = None
    ) -> "EncounterCard":
        """Select card as defense with strategic considerations."""
        modifier = modifier or {}
        opponent = game.offense

        # Calculate threat level
        opp_colonies = opponent.count_foreign_colonies(game.planets)
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent_near_win = opp_colonies >= 4

        # If opponent is about to win, defend aggressively
        if opponent_near_win and attacks:
            return max(attacks, key=lambda c: c.value)

        # Adjust for expected opponent strategy
        if modifier.get("expect_low_card"):
            # Against Loser/Anti-Matter
            if attacks:
                # Play our lowest card - it will probably win
                return min(attacks, key=lambda c: c.value)

        if modifier.get("play_aggressive"):
            # Against Virus/Macron/Human - need high cards
            if attacks:
                return max(attacks, key=lambda c: c.value)

        # If we have ship advantage, play lower card
        if ship_advantage >= 2 and attacks:
            sorted_attacks = sorted(attacks, key=lambda c: c.value)
            # Play lowest card that might still win
            for card in sorted_attacks:
                if card.value + ship_advantage >= 10:  # Likely to beat average
                    return card
            return sorted_attacks[-1]  # Or just play highest

        # Consider negotiate for compensation (if not near winning)
        avoid_negotiate = modifier.get("avoid_negotiate", False)
        if negotiates and attacks and my_colonies < 4 and not avoid_negotiate:
            best_attack = max(c.value for c in attacks)
            # Negotiate gives guaranteed cards, risky attack might fail
            if best_attack < 8:
                return negotiates[0]
            # Also negotiate if ship disadvantage is severe
            if ship_advantage <= -4 and best_attack < 15:
                return negotiates[0]

        # Play third highest (save top 2 for offense)
        if attacks:
            sorted_attacks = sorted(attacks, key=lambda c: c.value, reverse=True)
            idx = min(2, len(sorted_attacks) - 1)
            return sorted_attacks[idx]

        return negotiates[0] if negotiates else player.get_encounter_cards()[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Commit ships based on:
        - Colony count (more if going for win)
        - Hand strength
        - Opponent's likely response
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        total_ships = player.total_ships_in_play(game.planets)
        hand_strength = self.get_hand_strength(player)

        # Going for win - commit max
        if my_colonies >= 4:
            return max_ships

        # Have many ships - can afford to commit more
        if total_ships > 15:
            base = 4
        elif total_ships > 10:
            base = 3
        else:
            base = 2

        # Adjust based on hand strength
        if hand_strength > 0.7:
            base = max(2, base - 1)  # Strong hand, save ships
        elif hand_strength < 0.3:
            base = min(max_ships, base + 1)  # Weak hand, use more ships

        return min(base, max_ships)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Strategic invitations:
        - Invite players who won't benefit too much
        - Consider power synergies
        - Balance ship gains vs shared victory risk
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        invited = []

        for ally in potential_allies:
            ally_colonies = ally.count_foreign_colonies(game.planets)

            # Never invite someone about to win (unless we're also winning)
            if ally_colonies >= 4 and my_colonies < 4:
                continue

            # Strategic considerations based on colonies
            if my_colonies == 4:
                # Only invite if they can't win with us
                if ally_colonies <= 2:
                    invited.append(ally)
            elif my_colonies == 3:
                # Be somewhat selective
                if ally_colonies <= 3:
                    invited.append(ally)
            else:
                # Earlier game - invite most players
                if ally_colonies <= my_colonies + 1:
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
        Sophisticated alliance decisions:
        - Model likely encounter outcome
        - Consider shared victory implications
        - Weigh colony gain vs card rewards
        """
        from ..types import Side

        if not invited_by_offense and not invited_by_defense:
            return None

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        # Estimate hand strengths
        off_strength = self.get_hand_strength(offense)
        def_strength = self.get_hand_strength(defense)

        # Block potential winners
        if off_colonies >= 4 and my_colonies < 4 and invited_by_defense:
            return Side.DEFENSE  # Block their win

        if def_colonies >= 4 and my_colonies < 4 and not invited_by_defense:
            if invited_by_offense:
                return Side.OFFENSE  # Help attack leader

        # Standard decision
        if invited_by_offense and invited_by_defense:
            # Prefer offense (colony opportunity) unless defense looks strong
            if def_strength > off_strength + 0.2:
                return Side.DEFENSE
            return Side.OFFENSE

        if invited_by_offense:
            # Don't help if they're about to win alone
            if off_colonies >= 4 and my_colonies < 4:
                return None
            return Side.OFFENSE

        if invited_by_defense:
            return Side.DEFENSE

        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Usually send 2 ships as ally, but can vary."""
        total_ships = player.total_ships_in_play(game.planets)

        if total_ships > 15:
            return min(3, max_ships)
        elif total_ships > 10:
            return min(2, max_ships)
        else:
            return min(1, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """
        Select best planet based on:
        - Defense ships (prefer fewer)
        - Don't already have colony there
        - Strategic value
        """
        home_planets = [p for p in game.planets if p.owner == defense]
        valid = [p for p in home_planets if not p.has_colony(player.name)]
        if not valid:
            valid = home_planets

        # Score planets
        scored = []
        for planet in valid:
            defender_ships = planet.get_ships(defense.name)
            # Lower defender ships = better
            score = 10 - defender_ships
            scored.append((planet, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[0][0] if scored else home_planets[0]

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """
        Strategic negotiation:
        - Usually make deals (both get colonies)
        - Fail if we're significantly ahead
        - Consider card advantage
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        opp_colonies = opponent.count_foreign_colonies(game.planets)

        # If we're ahead by 2+ colonies, sometimes fail
        if my_colonies >= opp_colonies + 2:
            if self._rng.random() < 0.4:
                return None

        # If they'd win with this deal, sometimes fail
        if opp_colonies == 4 and my_colonies < 4:
            if self._rng.random() < 0.3:
                return None

        # Usually make the deal
        return {"type": "colony_swap", "cards": 0}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Delegate to alien's should_use method."""
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
        - We have good encounter cards
        - Not giving opponent free colonies
        """
        if not player.has_encounter_card():
            return False

        colonies = player.count_foreign_colonies(game.planets)
        hand_strength = self.get_hand_strength(player)

        # At 4 colonies, go for win
        if colonies >= 4:
            return True

        # Good hand - take it
        if hand_strength > 0.5:
            return True

        # Mediocre hand at 3 colonies - still worth it
        if colonies == 3 and hand_strength > 0.3:
            return True

        # Otherwise, be more conservative
        return self._rng.random() < 0.5

    def set_seed(self, seed: int) -> None:
        """Set random seed for reproducibility."""
        self._rng.seed(seed)
