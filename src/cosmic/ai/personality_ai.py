"""
Personality-based AI strategies for Cosmic Encounter.

These AIs have distinct playstyles that affect their decision-making:
- AggressiveAI: Commits maximum ships, plays highest cards, rarely negotiates
- CautiousAI: Conserves resources, negotiates more, avoids risky encounters
- OpportunisticAI: Allies frequently, targets weak players
- SocialAI: Focuses on alliances and deals over combat
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
class AggressiveAI(AIStrategy):
    """
    Aggressive AI that maximizes combat power.

    Traits:
    - Always commits maximum ships
    - Plays highest attack cards
    - Rarely negotiates (only when forced)
    - Takes second encounters whenever possible
    - Invites few allies (wants glory alone)
    """
    name: str = field(default="AggressiveAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Always play highest attack card."""
        attack_cards = player.get_attack_cards()
        if attack_cards:
            return max(attack_cards, key=lambda c: c.value)

        # Forced to use other cards
        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Always commit maximum ships."""
        return max_ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Rarely invite allies - want to win alone."""
        # Only invite if we're likely to lose
        hand_strength = self.get_hand_strength(player)
        if hand_strength < 0.3:
            # Invite one ally if desperate
            if potential_allies:
                return [self._rng.choice(potential_allies)]
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Accept offense side for chance to gain colonies."""
        from ..types import Side
        if invited_by_offense:
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit maximum ships as ally too."""
        return max_ships

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack planet with most ships (challenge strongest)."""
        planets = defense.home_planets
        if not planets:
            return None

        return max(
            planets,
            key=lambda p: p.get_ships(defense.name)
        )

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Rarely accept deals - prefer to fight."""
        # Only deal if it's very favorable
        return None

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power if it helps combat."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Always take second encounter if possible."""
        cards = player.get_encounter_cards()
        return len(cards) > 0


