"""
Mythical Artifact themed alien powers for Cosmic Encounter.
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
class Excalibur(AlienPower):
    """Excalibur - Power of Legend."""
    name: str = field(default="Excalibur", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class HolyGrail(AlienPower):
    """Holy Grail - Power of Salvation."""
    name: str = field(default="HolyGrail", init=False)
    description: str = field(default="Retrieve all ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mjolnir(AlienPower):
    """Mjolnir - Power of Thunder."""
    name: str = field(default="Mjolnir", init=False)
    description: str = field(default="+6 first combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Aegis(AlienPower):
    """Aegis - Power of Protection."""
    name: str = field(default="Aegis", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class GoldenFleece(AlienPower):
    """Golden Fleece - Power of Quest."""
    name: str = field(default="GoldenFleece", init=False)
    description: str = field(default="+3 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Trident_Myth(AlienPower):
    """Trident - Power of Seas."""
    name: str = field(default="Trident_Myth", init=False)
    description: str = field(default="+3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Gungnir(AlienPower):
    """Gungnir - Power of Aim."""
    name: str = field(default="Gungnir", init=False)
    description: str = field(default="Never miss attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class PandorasBox(AlienPower):
    """Pandora's Box - Power of Chaos."""
    name: str = field(default="PandorasBox", init=False)
    description: str = field(default="Random bonus 0-8.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class AchillesArmor(AlienPower):
    """Achilles Armor - Power of Invulnerability."""
    name: str = field(default="AchillesArmor", init=False)
    description: str = field(default="Lose only 1 ship max.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class RingOfPower(AlienPower):
    """Ring of Power - Power of Dominion."""
    name: str = field(default="RingOfPower", init=False)
    description: str = field(default="+2 per player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class PhilosophersStone(AlienPower):
    """Philosopher's Stone - Power of Transformation."""
    name: str = field(default="PhilosophersStone", init=False)
    description: str = field(default="Convert low card to high.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ankh(AlienPower):
    """Ankh - Power of Life."""
    name: str = field(default="Ankh", init=False)
    description: str = field(default="Retrieve 2 ships on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Excalibur, HolyGrail, Mjolnir, Aegis, GoldenFleece, Trident_Myth,
    Gungnir, PandorasBox, AchillesArmor, RingOfPower, PhilosophersStone, Ankh,
]:
    AlienRegistry.register(alien_class())
