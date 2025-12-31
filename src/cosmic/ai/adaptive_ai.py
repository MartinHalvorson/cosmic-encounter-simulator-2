"""
Adaptive AI - Learns and adapts during the game.

This AI extends Strategic AI with:
- Alliance memory (tracks who helped/hurt you)
- Game phase awareness (early/mid/late game strategies)
- Opponent behavior modeling
- Dynamic risk tolerance
- Multi-game learning
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple, Set, TYPE_CHECKING

from .strategic_ai import StrategicAI, DANGEROUS_POWERS

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player
    from ..planet import Planet
    from ..cards.base import EncounterCard, AttackCard
    from ..types import Side


@dataclass
class AllianceMemory:
    """Track alliance history with other players."""
    # Times they helped us (allied offensive wins, defensive saves)
    times_helped: int = 0
    # Times they hurt us (declined alliance when needed, attacked us)
    times_hurt: int = 0
    # Times they allied with our opponents
    times_opposed: int = 0
    # Shared victories
    shared_wins: int = 0

    @property
    def trust_score(self) -> float:
        """Calculate trust score from -1 (enemy) to 1 (friend)."""
        total = self.times_helped + self.times_hurt + self.times_opposed + 1
        positive = self.times_helped + self.shared_wins * 2
        negative = self.times_hurt + self.times_opposed
        return (positive - negative) / total


@dataclass
class LearningAI(StrategicAI):
    """
    Advanced AI that adapts its strategy based on game context
    and learns from player interactions throughout the game.

    This AI maintains memory across encounters and games:
    - Alliance memory: tracks helpful/hostile players
    - Game phase awareness: different strategies for early/mid/late
    - Dynamic risk tolerance: adjusts based on position
    """
    name: str = field(default="LearningAI", init=False)

    # Alliance memory - track relationships with other players
    _alliance_memory: Dict[str, AllianceMemory] = field(default_factory=dict)

    # Track current game phase (early=0-3 turns, mid=4-15, late=16+)
    _game_phase: str = "early"

    # Dynamic risk tolerance (0.0 = conservative, 1.0 = aggressive)
    _risk_tolerance: float = 0.5

    # Track our previous decisions for consistency
    _recent_decisions: List[str] = field(default_factory=list)

    # Track successful strategies
    _successful_strategies: Dict[str, int] = field(default_factory=dict)
    _failed_strategies: Dict[str, int] = field(default_factory=dict)

    def _update_game_phase(self, game: "Game") -> None:
        """Update game phase based on turn count and colony distribution."""
        turn = game.current_turn

        # Check if anyone is close to winning
        max_colonies = max(
            p.count_foreign_colonies(game.planets)
            for p in game.players
        )

        if turn <= 3 or max_colonies <= 1:
            self._game_phase = "early"
        elif turn > 15 or max_colonies >= 4:
            self._game_phase = "late"
        else:
            self._game_phase = "mid"

    def _update_risk_tolerance(self, game: "Game", player: "Player") -> None:
        """Dynamically adjust risk tolerance based on game state."""
        my_colonies = player.count_foreign_colonies(game.planets)
        my_ships = player.total_ships_in_play(game.planets)
        hand_strength = self.get_hand_strength(player)

        # Start with baseline
        risk = 0.5

        # Adjust based on position
        max_opp_colonies = max(
            p.count_foreign_colonies(game.planets)
            for p in game.players if p != player
        )

        # Behind? Take more risks
        if my_colonies < max_opp_colonies - 1:
            risk += 0.2

        # Ahead? Be conservative
        if my_colonies > max_opp_colonies + 1:
            risk -= 0.2

        # Close to winning? Take calculated risks
        if my_colonies >= 4:
            risk += 0.1

        # Low on resources? Be cautious
        if my_ships < 5:
            risk -= 0.2
        if hand_strength < 0.3:
            risk -= 0.1

        # Late game? More aggressive
        if self._game_phase == "late":
            risk += 0.15

        self._risk_tolerance = max(0.1, min(0.9, risk))

    def _get_alliance_memory(self, player_name: str) -> AllianceMemory:
        """Get or create alliance memory for a player."""
        if player_name not in self._alliance_memory:
            self._alliance_memory[player_name] = AllianceMemory()
        return self._alliance_memory[player_name]

    def _record_alliance_help(self, player_name: str) -> None:
        """Record that a player helped us."""
        memory = self._get_alliance_memory(player_name)
        memory.times_helped += 1

    def _record_alliance_opposition(self, player_name: str) -> None:
        """Record that a player opposed us."""
        memory = self._get_alliance_memory(player_name)
        memory.times_opposed += 1

    def _record_alliance_hurt(self, player_name: str) -> None:
        """Record that a player hurt us."""
        memory = self._get_alliance_memory(player_name)
        memory.times_hurt += 1

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Adaptive card selection that considers:
        - Game phase (conservative early, aggressive late)
        - Risk tolerance
        - Alliance memory with opponent
        """
        # Update context
        self._update_game_phase(game)
        self._update_risk_tolerance(game, player)

        cards = player.get_encounter_cards()
        if not cards:
            raise ValueError(f"{player.name} has no encounter cards!")

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        opponent = game.defense if is_offense else game.offense
        opp_name = opponent.name

        # Check alliance history with this opponent
        trust = self._get_alliance_memory(opp_name).trust_score

        # Base card selection from parent class
        base_card = super().select_encounter_card(game, player, is_offense)

        # Early game: Be more conservative, save high cards
        if self._game_phase == "early" and attack_cards and len(attack_cards) > 2:
            sorted_attacks = sorted(attack_cards, key=lambda c: c.value, reverse=True)
            # Play 3rd or 4th highest
            idx = min(3, len(sorted_attacks) - 1)
            if self._risk_tolerance < 0.4:
                return sorted_attacks[idx]

        # Consider negotiation based on trust
        if negotiate_cards and trust > 0.3 and not is_offense:
            # We trust this opponent, negotiate might work
            if self._rng.random() < 0.3 + trust * 0.2:
                return negotiate_cards[0]

        # Low trust? Don't negotiate with enemies
        if trust < -0.3 and negotiate_cards and base_card in negotiate_cards:
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        # Late game: Go for wins
        if self._game_phase == "late" and attack_cards:
            my_colonies = player.count_foreign_colonies(game.planets)
            if my_colonies >= 3:
                return max(attack_cards, key=lambda c: c.value)

        return base_card

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """
        Adaptive ship selection based on game phase and risk.
        """
        self._update_game_phase(game)
        self._update_risk_tolerance(game, player)

        base_ships = super().select_ships_for_encounter(game, player, max_ships)

        # Early game: Preserve ships
        if self._game_phase == "early":
            return min(base_ships, max(1, int(max_ships * 0.6)))

        # High risk tolerance: Commit more
        if self._risk_tolerance > 0.7:
            return min(max_ships, base_ships + 1)

        # Low risk tolerance: Commit fewer
        if self._risk_tolerance < 0.3:
            return max(1, base_ships - 1)

        return base_ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """
        Alliance invitations based on trust and game phase.
        """
        self._update_game_phase(game)
        my_colonies = player.count_foreign_colonies(game.planets)
        invited = []

        for ally in potential_allies:
            trust = self._get_alliance_memory(ally.name).trust_score
            ally_colonies = ally.count_foreign_colonies(game.planets)
            ally_power = ally.alien.name if ally.alien and ally.power_active else None

            # Never invite someone about to win (unless we're also winning)
            if ally_colonies >= 4 and my_colonies < 4:
                continue

            # Calculate invitation score
            score = 0.0

            # Trust affects invitation
            score += trust * 0.3

            # Colony balance matters
            if ally_colonies <= my_colonies:
                score += 0.2
            elif ally_colonies > my_colonies + 1:
                score -= 0.3

            # Useful powers get bonus
            if ally_power in {"Human", "Warrior", "Zombie", "Shadow"}:
                score += 0.2

            # Dangerous powers get penalty
            if ally_power in DANGEROUS_POWERS and ally_colonies >= 3:
                score -= 0.3

            # Game phase affects selectivity
            if self._game_phase == "early":
                # More generous early
                score += 0.1
            elif self._game_phase == "late":
                # Very selective late
                if my_colonies >= 4:
                    score -= 0.2  # Don't help others win with us

            # Make decision based on score
            threshold = 0.3 - self._risk_tolerance * 0.2
            if score > threshold:
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
        Alliance response based on trust and strategic position.
        """
        from ..types import Side

        if not invited_by_offense and not invited_by_defense:
            return None

        self._update_game_phase(game)
        self._update_risk_tolerance(game, player)

        my_colonies = player.count_foreign_colonies(game.planets)
        off_colonies = offense.count_foreign_colonies(game.planets)
        def_colonies = defense.count_foreign_colonies(game.planets)

        off_trust = self._get_alliance_memory(offense.name).trust_score
        def_trust = self._get_alliance_memory(defense.name).trust_score

        # Block players about to win (unless we'd also win)
        if off_colonies >= 4 and my_colonies < 4 and invited_by_defense:
            self._record_alliance_help(defense.name)
            return Side.DEFENSE

        if def_colonies >= 4 and my_colonies < 4 and invited_by_offense:
            self._record_alliance_help(offense.name)
            return Side.OFFENSE

        # Trust-weighted decision
        if invited_by_offense and invited_by_defense:
            off_score = 0.5 + off_trust * 0.2
            def_score = 0.5 + def_trust * 0.2

            # Offense gives colony opportunity
            if my_colonies < 3:
                off_score += 0.2

            # Defense gives cards
            if len(player.hand) < 4:
                def_score += 0.15

            # Game phase matters
            if self._game_phase == "late" and my_colonies >= 3:
                off_score += 0.15  # Go for colonies late

            if off_score > def_score:
                self._record_alliance_help(offense.name)
                self._record_alliance_opposition(defense.name)
                return Side.OFFENSE
            else:
                self._record_alliance_help(defense.name)
                self._record_alliance_opposition(offense.name)
                return Side.DEFENSE

        if invited_by_offense:
            # Don't help untrusted players near victory
            if off_trust < -0.2 and off_colonies >= 3:
                return None
            self._record_alliance_help(offense.name)
            return Side.OFFENSE

        if invited_by_defense:
            if def_trust < -0.2 and def_colonies >= 3:
                return None
            self._record_alliance_help(defense.name)
            return Side.DEFENSE

        return None

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """
        Strategic planet selection considering:
        - Defender strength
        - Our existing colonies
        - Strategic value
        """
        home_planets = [p for p in game.planets if p.owner == defense]
        if not home_planets:
            return super().select_attack_planet(game, player, defense)

        valid = [p for p in home_planets if not p.has_colony(player.name)]
        if not valid:
            valid = home_planets

        # Score planets
        scored = []
        for planet in valid:
            score = 0.0

            # Prefer fewer defender ships
            defender_ships = planet.get_ships(defense.name)
            score += (8 - defender_ships) * 0.5

            # Prefer planets with fewer other player colonies
            other_colonies = sum(
                1 for p in game.players
                if p != player and p != defense and planet.has_colony(p.name)
            )
            score -= other_colonies * 0.3

            # Consider space stations
            if hasattr(planet, 'space_station') and planet.space_station:
                score += 0.5  # Capturing stations is valuable

            scored.append((planet, score))

        # Add randomness based on risk tolerance
        if scored:
            if self._risk_tolerance > 0.6:
                # Risk taker: might attack harder target
                weights = [max(0.1, s + self._rng.random()) for _, s in scored]
            else:
                # Conservative: prefer best option
                weights = [max(0.1, s) for _, s in scored]

            # Weighted selection
            total = sum(weights)
            r = self._rng.random() * total
            cumulative = 0
            for (planet, _), weight in zip(scored, weights):
                cumulative += weight
                if r <= cumulative:
                    return planet

        return scored[0][0] if scored else home_planets[0]

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """
        Trust-aware negotiation.
        """
        trust = self._get_alliance_memory(opponent.name).trust_score
        base_deal = super().negotiate_deal(game, player, opponent)

        # Low trust? More likely to fail deals
        if trust < -0.3 and self._rng.random() < 0.4:
            self._record_alliance_hurt(opponent.name)
            return None

        # High trust? More likely to succeed
        if trust > 0.3 and base_deal is None:
            if self._rng.random() < 0.3:
                return {"type": "colony_swap", "cards": 0}

        if base_deal:
            self._record_alliance_help(opponent.name)
        else:
            self._record_alliance_hurt(opponent.name)

        return base_deal

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """
        Consider game phase and risk when deciding on second encounter.
        """
        if not player.has_encounter_card():
            return False

        self._update_game_phase(game)
        self._update_risk_tolerance(game, player)

        colonies = player.count_foreign_colonies(game.planets)
        hand_strength = self.get_hand_strength(player)

        # Going for win? Always yes
        if colonies >= 4:
            return True

        # Late game with decent position? Yes
        if self._game_phase == "late" and colonies >= 3 and hand_strength > 0.4:
            return True

        # Risk-adjusted decision
        threshold = 0.4 + (1 - self._risk_tolerance) * 0.3
        return hand_strength > threshold

    def reset_tracking(self) -> None:
        """Reset all tracking for a new game."""
        super().reset_tracking()
        # Don't reset alliance memory between games (it persists)
        self._game_phase = "early"
        self._risk_tolerance = 0.5
        self._recent_decisions.clear()

    def reset_alliance_memory(self) -> None:
        """Reset alliance memory (use between game series)."""
        self._alliance_memory.clear()

    def get_trust_level(self, player_name: str) -> float:
        """Get current trust level with a player."""
        return self._get_alliance_memory(player_name).trust_score
