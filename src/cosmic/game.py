"""
Main Game class for Cosmic Encounter simulator.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

from .types import GamePhase, GameConfig, Side, PlayerRole, Color, ShipCount
from .player import Player
from .planet import Planet
from .cards import CosmicDeck, DestinyDeck, RewardsDeck
from .cards.base import Card, EncounterCard, AttackCard, NegotiateCard, MorphCard
from .aliens import AlienRegistry, AlienPower
from .ai.basic_ai import BasicAI


@dataclass
class Game:
    """
    A single game of Cosmic Encounter.
    """
    config: GameConfig = field(default_factory=GameConfig)
    players: List[Player] = field(default_factory=list)
    planets: List[Planet] = field(default_factory=list)

    # Decks
    cosmic_deck: CosmicDeck = field(default_factory=CosmicDeck)
    destiny_deck: DestinyDeck = field(default_factory=DestinyDeck)
    rewards_deck: RewardsDeck = field(default_factory=RewardsDeck)

    # Game state
    phase: GamePhase = GamePhase.START_TURN
    current_turn: int = 0
    encounter_number: int = 1  # 1 or 2 per turn

    # Current encounter state
    offense: Optional[Player] = None
    defense: Optional[Player] = None
    defense_planet: Optional[Planet] = None
    offense_card: Optional[EncounterCard] = None
    defense_card: Optional[EncounterCard] = None
    offense_ships: Dict[str, int] = field(default_factory=dict)
    defense_ships: Dict[str, int] = field(default_factory=dict)
    offense_allies: List[Player] = field(default_factory=list)
    defense_allies: List[Player] = field(default_factory=list)

    # Game result
    is_over: bool = False
    winners: List[Player] = field(default_factory=list)

    # Internal
    _rng: random.Random = field(default_factory=random.Random)
    _turn_order: List[Player] = field(default_factory=list)
    _player_index: int = 0

    # Logging/debugging
    log: List[str] = field(default_factory=list)
    verbose: bool = False

    def __post_init__(self):
        if self.config.seed is not None:
            self._rng.seed(self.config.seed)
            self.cosmic_deck.set_rng(self._rng)
            self.destiny_deck.set_rng(self._rng)
            self.rewards_deck.set_rng(self._rng)

    def setup(
        self,
        player_names: Optional[List[str]] = None,
        powers: Optional[List[str]] = None
    ) -> None:
        """
        Set up a new game with players and powers.

        Args:
            player_names: Names for players (default: Player 1, Player 2, etc.)
            powers: Alien power names to assign (default: random)
        """
        num_players = self.config.num_players

        # Generate player names if not provided
        if player_names is None:
            player_names = [f"Player {i+1}" for i in range(num_players)]

        # Get colors
        colors = list(Color)[:num_players]

        # Get alien powers
        if powers is None:
            all_aliens = AlienRegistry.get_all()
            selected_powers = self._rng.sample(
                all_aliens,
                min(num_players, len(all_aliens))
            )
        else:
            selected_powers = []
            for name in powers:
                alien = AlienRegistry.get(name)
                if alien:
                    selected_powers.append(alien)
                else:
                    # Default to no power
                    selected_powers.append(None)

        # Create players
        default_ai = BasicAI()
        self.players = []
        for i in range(num_players):
            player = Player(
                name=player_names[i],
                color=colors[i],
                alien=selected_powers[i] if i < len(selected_powers) else None,
                ai_strategy=default_ai
            )
            self.players.append(player)

        # Randomize turn order
        self._turn_order = list(self.players)
        self._rng.shuffle(self._turn_order)
        self._player_index = 0

        # Create planets
        self._create_planets()

        # Initialize destiny deck with players
        self.destiny_deck.initialize(self.players)

        # Deal starting hands
        for player in self.players:
            self._deal_starting_hand(player)

        # Apply game start effects
        for player in self.players:
            if player.alien:
                player.alien.on_game_start(self, player)

        self._log(f"Game started with {num_players} players")

    def _create_planets(self) -> None:
        """Create home planets for all players."""
        self.planets = []
        planet_id = 0

        for player in self.players:
            home_planets = []
            ships_per_planet = self.config.starting_ships_per_planet

            # Check for Symbiote (double ships)
            if player.alien and player.alien.name == "Symbiote":
                ships_per_planet = ships_per_planet * 2

            for _ in range(self.config.starting_planets):
                planet = Planet(
                    owner=player,
                    ships=ShipCount(counts={player.name: ships_per_planet}),
                    planet_id=planet_id
                )
                self.planets.append(planet)
                home_planets.append(planet)
                planet_id += 1

            player.home_planets = home_planets

    def _deal_starting_hand(self, player: Player) -> None:
        """Deal starting hand to a player."""
        cards = self.cosmic_deck.draw_multiple(self.config.starting_hand_size)
        player.add_cards(cards)

        # Redeal if no encounter cards
        while not player.has_encounter_card():
            # Discard and redraw
            for card in list(player.hand):
                self.cosmic_deck.discard(card)
            player.hand.clear()
            cards = self.cosmic_deck.draw_multiple(self.config.starting_hand_size)
            player.add_cards(cards)

    def get_player_by_name(self, name: str) -> Optional[Player]:
        """Get player by name."""
        for player in self.players:
            if player.name == name:
                return player
        return None

    def get_home_planets(self, player: Player) -> List[Planet]:
        """Get home planets for a player."""
        return [p for p in self.planets if p.owner == player]

    def get_foreign_colonies(self, player: Player) -> List[Planet]:
        """Get foreign colonies for a player."""
        return [p for p in self.planets if p.is_foreign_colony(player)]

    def _log(self, message: str) -> None:
        """Log a game event."""
        self.log.append(message)
        if self.verbose:
            print(message)

    # ========== Game Flow ==========

    def play(self) -> List[Player]:
        """
        Play the game to completion.

        Returns:
            List of winners
        """
        while not self.is_over and self.current_turn < self.config.max_turns:
            self.play_encounter()

        return self.winners

    def play_encounter(self) -> None:
        """Play a single encounter."""
        if self.is_over:
            return

        # Start turn phase
        if self.encounter_number == 1:
            self.current_turn += 1
            self.offense = self._turn_order[self._player_index]
            self._log(f"\n=== Turn {self.current_turn}: {self.offense.name}'s turn ===")

        self.phase = GamePhase.START_TURN

        # Call turn start hooks
        for player in self.players:
            if player.alien:
                player.alien.on_turn_start(self, player)
            if player.alien:
                player.alien.on_encounter_start(self, player)

        # Regroup phase (retrieve ship from warp)
        self._regroup_phase()

        # Destiny phase
        self._destiny_phase()

        # Launch phase
        self._launch_phase()

        # Alliance phase
        self._alliance_phase()

        # Planning phase
        self._planning_phase()

        # Reveal phase
        self._reveal_phase()

        # Resolution phase
        self._resolution_phase()

        # Check for game end
        self._check_game_end()

        # End of encounter hooks
        for player in self.players:
            if player.alien:
                player.alien.on_encounter_end(self, player)

        # Determine if second encounter
        if not self.is_over:
            self._handle_turn_end()

    def _regroup_phase(self) -> None:
        """Handle the regroup phase."""
        self.phase = GamePhase.REGROUP

        # Offense can retrieve 1 ship from warp
        if self.offense.ships_in_warp > 0:
            retrieved = self.offense.retrieve_ships_from_warp(1)
            if retrieved > 0:
                self.offense.return_ships_to_colonies(retrieved, self.offense.home_planets)
                self._log(f"{self.offense.name} retrieves 1 ship from warp")

        # Power hooks
        for player in self.players:
            role = self._get_player_role(player)
            if player.alien:
                player.alien.on_regroup(self, player, role)

    def _destiny_phase(self) -> None:
        """Handle the destiny phase."""
        self.phase = GamePhase.DESTINY

        # Draw destiny
        destiny_card = self.destiny_deck.draw(self.offense)
        self.defense = destiny_card.player
        self.destiny_deck.discard(destiny_card)

        self._log(f"Destiny: {self.defense.name}")

        # Power hooks (can redirect destiny)
        for player in self.players:
            role = self._get_player_role(player)
            if player.alien and player.power_active:
                redirect = player.alien.on_destiny(self, player, role, self.defense)
                if redirect and redirect != self.defense:
                    self._log(f"{player.name} redirects destiny to {redirect.name}")
                    self.defense = redirect

    def _launch_phase(self) -> None:
        """Handle the launch phase."""
        self.phase = GamePhase.LAUNCH

        # Reset encounter state
        self.offense_ships = {}
        self.defense_ships = {}
        self.offense_allies = []
        self.defense_allies = []

        # Select planet to attack
        ai = self.offense.ai_strategy or BasicAI()
        self.defense_planet = ai.select_attack_planet(self, self.offense, self.defense)

        # Select ships to commit
        max_ships = self.config.max_ships_per_encounter
        ship_count = ai.select_ships_for_encounter(self, self.offense, max_ships)

        # Take ships from colonies
        taken = self.offense.get_ships_from_colonies(ship_count, self.planets)
        self.offense_ships[self.offense.name] = taken

        # Defense ships are those on the planet
        def_ships = self.defense_planet.get_ships(self.defense.name)
        self.defense_ships[self.defense.name] = def_ships

        self._log(f"Attack: {self.defense_planet} with {taken} ships")
        self._log(f"Defense: {def_ships} ships")

    def _alliance_phase(self) -> None:
        """Handle the alliance phase."""
        self.phase = GamePhase.ALLIANCE

        # Get potential allies (not offense or defense)
        potential = [p for p in self.players if p != self.offense and p != self.defense]

        # Offense invites allies
        off_ai = self.offense.ai_strategy or BasicAI()
        off_invites = off_ai.decide_alliance_invitation(self, self.offense, potential, True)

        # Defense invites allies
        def_ai = self.defense.ai_strategy or BasicAI()
        def_invites = def_ai.decide_alliance_invitation(self, self.defense, potential, False)

        # Players respond to invitations
        for player in potential:
            invited_off = player in off_invites
            invited_def = player in def_invites

            # Check for Parasite power (can join uninvited)
            if player.alien and player.alien.name == "Parasite" and player.power_active:
                invited_off = True
                invited_def = True

            if not invited_off and not invited_def:
                continue

            player_ai = player.ai_strategy or BasicAI()
            choice = player_ai.decide_alliance_response(
                self, player, self.offense, self.defense,
                invited_off, invited_def
            )

            if choice == Side.OFFENSE:
                self.offense_allies.append(player)
                ships = player_ai.select_ally_ships(
                    self, player, self.config.max_ships_per_encounter
                )
                taken = player.get_ships_from_colonies(ships, self.planets)
                self.offense_ships[player.name] = taken
                self._log(f"{player.name} joins offense with {taken} ships")

            elif choice == Side.DEFENSE:
                self.defense_allies.append(player)
                ships = player_ai.select_ally_ships(
                    self, player, self.config.max_ships_per_encounter
                )
                taken = player.get_ships_from_colonies(ships, self.planets)
                self.defense_ships[player.name] = taken
                self._log(f"{player.name} joins defense with {taken} ships")

    def _planning_phase(self) -> None:
        """Handle the planning phase."""
        self.phase = GamePhase.PLANNING

        # Ensure players have encounter cards
        self._ensure_encounter_card(self.offense)
        self._ensure_encounter_card(self.defense)

        # Power hooks (Trader, Kamikazee, etc.)
        for player in [self.offense, self.defense]:
            role = self._get_player_role(player)
            if player.alien and player.power_active:
                player.alien.on_planning(self, player, role)

        # Select cards
        off_ai = self.offense.ai_strategy or BasicAI()
        self.offense_card = off_ai.select_encounter_card(self, self.offense, True)
        self.offense.remove_card(self.offense_card)

        def_ai = self.defense.ai_strategy or BasicAI()
        self.defense_card = def_ai.select_encounter_card(self, self.defense, False)
        self.defense.remove_card(self.defense_card)

        self._log(f"{self.offense.name} selects card")
        self._log(f"{self.defense.name} selects card")

    def _reveal_phase(self) -> None:
        """Handle the reveal phase."""
        self.phase = GamePhase.REVEAL

        self._log(f"Reveal: {self.offense.name} plays {self.offense_card}")
        self._log(f"Reveal: {self.defense.name} plays {self.defense_card}")

        # Power hooks (Mirror, Sorcerer, etc.)
        for player in [self.offense, self.defense]:
            role = self._get_player_role(player)
            if player.alien and player.power_active:
                player.alien.on_reveal(self, player, role)

    def _resolution_phase(self) -> None:
        """Handle the resolution phase."""
        self.phase = GamePhase.RESOLUTION

        off_card = self.offense_card
        def_card = self.defense_card

        # Handle different card combinations
        off_is_attack = isinstance(off_card, AttackCard)
        def_is_attack = isinstance(def_card, AttackCard)
        off_is_neg = isinstance(off_card, NegotiateCard)
        def_is_neg = isinstance(def_card, NegotiateCard)

        # Both negotiate -> deal
        if off_is_neg and def_is_neg:
            self._resolve_deal()
            return

        # One negotiate, one attack
        if off_is_neg and def_is_attack:
            # Check Pacifist
            if self.offense.alien and self.offense.alien.name == "Pacifist" and self.offense.power_active:
                self._resolve_offense_wins()
            else:
                self._resolve_defense_wins()
                self._give_compensation(self.offense, self.defense)
            return

        if def_is_neg and off_is_attack:
            # Check Pacifist
            if self.defense.alien and self.defense.alien.name == "Pacifist" and self.defense.power_active:
                self._resolve_defense_wins()
            else:
                self._resolve_offense_wins()
                self._give_compensation(self.defense, self.offense)
            return

        # Both attack -> compare totals
        self._resolve_attack_vs_attack()

    def _resolve_attack_vs_attack(self) -> None:
        """Resolve when both sides play attack cards."""
        off_card = self.offense_card
        def_card = self.defense_card

        # Get base values
        off_value = off_card.value if isinstance(off_card, AttackCard) else 0
        def_value = def_card.value if isinstance(def_card, AttackCard) else 0

        # Apply power modifications to card values
        for player in [self.offense, self.defense]:
            if player.alien and player.power_active:
                if player == self.offense:
                    off_value = player.alien.modify_attack_value(
                        self, player, off_value, Side.OFFENSE
                    )
                else:
                    def_value = player.alien.modify_attack_value(
                        self, player, def_value, Side.DEFENSE
                    )

        # Calculate ship totals
        off_ships = sum(self.offense_ships.values())
        def_ships = sum(self.defense_ships.values())

        # Apply power modifications to ship counts
        for player in [self.offense, self.defense]:
            if player.alien and player.power_active:
                if player == self.offense:
                    off_ships = player.alien.modify_ship_count(
                        self, player, off_ships, Side.OFFENSE
                    )
                else:
                    def_ships = player.alien.modify_ship_count(
                        self, player, def_ships, Side.DEFENSE
                    )

        # Calculate totals
        off_total = off_value + off_ships
        def_total = def_value + def_ships

        # Apply power modifications to totals
        for player in [self.offense, self.defense]:
            if player.alien and player.power_active:
                if player == self.offense:
                    off_total = player.alien.modify_total(
                        self, player, off_total, Side.OFFENSE
                    )
                else:
                    def_total = player.alien.modify_total(
                        self, player, def_total, Side.DEFENSE
                    )

        self._log(f"Offense total: {off_total} ({off_value} + {sum(self.offense_ships.values())} ships)")
        self._log(f"Defense total: {def_total} ({def_value} + {sum(self.defense_ships.values())} ships)")

        # Check for Loser/Antimatter
        reverse_winner = False
        for player in [self.offense, self.defense]:
            if player.alien and player.power_active:
                if player.alien.name in ["Loser", "Antimatter"]:
                    reverse_winner = True
                    break

        # Determine winner
        if reverse_winner:
            if off_total < def_total:
                self._resolve_offense_wins()
            else:
                self._resolve_defense_wins()
        else:
            if off_total > def_total:
                self._resolve_offense_wins()
            else:
                self._resolve_defense_wins()

    def _resolve_offense_wins(self) -> None:
        """Handle offense winning the encounter."""
        self._log("Offense wins!")

        # Defense ships go to warp
        for name, count in self.defense_ships.items():
            player = self.get_player_by_name(name)
            if player:
                ships_to_warp = count
                if player.alien and player.power_active:
                    ships_to_warp = player.alien.on_ships_to_warp(
                        self, player, ships_to_warp, "encounter_loss"
                    )
                player.send_ships_to_warp(ships_to_warp)

        # Clear defense ships from planet
        self.defense_planet.set_ships(self.defense.name, 0)

        # Offense and allies land on planet
        for name, count in self.offense_ships.items():
            self.defense_planet.add_ships(name, count)
            player = self.get_player_by_name(name)
            if player and player.alien:
                player.alien.on_gain_colony(self, player, self.defense_planet)

        # Win/lose hooks
        self.offense.alien and self.offense.alien.on_win_encounter(self, self.offense, True)
        self.defense.alien and self.defense.alien.on_lose_encounter(self, self.defense, True)

        # Discard encounter cards
        self._discard_encounter_cards()

    def _resolve_defense_wins(self) -> None:
        """Handle defense winning the encounter."""
        self._log("Defense wins!")

        # Offense ships go to warp
        for name, count in self.offense_ships.items():
            player = self.get_player_by_name(name)
            if player:
                ships_to_warp = count
                if player.alien and player.power_active:
                    ships_to_warp = player.alien.on_ships_to_warp(
                        self, player, ships_to_warp, "encounter_loss"
                    )
                player.send_ships_to_warp(ships_to_warp)

        # Defensive allies get rewards
        for ally in self.defense_allies:
            reward_count = self.defense_ships.get(ally.name, 0)
            rewards = self.rewards_deck.draw_multiple(reward_count)
            ally.add_cards(rewards)
            # Return ally ships to colonies
            ally.return_ships_to_colonies(reward_count, ally.home_planets)

        # Defense ships stay on planet (return to planet for allies)
        for ally in self.defense_allies:
            ally_ships = self.defense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ally_ships, ally.home_planets)

        # Win/lose hooks
        self.defense.alien and self.defense.alien.on_win_encounter(self, self.defense, True)
        self.offense.alien and self.offense.alien.on_lose_encounter(self, self.offense, True)

        # Discard encounter cards
        self._discard_encounter_cards()

    def _resolve_deal(self) -> None:
        """Handle deal negotiation when both play negotiate."""
        self._log("Deal phase!")

        off_ai = self.offense.ai_strategy or BasicAI()
        deal = off_ai.negotiate_deal(self, self.offense, self.defense)

        if deal:
            self._log("Deal successful - colony swap")
            # Both gain colonies
            # Offense lands on defense planet
            off_ships = self.offense_ships.get(self.offense.name, 0)
            self.defense_planet.add_ships(self.offense.name, off_ships)

            # Defense lands on offense planet
            def_ships = self.defense_ships.get(self.defense.name, 0)
            off_planet = self._rng.choice(self.offense.home_planets)
            off_planet.add_ships(self.defense.name, def_ships)

            # Deal success hooks
            for player in [self.offense, self.defense]:
                if player.alien:
                    player.alien.on_deal_success(self, player, self.defense if player == self.offense else self.offense)
        else:
            self._log("Deal failed!")
            # Both lose ships
            for name, count in self.offense_ships.items():
                player = self.get_player_by_name(name)
                if player:
                    player.send_ships_to_warp(count)

            for name, count in self.defense_ships.items():
                player = self.get_player_by_name(name)
                if player:
                    player.send_ships_to_warp(count)

            # Deal failure hooks
            for player in [self.offense, self.defense]:
                if player.alien:
                    player.alien.on_deal_failure(self, player, self.defense if player == self.offense else self.offense)

        self._discard_encounter_cards()

    def _give_compensation(self, receiver: Player, giver: Player) -> None:
        """Give compensation to player who played negotiate."""
        # Number of cards = ships lost
        count = self.offense_ships.get(receiver.name, 0) if receiver == self.offense else self.defense_ships.get(receiver.name, 0)

        if count == 0:
            count = 1

        # Check for Hacker power
        if receiver.alien and receiver.alien.name == "Hacker" and receiver.power_active:
            count = receiver.alien.on_compensation(self, receiver, giver, count)
            if count == 0:
                return  # Hacker handled it

        # Take random cards from giver
        for _ in range(min(count, len(giver.hand))):
            if giver.hand:
                card = self._rng.choice(giver.hand)
                giver.remove_card(card)
                receiver.add_card(card)

    def _discard_encounter_cards(self) -> None:
        """Discard the played encounter cards."""
        if self.offense_card:
            self.cosmic_deck.discard(self.offense_card)
            self.offense_card = None
        if self.defense_card:
            self.cosmic_deck.discard(self.defense_card)
            self.defense_card = None

    def _ensure_encounter_card(self, player: Player) -> None:
        """Ensure player has an encounter card, dealing new hand if needed."""
        if not player.has_encounter_card():
            # Discard hand
            for card in list(player.hand):
                self.cosmic_deck.discard(card)
            player.hand.clear()

            # Draw new hand
            cards = self.cosmic_deck.draw_multiple(self.config.starting_hand_size)
            player.add_cards(cards)
            self._log(f"{player.name} draws a new hand")

    def _get_player_role(self, player: Player) -> PlayerRole:
        """Get a player's role in the current encounter."""
        if player == self.offense:
            return PlayerRole.OFFENSE
        if player == self.defense:
            return PlayerRole.DEFENSE
        if player in self.offense_allies:
            return PlayerRole.OFFENSIVE_ALLY
        if player in self.defense_allies:
            return PlayerRole.DEFENSIVE_ALLY
        return PlayerRole.NOT_INVOLVED

    def _handle_turn_end(self) -> None:
        """Handle end of encounter, possibly allowing second encounter."""
        # Check if Machine power or won encounter
        won_encounter = any(
            player == self.offense and self.defense_planet.has_colony(player.name)
            for player in [self.offense]
        )

        can_have_second = False

        # Machine can always have another encounter if they have encounter cards
        if self.offense.alien and self.offense.alien.name == "Machine" and self.offense.power_active:
            if self.offense.has_encounter_card():
                can_have_second = True

        # Normal: won first encounter and have encounter card
        elif self.encounter_number == 1 and won_encounter and self.offense.has_encounter_card():
            can_have_second = True

        if can_have_second:
            ai = self.offense.ai_strategy or BasicAI()
            if ai.want_second_encounter(self, self.offense):
                self.encounter_number = 2
                self._log(f"{self.offense.name} takes a second encounter")
                return

        # Move to next player's turn
        self._player_index = (self._player_index + 1) % len(self._turn_order)
        self.encounter_number = 1

    def _check_game_end(self) -> None:
        """Check if any player has won the game."""
        for player in self.players:
            # Standard win: 5 foreign colonies
            colonies = player.count_foreign_colonies(self.planets)
            if colonies >= self.config.colonies_to_win:
                if player not in self.winners:
                    self.winners.append(player)
                    self._log(f"{player.name} wins with {colonies} colonies!")

            # Alternate win conditions
            if player.alien and player.alien.has_alternate_win:
                if player.alien.check_alternate_win(self, player):
                    if player not in self.winners:
                        self.winners.append(player)
                        self._log(f"{player.name} wins via {player.alien.name}!")

            # Update power status
            home_count = len([p for p in self.planets if p.owner == player and p.has_colony(player.name)])
            player.check_power_status(home_count)

        if self.winners:
            self.is_over = True
