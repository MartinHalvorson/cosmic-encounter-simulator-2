"""
Mythical creature themed alien powers for Cosmic Encounter.

Powers inspired by legendary creatures from mythology and folklore.
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
class Griffin(AlienPower):
    """Griffin - Power of Majesty. Noble strength."""
    name: str = field(default="Griffin", init=False)
    description: str = field(default="+4 offense, +2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 4
        elif side == Side.DEFENSE:
            return base_total + 2
        return base_total


@dataclass
class Unicorn(AlienPower):
    """Unicorn - Power of Purity. Healing presence."""
    name: str = field(default="Unicorn", init=False)
    description: str = field(default="Return 2 ships from warp on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Centaur(AlienPower):
    """Centaur - Power of Speed. Swift attacks."""
    name: str = field(default="Centaur", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Minotaur(AlienPower):
    """Minotaur - Power of Labyrinth. Confusing defense."""
    name: str = field(default="Minotaur", init=False)
    description: str = field(default="+5 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 5
        return base_total


@dataclass
class Mermaid(AlienPower):
    """Mermaid - Power of Song. Enchanting presence."""
    name: str = field(default="Mermaid", init=False)
    description: str = field(default="Opponent cannot have allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cyclops(AlienPower):
    """Cyclops - Power of One Eye. Focused strength."""
    name: str = field(default="Cyclops", init=False)
    description: str = field(default="+6 with 1 ship.", init=False)
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
            return base_total + 6
        return base_total


@dataclass
class Harpy(AlienPower):
    """Harpy - Power of Swoop. Hit and run."""
    name: str = field(default="Harpy", init=False)
    description: str = field(default="Lose only 1 ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hydra(AlienPower):
    """Hydra - Power of Regeneration. Regrow losses."""
    name: str = field(default="Hydra", init=False)
    description: str = field(default="Return 1 ship from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cerberus(AlienPower):
    """Cerberus - Power of Three Heads. Triple threat."""
    name: str = field(default="Cerberus", init=False)
    description: str = field(default="+3 with 3+ ships.", init=False)
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
        if ships >= 3:
            return base_total + 3
        return base_total


@dataclass
class Chimera(AlienPower):
    """Chimera - Power of Mixture. Combined strengths."""
    name: str = field(default="Chimera", init=False)
    description: str = field(default="+2 per ally.", init=False)
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
        return base_total + (allies * 2)


@dataclass
class Sphinx_Creature(AlienPower):
    """Sphinx_Creature - Power of Riddles. Test opponents."""
    name: str = field(default="Sphinx_Creature", init=False)
    description: str = field(default="Opponent reveals card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pegasus(AlienPower):
    """Pegasus - Power of Wings. Swift travel."""
    name: str = field(default="Pegasus", init=False)
    description: str = field(default="+2 offense, take second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 2
        return base_total


@dataclass
class Kraken(AlienPower):
    """Kraken - Power of Depths. Ocean terror."""
    name: str = field(default="Kraken", init=False)
    description: str = field(default="+1 per opponent ship.", init=False)
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
        return base_total + opp_ships


@dataclass
class Thunderbird(AlienPower):
    """Thunderbird - Power of Storm. Lightning strikes."""
    name: str = field(default="Thunderbird", init=False)
    description: str = field(default="+4 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 4
        return base_total


@dataclass
class Kelpie(AlienPower):
    """Kelpie - Power of Lure. Draw opponents in."""
    name: str = field(default="Kelpie", init=False)
    description: str = field(default="+3 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 3
        return base_total


@dataclass
class Wendigo(AlienPower):
    """Wendigo - Power of Hunger. Growing strength."""
    name: str = field(default="Wendigo", init=False)
    description: str = field(default="+1 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn)
            return base_total + bonus
        return base_total


# Register all mythical creature powers
MYTHICAL_CREATURE_POWERS = [
    Griffin, Unicorn, Centaur, Minotaur, Mermaid,
    Cyclops, Harpy, Hydra, Cerberus, Chimera,
    Sphinx_Creature, Pegasus, Kraken, Thunderbird, Kelpie, Wendigo,
]

for power_class in MYTHICAL_CREATURE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