@dataclass
class CautiousAI(AIStrategy):
    """
    Cautious AI that conserves resources.

    Traits:
    - Commits minimal ships when possible
    - Saves best cards for important encounters
    - Negotiates when appropriate
    - Avoids risky second encounters
    - Seeks alliances for protection
    """
    name: str = field(default="CautiousAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """
        Play conservatively - don't waste best cards.
        Use negotiate more often.
        """
        cards = player.get_encounter_cards()
        if not cards:
            return None

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        # Consider negotiating more often
        if negotiate_cards:
            hand_strength = self.get_hand_strength(player)
            if hand_strength < 0.4 or (not is_offense and hand_strength < 0.6):
                return negotiate_cards[0]

        if attack_cards:
            # Play 4th or 5th best card - save the good ones
            sorted_cards = sorted(attack_cards, key=lambda c: c.value, reverse=True)
            index = min(3, len(sorted_cards) - 1)
            return sorted_cards[index]

        return cards[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit minimal ships to preserve resources."""
        if max_ships <= 1:
            return max_ships

        # Only commit 1-2 ships usually
        hand_strength = self.get_hand_strength(player)
        if hand_strength > 0.6:
            return 1  # Good hand, don't need many ships
        elif hand_strength > 0.3:
            return 2
        else:
            return 3  # Weak hand, need ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite allies for safety."""
        # Invite up to 2 allies
        count = min(2, len(potential_allies))
        if count > 0:
            return self._rng.sample(potential_allies, count)
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Prefer defense side (less risk, still get rewards)."""
        from ..types import Side
        if invited_by_defense:
            return Side.DEFENSE
        if invited_by_offense:
            # Only join offense if likely to win
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit minimal ships as ally."""
        return 1

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack planet with fewest enemy ships."""
        planets = defense.home_planets
        if not planets:
            return None

        return min(
            planets,
            key=lambda p: p.get_ships(defense.name)
        )

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Accept deals when possible."""
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power only when beneficial and not risky."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Only take second encounter if hand is still strong."""
        cards = player.get_encounter_cards()
        if len(cards) < 3:
            return False
        return self.get_hand_strength(player) > 0.5


@dataclass
class OpportunisticAI(AIStrategy):
    """
    Opportunistic AI that exploits weaknesses.

    Traits:
    - Targets weak players
    - Allies with winning side
    - Adapts card play to situation
    - Takes calculated risks
    """
    name: str = field(default="OpportunisticAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Play just enough to win."""
        cards = player.get_encounter_cards()
        if not cards:
            return None

        attack_cards = player.get_attack_cards()

        if is_offense:
            # Estimate defense strength
            defense_ships = len(game.defense_ships) if game.defense_ships else 4
            # Play card just strong enough to probably win
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                for card in sorted_cards:
                    if card.value + 4 > defense_ships + 10:
                        return card
                return sorted_cards[-1]  # Play highest if none sufficient
        else:
            # Defense: check if worth fighting
            offense_colonies = game.offense.count_foreign_colonies(game.planets)
            if offense_colonies >= 4:
                # Opponent close to winning - fight hard
                if attack_cards:
                    return max(attack_cards, key=lambda c: c.value)

            # Otherwise play medium card
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                mid_index = len(sorted_cards) // 2
                return sorted_cards[mid_index]

        return cards[0]

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit ships based on opponent strength."""
        return max(2, max_ships - 1)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite players with strong hands."""
        invites = []
        for p in potential_allies:
            if len(p.hand) >= 6:  # Has cards to help
                invites.append(p)
            if len(invites) >= 2:
                break
        return invites

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Join the likely winner."""
        from ..types import Side

        # Estimate who will win based on colonies and hand size
        offense_strength = (
            offense.count_foreign_colonies(game.planets) +
            len(offense.hand) * 0.3
        )
        defense_strength = (
            defense.count_foreign_colonies(game.planets) +
            len(defense.hand) * 0.3
        )

        if invited_by_offense and offense_strength > defense_strength:
            return Side.OFFENSE
        if invited_by_defense:
            return Side.DEFENSE
        if invited_by_offense:
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit moderate ships."""
        return min(3, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack based on strategic value - prefer weak or undefended planets."""
        planets = defense.home_planets
        if not planets:
            return None

        # Prefer planets with fewest ships - undefended planets are ideal targets
        # (easier to win and establish colony)
        return min(planets, key=lambda p: p.get_ships(defense.name))

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Accept deal if beneficial."""
        # Accept if we need cards
        if len(player.hand) < 5:
            return {"type": "colony_swap"}
        return None

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power opportunistically."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter if good opportunity."""
        cards = player.get_encounter_cards()
        return len(cards) >= 2 and self.get_hand_strength(player) > 0.3


@dataclass
class SocialAI(AIStrategy):
    """
    Social AI focused on alliances and diplomacy.

    Traits:
    - Always invites all possible allies
    - Accepts most alliance invitations
    - Prefers negotiation over combat
    - Makes deals whenever possible
    """
    name: str = field(default="SocialAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Prefer negotiate cards."""
        negotiate_cards = player.get_negotiate_cards()
        if negotiate_cards:
            return negotiate_cards[0]

        attack_cards = player.get_attack_cards()
        if attack_cards:
            # Play low attack if forced to fight
            return min(attack_cards, key=lambda c: c.value)

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit moderate ships."""
        # Aim for half of max, minimum of 2, but never exceed max_ships
        return min(max_ships, max(2, max_ships // 2))

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite everyone!"""
        return list(potential_allies)

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Accept any invitation."""
        from ..types import Side
        if invited_by_offense:
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
        """Commit ships to help allies."""
        return max(2, max_ships - 1)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Random planet selection."""
        planets = defense.home_planets
        if not planets:
            return None
        return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Always try to deal."""
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use power if it helps diplomacy."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter for more interaction."""
        cards = player.get_encounter_cards()
        return len(cards) >= 3


@dataclass
class AdaptiveAI(AIStrategy):
    """
    Adaptive AI that changes strategy based on game state.

    Traits:
    - Plays aggressively when behind
    - Plays cautiously when ahead
    - Targets leader when not winning
    - Defends aggressively when threatened
    """
    name: str = field(default="AdaptiveAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def _get_position(self, game: "Game", player: "Player") -> str:
        """Determine player's position: 'leading', 'contending', 'behind'."""
        my_colonies = player.count_foreign_colonies(game.planets)

        all_colonies = [
            p.count_foreign_colonies(game.planets)
            for p in game.players
        ]
        max_colonies = max(all_colonies)
        avg_colonies = sum(all_colonies) / len(all_colonies)

        if my_colonies == max_colonies and my_colonies >= 3:
            return 'leading'
        elif my_colonies >= avg_colonies:
            return 'contending'
        else:
            return 'behind'

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Adapt card selection to position."""
        position = self._get_position(game, player)
        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        if position == 'leading':
            # Play conservatively when ahead
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                return sorted_cards[len(sorted_cards) // 2]  # Medium card
            if negotiate_cards:
                return negotiate_cards[0]

        elif position == 'behind':
            # Play aggressively when behind
            if attack_cards:
                return max(attack_cards, key=lambda c: c.value)

        else:  # contending
            if is_offense and attack_cards:
                return max(attack_cards, key=lambda c: c.value)
            elif attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value, reverse=True)
                return sorted_cards[min(2, len(sorted_cards)-1)]

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Adapt ship commitment to position."""
        position = self._get_position(game, player)

        if position == 'behind':
            return max_ships  # Go all in when behind
        elif position == 'leading':
            return max(1, max_ships - 2)  # Conserve when ahead
        else:
            return max(2, max_ships - 1)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite based on position."""
        position = self._get_position(game, player)

        if position == 'behind':
            # Need help when behind
            return list(potential_allies)
        elif position == 'leading':
            # Don't share wins when ahead
            return []
        else:
            # Invite 1-2 when contending
            count = min(2, len(potential_allies))
            if count > 0:
                return self._rng.sample(potential_allies, count)
            return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Join side that benefits our position."""
        from ..types import Side
        position = self._get_position(game, player)

        # Check if offense is leading
        offense_colonies = offense.count_foreign_colonies(game.planets)
        defense_colonies = defense.count_foreign_colonies(game.planets)

        if position == 'leading':
            # Don't help others win
            return None

        if invited_by_defense and offense_colonies >= 4:
            # Help stop leader
            return Side.DEFENSE

        if invited_by_offense:
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
        """Commit based on stakes."""
        return max(2, max_ships - 1)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack strategic targets."""
        planets = defense.home_planets
        if not planets:
            return None

        position = self._get_position(game, player)

        if position == 'behind':
            # Attack weakest to guarantee colony
            return min(planets, key=lambda p: p.get_ships(defense.name))
        else:
            # Random attack
            return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Deal based on position."""
        position = self._get_position(game, player)

        if position == 'behind':
            return {"type": "colony_swap"}  # Need progress
        elif position == 'leading':
            return None  # Don't give opponent colonies
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Second encounter based on position."""
        position = self._get_position(game, player)
        cards = player.get_encounter_cards()

        if position == 'behind' and len(cards) >= 2:
            return True
        if position == 'contending' and len(cards) >= 3:
            return True
        return False


@dataclass
class VengefulAI(AIStrategy):
    """
    Vengeful AI that remembers grudges and targets enemies.

    Traits:
    - Tracks players who attacked them
    - Prioritizes attacking grudge targets
    - Fights hard against grudge targets
    - Less likely to ally with enemies
    - Remembers across encounters
    """
    name: str = field(default="VengefulAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)
    grudges: Dict[str, int] = field(default_factory=dict)  # Player name -> grudge level

    def record_attack(self, attacker_name: str) -> None:
        """Record when someone attacks us."""
        self.grudges[attacker_name] = self.grudges.get(attacker_name, 0) + 1

    def get_grudge(self, player_name: str) -> int:
        """Get grudge level against a player."""
        return self.grudges.get(player_name, 0)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Play best cards against grudge targets."""
        opponent = game.defense if is_offense else game.offense
        grudge_level = self.get_grudge(opponent.name) if opponent else 0

        attack_cards = player.get_attack_cards()

        if grudge_level >= 2 and attack_cards:
            # High grudge - play best card
            return max(attack_cards, key=lambda c: c.value)
        elif grudge_level >= 1 and attack_cards:
            # Some grudge - play above average
            sorted_cards = sorted(attack_cards, key=lambda c: c.value, reverse=True)
            return sorted_cards[min(1, len(sorted_cards)-1)]
        elif attack_cards:
            # No grudge - play medium card
            sorted_cards = sorted(attack_cards, key=lambda c: c.value)
            return sorted_cards[len(sorted_cards) // 2]

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Commit more ships against grudge targets."""
        opponent = game.defense if game.offense == player else game.offense
        grudge_level = self.get_grudge(opponent.name) if opponent else 0

        base_ships = max(2, max_ships - 1)
        if grudge_level >= 2:
            return max_ships  # Go all in against enemies
        elif grudge_level >= 1:
            return min(max_ships, base_ships + 1)
        return base_ships

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Don't invite grudge targets as allies."""
        non_enemies = [p for p in potential_allies if self.get_grudge(p.name) < 2]
        if len(non_enemies) >= 2:
            return self._rng.sample(non_enemies, 2)
        return non_enemies

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Side against grudge targets."""
        from ..types import Side

        offense_grudge = self.get_grudge(offense.name)
        defense_grudge = self.get_grudge(defense.name)

        # Always fight against high grudge targets
        if invited_by_defense and offense_grudge >= 2:
            return Side.DEFENSE
        if invited_by_offense and defense_grudge >= 2:
            return Side.OFFENSE

        # Otherwise prefer side with lower grudge
        if invited_by_offense and invited_by_defense:
            if offense_grudge < defense_grudge:
                return Side.OFFENSE
            else:
                return Side.DEFENSE

        if invited_by_offense:
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
        """Commit ships based on grudges."""
        opponent = game.defense if game.offense != player else game.offense
        if opponent and self.get_grudge(opponent.name) >= 2:
            return max_ships  # Want enemy to lose
        return max(2, max_ships - 1)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack grudge targets more aggressively."""
        planets = defense.home_planets
        if not planets:
            return None

        grudge_level = self.get_grudge(defense.name)
        if grudge_level >= 1:
            # Attack their strongest planet - hurt them most
            return max(planets, key=lambda p: p.get_ships(defense.name))
        else:
            # Normal attack - weakest planet
            return min(planets, key=lambda p: p.get_ships(defense.name))

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Don't deal with high grudge targets."""
        grudge = self.get_grudge(opponent.name)
        if grudge >= 2:
            return None  # No deals with enemies
        if grudge >= 1:
            # Grudge but willing to deal for cards
            return {"type": "card_trade", "cards": 2}
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power against grudge targets."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Take second encounter against grudge targets."""
        cards = player.get_encounter_cards()
        return len(cards) >= 2


@dataclass
class KingmakerAI(AIStrategy):
    """
    Kingmaker AI that prevents leaders from winning.

    Traits:
    - Always targets the player closest to winning
    - Allies against leaders
    - Plays defensively against weak players
    - Will sacrifice own progress to stop leaders
    """
    name: str = field(default="KingmakerAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def _get_leader(self, game: "Game", exclude: "Player" = None) -> Optional["Player"]:
        """Find the player closest to winning."""
        best_player = None
        best_colonies = -1

        for p in game.players:
            if p == exclude:
                continue
            colonies = p.count_foreign_colonies(game.planets)
            if colonies > best_colonies:
                best_colonies = colonies
                best_player = p

        return best_player if best_colonies >= 3 else None

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Play hardest against leaders."""
        opponent = game.defense if is_offense else game.offense
        leader = self._get_leader(game, player)

        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        if opponent == leader and attack_cards:
            # Fighting the leader - go all out
            return max(attack_cards, key=lambda c: c.value)
        elif opponent != leader:
            # Not fighting leader - conserve
            if negotiate_cards and self._rng.random() < 0.4:
                return negotiate_cards[0]
            if attack_cards:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                return sorted_cards[0]  # Play lowest

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Max ships against leaders."""
        opponent = game.defense if game.offense == player else game.offense
        leader = self._get_leader(game, player)

        if opponent == leader:
            return max_ships
        return max(1, max_ships - 2)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Invite allies to fight leader."""
        leader = self._get_leader(game, player)
        opponent = game.defense if as_offense else game.offense

        if opponent == leader:
            # Fighting leader - invite everyone
            return list(potential_allies)
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Side against the leader."""
        from ..types import Side
        leader = self._get_leader(game, player)

        if leader == offense and invited_by_defense:
            return Side.DEFENSE
        if leader == defense and invited_by_offense:
            return Side.OFFENSE

        # Otherwise random
        if invited_by_defense:
            return Side.DEFENSE
        if invited_by_offense:
            return Side.OFFENSE
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Max ships when fighting leader."""
        leader = self._get_leader(game, player)
        opponent = game.defense if game.offense != player else game.offense

        if opponent == leader:
            return max_ships
        return 1

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Target leader's weakest spot."""
        planets = defense.home_planets
        if not planets:
            return None

        leader = self._get_leader(game, player)
        if defense == leader:
            # Attack weakest to guarantee victory
            return min(planets, key=lambda p: p.get_ships(defense.name))
        return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Don't give leaders colonies."""
        leader = self._get_leader(game, player)
        if opponent == leader:
            return None  # No deals with leaders
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Always use power against leaders."""
        return True

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Second encounter if not helping leader win."""
        cards = player.get_encounter_cards()
        return len(cards) >= 2


@dataclass
class BlufferAI(AIStrategy):
    """
    Bluffer AI that uses deception and misdirection.

    Traits:
    - Sometimes plays weak cards to appear vulnerable
    - Uses negotiate cards strategically
    - Varies ship commitment unpredictably
    - Makes opponents guess their strength
    """
    name: str = field(default="BlufferAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Unpredictable card selection."""
        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()
        morph_cards = [c for c in player.get_encounter_cards()
                      if hasattr(c, 'card_type') and c.card_type.value == 'morph']

        # Bluff chance - play unexpectedly
        if self._rng.random() < 0.3:
            # 30% chance to bluff
            if attack_cards and len(attack_cards) >= 3:
                # Play lowest card as a bluff
                return min(attack_cards, key=lambda c: c.value)
            if negotiate_cards:
                return negotiate_cards[0]

        # Morph cards are great for bluffing
        if morph_cards and self._rng.random() < 0.4:
            return morph_cards[0]

        # Normal play
        if attack_cards:
            # Mix of high and medium cards
            if self._rng.random() < 0.5:
                return max(attack_cards, key=lambda c: c.value)
            else:
                sorted_cards = sorted(attack_cards, key=lambda c: c.value)
                return sorted_cards[len(sorted_cards) // 2]

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Vary ship commitment to be unpredictable."""
        # Randomly commit between 1 and max
        return self._rng.randint(1, max_ships)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Sometimes invite many, sometimes none."""
        if self._rng.random() < 0.3:
            return []  # No allies - bluff confidence
        if self._rng.random() < 0.5:
            return list(potential_allies)  # All allies - bluff weakness

        count = self._rng.randint(1, min(2, len(potential_allies)))
        if count > 0:
            return self._rng.sample(potential_allies, count)
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Random alliance decisions."""
        from ..types import Side

        if invited_by_offense and invited_by_defense:
            return self._rng.choice([Side.OFFENSE, Side.DEFENSE])
        if invited_by_offense:
            return Side.OFFENSE if self._rng.random() > 0.3 else None
        if invited_by_defense:
            return Side.DEFENSE if self._rng.random() > 0.3 else None
        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Unpredictable ally commitment."""
        return self._rng.randint(1, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Random planet to be unpredictable."""
        planets = defense.home_planets
        if not planets:
            return None
        return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Unpredictable dealing."""
        if self._rng.random() < 0.4:
            return None  # Bluff that we want to fight
        if self._rng.random() < 0.5:
            return {"type": "card_trade", "cards": self._rng.randint(1, 3)}
        return {"type": "colony_swap"}

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Sometimes don't use power to bluff."""
        return self._rng.random() > 0.2  # 80% use power

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Randomly take second encounter."""
        cards = player.get_encounter_cards()
        if len(cards) < 2:
            return False
        return self._rng.random() > 0.4


@dataclass
class MinimalistAI(AIStrategy):
    """
    Minimalist AI focused on efficiency and resource preservation.

    Traits:
    - Wins with minimum resources
    - Never over-commits ships or cards
    - Extremely conservative play
    - Only takes calculated risks
    """
    name: str = field(default="MinimalistAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Play the minimum card that wins."""
        attack_cards = player.get_attack_cards()
        negotiate_cards = player.get_negotiate_cards()

        # Estimate opponent's likely strength
        opponent = game.defense if is_offense else game.offense
        opp_ships = 4  # Assume 4 ships
        opp_avg_card = 8  # Assume average card
        estimated_opp = opp_ships + opp_avg_card

        # Calculate our ships
        my_ships = 1  # Minimum commitment

        if attack_cards:
            sorted_cards = sorted(attack_cards, key=lambda c: c.value)
            # Find minimum card that beats estimate
            for card in sorted_cards:
                if card.value + my_ships > estimated_opp:
                    return card
            # If none sufficient, still play lowest
            return sorted_cards[0]

        if negotiate_cards:
            return negotiate_cards[0]

        cards = player.get_encounter_cards()
        return cards[0] if cards else None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Always commit minimum ships (1)."""
        return 1

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Don't invite allies - don't share wins."""
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Only ally if clear benefit with low risk."""
        from ..types import Side

        # Check if offense likely to win big
        offense_colonies = offense.count_foreign_colonies(game.planets)
        if invited_by_offense and offense_colonies >= 3:
            return Side.OFFENSE  # Bandwagon on leader

        # Defense is safer
        if invited_by_defense:
            return Side.DEFENSE

        return None

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Minimum ships as ally."""
        return 1

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Attack weakest planet for guaranteed win."""
        planets = defense.home_planets
        if not planets:
            return None

        return min(planets, key=lambda p: p.get_ships(defense.name))

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Accept deals to save resources."""
        return {"type": "one_colony"}  # Just get a colony, no reciprocation needed

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Only use power when necessary."""
        return True  # Powers are free

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Only second encounter if well-positioned."""
        cards = player.get_encounter_cards()
        if len(cards) < 4:
            return False

        # Only if we have plenty of resources
        my_colonies = player.count_foreign_colonies(game.planets)
        return my_colonies >= 3  # Close to winning


@dataclass
class ChaosAI(AIStrategy):
    """
    Chaos AI with unpredictable, random decisions.

    Traits:
    - Completely random card selection
    - Random ship commitment
    - Random alliance decisions
    - Makes games unpredictable
    """
    name: str = field(default="ChaosAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Random card selection."""
        cards = player.get_encounter_cards()
        if cards:
            return self._rng.choice(cards)
        return None

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Random ship commitment."""
        return self._rng.randint(1, max_ships)

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Random alliance invitations."""
        if not potential_allies:
            return []

        # Random number of allies
        count = self._rng.randint(0, len(potential_allies))
        if count > 0:
            return self._rng.sample(potential_allies, count)
        return []

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Random alliance response."""
        from ..types import Side

        options = [None]
        if invited_by_offense:
            options.append(Side.OFFENSE)
        if invited_by_defense:
            options.append(Side.DEFENSE)

        return self._rng.choice(options)

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Random ally ships."""
        return self._rng.randint(1, max_ships)

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Random planet selection."""
        planets = defense.home_planets
        if not planets:
            return None
        return self._rng.choice(planets)

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Random deal decision."""
        options = [
            None,
            {"type": "colony_swap"},
            {"type": "card_trade", "cards": self._rng.randint(1, 3)},
            {"type": "one_colony"}
        ]
        return self._rng.choice(options)

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Random power use."""
        return self._rng.random() > 0.3

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Random second encounter decision."""
        cards = player.get_encounter_cards()
        if len(cards) < 1:
            return False
        return self._rng.random() > 0.5
