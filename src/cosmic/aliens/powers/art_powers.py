"""
Art Powers for Cosmic Encounter.

Aliens inspired by visual arts and artistic concepts.
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
# VISUAL ARTS
# ============================================================================

@dataclass
class Painter(AlienPower):
    """Painter - Power of Creation. Draw extra cards."""
    name: str = field(default="Painter", init=False)
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
class Sculptor(AlienPower):
    """Sculptor - Power of Shaping. Modify card values."""
    name: str = field(default="Sculptor", init=False)
    description: str = field(default="Change card value by up to 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Photographer(AlienPower):
    """Photographer - Power of Capture. Copy opponent's card."""
    name: str = field(default="Photographer", init=False)
    description: str = field(default="Use same value as opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Architect_Art(AlienPower):
    """Architect - Power of Design. +2 for each home colony."""
    name: str = field(default="Architect_Art", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + (home_colonies * 2)
        return base_total


@dataclass
class Illustrator(AlienPower):
    """Illustrator - Power of Detail. See opponent's hand."""
    name: str = field(default="Illustrator", init=False)
    description: str = field(default="See opponent's full hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# ARTISTIC STYLES
# ============================================================================

@dataclass
class Abstract(AlienPower):
    """Abstract - Power of Interpretation. Randomize card effects."""
    name: str = field(default="Abstract", init=False)
    description: str = field(default="Random card value change.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Impressionist(AlienPower):
    """Impressionist - Power of Suggestion. Cards seem stronger."""
    name: str = field(default="Impressionist", init=False)
    description: str = field(default="+3 to displayed value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Surrealist(AlienPower):
    """Surrealist - Power of Dreams. Swap cards with discard."""
    name: str = field(default="Surrealist", init=False)
    description: str = field(default="Exchange cards with discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Minimalist(AlienPower):
    """Minimalist - Power of Simplicity. +5 with 3 or fewer cards."""
    name: str = field(default="Minimalist", init=False)
    description: str = field(default="+5 with small hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return base_total + 5
        return base_total


@dataclass
class Cubist(AlienPower):
    """Cubist - Power of Perspective. View from multiple angles."""
    name: str = field(default="Cubist", init=False)
    description: str = field(default="See 3 cards from deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# PERFORMING ARTS
# ============================================================================

@dataclass
class Dancer_Art(AlienPower):
    """Dancer - Power of Movement. Ships can move freely."""
    name: str = field(default="Dancer_Art", init=False)
    description: str = field(default="Move ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Musician_Art(AlienPower):
    """Musician - Power of Harmony. Allies get +1 each."""
    name: str = field(default="Musician_Art", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Actor(AlienPower):
    """Actor - Power of Performance. Pretend card is different."""
    name: str = field(default="Actor", init=False)
    description: str = field(default="Bluff card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Director(AlienPower):
    """Director - Power of Control. Choose encounter order."""
    name: str = field(default="Director", init=False)
    description: str = field(default="Control encounter sequence.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Conductor(AlienPower):
    """Conductor - Power of Coordination. +2 for each ally."""
    name: str = field(default="Conductor", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# CRAFT & DESIGN
# ============================================================================

@dataclass
class Potter(AlienPower):
    """Potter - Power of Shaping. Modify ship count."""
    name: str = field(default="Potter", init=False)
    description: str = field(default="Add 2 virtual ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count + 2
        return base_count


@dataclass
class Weaver(AlienPower):
    """Weaver - Power of Connection. Link colonies."""
    name: str = field(default="Weaver", init=False)
    description: str = field(default="Ships count from any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glassblower(AlienPower):
    """Glassblower - Power of Fragility. High risk high reward."""
    name: str = field(default="Glassblower", init=False)
    description: str = field(default="+8 but lose 2 ships on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Calligrapher(AlienPower):
    """Calligrapher - Power of Script. Cards reveal information."""
    name: str = field(default="Calligrapher", init=False)
    description: str = field(default="See opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mosaic(AlienPower):
    """Mosaic - Power of Assembly. Combine card values."""
    name: str = field(default="Mosaic", init=False)
    description: str = field(default="Play 2 cards, use total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
for alien_class in [
    Painter, Sculptor, Photographer, Architect_Art, Illustrator,
    Abstract, Impressionist, Surrealist, Minimalist, Cubist,
    Dancer_Art, Musician_Art, Actor, Director, Conductor,
    Potter, Weaver, Glassblower, Calligrapher, Mosaic,
]:
    AlienRegistry.register(alien_class())
