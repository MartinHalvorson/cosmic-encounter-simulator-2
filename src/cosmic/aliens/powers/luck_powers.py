"""
Luck Powers - Aliens with fortune and chance abilities.
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
class Blessed(AlienPower):
    """
    Blessed - Divine Favor.
    Win random effects.
    """
    name: str = field(default="Blessed", init=False)
    description: str = field(default="Win random.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chancy(AlienPower):
    """
    Chancy - Take Risks.
    Double or nothing.
    """
    name: str = field(default="Chancy", init=False)
    description: str = field(default="Risk it all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Charmed(AlienPower):
    """
    Charmed - Lucky Life.
    Avoid bad outcomes.
    """
    name: str = field(default="Charmed", init=False)
    description: str = field(default="Avoid bad.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cursed(AlienPower):
    """
    Cursed - Bad Luck Aura.
    Opponent loses random effects.
    """
    name: str = field(default="Cursed", init=False)
    description: str = field(default="Curse opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Destined(AlienPower):
    """
    Destined - Fated Winner.
    Know outcome beforehand.
    """
    name: str = field(default="Destined", init=False)
    description: str = field(default="Know outcome.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fated(AlienPower):
    """
    Fated - Inevitable.
    Control destiny draw.
    """
    name: str = field(default="Fated", init=False)
    description: str = field(default="Control destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fortunate(AlienPower):
    """
    Fortunate - Good Luck.
    Extra rewards.
    """
    name: str = field(default="Fortunate", init=False)
    description: str = field(default="Extra rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jinxed(AlienPower):
    """
    Jinxed - Spread Bad Luck.
    Opponent cards -2.
    """
    name: str = field(default="Jinxed", init=False)
    description: str = field(default="Opponent -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lotto(AlienPower):
    """
    Lotto - Big Win.
    Jackpot on special cards.
    """
    name: str = field(default="Lotto", init=False)
    description: str = field(default="Jackpot chance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lucky_Alt(AlienPower):
    """
    Lucky_Alt - Natural Luck.
    Reroll bad results.
    """
    name: str = field(default="Lucky_Alt", init=False)
    description: str = field(default="Reroll bad.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Odds(AlienPower):
    """
    Odds - Beat the Odds.
    Win unlikely encounters.
    """
    name: str = field(default="Odds", init=False)
    description: str = field(default="Beat odds.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Omen(AlienPower):
    """
    Omen - See Signs.
    Preview cards.
    """
    name: str = field(default="Omen", init=False)
    description: str = field(default="Preview cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Probability(AlienPower):
    """
    Probability - Manipulate Chance.
    Change random results.
    """
    name: str = field(default="Probability", init=False)
    description: str = field(default="Change random.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Risk(AlienPower):
    """
    Risk - High Stakes.
    Gamble for bonus.
    """
    name: str = field(default="Risk", init=False)
    description: str = field(default="Gamble bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Serendipity(AlienPower):
    """
    Serendipity - Happy Accident.
    Gain from mistakes.
    """
    name: str = field(default="Serendipity", init=False)
    description: str = field(default="Gain from loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wager(AlienPower):
    """
    Wager - Bet on Outcome.
    Double stakes.
    """
    name: str = field(default="Wager", init=False)
    description: str = field(default="Double stakes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Blessed())
AlienRegistry.register(Chancy())
AlienRegistry.register(Charmed())
AlienRegistry.register(Cursed())
AlienRegistry.register(Destined())
AlienRegistry.register(Fated())
AlienRegistry.register(Fortunate())
AlienRegistry.register(Jinxed())
AlienRegistry.register(Lotto())
AlienRegistry.register(Lucky_Alt())
AlienRegistry.register(Odds())
AlienRegistry.register(Omen())
AlienRegistry.register(Probability())
AlienRegistry.register(Risk())
AlienRegistry.register(Serendipity())
AlienRegistry.register(Wager())
