"""
Emotion Powers - Feeling and sentiment-themed aliens.
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
class Rage(AlienPower):
    """Rage - Unbridled anger. +5 when attacking."""
    name: str = field(default="Rage", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Fear(AlienPower):
    """Fear - Terrifying presence. Opponent plays lowest card."""
    name: str = field(default="Fear_Alt", init=False)
    description: str = field(default="Force opponent's lowest card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Joy(AlienPower):
    """Joy - Infectious happiness. All allies gain +1."""
    name: str = field(default="Joy", init=False)
    description: str = field(default="+1 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sorrow(AlienPower):
    """Sorrow - Deep sadness. Opponent loses 1 ship when you lose."""
    name: str = field(default="Sorrow", init=False)
    description: str = field(default="Opponent loses ship when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hope(AlienPower):
    """Hope - Eternal optimist. Draw card when losing encounter."""
    name: str = field(default="Hope", init=False)
    description: str = field(default="Draw card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Despair(AlienPower):
    """Despair - Crushing hopelessness. -3 to opponent's total."""
    name: str = field(default="Despair", init=False)
    description: str = field(default="-3 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pride(AlienPower):
    """Pride - Confident strength. +3 when ahead in colonies."""
    name: str = field(default="Pride", init=False)
    description: str = field(default="+3 when leading.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Envy(AlienPower):
    """Envy - Jealous desire. Copy opponent's card value."""
    name: str = field(default="Envy", init=False)
    description: str = field(default="Match opponent's card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Greed(AlienPower):
    """Greed - Insatiable want. Draw 2 cards when winning."""
    name: str = field(default="Greed_Alt", init=False)
    description: str = field(default="Draw 2 cards on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Love(AlienPower):
    """Love - Binding emotion. Allies can't refuse your invitation."""
    name: str = field(default="Love", init=False)
    description: str = field(default="Force ally acceptance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hate(AlienPower):
    """Hate - Bitter enemy. +4 against specific opponent."""
    name: str = field(default="Hate", init=False)
    description: str = field(default="+4 vs chosen nemesis.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Calm(AlienPower):
    """Calm - Inner peace. Ignore kickers."""
    name: str = field(default="Calm", init=False)
    description: str = field(default="Ignore opponent's kickers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Anxiety(AlienPower):
    """Anxiety - Nervous energy. +2 when behind in colonies."""
    name: str = field(default="Anxiety", init=False)
    description: str = field(default="+2 when trailing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Courage(AlienPower):
    """Courage - Brave spirit. +3 when outnumbered."""
    name: str = field(default="Courage", init=False)
    description: str = field(default="+3 when fewer ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trust(AlienPower):
    """Trust - Faithful bond. Allies get +2."""
    name: str = field(default="Trust", init=False)
    description: str = field(default="Allied ships +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Rage())
AlienRegistry.register(Fear())
AlienRegistry.register(Joy())
AlienRegistry.register(Sorrow())
AlienRegistry.register(Hope())
AlienRegistry.register(Despair())
AlienRegistry.register(Pride())
AlienRegistry.register(Envy())
AlienRegistry.register(Greed())
AlienRegistry.register(Love())
AlienRegistry.register(Hate())
AlienRegistry.register(Calm())
AlienRegistry.register(Anxiety())
AlienRegistry.register(Courage())
AlienRegistry.register(Trust())
