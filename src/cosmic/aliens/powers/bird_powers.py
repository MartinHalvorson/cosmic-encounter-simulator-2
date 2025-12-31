"""
Bird-themed alien powers for Cosmic Encounter.

Powers based on birds and their unique characteristics.
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
class Eagle(AlienPower):
    """Eagle - Power of Vision. +3 on offense."""
    name: str = field(default="Eagle", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Hawk(AlienPower):
    """Hawk - Power of Swoop. +5 against low card values."""
    name: str = field(default="Hawk", init=False)
    description: str = field(default="+5 if opponent plays card value 10 or less.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Owl(AlienPower):
    """Owl - Power of Wisdom. +2 per card in hand."""
    name: str = field(default="Owl", init=False)
    description: str = field(default="+1 per card in hand (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(5, player.hand_size())
            return base_total + bonus
        return base_total


@dataclass
class Crow(AlienPower):
    """Crow - Power of Collection. Draw card on win."""
    name: str = field(default="Crow", init=False)
    description: str = field(default="Draw 1 card when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Penguin(AlienPower):
    """Penguin - Power of Sliding. +4 on defense."""
    name: str = field(default="Penguin", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Parrot(AlienPower):
    """Parrot - Power of Mimicry. Copy opponent's alien power."""
    name: str = field(default="Parrot", init=False)
    description: str = field(default="May use opponent's power this encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Raven(AlienPower):
    """Raven - Power of Omen. +3 at 3 colonies."""
    name: str = field(default="Raven", init=False)
    description: str = field(default="+3 when at exactly 3 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies == 3:
                return base_total + 3
        return base_total


@dataclass
class Falcon(AlienPower):
    """Falcon - Power of Dive. +6 on first attack vs player."""
    name: str = field(default="Falcon", init=False)
    description: str = field(default="+6 on offense with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
            if ships >= 4:
                return base_total + 6
        return base_total


@dataclass
class Peacock(AlienPower):
    """Peacock - Power of Display. Allies get +1 each."""
    name: str = field(default="Peacock", init=False)
    description: str = field(default="Each ally adds +2 instead of +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hummingbird(AlienPower):
    """Hummingbird - Power of Speed. Two encounters per turn."""
    name: str = field(default="Hummingbird", init=False)
    description: str = field(default="Always take second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flamingo(AlienPower):
    """Flamingo - Power of Balance. Win ties."""
    name: str = field(default="Flamingo", init=False)
    description: str = field(default="You win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pelican(AlienPower):
    """Pelican - Power of Storage. Hold extra cards."""
    name: str = field(default="Pelican", init=False)
    description: str = field(default="+2 if hand size > 8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and player.hand_size() > 8:
            return base_total + 2
        return base_total


@dataclass
class Vulture(AlienPower):
    """Vulture - Power of Scavenging. Gain from losses."""
    name: str = field(default="Vulture", init=False)
    description: str = field(default="Draw 1 card when opponent loses ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Condor(AlienPower):
    """Condor - Power of Soaring. +3 with most colonies."""
    name: str = field(default="Condor", init=False)
    description: str = field(default="+3 if you have most foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        max_others = max((p.count_foreign_colonies(game.planets) for p in game.players if p != player), default=0)
        if my_colonies > max_others:
            return base_total + 3
        return base_total


@dataclass
class Toucan(AlienPower):
    """Toucan - Power of Reach. Attack distant planets."""
    name: str = field(default="Toucan", init=False)
    description: str = field(default="+2 attacking planets you have no colony on.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if game.defense_planet and not game.defense_planet.has_colony(player.name):
                return base_total + 2
        return base_total


@dataclass
class Albatross(AlienPower):
    """Albatross - Power of Endurance. Never lose ships to warp."""
    name: str = field(default="Albatross", init=False)
    description: str = field(default="Lost ships go to colonies, not warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Woodpecker(AlienPower):
    """Woodpecker - Power of Persistence. Repeat attacks."""
    name: str = field(default="Woodpecker", init=False)
    description: str = field(default="+2 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 2:
            return base_total + 2
        return base_total


@dataclass
class Stork(AlienPower):
    """Stork - Power of Delivery. Move ships freely."""
    name: str = field(default="Stork", init=False)
    description: str = field(default="May move 1 ship before encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all bird powers
BIRD_POWERS = [
    Eagle, Hawk, Owl, Crow, Penguin,
    Parrot, Raven, Falcon, Peacock, Hummingbird,
    Flamingo, Pelican, Vulture, Condor, Toucan,
    Albatross, Woodpecker, Stork,
]

for power_class in BIRD_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
