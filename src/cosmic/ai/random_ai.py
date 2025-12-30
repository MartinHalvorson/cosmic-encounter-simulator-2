"""
Random AI strategy - makes random decisions.
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
class RandomAI(AIStrategy):
    """
    AI that makes random valid decisions.
    Useful for baseline comparisons and testing.
    """
    name: str = field(default="RandomAI", init=False)
    _rng: random.Random = field(default_factory=random.Random)

    def select_encounter_card(
        self,
        game: "Game",
        player: "Player",
        is_offense: bool
    ) -> "EncounterCard":
        """Select a random encounter card."""
        cards = player.get_encounter_cards()
        if not cards:
            raise ValueError(f"{player.name} has no encounter cards!")
        return self._rng.choice(cards)

    def select_ships_for_encounter(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Select random number of ships (1 to max)."""
        return self._rng.randint(1, max(1, max_ships))

    def decide_alliance_invitation(
        self,
        game: "Game",
        player: "Player",
        potential_allies: List["Player"],
        as_offense: bool
    ) -> List["Player"]:
        """Randomly invite some allies."""
        if not potential_allies:
            return []
        count = self._rng.randint(0, len(potential_allies))
        return self._rng.sample(potential_allies, count)

    def decide_alliance_response(
        self,
        game: "Game",
        player: "Player",
        offense: "Player",
        defense: "Player",
        invited_by_offense: bool,
        invited_by_defense: bool
    ) -> Optional["Side"]:
        """Randomly accept or decline."""
        from ..types import Side

        options = []
        if invited_by_offense:
            options.append(Side.OFFENSE)
        if invited_by_defense:
            options.append(Side.DEFENSE)
        options.append(None)  # Decline

        return self._rng.choice(options)

    def select_ally_ships(
        self,
        game: "Game",
        player: "Player",
        max_ships: int
    ) -> int:
        """Select random number of ally ships."""
        return self._rng.randint(1, max(1, max_ships))

    def select_attack_planet(
        self,
        game: "Game",
        player: "Player",
        defense: "Player"
    ) -> "Planet":
        """Select random planet to attack."""
        home_planets = [p for p in game.planets if p.owner == defense]
        # Prefer planets we don't already have colonies on
        valid = [p for p in home_planets if not p.has_colony(player.name)]
        if not valid:
            valid = home_planets
        return self._rng.choice(valid) if valid else home_planets[0]

    def negotiate_deal(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> Optional[Dict[str, Any]]:
        """Randomly succeed or fail deal."""
        if self._rng.random() < 0.5:
            return {"type": "colony_swap"}  # Simple deal
        return None

    def should_use_power(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Randomly use power."""
        return self._rng.random() < 0.5

    def want_second_encounter(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Randomly want second encounter if we have cards."""
        if not player.has_encounter_card():
            return False
        return self._rng.random() < 0.7  # Usually want it

    def set_seed(self, seed: int) -> None:
        """Set random seed for reproducibility."""
        self._rng.seed(seed)
