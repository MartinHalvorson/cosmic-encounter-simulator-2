"""
Extended Astronomy themed alien powers for Cosmic Encounter.

Powers based on celestial objects, space phenomena, and astronomical concepts.
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
# STARS
# ============================================================================

@dataclass
class RedGiant(AlienPower):
    """RedGiant - Power of Expansion. Grow larger over time."""
    name: str = field(default="RedGiant", init=False)
    description: str = field(default="+1 per turn (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class WhiteDwarf(AlienPower):
    """WhiteDwarf - Power of Density. Small but powerful."""
    name: str = field(default="WhiteDwarf", init=False)
    description: str = field(default="+4 when you have fewer ships than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            opp_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
        if my_ships < opp_ships:
            return base_total + 4
        return base_total


@dataclass
class NeutronStar(AlienPower):
    """NeutronStar - Power of Magnetism. Pull ships in."""
    name: str = field(default="NeutronStar", init=False)
    description: str = field(default="Opponent must commit all available ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class BlackHole(AlienPower):
    """BlackHole - Power of Absorption. Consume everything."""
    name: str = field(default="BlackHole", init=False)
    description: str = field(default="Ships lost against you are removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Pulsar(AlienPower):
    """Pulsar - Power of Rhythm. Regular bursts."""
    name: str = field(default="Pulsar", init=False)
    description: str = field(default="+5 on odd-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 5
        return base_total


@dataclass
class BlueStar(AlienPower):
    """BlueStar - Power of Youth. Strong early game."""
    name: str = field(default="BlueStar", init=False)
    description: str = field(default="+6 in first 5 turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn <= 5:
            return base_total + 6
        return base_total


# ============================================================================
# GALAXIES
# ============================================================================

@dataclass
class Spiral(AlienPower):
    """Spiral - Power of Motion. Constant movement."""
    name: str = field(default="Spiral", init=False)
    description: str = field(default="Move 1 ship between planets each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Elliptical(AlienPower):
    """Elliptical - Power of Order. Predictable patterns."""
    name: str = field(default="Elliptical", init=False)
    description: str = field(default="Know destiny before it's drawn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Irregular(AlienPower):
    """Irregular - Power of Chaos. Random bonuses."""
    name: str = field(default="Irregular", init=False)
    description: str = field(default="Random +1 to +8 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 8)
        return base_total


@dataclass
class Dwarf_Galaxy(AlienPower):
    """Dwarf_Galaxy - Power of Smallness. Small but effective."""
    name: str = field(default="Dwarf_Galaxy", init=False)
    description: str = field(default="+3 when you have 2 or fewer colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies <= 2:
                return base_total + 3
        return base_total


# ============================================================================
# SPACE PHENOMENA
# ============================================================================

@dataclass
class Supernova(AlienPower):
    """Supernova - Power of Explosion. Massive damage."""
    name: str = field(default="Supernova", init=False)
    description: str = field(default="Once per game: +15 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    used: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and not self.used:
            if random.random() < 0.3:  # 30% chance to use
                self.used = True
                return base_total + 15
        return base_total


@dataclass
class GammaRay(AlienPower):
    """GammaRay - Power of Penetration. Pierce defenses."""
    name: str = field(default="GammaRay", init=False)
    description: str = field(default="Your attacks ignore reinforcements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class SolarFlare(AlienPower):
    """SolarFlare - Power of Burst. Temporary strength."""
    name: str = field(default="SolarFlare", init=False)
    description: str = field(default="+6 but -3 next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    debuff_active: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if self.debuff_active:
            self.debuff_active = False
            return base_total - 3
        if random.random() < 0.4:
            self.debuff_active = True
            return base_total + 6
        return base_total


@dataclass
class Asteroid(AlienPower):
    """Asteroid - Power of Impact. Collision damage."""
    name: str = field(default="Asteroid_Power", init=False)
    description: str = field(default="On win, opponent loses 1 extra ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class DarkMatter(AlienPower):
    """DarkMatter - Power of the Unseen. Hidden strength."""
    name: str = field(default="DarkMatter", init=False)
    description: str = field(default="+4 that isn't revealed until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Wormhole(AlienPower):
    """Wormhole - Power of Transit. Instant travel."""
    name: str = field(default="Wormhole", init=False)
    description: str = field(default="Attack any planet, ignoring destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class CosmicDust(AlienPower):
    """CosmicDust - Power of Obscurity. Hide your plans."""
    name: str = field(default="CosmicDust", init=False)
    description: str = field(default="Opponent can't see your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class DarkEnergy(AlienPower):
    """DarkEnergy - Power of Expansion. Growing influence."""
    name: str = field(default="DarkEnergy", init=False)
    description: str = field(default="+2 per foreign colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


# Register all extended astronomy powers
ASTRONOMY_EXTENDED_POWERS = [
    RedGiant, WhiteDwarf, NeutronStar, BlackHole, Pulsar, BlueStar,
    Spiral, Elliptical, Irregular, Dwarf_Galaxy,
    Supernova, GammaRay, SolarFlare, Asteroid, DarkMatter,
    Wormhole, CosmicDust, DarkEnergy,
]


# Auto-register all powers
for power_class in ASTRONOMY_EXTENDED_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
