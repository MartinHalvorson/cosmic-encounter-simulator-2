"""
Additional alien powers from Cosmic Encounter expansions.
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
class Assassin(AlienPower):
    """
    Assassin - Target opponent's ships go to warp even if you lose.
    """
    name: str = field(default="Assassin", init=False)
    description: str = field(
        default="Defense ships go to warp even if you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Butler(AlienPower):
    """
    Butler - Collect cards discarded by other players.
    """
    name: str = field(default="Butler", init=False)
    description: str = field(
        default="Collect one card whenever others discard.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Changeling(AlienPower):
    """
    Changeling - Copy an opponent's alien power.
    """
    name: str = field(default="Changeling", init=False)
    description: str = field(
        default="Use opponent's alien power.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Chronos(AlienPower):
    """
    Chronos - Restart encounters.
    """
    name: str = field(default="Chronos", init=False)
    description: str = field(
        default="Restart encounter after reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Claw(AlienPower):
    """
    Claw - Force opponents to ally with you.
    """
    name: str = field(default="Claw", init=False)
    description: str = field(
        default="Force one player to ally with you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Crone(AlienPower):
    """
    Crone - Curse opponents to lose power.
    """
    name: str = field(default="Crone", init=False)
    description: str = field(
        default="Disable an opponent's power for the encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Dictator(AlienPower):
    """
    Dictator - Control alliance decisions.
    """
    name: str = field(default="Dictator", init=False)
    description: str = field(
        default="Control all alliance decisions.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Empath(AlienPower):
    """
    Empath - Know opponent's encounter card value.
    """
    name: str = field(default="Empath", init=False)
    description: str = field(
        default="Know opponent's card value before reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Ethic(AlienPower):
    """
    Ethic - Force fair encounters.
    """
    name: str = field(default="Ethic", init=False)
    description: str = field(
        default="Force equal ship counts in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Gambler(AlienPower):
    """
    Gambler - Double the stakes.
    """
    name: str = field(default="Gambler", init=False)
    description: str = field(
        default="Both sides lose ships regardless of outcome.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Grudge(AlienPower):
    """
    Grudge - Gain strength from defeats.
    """
    name: str = field(default="Grudge", init=False)
    description: str = field(
        default="Gain tokens from losses, add to combat total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Human(AlienPower):
    """
    Human - Gain +4 in all encounters.
    """
    name: str = field(default="Human", init=False)
    description: str = field(
        default="+4 in all encounters.",
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
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Mutant(AlienPower):
    """
    Mutant - Refill hand at start of each turn.
    """
    name: str = field(default="Mutant", init=False)
    description: str = field(
        default="Draw up to 8 cards at turn start.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active and game.offense == player:
            while len(player.hand) < 8:
                card = game.cosmic_deck.draw()
                player.add_card(card)


@dataclass
class Negator(AlienPower):
    """
    Negator - Cancel alien powers.
    """
    name: str = field(default="Negator", init=False)
    description: str = field(
        default="Cancel another player's power use.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Observer(AlienPower):
    """
    Observer - See all hidden information.
    """
    name: str = field(default="Observer", init=False)
    description: str = field(
        default="See all hidden cards and hands.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pentaform(AlienPower):
    """
    Pentaform - Start with 5 alien powers.
    """
    name: str = field(default="Pentaform", init=False)
    description: str = field(
        default="Start with 5 powers, lose one per lost encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Giver(AlienPower):
    """
    Giver - Draw extra cards for others.
    """
    name: str = field(default="Giver", init=False)
    description: str = field(
        default="Give extra drawn cards to other players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Seeker(AlienPower):
    """
    Seeker - Search the deck for specific cards.
    """
    name: str = field(default="Seeker", init=False)
    description: str = field(
        default="Search deck for cards when drawing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sheriff(AlienPower):
    """
    Sheriff - Prevent attacks on other players.
    """
    name: str = field(default="Sheriff", init=False)
    description: str = field(
        default="Force attacks to target you instead.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sniveler(AlienPower):
    """
    Sniveler - Whine for advantages.
    """
    name: str = field(default="Sniveler", init=False)
    description: str = field(
        default="Whine for +5 if no one helps you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Surge(AlienPower):
    """
    Surge - Add extra ships mid-encounter.
    """
    name: str = field(default="Surge", init=False)
    description: str = field(
        default="Add ships after cards are revealed.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Yin(AlienPower):
    """
    Yin - Win ties.
    """
    name: str = field(default="Yin", init=False)
    description: str = field(
        default="Win all ties.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Fido(AlienPower):
    """
    Fido - Retrieve ships when winning.
    """
    name: str = field(default="Fido", init=False)
    description: str = field(
        default="Win: retrieve all ships from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        if as_main_player and player.power_active:
            ships = player.ships_in_warp
            retrieved = player.retrieve_ships_from_warp(ships)
            player.return_ships_to_colonies(retrieved, player.home_planets)


@dataclass
class Visionary(AlienPower):
    """
    Visionary - Predict and benefit from correct predictions.
    """
    name: str = field(default="Visionary", init=False)
    description: str = field(
        default="Predict encounter outcome for bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Silencer(AlienPower):
    """
    Silencer - Prevent players from speaking.
    """
    name: str = field(default="Silencer", init=False)
    description: str = field(
        default="Silence a player each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Philanthropist_Alt(AlienPower):
    """
    Altruist - Give away ships for cards.
    """
    name: str = field(default="Altruist", init=False)
    description: str = field(
        default="Give ships to others, draw cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ========== Cosmic Incursion Expansion ==========

@dataclass
class Cryo(AlienPower):
    """
    Cryo - Power to Preserve.
    Official FFG rules: As main player or ally, after allies are invited,
    take one card from hand and store it in cold storage. Draw a replacement.
    When you have 8+ cards stored, discard hand and take stored cards.
    """
    name: str = field(default="Cryo", init=False)
    description: str = field(
        default="Store cards in cold storage for later use.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    cold_storage: List[Any] = field(default_factory=list, init=False)

    def on_alliance_phase(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Store a card in cold storage."""
        if not player.power_active or not player.hand:
            return

        # Store one card (AI chooses lowest value attack or first card)
        card_to_store = None
        attacks = player.get_attack_cards()
        if attacks:
            card_to_store = min(attacks, key=lambda c: c.value)
        elif player.hand:
            card_to_store = player.hand[0]

        if card_to_store:
            player.remove_card(card_to_store)
            self.cold_storage.append(card_to_store)

            # Draw replacement
            new_card = game.cosmic_deck.draw()
            player.add_card(new_card)

            # Check if we should swap to stored cards
            if len(self.cold_storage) >= 8:
                # Discard current hand
                for card in list(player.hand):
                    player.remove_card(card)
                    game.cosmic_deck.discard(card)
                # Take stored cards
                for card in self.cold_storage:
                    player.add_card(card)
                self.cold_storage = []


