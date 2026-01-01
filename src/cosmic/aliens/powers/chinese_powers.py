"""
Chinese-themed alien powers for Cosmic Encounter.

Powers inspired by ancient Chinese civilization.
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
class Emperor_China(AlienPower):
    """Emperor_China - Power of Mandate. Son of Heaven."""
    name: str = field(default="Emperor_China", init=False)
    description: str = field(default="+4 offense, +4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Dragon_China(AlienPower):
    """Dragon_China - Power of Fortune. Divine beast."""
    name: str = field(default="Dragon_China", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 5
        return base_total


@dataclass
class Great_Wall(AlienPower):
    """Great_Wall - Power of Barrier. Mighty fortification."""
    name: str = field(default="Great_Wall", init=False)
    description: str = field(default="+6 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 6
        return base_total


@dataclass
class Mandarin(AlienPower):
    """Mandarin - Power of Bureaucracy. Imperial official."""
    name: str = field(default="Mandarin", init=False)
    description: str = field(default="+1 per card in hand (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(7, player.hand_size())
            return base_total + bonus
        return base_total


@dataclass
class Terracotta(AlienPower):
    """Terracotta - Power of Army. Eternal soldiers."""
    name: str = field(default="Terracotta", init=False)
    description: str = field(default="+2 per ship.", init=False)
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


@dataclass
class Jade(AlienPower):
    """Jade - Power of Purity. Sacred stone."""
    name: str = field(default="Jade", init=False)
    description: str = field(default="+3 with no ships in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and player.ships_in_warp == 0:
            return base_total + 3
        return base_total


@dataclass
class Silk_Road(AlienPower):
    """Silk_Road - Power of Trade. Ancient highway."""
    name: str = field(default="Silk_Road", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Forbidden_City(AlienPower):
    """Forbidden_City - Power of Mystery. Imperial palace."""
    name: str = field(default="Forbidden_City", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Monk_China(AlienPower):
    """Monk_China - Power of Discipline. Temple warrior."""
    name: str = field(default="Monk_China", init=False)
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
class Gunpowder(AlienPower):
    """Gunpowder - Power of Explosion. Chinese invention."""
    name: str = field(default="Gunpowder", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Pagoda(AlienPower):
    """Pagoda - Power of Temple. Sacred tower."""
    name: str = field(default="Pagoda", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Junk(AlienPower):
    """Junk - Power of Ship. Chinese vessel."""
    name: str = field(default="Junk", init=False)
    description: str = field(default="+5 with 4 ships.", init=False)
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
            return base_total + 5
        return base_total


@dataclass
class Dynasty_China(AlienPower):
    """Dynasty_China - Power of Legacy. Imperial line."""
    name: str = field(default="Dynasty_China", init=False)
    description: str = field(default="+3 per ally.", init=False)
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
        return base_total + (allies * 3)


@dataclass
class Crossbow(AlienPower):
    """Crossbow - Power of Range. Chinese weapon."""
    name: str = field(default="Crossbow", init=False)
    description: str = field(default="+4 with 1-2 ships.", init=False)
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
        if ships in (1, 2):
            return base_total + 4
        return base_total


# Register all chinese powers
CHINESE_POWERS = [
    Emperor_China, Dragon_China, Great_Wall, Mandarin, Terracotta,
    Jade, Silk_Road, Forbidden_City, Monk_China, Gunpowder,
    Pagoda, Junk, Dynasty_China, Crossbow,
]

for power_class in CHINESE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
