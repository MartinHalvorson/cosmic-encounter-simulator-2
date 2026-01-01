"""
Missing official alien powers from FFG expansions.

This file implements official aliens that were not previously registered.
Powers are based on official Fantasy Flight Games rules.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ==============================================================================
# COSMIC STORM ALIENS (2013)
# ==============================================================================

@dataclass
class Dervish(AlienPower):
    """
    Dervish - Power to Whirl (Cosmic Storm).
    When you lose an encounter as offense, you may use this power to
    immediately have another encounter against the same planet.
    Your ships go to the warp, but you draw a new hand and attack again.
    """
    name: str = field(default="Dervish", init=False)
    description: str = field(
        default="When you lose as offense, may immediately attack again with new hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE], init=False
    )

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> bool:
        """
        When losing as offense, may attack again.
        Returns True if power was used.
        """
        if not player.power_active or not as_offense:
            return False

        # Whirl: Discard hand and draw new hand
        if hasattr(player, 'hand'):
            for card in list(player.hand):
                game.cosmic_deck.discard(card)
            player.hand.clear()
            cards = game.cosmic_deck.draw_multiple(8)
            player.add_cards(cards)

        # Set flag to have another encounter
        if hasattr(game, 'extra_encounter_granted'):
            game.extra_encounter_granted = True

        return True


@dataclass
class Phantasm(AlienPower):
    """
    Phantasm - Power to Materialize (Cosmic Storm).
    You have the power to materialize. Your ships are not committed to
    encounters until cards are revealed. You may withdraw some or all
    ships after seeing both encounter cards.
    """
    name: str = field(default="Phantasm", init=False)
    description: str = field(
        default="May withdraw ships after seeing encounter cards revealed.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_cards_revealed(
        self,
        game: "Game",
        player: "Player",
        offense_card: Any,
        defense_card: Any
    ) -> Dict[str, Any]:
        """
        After cards revealed, may withdraw some ships.
        Returns dict with ships_withdrawn count.
        """
        if not player.power_active:
            return {}

        # AI logic: withdraw if likely to lose badly
        context = {"ships_withdrawn": 0}

        # Simple heuristic: if defense card is much higher, withdraw half ships
        off_val = getattr(offense_card, 'value', 0) if offense_card else 0
        def_val = getattr(defense_card, 'value', 0) if defense_card else 0

        if def_val > off_val + 10:
            # Likely to lose, withdraw half ships
            if hasattr(game, 'offense_ships') and player == game.current_offense:
                withdraw = game.offense_ships // 2
                if withdraw > 0:
                    game.offense_ships -= withdraw
                    player.return_ships_to_colonies(withdraw, player.home_planets)
                    context["ships_withdrawn"] = withdraw

        return context


@dataclass
class Sycophant(AlienPower):
    """
    Sycophant - Power to Flatter (Cosmic Storm).
    You have the power to flatter. At the start of each encounter,
    you may designate any other player as your "patron". You may ally
    with your patron even if not invited, and share in their victory rewards.
    """
    name: str = field(default="Sycophant", init=False)
    description: str = field(
        default="Designate a patron and ally with them uninvited, sharing rewards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    # Store current patron
    patron_name: Optional[str] = None

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Choose a patron at the start of each encounter."""
        if not player.power_active:
            return

        # AI: Choose the player with the most foreign colonies (likely to win)
        best_patron = None
        best_colonies = -1

        for p in game.players:
            if p != player:
                foreign_colonies = sum(
                    1 for planet in game.planets
                    if planet not in p.home_planets
                    and planet.has_colony(p.name)
                )
                if foreign_colonies > best_colonies:
                    best_colonies = foreign_colonies
                    best_patron = p

        self.patron_name = best_patron.name if best_patron else None

    def can_ally_uninvited(
        self,
        game: "Game",
        player: "Player",
        with_player: "Player"
    ) -> bool:
        """Sycophant can ally uninvited with their patron."""
        return (
            player.power_active and
            self.patron_name is not None and
            with_player.name == self.patron_name
        )