@dataclass
class Locust(AlienPower):
    """
    Locust - Power to Devour.
    Official FFG rules: At start of regroup phase, if you have a foreign
    colony alone on a planet (no other players' ships), devour the planet,
    removing it from the game. Your ships return to other colonies.
    Each devoured planet counts as one foreign colony.
    """
    name: str = field(default="Locust", init=False)
    description: str = field(
        default="Devour planets where you are alone; they count as colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    devoured_count: int = field(default=0, init=False)

    def on_regroup(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Check for and devour planets where we're alone."""
        if not player.power_active:
            return

        planets_to_devour = []
        for planet in game.planets:
            # Check if it's a foreign colony
            if not planet.is_foreign_colony(player):
                continue
            # Check if we're alone
            other_colonies = [
                p for p in game.players if p != player and planet.has_colony(p.name)
            ]
            if not other_colonies:
                planets_to_devour.append(planet)

        for planet in planets_to_devour:
            # Return our ships to home
            ships = planet.get_ships(player.name)
            planet.remove_ships(player.name, ships)
            player.return_ships_to_colonies(ships, player.home_planets)
            # Remove planet from game
            if planet in game.planets:
                game.planets.remove(planet)
            self.devoured_count += 1


@dataclass
class Mercenary(AlienPower):
    """
    Mercenary - Power of Bounty Hunting.
    Official FFG rules: After your side wins an encounter as main player
    or offensive ally, gain defender rewards (1 card or 1 ship per ship involved).
    """
    name: str = field(default="Mercenary", init=False)
    description: str = field(
        default="Gain defender rewards when winning as offense/ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Get defender rewards when winning on offense."""
        if not player.power_active:
            return

        # Only works on offense side
        is_offense_side = (
            player == game.offense or player in game.offense_allies
        )
        if not is_offense_side:
            return

        # Get ships committed
        ships = game.offense_ships.get(player.name, 0)
        if ships <= 0:
            return

        # Choose cards or ships (AI prefers cards if hand is small)
        if len(player.hand) < 6:
            # Draw cards
            for _ in range(ships):
                if game.rewards_deck:
                    card = game.rewards_deck.draw()
                    player.add_card(card)
        else:
            # Retrieve ships from warp
            retrieved = min(ships, player.ships_in_warp)
            if retrieved > 0:
                player.retrieve_ships_from_warp(retrieved)
                player.return_ships_to_colonies(retrieved, player.home_planets)


@dataclass
class Merchant(AlienPower):
    """
    Merchant - Power to Hire.
    Official FFG rules: After encounter cards are selected but before reveal,
    play cards from hand face-down as extra ships (beyond 4-ship limit).
    These hired ships return to hand at encounter end.
    """
    name: str = field(default="Merchant", init=False)
    description: str = field(
        default="Play cards as extra ships during encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Add hired ships to count."""
        if not player.power_active:
            return base_count

        # Merchant can hire up to 2 extra ships from cards
        # Each card in hand over 5 can be used as a hired ship
        extra_cards = max(0, len(player.hand) - 5)
        hired_ships = min(2, extra_cards)

        return base_count + hired_ships


@dataclass
class Plant(AlienPower):
    """
    Plant - Power of Grafting.
    Official FFG rules: When you have a colony in another player's home
    system, you may use their power instead of them for one encounter.
    Cannot graft if you've lost your own power.
    """
    name: str = field(default="Plant", init=False)
    description: str = field(
        default="Use opponent's power when you have colony in their home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Check if we can graft another player's power."""
        if not player.power_active:
            return

        # Find opponent whose home system we've colonized
        for other in game.players:
            if other == player:
                continue
            # Check if we have a colony on any of their home planets
            for planet in other.home_planets:
                if planet.has_colony(player.name):
                    # Can graft their power - store for reference
                    # In simulation, this just means we could use their power
                    break


# ========== Cosmic Conflict Expansion ==========

@dataclass
class Filth(AlienPower):
    """
    Filth - Power to Reek.
    Official FFG rules: Any time your ships share a planet with other
    players' ships, those ships must leave to other colonies or warp.
    """
    name: str = field(default="Filth", init=False)
    description: str = field(
        default="Forces other ships to leave planets you occupy.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Graviton(AlienPower):
    """
    Graviton - Power of Gravity.
    Official FFG rules: As main player, after cards selected but before
    reveal, declare 'tens' or 'ones'. Attack cards only use that digit.
    """
    name: str = field(default="Graviton", init=False)
    description: str = field(
        default="Declare tens or ones digit for attack cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        base_value: int,
        side: Side
    ) -> int:
        """Reduce cards to single digit (simplified: ones digit)."""
        if not player.power_active:
            return base_value
        # Use ones digit
        return base_value % 10


@dataclass
class Lunatic(AlienPower):
    """
    Lunatic - Power of Insanity.
    Official FFG rules: As main player, after allies invited, may ally
    against yourself. Get rewards from either side winning.
    """
    name: str = field(default="Lunatic", init=False)
    description: str = field(
        default="Ally against yourself; gain rewards either way.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Industrialist(AlienPower):
    """
    Industrialist - Power to Build.
    Official FFG rules: When you lose with attack card, opponent must let
    you win OR you stack the card as permanent bonus for future encounters.
    """
    name: str = field(default="Industrialist", init=False)
    description: str = field(
        default="Stack lost attack cards as permanent combat bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    stack_bonus: int = field(default=0, init=False)

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Add lost attack card value to permanent stack."""
        if not as_main_player or not player.power_active:
            return
        # Get the attack card that was played
        if game.offense == player and game.offense_card:
            from ...cards.base import AttackCard
            if isinstance(game.offense_card, AttackCard):
                self.stack_bonus += game.offense_card.value
        elif game.defense == player and game.defense_card:
            from ...cards.base import AttackCard
            if isinstance(game.defense_card, AttackCard):
                self.stack_bonus += game.defense_card.value

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add stack bonus to combat total."""
        if player.power_active:
            return base_total + self.stack_bonus
        return base_total


@dataclass
class Relic(AlienPower):
    """
    Relic - Power to Awaken.
    Official FFG rules: Gain free foreign colony when others draw new hands.
    When you draw new hand, retrieve all ships from warp.
    """
    name: str = field(default="Relic", init=False)
    description: str = field(
        default="Gain colony when others draw hands; retrieve all ships when you draw.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Saboteur(AlienPower):
    """
    Saboteur - Power of Booby Trap.
    Official FFG rules: Place trap tokens on planets. When ships land,
    reveal token - if trap, all ships on planet go to warp.
    """
    name: str = field(default="Saboteur", init=False)
    description: str = field(
        default="Place trap tokens that send landing ships to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Sadist(AlienPower):
    """
    Sadist - Power to Inflict Pain.
    Official FFG rules: At start of regroup, if all other players have
    lost 8+ ships each (warp + removed), Sadist wins immediately.
    """
    name: str = field(default="Sadist", init=False)
    description: str = field(
        default="Win if all others have lost 8+ ships each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def check_alternate_win(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """Check if Sadist wins via alternate condition."""
        if not player.power_active:
            return False

        for other in game.players:
            if other == player:
                continue
            if other.ships_in_warp < 8:
                return False
        return True


@dataclass
class Trickster(AlienPower):
    """
    Trickster - Power of Possibilities.
    Official FFG rules: As main player, hide token in fist. Opponent
    guesses - if correct, you lose; if wrong, you win.
    """
    name: str = field(default="Trickster", init=False)
    description: str = field(
        default="Hide token; opponent guesses to determine winner.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Warhawk(AlienPower):
    """
    Warhawk - Power of Attack.
    Official FFG rules: Never negotiates. Opponent's negotiate becomes
    attack 00. Your negotiate becomes morph. Both negotiate = both 00.
    """
    name: str = field(default="Warhawk", init=False)
    description: str = field(
        default="Never negotiates; opponent's negotiate becomes attack 00.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# ========== Cosmic Alliance Expansion ==========

@dataclass
class Animal(AlienPower):
    """
    Animal - Power to Party.
    When not invited as ally, that main player loses a ship.
    When your side wins, all on winning side draw a card.
    """
    name: str = field(default="Animal", init=False)
    description: str = field(default="Punish those who don't invite you; reward winners.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bandit(AlienPower):
    """
    Bandit - Power to Take a Spin.
    At start of each turn, reveal 3 cards from deck. Get cards based on matches.
    """
    name: str = field(default="Bandit", init=False)
    description: str = field(default="Reveal top 3 cards; gain cards based on matches.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class General(AlienPower):
    """
    General - Power of Leadership.
    As main player, draw one card per ally. Each ally also draws one.
    """
    name: str = field(default="General", init=False)
    description: str = field(default="Draw cards for allies; allies also draw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gorgon(AlienPower):
    """
    Gorgon - Power to Petrify.
    Ships attempting to leave your planets must go to warp instead.
    """
    name: str = field(default="Gorgon", init=False)
    description: str = field(default="Ships leaving your planets go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lightning(AlienPower):
    """
    Lightning - Power of Speed.
    Take two turns in a row instead of one.
    """
    name: str = field(default="Lightning", init=False)
    description: str = field(default="Take two consecutive turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pygmy(AlienPower):
    """
    Pygmy - Power of Small.
    Start with 3 ships per planet. Ships count as 2 each in combat.
    """
    name: str = field(default="Pygmy", init=False)
    description: str = field(default="Fewer ships but each counts as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if not player.power_active:
            return base_count
        # Get this player's ships in the encounter
        if side == Side.OFFENSE:
            my_ships = game.offense_ships.get(player.name, 0)
        else:
            my_ships = game.defense_ships.get(player.name, 0)
        other_ships = base_count - my_ships
        return other_ships + (my_ships * 2)


@dataclass
class Reborn(AlienPower):
    """
    Reborn - Power of Renewal.
    When you would lose a home colony, draw a new hand and retrieve all ships.
    """
    name: str = field(default="Reborn", init=False)
    description: str = field(default="When losing home colony, draw new hand and retrieve ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Remote(AlienPower):
    """
    Remote - Power of Distance.
    You may attack any system, ignoring destiny. Defense doesn't choose planet.
    """
    name: str = field(default="Remote", init=False)
    description: str = field(default="Attack any system; choose the planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sapient(AlienPower):
    """
    Sapient - Power of Wisdom.
    Look at opponent's hand before selecting encounter card.
    """
    name: str = field(default="Sapient", init=False)
    description: str = field(default="See opponent's hand before card selection.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skeptic(AlienPower):
    """
    Skeptic - Power of Doubt.
    Before cards revealed, guess opponent's card type. If wrong, +5 to total.
    """
    name: str = field(default="Skeptic", init=False)
    description: str = field(default="Guess opponent's card type; +5 if wrong.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        # 60% chance of guessing wrong (simplified)
        if random.random() < 0.6:
            return base_total + 5
        return base_total


@dataclass
class Sting(AlienPower):
    """
    Sting - Power of the Bee.
    When you lose ships to warp, send one opponent ship to warp too.
    """
    name: str = field(default="Sting", init=False)
    description: str = field(default="When you lose ships, opponent loses one too.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Winner(AlienPower):
    """
    Winner - Power to Win More.
    When you win by 10+, gain one free foreign colony.
    """
    name: str = field(default="Winner", init=False)
    description: str = field(default="Win by 10+ to gain extra colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# =============================================================================
# COSMIC STORM EXPANSION (25 aliens)
# =============================================================================

@dataclass
class Arcade(AlienPower):
    """
    Arcade - Power to Pwn.
    Official FFG rules: When you win by 10+ or win vs negotiate, capture one opponent ship.
    Win the game if you collect 3 ships of same color or 5 total ships.
    """
    name: str = field(default="Arcade", init=False)
    description: str = field(default="Capture ships to win; 3 same color or 5 total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    captured_ships: Dict[str, int] = field(default_factory=dict, init=False)

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        """Capture a ship when winning big or vs negotiate."""
        if not player.power_active or not as_main_player:
            return

        opponent = game.defense if game.offense == player else game.offense

        # Check if opponent played negotiate
        opp_card = game.defense_card if game.offense == player else game.offense_card
        opponent_negotiated = hasattr(opp_card, 'card_type') and opp_card.card_type == 'negotiate'

        # Calculate margin by comparing card values + ship counts
        my_card = game.offense_card if game.offense == player else game.defense_card
        my_card_value = getattr(my_card, 'value', 0) or 0
        opp_card_value = getattr(opp_card, 'value', 0) or 0

        my_ships = sum(game.offense_ships.values()) if game.offense == player else sum(game.defense_ships.values())
        opp_ships = sum(game.defense_ships.values()) if game.offense == player else sum(game.offense_ships.values())

        my_total = my_card_value + my_ships
        opp_total = opp_card_value + opp_ships
        margin = my_total - opp_total

        if margin >= 10 or opponent_negotiated:
            # Capture one ship from opponent
            color = opponent.name
            self.captured_ships[color] = self.captured_ships.get(color, 0) + 1

    def check_alternate_win(self, game: "Game", player: "Player") -> bool:
        """Check if Arcade wins via captured ships."""
        total_captured = sum(self.captured_ships.values())
        if total_captured >= 5:
            return True
        for count in self.captured_ships.values():
            if count >= 3:
                return True
        return False


@dataclass
class Bride(AlienPower):
    """
    Bride - Power to Marry.
    Official FFG rules: Force opponent to place ship on your sheet (marriage).
    Share alliances and cards with spouse. Divorce for half their cards.
    """
    name: str = field(default="Bride", init=False)
    description: str = field(default="Marry opponent; share cards, divorce for alimony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    spouse: Optional[str] = field(default=None, init=False)
    divorced_players: List[str] = field(default_factory=list, init=False)


@dataclass
class Grumpus(AlienPower):
    """
    Grumpus - Power to Grump.
    Official FFG rules: When your colony is removed from any planet,
    every other player with a colony there loses one ship to warp.
    """
    name: str = field(default="Grumpus", init=False)
    description: str = field(default="When colony removed, others on planet lose ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mouth(AlienPower):
    """
    Mouth - Power to Gobble.
    Official FFG rules: After alliances, collect cards opponent discards.
    If 5+ cards collected, return one to hand; rest removed from game.
    """
    name: str = field(default="Mouth", init=False)
    description: str = field(default="Gobble opponent discards; 5+ returns one to hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    gobbled_cards: List[Any] = field(default_factory=list, init=False)


@dataclass
class Neighbor(AlienPower):
    """
    Neighbor - Power of Community.
    Official FFG rules: As main player or ally after revealing attack card,
    add +1 for each of your uninvolved ships in the targeted system.
    """
    name: str = field(default="Neighbor", init=False)
    description: str = field(default="+1 for each uninvolved ship in targeted system.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Add +1 for each uninvolved ship in targeted system (defender's planets)."""
        if not player.power_active:
            return base_total

        # Count uninvolved ships on defender's other home planets
        bonus = 0
        if game.defense_planet and game.defense:
            # The "targeted system" is the defender's home system
            for planet in game.defense.home_planets:
                if player.name in planet.ships:
                    # Ships on defender's planets not involved in encounter
                    if planet != game.defense_planet:
                        bonus += planet.ships[player.name]

        return base_total + bonus


@dataclass
class Outlaw(AlienPower):
    """
    Outlaw - Power to Waylay.
    Official FFG rules: After alliances formed, as main player,
    take one random card from opponent and each of their allies.
    """
    name: str = field(default="Outlaw", init=False)
    description: str = field(default="Steal random card from opponent and their allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Porcupine(AlienPower):
    """
    Porcupine - Power to Needle.
    Official FFG rules: When losing as main player or ally with attack cards revealed,
    discard any cards from hand to add/subtract that amount from your total.
    """
    name: str = field(default="Porcupine", init=False)
    description: str = field(default="Discard cards when losing to adjust total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        """Discard cards to potentially turn a loss into a win."""
        if not player.power_active:
            return base_total

        # Use base_total as our current total since full totals aren't calculated yet
        # Estimate opponent total from visible information
        if side == Side.OFFENSE:
            # Estimate defense total: card value + ships
            opp_card = game.defense_card
            opp_card_value = opp_card.value if hasattr(opp_card, 'value') and opp_card.value else 0
            opp_ships = sum(game.defense_ships.values())
            estimated_opp = opp_card_value + opp_ships
        else:
            # Estimate offense total
            opp_card = game.offense_card
            opp_card_value = opp_card.value if hasattr(opp_card, 'value') and opp_card.value else 0
            opp_ships = sum(game.offense_ships.values())
            estimated_opp = opp_card_value + opp_ships

        # Only activate if likely losing
        if base_total >= estimated_opp:
            return base_total

        # Discard cards to make up the difference (AI decision)
        deficit = estimated_opp - base_total + 1  # Need to win by at least 1
        cards_to_discard = min(deficit, len(player.hand) // 2)  # Don't discard more than half

        return base_total + cards_to_discard


@dataclass
class Sloth(AlienPower):
    """
    Sloth - Power of Laziness.
    Official FFG rules: Instead of committing ships during launch,
    place token. After card selection, replace with 0-4 ships.
    """
    name: str = field(default="Sloth", init=False)
    description: str = field(default="Commit ships after card selection, not during launch.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Squee(AlienPower):
    """
    Squee - Power of Unimaginable Cuteness.
    Official FFG rules: As defender after cards selected,
    force offense to concede or send 3 ships to warp.
    If they continue and win with attack, Squee gets compensation anyway.
    """
    name: str = field(default="Squee", init=False)
    description: str = field(default="Force offense to concede or lose 3 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Swindler(AlienPower):
    """
    Swindler - Power of Identity Theft.
    Official FFG rules: After defense determined, reveal mark and swap
    everything with them - seats, powers, ships, hands, colonies.
    """
    name: str = field(default="Swindler", init=False)
    description: str = field(default="Swap everything with secretly marked player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    marked_player: Optional[str] = field(default=None, init=False)


# Register all powers
AlienRegistry.register(Assassin())
AlienRegistry.register(Butler())
AlienRegistry.register(Changeling())
AlienRegistry.register(Chronos())
AlienRegistry.register(Claw())
AlienRegistry.register(Crone())
AlienRegistry.register(Dictator())
AlienRegistry.register(Empath())
AlienRegistry.register(Ethic())
AlienRegistry.register(Gambler())
AlienRegistry.register(Grudge())
AlienRegistry.register(Human())
AlienRegistry.register(Mutant())
AlienRegistry.register(Negator())
AlienRegistry.register(Observer())
AlienRegistry.register(Pentaform())
AlienRegistry.register(Giver())
AlienRegistry.register(Seeker())
AlienRegistry.register(Sheriff())
AlienRegistry.register(Sniveler())
AlienRegistry.register(Surge())
AlienRegistry.register(Yin())
AlienRegistry.register(Fido())
AlienRegistry.register(Visionary())
AlienRegistry.register(Silencer())
AlienRegistry.register(Philanthropist_Alt())
# Cosmic Incursion expansion
AlienRegistry.register(Cryo())
AlienRegistry.register(Locust())
AlienRegistry.register(Mercenary())
AlienRegistry.register(Merchant())
AlienRegistry.register(Plant())
# Cosmic Conflict expansion
AlienRegistry.register(Filth())
AlienRegistry.register(Graviton())
AlienRegistry.register(Lunatic())
AlienRegistry.register(Industrialist())
AlienRegistry.register(Relic())
AlienRegistry.register(Saboteur())
AlienRegistry.register(Sadist())
AlienRegistry.register(Trickster())
AlienRegistry.register(Warhawk())
# Cosmic Alliance expansion
AlienRegistry.register(Animal())
AlienRegistry.register(Bandit())
AlienRegistry.register(General())
AlienRegistry.register(Gorgon())
AlienRegistry.register(Lightning())
AlienRegistry.register(Pygmy())
AlienRegistry.register(Reborn())
AlienRegistry.register(Remote())
AlienRegistry.register(Sapient())
AlienRegistry.register(Skeptic())
AlienRegistry.register(Sting())
AlienRegistry.register(Winner())
# Cosmic Storm expansion
AlienRegistry.register(Arcade())
AlienRegistry.register(Bride())
AlienRegistry.register(Grumpus())
AlienRegistry.register(Mouth())
AlienRegistry.register(Neighbor())
AlienRegistry.register(Outlaw())
AlienRegistry.register(Porcupine())
AlienRegistry.register(Sloth())
AlienRegistry.register(Squee())
AlienRegistry.register(Swindler())


# =============================================================================
# COSMIC EONS EXPANSION (30 aliens)
# =============================================================================

@dataclass
class Anarchist(AlienPower):
    """
    Anarchist - Power of Chaos.
    Official FFG rules: When you lose or fail a deal as main player,
    reveal a rule disruption. Win when all 8 disruptions revealed.

    Balance adjustment v2: Requires 12 disruptions (increased from 8) and only
    counts offensive losses to prevent intentional losing strategies.
    """
    name: str = field(default="Anarchist", init=False)
    description: str = field(default="Disrupt rules on offensive loss; win with 12 disruptions.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    has_alternate_win: bool = field(default=True, init=False)
    disruptions_revealed: int = field(default=0, init=False)

    def on_lose_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        # Only count losses as offense (per FFG clarification)
        if as_main_player and player.power_active:
            if player == game.offense:
                self.disruptions_revealed += 1

    def check_alternate_win(self, game: "Game", player: "Player") -> bool:
        # Requires 12 disruptions (increased from 8 for balance)
        return self.disruptions_revealed >= 12


@dataclass
class AssistantAlien(AlienPower):
    """
    Assistant - Power to Be Helpful.
    Official FFG rules: As main player or ally, give help card to ally; gain reward.
    """
    name: str = field(default="Assistant", init=False)
    description: str = field(default="Give help to allies; gain rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class BleedingHeart(AlienPower):
    """
    Bleeding Heart - Power of Rapport.
    Official FFG rules: Before alliances, declare peace - attack cards 10 or lower
    become negotiates; compensation is doubled.
    """
    name: str = field(default="BleedingHeart", init=False)
    description: str = field(default="Convert low attacks to negotiates; double compensation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Coward(AlienPower):
    """
    Coward - Power to Flee.
    Official FFG rules: After cards selected, may flee - counts as success,
    ships return, get rewards for opponent ships.
    """
    name: str = field(default="Coward", init=False)
    description: str = field(default="Flee before reveal; counts as success.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Crusher(AlienPower):
    """
    Crusher - Power to Crush.
    Official FFG rules: After cards selected, opponent's ships count as just 1
    for totals, compensation, and rewards.
    """
    name: str = field(default="Crusher", init=False)
    description: str = field(default="Opponent ships count as 1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class EvilTwin(AlienPower):
    """
    Evil Twin - Power to Blame.
    Official FFG rules: As main player after launch, designate a "good twin"
    who suffers all your losses and penalties.
    """
    name: str = field(default="EvilTwin", init=False)
    description: str = field(default="Another player suffers your losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class FireDancer(AlienPower):
    """
    Fire Dancer - Power to Awe.
    Official FFG rules: As main player, place fire tokens. Fuel cards under
    fire add to defense total in that system.
    """
    name: str = field(default="FireDancer", init=False)
    description: str = field(default="Create fires that boost defense in systems.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    fire_bonus: int = field(default=0, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        # Fire provides defensive bonus
        if side == Side.DEFENSE:
            return base_total + self.fire_bonus
        return base_total


@dataclass
class Hunger(AlienPower):
    """
    Hunger - Power of Extra Helpings.
    Official FFG rules: At start of your turn, take one random card from each
    other player. At start of others' turns, take one from that player.
    """
    name: str = field(default="Hunger", init=False)
    description: str = field(default="Take random cards from all players each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hypochondriac(AlienPower):
    """
    Hypochondriac - Power of Anxiety.
    Official FFG rules: Name a player who makes you anxious; they offer remedy
    or get anxiety token. Players with most tokens can't win.
    """
    name: str = field(default="Hypochondriac", init=False)
    description: str = field(default="Give anxiety tokens; most tokens can't win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Klutz(AlienPower):
    """
    Klutz - Power to Fumble.
    Official FFG rules: When drawing multiple cards, must drop 1-2.
    When placing multiple ships on same planet, drop one nearby ship to warp.
    """
    name: str = field(default="Klutz", init=False)
    description: str = field(default="Drop cards when drawing; drop ships when landing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Maven(AlienPower):
    """
    Maven - Power to Be Right.
    Official FFG rules: When not main player or ally after cards selected,
    take all facedown cards and declare outcome. Discard a card to make prediction.
    """
    name: str = field(default="Maven", init=False)
    description: str = field(default="Predict and control encounter outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Moocher(AlienPower):
    """
    Moocher - Power to Barge In.
    Official FFG rules: After destiny, mooch a colony on empty planet.
    Place couch tokens that function as planets.
    """
    name: str = field(default="Moocher", init=False)
    description: str = field(default="Create couch colonies on empty planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Oligarch(AlienPower):
    """
    Oligarch - Power of Greed.
    Official FFG rules: When drawing a new hand, draw one additional card.
    Accumulate privileges as others gain colonies.
    """
    name: str = field(default="Oligarch", init=False)
    description: str = field(default="Draw extra card with new hands; accumulate privileges.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class PackRat(AlienPower):
    """
    Pack Rat - Power to Collect.
    Official FFG rules: Before cards selected, take one object from opponent.
    Each collected object adds +1 to your defense total.
    """
    name: str = field(default="PackRat", init=False)
    description: str = field(default="Collect objects; each adds +1 to defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    collected_items: int = field(default=0, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE:
            return base_total + self.collected_items
        return base_total


@dataclass
class Peddler(AlienPower):
    """
    Peddler - Power to Sell.
    Official FFG rules: At start of turn, may spread hand and sell to players.
    Maintain a store of 8 cards to sell during encounters.
    """
    name: str = field(default="Peddler", init=False)
    description: str = field(default="Sell cards from hand or store to other players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Surgeon(AlienPower):
    """
    Surgeon - Power of Surgery.
    Official FFG rules: After destiny, offer wild flares as "facelifts"
    that become temporary alien powers for other players.
    """
    name: str = field(default="Surgeon", init=False)
    description: str = field(default="Give temporary powers to other players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tortoise(AlienPower):
    """
    Tortoise - Power to Dawdle.
    Official FFG rules: At start of turn, receive 4 rewards and end turn.
    Store cards in shell. May attempt solo victory instead of shared win.
    """
    name: str = field(default="Tortoise", init=False)
    description: str = field(default="Take rewards instead of turn; store cards in shell.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    shell_cards: int = field(default=0, init=False)


@dataclass
class Nanny(AlienPower):
    """
    Nanny - Power of Consequences.
    Official FFG rules: When not main player, motivate players with negotiate cards.
    Players in timeout cannot participate. Collect discarded negotiates.
    """
    name: str = field(default="Nanny", init=False)
    description: str = field(default="Give negotiates with consequences; collect discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pretender(AlienPower):
    """
    Pretender - Power to Take Over.
    Official FFG rules: As offense after destiny, swap seats with any player.
    Powers move with you, everything else stays.
    """
    name: str = field(default="Pretender", init=False)
    description: str = field(default="Swap seats with another player; keep your power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Perfectionist(AlienPower):
    """
    Perfectionist - Power to Be Finicky.
    Official FFG rules: When receiving cards, reject unwanted ones and draw replacements.
    Stack rejected cards for later use.
    """
    name: str = field(default="Perfectionist", init=False)
    description: str = field(default="Reject cards when drawing; get replacements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    rejected_cards: int = field(default=0, init=False)


@dataclass
class Particle(AlienPower):
    """
    Particle - Power of Quantum Entanglement.
    Official FFG rules: As offense/ally when landing, entangle planets.
    Ships must stay balanced between entangled planets.
    """
    name: str = field(default="Particle", init=False)
    description: str = field(default="Entangle planets; balance ships between them.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    entangled_pairs: List[Any] = field(default_factory=list, init=False)


@dataclass
class TheCult(AlienPower):
    """
    The Cult - Power of Allegiance.
    Official FFG rules: Offer opponents membership. Members share wins,
    can't ally against each other. Both members in combat = all cards become negotiates.
    """
    name: str = field(default="TheCult", init=False)
    description: str = field(default="Recruit members; all members share wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    members: List[str] = field(default_factory=list, init=False)


# Register Cosmic Eons aliens
AlienRegistry.register(Anarchist())
AlienRegistry.register(AssistantAlien())
AlienRegistry.register(BleedingHeart())
AlienRegistry.register(Coward())
AlienRegistry.register(Crusher())
AlienRegistry.register(EvilTwin())
AlienRegistry.register(FireDancer())
AlienRegistry.register(Hunger())
AlienRegistry.register(Hypochondriac())
AlienRegistry.register(Klutz())
AlienRegistry.register(Maven())
AlienRegistry.register(Moocher())
AlienRegistry.register(Nanny())
AlienRegistry.register(Oligarch())
AlienRegistry.register(PackRat())
AlienRegistry.register(Particle())
AlienRegistry.register(Peddler())
AlienRegistry.register(Perfectionist())
AlienRegistry.register(Pretender())
AlienRegistry.register(Surgeon())
AlienRegistry.register(TheCult())
AlienRegistry.register(Tortoise())


# =============================================================================
# COSMIC DOMINION EXPANSION (30 aliens - adding missing 15)
# =============================================================================

@dataclass
class Angler(AlienPower):
    """
    Angler - Power to Fish.
    Official FFG rules: As main player before cards selected, ask opponent for
    specific card. They give it or you draw from deck.
    """
    name: str = field(default="Angler", init=False)
    description: str = field(default="Fish for specific cards from opponents.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Daredevil(AlienPower):
    """
    Daredevil - Power to Risk.
    Official FFG rules: After reveal, discard attack 01-08 to subtract from total.
    Win by 4 or fewer = rewards equal to ships in encounter.
    """
    name: str = field(default="Daredevil", init=False)
    description: str = field(default="Reduce attack for bigger rewards on close wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Explorer(AlienPower):
    """
    Explorer - Power of Discovery.
    Official FFG rules: As offense after gate aimed, place new planet in system.
    Gain bonuses based on discovered planets.
    """
    name: str = field(default="Explorer", init=False)
    description: str = field(default="Discover new planets; gain bonuses from them.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    discovered_planets: int = field(default=0, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        # Bonus based on discovered planets
        return base_total + self.discovered_planets


@dataclass
class Greenhorn(AlienPower):
    """
    Greenhorn - Power of Ignorance.
    Official FFG rules: Show cards and ask questions. Draw new hand when no attacks.
    Play kickers after reveal. Flexible card timing.
    """
    name: str = field(default="Greenhorn", init=False)
    description: str = field(default="Flexible card timing; draw hand when no attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Host(AlienPower):
    """
    Host - Power to Welcome.
    Official FFG rules: When defending, give gifts to attackers to discourage.
    """
    name: str = field(default="Host", init=False)
    description: str = field(default="Give gifts to discourage attacks.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Joker(AlienPower):
    """
    Joker - Power to Jest.
    Official FFG rules: Play wild with card effects and timing.
    """
    name: str = field(default="Joker", init=False)
    description: str = field(default="Play cards in unexpected ways.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Lizard(AlienPower):
    """
    Lizard - Power to Transmogrify.
    Official FFG rules: After winning as offense, morph 1 ship into +2 bonus.
    Win when all ships morphed.

    Balance adjustment v2: Requires more ships to morph (30) and bonus is +1 per ship.
    Alternate win is harder to achieve but still provides combat advantage.
    """
    name: str = field(default="Lizard", init=False)
    description: str = field(default="Morph 1 ship on offensive wins; each adds +1.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    has_alternate_win: bool = field(default=True, init=False)
    morphed_ships: int = field(default=0, init=False)
    normal_ships: int = field(default=50, init=False)  # Increased for balance (very hard alternate win)

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        # Only morph on offensive wins (per FFG rules)
        if as_main_player and player.power_active and player == game.offense:
            # Morph 1 ship per win
            ships_to_morph = min(1, self.normal_ships)
            self.morphed_ships += ships_to_morph
            self.normal_ships -= ships_to_morph

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        # Morphed ships add +1 each (reduced from +2 for balance)
        return base_total + self.morphed_ships

    def check_alternate_win(self, game: "Game", player: "Player") -> bool:
        return self.normal_ships <= 0


@dataclass
class Love(AlienPower):
    """
    Love - Power of Joy.
    Official FFG rules: At turn start, discard card. Others who match type
    release ships from warp. If not all match, get colony.
    """
    name: str = field(default="Love", init=False)
    description: str = field(default="Match card types to release ships or gain colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mesmer(AlienPower):
    """
    Mesmer - Power of Mass Hypnosis.
    Official FFG rules: After revealing attack < 10, may change it to negotiate.
    Play non-encounter cards as any artifact.
    """
    name: str = field(default="Mesmer", init=False)
    description: str = field(default="Convert low attacks to negotiates.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Mirage(AlienPower):
    """
    Mirage - Power of Delusion.
    Official FFG rules: After reveal, recalculate totals using different colonies'
    ship counts instead of actual ships in encounter.
    """
    name: str = field(default="Mirage", init=False)
    description: str = field(default="Use different colony ship counts for totals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Muckraker(AlienPower):
    """
    Muckraker - Power to Slander.
    Official FFG rules: At resolution start, accuse winning allies of misconduct.
    They pay bribe or lose rewards and ships return.
    """
    name: str = field(default="Muckraker", init=False)
    description: str = field(default="Accuse allies; they bribe or lose rewards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tourist(AlienPower):
    """
    Tourist - Power to Sightsee.
    Official FFG rules: View hidden cards. Cruise liner moves between systems.
    Disembark ships or send postcards home for cards.
    """
    name: str = field(default="Tourist", init=False)
    description: str = field(default="Cruise liner travels; view hidden cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Voyager(AlienPower):
    """
    Voyager - Power to Journey.
    Official FFG rules: At turn start, move home planet to warp. Ships there
    count as both colony and warp location.
    """
    name: str = field(default="Voyager", init=False)
    description: str = field(default="Move home planets to warp; dual location.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Whirligig(AlienPower):
    """
    Whirligig - Power to Swirl.
    Official FFG rules: During planning, mix hands with opponent.
    Choose distribution method, opponent draws randomly.
    """
    name: str = field(default="Whirligig", init=False)
    description: str = field(default="Mix hands with opponent; redistribute.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class YinYang(AlienPower):
    """
    Yin-Yang - Power of Balance.
    Official FFG rules: Ally with both sides simultaneously. Losing defense
    preserves ships. Losing offense gets rewards. Distribute penalty tokens.
    """
    name: str = field(default="YinYang", init=False)
    description: str = field(default="Ally both sides; balance wins and losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register Cosmic Dominion aliens
AlienRegistry.register(Angler())
AlienRegistry.register(Daredevil())
AlienRegistry.register(Explorer())
AlienRegistry.register(Greenhorn())
AlienRegistry.register(Host())
AlienRegistry.register(Joker())
AlienRegistry.register(Lizard())
AlienRegistry.register(Love())
AlienRegistry.register(Mesmer())
AlienRegistry.register(Mirage())
AlienRegistry.register(Muckraker())
AlienRegistry.register(Tourist())
AlienRegistry.register(Voyager())
AlienRegistry.register(Whirligig())
AlienRegistry.register(YinYang())


# =============================================================================
# COSMIC ODYSSEY EXPANSION (42 aliens - adding documented ones)
# =============================================================================

@dataclass
class Magnet(AlienPower):
    """
    Magnet - Power to Attract or Repel.
    Official FFG rules: After alliances formed, force one non-main player
    to join specified side or prevent them from allying.
    """
    name: str = field(default="Magnet", init=False)
    description: str = field(default="Force or prevent player alliances.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Zilch(AlienPower):
    """
    Zilch - Power to Kibitz.
    Official FFG rules: No game components. Predict winner at start.
    If predicted player wins, Zilch wins instead. Can examine anything.
    """
    name: str = field(default="Zilch", init=False)
    description: str = field(default="Predict winner; view everything; win if right.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    has_alternate_win: bool = field(default=True, init=False)
    predicted_winner: Optional[str] = field(default=None, init=False)

    def check_alternate_win(self, game: "Game", player: "Player") -> bool:
        # Zilch wins if their predicted player won
        if self.predicted_winner and game.winners:
            for winner in game.winners:
                if winner.name == self.predicted_winner:
                    return True
        return False


# Register Cosmic Odyssey aliens
AlienRegistry.register(Magnet())
AlienRegistry.register(Zilch())
