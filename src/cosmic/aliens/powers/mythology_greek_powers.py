"""
Greek Mythology Powers for Cosmic Encounter.

Aliens inspired by Greek gods and mythological creatures.
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
class Zeus_Alt(AlienPower):
    """Zeus_Alt - Power of Lightning. +4 on offense."""
    name: str = field(default="Zeus_Alt", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Poseidon_Alt(AlienPower):
    """Poseidon_Alt - Power of Seas. +3 on defense."""
    name: str = field(default="Poseidon_Alt", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 3
        return total


@dataclass
class Hades_Alt(AlienPower):
    """Hades_Alt - Power of Underworld. Ships go to your hand as cards."""
    name: str = field(default="Hades_Alt", init=False)
    description: str = field(default="Lost ships become cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Athena_Alt(AlienPower):
    """Athena_Alt - Power of Wisdom. See opponent's card before choosing."""
    name: str = field(default="Athena_Alt", init=False)
    description: str = field(default="See opponent's card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ares_Alt(AlienPower):
    """Ares_Alt - Power of War. +5 but allies cannot join you."""
    name: str = field(default="Ares_Alt", init=False)
    description: str = field(default="+5, no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Apollo_Alt(AlienPower):
    """Apollo_Alt - Power of Light. +2 and see top 3 deck cards."""
    name: str = field(default="Apollo_Alt", init=False)
    description: str = field(default="+2 and see deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Hermes_Alt(AlienPower):
    """Hermes_Alt - Power of Speed. Take second encounter more often."""
    name: str = field(default="Hermes_Alt", init=False)
    description: str = field(default="Second encounter on any win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hera(AlienPower):
    """Hera - Power of Marriage. +2 for each ally ship."""
    name: str = field(default="Hera", init=False)
    description: str = field(default="+2 per ally ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Demeter(AlienPower):
    """Demeter - Power of Harvest. Draw 1 card at turn start."""
    name: str = field(default="Demeter", init=False)
    description: str = field(default="Draw 1 card at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dionysus(AlienPower):
    """Dionysus - Power of Wine. Opponent discards 1 card before reveal."""
    name: str = field(default="Dionysus", init=False)
    description: str = field(default="Opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hephaestus(AlienPower):
    """Hephaestus - Power of Forge. Ships count as 1.5 each."""
    name: str = field(default="Hephaestus", init=False)
    description: str = field(default="Ships count as 1.5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Artemis(AlienPower):
    """Artemis - Power of Hunt. +3 on first encounter of turn."""
    name: str = field(default="Artemis", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return total + 3
        return total


@dataclass
class Persephone(AlienPower):
    """Persephone - Power of Seasons. +4 every other turn."""
    name: str = field(default="Persephone", init=False)
    description: str = field(default="+4 every other turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 4
        return total


@dataclass
class Prometheus_Alt(AlienPower):
    """Prometheus_Alt - Power of Fire. Win ties automatically."""
    name: str = field(default="Prometheus_Alt", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hercules_Alt(AlienPower):
    """Hercules_Alt - Power of Strength. +3 always."""
    name: str = field(default="Hercules_Alt", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


# Register all Greek mythology powers
AlienRegistry.register(Zeus_Alt())
AlienRegistry.register(Poseidon_Alt())
AlienRegistry.register(Hades_Alt())
AlienRegistry.register(Athena_Alt())
AlienRegistry.register(Ares_Alt())
AlienRegistry.register(Apollo_Alt())
AlienRegistry.register(Hermes_Alt())
AlienRegistry.register(Hera())
AlienRegistry.register(Demeter())
AlienRegistry.register(Dionysus())
AlienRegistry.register(Hephaestus())
AlienRegistry.register(Artemis())
AlienRegistry.register(Persephone())
AlienRegistry.register(Prometheus_Alt())
AlienRegistry.register(Hercules_Alt())
