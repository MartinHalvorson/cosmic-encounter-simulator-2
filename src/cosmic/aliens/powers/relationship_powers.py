"""
Relationship Powers for Cosmic Encounter.

Aliens inspired by interpersonal relationships and social dynamics.
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
class Friend_Alt(AlienPower):
    """
    Friend_Alt - Power of Friendship.
    +1 for each ally you have.
    """
    name: str = field(default="Friend_Alt", init=False)
    description: str = field(
        default="+1 per ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rival_Alt(AlienPower):
    """
    Rival_Alt - Power of Competition.
    +4 against the player with most colonies.
    """
    name: str = field(default="Rival_Alt", init=False)
    description: str = field(
        default="+4 vs player with most colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Partner(AlienPower):
    """
    Partner - Power to Share.
    When you win, one ally may also establish a colony.
    """
    name: str = field(default="Partner", init=False)
    description: str = field(
        default="Ally gains colony when you win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Nemesis(AlienPower):
    """
    Nemesis - Power of Vengeance.
    +5 against the last player who defeated you.
    """
    name: str = field(default="Nemesis", init=False)
    description: str = field(
        default="+5 vs last player who defeated you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sibling(AlienPower):
    """
    Sibling - Power of Rivalry.
    You may force any player to attack another player you choose.
    """
    name: str = field(default="Sibling", init=False)
    description: str = field(
        default="Redirect attacks between other players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mentor(AlienPower):
    """
    Mentor - Power to Teach.
    Allies you invite get +2 to their contributions.
    """
    name: str = field(default="Mentor", init=False)
    description: str = field(
        default="Your allies get +2.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Student(AlienPower):
    """
    Student - Power to Learn.
    Copy the ability of the main player you're allied with.
    """
    name: str = field(default="Student", init=False)
    description: str = field(
        default="Copy allied main player's power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Parent(AlienPower):
    """
    Parent - Power to Protect.
    Your allies' ships cannot be sent to warp.
    """
    name: str = field(default="Parent", init=False)
    description: str = field(
        default="Protect ally ships from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Child(AlienPower):
    """
    Child - Power to Grow.
    +1 for each turn that has passed this game.
    """
    name: str = field(default="Child", init=False)
    description: str = field(
        default="+1 per turn (max +5).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Colleague(AlienPower):
    """
    Colleague - Power to Cooperate.
    When you ally, draw 1 card regardless of outcome.
    """
    name: str = field(default="Colleague", init=False)
    description: str = field(
        default="Draw 1 card when allying.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Boss(AlienPower):
    """
    Boss - Power to Command.
    Allies on your side must commit at least 2 ships.
    """
    name: str = field(default="Boss", init=False)
    description: str = field(
        default="Allies must commit 2+ ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stranger(AlienPower):
    """
    Stranger - Power of Mystery.
    Your power is hidden until you choose to reveal it.
    """
    name: str = field(default="Stranger", init=False)
    description: str = field(
        default="Power hidden until revealed.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Twin(AlienPower):
    """
    Twin - Power to Mirror.
    Copy the card played by your opponent.
    """
    name: str = field(default="Twin", init=False)
    description: str = field(
        default="Copy opponent's card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ancestor(AlienPower):
    """
    Ancestor - Power of Legacy.
    +3 when defending your home planets.
    """
    name: str = field(default="Ancestor", init=False)
    description: str = field(
        default="+3 defending home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Descendant(AlienPower):
    """
    Descendant - Power of Heritage.
    Inherit +2 from any eliminated player.
    """
    name: str = field(default="Descendant", init=False)
    description: str = field(
        default="+2 from eliminated players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all relationship powers
AlienRegistry.register(Friend_Alt())
AlienRegistry.register(Rival_Alt())
AlienRegistry.register(Partner())
AlienRegistry.register(Nemesis())
AlienRegistry.register(Sibling())
AlienRegistry.register(Mentor())
AlienRegistry.register(Student())
AlienRegistry.register(Parent())
AlienRegistry.register(Child())
AlienRegistry.register(Colleague())
AlienRegistry.register(Boss())
AlienRegistry.register(Stranger())
AlienRegistry.register(Twin())
AlienRegistry.register(Ancestor())
AlienRegistry.register(Descendant())
