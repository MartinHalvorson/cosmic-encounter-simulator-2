"""
Extended Nature Powers for Cosmic Encounter.

Aliens inspired by natural phenomena and elements.
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
# GEOLOGICAL POWERS
# ============================================================================

@dataclass
class Mountain_Alt(AlienPower):
    """Mountain - Power of Height. +4 when defending home."""
    name: str = field(default="Mountain_Alt", init=False)
    description: str = field(default="+4 when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE and game.defense_planet in player.home_planets:
            return base_total + 4
        return base_total


@dataclass
class Valley(AlienPower):
    """Valley - Power of Shelter. Ships protected on defense."""
    name: str = field(default="Valley", init=False)
    description: str = field(default="Ships stay on planet when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Canyon(AlienPower):
    """Canyon - Power of Division. Split opponent's forces."""
    name: str = field(default="Canyon", init=False)
    description: str = field(default="Opponent uses half their ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cave(AlienPower):
    """Cave - Power of Hiding. Ships can avoid encounters."""
    name: str = field(default="Cave", init=False)
    description: str = field(default="Hide ships from attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cliff(AlienPower):
    """Cliff - Power of Edge. Win ties."""
    name: str = field(default="Cliff", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# WATER POWERS
# ============================================================================

@dataclass
class River_Alt(AlienPower):
    """River - Power of Flow. Ships can attack from any colony."""
    name: str = field(default="River_Alt", init=False)
    description: str = field(default="Attack from any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lake(AlienPower):
    """Lake - Power of Stillness. Opponents can't use reinforcements."""
    name: str = field(default="Lake", init=False)
    description: str = field(default="Block opponent's reinforcements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Waterfall(AlienPower):
    """Waterfall - Power of Force. +3 when attacking downhill."""
    name: str = field(default="Waterfall", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Pond(AlienPower):
    """Pond - Power of Reflection. Copy ally's alien power."""
    name: str = field(default="Pond", init=False)
    description: str = field(default="Use ally's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spring_Alt(AlienPower):
    """Spring - Power of Renewal. Retrieve ships each turn."""
    name: str = field(default="Spring_Alt", init=False)
    description: str = field(default="Retrieve 1 ship per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)


# ============================================================================
# PLANT POWERS
# ============================================================================

@dataclass
class Forest_Alt(AlienPower):
    """Forest - Power of Growth. +1 for each home colony."""
    name: str = field(default="Forest_Alt", init=False)
    description: str = field(default="+1 for each home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + home_colonies
        return base_total


@dataclass
class Jungle(AlienPower):
    """Jungle - Power of Density. Ships worth double on home."""
    name: str = field(default="Jungle", init=False)
    description: str = field(default="Ships worth double at home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Meadow(AlienPower):
    """Meadow - Power of Peace. Both sides draw 1 card after encounter."""
    name: str = field(default="Meadow", init=False)
    description: str = field(default="Both sides draw 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Swamp(AlienPower):
    """Swamp - Power of Trapping. Opponent's ships stuck in warp longer."""
    name: str = field(default="Swamp", init=False)
    description: str = field(default="Trap opponent's ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tundra(AlienPower):
    """Tundra - Power of Cold. Slow opponent's card draws."""
    name: str = field(default="Tundra", init=False)
    description: str = field(default="Opponent draws fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# WEATHER POWERS
# ============================================================================

@dataclass
class Sunshine(AlienPower):
    """Sunshine - Power of Light. See all hidden information."""
    name: str = field(default="Sunshine", init=False)
    description: str = field(default="See opponent's cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cloudy(AlienPower):
    """Cloudy - Power of Obscurity. Hide your card until reveal."""
    name: str = field(default="Cloudy", init=False)
    description: str = field(default="Card remains hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Windy(AlienPower):
    """Windy - Power of Movement. Move ships between colonies freely."""
    name: str = field(default="Windy", init=False)
    description: str = field(default="Free ship movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rainy(AlienPower):
    """Rainy - Power of Abundance. Draw extra cards each turn."""
    name: str = field(default="Rainy", init=False)
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
class Snowy(AlienPower):
    """Snowy - Power of Slowing. Opponent attacks with fewer ships."""
    name: str = field(default="Snowy", init=False)
    description: str = field(default="Opponent uses 1 less ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
for alien_class in [
    Mountain_Alt, Valley, Canyon, Cave, Cliff,
    River_Alt, Lake, Waterfall, Pond, Spring_Alt,
    Forest_Alt, Jungle, Meadow, Swamp, Tundra,
    Sunshine, Cloudy, Windy, Rainy, Snowy,
]:
    AlienRegistry.register(alien_class())
