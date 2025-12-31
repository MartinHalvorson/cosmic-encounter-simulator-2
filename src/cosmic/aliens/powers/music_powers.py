"""
Music Powers - Sound and rhythm-themed aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Conductor(AlienPower):
    """Conductor - Orchestra leader. Allies act in your order."""
    name: str = field(default="Conductor", init=False)
    description: str = field(default="Control ally ship commitment order.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Drummer(AlienPower):
    """Drummer - Keeping time. +1 per turn that has passed."""
    name: str = field(default="Drummer", init=False)
    description: str = field(default="+1 per turn in game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Singer(AlienPower):
    """Singer - Captivating voice. Force one player to ally."""
    name: str = field(default="Singer", init=False)
    description: str = field(default="Compel one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Composer(AlienPower):
    """Composer - Creating melody. Rearrange top 5 destiny cards."""
    name: str = field(default="Composer", init=False)
    description: str = field(default="Reorder destiny deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harmonist(AlienPower):
    """Harmonist - Perfect harmony. Allies gain +2 each."""
    name: str = field(default="Harmonist", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Soloist(AlienPower):
    """Soloist - Performing alone. +4 without allies."""
    name: str = field(default="Soloist", init=False)
    description: str = field(default="+4 when no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pianist(AlienPower):
    """Pianist - Key player. Use two encounter cards."""
    name: str = field(default="Pianist", init=False)
    description: str = field(default="Play two encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Violinist(AlienPower):
    """Violinist - Emotional player. +2 when defending."""
    name: str = field(default="Violinist", init=False)
    description: str = field(default="+2 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 2
        return total


@dataclass
class Trumpeter(AlienPower):
    """Trumpeter - Loud announcement. Reveal opponent's card."""
    name: str = field(default="Trumpeter", init=False)
    description: str = field(default="Force opponent to reveal card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cellist(AlienPower):
    """Cellist - Deep tones. +3 when lowest attack card."""
    name: str = field(default="Cellist", init=False)
    description: str = field(default="+3 when playing low card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flutist(AlienPower):
    """Flutist - High notes. +2 when attacking."""
    name: str = field(default="Flutist", init=False)
    description: str = field(default="+2 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 2
        return total


@dataclass
class Bard(AlienPower):
    """Bard - Storyteller. Share rewards with allies."""
    name: str = field(default="Bard", init=False)
    description: str = field(default="Allies draw cards too.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rhythm(AlienPower):
    """Rhythm - Steady beat. +1 per encounter this turn."""
    name: str = field(default="Rhythm", init=False)
    description: str = field(default="+1 per encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.encounter_number
        return total


@dataclass
class Melody(AlienPower):
    """Melody - Beautiful tune. Opponent must accept deals."""
    name: str = field(default="Melody", init=False)
    description: str = field(default="Negotiate deals can't be refused.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Symphony(AlienPower):
    """Symphony - Grand performance. Win encounter to gain 2 colonies."""
    name: str = field(default="Symphony", init=False)
    description: str = field(default="Win for double colony reward.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Conductor())
AlienRegistry.register(Drummer())
AlienRegistry.register(Singer())
AlienRegistry.register(Composer())
AlienRegistry.register(Harmonist())
AlienRegistry.register(Soloist())
AlienRegistry.register(Pianist())
AlienRegistry.register(Violinist())
AlienRegistry.register(Trumpeter())
AlienRegistry.register(Cellist())
AlienRegistry.register(Flutist())
AlienRegistry.register(Bard())
AlienRegistry.register(Rhythm())
AlienRegistry.register(Melody())
AlienRegistry.register(Symphony())
