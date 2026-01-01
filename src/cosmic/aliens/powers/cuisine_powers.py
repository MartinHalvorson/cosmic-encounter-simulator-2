"""
Cuisine themed alien powers for Cosmic Encounter.

Powers based on world cuisines, cooking styles, and culinary concepts.
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
# COOKING METHODS
# ============================================================================

@dataclass
class Griller(AlienPower):
    """Griller - Power of Fire. Direct heat attack."""
    name: str = field(default="Griller", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Steamer(AlienPower):
    """Steamer - Power of Pressure. Build up slowly."""
    name: str = field(default="Steamer_Cook", init=False)
    description: str = field(default="+1 per turn passed (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Fryer(AlienPower):
    """Fryer - Power of Immersion. Quick and powerful."""
    name: str = field(default="Fryer", init=False)
    description: str = field(default="+5 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Smoker(AlienPower):
    """Smoker - Power of Slow Cook. Patient approach."""
    name: str = field(default="Smoker", init=False)
    description: str = field(default="+2 per colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Roaster(AlienPower):
    """Roaster - Power of Even Heat. Consistent results."""
    name: str = field(default="Roaster", init=False)
    description: str = field(default="Your card is always worth at least 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stewer(AlienPower):
    """Stewer - Power of Combination. Mix ingredients."""
    name: str = field(default="Stewer", init=False)
    description: str = field(default="+1 for each ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + allies


# ============================================================================
# WORLD CUISINES
# ============================================================================

@dataclass
class Sushi(AlienPower):
    """Sushi - Power of Precision. Careful preparation."""
    name: str = field(default="Sushi", init=False)
    description: str = field(default="+4 if your card is exactly 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Curry(AlienPower):
    """Curry - Power of Spice. Heated combat."""
    name: str = field(default="Curry", init=False)
    description: str = field(default="Random +0 to +5 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(0, 5)
        return base_total


@dataclass
class Pasta(AlienPower):
    """Pasta - Power of Versatility. Adapt to situation."""
    name: str = field(default="Pasta", init=False)
    description: str = field(default="Copy opponent's power for this encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Taco(AlienPower):
    """Taco - Power of Layering. Multiple bonuses."""
    name: str = field(default="Taco", init=False)
    description: str = field(default="+1 per card in hand (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(5, len(player.hand))
        return base_total


@dataclass
class Ramen(AlienPower):
    """Ramen - Power of Comfort. Defensive strength."""
    name: str = field(default="Ramen", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Pizza(AlienPower):
    """Pizza - Power of Sharing. Benefit allies."""
    name: str = field(default="Pizza", init=False)
    description: str = field(default="Allies draw 1 card each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kebab(AlienPower):
    """Kebab - Power of Skewering. Pierce defenses."""
    name: str = field(default="Kebab", init=False)
    description: str = field(default="Ignore 2 defense ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dumpling(AlienPower):
    """Dumpling - Power of Packages. Ships in groups."""
    name: str = field(default="Dumpling", init=False)
    description: str = field(default="Ships count as pairs (+1 per 2 ships).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + (ships // 2)


# ============================================================================
# INGREDIENTS & FLAVORS
# ============================================================================

@dataclass
class Pepper(AlienPower):
    """Pepper - Power of Heat. Increasing intensity."""
    name: str = field(default="Pepper", init=False)
    description: str = field(default="+1 per encounter this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    encounters: int = 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            self.encounters += 1
            return base_total + min(10, self.encounters)
        return base_total


@dataclass
class Salt(AlienPower):
    """Salt - Power of Enhancement. Improve everything."""
    name: str = field(default="Salt", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Sugar(AlienPower):
    """Sugar - Power of Sweetness. Make deals attractive."""
    name: str = field(default="Sugar", init=False)
    description: str = field(default="Negotiations always succeed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Umami(AlienPower):
    """Umami - Power of Depth. Hidden strength."""
    name: str = field(default="Umami", init=False)
    description: str = field(default="+3 that opponent doesn't see until reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Vinegar(AlienPower):
    """Vinegar - Power of Sourness. Reduce opponent."""
    name: str = field(default="Vinegar", init=False)
    description: str = field(default="Opponent's card -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Garlic(AlienPower):
    """Garlic - Power of Repelling. Keep enemies away."""
    name: str = field(default="Garlic", init=False)
    description: str = field(default="Opponents can't ally against you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all cuisine powers
CUISINE_POWERS = [
    Griller, Steamer, Fryer, Smoker, Roaster, Stewer,
    Sushi, Curry, Pasta, Taco, Ramen, Pizza, Kebab, Dumpling,
    Pepper, Salt, Sugar, Umami, Vinegar, Garlic,
]


# Auto-register all powers
for power_class in CUISINE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
