"""
Reptile-themed alien powers for Cosmic Encounter.

Powers based on reptiles and their unique characteristics.
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
class Cobra(AlienPower):
    """Cobra - Power of Venom. Opponent loses 1 ship on ties."""
    name: str = field(default="Cobra", init=False)
    description: str = field(default="On ties, opponent loses 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Crocodile(AlienPower):
    """Crocodile - Power of Ambush. +4 on defense."""
    name: str = field(default="Crocodile", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Chameleon(AlienPower):
    """Chameleon - Power of Blending. Copy opponent's card value."""
    name: str = field(default="Chameleon", init=False)
    description: str = field(default="May use opponent's card value instead.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gecko(AlienPower):
    """Gecko - Power of Climbing. +2 per ally."""
    name: str = field(default="Gecko", init=False)
    description: str = field(default="+2 per ally on your side.", init=False)
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
class Iguana(AlienPower):
    """Iguana - Power of Basking. +3 with 2+ ships."""
    name: str = field(default="Iguana", init=False)
    description: str = field(default="+3 when you have 2+ ships.", init=False)
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
            return base_total + 3
        return base_total


@dataclass
class Turtle(AlienPower):
    """Turtle - Power of Shell. +5 on defense, -2 on offense."""
    name: str = field(default="Turtle", init=False)
    description: str = field(default="+5 defense, -2 offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE:
            return base_total + 5
        elif side == Side.OFFENSE:
            return base_total - 2
        return base_total


@dataclass
class Rattlesnake(AlienPower):
    """Rattlesnake - Power of Warning. Opponent reveals card first."""
    name: str = field(default="Rattlesnake", init=False)
    description: str = field(default="Opponent must reveal card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Komodo(AlienPower):
    """Komodo - Power of Persistence. Win ties."""
    name: str = field(default="Komodo", init=False)
    description: str = field(default="You win on ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Python(AlienPower):
    """Python - Power of Constriction. +1 per ship opponent has."""
    name: str = field(default="Python", init=False)
    description: str = field(default="+1 per enemy ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            enemy_ships = sum(game.defense_ships.values())
        else:
            enemy_ships = sum(game.offense_ships.values())
        return base_total + enemy_ships


@dataclass
class Alligator(AlienPower):
    """Alligator - Power of Death Roll. Destroy 2 ships on win."""
    name: str = field(default="Alligator", init=False)
    description: str = field(default="Destroy 2 extra enemy ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Salamander(AlienPower):
    """Salamander - Power of Regeneration. Regrow after loss."""
    name: str = field(default="Salamander", init=False)
    description: str = field(default="Return 1 ship from warp after losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tortoise(AlienPower):
    """Tortoise - Power of Patience. +1 per turn number."""
    name: str = field(default="Tortoise", init=False)
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
class Skink(AlienPower):
    """Skink - Power of Tail Drop. Lose ships to save others."""
    name: str = field(default="Skink", init=False)
    description: str = field(default="Sacrifice 1 ship to save others from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monitor(AlienPower):
    """Monitor - Power of Watching. See opponent's hand size effect."""
    name: str = field(default="Monitor", init=False)
    description: str = field(default="+2 if opponent has more cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and opponent.hand_size() > player.hand_size():
            return base_total + 2
        return base_total


@dataclass
class Anole(AlienPower):
    """Anole - Power of Display. +3 when alone."""
    name: str = field(default="Anole", init=False)
    description: str = field(default="+3 with no allies.", init=False)
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
            return base_total + 3
        return base_total


@dataclass
class Viper(AlienPower):
    """Viper - Power of Speed. +4 on first encounter each turn."""
    name: str = field(default="Viper", init=False)
    description: str = field(default="+4 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 4
        return base_total


@dataclass
class Newt(AlienPower):
    """Newt - Power of Toxin. -2 to opponent."""
    name: str = field(default="Newt", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Basilisk(AlienPower):
    """Basilisk - Power of Petrification. Freeze opponent's ships."""
    name: str = field(default="Basilisk", init=False)
    description: str = field(default="Opponent's ally ships don't count.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all reptile powers
REPTILE_POWERS = [
    Cobra, Crocodile, Chameleon, Gecko, Iguana,
    Turtle, Rattlesnake, Komodo, Python, Alligator,
    Salamander, Tortoise, Skink, Monitor, Anole,
    Viper, Newt, Basilisk,
]

for power_class in REPTILE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
