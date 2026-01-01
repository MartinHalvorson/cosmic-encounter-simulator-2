"""
Technology Powers for Cosmic Encounter.

Aliens inspired by technology and computing concepts.
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
# COMPUTING
# ============================================================================

@dataclass
class Algorithm(AlienPower):
    """Algorithm - Power of Logic. Always play optimal card."""
    name: str = field(default="Algorithm", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Debugger(AlienPower):
    """Debugger - Power of Fixing. Redo failed encounters."""
    name: str = field(default="Debugger", init=False)
    description: str = field(default="Retry after losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Encryption(AlienPower):
    """Encryption - Power of Secrecy. Cards can't be seen by others."""
    name: str = field(default="Encryption", init=False)
    description: str = field(default="Hide all card information.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Compiler(AlienPower):
    """Compiler - Power of Translation. Use any card as attack 20."""
    name: str = field(default="Compiler", init=False)
    description: str = field(default="Any card counts as attack 20.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Recursion(AlienPower):
    """Recursion - Power of Loops. +1 for each previous encounter."""
    name: str = field(default="Recursion", init=False)
    description: str = field(default="+1 per previous encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# ELECTRONICS
# ============================================================================

@dataclass
class Transistor(AlienPower):
    """Transistor - Power of Switching. Swap attack and defense values."""
    name: str = field(default="Transistor", init=False)
    description: str = field(default="Swap attack and defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Capacitor(AlienPower):
    """Capacitor - Power of Storage. Store cards for later use."""
    name: str = field(default="Capacitor", init=False)
    description: str = field(default="Save cards for future encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Resistor(AlienPower):
    """Resistor - Power of Blocking. Reduce opponent's total by 3."""
    name: str = field(default="Resistor", init=False)
    description: str = field(default="Reduce opponent by 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Amplifier(AlienPower):
    """Amplifier - Power of Boosting. Double your card value."""
    name: str = field(default="Amplifier", init=False)
    description: str = field(default="Double your card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Oscillator(AlienPower):
    """Oscillator - Power of Cycles. Alternate between +3 and -3."""
    name: str = field(default="Oscillator", init=False)
    description: str = field(default="Alternate +3/-3 each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# INTERNET
# ============================================================================

@dataclass
class Bandwidth(AlienPower):
    """Bandwidth - Power of Capacity. Draw extra cards based on colonies."""
    name: str = field(default="Bandwidth", init=False)
    description: str = field(default="Draw 1 card per 2 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            cards_to_draw = colonies // 2
            if cards_to_draw > 0:
                cards = game.cosmic_deck.draw_multiple(min(cards_to_draw, 3))
                player.add_cards(cards)


@dataclass
class Ping(AlienPower):
    """Ping - Power of Detection. See opponent's top card."""
    name: str = field(default="Ping", init=False)
    description: str = field(default="See opponent's next card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Router(AlienPower):
    """Router - Power of Direction. Send ships to any planet."""
    name: str = field(default="Router", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Proxy(AlienPower):
    """Proxy - Power of Substitution. Use ally's power instead."""
    name: str = field(default="Proxy", init=False)
    description: str = field(default="Borrow ally's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cache(AlienPower):
    """Cache - Power of Memory. Play cards from discard."""
    name: str = field(default="Cache", init=False)
    description: str = field(default="Play cards from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# AI & ROBOTICS
# ============================================================================

@dataclass
class NeuralNet(AlienPower):
    """NeuralNet - Power of Learning. +1 for each win this game."""
    name: str = field(default="NeuralNet", init=False)
    description: str = field(default="+1 for each previous win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sensor_Tech(AlienPower):
    """Sensor - Power of Detection. See all hidden cards."""
    name: str = field(default="Sensor_Tech", init=False)
    description: str = field(default="See all opponent's cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Servo(AlienPower):
    """Servo - Power of Automation. Extra ship actions."""
    name: str = field(default="Servo", init=False)
    description: str = field(default="Move extra ships each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drone_Tech(AlienPower):
    """Drone - Power of Extension. Ships can attack from any colony."""
    name: str = field(default="Drone_Tech", init=False)
    description: str = field(default="Attack from any colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hologram(AlienPower):
    """Hologram - Power of Illusion. Ships appear to be more."""
    name: str = field(default="Hologram", init=False)
    description: str = field(default="Ships count as +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count + base_count  # Double
        return base_count


# Register all aliens
for alien_class in [
    Algorithm, Debugger, Encryption, Compiler, Recursion,
    Transistor, Capacitor, Resistor, Amplifier, Oscillator,
    Bandwidth, Ping, Router, Proxy, Cache,
    NeuralNet, Sensor_Tech, Servo, Drone_Tech, Hologram,
]:
    AlienRegistry.register(alien_class())
