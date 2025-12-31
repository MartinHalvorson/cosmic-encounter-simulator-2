"""
Card Manipulation themed alien powers for Cosmic Encounter.

Powers that interact with cards in unique ways - drawing, discarding,
revealing, swapping, and manipulating card values.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# CARD DRAW POWERS
# ============================================================================

@dataclass
class CardShark(AlienPower):
    """CardShark - Power of the Draw. Extra cards when winning."""
    name: str = field(default="CardShark", init=False)
    description: str = field(default="Draw 2 extra cards when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        as_offense: bool
    ) -> None:
        """Draw extra cards on win."""
        if not player.power_active:
            return
        cards = game.cosmic_deck.draw_multiple(2)
        player.add_cards(cards)


@dataclass
class Hoarder(AlienPower):
    """Hoarder - Power of Accumulation. Never discard down."""
    name: str = field(default="Hoarder", init=False)
    description: str = field(default="No maximum hand size limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scavenger(AlienPower):
    """Scavenger - Power of Retrieval. Get cards from discard."""
    name: str = field(default="Scavenger", init=False)
    description: str = field(default="Draw 1 card from discard instead of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dumpster(AlienPower):
    """Dumpster - Power of the Refuse. Benefit from discards."""
    name: str = field(default="Dumpster", init=False)
    description: str = field(default="When any player discards, you may take 1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CARD REVEAL POWERS
# ============================================================================

@dataclass
class Inspector(AlienPower):
    """Inspector - Power of the Search. Look at opponent's hand."""
    name: str = field(default="Inspector", init=False)
    description: str = field(default="See opponent's hand before planning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Revealer(AlienPower):
    """Revealer - Power of Exposure. Force all cards visible."""
    name: str = field(default="Revealer", init=False)
    description: str = field(default="All players must play cards face-up.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class PeekAboo(AlienPower):
    """PeekAboo - Power of the Glimpse. Sneak peeks at cards."""
    name: str = field(default="PeekAboo", init=False)
    description: str = field(default="See top 3 cards of any deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# CARD SWAP POWERS
# ============================================================================

@dataclass
class Exchanger(AlienPower):
    """Exchanger - Power of the Trade. Swap cards with opponent."""
    name: str = field(default="Exchanger", init=False)
    description: str = field(default="Before reveal, swap 1 card with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Switcher(AlienPower):
    """Switcher - Power of the Change. Swap encounter cards after reveal."""
    name: str = field(default="Switcher", init=False)
    description: str = field(default="After reveal, may swap both encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Borrower(AlienPower):
    """Borrower - Power of the Loan. Use opponent's cards."""
    name: str = field(default="Borrower", init=False)
    description: str = field(default="Play card from opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ============================================================================
# CARD VALUE MANIPULATION
# ============================================================================

@dataclass
class Doubler(AlienPower):
    """Doubler - Power of the Duplicate. Double card values."""
    name: str = field(default="Doubler", init=False)
    description: str = field(default="Once per encounter, double your card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Can double the card value."""
        if not player.power_active:
            return base_total
        # Double 50% of the time when advantageous
        if random.random() < 0.5 and base_total > 20:
            return base_total + (base_total - player.ships_committed)
        return base_total


@dataclass
class Halver(AlienPower):
    """Halver - Power of the Split. Halve opponent's card."""
    name: str = field(default="Halver", init=False)
    description: str = field(default="Halve opponent's card value (round down).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Inverter(AlienPower):
    """Inverter - Power of the Reverse. Invert card value."""
    name: str = field(default="Inverter", init=False)
    description: str = field(default="Turn opponent's card value to 20-X.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Maximizer(AlienPower):
    """Maximizer - Power of the Peak. Play highest card always."""
    name: str = field(default="Maximizer", init=False)
    description: str = field(default="Your lowest card counts as your highest.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Minimizer(AlienPower):
    """Minimizer - Power of the Valley. Low cards win."""
    name: str = field(default="Minimizer", init=False)
    description: str = field(default="Lower total wins encounters involving you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# SPECIAL CARD POWERS
# ============================================================================

@dataclass
class Wildcard(AlienPower):
    """Wildcard - Power of Any. Cards can be anything."""
    name: str = field(default="Wildcard", init=False)
    description: str = field(default="Attack cards can act as negotiate or vice versa.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Joker(AlienPower):
    """Joker - Power of the Wild. Random card effects."""
    name: str = field(default="Joker", init=False)
    description: str = field(default="Your card becomes a random value 1-20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Randomize card value."""
        if not player.power_active:
            return base_total
        # Replace card value with random
        ships = base_total - game.offense_card.value if hasattr(game, 'offense_card') else 0
        return ships + random.randint(1, 20)


@dataclass
class Counterfeit(AlienPower):
    """Counterfeit - Power of the Fake. Copy card values."""
    name: str = field(default="Counterfeit", init=False)
    description: str = field(default="Use opponent's card value as your own.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Recycler(AlienPower):
    """Recycler - Power of Reuse. Play cards from discard."""
    name: str = field(default="Recycler", init=False)
    description: str = field(default="May play encounter card from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shredder(AlienPower):
    """Shredder - Power of Destruction. Remove cards from game."""
    name: str = field(default="Shredder", init=False)
    description: str = field(default="Encounter cards are removed from game, not discarded.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# HAND MANIPULATION
# ============================================================================

@dataclass
class Shuffler(AlienPower):
    """Shuffler - Power of the Mix. Randomize hands."""
    name: str = field(default="Shuffler", init=False)
    description: str = field(default="All players shuffle hands and redistribute.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Collector(AlienPower):
    """Collector - Power of Sets. Bonus for card sets."""
    name: str = field(default="Collector", init=False)
    description: str = field(default="+2 for each pair in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Purger(AlienPower):
    """Purger - Power of Cleansing. Remove bad cards."""
    name: str = field(default="Purger", init=False)
    description: str = field(default="Discard all cards below 8 and redraw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all card manipulation powers
CARD_MANIPULATION_POWERS = [
    CardShark, Hoarder, Scavenger, Dumpster,
    Inspector, Revealer, PeekAboo,
    Exchanger, Switcher, Borrower,
    Doubler, Halver, Inverter, Maximizer, Minimizer,
    Wildcard, Joker, Counterfeit, Recycler, Shredder,
    Shuffler, Collector, Purger,
]


# Auto-register all powers
for power_class in CARD_MANIPULATION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
