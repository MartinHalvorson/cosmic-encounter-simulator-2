"""
Household Powers for Cosmic Encounter.

Aliens inspired by household items and domestic concepts.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Broom(AlienPower):
    """Broom - Power of Sweeping."""
    name: str = field(default="Broom", init=False)
    description: str = field(default="Opponent loses 1 extra ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mop(AlienPower):
    """Mop - Power of Cleaning."""
    name: str = field(default="Mop", init=False)
    description: str = field(default="+2 after each loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sponge(AlienPower):
    """Sponge - Power of Absorption."""
    name: str = field(default="Sponge", init=False)
    description: str = field(default="Draw 1 extra card per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Cabinet(AlienPower):
    """Cabinet - Power of Storage."""
    name: str = field(default="Cabinet", init=False)
    description: str = field(default="No hand size limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pantry(AlienPower):
    """Pantry - Power of Reserves."""
    name: str = field(default="Pantry", init=False)
    description: str = field(default="Draw 2 cards at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Shelf(AlienPower):
    """Shelf - Power of Display."""
    name: str = field(default="Shelf", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(5, len(player.hand))
        return base_total


@dataclass
class Oven(AlienPower):
    """Oven - Power of Heat."""
    name: str = field(default="Oven", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Chandelier(AlienPower):
    """Chandelier - Power of Brilliance."""
    name: str = field(default="Chandelier", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Candle(AlienPower):
    """Candle - Power of Warmth."""
    name: str = field(default="Candle", init=False)
    description: str = field(default="+2 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet in player.home_planets:
                return base_total + 2
        return base_total


@dataclass
class Lamp(AlienPower):
    """Lamp - Power of Light."""
    name: str = field(default="Lamp", init=False)
    description: str = field(default="See opponent's chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Broom, Mop, Sponge, Cabinet, Pantry,
    Shelf, Oven, Chandelier, Candle, Lamp,
]:
    AlienRegistry.register(alien_class())