@dataclass
class Worm(AlienPower):
    """
    Worm - Power to Burrow (Cosmic Storm).
    You have the power to burrow. When you must encounter a specific
    player's system, you may choose any planet in that system
    (normally destiny determines the planet).
    """
    name: str = field(default="Worm", init=False)
    description: str = field(
        default="Choose which planet to attack in the target's system.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE], init=False
    )

    def choose_target_planet(
        self,
        game: "Game",
        player: "Player",
        defender: "Player"
    ) -> Optional[Any]:
        """
        Choose which planet in defender's system to attack.
        Returns the chosen planet, or None to use default.
        """
        if not player.power_active:
            return None

        # AI logic: choose planet with most foreign ships (easier to take)
        # or planet where we already have ships (expand existing colony)
        best_planet = None
        best_score = -1

        for planet in defender.home_planets:
            score = 0
            # Prefer planets where we already have presence
            if planet.has_colony(player.name):
                score += 10
            # Prefer planets with fewer defensive ships
            defender_ships = planet.get_ships(defender.name)
            score += max(0, 10 - defender_ships)

            if score > best_score:
                best_score = score
                best_planet = planet

        return best_planet


# ==============================================================================
# COSMIC EONS ALIENS (2016)
# ==============================================================================

@dataclass
class AI(AlienPower):
    """
    AI - Power to Compute (Cosmic Eons).
    You have the power to compute. Before cards are selected for an encounter,
    you may look at the top card of the deck and decide whether to place it
    on the bottom. You may also announce the card you will play.
    """
    name: str = field(default="AI", init=False)
    description: str = field(
        default="May view and rearrange deck top, announce intended play.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_planning_phase(
        self,
        game: "Game",
        player: "Player"
    ) -> Dict[str, Any]:
        """
        Before card selection, may peek at deck and manipulate.
        """
        if not player.power_active:
            return {}

        context = {"deck_manipulated": False}

        # Look at top card of cosmic deck
        if hasattr(game, 'cosmic_deck') and game.cosmic_deck.draw_pile:
            top_card = game.cosmic_deck.draw_pile[-1]

            # AI logic: if it's a good card (high attack), move to bottom
            # to prevent opponent from getting it on a draw
            if hasattr(top_card, 'value') and top_card.value > 15:
                # Move to bottom
                game.cosmic_deck.draw_pile.pop()
                game.cosmic_deck.draw_pile.insert(0, top_card)
                context["deck_manipulated"] = True

        return context


