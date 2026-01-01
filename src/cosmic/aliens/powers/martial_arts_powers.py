"""
Martial arts themed alien powers for Cosmic Encounter.

Powers inspired by combat disciplines and fighting styles.
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
class Judoka(AlienPower):
    """Judoka - Power of Throws. Use opponent's strength."""
    name: str = field(default="Judoka", init=False)
    description: str = field(default="+2 per opponent ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            opp_ships = sum(game.defense_ships.values())
        else:
            opp_ships = sum(game.offense_ships.values())
        return base_total + (opp_ships * 2)


@dataclass
class Karateka(AlienPower):
    """Karateka - Power of Strikes. Quick attacks."""
    name: str = field(default="Karateka", init=False)
    description: str = field(default="+4 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Wrestler(AlienPower):
    """Wrestler - Power of Grappling. Pin opponents."""
    name: str = field(default="Wrestler", init=False)
    description: str = field(default="+5 defending with 3+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            ships = game.defense_ships.get(player.name, 0)
            if ships >= 3:
                return base_total + 5
        return base_total


@dataclass
class Boxer(AlienPower):
    """Boxer - Power of Punches. Damage dealer."""
    name: str = field(default="Boxer", init=False)
    description: str = field(default="Opponent loses 1 extra ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Aikido(AlienPower):
    """Aikido - Power of Redirection. Turn attacks back."""
    name: str = field(default="Aikido", init=False)
    description: str = field(default="+3 when outnumbered.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            opp_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
        if opp_ships > my_ships:
            return base_total + 3
        return base_total


@dataclass
class KungFu(AlienPower):
    """KungFu - Power of Forms. Versatile fighter."""
    name: str = field(default="KungFu", init=False)
    description: str = field(default="+2 offense, +2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class TaeKwonDo(AlienPower):
    """TaeKwonDo - Power of Kicks. Long range."""
    name: str = field(default="TaeKwonDo", init=False)
    description: str = field(default="+3 with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships >= 4:
            return base_total + 3
        return base_total


@dataclass
class MuayThai(AlienPower):
    """MuayThai - Power of Eight Limbs. Multiple attacks."""
    name: str = field(default="MuayThai", init=False)
    description: str = field(default="+4 with 2+ ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships >= 2:
            return base_total + 4
        return base_total


@dataclass
class Fencer(AlienPower):
    """Fencer - Power of Precision. Accurate strikes."""
    name: str = field(default="Fencer", init=False)
    description: str = field(default="+3 with 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships == 1:
            return base_total + 3
        return base_total


@dataclass
class Samurai(AlienPower):
    """Samurai - Power of Honor. Strong single combat."""
    name: str = field(default="Samurai", init=False)
    description: str = field(default="+5 with no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        if allies == 0:
            return base_total + 5
        return base_total


@dataclass
class Ninja(AlienPower):
    """Ninja - Power of Stealth. Surprise attacks."""
    name: str = field(default="Ninja", init=False)
    description: str = field(default="+4 on first attack vs each player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    attacked: set = field(default_factory=set)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE and game.defense:
            if game.defense.name not in self.attacked:
                self.attacked.add(game.defense.name)
                return base_total + 4
        return base_total


@dataclass
class Capoeira(AlienPower):
    """Capoeira - Power of Flow. Dodge attacks."""
    name: str = field(default="Capoeira", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kendo(AlienPower):
    """Kendo - Power of the Sword. Strong strikes."""
    name: str = field(default="Kendo", init=False)
    description: str = field(default="+3 offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class JiuJitsu(AlienPower):
    """JiuJitsu - Power of Submission. Ground control."""
    name: str = field(default="JiuJitsu", init=False)
    description: str = field(default="+4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Sumo(AlienPower):
    """Sumo - Power of Mass. Push opponents."""
    name: str = field(default="Sumo", init=False)
    description: str = field(default="+2 per your ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + (ships * 2)


# Register all martial arts powers
MARTIAL_ARTS_POWERS = [
    Judoka, Karateka, Wrestler, Boxer, Aikido,
    KungFu, TaeKwonDo, MuayThai, Fencer, Samurai,
    Ninja, Capoeira, Kendo, JiuJitsu, Sumo,
]

for power_class in MARTIAL_ARTS_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
