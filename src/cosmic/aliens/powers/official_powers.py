"""
Official Cosmic Encounter alien powers from Fantasy Flight Games.

Contains all 238 aliens from:
- Base Game (2008): 50 aliens
- Cosmic Incursion (2010): 20 aliens
- Cosmic Conflict (2011): 20 aliens
- Cosmic Alliance (2012): 20 aliens
- Cosmic Storm (2013): 25 aliens
- Cosmic Dominion (2014): 30 aliens
- Cosmic Eons (2016): 30 aliens
- Cosmic Odyssey (2022): 42 aliens (includes alternate versions)
- Promos: 1 alien
"""

from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING, Any, Dict

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Expansion, Side
from ..registry import AlienRegistry

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


# =============================================================================
# BASE GAME ALIENS (50)
# =============================================================================

@dataclass
class Amoeba(AlienPower):
    """You have the power to Ooze. As a main player, after alliances are formed,
    you may add up to four ships from any of your other colonies to your side."""
    name: str = field(default="Amoeba", init=False)
    description: str = field(default="Add ships from other colonies to encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        """Add up to 4 extra ships from other colonies."""
        # Get ships from other colonies (up to 4 extra)
        extra_ships = min(4, player.total_ships_in_play(game.planets) - base_count)
        if extra_ships > 0:
            # Actually remove ships from colonies
            taken = player.get_ships_from_colonies(extra_ships, game.planets)
            return base_count + taken
        return base_count


@dataclass
class Antimatter(AlienPower):
    """You have the power of Negation. As a main player, when totals are compared,
    the lower total wins instead of the higher."""
    name: str = field(default="Antimatter", init=False)
    description: str = field(default="Lower total wins instead of higher.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Barbarian(AlienPower):
    """You have the power to Pillage. As offense, if you lose the encounter,
    you still collect compensation from the defense."""
    name: str = field(default="Barbarian", init=False)
    description: str = field(default="Collect compensation even when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        """Collect compensation from defense when losing as offense."""
        if as_main_player and game.offense == player and game.defense:
            # Get ships lost count for compensation
            ships_lost = game.offense_ships.get(player.name, 0)
            if ships_lost > 0 and len(game.defense.hand) > 0:
                compensation = min(ships_lost, len(game.defense.hand))
                cards = game._rng.sample(game.defense.hand, compensation)
                for card in cards:
                    game.defense.hand.remove(card)
                player.add_cards(cards)


@dataclass
class Calculator(AlienPower):
    """You have the power to Calculate. As a main player, before cards are selected,
    you may announce a total. If your announced total matches your final total exactly,
    you automatically win."""
    name: str = field(default="Calculator", init=False)
    description: str = field(default="Win by predicting exact total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Chosen(AlienPower):
    """You have the power of Destiny. As offense, instead of drawing from the destiny
    deck, you may choose any player to have an encounter against."""
    name: str = field(default="Chosen", init=False)
    description: str = field(default="Choose encounter target instead of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Citadel(AlienPower):
    """You have the power to Fortify. As defense, each of your ships on the targeted
    planet counts as two ships."""
    name: str = field(default="Citadel", init=False)
    description: str = field(default="Defending ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        """As defense, Citadel's ships count double."""
        if side != Side.DEFENSE:
            return base_count
        # Get Citadel's ship count
        citadel_ships = game.defense_ships.get(player.name, 0)
        # Other players' ships count normally, Citadel's ships count double
        ally_ships = base_count - citadel_ships
        return ally_ships + (citadel_ships * 2)


@dataclass
class Clone(AlienPower):
    """You have the power to Replicate. Whenever you lose an encounter card to the
    discard pile, you may immediately retrieve it to your hand."""
    name: str = field(default="Clone", init=False)
    description: str = field(default="Retrieve encounter cards after playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_discard_card(self, game: "Game", player: "Player", card: Any) -> bool:
        """Retrieve encounter cards instead of discarding them."""
        from ...cards.base import EncounterCard
        if isinstance(card, EncounterCard):
            player.add_cards([card])
            return False  # Prevent discard
        return True  # Allow other cards to discard


@dataclass
class Cudgel(AlienPower):
    """You have the power to Stun. As a main player, after cards are selected but
    before they are revealed, you may force your opponent to play their lowest
    encounter card instead."""
    name: str = field(default="Cudgel", init=False)
    description: str = field(default="Force opponent to play lowest card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Dictator(AlienPower):
    """You have the power to Oppress. As a main player, you control where your
    allies' ships are placed during the encounter."""
    name: str = field(default="Dictator", init=False)
    description: str = field(default="Control ally ship placement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fido(AlienPower):
    """You have the power to Fetch. Once per encounter, you may retrieve any one
    card from the discard pile and add it to your hand."""
    name: str = field(default="Fido", init=False)
    description: str = field(default="Retrieve card from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Filch(AlienPower):
    """You have the power to Steal. As a main player, before cards are selected,
    you may randomly draw one card from your opponent's hand and add it to yours."""
    name: str = field(default="Filch", init=False)
    description: str = field(default="Steal random card from opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fodder(AlienPower):
    """You have the power to Sacrifice. As offense, after cards are revealed,
    you may send any of your ships from the encounter to the warp to add 1 to
    your total for each ship sacrificed."""
    name: str = field(default="Fodder", init=False)
    description: str = field(default="Sacrifice ships for +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Sacrifice ships for +1 each (AI decides to sacrifice half, rounded down)."""
        if side != Side.OFFENSE:
            return base_total
        ships_in_encounter = game.offense_ships.get(player.name, 0)
        # AI strategy: sacrifice half of ships if losing
        to_sacrifice = ships_in_encounter // 2
        if to_sacrifice > 0:
            game.offense_ships[player.name] = ships_in_encounter - to_sacrifice
            player.send_ships_to_warp(to_sacrifice)
            return base_total + to_sacrifice
        return base_total


@dataclass
class Gambler(AlienPower):
    """You have the power to Risk. As a main player, after cards are revealed,
    you may draw a card from the deck. If it's an encounter card, swap it with
    your played card; otherwise, discard it."""
    name: str = field(default="Gambler", init=False)
    description: str = field(default="Risk drawing to replace played card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Grudge(AlienPower):
    """You have the power of Vendetta. Place a grudge token on any player who
    wins an encounter against you. You get +4 against players with grudge tokens."""
    name: str = field(default="Grudge", init=False)
    description: str = field(default="+4 against players who defeated you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        """Place a grudge token on the player who defeated Grudge."""
        if as_main_player:
            opponent = game.defense if game.offense == player else game.offense
            if opponent:
                if not hasattr(player, 'grudge_tokens'):
                    player.grudge_tokens = set()
                player.grudge_tokens.add(opponent.name)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Add +4 against players with grudge tokens."""
        opponent = game.defense if game.offense == player else game.offense
        if opponent and hasattr(player, 'grudge_tokens') and opponent.name in player.grudge_tokens:
            return base_total + 4
        return base_total


@dataclass
class Hacker(AlienPower):
    """You have the power to Peek. As a main player, before cards are selected,
    you may look at your opponent's hand and choose which card they must play."""
    name: str = field(default="Hacker", init=False)
    description: str = field(default="See opponent's hand and choose their card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Hate(AlienPower):
    """You have the power of Vengeance. You get +1 for each ship you have lost
    in previous encounters against your current opponent this game."""
    name: str = field(default="Hate", init=False)
    description: str = field(default="+1 per ship lost to current opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        """Track ships lost to each opponent."""
        if as_main_player:
            opponent = game.defense if game.offense == player else game.offense
            ships_lost = game.offense_ships.get(player.name, 0) if game.offense == player else game.defense_ships.get(player.name, 0)
            if opponent and ships_lost > 0:
                if not hasattr(player, 'hate_ships_lost'):
                    player.hate_ships_lost = {}
                player.hate_ships_lost[opponent.name] = player.hate_ships_lost.get(opponent.name, 0) + ships_lost

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Add +1 per ship previously lost to current opponent."""
        opponent = game.defense if game.offense == player else game.offense
        if opponent and hasattr(player, 'hate_ships_lost'):
            ships_lost = player.hate_ships_lost.get(opponent.name, 0)
            return base_total + ships_lost
        return base_total


@dataclass
class Healer(AlienPower):
    """You have the power to Heal. Whenever any player's ships would go to the warp,
    you may prevent up to 3 of them from going, returning them to colonies instead."""
    name: str = field(default="Healer", init=False)
    description: str = field(default="Save ships from going to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        """Save up to 3 ships from going to warp, returning them to colonies."""
        saved = min(3, count)
        if saved > 0:
            player.return_ships_to_colonies(saved, player.home_planets)
        return count - saved


@dataclass
class Human(AlienPower):
    """You have the power of Humanity. As a main player, you may add 4 to your
    total after encounter cards are revealed."""
    name: str = field(default="Human", init=False)
    description: str = field(default="+4 to encounter total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: "Side") -> int:
        """Add +4 to total as main player."""
        return base_total + 4


@dataclass
class Kamikaze(AlienPower):
    """You have the power of Self-Destruction. As offense, after alliances are formed,
    you may triple the value of your ships (each counts as 3) but all your ships in
    the encounter go to the warp regardless of outcome."""
    name: str = field(default="Kamikaze", init=False)
    description: str = field(default="Triple ship value but lose them all.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Loser(AlienPower):
    """You have the power to Win by Losing. As a main player, if you would lose
    an encounter, you win instead (and vice versa)."""
    name: str = field(default="Loser", init=False)
    description: str = field(default="Win when you would lose, lose when you would win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Machine(AlienPower):
    """You have the power of Continuity. As offense, after every encounter,
    regardless of the outcome, you may have an additional encounter."""
    name: str = field(default="Machine", init=False)
    description: str = field(default="Extra encounter after any encounter, win or lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Macron(AlienPower):
    """You have the power of Mass. Each of your ships counts as 4 instead of 1.
    You may only have 1-4 ships in any encounter."""
    name: str = field(default="Macron", init=False)
    description: str = field(default="Ships count as 4 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        """Each of Macron's ships counts as 4 instead of 1."""
        # Get Macron's ship count from the appropriate side
        if side == Side.OFFENSE:
            macron_ships = game.offense_ships.get(player.name, 0)
        else:
            macron_ships = game.defense_ships.get(player.name, 0)
        # Other players' ships count normally, Macron's ships count as 4 each
        ally_ships = base_count - macron_ships
        return ally_ships + (macron_ships * 4)


@dataclass
class Masochist(AlienPower):
    """You have the power to Enjoy Pain. Whenever you lose ships to the warp,
    draw one card for each ship lost."""
    name: str = field(default="Masochist", init=False)
    description: str = field(default="Draw card per ship sent to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        """Draw a card for each ship going to warp."""
        if count > 0:
            cards = game.cosmic_deck.draw_multiple(count)
            player.add_cards(cards)
        # Ships still go to warp normally
        return count


@dataclass
class Mind(AlienPower):
    """You have the power of Foresight. As a main player, before cards are selected,
    you may look at your opponent's hand."""
    name: str = field(default="Mind", init=False)
    description: str = field(default="See opponent's hand before selecting.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Mirror(AlienPower):
    """You have the power to Copy. As a main player, you may use your opponent's
    alien power instead of your own for this encounter."""
    name: str = field(default="Mirror", init=False)
    description: str = field(default="Use opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Miser(AlienPower):
    """You have the power to Hoard. Whenever you draw a new hand, you may keep
    one card from your old hand."""
    name: str = field(default="Miser", init=False)
    description: str = field(default="Keep one card when drawing new hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Mite(AlienPower):
    """You have the power of Infection. You cannot ally normally. Instead, before
    alliances, place one of your ships on any planet in the encounter. If your side
    wins, your ship stays; otherwise, it goes to warp."""
    name: str = field(default="Mite", init=False)
    description: str = field(default="Place ship instead of allying normally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Mutant(AlienPower):
    """You have the power to Mutate. Once per encounter, you may discard your hand
    and draw 8 new cards."""
    name: str = field(default="Mutant", init=False)
    description: str = field(default="Discard hand and draw 8 new cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Observer(AlienPower):
    """You have the power to Watch. Whenever you are not a main player or ally,
    you draw one card from the deck."""
    name: str = field(default="Observer", init=False)
    description: str = field(default="Draw card when not in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.NOT_INVOLVED], init=False)

    def on_resolution(self, game: "Game", player: "Player", role: "PlayerRole") -> None:
        """Draw a card when not involved in the encounter."""
        if role == PlayerRole.NOT_INVOLVED:
            card = game.cosmic_deck.draw()
            if card:
                player.add_cards([card])


@dataclass
class Oracle(AlienPower):
    """You have the power to Foresee. As a main player, your opponent must play
    their encounter card face-up while yours remains hidden until reveal."""
    name: str = field(default="Oracle", init=False)
    description: str = field(default="Opponent plays card face-up.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Pacifist(AlienPower):
    """You have the power of Peace. As a main player, if you play a negotiate card
    and your opponent plays an attack card, you win the encounter."""
    name: str = field(default="Pacifist", init=False)
    description: str = field(default="Win when playing negotiate against attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Parasite(AlienPower):
    """You have the power to Infest. You may join either side of any encounter
    uninvited, adding your ships to that side."""
    name: str = field(default="Parasite", init=False)
    description: str = field(default="Join any encounter uninvited.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Philanthropist(AlienPower):
    """You have the power to Give. At the start of each encounter, you must give
    one card from your hand to another player. For each card given this way, draw one."""
    name: str = field(default="Philanthropist", init=False)
    description: str = field(default="Must give cards but draw replacements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Reincarnator(AlienPower):
    """You have the power to be Reborn. When you lose your last home colony,
    discard your alien sheet and draw a new one."""
    name: str = field(default="Reincarnator", init=False)
    description: str = field(default="Get new alien when losing last home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Remora(AlienPower):
    """You have the power to Suck. Whenever any player receives cards from the deck
    or as compensation, you receive one card too."""
    name: str = field(default="Remora", init=False)
    description: str = field(default="Get card when others draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_draw_card(self, game: "Game", player: "Player", card: Any) -> Any:
        """When any other player draws, Remora gets a card too.
        Note: This is called when Remora draws - game.py handles Remora logic."""
        return card

    def on_compensation(self, game: "Game", player: "Player", from_player: "Player", count: int) -> int:
        """Draw an extra card when receiving compensation."""
        extra = game.cosmic_deck.draw()
        if extra:
            player.add_cards([extra])
        return count


@dataclass
class Reserve(AlienPower):
    """You have the power to Delay. As a main player, you may call for allies
    before selecting encounter cards."""
    name: str = field(default="Reserve", init=False)
    description: str = field(default="Call allies before selecting cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Shadow(AlienPower):
    """You have the power to Lurk. After encounter cards are revealed, you may
    join the winning side as an ally (even if not invited)."""
    name: str = field(default="Shadow", init=False)
    description: str = field(default="Join winning side after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Sorcerer(AlienPower):
    """You have the power to Switch. As a main player, after cards are selected
    but before reveal, you may switch encounter cards with your opponent."""
    name: str = field(default="Sorcerer", init=False)
    description: str = field(default="Switch cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Spiff(AlienPower):
    """You have the power to Crash Land. As offense, when you lose an encounter,
    one of your ships from the gate may land on the targeted planet anyway."""
    name: str = field(default="Spiff", init=False)
    description: str = field(default="Land one ship even when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class TickTock(AlienPower):
    """You have the power of Time. Place 10 tokens on this sheet at game start.
    Remove one each encounter. If reduced to 0 and you have at least one foreign colony,
    you win alone."""
    name: str = field(default="TickTock", init=False)
    description: str = field(default="Win alone after 10 encounters if foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    has_alternate_win: bool = True


@dataclass
class Trader(AlienPower):
    """You have the power to Trade. As a main player, before cards are selected,
    you may swap hands with any other player."""
    name: str = field(default="Trader", init=False)
    description: str = field(default="Swap hands with any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Tripler(AlienPower):
    """You have the power to Triple. As a main player, your encounter card value
    is tripled."""
    name: str = field(default="Tripler", init=False)
    description: str = field(default="Triple encounter card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)

    def modify_attack_value(self, game: "Game", player: "Player", base_value: int, side: Side) -> int:
        """Triple the encounter card value."""
        return base_value * 3


@dataclass
class Vacuum(AlienPower):
    """You have the power to Suck In. When you win an encounter, losing ships go
    to your colonies as prisoners instead of the warp."""
    name: str = field(default="Vacuum", init=False)
    description: str = field(default="Capture losing ships as prisoners.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Virus(AlienPower):
    """You have the power to Multiply. As a main player, multiply your encounter
    card value by your number of ships instead of adding them."""
    name: str = field(default="Virus", init=False)
    description: str = field(default="Multiply card by ships instead of adding.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        """Ships don't add to total - they multiply the card value instead."""
        return 0

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Multiply card value by ship count."""
        # base_total is just the card value since ships were set to 0
        # Get original ship count from game state
        if side == Side.OFFENSE:
            ship_count = sum(game.offense_ships.values())
        else:
            ship_count = sum(game.defense_ships.values())
        # Multiply instead of add (base_total is card value, multiply by ships)
        return base_total * ship_count


@dataclass
class Void(AlienPower):
    """You have the power to Eradicate. When you win an encounter, losing ships
    are removed from the game instead of going to the warp."""
    name: str = field(default="Void", init=False)
    description: str = field(default="Remove losing ships from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Vulch(AlienPower):
    """You have the power to Scrounge. Whenever any player plays an artifact card,
    you may take it for yourself instead of it going to the discard pile."""
    name: str = field(default="Vulch", init=False)
    description: str = field(default="Take played artifacts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)


@dataclass
class Warpish(AlienPower):
    """You have the power of Warp Speed. Ships you have in the warp may be added
    to your side in encounters as if they were in your colonies."""
    name: str = field(default="Warpish", init=False)
    description: str = field(default="Use warp ships in encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        """Add ships from warp to encounter (up to 4 extra)."""
        warp_ships = min(4, player.ships_in_warp)
        if warp_ships > 0:
            player.ships_in_warp -= warp_ships
            return base_count + warp_ships
        return base_count


@dataclass
class Warrior(AlienPower):
    """You have the power of the Bonus. For each ship you have in the warp, add
    1 to your total as a main player."""
    name: str = field(default="Warrior", init=False)
    description: str = field(default="+1 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Add +1 per ship in warp."""
        return base_total + player.ships_in_warp


@dataclass
class Will(AlienPower):
    """You have the power of Willpower. As a main player, after encounter cards
    are revealed, you may force both players to play the same card type next encounter."""
    name: str = field(default="Will", init=False)
    description: str = field(default="Force same card type next encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Zombie(AlienPower):
    """You have the power of Immortality. Your ships never go to the warp. Instead,
    return them to any of your colonies."""
    name: str = field(default="Zombie", init=False)
    description: str = field(default="Ships return to colonies instead of warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        """Ships never go to warp - return them to colonies instead."""
        # Return ships to colonies instead of warp
        if count > 0:
            player.return_ships_to_colonies(count, player.home_planets)
        # Return 0 to prevent ships from going to warp
        return 0


# =============================================================================
# COSMIC INCURSION ALIENS (20)
# =============================================================================

@dataclass
class Bully(AlienPower):
    """You have the power to Intimidate. As a main player against an opponent with
    fewer ships in the encounter, you may force them to negotiate."""
    name: str = field(default="Bully", init=False)
    description: str = field(default="Force weaker opponent to negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Chronos(AlienPower):
    """You have the power of Time Travel. After an encounter ends, you may undo
    everything and replay the encounter from the start."""
    name: str = field(default="Chronos", init=False)
    description: str = field(default="Replay encounter from start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Cryo(AlienPower):
    """You have the power to Preserve. Ships you lose go to your alien sheet frozen
    instead of the warp. Return them to colonies when you win an encounter."""
    name: str = field(default="Cryo", init=False)
    description: str = field(default="Freeze lost ships, thaw on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        """Freeze ships instead of sending to warp."""
        if count > 0:
            if not hasattr(player, 'frozen_ships'):
                player.frozen_ships = 0
            player.frozen_ships += count
        return 0  # No ships go to warp

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        """Thaw frozen ships when winning."""
        frozen = getattr(player, 'frozen_ships', 0)
        if frozen > 0:
            player.return_ships_to_colonies(frozen, player.home_planets)
            player.frozen_ships = 0


@dataclass
class Deuce(AlienPower):
    """You have the power of Duality. As a main player, you may play two encounter
    cards and use the total of both."""
    name: str = field(default="Deuce", init=False)
    description: str = field(default="Play two encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Disease(AlienPower):
    """You have the power of Contagion. When you win an encounter, place disease
    tokens on opponent. Each token gives -1 in future encounters."""
    name: str = field(default="Disease", init=False)
    description: str = field(default="Infect opponents with -1 tokens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Ethic(AlienPower):
    """You have the power of Guilt. As a main player, allies on the opposing side
    must give you one card or one ship."""
    name: str = field(default="Ethic", init=False)
    description: str = field(default="Opposing allies pay you tribute.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Fungus(AlienPower):
    """You have the power to Adhere. Ships that ally with you remain in the
    encounter for subsequent encounters this turn."""
    name: str = field(default="Fungus", init=False)
    description: str = field(default="Allied ships stick for multiple encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Fury(AlienPower):
    """You have the power of Rage. Each time you lose ships, gain +2 to your
    total for the rest of the game (cumulative)."""
    name: str = field(default="Fury", init=False)
    description: str = field(default="Permanent +2 each time you lose ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        """Gain +2 rage each time ships go to warp."""
        if count > 0:
            if not hasattr(player, 'fury_rage'):
                player.fury_rage = 0
            player.fury_rage += 2
        return count

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Add accumulated rage to total."""
        rage = getattr(player, 'fury_rage', 0)
        return base_total + rage


@dataclass
class Genius(AlienPower):
    """You have the power to Outwit. Before cards are revealed, predict opponent's
    card value. If correct, win automatically."""
    name: str = field(default="Genius", init=False)
    description: str = field(default="Win by predicting opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Ghoul(AlienPower):
    """You have the power to Feast. When ships go to the warp, draw one card from
    the deck for every three ships that went there."""
    name: str = field(default="Ghoul", init=False)
    description: str = field(default="Draw card per 3 ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        """Draw cards based on ships that went to warp this encounter.
        Note: Ghoul triggers on any ships going to warp, tracked at encounter end."""
        # Count total ships in warp from all players at end of encounter
        total_to_warp = 0
        for p in game.players:
            # Track ships sent to warp during this encounter
            if hasattr(p, '_ships_to_warp_this_encounter'):
                total_to_warp += p._ships_to_warp_this_encounter
                p._ships_to_warp_this_encounter = 0
        cards_to_draw = total_to_warp // 3
        if cards_to_draw > 0:
            cards = game.cosmic_deck.draw_multiple(cards_to_draw)
            player.add_cards(cards)


@dataclass
class Guerrilla(AlienPower):
    """You have the power of Attrition. As a main player, before cards are revealed,
    you may send one opposing ship to the warp."""
    name: str = field(default="Guerrilla", init=False)
    description: str = field(default="Send one opposing ship to warp before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Leviathan(AlienPower):
    """You have the power of Worldships. Your home planets can move. As offense,
    you may move one home planet to the targeted system."""
    name: str = field(default="Leviathan", init=False)
    description: str = field(default="Move home planets to other systems.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Locust(AlienPower):
    """You have the power to Devour. When you win an encounter as offense,
    remove the colony - no one can have ships there."""
    name: str = field(default="Locust", init=False)
    description: str = field(default="Destroy planets you conquer.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Magician(AlienPower):
    """You have the power of Prestidigitation. As a main player, after reveal,
    make your played card disappear and draw a new one to play instead."""
    name: str = field(default="Magician", init=False)
    description: str = field(default="Replace played card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Mercenary(AlienPower):
    """You have the power of Bounty Hunting. When allying, the main player must
    pay you one card per ship you commit, or you don't ally."""
    name: str = field(default="Mercenary", init=False)
    description: str = field(default="Get paid to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Merchant(AlienPower):
    """You have the power to Trade. Once per encounter, you may buy a card from
    any player for one of your ships (their choice of which card)."""
    name: str = field(default="Merchant", init=False)
    description: str = field(default="Buy cards with ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Plant(AlienPower):
    """You have the power of Grafting. Ships you commit to successful offensive
    encounters stay on the planet as permanent roots, not returning to colonies."""
    name: str = field(default="Plant", init=False)
    description: str = field(default="Establish permanent presence on planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Seeker(AlienPower):
    """You have the power of Truth. Once per encounter, you may ask any player
    a yes/no question about their hand. They must answer honestly."""
    name: str = field(default="Seeker", init=False)
    description: str = field(default="Ask truthful questions about hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Sniveler(AlienPower):
    """You have the power to Whine. At the start of each encounter, if you have
    fewer home colonies than another player, draw two cards."""
    name: str = field(default="Sniveler", init=False)
    description: str = field(default="Draw cards when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


@dataclass
class Symbiote(AlienPower):
    """You have the power of Bonding. At game start, bond with another player.
    You share colonies - when either wins, both get the benefit."""
    name: str = field(default="Symbiote", init=False)
    description: str = field(default="Share victories with bonded player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_INCURSION, init=False)


# =============================================================================
# COSMIC CONFLICT ALIENS (20)
# =============================================================================

@dataclass
class Cavalry(AlienPower):
    """You have the power to Rescue. At the end of every encounter, you may retrieve
    one ship from the warp to any colony."""
    name: str = field(default="Cavalry", init=False)
    description: str = field(default="Retrieve one ship from warp each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Changeling(AlienPower):
    """You have the power to Transform. When your flare is played, you may exchange
    alien powers with any other player."""
    name: str = field(default="Changeling", init=False)
    description: str = field(default="Exchange powers when flare played.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Empath(AlienPower):
    """You have the power to Sense. As a main player, before cards are revealed,
    you may sense if your opponent's card is higher or lower than 10."""
    name: str = field(default="Empath", init=False)
    description: str = field(default="Sense if opponent's card is high or low.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Filth(AlienPower):
    """You have the power to Disgust. Whenever you lose ships in an encounter,
    your opponent must discard one card per ship you lost."""
    name: str = field(default="Filth", init=False)
    description: str = field(default="Force opponent to discard when you lose ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Glutton(AlienPower):
    """You have the power to Devour. When you draw cards, draw double and keep half."""
    name: str = field(default="Glutton", init=False)
    description: str = field(default="Draw double, keep half.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Graviton(AlienPower):
    """You have the power to Pull. As a main player, after alliances are formed,
    you may use this power. If you do, ships may not retreat this encounter.
    Ships that would be lost to the warp are instead removed from the game."""
    name: str = field(default="Graviton", init=False)
    description: str = field(default="Destroys losing ships instead of warping them.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Industrialist(AlienPower):
    """You have the power of Production. At the start of your turn, draw one card
    for each colony you have (home and foreign)."""
    name: str = field(default="Industrialist", init=False)
    description: str = field(default="Draw card per colony at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Invader(AlienPower):
    """You have the power to Intrude. As offense, you may launch to any planet
    regardless of destiny."""
    name: str = field(default="Invader", init=False)
    description: str = field(default="Launch to any planet ignoring destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Lunatic(AlienPower):
    """You have the power of Insanity. At the start of each encounter, randomly
    determine your encounter card from your hand."""
    name: str = field(default="Lunatic", init=False)
    description: str = field(default="Play random encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Mimic(AlienPower):
    """You have the power to Imitate. As a main player, you may use any one game
    power that has been zapped this game."""
    name: str = field(default="Mimic", init=False)
    description: str = field(default="Use zapped powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Prophet(AlienPower):
    """You have the power of Prophecy. Before destiny is drawn, predict the color.
    If correct, gain a colony token."""
    name: str = field(default="Prophet", init=False)
    description: str = field(default="Predict destiny for bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Relic(AlienPower):
    """You have the power of the Ancients. Start with an additional artifact card.
    When you play artifacts, retrieve them instead of discarding."""
    name: str = field(default="Relic", init=False)
    description: str = field(default="Keep artifacts after playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Saboteur(AlienPower):
    """You have the power to Undermine. As a main player, after cards are revealed,
    you may discard an artifact to cancel your opponent's card."""
    name: str = field(default="Saboteur", init=False)
    description: str = field(default="Discard artifact to cancel opponent's card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Sadist(AlienPower):
    """You have the power to Torment. When you win an encounter, you may send
    one additional opposing ship to the warp."""
    name: str = field(default="Sadist", init=False)
    description: str = field(default="Send extra ship to warp on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Siren(AlienPower):
    """You have the power to Lure. As a main player, you may force one ally to
    switch sides."""
    name: str = field(default="Siren", init=False)
    description: str = field(default="Force ally to switch sides.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Claw(AlienPower):
    """You have the power to Snatch. When an opponent plays a negotiate, you may
    take two cards from their hand instead of normal compensation."""
    name: str = field(default="Claw", init=False)
    description: str = field(default="Take two cards when opponent negotiates.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Trickster(AlienPower):
    """You have the power to Fool. As a main player, you may play an encounter
    card face-down without looking at it."""
    name: str = field(default="Trickster", init=False)
    description: str = field(default="Play card without seeing it.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Visionary(AlienPower):
    """You have the power to See Ahead. Look at the top three destiny cards
    at game start. You may reorder them."""
    name: str = field(default="Visionary", init=False)
    description: str = field(default="See and reorder top destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


@dataclass
class Warhawk(AlienPower):
    """You have the power of Aggression. As offense, after destiny, you may
    declare a second simultaneous encounter."""
    name: str = field(default="Warhawk", init=False)
    description: str = field(default="Launch two simultaneous encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Xenophile(AlienPower):
    """You have the power to Attract. Whenever another player becomes your ally,
    you draw one card."""
    name: str = field(default="Xenophile", init=False)
    description: str = field(default="Draw card when gaining allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_CONFLICT, init=False)


# =============================================================================
# COSMIC ALLIANCE ALIENS (20)
# =============================================================================

@dataclass
class Animal(AlienPower):
    """You have the power to Stampede. As a main player, you may add all ships
    from one of your colonies to the encounter."""
    name: str = field(default="Animal", init=False)
    description: str = field(default="Add entire colony to encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class Bandit(AlienPower):
    """You have the power to Rob. As offense, when you win, you may take one
    random card from defender instead of normal rewards."""
    name: str = field(default="Bandit", init=False)
    description: str = field(default="Rob card from defender on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Butler(AlienPower):
    """You have the power to Serve. Before alliances, you may give one card to
    each main player. They must accept you as ally."""
    name: str = field(default="Butler", init=False)
    description: str = field(default="Give cards to guarantee alliance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Chrysalis(AlienPower):
    """You have the power to Transform. Place cocoon tokens on your sheet.
    When you have 20, reveal a second alien power."""
    name: str = field(default="Chrysalis", init=False)
    description: str = field(default="Gain second power after collecting tokens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Crystal(AlienPower):
    """You have the power to Reflect. As defense, attack cards played against
    you are reflected back at the attacker."""
    name: str = field(default="Crystal", init=False)
    description: str = field(default="Reflect attack cards back at opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Cyborg(AlienPower):
    """You have the power of Integration. Once per encounter, you may discard
    a card to place one ship from warp to any colony."""
    name: str = field(default="Cyborg", init=False)
    description: str = field(default="Discard card to retrieve ship from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Extortionist(AlienPower):
    """You have the power to Blackmail. As a main player, before alliances,
    demand payment from any player or threaten to ally against them."""
    name: str = field(default="Extortionist", init=False)
    description: str = field(default="Demand payment or ally against.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE], init=False)


@dataclass
class General(AlienPower):
    """You have the power of Command. Your allies get +1 per ship they commit
    instead of the normal value."""
    name: str = field(default="General", init=False)
    description: str = field(default="Allied ships worth +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Gorgon(AlienPower):
    """You have the power to Petrify. Ships that encounter you become petrified
    and cannot be used until freed."""
    name: str = field(default="Gorgon", init=False)
    description: str = field(default="Petrify opposing ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Horde(AlienPower):
    """You have the power of the Masses. Start with 25 ships instead of 20.
    Ships count as half value (round up)."""
    name: str = field(default="Horde", init=False)
    description: str = field(default="25 ships but count as half value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Lightning(AlienPower):
    """You have the power of Speed. You may take two consecutive turns."""
    name: str = field(default="Lightning", init=False)
    description: str = field(default="Take two consecutive turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Poison(AlienPower):
    """You have the power to Infect. Ships that ally against you are poisoned
    and go to the warp at the end of the encounter."""
    name: str = field(default="Poison", init=False)
    description: str = field(default="Poison opposing allied ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Pygmy(AlienPower):
    """You have the power of Smallness. Your ships cannot be targeted individually.
    Effects targeting your ships target all or none."""
    name: str = field(default="Pygmy", init=False)
    description: str = field(default="Ships cannot be targeted individually.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Reborn(AlienPower):
    """You have the power of Renewal. When you lose your last home colony,
    regain all your home colonies with three ships each."""
    name: str = field(default="Reborn", init=False)
    description: str = field(default="Regain home colonies when losing last.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Remote(AlienPower):
    """You have the power of Distance. You may commit ships from the warp
    instead of from colonies."""
    name: str = field(default="Remote", init=False)
    description: str = field(default="Commit ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Sapient(AlienPower):
    """You have the power of Awareness. You may look at all face-down aliens
    at game start."""
    name: str = field(default="Sapient", init=False)
    description: str = field(default="See all face-down aliens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Schizoid(AlienPower):
    """You have the power of Madness. Start with two alien powers. Use one
    per encounter, alternating."""
    name: str = field(default="Schizoid", init=False)
    description: str = field(default="Alternate between two powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Skeptic(AlienPower):
    """You have the power to Doubt. Once per encounter, you may force a player
    to prove a claim about their hand or board state."""
    name: str = field(default="Skeptic", init=False)
    description: str = field(default="Force proof of claims.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Sting(AlienPower):
    """You have the power to Sting. When you lose an encounter, the winner
    loses one ship to the warp."""
    name: str = field(default="Sting", init=False)
    description: str = field(default="Winner loses ship when you lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


@dataclass
class Winner(AlienPower):
    """You have the power of Luck. When you win an encounter, draw one card."""
    name: str = field(default="Winner", init=False)
    description: str = field(default="Draw card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ALLIANCE, init=False)


# =============================================================================
# COSMIC STORM ALIENS (25)
# =============================================================================

@dataclass
class Arcade(AlienPower):
    """You have the power of Gaming. Opponents must play a minigame to determine
    encounter outcomes."""
    name: str = field(default="Arcade", init=False)
    description: str = field(default="Force minigames for encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Brute(AlienPower):
    """You have the power to Crush. As a main player, when you win by 10 or more,
    remove losing ships from game."""
    name: str = field(default="Brute", init=False)
    description: str = field(default="Remove ships on decisive wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Bulwark(AlienPower):
    """You have the power to Defend. As defense, your ships on the targeted
    planet cannot be sent to the warp."""
    name: str = field(default="Bulwark", init=False)
    description: str = field(default="Defending ships immune to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Converter(AlienPower):
    """You have the power of Change. Once per encounter, convert an attack card
    to a negotiate or vice versa."""
    name: str = field(default="Converter", init=False)
    description: str = field(default="Change attack to negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Coordinator(AlienPower):
    """You have the power to Organize. Before alliances, choose one player to
    ally with you. They cannot refuse."""
    name: str = field(default="Coordinator", init=False)
    description: str = field(default="Force one player to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Dervish(AlienPower):
    """You have the power to Spin. After destiny is drawn, you may spin all
    colonies clockwise to the next player."""
    name: str = field(default="Dervish", init=False)
    description: str = field(default="Spin all colonies clockwise.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Grumpus(AlienPower):
    """You have the power to Grouch. At the start of each encounter, if you
    did not win the previous encounter, gain one token."""
    name: str = field(default="Grumpus", init=False)
    description: str = field(default="Gain token when not winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Mouth(AlienPower):
    """You have the power of Persuasion. Once per encounter, convince an ally
    to commit additional ships."""
    name: str = field(default="Mouth", init=False)
    description: str = field(default="Convince allies for more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Neighbor(AlienPower):
    """You have the power of Proximity. You may ally with either side without
    being invited if you have a colony adjacent to the target."""
    name: str = field(default="Neighbor", init=False)
    description: str = field(default="Ally uninvited if adjacent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Outlaw(AlienPower):
    """You have the power to Rob. At the start of your turn, steal one card
    from a player with more cards than you."""
    name: str = field(default="Outlaw", init=False)
    description: str = field(default="Steal from card-rich players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Patriot(AlienPower):
    """You have the power of Loyalty. Your ships on home colonies cannot be
    removed or moved by other powers."""
    name: str = field(default="Patriot", init=False)
    description: str = field(default="Home colony ships protected.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Phantasm(AlienPower):
    """You have the power of Illusion. As defense, before cards revealed,
    declare your total. If opponent's total is lower, you win."""
    name: str = field(default="Phantasm", init=False)
    description: str = field(default="Declare phantom total as defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Porcupine(AlienPower):
    """You have the power to Pierce. Allies against you lose one ship each
    even if their side wins."""
    name: str = field(default="Porcupine", init=False)
    description: str = field(default="Opposing allies lose ship regardless.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Roach(AlienPower):
    """You have the power to Survive. Your ships in the warp may return to
    colonies at the end of each encounter."""
    name: str = field(default="Roach", init=False)
    description: str = field(default="Warp ships may return each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Scavenger(AlienPower):
    """You have the power to Salvage. When cards are discarded, you may take
    one and add it to your hand."""
    name: str = field(default="Scavenger", init=False)
    description: str = field(default="Take discarded cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Sloth(AlienPower):
    """You have the power of Slowness. You take your turns in reverse order."""
    name: str = field(default="Sloth", init=False)
    description: str = field(default="Take turns in reverse order.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Sneak(AlienPower):
    """You have the power to Infiltrate. As offense, you may land one ship on
    defense's planet before revealing."""
    name: str = field(default="Sneak", init=False)
    description: str = field(default="Pre-land ship before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Squee(AlienPower):
    """You have the power of Screaming. When you lose ships, all players
    discard one card."""
    name: str = field(default="Squee", init=False)
    description: str = field(default="All discard when you lose ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Swindler(AlienPower):
    """You have the power to Cheat. Once per encounter, look at one card in
    opponent's hand and exchange it with one of yours."""
    name: str = field(default="Swindler", init=False)
    description: str = field(default="Exchange specific cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Sycophant(AlienPower):
    """You have the power of Flattery. When you ally, gain the allied main
    player's power until end of encounter."""
    name: str = field(default="Sycophant", init=False)
    description: str = field(default="Use allied main player's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Tide(AlienPower):
    """You have the power of the Ocean. Ship counts alternate between high
    tide (doubled) and low tide (halved)."""
    name: str = field(default="Tide", init=False)
    description: str = field(default="Ships alternate double/half value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Tyrant(AlienPower):
    """You have the power to Oppress. When you win as offense, choose one
    opponent ship to join your colonies as a hostage."""
    name: str = field(default="Tyrant", init=False)
    description: str = field(default="Take hostage ship on offensive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Vox(AlienPower):
    """You have the power of Voice. Once per encounter, force a vote on any
    game decision."""
    name: str = field(default="Vox", init=False)
    description: str = field(default="Call votes on game decisions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Worm(AlienPower):
    """You have the power to Burrow. Your ships can move through wormholes
    to reach any planet."""
    name: str = field(default="Worm", init=False)
    description: str = field(default="Ships travel via wormholes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


@dataclass
class Wormhole(AlienPower):
    """You have the power of Tunneling. Create wormholes connecting planets.
    Ships may travel through."""
    name: str = field(default="Wormhole", init=False)
    description: str = field(default="Create planet connections.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_STORM, init=False)


# =============================================================================
# COSMIC DOMINION ALIENS (30)
# =============================================================================

@dataclass
class Ace(AlienPower):
    """You have the power of Excellence. Your encounter card value is increased
    by the number of colonies you have."""
    name: str = field(default="Ace", init=False)
    description: str = field(default="Card +1 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Alchemist(AlienPower):
    """You have the power to Transmute. Once per encounter, change any card's
    type (attack/negotiate/artifact)."""
    name: str = field(default="Alchemist", init=False)
    description: str = field(default="Change card types.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Angler(AlienPower):
    """You have the power to Fish. At start of encounter, draw from bottom of deck."""
    name: str = field(default="Angler", init=False)
    description: str = field(default="Draw from deck bottom.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Aristocrat(AlienPower):
    """You have the power of Nobility. You automatically win ties."""
    name: str = field(default="Aristocrat", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Bride(AlienPower):
    """You have the power of Union. At game start, bond with another player.
    Win together."""
    name: str = field(default="Bride", init=False)
    description: str = field(default="Share victory with bonded player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Daredevil(AlienPower):
    """You have the power of Risk. Double your encounter card value, but lose
    double ships if you lose."""
    name: str = field(default="Daredevil", init=False)
    description: str = field(default="Double card and ship losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Diplomat(AlienPower):
    """You have the power of Negotiation. You may make deals even when encounter
    cards don't allow it."""
    name: str = field(default="Diplomat", init=False)
    description: str = field(default="Make deals despite card types.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Doppelganger(AlienPower):
    """You have the power to Double. Choose another player at game start.
    Use their power as your own."""
    name: str = field(default="Doppelganger", init=False)
    description: str = field(default="Copy another player's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Engineer(AlienPower):
    """You have the power to Build. Place tech tokens. Gain benefits based
    on tech level."""
    name: str = field(default="Engineer", init=False)
    description: str = field(default="Build tech for benefits.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Explorer(AlienPower):
    """You have the power to Discover. After winning offense, draw a card for
    each foreign colony you have."""
    name: str = field(default="Explorer", init=False)
    description: str = field(default="Draw per foreign colony on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Greenhorn(AlienPower):
    """You have the power of Inexperience. Draw two flares at start. Use one
    as super each encounter."""
    name: str = field(default="Greenhorn", init=False)
    description: str = field(default="Use flares as super powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Host(AlienPower):
    """You have the power to Invite. As defense, you may invite all players
    to ally before offense."""
    name: str = field(default="Host", init=False)
    description: str = field(default="Invite allies before offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Joker(AlienPower):
    """You have the power of Humor. Once per encounter, cancel any other power."""
    name: str = field(default="Joker", init=False)
    description: str = field(default="Cancel any power use.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Judge(AlienPower):
    """You have the power of Judgment. You determine the outcome of all ties."""
    name: str = field(default="Judge", init=False)
    description: str = field(default="Decide tie outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Laser(AlienPower):
    """You have the power to Focus. Add +1 for each ship you have on home colonies."""
    name: str = field(default="Laser", init=False)
    description: str = field(default="+1 per ship on home colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Lizard(AlienPower):
    """You have the power to Regenerate. At end of encounter, return one ship
    from warp for each you lost."""
    name: str = field(default="Lizard", init=False)
    description: str = field(default="Retrieve ships equal to lost.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Love(AlienPower):
    """You have the power of Affection. Players cannot refuse to ally with you."""
    name: str = field(default="Love", init=False)
    description: str = field(default="Allies cannot refuse you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Mesmer(AlienPower):
    """You have the power to Hypnotize. Once per encounter, look at opponent's
    hand and choose their card."""
    name: str = field(default="Mesmer", init=False)
    description: str = field(default="Choose opponent's encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Mirage(AlienPower):
    """You have the power of Illusion. Ships you commit may not actually be there.
    Reveal after cards are revealed."""
    name: str = field(default="Mirage", init=False)
    description: str = field(default="Phantom ships revealed after cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Muckraker(AlienPower):
    """You have the power of Dirt. Once per encounter, reveal any other player's hand."""
    name: str = field(default="Muckraker", init=False)
    description: str = field(default="Reveal opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Pentaform(AlienPower):
    """You have the power of Five. Use five different powers, one per encounter,
    cycling through."""
    name: str = field(default="Pentaform", init=False)
    description: str = field(default="Cycle through five powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Pickpocket(AlienPower):
    """You have the power to Lift. When you ally, take one random card from
    the main player you sided with."""
    name: str = field(default="Pickpocket", init=False)
    description: str = field(default="Steal from allied main player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Pirate(AlienPower):
    """You have the power to Plunder. As offense, when you win, take all cards
    from defender's hand."""
    name: str = field(default="Pirate", init=False)
    description: str = field(default="Take defender's hand on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.OFFENSE], init=False)


@dataclass
class Quartermaster(AlienPower):
    """You have the power of Supply. Keep cards in a supply pile. Use them
    in future encounters."""
    name: str = field(default="Quartermaster", init=False)
    description: str = field(default="Build supply of cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Reactor(AlienPower):
    """You have the power of Energy. Gain +2 for each card in hand over 7."""
    name: str = field(default="Reactor", init=False)
    description: str = field(default="+2 per card over 7.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Tourist(AlienPower):
    """You have the power of Travel. Once per encounter, move one ship to any
    planet as a visitor."""
    name: str = field(default="Tourist", init=False)
    description: str = field(default="Place visitor ships anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Usurper(AlienPower):
    """You have the power to Seize. When you win defense, become offense against
    attacker."""
    name: str = field(default="Usurper", init=False)
    description: str = field(default="Counter-attack on defensive win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Voyager(AlienPower):
    """You have the power of Exploration. Draw extra destiny card and choose
    which to use."""
    name: str = field(default="Voyager", init=False)
    description: str = field(default="Choose from multiple destinies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class Whirligig(AlienPower):
    """You have the power to Spin. After reveal, swap encounter cards with opponent."""
    name: str = field(default="Whirligig", init=False)
    description: str = field(default="Swap cards after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


@dataclass
class YinYang(AlienPower):
    """You have the power of Balance. Your total is always equal to opponent's
    plus or minus 1."""
    name: str = field(default="YinYang", init=False)
    description: str = field(default="Total equals opponent +/- 1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_DOMINION, init=False)


# =============================================================================
# COSMIC EONS ALIENS (30)
# =============================================================================

@dataclass
class AI(AlienPower):
    """You have the power of Logic. Play encounter cards face-down. Both
    reveal simultaneously using perfect logic."""
    name: str = field(default="AI", init=False)
    description: str = field(default="Perfect logical card play.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Alien(AlienPower):
    """You have the power of Mystery. Start with face-down power. Reveal
    when you choose."""
    name: str = field(default="Alien", init=False)
    description: str = field(default="Hidden power until revealed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Anarchist(AlienPower):
    """You have the power of Chaos. Encounters have random modifications."""
    name: str = field(default="Anarchist", init=False)
    description: str = field(default="Random encounter modifiers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Architect(AlienPower):
    """You have the power to Build. Construct structures that provide benefits."""
    name: str = field(default="Architect", init=False)
    description: str = field(default="Build beneficial structures.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Assistant(AlienPower):
    """You have the power to Help. Allied main player gets +3."""
    name: str = field(default="Assistant", init=False)
    description: str = field(default="Allied main player +3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class BleedingHeart(AlienPower):
    """You have the power of Compassion. Retrieve two ships from warp when any
    player loses ships."""
    name: str = field(default="BleedingHeart", init=False)
    description: str = field(default="Retrieve ships when others lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Cloak(AlienPower):
    """You have the power to Hide. Your hand is kept face-down and secret."""
    name: str = field(default="Cloak", init=False)
    description: str = field(default="Hidden hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Coward(AlienPower):
    """You have the power to Flee. As defense, you may retreat before reveal,
    losing no ships."""
    name: str = field(default="Coward", init=False)
    description: str = field(default="Retreat as defense without loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)
    usable_as: List[PlayerRole] = field(default_factory=lambda: [PlayerRole.DEFENSE], init=False)


@dataclass
class Crusher(AlienPower):
    """You have the power to Crush. When you win by 20+, eliminate all
    opposing ships from game."""
    name: str = field(default="Crusher", init=False)
    description: str = field(default="Eliminate ships on huge wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Emperor(AlienPower):
    """You have the power to Command. Once per encounter, give another player
    an order they must follow."""
    name: str = field(default="Emperor", init=False)
    description: str = field(default="Command other players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class EvilTwin(AlienPower):
    """You have the power of Duality. Use opponent's power against them in
    encounters."""
    name: str = field(default="EvilTwin", init=False)
    description: str = field(default="Use opponent's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class FireDancer(AlienPower):
    """You have the power of Flame. Burn cards for permanent bonuses."""
    name: str = field(default="FireDancer", init=False)
    description: str = field(default="Burn cards for bonuses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Hunger(AlienPower):
    """You have the power to Consume. Eat cards from encounter for bonuses."""
    name: str = field(default="Hunger", init=False)
    description: str = field(default="Consume cards for power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Hypochondriac(AlienPower):
    """You have the power of Illness. Gain benefits when losing ships."""
    name: str = field(default="Hypochondriac", init=False)
    description: str = field(default="Benefits from losing ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Klutz(AlienPower):
    """You have the power of Clumsiness. Draw extra cards but must discard randomly."""
    name: str = field(default="Klutz", init=False)
    description: str = field(default="Draw more, discard randomly.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Maven(AlienPower):
    """You have the power of Expertise. You know all face-down information."""
    name: str = field(default="Maven", init=False)
    description: str = field(default="Know all hidden info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Moocher(AlienPower):
    """You have the power to Bum. Draw cards when others draw."""
    name: str = field(default="Moocher", init=False)
    description: str = field(default="Draw when others draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Multitude(AlienPower):
    """You have the power of Numbers. Ships in encounters count double."""
    name: str = field(default="Multitude", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Nanny(AlienPower):
    """You have the power to Protect. Allied ships cannot go to warp."""
    name: str = field(default="Nanny", init=False)
    description: str = field(default="Protect allied ships from warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Nightmare(AlienPower):
    """You have the power of Fear. Opponents must commit extra ships or lose."""
    name: str = field(default="Nightmare", init=False)
    description: str = field(default="Force extra ship commitment.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Oligarch(AlienPower):
    """You have the power of Wealth. Pay cards for special benefits."""
    name: str = field(default="Oligarch", init=False)
    description: str = field(default="Buy benefits with cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class PackRat(AlienPower):
    """You have the power to Hoard. No hand limit. Cards never discarded."""
    name: str = field(default="PackRat", init=False)
    description: str = field(default="Unlimited hand, no discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Particle(AlienPower):
    """You have the power of Splitting. Ships can split into multiple tokens."""
    name: str = field(default="Particle", init=False)
    description: str = field(default="Split ships into tokens.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Peddler(AlienPower):
    """You have the power to Sell. Sell cards to other players for ships."""
    name: str = field(default="Peddler", init=False)
    description: str = field(default="Sell cards for ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Perfectionist(AlienPower):
    """You have the power of Precision. Win by exactly the predicted amount."""
    name: str = field(default="Perfectionist", init=False)
    description: str = field(default="Win by exact prediction.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Pretender(AlienPower):
    """You have the power to Fake. Claim to have any power. Use it until challenged."""
    name: str = field(default="Pretender", init=False)
    description: str = field(default="Claim any power until challenged.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Sheriff(AlienPower):
    """You have the power of Law. Cancel illegal actions by other players."""
    name: str = field(default="Sheriff", init=False)
    description: str = field(default="Cancel illegal actions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Surgeon(AlienPower):
    """You have the power to Operate. Remove ships from warp for bonuses."""
    name: str = field(default="Surgeon", init=False)
    description: str = field(default="Extract warp ships for bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class TheCult(AlienPower):
    """You have the power of Conversion. Convert opponents' ships to yours."""
    name: str = field(default="TheCult", init=False)
    description: str = field(default="Convert enemy ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


@dataclass
class Tortoise(AlienPower):
    """You have the power of Patience. Slower but steadier progress to victory."""
    name: str = field(default="Tortoise", init=False)
    description: str = field(default="Steady progress benefits.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_EONS, init=False)


# =============================================================================
# COSMIC ODYSSEY ALIENS (31 + 11 Alternates)
# =============================================================================

@dataclass
class Assessor(AlienPower):
    """You have the power to Evaluate. See all players' hands at start of encounter."""
    name: str = field(default="Assessor", init=False)
    description: str = field(default="See all hands at encounter start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Aura(AlienPower):
    """You have the power of Presence. Gain bonuses based on colonies in system."""
    name: str = field(default="Aura", init=False)
    description: str = field(default="Bonus from system presence.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Boomerang(AlienPower):
    """You have the power to Return. Cards you play come back to your hand."""
    name: str = field(default="Boomerang", init=False)
    description: str = field(default="Retrieve played cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Booster(AlienPower):
    """You have the power to Boost. Add +5 to allied main player's total."""
    name: str = field(default="Booster", init=False)
    description: str = field(default="+5 to allied main player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Bubble(AlienPower):
    """You have the power to Protect. Create protective bubbles around colonies."""
    name: str = field(default="Bubble", init=False)
    description: str = field(default="Protect colonies with bubbles.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Cosmos(AlienPower):
    """You have the power of the Universe. Access to unique cosmic abilities."""
    name: str = field(default="Cosmos", init=False)
    description: str = field(default="Universal cosmic powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Decoy(AlienPower):
    """You have the power to Misdirect. Ships may be decoys that don't count."""
    name: str = field(default="Decoy", init=False)
    description: str = field(default="Use fake ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Delegator(AlienPower):
    """You have the power to Delegate. Others act on your behalf."""
    name: str = field(default="Delegator", init=False)
    description: str = field(default="Delegate actions to others.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Dragon(AlienPower):
    """You have the power of Fire. Breathe fire to destroy opposing ships."""
    name: str = field(default="Dragon", init=False)
    description: str = field(default="Fire breath destroys ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Extractor(AlienPower):
    """You have the power to Extract. Remove cards from other players' hands."""
    name: str = field(default="Extractor", init=False)
    description: str = field(default="Remove cards from hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Force(AlienPower):
    """You have the power of Momentum. Ships count double after consecutive wins."""
    name: str = field(default="Force", init=False)
    description: str = field(default="Ships count double after consecutive wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Geek(AlienPower):
    """You have the power of Knowledge. Know all game state information."""
    name: str = field(default="Geek", init=False)
    description: str = field(default="Full game state knowledge.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Gremlin(AlienPower):
    """You have the power to Sabotage. Break opponents' card plays."""
    name: str = field(default="Gremlin", init=False)
    description: str = field(default="Break card effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Guardian(AlienPower):
    """You have the power to Protect. Defend other players' colonies."""
    name: str = field(default="Guardian", init=False)
    description: str = field(default="Defend others' colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Hurtz(AlienPower):
    """You have the power to Pain. Deal damage to players when ships lost."""
    name: str = field(default="Hurtz", init=False)
    description: str = field(default="Cause pain on ship loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Inferno(AlienPower):
    """You have the power of Burning. Burn cards for massive damage."""
    name: str = field(default="Inferno", init=False)
    description: str = field(default="Burn cards for damage.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Insect(AlienPower):
    """You have the power of Swarming. Extra ship deployment abilities."""
    name: str = field(default="Insect", init=False)
    description: str = field(default="Swarm ship deployment.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Lemming(AlienPower):
    """You have the power of Following. Copy other players' actions."""
    name: str = field(default="Lemming", init=False)
    description: str = field(default="Copy player actions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Lloyd(AlienPower):
    """You have the power of Insurance. Recover from losses."""
    name: str = field(default="Lloyd", init=False)
    description: str = field(default="Insurance against losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Magnet(AlienPower):
    """You have the power of Attraction. Pull ships and cards to you."""
    name: str = field(default="Magnet", init=False)
    description: str = field(default="Attract ships and cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Micron(AlienPower):
    """You have the power of Smallness. Ships count less but are harder to hit."""
    name: str = field(default="Micron", init=False)
    description: str = field(default="Small ships, harder to lose.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Negator(AlienPower):
    """You have the power to Negate. Cancel card or power effects."""
    name: str = field(default="Negator", init=False)
    description: str = field(default="Negate effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Phantom(AlienPower):
    """You have the power of Phasing. Ships can phase through attacks."""
    name: str = field(default="Phantom", init=False)
    description: str = field(default="Phase through attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Silencer(AlienPower):
    """You have the power to Silence. Prevent players from using powers."""
    name: str = field(default="Silencer", init=False)
    description: str = field(default="Silence other powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Tentacle(AlienPower):
    """You have the power to Grasp. Grab ships from other locations."""
    name: str = field(default="Tentacle", init=False)
    description: str = field(default="Grab ships from anywhere.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class TheMeek(AlienPower):
    """You have the power of Humility. Win by losing three encounters as offense."""
    name: str = field(default="The Meek", init=False)
    description: str = field(default="Win by losing three encounters as offense.", init=False)
    has_alternate_win: bool = True
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Throwback(AlienPower):
    """You have the power of the Past. Use old-style game mechanics."""
    name: str = field(default="Throwback", init=False)
    description: str = field(default="Classic game mechanics.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Vector(AlienPower):
    """You have the power of Direction. Control movement of all ships."""
    name: str = field(default="Vector", init=False)
    description: str = field(default="Control ship movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Witch(AlienPower):
    """You have the power of Hexes. Curse players with negative effects."""
    name: str = field(default="Witch", init=False)
    description: str = field(default="Curse opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Wrack(AlienPower):
    """You have the power of Destruction. Destroy cards and ships."""
    name: str = field(default="Wrack", init=False)
    description: str = field(default="Destroy cards and ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Zilch(AlienPower):
    """You have the power of Nothing. Win with zero total."""
    name: str = field(default="Zilch", init=False)
    description: str = field(default="Win with zero.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


# =============================================================================
# COSMIC ODYSSEY ALTERNATE TIMELINE ALIENS (11)
# =============================================================================

@dataclass
class Brute_Alt(AlienPower):
    """[Alternate] You have the power to Crush. Different mechanics from original Brute."""
    name: str = field(default="Brute_Alt", init=False)
    description: str = field(default="Alternate crushing power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Daredevil_Alt(AlienPower):
    """[Alternate] You have the power of Risk. Different mechanics from original Daredevil."""
    name: str = field(default="Daredevil_Alt", init=False)
    description: str = field(default="Alternate risk power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Demon(AlienPower):
    """You have the power of Darkness. Dark powers from the void."""
    name: str = field(default="Demon", init=False)
    description: str = field(default="Dark void powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.BASE, init=False)  # Promo, counts as BASE


@dataclass
class Demon_Alt(AlienPower):
    """[Alternate] You have the power of Darkness. Different mechanics from original Demon."""
    name: str = field(default="Demon_Alt", init=False)
    description: str = field(default="Alternate demon power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Grumpus_Alt(AlienPower):
    """[Alternate] You have the power to Grouch. Different mechanics from original Grumpus."""
    name: str = field(default="Grumpus_Alt", init=False)
    description: str = field(default="Alternate grouch power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Locust_Alt(AlienPower):
    """[Alternate] You have the power to Devour. When you win, opponent discards a card."""
    name: str = field(default="Locust_Alt", init=False)
    description: str = field(default="When you win, opponent discards a card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Masochist_Alt(AlienPower):
    """[Alternate] You have the power to Enjoy Pain. Gain bonus based on warp ships."""
    name: str = field(default="Masochist_Alt", init=False)
    description: str = field(default="Gain bonus based on ships in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Perfectionist_Alt(AlienPower):
    """[Alternate] You have the power of Precision. Different mechanics from original."""
    name: str = field(default="Perfectionist_Alt", init=False)
    description: str = field(default="Alternate precision power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Sadist_Alt(AlienPower):
    """[Alternate] You have the power to Torment. Different mechanics from original."""
    name: str = field(default="Sadist_Alt", init=False)
    description: str = field(default="Alternate torment power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Schizoid_Alt(AlienPower):
    """[Alternate] You have the power of Madness. Different mechanics from original."""
    name: str = field(default="Schizoid_Alt", init=False)
    description: str = field(default="Alternate madness power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Void_Alt(AlienPower):
    """[Alternate] You have the power to Eradicate. Different mechanics from original."""
    name: str = field(default="Void_Alt", init=False)
    description: str = field(default="Alternate eradication power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


@dataclass
class Zombie_Alt(AlienPower):
    """[Alternate] You have the power of Immortality. Ships return from warp differently."""
    name: str = field(default="Zombie_Alt", init=False)
    description: str = field(default="Ships return from warp in alternate manner.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    expansion: Expansion = field(default=Expansion.COSMIC_ODYSSEY, init=False)


# Register all official powers
_official_powers = [
    # Base Game (50)
    Amoeba, Antimatter, Barbarian, Calculator, Chosen, Citadel, Clone, Cudgel,
    Dictator, Fido, Filch, Fodder, Gambler, Grudge, Hacker, Hate, Healer, Human,
    Kamikaze, Loser, Machine, Macron, Masochist, Mind, Mirror, Miser, Mite, Mutant,
    Observer, Oracle, Pacifist, Parasite, Philanthropist, Reincarnator, Remora,
    Reserve, Shadow, Sorcerer, Spiff, TickTock, Trader, Tripler, Vacuum, Virus,
    Void, Vulch, Warpish, Warrior, Will, Zombie,
    # Cosmic Incursion (20)
    Bully, Chronos, Cryo, Deuce, Disease, Ethic, Fungus, Fury, Genius, Ghoul,
    Guerrilla, Leviathan, Locust, Magician, Mercenary, Merchant, Plant, Seeker,
    Sniveler, Symbiote,
    # Cosmic Conflict (20)
    Cavalry, Changeling, Empath, Filth, Glutton, Graviton, Industrialist, Invader,
    Lunatic, Mimic, Prophet, Relic, Saboteur, Sadist, Siren, Claw, Trickster,
    Visionary, Warhawk, Xenophile,
    # Cosmic Alliance (20)
    Animal, Bandit, Butler, Chrysalis, Crystal, Cyborg, Extortionist, General,
    Gorgon, Horde, Lightning, Poison, Pygmy, Reborn, Remote, Sapient, Schizoid,
    Skeptic, Sting, Winner,
    # Cosmic Storm (25)
    Arcade, Brute, Bulwark, Converter, Coordinator, Dervish, Grumpus, Mouth,
    Neighbor, Outlaw, Patriot, Phantasm, Porcupine, Roach, Scavenger, Sloth,
    Sneak, Squee, Swindler, Sycophant, Tide, Tyrant, Vox, Worm, Wormhole,
    # Cosmic Dominion (30)
    Ace, Alchemist, Angler, Aristocrat, Bride, Daredevil, Diplomat, Doppelganger,
    Engineer, Explorer, Greenhorn, Host, Joker, Judge, Laser, Lizard, Love,
    Mesmer, Mirage, Muckraker, Pentaform, Pickpocket, Pirate, Quartermaster,
    Reactor, Tourist, Usurper, Voyager, Whirligig, YinYang,
    # Cosmic Eons (30)
    AI, Alien, Anarchist, Architect, Assistant, BleedingHeart, Cloak, Coward,
    Crusher, Emperor, EvilTwin, FireDancer, Hunger, Hypochondriac, Klutz, Maven,
    Moocher, Multitude, Nanny, Nightmare, Oligarch, PackRat, Particle, Peddler,
    Perfectionist, Pretender, Sheriff, Surgeon, TheCult, Tortoise,
    # Cosmic Odyssey (31)
    Assessor, Aura, Boomerang, Booster, Bubble, Cosmos, Decoy, Delegator, Dragon,
    Extractor, Force, Geek, Gremlin, Guardian, Hurtz, Inferno, Insect, Lemming,
    Lloyd, Magnet, Micron, Negator, Phantom, Silencer, Tentacle, TheMeek, Throwback,
    Vector, Witch, Wrack, Zilch,
    # Cosmic Odyssey Alternates (11)
    Brute_Alt, Daredevil_Alt, Demon, Demon_Alt, Grumpus_Alt, Locust_Alt,
    Masochist_Alt, Perfectionist_Alt, Sadist_Alt, Schizoid_Alt, Void_Alt, Zombie_Alt,
]

for power_class in _official_powers:
    AlienRegistry.register(power_class())
