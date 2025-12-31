"""
Climate and Weather themed alien powers for Cosmic Encounter.

Powers based on weather phenomena, climate systems, and atmospheric events.
"""

from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


# ============================================================================
# ATMOSPHERIC ALIENS
# ============================================================================

@dataclass
class Hurricane(AlienPower):
    """Hurricane - Power of the Storm. Scatter opponent's ships when winning."""
    name: str = field(default="Hurricane", init=False)
    description: str = field(default="When you win, scatter losing ships across random planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tornado(AlienPower):
    """Tornado - Power of the Vortex. Pull ships from other planets into encounters."""
    name: str = field(default="Tornado", init=False)
    description: str = field(default="Pull 1 ship from any planet to join your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monsoon(AlienPower):
    """Monsoon - Power of the Deluge. Flood the board with ships during seasonal turns."""
    name: str = field(default="Monsoon", init=False)
    description: str = field(default="Every 4 turns, return all ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Drought(AlienPower):
    """Drought - Power of the Dry. Deplete opponent's hand when they attack you."""
    name: str = field(default="Drought", init=False)
    description: str = field(default="When defending, attacker discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lightning(AlienPower):
    """Lightning - Power of the Strike. Instant damage to opponent's ships."""
    name: str = field(default="Lightning", init=False)
    description: str = field(default="Zap 1 opposing ship to warp before resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thunder(AlienPower):
    """Thunder - Power of the Rumble. Intimidate opponents with loud presence."""
    name: str = field(default="Thunder", init=False)
    description: str = field(default="Opponents commit 1 fewer ship against you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fog(AlienPower):
    """Fog - Power of the Mist. Obscure card values during encounters."""
    name: str = field(default="Fog", init=False)
    description: str = field(default="Opponent doesn't see your card value until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hail(AlienPower):
    """Hail - Power of the Barrage. Chip away at opponent's total."""
    name: str = field(default="Hail", init=False)
    description: str = field(default="Reduce opponent's total by 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Blizzard(AlienPower):
    """Blizzard - Power of the Freeze. Slow down opponents' progress."""
    name: str = field(default="Blizzard", init=False)
    description: str = field(default="Opponents skip 1 regroup phase each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Aurora(AlienPower):
    """Aurora - Power of the Lights. Distract opponents with beauty."""
    name: str = field(default="Aurora", init=False)
    description: str = field(default="Allies join your side for free (no ships needed).", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# CLIMATE ZONE ALIENS
# ============================================================================

@dataclass
class Arctic(AlienPower):
    """Arctic - Power of the Cold. Freeze ships in place."""
    name: str = field(default="Arctic", init=False)
    description: str = field(default="Ships on your planets cannot be moved by other players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tropical(AlienPower):
    """Tropical - Power of the Heat. Accelerate growth."""
    name: str = field(default="Tropical", init=False)
    description: str = field(default="Add 1 ship to any colony at end of each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Desert(AlienPower):
    """Desert - Power of the Waste. Survive with minimal resources."""
    name: str = field(default="Desert", init=False)
    description: str = field(default="You can commit 0 ships to an encounter and still win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tundra(AlienPower):
    """Tundra - Power of the Permafrost. Preserve ships in warp."""
    name: str = field(default="Tundra", init=False)
    description: str = field(default="Your ships in warp can still count for home colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Savanna(AlienPower):
    """Savanna - Power of the Plains. Wide visibility and reach."""
    name: str = field(default="Savanna", init=False)
    description: str = field(default="See all players' hand sizes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rainforest(AlienPower):
    """Rainforest - Power of the Canopy. Rich with resources."""
    name: str = field(default="Rainforest", init=False)
    description: str = field(default="Draw 2 cards instead of 1 during regroup.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# NATURAL PHENOMENON ALIENS
# ============================================================================

@dataclass
class Earthquake(AlienPower):
    """Earthquake - Power of the Tremor. Disrupt established positions."""
    name: str = field(default="Earthquake", init=False)
    description: str = field(default="Once per encounter, move ships between planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Volcano(AlienPower):
    """Volcano - Power of the Eruption. Devastating but infrequent attacks."""
    name: str = field(default="Volcano", init=False)
    description: str = field(default="Once per game, destroy all ships on target planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tsunami(AlienPower):
    """Tsunami - Power of the Wave. Overwhelming force when triggered."""
    name: str = field(default="Tsunami", init=False)
    description: str = field(default="When you win with +10 margin, take extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Avalanche(AlienPower):
    """Avalanche - Power of the Slide. Momentum builds with each victory."""
    name: str = field(default="Avalanche", init=False)
    description: str = field(default="Each win this turn adds +2 to next combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Geyser(AlienPower):
    """Geyser - Power of the Burst. Periodic powerful effects."""
    name: str = field(default="Geyser", init=False)
    description: str = field(default="Every 3 encounters, add +5 to your total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Whirlpool(AlienPower):
    """Whirlpool - Power of the Vortex. Draw opponents in."""
    name: str = field(default="Whirlpool", init=False)
    description: str = field(default="Opponents must ally with you if they ally at all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# SEASONAL ALIENS
# ============================================================================

@dataclass
class Spring(AlienPower):
    """Spring - Power of Renewal. Regrowth and fresh starts."""
    name: str = field(default="Spring", init=False)
    description: str = field(default="Return 2 extra ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Summer(AlienPower):
    """Summer - Power of the Sun. Peak performance."""
    name: str = field(default="Summer", init=False)
    description: str = field(default="Your ships count as +1 each during offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Autumn(AlienPower):
    """Autumn - Power of the Harvest. Gather resources."""
    name: str = field(default="Autumn", init=False)
    description: str = field(default="When you win, draw 1 extra card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Winter(AlienPower):
    """Winter - Power of the Frost. Endurance and survival."""
    name: str = field(default="Winter", init=False)
    description: str = field(default="You lose 1 fewer ship in failed encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Equinox(AlienPower):
    """Equinox - Power of Balance. Equal opportunity."""
    name: str = field(default="Equinox", init=False)
    description: str = field(default="Both players reveal cards simultaneously.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Solstice(AlienPower):
    """Solstice - Power of the Extreme. Maximum or minimum effects."""
    name: str = field(default="Solstice", init=False)
    description: str = field(default="Double your card's value if it's 1-5 or 16-20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all climate powers
CLIMATE_POWERS = [
    Hurricane, Tornado, Monsoon, Drought, Lightning, Thunder, Fog, Hail, Blizzard, Aurora,
    Arctic, Tropical, Desert, Tundra, Savanna, Rainforest,
    Earthquake, Volcano, Tsunami, Avalanche, Geyser, Whirlpool,
    Spring, Summer, Autumn, Winter, Equinox, Solstice,
]