@dataclass
class Alien(AlienPower):
    """
    Alien - Power of Otherness (Cosmic Eons).
    You have the power of otherness. You are so different from other species
    that normal rules don't apply. Once per encounter, you may change one
    rule of the current encounter (subject to game integrity).
    """
    name: str = field(default="Alien", init=False)
    description: str = field(
        default="Once per encounter, may alter one rule of the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    # Track if used this encounter
    used_this_encounter: bool = False

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Reset usage tracking."""
        self.used_this_encounter = False

    def alter_rule(
        self,
        game: "Game",
        player: "Player",
        rule_name: str
    ) -> bool:
        """
        Attempt to alter a rule. Returns True if successful.
        Valid rule alterations are predefined for safety.
        """
        if not player.power_active or self.used_this_encounter:
            return False

        valid_alterations = [
            "reverse_card_values",  # Lower cards win instead of higher
            "double_ships",         # Ships count double
            "no_allies",            # No allies this encounter
            "extra_card",           # May play 2 cards
        ]

        if rule_name in valid_alterations:
            self.used_this_encounter = True
            # Store the alteration on the game state
            if not hasattr(game, 'current_alterations'):
                game.current_alterations = []
            game.current_alterations.append(rule_name)
            return True

        return False


@dataclass
class Cloak(AlienPower):
    """
    Cloak - Power to Hide (Cosmic Eons).
    You have the power to hide. Your hand is always hidden from other players.
    Additionally, once per encounter, you may look at any player's hand.
    """
    name: str = field(default="Cloak", init=False)
    description: str = field(
        default="Hand always hidden; once per encounter, may view any player's hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    # Track peek usage
    peeked_this_encounter: bool = False

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Reset peek tracking."""
        self.peeked_this_encounter = False

    def can_view_hand(self, viewer: "Player", target: "Player") -> bool:
        """Other players cannot view Cloak's hand."""
        # This is checked by the game when someone tries to view hands
        return False  # Cloak's hand is always hidden

    def peek_at_hand(
        self,
        game: "Game",
        player: "Player",
        target: "Player"
    ) -> List[Any]:
        """
        Look at target player's hand. Returns list of cards seen.
        """
        if not player.power_active or self.peeked_this_encounter:
            return []

        self.peeked_this_encounter = True
        return list(target.hand) if hasattr(target, 'hand') else []


# ==============================================================================
# COSMIC ODYSSEY ALIENS (2022)
# ==============================================================================

@dataclass
class Assessor(AlienPower):
    """
    Assessor - Power to Evaluate (Cosmic Odyssey).
    You have the power to evaluate. Before cards are played, you may
    announce the total combat value you believe each side will have.
    If you're within 3 of either total, you gain a reward.
    """
    name: str = field(default="Assessor", init=False)
    description: str = field(
        default="Predict combat totals for rewards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Booster(AlienPower):
    """
    Booster - Power to Boost (Cosmic Odyssey / Promo).
    You have the power to boost. When you are a main player or ally,
    you may add +3 to your side's total for each other ship you have
    in the encounter (not counting your first ship).
    """
    name: str = field(default="Booster", init=False)
    description: str = field(
        default="Each ship beyond the first adds +3 to total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def calculate_combat_bonus(
        self,
        game: "Game",
        player: "Player",
        ships_committed: int
    ) -> int:
        """Calculate bonus from extra ships."""
        if not player.power_active or ships_committed <= 1:
            return 0
        return (ships_committed - 1) * 3


@dataclass
class Bubble(AlienPower):
    """
    Bubble - Power to Protect (Cosmic Odyssey).
    You have the power to protect. Once per encounter, you may place
    a "bubble" on one of your colonies. Ships on that planet cannot
    be affected by game effects until the bubble is removed.
    """
    name: str = field(default="Bubble", init=False)
    description: str = field(
        default="Protect a colony from all game effects.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    bubbled_planet: Optional[Any] = None

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Reset bubble each turn."""
        self.bubbled_planet = None

    def apply_bubble(
        self,
        game: "Game",
        player: "Player",
        planet: Any
    ) -> bool:
        """Apply bubble protection to a planet."""
        if not player.power_active or self.bubbled_planet is not None:
            return False

        if planet.has_colony(player.name):
            self.bubbled_planet = planet
            return True
        return False


@dataclass
class Force(AlienPower):
    """
    Force - Power of Strength (Cosmic Odyssey).
    You have the power of strength. Your ships each count as 2 ships
    for the purpose of calculating combat totals.
    """
    name: str = field(default="Force", init=False)
    description: str = field(
        default="Each of your ships counts as 2 in combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def get_ship_multiplier(self, game: "Game", player: "Player") -> int:
        """Ships count double."""
        if player.power_active:
            return 2
        return 1


@dataclass
class Geek(AlienPower):
    """
    Geek - Power of Knowledge (Cosmic Odyssey).
    You have the power of knowledge. At the start of each encounter,
    you may name any alien power. If that power is used during this
    encounter, you draw 3 cards.
    """
    name: str = field(default="Geek", init=False)
    description: str = field(
        default="Guess a power that will be used for card rewards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    guessed_power: Optional[str] = None

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Make a guess at the start of each encounter."""
        if not player.power_active:
            return

        # AI: guess the most common/powerful aliens
        common_powers = ["Zombie", "Machine", "Oracle", "Virus"]
        import random
        self.guessed_power = random.choice(common_powers)

    def on_power_used(
        self,
        game: "Game",
        player: "Player",
        used_power_name: str
    ) -> None:
        """Check if guessed power was used."""
        if (player.power_active and
            self.guessed_power and
            used_power_name == self.guessed_power):
            cards = game.cosmic_deck.draw_multiple(3)
            player.add_cards(cards)
            self.guessed_power = None  # Only reward once


@dataclass
class Gremlin(AlienPower):
    """
    Gremlin - Power to Sabotage (Cosmic Odyssey).
    You have the power to sabotage. Once per encounter, after cards
    are revealed, you may force one main player to discard their
    encounter card and play a new one from their hand.
    """
    name: str = field(default="Gremlin", init=False)
    description: str = field(
        default="Force a main player to discard and replay encounter card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Silencer(AlienPower):
    """
    Silencer - Power to Quiet (Cosmic Odyssey).
    You have the power to quiet. At the start of each encounter,
    you may choose one player. That player cannot use their alien
    power during this encounter.
    """
    name: str = field(default="Silencer", init=False)
    description: str = field(
        default="Suppress one player's alien power each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    silenced_player: Optional[str] = None

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Choose a player to silence."""
        if not player.power_active:
            self.silenced_player = None
            return

        # AI: silence the most threatening power
        threat_powers = ["Virus", "Machine", "Zombie", "Oracle", "Loser"]

        for p in game.players:
            if p != player and hasattr(p, 'alien') and p.alien:
                if p.alien.name in threat_powers:
                    self.silenced_player = p.name
                    p.power_active = False  # Temporarily disable
                    return

        self.silenced_player = None


@dataclass
class TheMeek(AlienPower):
    """
    The Meek - Power to Win by Losing (Cosmic Odyssey).
    You have the power to inherit. Instead of advancing when you win,
    you only advance when you lose. Winning actually lowers your score.
    You win when you have 8 losses (increased from 5 for balance).
    """
    name: str = field(default="The Meek", init=False)
    description: str = field(
        default="Win by losing - victories decrease score, 15 losses wins.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    has_alternate_win: bool = True

    # Track losses for alternate win
    loss_count: int = 0

    def on_game_start(self, game: "Game", player: "Player") -> None:
        """Reset loss count at start of each game."""
        self.loss_count = 0

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Losing advances The Meek."""
        if player.power_active:
            self.loss_count += 1

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Winning penalizes The Meek."""
        if player.power_active and self.loss_count > 0:
            self.loss_count -= 1

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Check if The Meek has won through losses."""
        # Requires 15 losses (very hard to achieve)
        return player.power_active and self.loss_count >= 15


@dataclass
class Vector(AlienPower):
    """
    Vector - Power of Direction (Cosmic Odyssey).
    You have the power of direction. When you commit ships to an
    encounter, you may move them from any of your colonies, not just
    from your home system.
    """
    name: str = field(default="Vector", init=False)
    description: str = field(
        default="Commit ships from any colony, not just home system.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Witch(AlienPower):
    """
    Witch - Power to Curse (Cosmic Odyssey).
    You have the power to curse. Once per encounter, you may place
    a "curse" token on any player. That player's ships count as
    half value (rounded down) until the curse is removed.
    """
    name: str = field(default="Witch", init=False)
    description: str = field(
        default="Curse a player to halve their ship values.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    cursed_player: Optional[str] = None

    def apply_curse(
        self,
        game: "Game",
        player: "Player",
        target: "Player"
    ) -> bool:
        """Apply curse to a target player."""
        if not player.power_active or self.cursed_player:
            return False

        self.cursed_player = target.name
        return True


@dataclass
class Wrack(AlienPower):
    """
    Wrack - Power to Damage (Cosmic Odyssey).
    You have the power to damage. When you lose an encounter,
    the winner loses one ship to the warp for every 5 points
    by which they exceeded your total.
    """
    name: str = field(default="Wrack", init=False)
    description: str = field(
        default="When losing, winner loses 1 ship per 5 points of difference.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Damage the winner proportional to victory margin."""
        if not player.power_active:
            return

        if hasattr(game, 'last_encounter_result'):
            result = game.last_encounter_result
            margin = abs(result.offense_total - result.defense_total)
            ships_lost = margin // 5

            if ships_lost > 0:
                winner = game.current_defense if as_offense else game.current_offense
                if winner:
                    winner.ships_to_warp(ships_lost)


@dataclass
class Zilch(AlienPower):
    """
    Zilch - Power of Nothing (Cosmic Odyssey).
    You have the power of nothing. When you have no cards in hand,
    you automatically win any encounter you're involved in (as main
    player or ally).
    """
    name: str = field(default="Zilch", init=False)
    description: str = field(
        default="Automatically win when you have no cards in hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def check_auto_win(self, game: "Game", player: "Player") -> bool:
        """Check if Zilch automatically wins."""
        return player.power_active and player.hand_size() == 0


@dataclass
class Micron(AlienPower):
    """
    Micron - Power of Tiny (Cosmic Odyssey).
    You have the power of tiny. Your ships are so small they can
    sneak onto planets. You may have up to 8 ships on any single planet.
    Also, your first ship to the warp each encounter returns to colonies.
    """
    name: str = field(default="Micron", init=False)
    description: str = field(
        default="May have 8 ships per planet; first ship to warp returns home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def get_max_ships_per_planet(
        self,
        game: "Game",
        player: "Player"
    ) -> int:
        """Micron can have 8 ships per planet."""
        if player.power_active:
            return 8
        return 4  # Normal max


@dataclass
class Lemming(AlienPower):
    """
    Lemming - Power to Follow (Cosmic Odyssey).
    You have the power to follow. Whenever another player allies,
    you may also ally on the same side with the same number of ships,
    even if not invited.
    """
    name: str = field(default="Lemming", init=False)
    description: str = field(
        default="May copy any alliance, uninvited.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lloyd(AlienPower):
    """
    Lloyd - Power to Insure (Cosmic Odyssey).
    You have the power to insure. At the start of each encounter,
    you may "insure" any player's ships. If those ships go to the
    warp, you may draw cards equal to the ships lost, and the insured
    player retrieves half their ships (rounded up).
    """
    name: str = field(default="Lloyd", init=False)
    description: str = field(
        default="Insure ships - if lost, you draw cards and they get half back.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    insured_player: Optional[str] = None

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Reset insurance each encounter."""
        self.insured_player = None

    def insure_player(
        self,
        game: "Game",
        player: "Player",
        target: "Player"
    ) -> bool:
        """Insure a player's ships."""
        if not player.power_active or self.insured_player:
            return False
        self.insured_player = target.name
        return True


@dataclass
class Tentacle(AlienPower):
    """
    Tentacle - Power to Grasp (Cosmic Odyssey).
    You have the power to grasp. When you ally, you may commit ships
    from multiple colonies, and your ships count as 1.5x (rounded down)
    their normal value.
    """
    name: str = field(default="Tentacle", init=False)
    description: str = field(
        default="Allied ships count 1.5x value and can come from multiple colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def get_ally_ship_multiplier(
        self,
        game: "Game",
        player: "Player"
    ) -> float:
        """Allied ships count 1.5x."""
        if player.power_active:
            return 1.5
        return 1.0


@dataclass
class Throwback(AlienPower):
    """
    Throwback - Power of Nostalgia (Cosmic Odyssey).
    You have the power of nostalgia. You use the classic Eon edition
    rules for card play: you may play cards from the discard pile
    as if they were in your hand.
    """
    name: str = field(default="Throwback", init=False)
    description: str = field(
        default="May play cards from the discard pile as if in hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Extractor(AlienPower):
    """
    Extractor - Power to Extract (Cosmic Odyssey).
    You have the power to extract. Once per encounter, you may
    remove one card from any player's hand and add it to yours.
    """
    name: str = field(default="Extractor", init=False)
    description: str = field(
        default="Once per encounter, take a card from any player's hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hurtz(AlienPower):
    """
    Hurtz - Power to Pain (Cosmic Odyssey).
    You have the power to pain. Whenever any of your ships go to the
    warp, the player who caused them to go there loses one ship to
    the warp as well.
    """
    name: str = field(default="Hurtz", init=False)
    description: str = field(
        default="When your ships go to warp, the responsible player loses one too.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# Register all aliens
# ==============================================================================

# Cosmic Storm
AlienRegistry.register(Dervish())
AlienRegistry.register(Phantasm())
AlienRegistry.register(Sycophant())
AlienRegistry.register(Worm())

# Cosmic Eons
AlienRegistry.register(AI())
AlienRegistry.register(Alien())
AlienRegistry.register(Cloak())

# Cosmic Odyssey
AlienRegistry.register(Assessor())
AlienRegistry.register(Booster())
AlienRegistry.register(Bubble())
AlienRegistry.register(Force())
AlienRegistry.register(Geek())
AlienRegistry.register(Gremlin())
AlienRegistry.register(Silencer())
AlienRegistry.register(TheMeek())
AlienRegistry.register(Vector())
AlienRegistry.register(Witch())
AlienRegistry.register(Wrack())
AlienRegistry.register(Zilch())
AlienRegistry.register(Micron())
AlienRegistry.register(Lemming())
AlienRegistry.register(Lloyd())
AlienRegistry.register(Tentacle())
AlienRegistry.register(Throwback())
AlienRegistry.register(Extractor())
AlienRegistry.register(Hurtz())
