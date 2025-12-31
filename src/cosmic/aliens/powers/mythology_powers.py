"""
Mythology and Legend themed alien powers for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Hercules(AlienPower):
    """
    Hercules - Power of Strength.
    +1 per ship you have in the encounter.
    """
    name: str = field(default="Hercules", init=False)
    description: str = field(
        default="+1 per ship in encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Strength bonus."""
        if not player.power_active:
            return base_total

        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)

        return base_total + ships


@dataclass
class Zeus(AlienPower):
    """
    Zeus - Power of Lightning.
    Once per encounter, destroy 1 opposing ship.
    """
    name: str = field(default="Zeus", init=False)
    description: str = field(
        default="Destroy 1 opposing ship per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Athena(AlienPower):
    """
    Athena - Power of Wisdom.
    See opponent's encounter card before playing yours.
    """
    name: str = field(default="Athena", init=False)
    description: str = field(
        default="See opponent's card before playing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Poseidon(AlienPower):
    """
    Poseidon - Power of the Sea.
    +3 when attacking from or defending a planet adjacent to warp.
    """
    name: str = field(default="Poseidon", init=False)
    description: str = field(
        default="+3 for sea-adjacent planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hades(AlienPower):
    """
    Hades - Power of the Underworld.
    Retrieve 2 ships from warp at the start of each turn.
    """
    name: str = field(default="Hades", init=False)
    description: str = field(
        default="Retrieve 2 ships from warp each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Apollo(AlienPower):
    """
    Apollo - Power of Light.
    All encounter cards are revealed simultaneously (no hidden information).
    """
    name: str = field(default="Apollo", init=False)
    description: str = field(
        default="All cards revealed at once.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ares(AlienPower):
    """
    Ares - Power of War.
    +2 attack per encounter you've been in this turn.
    """
    name: str = field(default="Ares", init=False)
    description: str = field(
        default="+2 per encounter this turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Aphrodite(AlienPower):
    """
    Aphrodite - Power of Love.
    Opponents must invite you to ally. You may always accept.
    """
    name: str = field(default="Aphrodite", init=False)
    description: str = field(
        default="Always invited to ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hermes(AlienPower):
    """
    Hermes - Power of Speed.
    May have a second encounter if you win the first.
    """
    name: str = field(default="Hermes", init=False)
    description: str = field(
        default="Extra encounter if you win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Odin(AlienPower):
    """
    Odin - Power of Wisdom.
    Draw 3 cards, keep 1, discard 2 at the start of each turn.
    """
    name: str = field(default="Odin", init=False)
    description: str = field(
        default="Draw 3, keep 1 each turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thor(AlienPower):
    """
    Thor - Power of Thunder.
    +4 when you have more ships than opponent.
    """
    name: str = field(default="Thor", init=False)
    description: str = field(
        default="+4 when more ships than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Thunder bonus."""
        if not player.power_active:
            return base_total

        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            their_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            their_ships = sum(game.offense_ships.values())

        if my_ships > their_ships:
            return base_total + 4
        return base_total


@dataclass
class Loki(AlienPower):
    """
    Loki - Power of Mischief.
    Once per encounter, swap encounter cards with opponent.
    """
    name: str = field(default="Loki", init=False)
    description: str = field(
        default="Swap encounter cards with opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ra(AlienPower):
    """
    Ra - Power of the Sun.
    +2 during morning (turns 1-50), -1 during night (turns 51+).
    """
    name: str = field(default="Ra", init=False)
    description: str = field(
        default="+2 early game, -1 late game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Sun cycle."""
        if not player.power_active:
            return base_total

        if game.current_turn <= 50:
            return base_total + 2
        return max(0, base_total - 1)


@dataclass
class Anubis(AlienPower):
    """
    Anubis - Power of Death.
    Ships you destroy don't go to warp - they're removed from game.
    """
    name: str = field(default="Anubis", init=False)
    description: str = field(
        default="Destroyed ships removed from game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Isis(AlienPower):
    """
    Isis - Power of Resurrection.
    Once per turn, return all ships from warp to colonies.
    """
    name: str = field(default="Isis", init=False)
    description: str = field(
        default="Return all ships from warp once per turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Set_Myth(AlienPower):
    """
    Set - Power of Chaos.
    Randomize one element of each encounter (determined by die roll).
    """
    name: str = field(default="Set_Myth", init=False)
    description: str = field(
        default="Random chaos element each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Medusa(AlienPower):
    """
    Medusa - Power to Petrify.
    One opposing ship per encounter is frozen and cannot participate.
    """
    name: str = field(default="Medusa", init=False)
    description: str = field(
        default="Freeze 1 opposing ship per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Minotaur(AlienPower):
    """
    Minotaur - Power of the Labyrinth.
    +3 when defending your home planets.
    """
    name: str = field(default="Minotaur", init=False)
    description: str = field(
        default="+3 home defense.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE], init=False
    )

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Home defense bonus."""
        if not player.power_active or side != Side.DEFENSE:
            return base_total
        return base_total + 3


@dataclass
class Phoenix_Myth(AlienPower):
    """
    Phoenix - Power of Rebirth.
    When you lose all foreign colonies, draw 5 cards and gain 1 colony.
    """
    name: str = field(default="Phoenix_Myth", init=False)
    description: str = field(
        default="Losing all colonies: draw 5 cards, gain 1.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all aliens
AlienRegistry.register(Hercules())
AlienRegistry.register(Zeus())
AlienRegistry.register(Athena())
AlienRegistry.register(Poseidon())
AlienRegistry.register(Hades())
AlienRegistry.register(Apollo())
AlienRegistry.register(Ares())
AlienRegistry.register(Aphrodite())
AlienRegistry.register(Hermes())
AlienRegistry.register(Odin())
AlienRegistry.register(Thor())
AlienRegistry.register(Loki())
AlienRegistry.register(Ra())
AlienRegistry.register(Anubis())
AlienRegistry.register(Isis())
AlienRegistry.register(Set_Myth())
AlienRegistry.register(Medusa())
AlienRegistry.register(Minotaur())
AlienRegistry.register(Phoenix_Myth())
