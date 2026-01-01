"""
Beverage Powers for Cosmic Encounter.

Aliens inspired by drinks and beverages.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# HOT BEVERAGES
# ============================================================================

@dataclass
class Coffee(AlienPower):
    """Coffee - Power of Energy. Extra encounter after win."""
    name: str = field(default="Coffee", init=False)
    description: str = field(default="Extra encounter after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tea(AlienPower):
    """Tea - Power of Calm. Draw card each turn."""
    name: str = field(default="Tea", init=False)
    description: str = field(default="Draw 1 card per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Cocoa(AlienPower):
    """Cocoa - Power of Comfort. +2 defending home."""
    name: str = field(default="Cocoa", init=False)
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
class Espresso(AlienPower):
    """Espresso - Power of Intensity. +5 attack, -2 defense."""
    name: str = field(default="Espresso", init=False)
    description: str = field(default="+5 attack, -2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 5
        return base_total - 2


@dataclass
class Latte(AlienPower):
    """Latte - Power of Blend. Allies get +1."""
    name: str = field(default="Latte", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# COLD BEVERAGES
# ============================================================================

@dataclass
class Soda(AlienPower):
    """Soda - Power of Fizz. Random +0 to +6."""
    name: str = field(default="Soda", init=False)
    description: str = field(default="Random bonus 0-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Juice(AlienPower):
    """Juice - Power of Health. Retrieve 1 ship from warp."""
    name: str = field(default="Juice", init=False)
    description: str = field(default="Retrieve 1 ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


@dataclass
class Smoothie(AlienPower):
    """Smoothie - Power of Mix. Combine cards."""
    name: str = field(default="Smoothie", init=False)
    description: str = field(default="Add lowest card to attack value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Milkshake(AlienPower):
    """Milkshake - Power of Thickness. +3 total."""
    name: str = field(default="Milkshake", init=False)
    description: str = field(default="+3 in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Lemonade(AlienPower):
    """Lemonade - Power of Refresh. Draw card on loss."""
    name: str = field(default="Lemonade", init=False)
    description: str = field(default="Draw 1 card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# ALCOHOLIC BEVERAGES
# ============================================================================

@dataclass
class Wine(AlienPower):
    """Wine - Power of Refinement. +1 per colony."""
    name: str = field(default="Wine", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + colonies
        return base_total


@dataclass
class Beer(AlienPower):
    """Beer - Power of the Crowd. +1 per player."""
    name: str = field(default="Beer", init=False)
    description: str = field(default="+1 per player in game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(game.players)
        return base_total


@dataclass
class Whiskey(AlienPower):
    """Whiskey - Power of Risk. +6 or -3 randomly."""
    name: str = field(default="Whiskey", init=False)
    description: str = field(default="50% chance of +6 or -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Champagne(AlienPower):
    """Champagne - Power of Victory. +5 on winning."""
    name: str = field(default="Champagne", init=False)
    description: str = field(default="Extra colony on winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sake(AlienPower):
    """Sake - Power of Tradition. +4 when using high card."""
    name: str = field(default="Sake", init=False)
    description: str = field(default="+4 with attack 20+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# SPECIALTY DRINKS
# ============================================================================

@dataclass
class Cocktail(AlienPower):
    """Cocktail - Power of Mix. Combine powers."""
    name: str = field(default="Cocktail", init=False)
    description: str = field(default="Use ally's power once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class EnergyDrink(AlienPower):
    """EnergyDrink - Power of Boost. Ships count extra."""
    name: str = field(default="EnergyDrink", init=False)
    description: str = field(default="Ships count as 1.5x.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Water(AlienPower):
    """Water - Power of Purity. No penalties apply."""
    name: str = field(default="Water", init=False)
    description: str = field(default="Immune to negative effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boba(AlienPower):
    """Boba - Power of Surprises. Random card from discard."""
    name: str = field(default="Boba", init=False)
    description: str = field(default="Add random discard to hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Matcha(AlienPower):
    """Matcha - Power of Focus. See opponent's card."""
    name: str = field(default="Matcha", init=False)
    description: str = field(default="View opponent's chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Coffee, Tea, Cocoa, Espresso, Latte,
    Soda, Juice, Smoothie, Milkshake, Lemonade,
    Wine, Beer, Whiskey, Champagne, Sake,
    Cocktail, EnergyDrink, Water, Boba, Matcha,
]:
    AlienRegistry.register(alien_class())
