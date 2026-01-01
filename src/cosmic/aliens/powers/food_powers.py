"""
Food and Consumption themed alien powers for Cosmic Encounter.
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
class Gourmand(AlienPower):
    """
    Gourmand - Power to Feast.
    After winning an encounter, you may "consume" the losing player's
    encounter card, adding its value to your next attack.
    """
    name: str = field(default="Gourmand", init=False)
    description: str = field(
        default="Win: consume loser's card for next attack bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Nibbler(AlienPower):
    """
    Nibbler - Power of Small Bites.
    Each encounter, you may take 1 card from any player's hand.
    """
    name: str = field(default="Nibbler", init=False)
    description: str = field(
        default="Take 1 card from any hand each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Take a nibble."""
        if not player.power_active:
            return

        targets = [p for p in game.players if p != player and p.hand]
        if targets:
            target = random.choice(targets)
            if target.hand:
                card = random.choice(target.hand)
                target.remove_card(card)
                player.add_card(card)


@dataclass
class Chef(AlienPower):
    """
    Chef - Power to Combine.
    You may play two encounter cards as one, using their combined
    value (but both are discarded).
    """
    name: str = field(default="Chef", init=False)
    description: str = field(
        default="Play two cards as one combined value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Famine(AlienPower):
    """
    Famine - Power of Hunger.
    At the start of each encounter, all other players discard 1 card.
    """
    name: str = field(default="Famine", init=False)
    description: str = field(
        default="Others discard 1 card each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        """Spread famine."""
        if not player.power_active:
            return

        for other in game.players:
            if other != player and other.hand:
                card = random.choice(other.hand)
                other.remove_card(card)
                game.cosmic_deck.discard(card)


@dataclass
class Baker(AlienPower):
    """
    Baker - Power to Create.
    At the start of your turn, draw 2 cards.
    """
    name: str = field(default="Baker", init=False)
    description: str = field(
        default="Draw 2 cards at start of turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Bake some cards."""
        if not player.power_active:
            return

        cards = game.cosmic_deck.draw_multiple(2)
        player.add_cards(cards)


@dataclass
class Cannibal(AlienPower):
    """
    Cannibal - Power to Consume Own.
    You may sacrifice 2 of your ships to draw 4 cards.
    """
    name: str = field(default="Cannibal", init=False)
    description: str = field(
        default="Sacrifice 2 ships: draw 4 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Predator_Food(AlienPower):
    """
    Predator - Power to Hunt.
    +3 attack when attacking a player with fewer ships than you.
    """
    name: str = field(default="Predator_Food", init=False)
    description: str = field(
        default="+3 attack vs players with fewer ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        base_value: int,
        side: Side
    ) -> int:
        """Bonus vs weaker prey."""
        if not player.power_active or side != Side.OFFENSE:
            return base_value

        defender = game.defense
        if defender:
            my_ships = player.total_ships_in_play(game.planets)
            their_ships = defender.total_ships_in_play(game.planets)
            if my_ships > their_ships:
                return base_value + 3
        return base_value


@dataclass
class Herbivore(AlienPower):
    """
    Herbivore - Power of Passive Growth.
    Gain 1 ship at the start of each turn.
    """
    name: str = field(default="Herbivore", init=False)
    description: str = field(
        default="Gain 1 ship at start of turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Farmer(AlienPower):
    """
    Farmer - Power to Cultivate.
    At the end of each round, if you have no ships in warp,
    draw 2 cards.
    """
    name: str = field(default="Farmer", init=False)
    description: str = field(
        default="No ships in warp: draw 2 cards end of round.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Omnivore(AlienPower):
    """
    Omnivore - Power to Eat Anything.
    You may use any card type as an attack card worth 10.
    """
    name: str = field(default="Omnivore", init=False)
    description: str = field(
        default="Any card can be attack 10.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Feast(AlienPower):
    """
    Feast - Power to Share.
    When you win an encounter, each ally on your side draws 2 cards.
    """
    name: str = field(default="Feast", init=False)
    description: str = field(
        default="Win: allies draw 2 cards each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Starvation(AlienPower):
    """
    Starvation - Power of Deprivation.
    Players with no cards in hand have -4 to their encounter total.
    """
    name: str = field(default="Starvation", init=False)
    description: str = field(
        default="Empty-handed players get -4 total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Forager(AlienPower):
    """
    Forager - Power to Find.
    Before drawing from deck, you may look at top 3 and choose 1.
    """
    name: str = field(default="Forager", init=False)
    description: str = field(
        default="Look at top 3 cards, choose 1.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Glutton_Food(AlienPower):
    """
    Glutton - Power of Excess.
    You may hold up to 12 cards (instead of normal hand limit).
    """
    name: str = field(default="Glutton_Food", init=False)
    description: str = field(
        default="Hand limit is 12 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saprophyte(AlienPower):
    """
    Saprophyte - Power of Decay.
    Whenever cards are discarded, you may take one.
    """
    name: str = field(default="Saprophyte", init=False)
    description: str = field(
        default="Take discarded cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Gourmand())
AlienRegistry.register(Nibbler())
AlienRegistry.register(Chef())
AlienRegistry.register(Famine())
AlienRegistry.register(Baker())
AlienRegistry.register(Cannibal())
AlienRegistry.register(Predator_Food())
AlienRegistry.register(Herbivore())
AlienRegistry.register(Farmer())
AlienRegistry.register(Omnivore())
AlienRegistry.register(Feast())
AlienRegistry.register(Starvation())
AlienRegistry.register(Forager())
AlienRegistry.register(Glutton_Food())
AlienRegistry.register(Saprophyte())
