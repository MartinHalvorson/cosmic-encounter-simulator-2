"""
Alliance utility functions for sophisticated AI decision-making.

Provides helper functions for evaluating alliance opportunities,
tracking alliance history, and making power-aware decisions.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


# Powers that benefit significantly from having allies
ALLIANCE_SYNERGY_POWERS = {
    "Symbiote": 0.3,  # Gains cards when allies join
    "Horde": 0.2,  # Allies add to total more
    "Sheriff": 0.2,  # Controls ally actions
    "Diplomat": 0.15,  # Better at ending encounters
    "Philanthropist": 0.15,  # Gives cards but benefits
}

# Powers that are dangerous to ally with (they may backstab or cause problems)
DANGEROUS_ALLY_POWERS = {
    "Traitor": 0.5,  # Can switch sides
    "Saboteur": 0.3,  # Destroys ships of allies
    "Doppelganger": 0.2,  # Copies powers unpredictably
    "Will": 0.2,  # Forces actions
    "Siren": 0.15,  # Lures ships
}

# Powers that provide combat bonuses (valuable allies)
COMBAT_BONUS_POWERS = {
    "Human": 0.3,  # +4 bonus
    "Warrior": 0.25,  # Uses multiple attack cards
    "Virus": 0.25,  # Multiplies ship value
    "Macron": 0.25,  # Ships worth 4 each
    "Tripler": 0.2,  # Triples card value
    "Shadow": 0.2,  # Copies opponent card
    "Doppelganger": 0.15,  # Copies power
}

# Powers that are weak or risky allies
WEAK_ALLY_POWERS = {
    "Masochist": 0.3,  # Wants to lose
    "Loser": 0.25,  # Reverses combat
    "Pacifist": 0.2,  # Forces negotiation
    "Mite": 0.15,  # Takes cards
}


@dataclass
class AllianceHistory:
    """
    Tracks alliance history between players for reciprocity decisions.
    """
    # Maps (inviter, invitee) -> count of invitations
    invitations_sent: Dict[Tuple[str, str], int] = field(default_factory=dict)

    # Maps (invited, side) -> count of acceptances
    invitations_accepted: Dict[Tuple[str, str], int] = field(default_factory=dict)

    # Maps (player1, player2) -> count of times they allied together
    alliance_count: Dict[Tuple[str, str], int] = field(default_factory=dict)

    # Maps (betrayer, victim) -> count of "betrayals" (declining or joining enemy)
    betrayal_count: Dict[Tuple[str, str], int] = field(default_factory=dict)

    def record_invitation(self, inviter: str, invitee: str) -> None:
        """Record that inviter sent an invitation to invitee."""
        key = (inviter, invitee)
        self.invitations_sent[key] = self.invitations_sent.get(key, 0) + 1

    def record_alliance(self, player1: str, player2: str) -> None:
        """Record that two players allied together."""
        # Store in sorted order for consistency
        key = tuple(sorted([player1, player2]))
        self.alliance_count[key] = self.alliance_count.get(key, 0) + 1

    def record_betrayal(self, betrayer: str, victim: str) -> None:
        """Record that betrayer declined invitation or joined enemy side."""
        key = (betrayer, victim)
        self.betrayal_count[key] = self.betrayal_count.get(key, 0) + 1

    def get_relationship_score(self, player1: str, player2: str) -> float:
        """
        Get relationship score between two players.
        Positive = friendly, Negative = hostile.
        """
        key = tuple(sorted([player1, player2]))
        alliances = self.alliance_count.get(key, 0)

        betrayals1 = self.betrayal_count.get((player1, player2), 0)
        betrayals2 = self.betrayal_count.get((player2, player1), 0)
        total_betrayals = betrayals1 + betrayals2

        return (alliances * 0.1) - (total_betrayals * 0.15)


def evaluate_ally_power_synergy(
    main_player_power: Optional[str],
    ally_power: Optional[str]
) -> float:
    """
    Evaluate how well the ally's power synergizes with the main player.

    Returns a score from -0.5 to +0.5
    """
    score = 0.0

    # Check if ally has combat bonus power
    if ally_power in COMBAT_BONUS_POWERS:
        score += COMBAT_BONUS_POWERS[ally_power]

    # Check if ally has alliance synergy power
    if ally_power in ALLIANCE_SYNERGY_POWERS:
        score += ALLIANCE_SYNERGY_POWERS[ally_power] * 0.5

    # Penalty for dangerous allies
    if ally_power in DANGEROUS_ALLY_POWERS:
        score -= DANGEROUS_ALLY_POWERS[ally_power]

    # Penalty for weak allies
    if ally_power in WEAK_ALLY_POWERS:
        score -= WEAK_ALLY_POWERS[ally_power] * 0.5

    # Special cases
    if main_player_power == "Virus" and ally_power == "Macron":
        score += 0.2  # Ships worth 4 each, multiplied by Virus

    if main_player_power == "Human" and ally_power:
        score += 0.05  # Human welcomes any ally for +4

    return max(-0.5, min(0.5, score))


def estimate_win_probability(
    game: "Game",
    as_offense: bool,
    include_allies: bool = True
) -> float:
    """
    Estimate the probability that a side will win the current encounter.

    Args:
        game: Current game state
        as_offense: Whether estimating for offense side
        include_allies: Whether to include ally ships in calculation

    Returns:
        Probability estimate from 0.0 to 1.0
    """
    if not game.offense or not game.defense:
        return 0.5

    # Base probability
    prob = 0.5

    # Ship advantage
    off_ships = sum(game.offense_ships.values()) if hasattr(game, 'offense_ships') else 4
    def_ships = sum(game.defense_ships.values()) if hasattr(game, 'defense_ships') else 4

    if include_allies:
        # Rough ally ship estimate
        off_ships += len(getattr(game, 'offense_allies', [])) * 2
        def_ships += len(getattr(game, 'defense_allies', [])) * 2

    ship_diff = off_ships - def_ships
    prob += ship_diff * 0.025  # Each ship ≈ 2.5% advantage

    # Hand strength (cards available)
    off_hand = len(game.offense.hand) if game.offense else 0
    def_hand = len(game.defense.hand) if game.defense else 0
    hand_diff = off_hand - def_hand
    prob += hand_diff * 0.015

    # Power adjustments
    off_power = game.offense.alien.name if game.offense.alien and game.offense.power_active else None
    def_power = game.defense.alien.name if game.defense.alien and game.defense.power_active else None

    if off_power in COMBAT_BONUS_POWERS:
        prob += COMBAT_BONUS_POWERS[off_power]
    if def_power in COMBAT_BONUS_POWERS:
        prob -= COMBAT_BONUS_POWERS[def_power]

    # Loser power reverses expectations
    if off_power == "Loser":
        prob = 0.65  # Loser usually wins through reversal
    if def_power == "Loser":
        prob = 0.35  # Loser defender is hard to beat

    if as_offense:
        return max(0.1, min(0.9, prob))
    else:
        return max(0.1, min(0.9, 1.0 - prob))


def calculate_offense_ally_value(
    game: "Game",
    potential_ally: "Player",
    my_colonies: int,
    ally_colonies: int
) -> float:
    """
    Calculate the expected value of joining as an offensive ally.

    Returns a score indicating how valuable joining offense would be.
    """
    # Base value: chance of winning * value of colony
    win_prob = estimate_win_probability(game, as_offense=True)

    # Colony is worth more if we need it
    colony_value = 1.0 if my_colonies < 4 else 0.4

    # Diminishing returns if ally is already winning
    if ally_colonies >= 4:
        colony_value *= 0.5  # Shared win less valuable if they could win alone

    base_value = win_prob * colony_value

    # Risk: losing ships to warp
    lose_prob = 1.0 - win_prob
    ship_risk = lose_prob * 0.2  # 2 ships potentially lost

    return base_value - ship_risk


def calculate_defense_ally_value(
    game: "Game",
    potential_ally: "Player",
    defense_colonies: int
) -> float:
    """
    Calculate the expected value of joining as a defensive ally.

    Returns a score indicating how valuable joining defense would be.
    """
    # Base value: chance of winning * value of rewards
    win_prob = estimate_win_probability(game, as_offense=False)

    # Reward value estimation
    ships_in_warp = potential_ally.ships_in_warp if hasattr(potential_ally, 'ships_in_warp') else 0
    hand_size = len(potential_ally.hand) if potential_ally.hand else 0

    # Value of rewards depends on what we need
    if ships_in_warp >= 4:
        reward_value = 0.5  # Getting ships back is valuable
    elif hand_size < 4:
        reward_value = 0.45  # Need cards
    else:
        reward_value = 0.35  # Reward is nice but less critical

    base_value = win_prob * reward_value

    # Risk: losing ships to warp
    lose_prob = 1.0 - win_prob
    ship_risk = lose_prob * 0.2

    # Blocking a leader from winning has value
    if defense_colonies >= 4:
        base_value += 0.15  # Helping defend against a leader

    return base_value - ship_risk


def select_optimal_ally_ships(
    game: "Game",
    player: "Player",
    max_ships: int,
    is_offense_ally: bool
) -> int:
    """
    Select optimal number of ships to commit as an ally.

    Considers:
    - Win probability (commit more if likely to win)
    - Risk tolerance (fewer ships if position is precarious)
    - Colony proximity (more ships if close to winning)
    """
    available = min(max_ships, player.total_ships_in_play(game.planets) if hasattr(player, 'total_ships_in_play') else max_ships)

    if available <= 0:
        return 0

    # Calculate win probability
    win_prob = estimate_win_probability(game, as_offense=is_offense_ally)

    # Base commitment
    if win_prob > 0.7:
        base_ships = 3  # Likely to win, commit more
    elif win_prob > 0.5:
        base_ships = 2  # Even odds
    else:
        base_ships = 1  # Risky, minimize commitment

    # Colony proximity adjustment
    my_colonies = player.count_foreign_colonies(game.planets) if hasattr(player, 'count_foreign_colonies') else 0

    if my_colonies >= 4 and is_offense_ally:
        base_ships = min(4, available)  # Going for win, commit heavily

    # Risk adjustment
    ships_in_warp = player.ships_in_warp if hasattr(player, 'ships_in_warp') else 0
    total_ships = player.total_ships_in_play(game.planets) if hasattr(player, 'total_ships_in_play') else 20

    if ships_in_warp >= 5 or total_ships <= 8:
        base_ships = max(1, base_ships - 1)  # Be conservative

    return min(available, base_ships)


def should_block_leader(
    my_colonies: int,
    leader_colonies: int,
    other_colonies: int,
    invited_to_help_leader: bool
) -> bool:
    """
    Determine if we should prioritize blocking a leader from winning.

    Args:
        my_colonies: Our foreign colony count
        leader_colonies: The potential winner's colony count
        other_colonies: The other main player's colony count
        invited_to_help_leader: Whether we're invited to help the leader

    Returns:
        True if we should actively work against the leader
    """
    # If we're also at 4+ colonies, we can share the win - don't block
    if my_colonies >= 4:
        return False

    # If leader is at 4 and we're not, block them
    if leader_colonies >= 4:
        return True

    # If leader would win outright (4+ with this colony)
    if leader_colonies >= 4 and invited_to_help_leader:
        # Even if we'd share, maybe better to block
        if other_colonies <= 2:
            return True  # Block so game continues

    return False


def get_alliance_recommendation(
    game: "Game",
    player: "Player",
    offense: "Player",
    defense: "Player",
    invited_by_offense: bool,
    invited_by_defense: bool,
    history: Optional[AllianceHistory] = None
) -> Tuple[Optional[str], float]:
    """
    Get a recommendation for alliance decision.

    Returns:
        Tuple of (recommended_side or None, confidence_score)
        where confidence is 0.0 to 1.0
    """
    from ..types import Side

    if not invited_by_offense and not invited_by_defense:
        return (None, 1.0)

    my_colonies = player.count_foreign_colonies(game.planets) if hasattr(player, 'count_foreign_colonies') else 0
    off_colonies = offense.count_foreign_colonies(game.planets) if hasattr(offense, 'count_foreign_colonies') else 0
    def_colonies = defense.count_foreign_colonies(game.planets) if hasattr(defense, 'count_foreign_colonies') else 0

    # Check for leader blocking
    if invited_by_defense and should_block_leader(my_colonies, off_colonies, def_colonies, invited_by_offense):
        return ("defense", 0.9)

    if invited_by_offense and should_block_leader(my_colonies, def_colonies, off_colonies, invited_by_defense):
        return ("offense", 0.9)

    # Calculate values for each side
    off_value = 0.0
    def_value = 0.0

    if invited_by_offense:
        off_value = calculate_offense_ally_value(game, player, my_colonies, off_colonies)

        # Power synergy
        off_power = offense.alien.name if offense.alien and offense.power_active else None
        my_power = player.alien.name if player.alien and player.power_active else None
        off_value += evaluate_ally_power_synergy(off_power, my_power) * 0.5

        # Historical relationship
        if history:
            off_value += history.get_relationship_score(player.name, offense.name) * 0.3

    if invited_by_defense:
        def_value = calculate_defense_ally_value(game, player, def_colonies)

        # Power synergy
        def_power = defense.alien.name if defense.alien and defense.power_active else None
        my_power = player.alien.name if player.alien and player.power_active else None
        def_value += evaluate_ally_power_synergy(def_power, my_power) * 0.5

        # Historical relationship
        if history:
            def_value += history.get_relationship_score(player.name, defense.name) * 0.3

    # Make decision
    if off_value > def_value and off_value > 0.15:
        confidence = min(1.0, (off_value - def_value) * 2 + 0.5)
        return ("offense", confidence)
    elif def_value > 0.1:
        confidence = min(1.0, (def_value - off_value) * 2 + 0.5)
        return ("defense", confidence)
    else:
        return (None, 0.6)
