"""
Concept Powers - Abstract concept-themed aliens.
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
class Truth(AlienPower):
    """Truth - Power of Honesty. All cards visible."""
    name: str = field(default="Truth", init=False)
    description: str = field(default="All encounter cards revealed immediately.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lie(AlienPower):
    """Lie - Power of Deception. Fake card values."""
    name: str = field(default="Lie", init=False)
    description: str = field(default="Announce false card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Justice(AlienPower):
    """Justice - Power of Balance. Equal totals tie."""
    name: str = field(default="Justice", init=False)
    description: str = field(default="Win when totals are within 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mercy(AlienPower):
    """Mercy - Power of Compassion. Spare losing ships."""
    name: str = field(default="Mercy", init=False)
    description: str = field(default="Opponent loses 1 fewer ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chaos_Alt(AlienPower):
    """Chaos_Alt - Power of Disorder. Random effects."""
    name: str = field(default="Chaos_Alt", init=False)
    description: str = field(default="Random +/- 1-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return max(0, total + random.randint(-8, 8))
        return total


@dataclass
class Order(AlienPower):
    """Order - Power of Structure. Predictable +3."""
    name: str = field(default="Order", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Fear(AlienPower):
    """Fear - Power of Terror. Opponents flee."""
    name: str = field(default="Fear", init=False)
    description: str = field(default="Opponent commits 1 less ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Courage(AlienPower):
    """Courage - Power of Bravery. +2 when outnumbered."""
    name: str = field(default="Courage", init=False)
    description: str = field(default="+2 when facing more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hope(AlienPower):
    """Hope - Power of Optimism. +4 when losing."""
    name: str = field(default="Hope", init=False)
    description: str = field(default="+4 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Despair(AlienPower):
    """Despair - Power of Doom. -2 to opponent."""
    name: str = field(default="Despair", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pride(AlienPower):
    """Pride - Power of Ego. +3 when leading."""
    name: str = field(default="Pride", init=False)
    description: str = field(default="+3 when ahead in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Humility(AlienPower):
    """Humility - Power of Modesty. Bonus from low cards."""
    name: str = field(default="Humility", init=False)
    description: str = field(default="+5 when playing card under 8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Knowledge(AlienPower):
    """Knowledge - Power of Learning. See deck."""
    name: str = field(default="Knowledge", init=False)
    description: str = field(default="Look at top 5 cards of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ignorance(AlienPower):
    """Ignorance - Power of Unknowing. Hide information."""
    name: str = field(default="Ignorance", init=False)
    description: str = field(default="Opponent can't see your hand size.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Freedom(AlienPower):
    """Freedom - Power of Liberty. Escape encounters."""
    name: str = field(default="Freedom", init=False)
    description: str = field(default="Withdraw from encounter anytime.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oppression(AlienPower):
    """Oppression - Power of Control. Lock opponent."""
    name: str = field(default="Oppression", init=False)
    description: str = field(default="Opponent cannot ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Patience(AlienPower):
    """Patience - Power of Waiting. +1 each turn."""
    name: str = field(default="Patience", init=False)
    description: str = field(default="+1 per turn passed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Haste(AlienPower):
    """Haste - Power of Speed. Early reveal bonus."""
    name: str = field(default="Haste", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Peace(AlienPower):
    """Peace - Power of Calm. Bonus when negotiating."""
    name: str = field(default="Peace", init=False)
    description: str = field(default="+2 cards when dealing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class War(AlienPower):
    """War - Power of Conflict. +3 always."""
    name: str = field(default="War", init=False)
    description: str = field(default="+3 in all combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


# Register all powers
CONCEPT_POWERS = [
    Truth, Lie, Justice, Mercy, Chaos_Alt, Order, Fear, Courage, Hope, Despair,
    Pride, Humility, Knowledge, Ignorance, Freedom, Oppression, Patience, Haste, Peace, War,
]

for power_class in CONCEPT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
