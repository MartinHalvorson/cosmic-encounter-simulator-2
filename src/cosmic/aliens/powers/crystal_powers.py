"""
Crystal Powers for Cosmic Encounter.

Aliens inspired by crystals and crystalline structures.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Prism(AlienPower):
    """Prism - Power of Light. +2 per ship in encounter."""
    name: str = field(default="Prism", init=False)
    description: str = field(default="+2 per ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Geode(AlienPower):
    """Geode - Power of Hidden. +4 on defense."""
    name: str = field(default="Geode", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Crystal_Ball(AlienPower):
    """Crystal_Ball - Power of Foresight. See opponent's card before choosing."""
    name: str = field(default="Crystal_Ball", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Shard(AlienPower):
    """Shard - Power of Sharpness. +3 on offense."""
    name: str = field(default="Shard", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Lattice(AlienPower):
    """Lattice - Power of Structure. +1 per colony you have."""
    name: str = field(default="Lattice", init=False)
    description: str = field(default="+1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return total + colonies
        return total


@dataclass
class Facet(AlienPower):
    """Facet - Power of Reflection. Copy opponent's power for encounter."""
    name: str = field(default="Facet", init=False)
    description: str = field(default="Copy opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Matrix(AlienPower):
    """Matrix - Power of Formation. Allies get +2 each."""
    name: str = field(default="Matrix", init=False)
    description: str = field(default="Allies get +2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Refraction(AlienPower):
    """Refraction - Power of Bending. -2 to opponent's total."""
    name: str = field(default="Refraction", init=False)
    description: str = field(default="-2 to opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cluster(AlienPower):
    """Cluster - Power of Grouping. May commit up to 6 ships."""
    name: str = field(default="Cluster", init=False)
    description: str = field(default="Commit up to 6 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Clarity(AlienPower):
    """Clarity - Power of Seeing. See top 3 deck cards."""
    name: str = field(default="Clarity", init=False)
    description: str = field(default="See top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fracture(AlienPower):
    """Fracture - Power of Breaking. Opponent discards 1 card."""
    name: str = field(default="Fracture", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Resonance(AlienPower):
    """Resonance - Power of Vibration. Win ties automatically."""
    name: str = field(default="Resonance", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Growth_Crystal(AlienPower):
    """Growth_Crystal - Power of Growth. Draw 1 card when winning."""
    name: str = field(default="Growth_Crystal", init=False)
    description: str = field(default="Draw 1 card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Formation(AlienPower):
    """Formation - Power of Building. +3 always."""
    name: str = field(default="Formation", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Transparency(AlienPower):
    """Transparency - Power of Invisibility. Ships return home, not warp."""
    name: str = field(default="Transparency", init=False)
    description: str = field(default="Ships go home, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all crystal powers
AlienRegistry.register(Prism())
AlienRegistry.register(Geode())
AlienRegistry.register(Crystal_Ball())
AlienRegistry.register(Shard())
AlienRegistry.register(Lattice())
AlienRegistry.register(Facet())
AlienRegistry.register(Matrix())
AlienRegistry.register(Refraction())
AlienRegistry.register(Cluster())
AlienRegistry.register(Clarity())
AlienRegistry.register(Fracture())
AlienRegistry.register(Resonance())
AlienRegistry.register(Growth_Crystal())
AlienRegistry.register(Formation())
AlienRegistry.register(Transparency())
