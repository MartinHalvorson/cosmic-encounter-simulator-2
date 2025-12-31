"""
Magic Powers - Mystical and spell-themed aliens.
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
class Mage(AlienPower):
    """Mage - Arcane master. +3 when attacking."""
    name: str = field(default="Mage", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Warlock(AlienPower):
    """Warlock - Dark caster. -2 to opponent's total."""
    name: str = field(default="Warlock", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Witch(AlienPower):
    """Witch - Hex caster. Opponent discards after losing."""
    name: str = field(default="Witch", init=False)
    description: str = field(default="Force discard when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spellcaster(AlienPower):
    """Spellcaster - Versatile magic. Play two encounter cards."""
    name: str = field(default="Spellcaster", init=False)
    description: str = field(default="Play two cards summed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Enchanter_Alt(AlienPower):
    """Enchanter Alt - Charm magic. Force one ally to join."""
    name: str = field(default="Enchanter_Alt", init=False)
    description: str = field(default="Compel one ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Summoner(AlienPower):
    """Summoner - Creature caller. +1 per ship committed."""
    name: str = field(default="Summoner", init=False)
    description: str = field(default="+1 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Conjurer(AlienPower):
    """Conjurer - Object creator. Draw card when winning."""
    name: str = field(default="Conjurer", init=False)
    description: str = field(default="Draw card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Necro(AlienPower):
    """Necro - Death magic. Retrieve 2 ships from warp."""
    name: str = field(default="Necro", init=False)
    description: str = field(default="Retrieve 2 ships each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diviner(AlienPower):
    """Diviner - Future sight. See opponent's encounter card."""
    name: str = field(default="Diviner", init=False)
    description: str = field(default="View opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Abjurer(AlienPower):
    """Abjurer - Protection magic. Immune to artifacts."""
    name: str = field(default="Abjurer", init=False)
    description: str = field(default="Immune to artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Evoker(AlienPower):
    """Evoker - Energy magic. +4 when attacking."""
    name: str = field(default="Evoker", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Transmuter(AlienPower):
    """Transmuter - Change magic. Switch attack to negotiate."""
    name: str = field(default="Transmuter", init=False)
    description: str = field(default="Switch card type after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Illusioner(AlienPower):
    """Illusioner - Trick magic. Hide encounter card value."""
    name: str = field(default="Illusioner", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dispeller(AlienPower):
    """Dispeller - Counter magic. Cancel opponent's power."""
    name: str = field(default="Dispeller", init=False)
    description: str = field(default="Cancel opponent's alien power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ritualist(AlienPower):
    """Ritualist - Ceremony magic. +2 per home colony."""
    name: str = field(default="Ritualist", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            home_count = len([p for p in player.home_planets if player.name in p.ships])
            return total + (home_count * 2)
        return total


# Register all powers
AlienRegistry.register(Mage())
AlienRegistry.register(Warlock())
AlienRegistry.register(Witch())
AlienRegistry.register(Spellcaster())
AlienRegistry.register(Enchanter_Alt())
AlienRegistry.register(Summoner())
AlienRegistry.register(Conjurer())
AlienRegistry.register(Necro())
AlienRegistry.register(Diviner())
AlienRegistry.register(Abjurer())
AlienRegistry.register(Evoker())
AlienRegistry.register(Transmuter())
AlienRegistry.register(Illusioner())
AlienRegistry.register(Dispeller())
AlienRegistry.register(Ritualist())
