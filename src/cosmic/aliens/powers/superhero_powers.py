"""
Superhero-themed alien powers for Cosmic Encounter.

Powers inspired by superhero abilities and archetypes.
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
class Invincible(AlienPower):
    """Invincible - Power of Immunity. Cannot lose ships."""
    name: str = field(default="Invincible", init=False)
    description: str = field(default="Lose only 1 ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Teleporter(AlienPower):
    """Teleporter - Power of Blink. Move ships instantly."""
    name: str = field(default="Teleporter", init=False)
    description: str = field(default="Move 2 ships to encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Strongman(AlienPower):
    """Strongman - Power of Strength. +5 always."""
    name: str = field(default="Strongman", init=False)
    description: str = field(default="+5 in every encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 5
        return base_total


@dataclass
class Speedster(AlienPower):
    """Speedster - Power of Speed. +3 on first encounter."""
    name: str = field(default="Speedster", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 3
        return base_total


@dataclass
class Mindreader(AlienPower):
    """Mindreader - Power of Telepathy. See opponent's card."""
    name: str = field(default="Mindreader", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Invisible(AlienPower):
    """Invisible - Power of Stealth. Opponent can't invite allies."""
    name: str = field(default="Invisible", init=False)
    description: str = field(default="Opponent cannot have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Flyer(AlienPower):
    """Flyer - Power of Flight. Attack any planet."""
    name: str = field(default="Flyer", init=False)
    description: str = field(default="+2 attacking any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 2
        return base_total


@dataclass
class Shapechanger(AlienPower):
    """Shapechanger - Power of Morphing. Copy opponent."""
    name: str = field(default="Shapechanger", init=False)
    description: str = field(default="Use opponent's card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Healer(AlienPower):
    """Healer - Power of Healing. Recover ships."""
    name: str = field(default="Healer", init=False)
    description: str = field(default="Return 2 ships from warp after win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magnetizer(AlienPower):
    """Magnetizer - Power of Magnetism. Pull ships."""
    name: str = field(default="Magnetizer", init=False)
    description: str = field(default="+1 per opponent ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            enemy_allies = len([p for p in game.defense_ships if p != game.defense.name]) if game.defense else 0
        else:
            enemy_allies = len([p for p in game.offense_ships if p != game.offense.name]) if game.offense else 0
        return base_total + enemy_allies


@dataclass
class Elemental(AlienPower):
    """Elemental - Power of Elements. Versatile bonus."""
    name: str = field(default="Elemental", init=False)
    description: str = field(default="+3 offense, +3 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Psychic(AlienPower):
    """Psychic - Power of Mind. +2 per card difference."""
    name: str = field(default="Psychic", init=False)
    description: str = field(default="+2 if more cards than opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and player.hand_size() > opponent.hand_size():
            return base_total + 2
        return base_total


@dataclass
class Laser(AlienPower):
    """Laser - Power of Beam. +4 vs single target."""
    name: str = field(default="Laser", init=False)
    description: str = field(default="+4 vs 1 defender.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if len(game.defense_ships) == 1:
                return base_total + 4
        return base_total


@dataclass
class Armored(AlienPower):
    """Armored - Power of Armor. Reduce losses."""
    name: str = field(default="Armored", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Vigilante(AlienPower):
    """Vigilante - Power of Justice. +3 vs leaders."""
    name: str = field(default="Vigilante", init=False)
    description: str = field(default="+3 vs player with most colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            max_colonies = max(p.count_foreign_colonies(game.planets) for p in game.players)
            if opp_colonies >= max_colonies and max_colonies > 0:
                return base_total + 3
        return base_total


@dataclass
class Sidekick(AlienPower):
    """Sidekick - Power of Partnership. Bonus with allies."""
    name: str = field(default="Sidekick", init=False)
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


# Register all superhero powers
SUPERHERO_POWERS = [
    Invincible, Teleporter, Strongman, Speedster, Mindreader,
    Invisible, Flyer, Shapechanger, Healer, Magnetizer,
    Elemental, Psychic, Laser, Armored, Vigilante, Sidekick,
]

for power_class in SUPERHERO_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
