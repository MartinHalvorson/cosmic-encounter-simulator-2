"""
Lux System (Cosmic Odyssey expansion).

Lux is an in-game currency that allows players more control over resources:
- Buy additional cards for your hand
- Retrieve ships from the warp
- Use special Lux abilities

Formerly known as "Lucre" in earlier editions.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, TYPE_CHECKING
from enum import Enum

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


class LuxAction(Enum):
    """Actions that can be purchased with Lux."""
    BUY_CARD = "buy_card"           # Cost: 3 Lux - Draw 1 card from cosmic deck
    RETRIEVE_SHIP = "retrieve_ship"  # Cost: 2 Lux - Return 1 ship from warp
    EXTRA_SHIP = "extra_ship"        # Cost: 4 Lux - Add 1 extra ship to encounter
    PEEK_HAND = "peek_hand"          # Cost: 1 Lux - Look at opponent's hand
    REROLL_DESTINY = "reroll"        # Cost: 5 Lux - Redraw destiny card


# Lux costs for each action
LUX_COSTS: Dict[LuxAction, int] = {
    LuxAction.BUY_CARD: 3,
    LuxAction.RETRIEVE_SHIP: 2,
    LuxAction.EXTRA_SHIP: 4,
    LuxAction.PEEK_HAND: 1,
    LuxAction.REROLL_DESTINY: 5,
}


@dataclass
class LuxToken:
    """A single Lux token."""
    value: int = 1  # Regular tokens are worth 1, Ultra Lux worth 3


@dataclass
class UltraLuxToken(LuxToken):
    """Ultra Lux token worth 3 regular Lux."""
    value: int = 3


@dataclass
class PlayerLuxState:
    """
    Tracks a player's Lux holdings and spending.
    """
    lux_count: int = 0
    ultra_lux_count: int = 0
    lux_spent_this_game: int = 0
    actions_purchased: List[LuxAction] = field(default_factory=list)

    @property
    def total_lux(self) -> int:
        """Get total Lux value."""
        return self.lux_count + (self.ultra_lux_count * 3)

    def add_lux(self, amount: int) -> None:
        """Add regular Lux tokens."""
        self.lux_count += amount

    def add_ultra_lux(self, count: int = 1) -> None:
        """Add Ultra Lux tokens."""
        self.ultra_lux_count += count

    def can_afford(self, action: LuxAction) -> bool:
        """Check if player can afford an action."""
        return self.total_lux >= LUX_COSTS.get(action, 999)

    def spend(self, amount: int) -> bool:
        """
        Spend Lux tokens, preferring regular over Ultra.
        Returns True if successful.
        """
        if self.total_lux < amount:
            return False

        self.lux_spent_this_game += amount

        # Spend regular Lux first
        if self.lux_count >= amount:
            self.lux_count -= amount
        else:
            # Use combination of regular and ultra
            remaining = amount - self.lux_count
            self.lux_count = 0
            # Ultra Lux are worth 3 each
            ultra_needed = (remaining + 2) // 3  # Ceiling division
            self.ultra_lux_count -= ultra_needed
            # Any change goes back as regular Lux
            change = (ultra_needed * 3) - remaining
            self.lux_count += change

        return True

    def purchase_action(self, action: LuxAction) -> bool:
        """
        Attempt to purchase a Lux action.
        Returns True if successful.
        """
        cost = LUX_COSTS.get(action)
        if cost is None:
            return False

        if self.spend(cost):
            self.actions_purchased.append(action)
            return True
        return False


class LuxManager:
    """
    Manages the Lux economy for a game.
    """

    def __init__(self, starting_lux: int = 5):
        """
        Initialize Lux manager.

        Args:
            starting_lux: Lux each player starts with
        """
        self.starting_lux = starting_lux
        self.player_states: Dict[str, PlayerLuxState] = {}
        self.bank_lux: int = 100  # Available Lux in the bank
        self.bank_ultra_lux: int = 14  # Ultra Lux tokens available

    def initialize_player(self, player_name: str) -> None:
        """Give a player their starting Lux."""
        self.player_states[player_name] = PlayerLuxState(
            lux_count=self.starting_lux
        )
        self.bank_lux -= self.starting_lux

    def get_player_state(self, player_name: str) -> Optional[PlayerLuxState]:
        """Get a player's Lux state."""
        return self.player_states.get(player_name)

    def award_lux(self, player_name: str, amount: int) -> bool:
        """
        Award Lux to a player from the bank.
        Returns True if successful.
        """
        if player_name not in self.player_states:
            return False

        actual_amount = min(amount, self.bank_lux)
        if actual_amount > 0:
            self.player_states[player_name].add_lux(actual_amount)
            self.bank_lux -= actual_amount
            return True
        return False

    def award_ultra_lux(self, player_name: str, count: int = 1) -> bool:
        """
        Award Ultra Lux to a player from the bank.
        Returns True if successful.
        """
        if player_name not in self.player_states:
            return False

        actual_count = min(count, self.bank_ultra_lux)
        if actual_count > 0:
            self.player_states[player_name].add_ultra_lux(actual_count)
            self.bank_ultra_lux -= actual_count
            return True
        return False

    def return_to_bank(self, player_name: str, amount: int) -> None:
        """Return Lux from player to bank (e.g., when spending)."""
        self.bank_lux += amount

    def execute_action(
        self,
        game: "Game",
        player: "Player",
        action: LuxAction
    ) -> bool:
        """
        Execute a Lux action for a player.

        Returns True if the action was executed successfully.
        """
        state = self.player_states.get(player.name)
        if not state or not state.purchase_action(action):
            return False

        # Return spent Lux to the bank
        self.return_to_bank(player.name, LUX_COSTS[action])

        # Execute the action
        if action == LuxAction.BUY_CARD:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)
                return True

        elif action == LuxAction.RETRIEVE_SHIP:
            if player.ships_in_warp > 0:
                player.retrieve_ships_from_warp(1)
                player.return_ships_to_colonies(1, player.home_planets)
                return True

        elif action == LuxAction.EXTRA_SHIP:
            # This should be applied during encounter
            # Mark that player has an extra ship available
            return True

        elif action == LuxAction.PEEK_HAND:
            # This is informational - AI can use this info
            return True

        elif action == LuxAction.REROLL_DESTINY:
            # This should be called during destiny phase
            return True

        return False


# Lux income events - when players earn Lux
class LuxIncome:
    """Standard Lux income events."""

    @staticmethod
    def on_successful_deal(manager: LuxManager, player_names: List[str]) -> None:
        """Both players in a deal get 1 Lux."""
        for name in player_names:
            manager.award_lux(name, 1)

    @staticmethod
    def on_defense_win(manager: LuxManager, defender_name: str) -> None:
        """Defender gets 1 Lux for successfully defending."""
        manager.award_lux(defender_name, 1)

    @staticmethod
    def on_ally_reward(manager: LuxManager, ally_name: str) -> None:
        """Allies may choose 1 Lux instead of cards/ships."""
        manager.award_lux(ally_name, 1)

    @staticmethod
    def on_compensation(manager: LuxManager, player_name: str, ships_lost: int) -> None:
        """Player may get 1 Lux per 2 ships lost as compensation option."""
        lux_earned = ships_lost // 2
        manager.award_lux(player_name, lux_earned)
