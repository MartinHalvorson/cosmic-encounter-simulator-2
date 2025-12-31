"""
Sound Powers - Aliens with audio and vibration abilities.
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
class Bard(AlienPower):
    """
    Bard - Musical Power.
    +2 with allies.
    """
    name: str = field(default="Bard", init=False)
    description: str = field(default="+2 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boomer(AlienPower):
    """
    Boomer - Sonic Boom.
    +4 attack once.
    """
    name: str = field(default="Boomer", init=False)
    description: str = field(default="+4 once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Choir(AlienPower):
    """
    Choir - Harmony.
    Allies +1 each.
    """
    name: str = field(default="Choir", init=False)
    description: str = field(default="Allies +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Deafener(AlienPower):
    """
    Deafener - Block Sound.
    Cancel communication.
    """
    name: str = field(default="Deafener", init=False)
    description: str = field(default="Block communication.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harmonic(AlienPower):
    """
    Harmonic - Resonate.
    Copy ally bonus.
    """
    name: str = field(default="Harmonic", init=False)
    description: str = field(default="Copy ally bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Howler(AlienPower):
    """
    Howler - Loud Cry.
    Opponent -2.
    """
    name: str = field(default="Howler", init=False)
    description: str = field(default="Opponent -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Humming(AlienPower):
    """
    Humming - Constant Tune.
    +1 always.
    """
    name: str = field(default="Humming", init=False)
    description: str = field(default="+1 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +1 always."""
        return total + 1


@dataclass
class Lullaby(AlienPower):
    """
    Lullaby - Sleep Song.
    Skip opponent turn.
    """
    name: str = field(default="Lullaby", init=False)
    description: str = field(default="Skip turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Melody(AlienPower):
    """
    Melody - Sweet Sound.
    Draw extra card.
    """
    name: str = field(default="Melody", init=False)
    description: str = field(default="Draw card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Resonator(AlienPower):
    """
    Resonator - Amplify.
    Double one bonus.
    """
    name: str = field(default="Resonator", init=False)
    description: str = field(default="Double bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Screamer(AlienPower):
    """
    Screamer - Loud Scream.
    Opponent loses ship.
    """
    name: str = field(default="Screamer", init=False)
    description: str = field(default="Remove ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Silencer(AlienPower):
    """
    Silencer - Quiet Zone.
    Cancel power use.
    """
    name: str = field(default="Silencer", init=False)
    description: str = field(default="Cancel power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Singer(AlienPower):
    """
    Singer - Voice Power.
    +3 when main player.
    """
    name: str = field(default="Singer", init=False)
    description: str = field(default="+3 main player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sonar(AlienPower):
    """
    Sonar - Echo Location.
    See hidden cards.
    """
    name: str = field(default="Sonar", init=False)
    description: str = field(default="See hidden.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Vibrator(AlienPower):
    """
    Vibrator - Shake Things.
    Disrupt opponent.
    """
    name: str = field(default="Vibrator", init=False)
    description: str = field(default="Disrupt opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Whisper(AlienPower):
    """
    Whisper - Quiet Voice.
    Secret ally bonus.
    """
    name: str = field(default="Whisper", init=False)
    description: str = field(default="Secret bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Bard())
AlienRegistry.register(Boomer())
AlienRegistry.register(Choir())
AlienRegistry.register(Deafener())
AlienRegistry.register(Harmonic())
AlienRegistry.register(Howler())
AlienRegistry.register(Humming())
AlienRegistry.register(Lullaby())
AlienRegistry.register(Melody())
AlienRegistry.register(Resonator())
AlienRegistry.register(Screamer())
AlienRegistry.register(Silencer())
AlienRegistry.register(Singer())
AlienRegistry.register(Sonar())
AlienRegistry.register(Vibrator())
AlienRegistry.register(Whisper())
