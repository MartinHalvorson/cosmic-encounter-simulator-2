"""
Architecture Powers for Cosmic Encounter.

Aliens inspired by architectural concepts and building structures.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, List

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Architect(AlienPower):
    """
    Architect - Power to Design.
    Before each encounter, you may rearrange up to 3 ships among your colonies.
    """
    name: str = field(default="Architect", init=False)
    description: str = field(
        default="Rearrange up to 3 ships among your colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Builder(AlienPower):
    """
    Builder - Power to Construct.
    When you establish a new colony, draw 2 cards.
    """
    name: str = field(default="Builder", init=False)
    description: str = field(
        default="Draw 2 cards when establishing a colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Demolisher(AlienPower):
    """
    Demolisher - Power to Destroy.
    When you win as offense, remove 1 additional ship from the planet.
    """
    name: str = field(default="Demolisher", init=False)
    description: str = field(
        default="Remove 1 extra ship when winning offense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Foundation(AlienPower):
    """
    Foundation - Power of Stability.
    Your home colonies cannot have fewer than 2 ships removed at once.
    """
    name: str = field(default="Foundation", init=False)
    description: str = field(
        default="Home colonies: minimum 2 ships removed at once.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Skyscraper(AlienPower):
    """
    Skyscraper - Power to Rise.
    Add +1 for each colony you have (max +5).
    """
    name: str = field(default="Skyscraper", init=False)
    description: str = field(
        default="+1 per colony (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +1 per colony."""
        if not player.power_active:
            return base_total
        colonies = player.count_foreign_colonies(game.planets)
        home_colonies = sum(1 for p in game.planets if p.owner == player and p.has_colony(player.name))
        total_colonies = colonies + home_colonies
        return base_total + min(5, total_colonies)


@dataclass
class Pillar(AlienPower):
    """
    Pillar - Power to Support.
    Allied ships count double toward your side's total.
    """
    name: str = field(default="Pillar", init=False)
    description: str = field(
        default="Allied ships count double.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bridge(AlienPower):
    """
    Bridge - Power to Connect.
    You may invite one additional ally beyond the normal limit.
    """
    name: str = field(default="Bridge", init=False)
    description: str = field(
        default="Invite 1 extra ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tower(AlienPower):
    """
    Tower - Power of Defense.
    Add +4 when defending your home planets.
    """
    name: str = field(default="Tower", init=False)
    description: str = field(
        default="+4 defending home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add +4 defending home."""
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE and game.defense_planet:
            if game.defense_planet.owner == player:
                return base_total + 4
        return base_total


@dataclass
class Vault(AlienPower):
    """
    Vault - Power to Secure.
    Cards cannot be taken from your hand by other powers.
    """
    name: str = field(default="Vault", init=False)
    description: str = field(
        default="Cards cannot be stolen from your hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dome(AlienPower):
    """
    Dome - Power to Cover.
    Your allies are protected from losing ships when you win.
    """
    name: str = field(default="Dome", init=False)
    description: str = field(
        default="Allies don't lose ships when you win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fortress(AlienPower):
    """
    Fortress - Power to Fortify.
    You may commit up to 6 ships when defending (instead of 4).
    """
    name: str = field(default="Fortress", init=False)
    description: str = field(
        default="Commit up to 6 ships when defending.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Monument(AlienPower):
    """
    Monument - Power to Commemorate.
    Gain 1 token each time you win an encounter. Each token is worth +1.
    """
    name: str = field(default="Monument", init=False)
    description: str = field(
        default="Win tokens: +1 each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rampart(AlienPower):
    """
    Rampart - Power to Wall.
    Opponents need 4 additional ships to successfully invade your home planets.
    """
    name: str = field(default="Rampart", init=False)
    description: str = field(
        default="Invaders need +4 ships on home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spire(AlienPower):
    """
    Spire - Power to Reach.
    You may attack any planet in the game, ignoring destiny.
    """
    name: str = field(default="Spire", init=False)
    description: str = field(
        default="Attack any planet, ignore destiny.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ruins(AlienPower):
    """
    Ruins - Power of the Past.
    When you lose a colony, you may immediately attack it again.
    """
    name: str = field(default="Ruins", init=False)
    description: str = field(
        default="Attack again after losing a colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all architecture powers
AlienRegistry.register(Architect())
AlienRegistry.register(Builder())
AlienRegistry.register(Demolisher())
AlienRegistry.register(Foundation())
AlienRegistry.register(Skyscraper())
AlienRegistry.register(Pillar())
AlienRegistry.register(Bridge())
AlienRegistry.register(Tower())
AlienRegistry.register(Vault())
AlienRegistry.register(Dome())
AlienRegistry.register(Fortress())
AlienRegistry.register(Monument())
AlienRegistry.register(Rampart())
AlienRegistry.register(Spire())
AlienRegistry.register(Ruins())
