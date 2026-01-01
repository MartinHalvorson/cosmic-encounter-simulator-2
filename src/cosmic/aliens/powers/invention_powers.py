"""
Invention-themed alien powers for Cosmic Encounter.

Powers inspired by famous inventions and discoveries.
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
class Telegraph(AlienPower):
    """Telegraph - Power of Communication. Signal allies."""
    name: str = field(default="Telegraph", init=False)
    description: str = field(default="Allies always commit +1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lightbulb(AlienPower):
    """Lightbulb - Power of Illumination. Reveal plans."""
    name: str = field(default="Lightbulb", init=False)
    description: str = field(default="See opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Printing(AlienPower):
    """Printing - Power of Duplication. Copy resources."""
    name: str = field(default="Printing", init=False)
    description: str = field(default="Draw 2 cards after win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wheel(AlienPower):
    """Wheel - Power of Movement. Enhanced mobility."""
    name: str = field(default="Wheel", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Compass(AlienPower):
    """Compass - Power of Direction. Navigate encounters."""
    name: str = field(default="Compass", init=False)
    description: str = field(default="+2 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + (colonies * 2)
        return base_total


@dataclass
class Telescope(AlienPower):
    """Telescope - Power of Vision. See far ahead."""
    name: str = field(default="Telescope", init=False)
    description: str = field(default="+3 attacking distant players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Battery(AlienPower):
    """Battery - Power of Storage. Build up power."""
    name: str = field(default="Battery", init=False)
    description: str = field(default="+1 per card in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + player.hand_size()
        return base_total


@dataclass
class Engine(AlienPower):
    """Engine - Power of Drive. Enhanced power."""
    name: str = field(default="Engine", init=False)
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
class Radio(AlienPower):
    """Radio - Power of Broadcast. Reach all players."""
    name: str = field(default="Radio", init=False)
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
class Telephone(AlienPower):
    """Telephone - Power of Connection. Direct communication."""
    name: str = field(default="Telephone", init=False)
    description: str = field(default="Negotiate with any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Camera(AlienPower):
    """Camera - Power of Capture. Remember advantages."""
    name: str = field(default="Camera", init=False)
    description: str = field(default="+3 vs players you've beaten.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    beaten: set = field(default_factory=set)


@dataclass
class Computer(AlienPower):
    """Computer - Power of Calculation. Optimize outcomes."""
    name: str = field(default="Computer", init=False)
    description: str = field(default="+2 per turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(8, game.current_turn * 2)
            return base_total + bonus
        return base_total


@dataclass
class Internet(AlienPower):
    """Internet - Power of Network. Global reach."""
    name: str = field(default="Internet", init=False)
    description: str = field(default="+1 per player in game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + len(game.players)
        return base_total


@dataclass
class Satellite(AlienPower):
    """Satellite - Power of Orbit. Observe all."""
    name: str = field(default="Satellite", init=False)
    description: str = field(default="+4 attacking players with fewer colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE and game.defense:
            my_colonies = player.count_foreign_colonies(game.planets)
            opp_colonies = game.defense.count_foreign_colonies(game.planets)
            if opp_colonies < my_colonies:
                return base_total + 4
        return base_total


@dataclass
class Rocket(AlienPower):
    """Rocket - Power of Launch. Quick attacks."""
    name: str = field(default="Rocket", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 1:
            return base_total + 5
        return base_total


@dataclass
class Laser_Invention(AlienPower):
    """Laser_Invention - Power of Focus. Precise strikes."""
    name: str = field(default="Laser_Invention", init=False)
    description: str = field(default="+3 vs single defender.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if len(game.defense_ships) == 1:
                return base_total + 3
        return base_total


# Register all invention powers
INVENTION_POWERS = [
    Telegraph, Lightbulb, Printing, Wheel, Compass,
    Telescope, Battery, Engine, Radio, Telephone,
    Camera, Computer, Internet, Satellite, Rocket, Laser_Invention,
]

for power_class in INVENTION_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
