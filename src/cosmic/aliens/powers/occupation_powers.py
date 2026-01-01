"""
Occupation Powers for Cosmic Encounter.

Aliens inspired by various professions and occupations.
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
# CREATIVE OCCUPATIONS
# ============================================================================

@dataclass
class Writer(AlienPower):
    """Writer - Power of Words. +1 for each card in hand."""
    name: str = field(default="Writer", init=False)
    description: str = field(default="+1 for each card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(player.hand)
        return base_total


@dataclass
class Painter(AlienPower):
    """Painter - Power of Art. Draw 1 card when losing."""
    name: str = field(default="Painter", init=False)
    description: str = field(default="Draw 1 card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Sculptor(AlienPower):
    """Sculptor - Power of Form. Ships count as +2 each."""
    name: str = field(default="Sculptor", init=False)
    description: str = field(default="Ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count * 2
        return base_count


@dataclass
class Musician_Alt(AlienPower):
    """Musician - Power of Harmony. +1 for each ally."""
    name: str = field(default="Musician_Alt", init=False)
    description: str = field(default="+1 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        allies = len(game.offense_allies) if side == Side.OFFENSE else len(game.defense_allies)
        return base_total + allies


@dataclass
class Photographer(AlienPower):
    """Photographer - Power of Capture. See opponent's hand once per encounter."""
    name: str = field(default="Photographer", init=False)
    description: str = field(default="See opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# TECHNICAL OCCUPATIONS
# ============================================================================

@dataclass
class Mechanic(AlienPower):
    """Mechanic - Power of Repair. Retrieve 1 ship from warp each encounter."""
    name: str = field(default="Mechanic", init=False)
    description: str = field(default="Retrieve 1 ship from warp each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


@dataclass
class Electrician(AlienPower):
    """Electrician - Power of Connection. +2 when main player."""
    name: str = field(default="Electrician", init=False)
    description: str = field(default="+2 when main player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            if player == game.offense or player == game.defense:
                return base_total + 2
        return base_total


@dataclass
class Plumber(AlienPower):
    """Plumber - Power of Flow. Ships can move between colonies freely."""
    name: str = field(default="Plumber", init=False)
    description: str = field(default="Free ship movement between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Carpenter(AlienPower):
    """Carpenter - Power of Building. +1 for each colony you have."""
    name: str = field(default="Carpenter", init=False)
    description: str = field(default="+1 for each colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + colonies
        return base_total


@dataclass
class Welder(AlienPower):
    """Welder - Power of Joining. Allied ships fused with yours."""
    name: str = field(default="Welder", init=False)
    description: str = field(default="Allied ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# SERVICE OCCUPATIONS
# ============================================================================

@dataclass
class Waiter(AlienPower):
    """Waiter - Power of Service. Help allies get compensation."""
    name: str = field(default="Waiter", init=False)
    description: str = field(default="Allies draw extra compensation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bartender(AlienPower):
    """Bartender - Power of Mixing. Combine card values."""
    name: str = field(default="Bartender", init=False)
    description: str = field(default="Play two cards, use combined value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Barber(AlienPower):
    """Barber - Power of Trimming. Reduce opponent's total by 3."""
    name: str = field(default="Barber", init=False)
    description: str = field(default="Reduce opponent's total by 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Janitor(AlienPower):
    """Janitor - Power of Cleanup. Clear cards from discard."""
    name: str = field(default="Janitor", init=False)
    description: str = field(default="Take cards from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Librarian(AlienPower):
    """Librarian - Power of Knowledge. Look at top 3 cards of deck."""
    name: str = field(default="Librarian", init=False)
    description: str = field(default="See top 3 cards of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# PROFESSIONAL OCCUPATIONS
# ============================================================================

@dataclass
class Accountant(AlienPower):
    """Accountant - Power of Numbers. +1 per 5 cards in hand."""
    name: str = field(default="Accountant", init=False)
    description: str = field(default="+1 per 5 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (len(player.hand) // 5)
        return base_total


@dataclass
class Manager(AlienPower):
    """Manager - Power of Leadership. Allies get +1 each."""
    name: str = field(default="Manager", init=False)
    description: str = field(default="Allied ships worth +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Consultant(AlienPower):
    """Consultant - Power of Advice. See opponent's card before reveal."""
    name: str = field(default="Consultant", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Recruiter(AlienPower):
    """Recruiter - Power of Hiring. Invite extra allies."""
    name: str = field(default="Recruiter", init=False)
    description: str = field(default="Invite one extra ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Negotiator(AlienPower):
    """Negotiator - Power of Deals. Win ties when negotiating."""
    name: str = field(default="Negotiator", init=False)
    description: str = field(default="Win ties in negotiations.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Writer, Painter, Sculptor, Musician_Alt, Photographer,
    Mechanic, Electrician, Plumber, Carpenter, Welder,
    Waiter, Bartender, Barber, Janitor, Librarian,
    Accountant, Manager, Consultant, Recruiter, Negotiator,
]:
    AlienRegistry.register(alien_class())
