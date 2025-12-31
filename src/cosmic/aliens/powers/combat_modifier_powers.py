"""
Combat Modifier themed alien powers for Cosmic Encounter.

Powers that directly modify combat totals in various ways.
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
# FLAT COMBAT BONUSES
# ============================================================================

@dataclass
class Veteran(AlienPower):
    """Veteran - Power of Experience. Steady combat bonus."""
    name: str = field(default="Veteran", init=False)
    description: str = field(default="+3 to all combat totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add flat +3 bonus."""
        if not player.power_active:
            return base_total
        return base_total + 3


@dataclass
class Champion(AlienPower):
    """Champion - Power of Victory. Bonus when ahead."""
    name: str = field(default="Champion", init=False)
    description: str = field(default="+4 when you have more colonies than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add bonus when winning."""
        if not player.power_active:
            return base_total

        my_colonies = player.count_foreign_colonies(game.planets)

        # Find opponent
        opponent = game.defense if player == game.offense else game.offense
        opp_colonies = opponent.count_foreign_colonies(game.planets) if opponent else 0

        if my_colonies > opp_colonies:
            return base_total + 4
        return base_total


@dataclass
class Defender(AlienPower):
    """Defender - Power of the Wall. Bonus when defending."""
    name: str = field(default="Defender", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add defense bonus."""
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Aggressor(AlienPower):
    """Aggressor - Power of the Attack. Bonus when attacking."""
    name: str = field(default="Aggressor", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add attack bonus."""
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 5
        return base_total


# ============================================================================
# SCALING COMBAT BONUSES
# ============================================================================

@dataclass
class Swarm(AlienPower):
    """Swarm - Power of Numbers. +2 per ship in encounter."""
    name: str = field(default="Swarm", init=False)
    description: str = field(default="+2 per ship you have in the encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Scale bonus with ships."""
        if not player.power_active:
            return base_total

        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)

        return base_total + (ships * 2)


@dataclass
class Cardmaster(AlienPower):
    """Cardmaster - Power of the Hand. +1 per card in hand."""
    name: str = field(default="Cardmaster", init=False)
    description: str = field(default="+1 per card in your hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Scale with hand size."""
        if not player.power_active:
            return base_total
        return base_total + len(player.hand)


@dataclass
class Warlord(AlienPower):
    """Warlord - Power of Conquest. +2 per foreign colony."""
    name: str = field(default="Warlord", init=False)
    description: str = field(default="+2 per foreign colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Scale with colonies."""
        if not player.power_active:
            return base_total
        colonies = player.count_foreign_colonies(game.planets)
        return base_total + (colonies * 2)


@dataclass
class Desperado(AlienPower):
    """Desperado - Power of the Underdog. Bonus when behind."""
    name: str = field(default="Desperado", init=False)
    description: str = field(default="+8 when you have fewer colonies than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add bonus when losing."""
        if not player.power_active:
            return base_total

        my_colonies = player.count_foreign_colonies(game.planets)

        opponent = game.defense if player == game.offense else game.offense
        opp_colonies = opponent.count_foreign_colonies(game.planets) if opponent else 0

        if my_colonies < opp_colonies:
            return base_total + 8
        return base_total


# ============================================================================
# OPPONENT DEBUFFS
# ============================================================================

@dataclass
class Suppressor(AlienPower):
    """Suppressor - Power of the Dampen. Reduce opponent's total."""
    name: str = field(default="Suppressor", init=False)
    description: str = field(default="Opponent's total is reduced by 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nullifier(AlienPower):
    """Nullifier - Power of the Void. Negate opponent bonuses."""
    name: str = field(default="Nullifier", init=False)
    description: str = field(default="Opponent cannot use power bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Intimidator(AlienPower):
    """Intimidator - Power of Fear. Reduce opponent's ships."""
    name: str = field(default="Intimidator", init=False)
    description: str = field(default="Opponent's ships count as -1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# CONDITIONAL COMBAT POWERS
# ============================================================================

@dataclass
class Perfectionist(AlienPower):
    """Perfectionist - Power of Precision. Bonus for exact values."""
    name: str = field(default="Perfectionist", init=False)
    description: str = field(default="+6 if your card is exactly 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Extremist(AlienPower):
    """Extremist - Power of the Edge. Bonus for edge values."""
    name: str = field(default="Extremist", init=False)
    description: str = field(default="+5 if your card is 1-4 or 16-20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gambler(AlienPower):
    """Gambler - Power of Chance. Random bonus or penalty."""
    name: str = field(default="Gambler", init=False)
    description: str = field(default="Randomly add or subtract 1-6 from total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Random modifier."""
        if not player.power_active:
            return base_total
        modifier = random.randint(-6, 6)
        return max(0, base_total + modifier)


@dataclass
class Momentum(AlienPower):
    """Momentum - Power of the Streak. Bonus for consecutive wins."""
    name: str = field(default="Momentum", init=False)
    description: str = field(default="+3 per consecutive win this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Berserker(AlienPower):
    """Berserker - Power of Rage. Stronger when losing ships."""
    name: str = field(default="Berserker", init=False)
    description: str = field(default="+3 per ship you've lost this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Scale with ships lost."""
        if not player.power_active:
            return base_total
        ships_lost = player.ships_in_warp
        return base_total + (ships_lost * 3)


# Register all combat modifier powers
COMBAT_MODIFIER_POWERS = [
    Veteran, Champion, Defender, Aggressor,
    Swarm, Cardmaster, Warlord, Desperado,
    Suppressor, Nullifier, Intimidator,
    Perfectionist, Extremist, Gambler, Momentum, Berserker,
]


# Auto-register all powers
for power_class in COMBAT_MODIFIER_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
