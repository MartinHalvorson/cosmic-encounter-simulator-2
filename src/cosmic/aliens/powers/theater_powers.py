"""
Theater Powers for Cosmic Encounter.

Aliens inspired by theatrical arts, drama, and performance.
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
class Actor(AlienPower):
    """
    Actor - Power to Perform.
    You may play encounter cards face-down until reveal; they can be any card type.
    """
    name: str = field(default="Actor", init=False)
    description: str = field(
        default="Play any card as encounter card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Director(AlienPower):
    """
    Director - Power to Control.
    Once per encounter, you may choose which player acts first.
    """
    name: str = field(default="Director", init=False)
    description: str = field(
        default="Choose turn order once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Playwright(AlienPower):
    """
    Playwright - Power to Script.
    Before destiny, you may name the encounter outcome. If correct, gain 2 cards.
    """
    name: str = field(default="Playwright", init=False)
    description: str = field(
        default="Predict outcome for 2 cards if correct.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Understudy(AlienPower):
    """
    Understudy - Power to Replace.
    When another player's power is zapped, you may use it instead.
    """
    name: str = field(default="Understudy", init=False)
    description: str = field(
        default="Use zapped player's power instead.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Critic(AlienPower):
    """
    Critic - Power to Judge.
    After reveal, you may declare a winner based on "artistic merit" once per game.
    """
    name: str = field(default="Critic", init=False)
    description: str = field(
        default="Declare winner once per game (override).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Stagehand(AlienPower):
    """
    Stagehand - Power Behind the Scenes.
    You may move ships between colonies before the launch phase.
    """
    name: str = field(default="Stagehand", init=False)
    description: str = field(
        default="Rearrange ships before launch.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Comedian(AlienPower):
    """
    Comedian - Power to Jest.
    When you lose, you may make the winner discard 1 card.
    """
    name: str = field(default="Comedian", init=False)
    description: str = field(
        default="Winner discards 1 card when you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tragedian(AlienPower):
    """
    Tragedian - Power of Drama.
    When you lose ships, each other player loses 1 ship in sympathy.
    """
    name: str = field(default="Tragedian", init=False)
    description: str = field(
        default="Others lose 1 ship when you lose ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mime(AlienPower):
    """
    Mime - Power of Silence.
    You may copy the last card played by any player.
    """
    name: str = field(default="Mime", init=False)
    description: str = field(
        default="Copy last played card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Puppeteer(AlienPower):
    """
    Puppeteer - Power to Manipulate.
    Control one ally's ships as if they were your own.
    """
    name: str = field(default="Puppeteer", init=False)
    description: str = field(
        default="Control ally ships as your own.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dancer(AlienPower):
    """
    Dancer - Power of Grace.
    Your ships may retreat from any encounter without going to warp.
    """
    name: str = field(default="Dancer", init=False)
    description: str = field(
        default="Ships retreat without going to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Singer(AlienPower):
    """
    Singer - Power to Inspire.
    All your allies add +1 to their ship count.
    """
    name: str = field(default="Singer", init=False)
    description: str = field(
        default="Allies add +1 to ship count.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Improvisor(AlienPower):
    """
    Improvisor - Power to Adapt.
    After seeing the opponent's card, draw and play a new card.
    """
    name: str = field(default="Improvisor", init=False)
    description: str = field(
        default="Draw and play new card after seeing opponent's.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Producer(AlienPower):
    """
    Producer - Power to Fund.
    Pay 2 cards to gain +4 in any encounter you're involved in.
    """
    name: str = field(default="Producer", init=False)
    description: str = field(
        default="Pay 2 cards for +4.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class StageManager(AlienPower):
    """
    StageManager - Power of Timing.
    You decide when cards are revealed during the reveal phase.
    """
    name: str = field(default="StageManager", init=False)
    description: str = field(
        default="Control reveal timing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all theater powers
AlienRegistry.register(Actor())
AlienRegistry.register(Director())
AlienRegistry.register(Playwright())
AlienRegistry.register(Understudy())
AlienRegistry.register(Critic())
AlienRegistry.register(Stagehand())
AlienRegistry.register(Comedian())
AlienRegistry.register(Tragedian())
AlienRegistry.register(Mime())
AlienRegistry.register(Puppeteer())
AlienRegistry.register(Dancer())
AlienRegistry.register(Singer())
AlienRegistry.register(Improvisor())
AlienRegistry.register(Producer())
AlienRegistry.register(StageManager())
