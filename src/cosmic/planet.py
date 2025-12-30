"""
Planet representation for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING

from .types import ShipCount

if TYPE_CHECKING:
    from .player import Player


@dataclass
class Planet:
    """
    A planet in the Cosmic Encounter game.
    Each player has 5 home planets, and can establish colonies on others' planets.
    """
    owner: "Player"
    ships: ShipCount = field(default_factory=ShipCount)
    planet_id: int = 0  # Unique identifier for this planet

    def __post_init__(self):
        # Initialize with owner's ships if not already set
        if not self.ships.players_present():
            self.ships.set(self.owner.name, 4)

    def get_ships(self, player_name: str) -> int:
        """Get the number of ships a player has on this planet."""
        return self.ships.get(player_name)

    def set_ships(self, player_name: str, count: int) -> None:
        """Set the number of ships for a player on this planet."""
        self.ships.set(player_name, count)

    def add_ships(self, player_name: str, count: int) -> None:
        """Add ships for a player on this planet."""
        self.ships.add(player_name, count)

    def remove_ships(self, player_name: str, count: int) -> int:
        """Remove ships for a player, returns actual number removed."""
        return self.ships.remove(player_name, count)

    def has_colony(self, player_name: str) -> bool:
        """Check if a player has a colony (at least 1 ship) on this planet."""
        return self.ships.get(player_name) > 0

    def is_home_planet(self, player: "Player") -> bool:
        """Check if this is a home planet for the given player."""
        return self.owner == player

    def is_foreign_colony(self, player: "Player") -> bool:
        """Check if this is a foreign colony for the given player."""
        return self.owner != player and self.has_colony(player.name)

    def colonizers(self) -> List[str]:
        """Get list of player names who have ships on this planet."""
        return self.ships.players_present()

    def total_ships(self) -> int:
        """Total ships on this planet from all players."""
        return self.ships.total()

    def clear_player(self, player_name: str) -> int:
        """Remove all ships of a player from this planet, returns count removed."""
        count = self.ships.get(player_name)
        self.ships.set(player_name, 0)
        return count

    def __str__(self) -> str:
        ship_strs = []
        for player_name in self.ships.players_present():
            count = self.ships.get(player_name)
            ship_strs.append(f"{player_name}: {count}")
        return f"Planet[{self.owner.name}] ({', '.join(ship_strs)})"

    def __repr__(self) -> str:
        return self.__str__()
