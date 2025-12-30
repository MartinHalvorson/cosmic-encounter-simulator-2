"""
Card-related alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Trader(AlienPower):
    """
    Trader - May swap hands with opponent.
    As a main player, before encounter cards are selected, you may
    swap hands with your opponent.
    """
    name: str = field(default="Trader", init=False)
    description: str = field(
        default="Swap hands with opponent before card selection.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Trade if opponent has more cards than us."""
        opponent = context.get("opponent")
        if not opponent:
            return False
        return len(opponent.hand) > len(player.hand)

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Swap hands if beneficial."""
        if not player.power_active:
            return

        if role == PlayerRole.OFFENSE:
            opponent = game.defense
        elif role == PlayerRole.DEFENSE:
            opponent = game.offense
        else:
            return

        # AI decision: trade if opponent has more/better cards
        if self.should_use(game, player, {"opponent": opponent}):
            player.hand, opponent.hand = opponent.hand, player.hand


@dataclass
class Hacker(AlienPower):
    """
    Hacker - Choose compensation cards.
    When collecting compensation, you may choose which cards to take
    from any player's hand instead of random draw.
    """
    name: str = field(default="Hacker", init=False)
    description: str = field(
        default="Choose compensation cards from any player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_compensation(
        self,
        game: "Game",
        player: "Player",
        from_player: "Player",
        count: int
    ) -> int:
        """Choose cards from player with most cards."""
        if not player.power_active:
            return count

        # Find player with most cards
        target = max(
            [p for p in game.players if p != player],
            key=lambda p: len(p.hand),
            default=from_player
        )

        # Take the best cards
        for _ in range(min(count, len(target.hand))):
            if target.hand:
                # Take highest attack card if available
                best = target.select_highest_attack()
                if best:
                    target.remove_card(best)
                    player.add_card(best)
                else:
                    # Take any card
                    card = target.hand[0]
                    target.remove_card(card)
                    player.add_card(card)

        return 0  # Already handled compensation


@dataclass
class Pickpocket(AlienPower):
    """
    Pickpocket - Steal a card from colonizers in your system.
    At the start of each encounter, you may take a random card from
    any player who has a colony in your home system.
    """
    name: str = field(default="Pickpocket", init=False)
    description: str = field(
        default="Steal card from players with colonies in your system.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Steal from colonizers."""
        if not player.power_active:
            return

        # Find players with colonies in our system
        targets = []
        for planet in player.home_planets:
            for colonizer_name in planet.colonizers():
                if colonizer_name != player.name:
                    colonizer = game.get_player_by_name(colonizer_name)
                    if colonizer and colonizer not in targets and colonizer.hand:
                        targets.append(colonizer)

        if targets:
            target = random.choice(targets)
            if target.hand:
                stolen = random.choice(target.hand)
                target.remove_card(stolen)
                player.add_card(stolen)


@dataclass
class Ghoul(AlienPower):
    """
    Ghoul - Collect rewards for ships you defeat.
    As a main player, when you win an encounter, you collect one card
    from the deck for each ship that was lost by the opposing side.
    """
    name: str = field(default="Ghoul", init=False)
    description: str = field(
        default="Win: draw cards for each ship opponent lost.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Draw cards for defeated ships."""
        if not as_main_player or not player.power_active:
            return

        # Count ships lost by opposing side
        if game.offense == player:
            lost_ships = sum(game.defense_ships.values())
        else:
            lost_ships = sum(game.offense_ships.values())

        # Draw reward cards
        cards = game.rewards_deck.draw_multiple(lost_ships)
        player.add_cards(cards)


@dataclass
class Kamikazee(AlienPower):
    """
    Kamikazee - Sacrifice ships for cards.
    As a main player, you may send up to 4 of your ships to the warp
    to draw 2 cards each.
    """
    name: str = field(default="Kamikazee", init=False)
    description: str = field(
        default="Sacrifice ships to draw 2 cards each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use if we need cards and have ships to spare."""
        total_ships = player.total_ships_in_play(game.planets)
        return player.hand_size() < 4 and total_ships > 8

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Sacrifice ships for cards."""
        if not player.power_active:
            return

        if not self.should_use(game, player, {}):
            return

        # Sacrifice up to 3 ships
        ships_to_sacrifice = min(3, player.total_ships_in_play(game.planets) - 5)
        if ships_to_sacrifice <= 0:
            return

        taken = player.get_ships_from_colonies(ships_to_sacrifice, game.planets)
        player.send_ships_to_warp(taken)

        # Draw 2 cards per ship
        cards = game.cosmic_deck.draw_multiple(taken * 2)
        player.add_cards(cards)


@dataclass
class Philanthropist(AlienPower):
    """
    Philanthropist - Give cards to players with fewer cards.
    Whenever you have more than six cards, you must give excess cards
    to the player(s) with the fewest cards.
    """
    name: str = field(default="Philanthropist", init=False)
    description: str = field(
        default="Must give excess cards (over 6) to players with fewest.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def _check_hand_limit(self, game: "Game", player: "Player") -> None:
        """Distribute excess cards."""
        while len(player.hand) > 6:
            # Find player with fewest cards
            others = [p for p in game.players if p != player]
            if not others:
                break

            target = min(others, key=lambda p: len(p.hand))

            # Give worst card to them
            worst = player.select_lowest_attack()
            if worst:
                player.remove_card(worst)
                target.add_card(worst)
            elif player.hand:
                card = player.hand[0]
                player.remove_card(card)
                target.add_card(card)
            else:
                break


@dataclass
class Reserve(AlienPower):
    """
    Reserve - Keep attack cards played in previous encounters.
    After you play an attack card as a main player, instead of
    discarding it, you may add it to your "reserve". Once per encounter
    you may play a card from reserve instead of from hand.
    """
    name: str = field(default="Reserve", init=False)
    description: str = field(
        default="Keep attack cards in reserve to reuse later.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Filch(AlienPower):
    """
    Filch - Steal cards from the discard pile.
    After any player discards cards, you may take one of those cards
    for yourself.
    """
    name: str = field(default="Filch", init=False)
    description: str = field(
        default="Take discarded cards for yourself.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_discard_card(
        self,
        game: "Game",
        player: "Player",
        card: Any
    ) -> bool:
        """Potentially steal discarded cards."""
        # This would be called when any card is discarded
        # For simulation, we can intercept high-value cards
        from ...cards.base import AttackCard
        if isinstance(card, AttackCard) and card.value >= 15:
            if player.power_active:
                player.add_card(card)
                return False  # Prevent normal discard
        return True


# Register all powers
AlienRegistry.register(Trader())
AlienRegistry.register(Hacker())
AlienRegistry.register(Pickpocket())
AlienRegistry.register(Ghoul())
AlienRegistry.register(Kamikazee())
AlienRegistry.register(Philanthropist())
AlienRegistry.register(Reserve())
AlienRegistry.register(Filch())
