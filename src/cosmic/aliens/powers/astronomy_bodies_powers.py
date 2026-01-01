"""
Astronomical bodies themed alien powers.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Red_Dwarf(AlienPower):
    name: str = field(default="Red_Dwarf", init=False)
    description: str = field(default="+2 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class White_Dwarf(AlienPower):
    name: str = field(default="White_Dwarf", init=False)
    description: str = field(default="+3 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Blue_Giant(AlienPower):
    name: str = field(default="Blue_Giant", init=False)
    description: str = field(default="+6 but -1 per turn (min 0).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + max(0, 6 - game.current_turn)
        return base_total


@dataclass
class Red_Giant(AlienPower):
    name: str = field(default="Red_Giant", init=False)
    description: str = field(default="+5 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return base_total + 5
        return base_total


@dataclass
class Neutron_Star(AlienPower):
    name: str = field(default="Neutron_Star", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Pulsar(AlienPower):
    name: str = field(default="Pulsar", init=False)
    description: str = field(default="+3 on turn % 3 == 0.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 3 == 0:
            return base_total + 3
        return base_total


@dataclass
class Magnetar(AlienPower):
    name: str = field(default="Magnetar", init=False)
    description: str = field(default="+5 vs opponents with 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Binary_Star(AlienPower):
    name: str = field(default="Binary_Star", init=False)
    description: str = field(default="+2 x 2 = +4 flat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Protostar(AlienPower):
    name: str = field(default="Protostar", init=False)
    description: str = field(default="+1 per turn (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(game.current_turn, 5)
        return base_total


@dataclass
class Supergiant(AlienPower):
    name: str = field(default="Supergiant", init=False)
    description: str = field(default="+7 flat bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 7
        return base_total


@dataclass
class Hypergiant(AlienPower):
    name: str = field(default="Hypergiant", init=False)
    description: str = field(default="+8 but random -0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 8 - random.randint(0, 3)
        return base_total


@dataclass
class Dwarf_Planet(AlienPower):
    name: str = field(default="Dwarf_Planet", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = len([p for p in player.home_planets if len(p.ships) > 0])
            return base_total + colonies * 2
        return base_total


@dataclass
class Gas_Giant(AlienPower):
    name: str = field(default="Gas_Giant", init=False)
    description: str = field(default="+5 when you have 4+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 4:
            return base_total + 5
        return base_total


@dataclass
class Ice_Giant(AlienPower):
    name: str = field(default="Ice_Giant", init=False)
    description: str = field(default="+4 when alone (no allies).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            no_allies = len(getattr(game, 'offense_allies', [])) == 0 and len(getattr(game, 'defense_allies', [])) == 0
            if no_allies:
                return base_total + 4
        return base_total


@dataclass
class Terrestrial(AlienPower):
    name: str = field(default="Terrestrial", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Rogue_Planet(AlienPower):
    name: str = field(default="Rogue_Planet", init=False)
    description: str = field(default="Random +1-6.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + random.randint(1, 6)
        return base_total


@dataclass
class Trojan_Asteroid(AlienPower):
    name: str = field(default="Trojan_Asteroid", init=False)
    description: str = field(default="+3 with allies, +1 without.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            has_allies = len(getattr(game, 'offense_allies', [])) > 0 or len(getattr(game, 'defense_allies', [])) > 0
            return base_total + (3 if has_allies else 1)
        return base_total


@dataclass
class Kuiper_Belt(AlienPower):
    name: str = field(default="Kuiper_Belt", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + player.count_foreign_colonies()
        return base_total


@dataclass
class Oort_Cloud(AlienPower):
    name: str = field(default="Oort_Cloud", init=False)
    description: str = field(default="+5 at edge of game (turn 8+).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.current_turn >= 8:
            return base_total + 5
        return base_total


ASTRONOMY_BODIES_POWERS = [
    Red_Dwarf, White_Dwarf, Blue_Giant, Red_Giant, Neutron_Star,
    Pulsar, Magnetar, Binary_Star, Protostar, Supergiant,
    Hypergiant, Dwarf_Planet, Gas_Giant, Ice_Giant, Terrestrial,
    Rogue_Planet, Trojan_Asteroid, Kuiper_Belt, Oort_Cloud,
]

for power_class in ASTRONOMY_BODIES_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
