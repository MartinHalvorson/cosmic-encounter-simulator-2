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
