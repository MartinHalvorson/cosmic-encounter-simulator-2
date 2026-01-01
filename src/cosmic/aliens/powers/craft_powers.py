"""
Craft Powers for Cosmic Encounter.

Aliens inspired by crafts and artisanal skills.
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
class Potter(AlienPower):
    """Potter - Power of Shaping."""
    name: str = field(default="Potter", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Weaver_Craft(AlienPower):
    """Weaver_Craft - Power of Threads."""
    name: str = field(default="Weaver_Craft", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glassblower(AlienPower):
    """Glassblower - Power of Transformation."""
    name: str = field(default="Glassblower", init=False)
    description: str = field(default="Change card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blacksmith_Craft(AlienPower):
    """Blacksmith_Craft - Power of Forging."""
    name: str = field(default="Blacksmith_Craft", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Carpenter_Craft(AlienPower):
    """Carpenter_Craft - Power of Building."""
    name: str = field(default="Carpenter_Craft", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Jeweler(AlienPower):
    """Jeweler - Power of Precision."""
    name: str = field(default="Jeweler", init=False)
    description: str = field(default="Draw extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Leatherworker(AlienPower):
    """Leatherworker - Power of Durability."""
    name: str = field(default="Leatherworker", init=False)
    description: str = field(default="Ships survive losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tailor(AlienPower):
    """Tailor - Power of Fitting."""
    name: str = field(default="Tailor", init=False)
    description: str = field(default="Match opponent card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cobbler(AlienPower):
    """Cobbler - Power of Travel."""
    name: str = field(default="Cobbler", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Embroiderer(AlienPower):
    """Embroiderer - Power of Detail."""
    name: str = field(default="Embroiderer", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Candlemaker(AlienPower):
    """Candlemaker - Power of Light."""
    name: str = field(default="Candlemaker", init=False)
    description: str = field(default="See opponent hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Woodcarver(AlienPower):
    """Woodcarver - Power of Sculpting."""
    name: str = field(default="Woodcarver", init=False)
    description: str = field(default="+3 with fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Basket_Weaver(AlienPower):
    """Basket_Weaver - Power of Containment."""
    name: str = field(default="Basket_Weaver", init=False)
    description: str = field(default="Hold extra cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Metalsmith(AlienPower):
    """Metalsmith - Power of Strength."""
    name: str = field(default="Metalsmith", init=False)
    description: str = field(default="+4 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Quilter(AlienPower):
    """Quilter - Power of Layers."""
    name: str = field(default="Quilter", init=False)
    description: str = field(default="+1 per card played.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tilemaker(AlienPower):
    """Tilemaker - Power of Pattern."""
    name: str = field(default="Tilemaker", init=False)
    description: str = field(default="+3 same side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clockmaker(AlienPower):
    """Clockmaker - Power of Time."""
    name: str = field(default="Clockmaker", init=False)
    description: str = field(default="Extra encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Papermaker(AlienPower):
    """Papermaker - Power of Creation."""
    name: str = field(default="Papermaker", init=False)
    description: str = field(default="Draw 2 cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Rugmaker(AlienPower):
    """Rugmaker - Power of Foundation."""
    name: str = field(default="Rugmaker", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Bookbinder(AlienPower):
    """Bookbinder - Power of Knowledge."""
    name: str = field(default="Bookbinder", init=False)
    description: str = field(default="Know all card values.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Potter, Weaver_Craft, Glassblower, Blacksmith_Craft, Carpenter_Craft,
    Jeweler, Leatherworker, Tailor, Cobbler, Embroiderer,
    Candlemaker, Woodcarver, Basket_Weaver, Metalsmith, Quilter,
    Tilemaker, Clockmaker, Papermaker, Rugmaker, Bookbinder,
]:
    AlienRegistry.register(alien_class())
