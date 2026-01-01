"""
Dinosaur-themed alien powers for Cosmic Encounter.

Powers based on dinosaurs and prehistoric creatures.
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
class Tyrannosaurus(AlienPower):
    """Tyrannosaurus - Power of Dominance. +6 on offense."""
    name: str = field(default="Tyrannosaurus", init=False)
    description: str = field(default="+6 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 6
        return base_total


@dataclass
class Triceratops(AlienPower):
    """Triceratops - Power of Defense. +6 on defense."""
    name: str = field(default="Triceratops", init=False)
    description: str = field(default="+6 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 6
        return base_total


@dataclass
class Velociraptor(AlienPower):
    """Velociraptor - Power of Pack. +2 per ship."""
    name: str = field(default="Velociraptor", init=False)
    description: str = field(default="Ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + ships  # Extra +1 per ship


@dataclass
class Stegosaurus(AlienPower):
    """Stegosaurus - Power of Plates. Reduce opponent's total."""
    name: str = field(default="Stegosaurus", init=False)
    description: str = field(default="Opponent's total -3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pterodactyl(AlienPower):
    """Pterodactyl - Power of Flight. Attack any planet."""
    name: str = field(default="Pterodactyl", init=False)
    description: str = field(default="+3 attacking undefended planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            def_ships = sum(game.defense_ships.values())
            if def_ships <= 1:
                return base_total + 3
        return base_total


@dataclass
class Brachiosaurus(AlienPower):
    """Brachiosaurus - Power of Height. See opponent's cards."""
    name: str = field(default="Brachiosaurus", init=False)
    description: str = field(default="+2 per card advantage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            card_diff = player.hand_size() - opponent.hand_size()
            if card_diff > 0:
                return base_total + (card_diff * 2)
        return base_total


@dataclass
class Ankylosaurus(AlienPower):
    """Ankylosaurus - Power of Armor. Reduce damage taken."""
    name: str = field(default="Ankylosaurus", init=False)
    description: str = field(default="Lose 1 fewer ship on defeat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Spinosaurus(AlienPower):
    """Spinosaurus - Power of Sail. +4 with full ships."""
    name: str = field(default="Spinosaurus", init=False)
    description: str = field(default="+4 with 4 ships.", init=False)
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
            return base_total + 4
        return base_total


@dataclass
class Diplodocus(AlienPower):
    """Diplodocus - Power of Length. +1 per colony."""
    name: str = field(default="Diplodocus", init=False)
    description: str = field(default="+1 per colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + colonies
        return base_total


@dataclass
class Parasaurolophus(AlienPower):
    """Parasaurolophus - Power of Call. Summon allies."""
    name: str = field(default="Parasaurolophus", init=False)
    description: str = field(default="Allies commit +1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pachycephalosaurus(AlienPower):
    """Pachycephalosaurus - Power of Headbutt. Stun opponent."""
    name: str = field(default="Pachycephalosaurus", init=False)
    description: str = field(default="On win, opponent discards 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dilophosaurus(AlienPower):
    """Dilophosaurus - Power of Spit. -2 to opponent."""
    name: str = field(default="Dilophosaurus", init=False)
    description: str = field(default="Opponent gets -2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Carnotaurus(AlienPower):
    """Carnotaurus - Power of Charge. +5 when behind."""
    name: str = field(default="Carnotaurus", init=False)
    description: str = field(default="+5 when at fewer colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            if my_colonies < opp_colonies:
                return base_total + 5
        return base_total


@dataclass
class Allosaurus(AlienPower):
    """Allosaurus - Power of Hunt. Destroy ships."""
    name: str = field(default="Allosaurus", init=False)
    description: str = field(default="Destroy 1 enemy ship on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Compsognathus(AlienPower):
    """Compsognathus - Power of Swarm. Strength in numbers."""
    name: str = field(default="Compsognathus", init=False)
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
class Iguanodon(AlienPower):
    """Iguanodon - Power of Thumb. Win by 1."""
    name: str = field(default="Iguanodon", init=False)
    description: str = field(default="+1 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 1
        return base_total


@dataclass
class Mosasaurus(AlienPower):
    """Mosasaurus - Power of Depths. +4 defending home."""
    name: str = field(default="Mosasaurus", init=False)
    description: str = field(default="+4 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 4
        return base_total


@dataclass
class Archaeopteryx(AlienPower):
    """Archaeopteryx - Power of Evolution. Adapt to situation."""
    name: str = field(default="Archaeopteryx", init=False)
    description: str = field(default="+2 defense, +2 offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


# Register all dinosaur powers
DINOSAUR_POWERS = [
    Tyrannosaurus, Triceratops, Velociraptor, Stegosaurus, Pterodactyl,
    Brachiosaurus, Ankylosaurus, Spinosaurus, Diplodocus, Parasaurolophus,
    Pachycephalosaurus, Dilophosaurus, Carnotaurus, Allosaurus, Compsognathus,
    Iguanodon, Mosasaurus, Archaeopteryx,
]

for power_class in DINOSAUR_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
