"""
Strategic Powers - Aliens with complex decision-making abilities.

These powers focus on information, timing, and tactical advantages.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Analyst(AlienPower):
    """
    Analyst - Information Gatherer.
    At the start of each encounter, look at the top 3 cards of the cosmic deck.
    """
    name: str = field(default="Analyst", init=False)
    description: str = field(default="Peek at cosmic deck before encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_destiny_drawn(self, game: "Game", player: "Player") -> None:
        """Peek at the deck."""
        if game.offense == player or game.defense == player:
            cards = game.cosmic_deck.peek(3)
            # AI can use this information for decisions


@dataclass
class Broker(AlienPower):
    """
    Broker - Deal Maker.
    When making a deal, you may trade cards instead of colonies.
    """
    name: str = field(default="Broker", init=False)
    description: str = field(default="Trade cards instead of colonies in deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Conductor(AlienPower):
    """
    Conductor - Orchestrator.
    Your allies may send up to 5 ships instead of 4.
    """
    name: str = field(default="Conductor", init=False)
    description: str = field(default="Your allies may send 5 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Deflector(AlienPower):
    """
    Deflector - Redirect.
    When targeted by destiny, you may redirect the encounter to another player.
    """
    name: str = field(default="Deflector", init=False)
    description: str = field(default="Redirect encounters targeting you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Embargo(AlienPower):
    """
    Embargo - Isolationist.
    Once per encounter, you may prevent one player from allying.
    """
    name: str = field(default="Embargo", init=False)
    description: str = field(default="Prevent one player from allying.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Forecaster(AlienPower):
    """
    Forecaster - Predictor.
    Before cards are revealed, you may guess the opponent's card type.
    If correct, add +5 to your total.
    """
    name: str = field(default="Forecaster", init=False)
    description: str = field(default="Guess opponent's card type for bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add bonus if prediction would be correct (simplified: random)."""
        import random
        if random.random() < 0.4:  # 40% chance of correct guess
            return total + 5
        return total


