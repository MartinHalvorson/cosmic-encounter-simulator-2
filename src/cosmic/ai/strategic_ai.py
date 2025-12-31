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


# Powers that are dangerous to let win - tend to snowball or have strong late game
DANGEROUS_POWERS = {
    "Machine", "Virus", "Void", "Parasite", "Loser", "Masochist",
    "Zombie", "Oracle", "Tick-Tock", "Chosen", "Chronos", "Clone",
    "Symbiote", "Horde", "Reincarnator", "Fury", "Genius", "Will"
}

# Powers that synergize well with negotiation
NEGOTIATE_FRIENDLY_POWERS = {
    "Pacifist", "Diplomat", "Trader", "Philanthropist", "Empath",
    "Negotiator", "Altruist", "Butler", "Connoisseur"
}

# Powers that benefit from high attack cards
HIGH_CARD_POWERS = {
    "Human", "Warrior", "Calculator", "Grudge", "Shadow",
    "Tripler", "Ace", "Battlemaster", "Captain", "Brute"
}

# Powers that benefit from low cards
LOW_CARD_POWERS = {
    "Loser", "Anti-Matter", "Underdog", "Masochist", "Deuce"
}

# Combat modifier powers - change how combat math works
COMBAT_MODIFIER_POWERS = {
    "Virus": "multiply_ships",       # Multiplies ship count instead of adding
    "Macron": "ships_as_4",          # Each ship counts as 4
    "Human": "add_4",                # Adds +4 to total
    "Tripler": "triple_card",        # Can triple encounter card
    "Anti-Matter": "reverse_total",  # Lower total wins
    "Loser": "loser_wins",           # Lower total wins (different mechanics)
    "Calculator": "use_hand_size",   # Uses hand size as card value
    "Mirror": "mirror_digits",       # Can reverse digits on attack card
}

# Powers that affect alliance decisions
ALLIANCE_AFFECTING_POWERS = {
    "Parasite": "forces_alliance",   # Joins encounters uninvited
    "Philanthropist": "gives_cards", # Gives cards to allies
    "Empath": "emotional_ally",      # Benefits from peaceful alliances
    "Hate": "enemy_alliances",       # Draws enemies into alliances
    "Observer": "watches_all",       # Can observe any encounter
    "Barbarian": "steals_ships",     # Takes ships from allies
}

# Powers that manipulate ships
SHIP_POWERS = {
    "Zombie", "Healer", "Phantom", "Horde", "Symbiote",
    "Warpish", "Vessel", "Cavalry", "Reincarnator", "Kamikaze"
}

# Powers that manipulate cards/hands
CARD_MANIPULATION_POWERS = {
    "Oracle", "Sorcerer", "Trader", "Gambler", "Clone", "Magician",
    "Pickpocket", "Thief", "Daredevil", "Sneak", "Bandit", "Collector"
}

# Powers that alter win conditions or game flow
GAME_FLOW_POWERS = {
    "Machine", "Chronos", "Tick-Tock", "Will", "Chosen",
    "Schizoid", "Visionary", "Prophet", "Seeker"
}

# Powers that work well as defensive allies
GOOD_DEFENSIVE_ALLY_POWERS = {
    "Zombie", "Warrior", "Human", "Macron", "Virus",
    "Symbiote", "Horde", "Cavalry"
}

