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

    def initialize(self, players: List["Player"]) -> None:
        """Initialize the deck with cards for all players."""
        self._players = players
        self.draw_pile = []
        self.discard_pile = []

        for player in players:
            for _ in range(self.cards_per_player):
                self.draw_pile.append(DestinyCard(player=player))

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
