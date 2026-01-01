"""
Frequency Powers - Vibration and frequency themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Resonator(AlienPower):
    """Resonator - Power of Resonance. +3 always."""
    name: str = field(default="Resonator", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Harmonic(AlienPower):
    """Harmonic - Power of Harmony. +2 per ally."""
    name: str = field(default="Harmonic", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dissonant(AlienPower):
    """Dissonant - Power of Discord. -3 to opponent."""
    name: str = field(default="Dissonant", init=False)
    description: str = field(default="Opponent gets -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Oscillator(AlienPower):
    """Oscillator - Power of Oscillation. Random +/- 4."""
    name: str = field(default="Oscillator", init=False)
    description: str = field(default="Random -4 to +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return max(0, total + random.randint(-4, 4))
        return total


@dataclass
class HighPitch(AlienPower):
    """HighPitch - Power of High Frequency. +4 on offense."""
    name: str = field(default="HighPitch", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class LowPitch(AlienPower):
    """LowPitch - Power of Low Frequency. +4 on defense."""
    name: str = field(default="LowPitch", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Ultrasonic(AlienPower):
    """Ultrasonic - Power of Ultrasound. +5 always."""
    name: str = field(default="Ultrasonic", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Infrasonic(AlienPower):
    """Infrasonic - Power of Infrasound. Ships escape."""
    name: str = field(default="Infrasonic", init=False)
    description: str = field(default="Ships go home not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wavelength(AlienPower):
    """Wavelength - Power of Waves. +2 always."""
    name: str = field(default="Wavelength", init=False)
    description: str = field(default="+2 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Amplitude(AlienPower):
    """Amplitude - Power of Strength. +3 on offense."""
    name: str = field(default="Amplitude", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Modulator(AlienPower):
    """Modulator - Power of Modulation. See opponent card."""
    name: str = field(default="Modulator", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Carrier(AlienPower):
    """Carrier - Power of Carrying. +1 per ship."""
    name: str = field(default="Carrier", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Bandwidth(AlienPower):
    """Bandwidth - Power of Range. Extra card draw."""
    name: str = field(default="Bandwidth", init=False)
    description: str = field(default="Draw extra card each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Static(AlienPower):
    """Static - Power of Interference. -2 to attacker."""
    name: str = field(default="Static", init=False)
    description: str = field(default="Attacker gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sync(AlienPower):
    """Sync - Power of Synchronization. +4 with allies."""
    name: str = field(default="Sync", init=False)
    description: str = field(default="+4 when you have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
FREQUENCY_POWERS = [
    Resonator, Harmonic, Dissonant, Oscillator, HighPitch, LowPitch, Ultrasonic,
    Infrasonic, Wavelength, Amplitude, Modulator, Carrier, Bandwidth, Static, Sync,
]

for power_class in FREQUENCY_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