# Powers weak to certain strategies
VULNERABLE_POWERS = {
    "Calculator": ["low_hand_size"],  # Weak when hand is small
    "Virus": ["high_ship_count"],     # Need to avoid high ship commitment vs them
    "Macron": ["high_ship_count"],    # Each of their ships = 4
    "Clone": ["card_zap"],            # Clone's advantage is reusing cards
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

        if alien_name == "Warrior":
            # Warrior gets bonus from ship count - play high cards with ship advantage
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        if alien_name == "Deuce":
            # Deuce benefits from playing 2s - look for low cards
            if attack_cards:
                twos = [c for c in attack_cards if c.value == 2]
                if twos:
                    return twos[0]
                return min(attack_cards, key=lambda c: c.value)

        if alien_name == "Ace":
            # Ace benefits from playing 1s or high cards
            if attack_cards:
                ones = [c for c in attack_cards if c.value == 1]
                if ones:
                    return ones[0]
                return max(attack_cards, key=lambda c: c.value)

        if alien_name == "Diplomat" and negotiate_cards:
            # Diplomat can redirect encounters after negotiate
            if self._rng.random() < 0.5:
                return negotiate_cards[0]

        if alien_name == "Masochist":
            # Masochist wants to lose - play lowest card
            if attack_cards:
                return min(attack_cards, key=lambda c: c.value)

        if alien_name == "Underdog":
            # Underdog gets bonus when behind - conserve high cards
            if attack_cards and len(attack_cards) > 1:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value)
                return sorted_attacks[len(sorted_attacks) // 2]

        if alien_name == "Cavalry":
            # Cavalry can add ships after reveal - mid-range cards work well
            if attack_cards and len(attack_cards) > 1:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value)
                return sorted_attacks[len(sorted_attacks) // 2]

        if alien_name == "Battlemaster":
            # Battlemaster excels in combat - play aggressive
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        if alien_name == "Sneak":
            # Sneak can steal cards - conserve high cards for when needed
            if attack_cards and len(attack_cards) > 2:
                sorted_attacks = sorted(attack_cards, key=lambda c: c.value)
                return sorted_attacks[1]  # Second lowest

        if alien_name == "Brute":
            # Brute uses force - high cards always
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

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
            "expect_high_card": False,
            "minimize_ships": False,      # Reduce ship commitment
            "maximize_ships": False,      # Increase ship commitment
            "expect_card_swap": False,    # Opponent might swap cards
            "power_can_zap": False,       # Consider zapping their power
        }

        if not opp_alien:
            return modifier

        # Low card powers
        if opp_alien == "Loser":
            modifier["expect_low_card"] = True
            modifier["play_defensive"] = True  # Low card often beats us

        if opp_alien == "Anti-Matter":
            modifier["expect_low_card"] = True

        if opp_alien == "Masochist":
            modifier["expect_low_card"] = True
            modifier["play_defensive"] = True

        if opp_alien == "Deuce":
            modifier["expect_low_card"] = True

        # High card/combat powers
        if opp_alien in {"Virus", "Macron", "Human"}:
            modifier["play_aggressive"] = True  # Need high cards

        if opp_alien == "Warrior":
            modifier["play_aggressive"] = True
            modifier["minimize_ships"] = True  # Their power scales with our ships

        if opp_alien == "Tripler":
            modifier["play_aggressive"] = True
            modifier["expect_high_card"] = True

        if opp_alien == "Brute":
            modifier["play_aggressive"] = True

        if opp_alien == "Battlemaster":
            modifier["play_aggressive"] = True

        # Card swap/manipulation powers
        if opp_alien == "Sorcerer":
            # They'll swap if they're losing - play mid cards
            modifier["play_defensive"] = True
            modifier["expect_card_swap"] = True

        if opp_alien == "Gambler":
            modifier["expect_card_swap"] = True

        if opp_alien == "Oracle":
            # They see our card first - be unpredictable
            modifier["play_defensive"] = True

        if opp_alien == "Clone":
            # They can replay cards - expect high cards repeatedly
            modifier["expect_high_card"] = True
            modifier["power_can_zap"] = True

        # Negotiation powers
        if opp_alien in NEGOTIATE_FRIENDLY_POWERS:
            modifier["avoid_negotiate"] = True  # They benefit from deals

        # Ship manipulation powers
        if opp_alien in {"Cavalry", "Horde", "Symbiote"}:
            modifier["minimize_ships"] = True  # They can add more ships

        if opp_alien == "Zombie":
            modifier["play_aggressive"] = True  # Their ships don't stay dead
            modifier["power_can_zap"] = True

        # Dangerous game-flow powers worth zapping
        if opp_alien in {"Machine", "Parasite", "Void"}:
            modifier["power_can_zap"] = True

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
        - Opponent's power and combat modifiers
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        total_ships = player.total_ships_in_play(game.planets)
        hand_strength = self.get_hand_strength(player)

        # Determine if we're offense or defense and get opponent
        is_offense = (game.offense == player)
        opponent = game.defense if is_offense else game.offense
        opp_alien = opponent.alien.name if opponent.alien and opponent.power_active else None

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

        # Power-based ship adjustments
        if opp_alien:
            # Against Virus - our ships become their multiplier, minimize commitment
            if opp_alien == "Virus":
                base = max(1, base - 2)

            # Against Macron - each of their ships = 4, need more ships ourselves
            elif opp_alien == "Macron":
                base = min(max_ships, base + 1)

            # Against Warrior - they benefit from our ship count
            elif opp_alien == "Warrior":
                base = max(1, base - 1)

            # Against powers that add ships (Cavalry, Symbiote) - commit more upfront
            elif opp_alien in {"Cavalry", "Symbiote", "Horde"}:
                base = min(max_ships, base + 1)

        # Player's own power adjustments
        my_alien = player.alien.name if player.alien and player.power_active else None
        if my_alien:
            # Virus - more ships = higher multiplier
            if my_alien == "Virus":
                base = min(max_ships, base + 2)

            # Macron - fewer ships needed (each = 4)
            elif my_alien == "Macron":
                base = max(1, base - 2)

            # Zombie - ships are cheap (come back from warp)
            elif my_alien == "Zombie":
                base = min(max_ships, base + 1)

            # Symbiote - has double ships, can commit more
            elif my_alien == "Symbiote":
                base = min(max_ships, base + 1)

        return min(base, max_ships)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Strategic invitations considering:
        - Colony counts and win proximity
        - Alien power synergies/dangers
        - Ship availability of potential allies
        """
        my_colonies = player.count_foreign_colonies(game.planets)
        invited = []

        for ally in potential_allies:
            ally_colonies = ally.count_foreign_colonies(game.planets)
            ally_power = ally.alien.name if ally.alien and ally.power_active else None

            # Never invite someone about to win (unless we're also winning)
            if ally_colonies >= 4 and my_colonies < 4:
                continue

            # Avoid inviting dangerous powers that get stronger with allies
            if ally_power == "Parasite":
                # Parasite allies without invitation, don't need to invite
                continue

            # Prefer allies with useful powers
            priority = 0
            if ally_power in {"Human", "Warrior", "Shadow"}:
                priority += 1  # Combat boost powers help
            if ally_power == "Zombie":
                priority += 1  # Zombie doesn't lose ships permanently

            # Strategic considerations based on colonies
            if my_colonies == 4:
                # Only invite if they can't win with us
                if ally_colonies <= 2 or priority > 0:
                    invited.append((ally, priority))
            elif my_colonies == 3:
                # Be somewhat selective
                if ally_colonies <= 3:
                    invited.append((ally, priority))
            else:
                # Earlier game - invite most players
                if ally_colonies <= my_colonies + 1:
                    invited.append((ally, priority))

        # Sort by priority (higher is better) and return just the players
        invited.sort(key=lambda x: x[1], reverse=True)
        return [ally for ally, _ in invited]

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
        Sophisticated alliance decisions considering:
        - Win probability modeling
        - Shared victory implications
        - Power danger assessment
        - Risk/reward of colony vs cards
        """
        from ..types import Side

        if not invited_by_offense and not invited_by_defense:
            return None

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        # Get power information
        off_power = offense.alien.name if offense.alien and offense.power_active else None
        def_power = defense.alien.name if defense.alien and defense.power_active else None

        # Estimate hand strengths and win probability
        off_strength = self.get_hand_strength(offense)
        def_strength = self.get_hand_strength(defense)

        # Power-based adjustments
        if off_power in {"Virus", "Macron", "Human"}:
            off_strength += 0.15  # Combat bonus powers
        if def_power in {"Virus", "Macron", "Human"}:
            def_strength += 0.15
        if off_power == "Loser":
            off_strength += 0.2  # Loser is tricky to beat
        if def_power == "Loser":
            def_strength += 0.2

        # Block potential winners - highest priority
        if off_colonies >= 4 and my_colonies < 4 and invited_by_defense:
            return Side.DEFENSE  # Block their win

        if def_colonies >= 4 and my_colonies < 4 and invited_by_offense:
            return Side.OFFENSE  # Help attack leader on defense

        # Avoid helping dangerous powers near victory
        if off_power in DANGEROUS_POWERS and off_colonies >= 3:
            if invited_by_defense:
                return Side.DEFENSE
            return None  # Don't help dangerous power

        # Standard decision
        if invited_by_offense and invited_by_defense:
            # Weight factors
            off_win_chance = 0.5 + (off_strength - def_strength) * 0.3
            off_win_chance = max(0.2, min(0.8, off_win_chance))

            # Colony opportunity vs card reward
            if off_win_chance > 0.6:
                return Side.OFFENSE
            elif off_win_chance < 0.4:
                return Side.DEFENSE
            else:
                # Close call - prefer offense for colony if we need it
                return Side.OFFENSE if my_colonies < 3 else Side.DEFENSE

        if invited_by_offense:
            # Don't help if they're about to win alone
            if off_colonies >= 4 and my_colonies < 4:
                return None
            # Accept if we need colonies or they're likely to win
            if my_colonies < 3 or off_strength > 0.5:
                return Side.OFFENSE
            return Side.OFFENSE

        if invited_by_defense:
            # Defensive alliance - guaranteed cards if we win
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

    def reset_tracking(self) -> None:
        """Reset opponent tracking for a new game."""
        self._opponent_aggression.clear()
        self._high_cards_seen = 0
        self._cards_seen_total = 0

    def observe_card_play(self, card: "Card", player_name: str) -> None:
        """Track cards played for card counting."""
        self._cards_seen_total += 1
        if hasattr(card, 'value') and card.value >= 15:
            self._high_cards_seen += 1

    def get_high_card_probability(self) -> float:
        """Estimate probability of opponent having high cards."""
        # Base probability from deck composition
        # ~10 cards are 15+ in standard deck of ~72 encounter cards
        base_prob = 10 / 72

        if self._cards_seen_total == 0:
            return base_prob

        # Adjust based on what we've seen
        high_cards_remaining = max(0, 10 - self._high_cards_seen)
        total_remaining = max(1, 72 - self._cards_seen_total)
        return high_cards_remaining / total_remaining

    def estimate_win_probability(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> float:
        """
        Estimate probability of winning current encounter.
        Returns value from 0.0 to 1.0.
        """
        opponent = game.defense if is_offense else game.offense

        # Base from hand strength
        my_strength = self.get_hand_strength(player)
        opp_strength = self.get_hand_strength(opponent)

        # Ship advantage
        if is_offense:
            my_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4
            opp_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
        else:
            my_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4
            opp_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4

        ship_diff = (my_ships - opp_ships) / 8  # Normalize

        # Power adjustments
        my_power = player.alien.name if player.alien and player.power_active else None
        opp_power = opponent.alien.name if opponent.alien and opponent.power_active else None

        power_mod = 0.0
        if my_power in {"Virus", "Macron", "Human"}:
            power_mod += 0.1
        if opp_power in {"Virus", "Macron", "Human"}:
            power_mod -= 0.1
        if my_power == "Loser":
            power_mod += 0.15
        if opp_power == "Loser":
            power_mod -= 0.15

        # Combine factors
        win_prob = 0.5 + (my_strength - opp_strength) * 0.3 + ship_diff * 0.1 + power_mod
        return max(0.1, min(0.9, win_prob))

    def should_play_flare(
        self,
        game: "Game",
        player: "Player",
        flare_card: "Card",
        phase: str
    ) -> bool:
        """Decide whether to play a flare card."""
        from ..cards.base import FlareCard

        if not isinstance(flare_card, FlareCard):
            return False

        my_colonies = player.count_foreign_colonies(game.planets)
        alien_name = flare_card.alien_name

        # Check if we can use Super (matching alien)
        can_use_super = (
            player.alien and
            player.alien.name == alien_name and
            player.power_active
        )

        # More willing to use Super effects
        if can_use_super:
            # Use Super flare if close to winning or in trouble
            if my_colonies >= 3:
                return True
            if player.ships_in_warp >= 5:
                return True
            return self._rng.random() < 0.4

        # Wild flares - use strategically
        # Combat flares during reveal phase
        if phase == "reveal":
            if alien_name in {"Human", "Warrior", "Macron", "Virus"}:
                return self.get_hand_strength(player) < 0.5

        # Defensive flares when defending
        if phase == "defense":
            if alien_name in {"Zombie", "Phantom", "Healer"}:
                return player.ships_in_warp >= 3

        # Generally conservative with wild flares
        return self._rng.random() < 0.2

    def get_game_urgency(self, game: "Game", player: "Player") -> float:
        """
        Calculate how urgently player needs to act.
        Returns 0.0 (no rush) to 1.0 (desperate/critical).
        """
        my_colonies = player.count_foreign_colonies(game.planets)

        # Check if any opponent is close to winning
        max_opp_colonies = 0
        for p in game.players:
            if p != player:
                colonies = p.count_foreign_colonies(game.planets)
                max_opp_colonies = max(max_opp_colonies, colonies)

        # Urgency factors
        urgency = 0.0

        # We're close to winning
        if my_colonies >= 4:
            urgency += 0.4

        # Opponent is close to winning
        if max_opp_colonies >= 4:
            urgency += 0.5
        elif max_opp_colonies >= 3:
            urgency += 0.2

        # We're far behind
        if max_opp_colonies - my_colonies >= 2:
            urgency += 0.3

        # Low on ships
        if player.ships_in_warp >= 10:
            urgency += 0.2

        return min(1.0, urgency)
