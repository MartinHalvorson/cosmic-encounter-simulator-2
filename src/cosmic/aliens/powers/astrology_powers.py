"""
Astrology-themed alien powers for Cosmic Encounter.

Powers inspired by astrological concepts and celestial bodies.
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
class Astrologer(AlienPower):
    """Astrologer - Power of Reading. Predict outcomes."""
    name: str = field(default="Astrologer", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Horoscope(AlienPower):
    """Horoscope - Power of Fortune. Luck-based bonus."""
    name: str = field(default="Horoscope", init=False)
    description: str = field(default="+3 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 3
        return base_total


@dataclass
class Ascendant(AlienPower):
    """Ascendant - Power of Rising. Early game strength."""
    name: str = field(default="Ascendant", init=False)
    description: str = field(default="+5 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 5
        return base_total


@dataclass
class Descendant(AlienPower):
    """Descendant - Power of Setting. Late game strength."""
    name: str = field(default="Descendant", init=False)
    description: str = field(default="+2 per turn after turn 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 5:
            bonus = (game.current_turn - 5) * 2
            return base_total + min(10, bonus)
        return base_total


@dataclass
class House(AlienPower):
    """House - Power of Domain. Control territory."""
    name: str = field(default="House", init=False)
    description: str = field(default="+4 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 4
        return base_total


@dataclass
class Transit(AlienPower):
    """Transit - Power of Passage. Movement bonus."""
    name: str = field(default="Transit", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Conjunction(AlienPower):
    """Conjunction - Power of Alignment. Ally bonus."""
    name: str = field(default="Conjunction", init=False)
    description: str = field(default="+3 per ally.", init=False)
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
        return base_total + (allies * 3)


@dataclass
class Opposition(AlienPower):
    """Opposition - Power of Contrast. Strength vs opponents."""
    name: str = field(default="Opposition", init=False)
    description: str = field(default="+1 per opponent ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            opp_ships = sum(game.defense_ships.values())
        else:
            opp_ships = sum(game.offense_ships.values())
        return base_total + opp_ships


@dataclass
class Trine(AlienPower):
    """Trine - Power of Harmony. +3 with 3 ships."""
    name: str = field(default="Trine", init=False)
    description: str = field(default="+3 with exactly 3 ships.", init=False)
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
        if ships == 3:
            return base_total + 3
        return base_total


@dataclass
class Square(AlienPower):
    """Square - Power of Challenge. +4 with 4 ships."""
    name: str = field(default="Square", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
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
        if ships >= 4:
            return base_total + 4
        return base_total


@dataclass
class Sextile(AlienPower):
    """Sextile - Power of Opportunity. Good timing."""
    name: str = field(default="Sextile", init=False)
    description: str = field(default="+2 offense, +2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Retrograde(AlienPower):
    """Retrograde - Power of Return. Ships come back."""
    name: str = field(default="Retrograde", init=False)
    description: str = field(default="Return 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Natal(AlienPower):
    """Natal - Power of Birth. Starting strength."""
    name: str = field(default="Natal", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 5
        return base_total


@dataclass
class Cusp(AlienPower):
    """Cusp - Power of Transition. Between states."""
    name: str = field(default="Cusp", init=False)
    description: str = field(default="+3 with 2 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies == 2:
                return base_total + 3
        return base_total


# Register all astrology powers
ASTROLOGY_POWERS = [
    Astrologer, Horoscope, Ascendant, Descendant, House,
    Transit, Conjunction, Opposition, Trine, Square,
    Sextile, Retrograde, Natal, Cusp,
]

for power_class in ASTROLOGY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
