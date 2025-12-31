"""
Cosmic Horror themed alien powers for Cosmic Encounter.

Inspired by Lovecraftian horror and cosmic dread.
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
class Eldritch(AlienPower):
    """
    Eldritch - Power of the Unknown.
    Your encounter card is always played face-down and only revealed
    at resolution. Opponent must commit to their card blind.
    """
    name: str = field(default="Eldritch", init=False)
    description: str = field(
        default="Encounter card always hidden until resolution.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harbinger(AlienPower):
    """
    Harbinger - Power of Portents.
    At the start of each encounter, draw the top card of the destiny
    deck and show it to all. That player cannot be invited to ally.
    """
    name: str = field(default="Harbinger", init=False)
    description: str = field(
        default="Reveal destiny; that player cannot ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cthonic(AlienPower):
    """
    Cthonic - Power from Below.
    Ships in the warp count as being on your home planets for
    defensive purposes.
    """
    name: str = field(default="Cthonic", init=False)
    description: str = field(
        default="Ships in warp defend home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Add warp ships to defense."""
        if not player.power_active:
            return base_count
        if side == Side.DEFENSE:
            return base_count + player.ships_in_warp
        return base_count


@dataclass
class Abomination(AlienPower):
    """
    Abomination - Power of Horror.
    When you win an encounter, one random ship from each opposing
    player goes to the warp (in addition to normal losses).
    """
    name: str = field(default="Abomination", init=False)
    description: str = field(
        default="Win: extra ship from each opponent to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Extra horror damage."""
        if not as_main_player or not player.power_active:
            return

        for other in game.players:
            if other != player:
                taken = other.get_ships_from_colonies(1, game.planets)
                other.send_ships_to_warp(taken)


@dataclass
class Lurker(AlienPower):
    """
    Lurker - Power to Wait.
    You may pass on your first encounter each turn. If you do,
    your second encounter has +5 attack.
    """
    name: str = field(default="Lurker", init=False)
    description: str = field(
        default="Pass first encounter; +5 on second.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dreamer(AlienPower):
    """
    Dreamer - Power of Sleep.
    You may skip any phase. If you skip combat, the encounter ends
    with no winner (all ships return home).
    """
    name: str = field(default="Dreamer", init=False)
    description: str = field(
        default="Skip phases; skipping combat ends encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Formless(AlienPower):
    """
    Formless - Power of No Shape.
    Your ships are immune to card effects that target "ships."
    They can only be affected by combat losses.
    """
    name: str = field(default="Formless", init=False)
    description: str = field(
        default="Ships immune to card effects.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Watcher(AlienPower):
    """
    Watcher - Power to Observe.
    You may look at any player's hand at any time. You see all
    encounter cards before they are played.
    """
    name: str = field(default="Watcher", init=False)
    description: str = field(
        default="See all hands and encounter cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Devourer(AlienPower):
    """
    Devourer - Power to Consume.
    When you win an encounter, you may remove 1 card from the
    game entirely (not to discard).
    """
    name: str = field(default="Devourer", init=False)
    description: str = field(
        default="Win: remove 1 card from the game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ancient(AlienPower):
    """
    Ancient - Power of Ages.
    Your ships gain +1 for each completed round of play.
    As the game progresses, you become stronger.
    """
    name: str = field(default="Ancient", init=False)
    description: str = field(
        default="+1 per ship for each round played.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Ships get stronger over time."""
        if not player.power_active:
            return base_count
        rounds = game.current_turn // len(game.players)
        return base_count * (1 + rounds)


@dataclass
class Mindflayer(AlienPower):
    """
    Mindflayer - Power of Control.
    Once per encounter, you may take control of one opposing ally's
    ships, adding them to your side.
    """
    name: str = field(default="Mindflayer", init=False)
    description: str = field(
        default="Take control of opposing ally's ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Void_Horror(AlienPower):
    """
    Void Horror - Power of Emptiness.
    Ships you defeat don't go to the warp - they are removed
    from the game entirely.
    """
    name: str = field(default="Void_Horror", init=False)
    description: str = field(
        default="Defeated ships removed from game.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Nyarlathotep(AlienPower):
    """
    Nyarlathotep - Power of Many Forms.
    At the start of each encounter, you may copy any other alien's
    power for that encounter.
    """
    name: str = field(default="Nyarlathotep", init=False)
    description: str = field(
        default="Copy any alien power each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Shoggoth(AlienPower):
    """
    Shoggoth - Power to Absorb.
    When you lose ships, they join your ships on a random colony
    instead of going to warp.
    """
    name: str = field(default="Shoggoth", init=False)
    description: str = field(
        default="Lost ships join random colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        source: str
    ) -> int:
        """Ships join a colony instead."""
        if not player.power_active:
            return count

        if player.home_planets:
            target = random.choice(player.home_planets)
            target.add_ships(player.name, count)
            return 0
        return count


@dataclass
class Cultist(AlienPower):
    """
    Cultist - Power of Devotion.
    Once per turn, you may sacrifice a ship to draw 3 cards.
    """
    name: str = field(default="Cultist", init=False)
    description: str = field(
        default="Sacrifice ship: draw 3 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Sacrifice for cards."""
        if not player.power_active:
            return

        if player.total_ships_in_play(game.planets) > 5:
            taken = player.get_ships_from_colonies(1, game.planets)
            player.send_ships_to_warp(taken)
            cards = game.cosmic_deck.draw_multiple(3)
            player.add_cards(cards)


@dataclass
class DeepOne(AlienPower):
    """
    Deep One - Power from the Depths.
    Your home planets are protected by the deep. Attackers must
    commit at least 3 ships to attack your home system.
    """
    name: str = field(default="DeepOne", init=False)
    description: str = field(
        default="Attackers must use 3+ ships on your home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mi_Go(AlienPower):
    """
    Mi-Go - Power of Science.
    At the start of your turn, you may look at the top 5 cards of
    the cosmic deck and rearrange them in any order.
    """
    name: str = field(default="Mi_Go", init=False)
    description: str = field(
        default="Rearrange top 5 cards of deck.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Byakhee(AlienPower):
    """
    Byakhee - Power of Flight.
    You may commit ships from any of your colonies, not just your
    home system, when attacking.
    """
    name: str = field(default="Byakhee", init=False)
    description: str = field(
        default="Attack ships from any colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class YogSothoth(AlienPower):
    """
    Yog-Sothoth - Power of Gates.
    You may move ships freely between your colonies during regroup.
    """
    name: str = field(default="YogSothoth", init=False)
    description: str = field(
        default="Move ships between colonies during regroup.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hastur(AlienPower):
    """
    Hastur - Power Unspeakable.
    You may not be named or discussed during alliance negotiations.
    You cannot be invited to ally, but may join uninvited.
    """
    name: str = field(default="Hastur", init=False)
    description: str = field(
        default="Cannot be invited; may ally uninvited.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Eldritch())
AlienRegistry.register(Harbinger())
AlienRegistry.register(Cthonic())
AlienRegistry.register(Abomination())
AlienRegistry.register(Lurker())
AlienRegistry.register(Dreamer())
AlienRegistry.register(Formless())
AlienRegistry.register(Watcher())
AlienRegistry.register(Devourer())
AlienRegistry.register(Ancient())
AlienRegistry.register(Mindflayer())
AlienRegistry.register(Void_Horror())
AlienRegistry.register(Nyarlathotep())
AlienRegistry.register(Shoggoth())
AlienRegistry.register(Cultist())
AlienRegistry.register(DeepOne())
AlienRegistry.register(Mi_Go())
AlienRegistry.register(Byakhee())
AlienRegistry.register(YogSothoth())
AlienRegistry.register(Hastur())
