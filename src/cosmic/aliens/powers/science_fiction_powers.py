"""
Science Fiction themed alien powers for Cosmic Encounter.

Powers based on sci-fi concepts, technology, and tropes.
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
# SPACE TRAVEL
# ============================================================================

@dataclass
class Warp_Drive(AlienPower):
    """Warp_Drive - Power of FTL. Faster than light."""
    name: str = field(default="Warp_Drive", init=False)
    description: str = field(default="Attack any planet regardless of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hyperdrive(AlienPower):
    """Hyperdrive - Power of Speed. Lightning fast."""
    name: str = field(default="Hyperdrive", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Teleporter(AlienPower):
    """Teleporter - Power of Transport. Instant movement."""
    name: str = field(default="Teleporter_SF", init=False)
    description: str = field(default="Move ships freely between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stasis_Pod(AlienPower):
    """Stasis_Pod - Power of Preservation. Frozen in time."""
    name: str = field(default="Stasis_Pod", init=False)
    description: str = field(default="Ships can't be destroyed, only sent to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# WEAPONS
# ============================================================================

@dataclass
class Laser_Cannon(AlienPower):
    """Laser_Cannon - Power of Precision. Accurate strikes."""
    name: str = field(default="Laser_Cannon", init=False)
    description: str = field(default="+4 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Plasma_Rifle(AlienPower):
    """Plasma_Rifle - Power of Heat. Burning damage."""
    name: str = field(default="Plasma_Rifle", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Ion_Blaster(AlienPower):
    """Ion_Blaster - Power of Disruption. Disable opponents."""
    name: str = field(default="Ion_Blaster", init=False)
    description: str = field(default="Opponent's card -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Photon_Torpedo(AlienPower):
    """Photon_Torpedo - Power of Destruction. Massive damage."""
    name: str = field(default="Photon_Torpedo", init=False)
    description: str = field(default="+6 once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    used: bool = False

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and not self.used:
            if random.random() < 0.3:
                self.used = True
                return base_total + 6
        return base_total


# ============================================================================
# TECHNOLOGY
# ============================================================================

@dataclass
class Force_Field_SF(AlienPower):
    """Force_Field_SF - Power of Shields. Defensive barrier."""
    name: str = field(default="Force_Field_SF", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Cloaking_Device(AlienPower):
    """Cloaking_Device - Power of Invisibility. Hide your plans."""
    name: str = field(default="Cloaking_Device", init=False)
    description: str = field(default="Opponent can't see your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tractor_Beam(AlienPower):
    """Tractor_Beam - Power of Pull. Force engagement."""
    name: str = field(default="Tractor_Beam", init=False)
    description: str = field(default="Opponent must commit all ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scanner(AlienPower):
    """Scanner - Power of Detection. See all."""
    name: str = field(default="Scanner_SF", init=False)
    description: str = field(default="See opponent's hand before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# SCI-FI TROPES
# ============================================================================

@dataclass
class Hive_Mind(AlienPower):
    """Hive_Mind - Power of Unity. Collective strength."""
    name: str = field(default="Hive_Mind", init=False)
    description: str = field(default="+2 per ship (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + min(10, ships * 2)


@dataclass
class Android_SF(AlienPower):
    """Android_SF - Power of Precision. Perfect execution."""
    name: str = field(default="Android_SF", init=False)
    description: str = field(default="+3 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Time_Traveler(AlienPower):
    """Time_Traveler - Power of Temporal. Manipulate time."""
    name: str = field(default="Time_Traveler", init=False)
    description: str = field(default="Take extra encounter once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    used: bool = False


@dataclass
class Alien_Queen(AlienPower):
    """Alien_Queen - Power of Command. Lead the swarm."""
    name: str = field(default="Alien_Queen", init=False)
    description: str = field(default="+3 per ally (max +9).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + min(9, allies * 3)


@dataclass
class Space_Marine(AlienPower):
    """Space_Marine - Power of Combat. Elite soldier."""
    name: str = field(default="Space_Marine", init=False)
    description: str = field(default="+4 in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Starship_Captain(AlienPower):
    """Starship_Captain - Power of Leadership. Command bonus."""
    name: str = field(default="Starship_Captain", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


# Register all science fiction powers
SCIENCE_FICTION_POWERS = [
    Warp_Drive, Hyperdrive, Teleporter, Stasis_Pod,
    Laser_Cannon, Plasma_Rifle, Ion_Blaster, Photon_Torpedo,
    Force_Field_SF, Cloaking_Device, Tractor_Beam, Scanner,
    Hive_Mind, Android_SF, Time_Traveler, Alien_Queen, Space_Marine, Starship_Captain,
]


# Auto-register all powers
for power_class in SCIENCE_FICTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