@dataclass
class Guarantor(AlienPower):
    """
    Guarantor - Promise Keeper.
    Deals you make cannot fail. Both parties must complete the deal.
    """
    name: str = field(default="Guarantor", init=False)
    description: str = field(default="Your deals always succeed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Harbinger(AlienPower):
    """
    Harbinger - Omen Bringer.
    At the start of your turn, name an alien. That alien cannot use their power.
    """
    name: str = field(default="Harbinger", init=False)
    description: str = field(default="Disable one alien power per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Insider(AlienPower):
    """
    Insider - Information Trader.
    You may look at any player's hand once per encounter.
    """
    name: str = field(default="Insider", init=False)
    description: str = field(default="Look at one player's hand per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jailer(AlienPower):
    """
    Jailer - Warden.
    Ships you send to warp stay in a separate prison.
    You retrieve them all when you have 3 or more.
    """
    name: str = field(default="Jailer", init=False)
    description: str = field(default="Ships in warp form a prison; retrieve at 3+.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player") -> None:
        """Check if we have enough ships to release."""
        if player.ships_in_warp >= 3:
            ships = player.retrieve_ships_from_warp(player.ships_in_warp)
            player.return_ships_to_colonies(ships, player.home_planets)


@dataclass
class Kibitzer(AlienPower):
    """
    Kibitzer - Advice Giver.
    When not involved, you may add +2 to either side's total.
    """
    name: str = field(default="Kibitzer", init=False)
    description: str = field(default="Add +2 to either side when not involved.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Locksmith(AlienPower):
    """
    Locksmith - Key Master.
    You may free ships from any player's warp.
    """
    name: str = field(default="Locksmith", init=False)
    description: str = field(default="Free ships from any warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mentor(AlienPower):
    """
    Mentor - Teacher.
    Your allies draw 1 card when they join your side.
    """
    name: str = field(default="Mentor", init=False)
    description: str = field(default="Allies draw 1 card when joining.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Negotiator(AlienPower):
    """
    Negotiator - Deal Expert.
    When making deals, you may exchange 2 colonies instead of 1.
    """
    name: str = field(default="Negotiator", init=False)
    description: str = field(default="Exchange 2 colonies in deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Obstinate(AlienPower):
    """
    Obstinate - Stubborn.
    Once per encounter, you may ignore the effects of one artifact.
    """
    name: str = field(default="Obstinate", init=False)
    description: str = field(default="Ignore one artifact per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pragmatist(AlienPower):
    """
    Pragmatist - Practical One.
    You may use negotiate cards as Attack 10.
    """
    name: str = field(default="Pragmatist", init=False)
    description: str = field(default="Negotiates count as Attack 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quorum(AlienPower):
    """
    Quorum - Majority Rule.
    You win ties. If you have the most allies, add +3.
    """
    name: str = field(default="Quorum", init=False)
    description: str = field(default="Win ties; +3 if most allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add bonus if we have the most allies."""
        if side == Side.OFFENSE:
            my_allies = len(game.offense_allies)
            opp_allies = len(game.defense_allies)
        else:
            my_allies = len(game.defense_allies)
            opp_allies = len(game.offense_allies)

        if my_allies > opp_allies:
            return total + 3
        return total


@dataclass
class Recycler(AlienPower):
    """
    Recycler - Waste Reducer.
    When cards are discarded, you may take one of them.
    """
    name: str = field(default="Recycler", init=False)
    description: str = field(default="Take one discarded card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Supplier(AlienPower):
    """
    Supplier - Resource Provider.
    At the start of each turn, draw 1 card.
    """
    name: str = field(default="Supplier", init=False)
    description: str = field(default="Draw 1 card at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Draw a card."""
        card = game.cosmic_deck.draw()
        player.add_card(card)


@dataclass
class Tactician(AlienPower):
    """
    Tactician - Strategic Planner.
    After seeing opponent's card, you may change your card.
    """
    name: str = field(default="Tactician", init=False)
    description: str = field(default="Change card after seeing opponent's.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Unifier(AlienPower):
    """
    Unifier - Coalition Builder.
    All players may ally with both sides.
    """
    name: str = field(default="Unifier", init=False)
    description: str = field(default="Players may ally with both sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Veto(AlienPower):
    """
    Veto - Blocker.
    Once per turn, cancel one player's power use.
    """
    name: str = field(default="Veto", init=False)
    description: str = field(default="Cancel one power use per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Watcher(AlienPower):
    """
    Watcher - Observer.
    You always see which cards other players are selecting.
    """
    name: str = field(default="Watcher", init=False)
    description: str = field(default="See which cards others select.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Xenophile(AlienPower):
    """
    Xenophile - Alien Lover.
    You may use any one alien's power once per game.
    """
    name: str = field(default="Xenophile", init=False)
    description: str = field(default="Use any power once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Yardmaster(AlienPower):
    """
    Yardmaster - Ship Commander.
    Ships on your home system count double for defense.
    """
    name: str = field(default="Yardmaster", init=False)
    description: str = field(default="Home ships count double for defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        """Double ships when defending at home."""
        if side == Side.DEFENSE and game.defense_planet and game.defense_planet.owner == player:
            return count * 2
        return count


@dataclass
class Zealotry(AlienPower):
    """
    Zealotry - Fanatic.
    When you lose an encounter, you may immediately start another.
    """
    name: str = field(default="Zealotry", init=False)
    description: str = field(default="Start new encounter when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Analyst())
AlienRegistry.register(Broker())
AlienRegistry.register(Conductor())
AlienRegistry.register(Deflector())
AlienRegistry.register(Embargo())
AlienRegistry.register(Forecaster())
AlienRegistry.register(Guarantor())
AlienRegistry.register(Harbinger())
AlienRegistry.register(Insider())
AlienRegistry.register(Jailer())
AlienRegistry.register(Kibitzer())
AlienRegistry.register(Locksmith())
AlienRegistry.register(Mentor())
AlienRegistry.register(Negotiator())
AlienRegistry.register(Obstinate())
AlienRegistry.register(Pragmatist())
AlienRegistry.register(Quorum())
AlienRegistry.register(Recycler())
AlienRegistry.register(Supplier())
AlienRegistry.register(Tactician())
AlienRegistry.register(Unifier())
AlienRegistry.register(Veto())
AlienRegistry.register(Watcher())
AlienRegistry.register(Xenophile())
AlienRegistry.register(Yardmaster())
AlienRegistry.register(Zealotry())
