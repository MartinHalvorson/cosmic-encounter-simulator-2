"""
Steampunk themed alien powers for Cosmic Encounter.

Powers based on steampunk aesthetics, Victorian technology, and clockwork.
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
# CLOCKWORK MACHINES
# ============================================================================

@dataclass
class Clockwork(AlienPower):
    """Clockwork - Power of Precision. Reliable timing."""
    name: str = field(default="Clockwork", init=False)
    description: str = field(default="+3 on even-numbered turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return base_total + 3
        return base_total


@dataclass
class Automaton(AlienPower):
    """Automaton - Power of Mechanism. Consistent performance."""
    name: str = field(default="Automaton", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Gear_Master(AlienPower):
    """Gear_Master - Power of Gears. Interconnected bonus."""
    name: str = field(default="Gear_Master", init=False)
    description: str = field(default="+1 per ship involved (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        total_ships = sum(game.offense_ships.values()) + sum(game.defense_ships.values())
        return base_total + min(5, total_ships)


@dataclass
class Cogsworth(AlienPower):
    """Cogsworth - Power of Cogs. Building momentum."""
    name: str = field(default="Cogsworth", init=False)
    description: str = field(default="+1 per 2 turns passed (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = game.current_turn // 2
            return base_total + min(6, bonus)
        return base_total


@dataclass
class Spring_Loaded(AlienPower):
    """Spring_Loaded - Power of Springs. Sudden burst."""
    name: str = field(default="Spring_Loaded", init=False)
    description: str = field(default="+5 but -2 next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    debuff_active: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if self.debuff_active:
            self.debuff_active = False
            return base_total - 2
        if random.random() < 0.4:
            self.debuff_active = True
            return base_total + 5
        return base_total


# ============================================================================
# STEAM TECHNOLOGY
# ============================================================================

@dataclass
class Steam_Engine(AlienPower):
    """Steam_Engine - Power of Steam. Building power."""
    name: str = field(default="Steam_Engine", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(8, game.current_turn)
        return base_total


@dataclass
class Boiler(AlienPower):
    """Boiler - Power of Pressure. Build up pressure."""
    name: str = field(default="Boiler", init=False)
    description: str = field(default="+3 after turn 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn > 5:
            return base_total + 3
        return base_total


@dataclass
class Valve_Master(AlienPower):
    """Valve_Master - Power of Valves. Control flow."""
    name: str = field(default="Valve_Master", init=False)
    description: str = field(default="May reduce any bonus by 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Piston(AlienPower):
    """Piston - Power of Thrust. Powerful attack."""
    name: str = field(default="Piston", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


# ============================================================================
# VICTORIAN ROLES
# ============================================================================

@dataclass
class Inventor(AlienPower):
    """Inventor - Power of Creation. Make new things."""
    name: str = field(default="Inventor", init=False)
    description: str = field(default="Draw extra card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tinkerer(AlienPower):
    """Tinkerer - Power of Modification. Adjust values."""
    name: str = field(default="Tinkerer", init=False)
    description: str = field(default="Your card +1 or -1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Brass_Baron(AlienPower):
    """Brass_Baron - Power of Brass. Industrial might."""
    name: str = field(default="Brass_Baron", init=False)
    description: str = field(default="+3 per colony (max +9).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + min(9, colonies * 3)
        return base_total


@dataclass
class Airship_Captain(AlienPower):
    """Airship_Captain - Power of Flight. Aerial advantage."""
    name: str = field(default="Airship_Captain", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Chronologist(AlienPower):
    """Chronologist - Power of Time. Manipulate timing."""
    name: str = field(default="Chronologist", init=False)
    description: str = field(default="Take extra encounter once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    used: bool = False


@dataclass
class Telegraph(AlienPower):
    """Telegraph - Power of Communication. Know enemy plans."""
    name: str = field(default="Telegraph", init=False)
    description: str = field(default="See opponent's card before you play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# MECHANICAL DEVICES
# ============================================================================

@dataclass
class Gyroscope(AlienPower):
    """Gyroscope - Power of Balance. Stability bonus."""
    name: str = field(default="Gyroscope", init=False)
    description: str = field(default="+3 when you have 2-3 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if 2 <= colonies <= 3:
                return base_total + 3
        return base_total


@dataclass
class Difference_Engine(AlienPower):
    """Difference_Engine - Power of Calculation. Compute bonus."""
    name: str = field(default="Difference_Engine", init=False)
    description: str = field(default="+1 per unique card value in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            unique_values = set()
            for card in player.hand:
                if hasattr(card, 'value'):
                    unique_values.add(card.value)
            return base_total + len(unique_values)
        return base_total


@dataclass
class Turbine(AlienPower):
    """Turbine - Power of Rotation. Spinning power."""
    name: str = field(default="Turbine", init=False)
    description: str = field(default="Random +2 to +6 bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(2, 6)
        return base_total


@dataclass
class Governor(AlienPower):
    """Governor - Power of Regulation. Control limits."""
    name: str = field(default="Governor", init=False)
    description: str = field(default="Card values cannot exceed 15.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all steampunk powers
STEAMPUNK_POWERS = [
    Clockwork, Automaton, Gear_Master, Cogsworth, Spring_Loaded,
    Steam_Engine, Boiler, Valve_Master, Piston,
    Inventor, Tinkerer, Brass_Baron, Airship_Captain, Chronologist, Telegraph,
    Gyroscope, Difference_Engine, Turbine, Governor,
]


# Auto-register all powers
for power_class in STEAMPUNK_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
