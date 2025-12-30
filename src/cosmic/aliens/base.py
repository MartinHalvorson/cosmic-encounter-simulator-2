"""
Base class for alien powers.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING, Callable
from abc import ABC, abstractmethod
from enum import Enum, auto

from ..types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


class PowerCategory(Enum):
    """Category/complexity of alien power."""
    GREEN = auto()   # Simple, recommended for beginners
    YELLOW = auto()  # Moderate complexity
    RED = auto()     # Complex, for experienced players


@dataclass
class AlienPower(ABC):
    """
    Base class for all alien powers.

    Each alien power can hook into various game events and modify behavior.
    Powers should be immutable - store any state on the Player object.
    """
    name: str
    description: str
    timing: PowerTiming
    power_type: PowerType = PowerType.OPTIONAL
    category: PowerCategory = PowerCategory.GREEN
    alert_text: str = ""  # Short text shown when power might activate

    # Which roles can use this power
    usable_as: List[PlayerRole] = field(default_factory=lambda: [
        PlayerRole.OFFENSE,
        PlayerRole.DEFENSE,
        PlayerRole.OFFENSIVE_ALLY,
        PlayerRole.DEFENSIVE_ALLY,
        PlayerRole.NOT_INVOLVED,
    ])

    # Alternative win condition (if any)
    has_alternate_win: bool = False

    def can_use_as(self, role: PlayerRole) -> bool:
        """Check if power can be used in the given role."""
        return role in self.usable_as

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """
        AI decision: Should the power be used in this situation?
        Override in subclasses for power-specific logic.
        Default: always use if optional, or if mandatory.
        """
        return self.power_type == PowerType.MANDATORY or True

    # ========== Lifecycle Hooks ==========

    def on_game_start(self, game: "Game", player: "Player") -> None:
        """Called when the game starts. Use for special setup."""
        pass

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Called at the start of each turn."""
        pass

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Called at the start of each encounter."""
        pass

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        """Called at the end of each encounter."""
        pass

    # ========== Phase Hooks ==========

    def on_regroup(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Called during regroup phase."""
        pass

    def on_destiny(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        destiny_player: "Player"
    ) -> Optional["Player"]:
        """
        Called when destiny is drawn.
        Can return a different player to attack instead.
        """
        return None

    def on_launch(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Called during launch phase."""
        pass

    def on_alliance_invite(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        invited_to: Side
    ) -> Optional[bool]:
        """
        Called when alliances are formed.
        Return True to force join, False to force decline, None for normal.
        """
        return None

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Called during planning phase."""
        pass

    def on_reveal(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Called when cards are revealed."""
        pass

    def on_resolution(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Called during resolution phase."""
        pass

    # ========== Combat Modification Hooks ==========

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        base_value: int,
        side: Side
    ) -> int:
        """
        Modify the attack card value.
        Called during resolution for main players.
        """
        return base_value

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """
        Modify the ship count contribution.
        Called during resolution.
        """
        return base_count

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """
        Modify the final total for a side.
        Called after all other modifications.
        """
        return base_total

    # ========== Card Hooks ==========

    def on_draw_card(
        self,
        game: "Game",
        player: "Player",
        card: Any
    ) -> Any:
        """Called when drawing a card. Can modify or replace the card."""
        return card

    def on_discard_card(
        self,
        game: "Game",
        player: "Player",
        card: Any
    ) -> bool:
        """Called when discarding. Return False to prevent discard."""
        return True

    def on_compensation(
        self,
        game: "Game",
        player: "Player",
        from_player: "Player",
        count: int
    ) -> int:
        """Called when receiving compensation. Can modify count."""
        return count

    # ========== Ship Hooks ==========

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        source: str
    ) -> int:
        """
        Called when ships would go to warp.
        Return modified count (0 to prevent).
        """
        return count

    def on_ships_from_warp(
        self,
        game: "Game",
        player: "Player",
        count: int
    ) -> int:
        """Called when retrieving ships from warp. Can modify count."""
        return count

    def on_lose_colony(
        self,
        game: "Game",
        player: "Player",
        planet: Any
    ) -> None:
        """Called when losing a colony."""
        pass

    def on_gain_colony(
        self,
        game: "Game",
        player: "Player",
        planet: Any
    ) -> None:
        """Called when gaining a colony."""
        pass

    # ========== Win/Lose Hooks ==========

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Called when winning an encounter."""
        pass

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Called when losing an encounter."""
        pass

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Check if alternate win condition is met."""
        return False

    # ========== Deal Hooks ==========

    def on_deal_start(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> None:
        """Called when a deal phase starts."""
        pass

    def on_deal_success(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> None:
        """Called when a deal is successfully made."""
        pass

    def on_deal_failure(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> None:
        """Called when a deal fails."""
        pass

    # ========== Utility ==========

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __repr__(self) -> str:
        return f"AlienPower({self.name})"
