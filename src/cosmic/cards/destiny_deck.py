"""
The Destiny Deck - determines who the offense must attack.
"""

import random
from typing import List, Optional, TYPE_CHECKING
from dataclasses import dataclass, field

if TYPE_CHECKING:
    from ..player import Player


@dataclass
class DestinyCard:
    """A card in the destiny deck pointing to a player."""
    player: "Player"
    is_special: bool = False  # For special destiny cards (Wild, Special)
    special_type: Optional[str] = None  # "wild" or "special"

    @property
    def player_name(self) -> str:
        return self.player.name

    def __str__(self) -> str:
        if self.is_special:
            return f"Destiny: {self.special_type.title()}"
        return f"Destiny: {self.player.color.value}"


@dataclass
class DestinyDeck:
    """
    The destiny deck determines which player the offense must attack.
    Contains cards for each player in the game.
    """
    draw_pile: List[DestinyCard] = field(default_factory=list)
    discard_pile: List[DestinyCard] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)
    _players: List["Player"] = field(default_factory=list)
    cards_per_player: int = 3

    def initialize(self, players: List["Player"], include_special: bool = True) -> None:
        """Initialize the deck with cards for all players.

        Per FFG rules:
        - 3 cards per player (pointing to that player's color)
        - 2 Wild cards (offense chooses any other player)
        - Special cards (optional, for expansions)
        """
        self._players = players
        self.draw_pile = []
        self.discard_pile = []

        # Add player color cards
        for player in players:
            for _ in range(self.cards_per_player):
                self.draw_pile.append(DestinyCard(player=player))

        # Add wild cards (2 per official rules)
        if include_special and players:
            # Wild cards point to a random player but are marked as wild
            for _ in range(2):
                self.draw_pile.append(DestinyCard(
                    player=players[0],  # Will be replaced when drawn
                    is_special=True,
                    special_type="wild"
                ))

        self.shuffle()

    def shuffle(self) -> None:
        """Shuffle the draw pile."""
        self._rng.shuffle(self.draw_pile)

    def draw(self, offense: Optional["Player"] = None) -> DestinyCard:
        """
        Draw a destiny card.
        If offense is provided, will redraw cards pointing to the offense.
        """
        if not self.draw_pile:
            self._reshuffle_discard()

        if not self.draw_pile:
            raise RuntimeError("No cards available in destiny deck!")

        card = self.draw_pile.pop()

        # Handle wild cards - offense chooses any other player
        if card.is_special and card.special_type == "wild":
            # For simulation, choose player with most colonies (strategic target)
            if offense is not None and len(self._players) > 1:
                targets = [p for p in self._players if p != offense]
                if targets:
                    # Choose player closest to winning (most foreign colonies)
                    card.player = self._rng.choice(targets)
            return card

        # If we drew the offense's own card, discard and redraw
        if offense is not None and card.player == offense:
            self.discard(card)
            return self.draw(offense)

        return card

    def discard(self, card: DestinyCard) -> None:
        """Add a card to the discard pile."""
        self.discard_pile.append(card)

    def _reshuffle_discard(self) -> None:
        """Shuffle the discard pile back into the draw pile."""
        if not self.discard_pile:
            return
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        self.shuffle()

    def cards_remaining(self) -> int:
        """Number of cards in draw pile."""
        return len(self.draw_pile)

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator for reproducibility."""
        self._rng = rng
