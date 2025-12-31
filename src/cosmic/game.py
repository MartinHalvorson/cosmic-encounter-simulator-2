"""
Main Game class for Cosmic Encounter simulator.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Tuple

from .types import GamePhase, GameConfig, Side, PlayerRole, Color, ShipCount, DealType
from .player import Player
from .planet import Planet
from .cards import CosmicDeck, DestinyDeck, RewardsDeck, FlareDeck
from .cards.base import Card, EncounterCard, AttackCard, NegotiateCard, MorphCard, ReinforcementCard, ArtifactCard, KickerCard, FlareCard
from .cards.tech_deck import TechDeck, TechCard, TECH_EFFECTS
from .cards.hazard_deck import HazardDeck, HazardCard, apply_hazard_effect, HazardTiming
from .types import ArtifactType
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
    tech_deck: Optional[TechDeck] = None
    hazard_deck: Optional[HazardDeck] = None

    # Current hazard for the encounter
    current_hazard: Optional[HazardCard] = None

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
    offense_kicker: Optional[KickerCard] = None
    defense_kicker: Optional[KickerCard] = None
    offense_ships: Dict[str, int] = field(default_factory=dict)
    defense_ships: Dict[str, int] = field(default_factory=dict)
    offense_allies: List[Player] = field(default_factory=list)
    defense_allies: List[Player] = field(default_factory=list)

    # Artifact tracking
    zapped_powers: List[Player] = field(default_factory=list)  # Players whose powers are zapped this encounter
    encounter_cancelled: bool = False  # Force Field was played

    # Combat totals (set during resolution for powers that need them)
    offense_total: int = 0
    defense_total: int = 0

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

        # Initialize optional expansion decks
        if self.config.use_tech:
            self.tech_deck = TechDeck()
            self.tech_deck.set_rng(self._rng)

        if self.config.use_hazards:
            self.hazard_deck = HazardDeck()
            self.hazard_deck.set_rng(self._rng)

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

        # Auto-enable 2-player mode for 2-player games
        if num_players == 2:
            self.config.two_player_mode = True
            # Default to dual powers in 2-player mode
            if not self.config.dual_powers:
                self.config.dual_powers = True

        # Generate player names if not provided
        if player_names is None:
            player_names = [f"Player {i+1}" for i in range(num_players)]

        # Get colors
        colors = list(Color)[:num_players]

        # Calculate how many powers needed (double for dual powers)
        powers_needed = num_players * 2 if self.config.dual_powers else num_players

        # Get alien powers
        if powers is None:
            all_aliens = AlienRegistry.get_all()

            # Check for required aliens from config
            if self.config.required_aliens:
                selected_powers = []
                for name in self.config.required_aliens:
                    alien = AlienRegistry.get(name)
                    if alien:
                        selected_powers.append(alien)

                # Fill remaining slots with random aliens
                remaining_count = powers_needed - len(selected_powers)
                if remaining_count > 0:
                    available = [a for a in all_aliens if a not in selected_powers]
                    additional = self._rng.sample(
                        available,
                        min(remaining_count, len(available))
                    )
                    selected_powers.extend(additional)
            else:
                selected_powers = self._rng.sample(
                    all_aliens,
                    min(powers_needed, len(all_aliens))
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
            # Assign secondary power for dual power variant
            if self.config.dual_powers:
                secondary_idx = num_players + i
                if secondary_idx < len(selected_powers):
                    player.secondary_alien = selected_powers[secondary_idx]
            self.players.append(player)

        # Randomize turn order
        self._turn_order = list(self.players)
        self._rng.shuffle(self._turn_order)
        self._player_index = 0

        # Create planets
        self._create_planets()

        # Initialize destiny deck with players
        self.destiny_deck.initialize(self.players)

        # Add flare cards to cosmic deck (one for each alien in the game)
        flare_deck = FlareDeck()
        flare_deck.set_rng(self._rng)
        alien_names = [p.alien.name for p in self.players if p.alien]
        # Add secondary alien flares for dual power games
        if self.config.dual_powers:
            for p in self.players:
                if p.secondary_alien:
                    alien_names.append(p.secondary_alien.name)
        flares = flare_deck.create_flares_for_game(alien_names)
        self.cosmic_deck.add_flares(flares)

        # Deal starting hands
        for player in self.players:
            self._deal_starting_hand(player)

        # Deal starting tech cards (Cosmic Incursion expansion)
        if self.config.use_tech and self.tech_deck:
            self._deal_starting_tech()

        # Apply game start effects
        for player in self.players:
            if player.alien:
                player.alien.on_game_start(self, player)
            # Apply secondary power game start effects
            if player.secondary_alien and self.config.dual_powers:
                player.secondary_alien.on_game_start(self, player)

        self._log(f"Game started with {num_players} players")
        if self.config.two_player_mode:
            self._log("2-player variant enabled")
        if self.config.dual_powers:
            self._log("Dual powers enabled")
        if self.config.use_tech:
            self._log("Tech cards enabled")
        if self.config.use_hazards:
            self._log("Hazards enabled")

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

    def _deal_starting_tech(self) -> None:
        """
        Deal starting tech cards to all players.
        Each player draws 2 tech cards and must start researching one.
        """
        if not self.tech_deck:
            return

        for player in self.players:
            # Draw 2 tech cards
            tech_cards = self.tech_deck.draw_multiple(2)
            player.tech_state.available_techs = tech_cards

            # AI chooses which tech to research
            if tech_cards:
                # For now, pick the first one (AI can be enhanced later)
                chosen = tech_cards[0]
                player.tech_state.start_research(chosen)
                self._log(f"{player.name} begins researching {chosen.name}")

    def _apply_tech_research_progress(self, player: Player) -> None:
        """
        Apply research progress when a player wins an encounter.
        Called during resolution when offense wins or defense holds.
        """
        if not self.config.use_tech:
            return

        completed = player.tech_state.add_research_progress(1)
        if completed:
            self._log(f"{player.name} completes research on {completed.name}!")

            # Draw a new tech to research if available
            if self.tech_deck and self.tech_deck.cards_remaining() > 0:
                new_tech = self.tech_deck.draw()
                if new_tech:
                    player.tech_state.available_techs.append(new_tech)
                    # Start researching the new one
                    player.tech_state.start_research(new_tech)
                    self._log(f"{player.name} begins researching {new_tech.name}")

    def _get_tech_combat_bonus(self, player: Player, is_offense: bool, ship_count: int) -> int:
        """Get combat bonus from completed technologies."""
        if not self.config.use_tech:
            return 0
        return player.tech_state.get_combat_bonus(is_offense, ship_count)

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

        # Reset artifact state for this encounter
        self._reset_encounter_artifacts()

        # Draw hazard for this encounter (Cosmic Storm expansion)
        self._draw_hazard()

        # Check for skip encounter hazard
        if self.current_hazard and self._check_hazard_skip():
            self._handle_turn_end()
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

        # Discard hazard card at end of encounter
        self._discard_hazard()

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
            if player.alien and self.is_power_active(player):
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
            if player.alien and player.alien.name == "Parasite" and self.is_power_active(player):
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
            if player.alien and self.is_power_active(player):
                player.alien.on_planning(self, player, role)

        # Select cards
        off_ai = self.offense.ai_strategy or BasicAI()
        self.offense_card = off_ai.select_encounter_card(self, self.offense, True)
        self.offense.remove_card(self.offense_card)

        def_ai = self.defense.ai_strategy or BasicAI()
        self.defense_card = def_ai.select_encounter_card(self, self.defense, False)
        self.defense.remove_card(self.defense_card)

        # Select kicker cards (optional)
        if isinstance(self.offense_card, AttackCard):
            off_kicker = off_ai.select_kicker_card(
                self, self.offense, True,
                self.offense_card.value, 15  # Estimate opponent total
            )
            if off_kicker:
                self.offense_kicker = off_kicker
                self.offense.remove_card(off_kicker)

        if isinstance(self.defense_card, AttackCard):
            def_kicker = def_ai.select_kicker_card(
                self, self.defense, False,
                self.defense_card.value, 15
            )
            if def_kicker:
                self.defense_kicker = def_kicker
                self.defense.remove_card(def_kicker)

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
            if player.alien and self.is_power_active(player):
                player.alien.on_reveal(self, player, role)

        # Check for flare card plays during reveal
        self._flare_context = {"phase": "reveal", "flare_bonus": 0, "flare_ship_multiplier": 1}
        self._check_flare_opportunity("reveal", self._flare_context)

    def _resolution_phase(self) -> None:
        """Handle the resolution phase."""
        self.phase = GamePhase.RESOLUTION

        # Check if Force Field was played (encounter cancelled)
        if self.encounter_cancelled:
            self._resolve_force_field()
            return

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
            if self.offense.alien and self.offense.alien.name == "Pacifist" and self.is_power_active(self.offense):
                self._resolve_offense_wins()
            else:
                self._resolve_defense_wins()
                self._give_compensation(self.offense, self.defense)
            return

        if def_is_neg and off_is_attack:
            # Check Pacifist
            if self.defense.alien and self.defense.alien.name == "Pacifist" and self.is_power_active(self.defense):
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

        # Apply kicker multipliers
        if self.offense_kicker:
            off_value *= self.offense_kicker.value
            self._log(f"{self.offense.name} plays {self.offense_kicker} (attack becomes {off_value})")
            self.cosmic_deck.discard(self.offense_kicker)

        if self.defense_kicker:
            def_value *= self.defense_kicker.value
            self._log(f"{self.defense.name} plays {self.defense_kicker} (attack becomes {def_value})")
            self.cosmic_deck.discard(self.defense_kicker)

        # Apply power modifications to card values
        for player in [self.offense, self.defense]:
            if player.alien and self.is_power_active(player):
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
            if player.alien and self.is_power_active(player):
                if player == self.offense:
                    off_ships = player.alien.modify_ship_count(
                        self, player, off_ships, Side.OFFENSE
                    )
                else:
                    def_ships = player.alien.modify_ship_count(
                        self, player, def_ships, Side.DEFENSE
                    )

        # Calculate base totals before reinforcements
        off_total = off_value + off_ships
        def_total = def_value + def_ships

        # Store current totals on game object for powers that need to reference them
        self.offense_total = off_total
        self.defense_total = def_total

        # Apply power modifications to totals
        for player in [self.offense, self.defense]:
            if player.alien and self.is_power_active(player):
                if player == self.offense:
                    off_total = player.alien.modify_total(
                        self, player, off_total, Side.OFFENSE
                    )
                    self.offense_total = off_total
                else:
                    def_total = player.alien.modify_total(
                        self, player, def_total, Side.DEFENSE
                    )
                    self.defense_total = def_total

        # Allow reinforcement cards to be played
        off_reinforcements = self._get_reinforcements(self.offense, self.offense_allies, True, off_total, def_total)
        def_reinforcements = self._get_reinforcements(self.defense, self.defense_allies, False, def_total, off_total)

        off_reinforce_bonus = sum(c.value for c in off_reinforcements)
        def_reinforce_bonus = sum(c.value for c in def_reinforcements)

        off_total += off_reinforce_bonus
        def_total += def_reinforce_bonus

        if off_reinforcements:
            for card in off_reinforcements:
                self._log(f"Offense plays {card}")
                self.cosmic_deck.discard(card)

        if def_reinforcements:
            for card in def_reinforcements:
                self._log(f"Defense plays {card}")
                self.cosmic_deck.discard(card)

        # Apply flare bonuses if any were played
        flare_bonus = getattr(self, '_flare_context', {}).get('flare_bonus', 0)
        if flare_bonus > 0:
            # Apply flare bonus to main player who played the flare
            # For simplicity, apply to offense (could be tracked more precisely)
            off_total += flare_bonus
            self._log(f"Flare bonus: +{flare_bonus}")

        # Apply tech bonuses (Cosmic Incursion expansion)
        off_tech_bonus = self._get_tech_combat_bonus(self.offense, True, sum(self.offense_ships.values()))
        def_tech_bonus = self._get_tech_combat_bonus(self.defense, False, sum(self.defense_ships.values()))
        off_total += off_tech_bonus
        def_total += def_tech_bonus

        if off_tech_bonus > 0:
            self._log(f"{self.offense.name} tech bonus: +{off_tech_bonus}")
        if def_tech_bonus > 0:
            self._log(f"{self.defense.name} tech bonus: +{def_tech_bonus}")

        # Update final totals on game object
        self.offense_total = off_total
        self.defense_total = def_total

        self._log(f"Offense total: {off_total} ({off_value} + {sum(self.offense_ships.values())} ships{f' + {off_reinforce_bonus} reinforcement' if off_reinforce_bonus else ''})")
        self._log(f"Defense total: {def_total} ({def_value} + {sum(self.defense_ships.values())} ships{f' + {def_reinforce_bonus} reinforcement' if def_reinforce_bonus else ''})")

        # Check for Loser/Antimatter
        reverse_winner = False
        for player in [self.offense, self.defense]:
            if player.alien and self.is_power_active(player):
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
                if player.alien and self.is_power_active(player):
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

        # Tech research progress for winner
        self._apply_tech_research_progress(self.offense)

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
                if player.alien and self.is_power_active(player):
                    ships_to_warp = player.alien.on_ships_to_warp(
                        self, player, ships_to_warp, "encounter_loss"
                    )
                player.send_ships_to_warp(ships_to_warp)

        # Defensive allies get rewards (choice: cards OR ships from warp)
        for ally in self.defense_allies:
            reward_count = self.defense_ships.get(ally.name, 0)
            ally_ai = ally.ai_strategy or BasicAI()
            reward_choice = ally_ai.choose_ally_reward(self, ally, reward_count)

            if reward_choice == "cards":
                # Draw cards from rewards deck
                rewards = self.rewards_deck.draw_multiple(reward_count)
                ally.add_cards(rewards)
                self._log(f"{ally.name} draws {reward_count} reward cards")
            else:
                # Retrieve ships from warp
                retrieved = ally.retrieve_ships_from_warp(reward_count)
                ally.return_ships_to_colonies(retrieved, ally.home_planets)
                self._log(f"{ally.name} retrieves {retrieved} ships from warp")

            # Return ally ships to colonies
            ally.return_ships_to_colonies(reward_count, ally.home_planets)

        # Defense ships stay on planet (return to planet for allies)
        for ally in self.defense_allies:
            ally_ships = self.defense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ally_ships, ally.home_planets)

        # Win/lose hooks
        self.defense.alien and self.defense.alien.on_win_encounter(self, self.defense, True)
        self.offense.alien and self.offense.alien.on_lose_encounter(self, self.offense, True)

        # Tech research progress for winner
        self._apply_tech_research_progress(self.defense)

        # Discard encounter cards
        self._discard_encounter_cards()

    def _resolve_deal(self) -> None:
        """Handle deal negotiation when both play negotiate."""
        self._log("Deal phase!")

        # Get proposals from both players
        off_ai = self.offense.ai_strategy or BasicAI()
        def_ai = self.defense.ai_strategy or BasicAI()

        off_proposal = off_ai.negotiate_deal(self, self.offense, self.defense)
        def_proposal = def_ai.negotiate_deal(self, self.defense, self.offense)

        # Both must agree for deal to succeed
        # A deal succeeds if both propose (any valid deal)
        deal = off_proposal if (off_proposal and def_proposal) else None

        if deal:
            deal_type = deal.get("type", "colony_swap")
            self._apply_deal(deal_type, deal)

            # Deal success hooks
            for player in [self.offense, self.defense]:
                if player.alien:
                    player.alien.on_deal_success(self, player, self.defense if player == self.offense else self.offense)
        else:
            self._log("Deal failed!")
            self._apply_failed_deal_penalty()

    def _apply_deal(self, deal_type: str, deal: Dict[str, Any]) -> None:
        """Apply the effects of a successful deal."""
        if deal_type == "colony_swap" or deal_type == DealType.COLONY_SWAP.value:
            self._log("Deal successful - colony swap")
            # Both gain colonies
            off_ships = self.offense_ships.get(self.offense.name, 0)
            self.defense_planet.add_ships(self.offense.name, off_ships)

            def_ships = self.defense_ships.get(self.defense.name, 0)
            if self.offense.home_planets:
                off_planet = self._rng.choice(self.offense.home_planets)
                off_planet.add_ships(self.defense.name, def_ships)

        elif deal_type == "card_trade" or deal_type == DealType.CARD_TRADE.value:
            self._log("Deal successful - card trade")
            cards_to_trade = deal.get("cards", 1)
            # Exchange cards (up to available)
            off_tradeable = min(cards_to_trade, len(self.offense.hand))
            def_tradeable = min(cards_to_trade, len(self.defense.hand))

            # Swap random cards
            off_cards = self._rng.sample(self.offense.hand, min(off_tradeable, def_tradeable))
            def_cards = self._rng.sample(self.defense.hand, min(off_tradeable, def_tradeable))

            for card in off_cards:
                self.offense.remove_card(card)
                self.defense.add_card(card)
            for card in def_cards:
                self.defense.remove_card(card)
                self.offense.add_card(card)

        elif deal_type == "one_colony" or deal_type == DealType.ONE_COLONY.value:
            self._log("Deal successful - one colony")
            # Only offense gets a colony
            off_ships = self.offense_ships.get(self.offense.name, 0)
            self.defense_planet.add_ships(self.offense.name, off_ships)

        elif deal_type == "card_colony" or deal_type == DealType.CARD_FOR_COLONY.value:
            self._log("Deal successful - cards for colony")
            # Offense gets colony, defense gets cards
            off_ships = self.offense_ships.get(self.offense.name, 0)
            self.defense_planet.add_ships(self.offense.name, off_ships)
            # Defense draws cards
            cards_to_draw = deal.get("cards", 2)
            for _ in range(cards_to_draw):
                card = self.cosmic_deck.draw()
                if card:
                    self.defense.add_card(card)

        # Return ally ships to their colonies
        for ally in self.offense_allies:
            ally_ships = self.offense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ally_ships, ally.home_planets)
        for ally in self.defense_allies:
            ally_ships = self.defense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ally_ships, ally.home_planets)

    def _apply_failed_deal_penalty(self) -> None:
        """Apply the 3-ship penalty for a failed deal."""
        failed_deal_penalty = 3

        for main_player in [self.offense, self.defense]:
            ships_to_lose = min(failed_deal_penalty, main_player.total_ships_in_play(self.planets))
            if ships_to_lose > 0:
                # Handle power modifications (like Zombie)
                actual_ships = ships_to_lose
                if main_player.alien and self.is_power_active(main_player):
                    actual_ships = main_player.alien.on_ships_to_warp(
                        self, main_player, ships_to_lose, "failed_deal"
                    )
                if actual_ships > 0:
                    main_player.get_ships_from_colonies(actual_ships, self.planets, exclude_last_ship=False)
                    main_player.send_ships_to_warp(actual_ships)

            # Return all ships in the encounter (they weren't lost, just not used)
            # Ships from gate go back to colonies
            for name, count in self.offense_ships.items():
                player = self.get_player_by_name(name)
                if player and player != self.offense:  # Allies return normally
                    player.return_ships_to_colonies(count, player.home_planets)

            for name, count in self.defense_ships.items():
                player = self.get_player_by_name(name)
                if player and player != self.defense:  # Allies return normally
                    player.return_ships_to_colonies(count, player.home_planets)

            # Deal failure hooks
            for player in [self.offense, self.defense]:
                if player.alien:
                    player.alien.on_deal_failure(self, player, self.defense if player == self.offense else self.offense)

        self._discard_encounter_cards()

    def _get_reinforcements(
        self,
        main_player: Player,
        allies: List[Player],
        is_offense: bool,
        current_total: int,
        opponent_total: int
    ) -> List[ReinforcementCard]:
        """
        Get reinforcement cards from main player and allies.

        Per rules: Main player plays first, then allies can add reinforcements.
        Each side totals their reinforcements before comparing.
        """
        all_reinforcements = []

        # Main player selects reinforcements
        ai = main_player.ai_strategy or BasicAI()
        main_reinforcements = ai.select_reinforcement_cards(
            self, main_player, is_offense, current_total, opponent_total
        )

        for card in main_reinforcements:
            if card in main_player.hand:
                main_player.remove_card(card)
                all_reinforcements.append(card)

        # Allies can also play reinforcements
        updated_total = current_total + sum(c.value for c in all_reinforcements)

        for ally in allies:
            ally_ai = ally.ai_strategy or BasicAI()
            ally_reinforcements = ally_ai.select_reinforcement_cards(
                self, ally, is_offense, updated_total, opponent_total
            )

            for card in ally_reinforcements:
                if card in ally.hand:
                    ally.remove_card(card)
                    all_reinforcements.append(card)
                    updated_total += card.value

        return all_reinforcements

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
        # Reset kicker cards (already discarded during combat if used)
        self.offense_kicker = None
        self.defense_kicker = None

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
        won_encounter = (
            self.defense_planet is not None and
            self.offense is not None and
            self.defense_planet.has_colony(self.offense.name)
        )

        can_have_second = False

        # Skip if no offense player set (encounter was skipped)
        if self.offense is None:
            self._player_index = (self._player_index + 1) % len(self._turn_order)
            self.encounter_number = 1
            return

        # Machine can always have another encounter if they have encounter cards
        if self.offense.alien and self.offense.alien.name == "Machine" and self.is_power_active(self.offense):
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

    # ========== Artifact Methods ==========

    def _reset_encounter_artifacts(self) -> None:
        """Reset artifact state at start of encounter."""
        self.zapped_powers = []
        self.encounter_cancelled = False

    def _check_artifact_opportunity(self, phase: str, context: Dict[str, Any]) -> Optional[ArtifactCard]:
        """
        Check if any player wants to play an artifact in the current context.

        Args:
            phase: Current phase name
            context: Context information for artifact decision

        Returns:
            The artifact played, or None
        """
        # Check each player in turn order (starting from offense)
        check_order = [self.offense, self.defense] + [
            p for p in self.players if p != self.offense and p != self.defense
        ]

        for player in check_order:
            if player is None:
                continue

            ai = player.ai_strategy or BasicAI()
            artifact = ai.select_artifact_to_play(self, player, phase, context)

            if artifact and artifact in player.hand:
                return self._play_artifact(player, artifact, context)

        return None

    def _play_artifact(self, player: Player, artifact: ArtifactCard, context: Dict[str, Any]) -> ArtifactCard:
        """
        Play an artifact card and apply its effect.

        Args:
            player: Player playing the artifact
            artifact: The artifact card to play
            context: Context for the effect

        Returns:
            The artifact that was played
        """
        player.remove_card(artifact)
        self._log(f"{player.name} plays {artifact}")

        artifact_type = artifact.artifact_type

        if artifact_type == ArtifactType.COSMIC_ZAP:
            self._apply_cosmic_zap(context)
        elif artifact_type == ArtifactType.MOBIUS_TUBES:
            self._apply_mobius_tubes(player)
        elif artifact_type == ArtifactType.FORCE_FIELD:
            self._apply_force_field()
        elif artifact_type == ArtifactType.CARD_ZAP:
            self._apply_card_zap(context)
        elif artifact_type == ArtifactType.IONIC_GAS:
            self._apply_ionic_gas(context)
        elif artifact_type == ArtifactType.PLAGUE:
            self._apply_plague(context)
        elif artifact_type == ArtifactType.EMOTION_CONTROL:
            self._apply_emotion_control(context)
        elif artifact_type == ArtifactType.QUASH:
            self._apply_quash(context)

        self.cosmic_deck.discard(artifact)
        return artifact

    def _apply_cosmic_zap(self, context: Dict[str, Any]) -> None:
        """Cancel a player's alien power for this encounter."""
        target = context.get("target_player")
        if target and target not in self.zapped_powers:
            self.zapped_powers.append(target)
            self._log(f"{target.name}'s power is zapped!")

    def _apply_mobius_tubes(self, player: Player) -> None:
        """Free all of player's ships from the warp."""
        ships = player.ships_in_warp
        if ships > 0:
            player.retrieve_ships_from_warp(ships)
            player.return_ships_to_colonies(ships, player.home_planets)
            self._log(f"{player.name} frees {ships} ships from warp!")

    def _apply_force_field(self) -> None:
        """End the encounter with no winner or loser."""
        self.encounter_cancelled = True
        self._log("Force Field ends the encounter!")

    def _apply_card_zap(self, context: Dict[str, Any]) -> None:
        """Cancel an encounter card - player must play another."""
        target_card = context.get("target_card")
        target_player = context.get("target_player")
        if target_card and target_player:
            # Card is already played, treat as 0 value attack
            self._log(f"{target_player.name}'s {target_card} is zapped!")

    def _apply_ionic_gas(self, context: Dict[str, Any]) -> None:
        """Prevent allies from participating."""
        # Clear allies from both sides
        for ally in self.offense_allies:
            ships = self.offense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ships, ally.home_planets)
        for ally in self.defense_allies:
            ships = self.defense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ships, ally.home_planets)

        self.offense_allies = []
        self.defense_allies = []
        # Remove ally ships from encounter totals
        self.offense_ships = {k: v for k, v in self.offense_ships.items() if k == self.offense.name}
        self.defense_ships = {k: v for k, v in self.defense_ships.items() if k == self.defense.name}
        self._log("Ionic Gas disperses all allies!")

    def _apply_plague(self, context: Dict[str, Any]) -> None:
        """Send ships from a colony to the warp."""
        target_player = context.get("target_player")
        target_planet = context.get("target_planet")
        if target_player and target_planet:
            ships = target_planet.get_ships(target_player.name)
            if ships > 0:
                target_planet.remove_ships(target_player.name, ships)
                target_player.send_ships_to_warp(ships)
                self._log(f"Plague sends {ships} of {target_player.name}'s ships to warp!")

    def _apply_emotion_control(self, context: Dict[str, Any]) -> None:
        """Force opponent to play a negotiate card if they have one."""
        target_player = context.get("target_player")
        if target_player:
            negotiate_cards = [c for c in target_player.hand if isinstance(c, NegotiateCard)]
            if negotiate_cards:
                self._log(f"{target_player.name} is forced to play Negotiate!")
                # The effect is checked during planning phase

    def _apply_quash(self, context: Dict[str, Any]) -> None:
        """Cancel a flare or artifact being played."""
        # Similar to cosmic zap but for cards
        self._log("Quash cancels the effect!")

    # ========== Flare Card Methods ==========

    def _check_flare_opportunity(self, phase: str, context: Dict[str, Any]) -> Optional[FlareCard]:
        """
        Check if any player wants to play a flare in the current context.

        Args:
            phase: Current phase name
            context: Context information for flare decision

        Returns:
            The flare played, or None
        """
        # Check each player in turn order
        check_order = [self.offense, self.defense] + [
            p for p in self.players if p != self.offense and p != self.defense
        ]

        for player in check_order:
            if player is None:
                continue

            ai = player.ai_strategy or BasicAI()
            flare = ai.select_flare_to_play(self, player, phase, context)

            if flare and flare in player.hand:
                return self._play_flare(player, flare, context)

        return None

    def _play_flare(self, player: Player, flare: FlareCard, context: Dict[str, Any]) -> FlareCard:
        """
        Play a flare card and apply its effect.

        Args:
            player: Player playing the flare
            flare: The flare card to play
            context: Context for the effect

        Returns:
            The flare that was played
        """
        player.remove_card(flare)

        # Check if player can use Super (matching alien)
        can_use_super = (
            player.alien and
            player.alien.name == flare.alien_name and
            player.power_active and
            player not in self.zapped_powers
        )

        if can_use_super:
            self._log(f"{player.name} plays {flare} (Super effect)!")
            self._apply_flare_super(player, flare, context)
        else:
            self._log(f"{player.name} plays {flare} (Wild effect)!")
            self._apply_flare_wild(player, flare, context)

        self.cosmic_deck.discard(flare)
        return flare

    def _apply_flare_wild(self, player: Player, flare: FlareCard, context: Dict[str, Any]) -> None:
        """Apply a flare's Wild effect (usable by anyone)."""
        alien_name = flare.alien_name

        # Machine Wild: Take one extra encounter
        if alien_name == "Machine":
            self._flare_extra_encounter = True

        # Zombie Wild: Return 2 ships from warp
        elif alien_name == "Zombie":
            ships = min(2, player.ships_in_warp)
            if ships > 0:
                player.retrieve_ships_from_warp(ships)
                player.return_ships_to_colonies(ships, player.home_planets)

        # Human Wild: Add +3 to total
        elif alien_name == "Human":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 3

        # Warrior Wild: +1 per ship in warp
        elif alien_name == "Warrior":
            bonus = player.ships_in_warp
            context["flare_bonus"] = context.get("flare_bonus", 0) + bonus

        # Macron Wild: Ships count as 2 each
        elif alien_name == "Macron":
            context["flare_ship_multiplier"] = 2

        # Healer Wild: Return 3 ships from any warp
        elif alien_name == "Healer":
            if player.ships_in_warp >= 3:
                player.retrieve_ships_from_warp(3)
                player.return_ships_to_colonies(3, player.home_planets)

        # Trader Wild: Draw 2 cards
        elif alien_name == "Trader":
            for _ in range(2):
                card = self.cosmic_deck.draw()
                player.add_card(card)

        # Filch Wild: Steal a random card
        elif alien_name == "Filch":
            opponents = [p for p in self.players if p != player and p.hand]
            if opponents:
                target = self._rng.choice(opponents)
                if target.hand:
                    stolen = self._rng.choice(target.hand)
                    target.remove_card(stolen)
                    player.add_card(stolen)

        # Shadow Wild: Add 2 ships from colonies
        elif alien_name == "Shadow":
            taken = player.get_ships_from_colonies(2, self.planets)
            if taken > 0:
                if player == self.offense:
                    self.offense_ships[player.name] = self.offense_ships.get(player.name, 0) + taken
                elif player == self.defense:
                    self.defense_ships[player.name] = self.defense_ships.get(player.name, 0) + taken
                context["flare_bonus"] = context.get("flare_bonus", 0)  # Ships add naturally

        # Warpish Wild: Send 2 opponent ships to warp
        elif alien_name == "Warpish":
            opponent = self.defense if player == self.offense else self.offense
            if opponent:
                ships_to_remove = min(2, sum(self.defense_ships.values()) if player == self.offense else sum(self.offense_ships.values()))
                if player == self.offense and self.defense:
                    removed = min(ships_to_remove, self.defense_ships.get(self.defense.name, 0))
                    self.defense_ships[self.defense.name] = self.defense_ships.get(self.defense.name, 0) - removed
                    self.defense.ships_in_warp += removed
                elif self.offense:
                    removed = min(ships_to_remove, self.offense_ships.get(self.offense.name, 0))
                    self.offense_ships[self.offense.name] = self.offense_ships.get(self.offense.name, 0) - removed
                    self.offense.ships_in_warp += removed

        # Spiff Wild: Draw 1 from rewards deck
        elif alien_name == "Spiff":
            card = self.rewards_deck.draw()
            if card:
                player.add_card(card)

        # Horde Wild: Return 1 ship from warp
        elif alien_name == "Horde":
            if player.ships_in_warp >= 1:
                player.retrieve_ships_from_warp(1)
                player.return_ships_to_colonies(1, player.home_planets)

        # Clone Wild: Copy card just played (give +2 bonus since we can't actually copy)
        elif alien_name == "Clone":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 2

        # Loser Wild: Win this encounter if you would lose
        elif alien_name == "Loser":
            context["loser_flare_wild"] = True

        # Pacifist Wild: Add +10 if playing negotiate
        elif alien_name == "Pacifist":
            if player == self.offense and isinstance(self.offense_card, NegotiateCard):
                context["flare_bonus"] = context.get("flare_bonus", 0) + 10
            elif player == self.defense and isinstance(self.defense_card, NegotiateCard):
                context["flare_bonus"] = context.get("flare_bonus", 0) + 10

        # Assassin Wild: Eliminate 1 opponent ship
        elif alien_name == "Assassin":
            opponent = self.defense if player == self.offense else self.offense
            if opponent:
                if player == self.offense:
                    removed = min(1, self.defense_ships.get(opponent.name, 0))
                    self.defense_ships[opponent.name] = self.defense_ships.get(opponent.name, 0) - removed
                    opponent.ships_in_warp += removed
                else:
                    removed = min(1, self.offense_ships.get(opponent.name, 0))
                    self.offense_ships[opponent.name] = self.offense_ships.get(opponent.name, 0) - removed
                    opponent.ships_in_warp += removed

        # Mutant Wild: Draw 2 cards, keep 1
        elif alien_name == "Mutant":
            cards = [self.cosmic_deck.draw() for _ in range(2)]
            cards = [c for c in cards if c]
            if cards:
                # Keep the better card (higher attack or any non-attack)
                best = max(cards, key=lambda c: c.value if hasattr(c, 'value') and c.value else 0)
                player.add_card(best)
                for c in cards:
                    if c != best:
                        self.cosmic_deck.discard(c)

        # Fodder Wild: Sacrifice 1 ship for +2
        elif alien_name == "Fodder":
            if player == self.offense and self.offense_ships.get(player.name, 0) > 1:
                self.offense_ships[player.name] -= 1
                player.ships_in_warp += 1
                context["flare_bonus"] = context.get("flare_bonus", 0) + 2
            elif player == self.defense and self.defense_ships.get(player.name, 0) > 1:
                self.defense_ships[player.name] -= 1
                player.ships_in_warp += 1
                context["flare_bonus"] = context.get("flare_bonus", 0) + 2

        # Grudge Wild: +3 against attacker
        elif alien_name == "Grudge":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 3

        # Chosen Wild: Add top card of deck to total
        elif alien_name == "Chosen":
            card = self.cosmic_deck.draw()
            if card and hasattr(card, 'value') and card.value:
                context["flare_bonus"] = context.get("flare_bonus", 0) + card.value
            self.cosmic_deck.discard(card)

        # Default: +2 to total (generic Wild effect)
        else:
            context["flare_bonus"] = context.get("flare_bonus", 0) + 2

    def _apply_flare_super(self, player: Player, flare: FlareCard, context: Dict[str, Any]) -> None:
        """Apply a flare's Super effect (only for matching alien)."""
        alien_name = flare.alien_name

        # Machine Super: Take two extra encounters
        if alien_name == "Machine":
            self._flare_extra_encounter = True
            self._flare_extra_encounter_count = 2

        # Zombie Super: Return all ships from warp
        elif alien_name == "Zombie":
            ships = player.ships_in_warp
            if ships > 0:
                player.retrieve_ships_from_warp(ships)
                player.return_ships_to_colonies(ships, player.home_planets)

        # Human Super: Add +6 to total
        elif alien_name == "Human":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 6

        # Warrior Super: +2 per ship in warp
        elif alien_name == "Warrior":
            bonus = player.ships_in_warp * 2
            context["flare_bonus"] = context.get("flare_bonus", 0) + bonus

        # Macron Super: Ships count as 5 each
        elif alien_name == "Macron":
            context["flare_ship_multiplier"] = 5

        # Healer Super: Return all ships from warp to colonies
        elif alien_name == "Healer":
            for p in self.players:
                ships = p.ships_in_warp
                if ships > 0:
                    p.retrieve_ships_from_warp(ships)
                    p.return_ships_to_colonies(ships, p.home_planets)

        # Trader Super: Trade hands with any player
        elif alien_name == "Trader":
            opponents = [p for p in self.players if p != player]
            if opponents:
                # Trade with player who has most cards
                target = max(opponents, key=lambda p: len(p.hand))
                player.hand, target.hand = target.hand, player.hand

        # Filch Super: Steal 2 cards
        elif alien_name == "Filch":
            opponents = [p for p in self.players if p != player and p.hand]
            if opponents:
                target = self._rng.choice(opponents)
                for _ in range(min(2, len(target.hand))):
                    if target.hand:
                        stolen = self._rng.choice(target.hand)
                        target.remove_card(stolen)
                        player.add_card(stolen)

        # Virus Super: Triple ship count when adding
        elif alien_name == "Virus":
            context["flare_ship_multiplier"] = 3

        # Oracle Super: Look at and force different card
        elif alien_name == "Oracle":
            # Effect handled specially during planning
            context["oracle_super"] = True

        # Parasite Super: Join both sides
        elif alien_name == "Parasite":
            context["parasite_both_sides"] = True

        # Shadow Super: Add 4 ships from colonies
        elif alien_name == "Shadow":
            taken = player.get_ships_from_colonies(4, self.planets)
            if taken > 0:
                if player == self.offense:
                    self.offense_ships[player.name] = self.offense_ships.get(player.name, 0) + taken
                elif player == self.defense:
                    self.defense_ships[player.name] = self.defense_ships.get(player.name, 0) + taken

        # Warpish Super: Send 4 opponent ships to warp
        elif alien_name == "Warpish":
            opponent = self.defense if player == self.offense else self.offense
            if opponent:
                if player == self.offense and self.defense:
                    removed = min(4, self.defense_ships.get(self.defense.name, 0))
                    self.defense_ships[self.defense.name] = self.defense_ships.get(self.defense.name, 0) - removed
                    self.defense.ships_in_warp += removed
                elif self.offense:
                    removed = min(4, self.offense_ships.get(self.offense.name, 0))
                    self.offense_ships[self.offense.name] = self.offense_ships.get(self.offense.name, 0) - removed
                    self.offense.ships_in_warp += removed

        # Spiff Super: Draw 2 from rewards deck
        elif alien_name == "Spiff":
            for _ in range(2):
                card = self.rewards_deck.draw()
                if card:
                    player.add_card(card)

        # Horde Super: Return 2 ships from warp
        elif alien_name == "Horde":
            ships = min(2, player.ships_in_warp)
            if ships > 0:
                player.retrieve_ships_from_warp(ships)
                player.return_ships_to_colonies(ships, player.home_planets)

        # Clone Super: Play same card again (give +4 bonus as approximation)
        elif alien_name == "Clone":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 4

        # Loser Super: Automatically lose and win
        elif alien_name == "Loser":
            context["loser_flare_super"] = True

        # Pacifist Super: Extra colony on negotiate win
        elif alien_name == "Pacifist":
            context["pacifist_extra_colony"] = True
            if player == self.offense and isinstance(self.offense_card, NegotiateCard):
                context["flare_bonus"] = context.get("flare_bonus", 0) + 10
            elif player == self.defense and isinstance(self.defense_card, NegotiateCard):
                context["flare_bonus"] = context.get("flare_bonus", 0) + 10

        # Assassin Super: Eliminate 3 opponent ships
        elif alien_name == "Assassin":
            opponent = self.defense if player == self.offense else self.offense
            if opponent:
                if player == self.offense:
                    removed = min(3, self.defense_ships.get(opponent.name, 0))
                    self.defense_ships[opponent.name] = self.defense_ships.get(opponent.name, 0) - removed
                    opponent.ships_in_warp += removed
                else:
                    removed = min(3, self.offense_ships.get(opponent.name, 0))
                    self.offense_ships[opponent.name] = self.offense_ships.get(opponent.name, 0) - removed
                    opponent.ships_in_warp += removed

        # Mutant Super: Draw 4 cards, keep 2
        elif alien_name == "Mutant":
            cards = [self.cosmic_deck.draw() for _ in range(4)]
            cards = [c for c in cards if c]
            if cards:
                # Sort by value and keep best 2
                cards.sort(key=lambda c: c.value if hasattr(c, 'value') and c.value else 0, reverse=True)
                for i, c in enumerate(cards):
                    if i < 2:
                        player.add_card(c)
                    else:
                        self.cosmic_deck.discard(c)

        # Fodder Super: Sacrifice any ships for +3 each
        elif alien_name == "Fodder":
            if player == self.offense:
                ships_available = self.offense_ships.get(player.name, 0) - 1
                sacrifice = min(ships_available, 2)  # Sacrifice up to 2
                if sacrifice > 0:
                    self.offense_ships[player.name] -= sacrifice
                    player.ships_in_warp += sacrifice
                    context["flare_bonus"] = context.get("flare_bonus", 0) + (sacrifice * 3)
            elif player == self.defense:
                ships_available = self.defense_ships.get(player.name, 0) - 1
                sacrifice = min(ships_available, 2)
                if sacrifice > 0:
                    self.defense_ships[player.name] -= sacrifice
                    player.ships_in_warp += sacrifice
                    context["flare_bonus"] = context.get("flare_bonus", 0) + (sacrifice * 3)

        # Grudge Super: +6 against attacker
        elif alien_name == "Grudge":
            context["flare_bonus"] = context.get("flare_bonus", 0) + 6

        # Chosen Super: Add top 2 cards of deck to total
        elif alien_name == "Chosen":
            total_bonus = 0
            for _ in range(2):
                card = self.cosmic_deck.draw()
                if card and hasattr(card, 'value') and card.value:
                    total_bonus += card.value
                if card:
                    self.cosmic_deck.discard(card)
            context["flare_bonus"] = context.get("flare_bonus", 0) + total_bonus

        # Tripler Super: Triple attack card value
        elif alien_name == "Tripler":
            context["tripler_super"] = True  # Handled in combat resolution

        # Chronos Super: Take two additional turns
        elif alien_name == "Chronos":
            context["chronos_extra_turns"] = 2

        # Diplomat Super: Force deal success with 2 colonies
        elif alien_name == "Diplomat":
            context["diplomat_force_deal"] = True

        # Default: +4 to total (generic Super effect)
        else:
            context["flare_bonus"] = context.get("flare_bonus", 0) + 4

    def _resolve_force_field(self) -> None:
        """Handle resolution when Force Field was played - encounter ends with no winner."""
        self._log("Force Field ends encounter - all ships return to colonies")

        # Return all offense ships to colonies
        for name, count in self.offense_ships.items():
            player = self.get_player_by_name(name)
            if player:
                player.return_ships_to_colonies(count, player.home_planets)

        # Defense ships stay on planet (they were defending there)
        # But allied defense ships return
        for ally in self.defense_allies:
            ally_ships = self.defense_ships.get(ally.name, 0)
            ally.return_ships_to_colonies(ally_ships, ally.home_planets)

        # Discard encounter cards
        self._discard_encounter_cards()

    def is_power_active(self, player: Player) -> bool:
        """Check if a player's power is currently active (not zapped)."""
        if player in self.zapped_powers:
            return False
        return player.power_active

    # ========== Hazard Methods ==========

    def _draw_hazard(self) -> None:
        """Draw a hazard card for this encounter if hazards are enabled."""
        if not self.config.use_hazards or not self.hazard_deck:
            self.current_hazard = None
            return

        self.current_hazard = self.hazard_deck.draw()
        if self.current_hazard:
            self._log(f"⚠️ Hazard: {self.current_hazard.name} - {self.current_hazard.description}")

            # Apply immediate (START_ENCOUNTER) hazard effects
            if self.current_hazard.timing == HazardTiming.START_ENCOUNTER:
                apply_hazard_effect(self, self.current_hazard)

    def _discard_hazard(self) -> None:
        """Discard the current hazard card at the end of the encounter."""
        if self.hazard_deck and self.current_hazard:
            self.hazard_deck.discard(self.current_hazard)
            self.current_hazard = None

    def _check_hazard_skip(self) -> bool:
        """Check if the current hazard causes the encounter to be skipped."""
        if not self.current_hazard:
            return False

        effect_data = self.hazard_deck.get_effect(self.current_hazard) if self.hazard_deck else {}
        if effect_data.get("effect") == "skip_encounter":
            self._log("Time Warp - Encounter skipped!")
            self._discard_hazard()
            return True

        return False

    def _check_hazard_no_alliances(self) -> bool:
        """Check if current hazard prevents alliances."""
        if not self.current_hazard:
            return False

        if self.current_hazard.timing == HazardTiming.DURING_ALLIANCE:
            effect_data = self.hazard_deck.get_effect(self.current_hazard) if self.hazard_deck else {}
            return effect_data.get("effect") == "no_alliances"

        return False

    def _apply_hazard_reveal_effects(self) -> None:
        """Apply hazard effects during reveal phase."""
        if not self.current_hazard or self.current_hazard.timing != HazardTiming.DURING_REVEAL:
            return

        effect_data = self.hazard_deck.get_effect(self.current_hazard) if self.hazard_deck else {}
        effect_type = effect_data.get("effect", "")

        if effect_type == "halve_attacks":
            # Attack values will be halved in resolution
            self._log("Nebula Cloud - Attack values are halved!")

    def _apply_hazard_resolution_effects(self) -> Tuple[bool, bool]:
        """
        Apply hazard effects during resolution.

        Returns:
            Tuple of (swap_outcome, permanent_loss)
        """
        swap_outcome = False
        permanent_loss = False

        if not self.current_hazard or self.current_hazard.timing != HazardTiming.DURING_RESOLUTION:
            return swap_outcome, permanent_loss

        effect_data = self.hazard_deck.get_effect(self.current_hazard) if self.hazard_deck else {}
        effect_type = effect_data.get("effect", "")

        if effect_type == "swap_outcome":
            swap_outcome = True
            self._log("Dimensional Rift - Winner and loser are swapped!")

        if effect_type == "permanent_loss":
            permanent_loss = True
            self._log("Ships are permanently lost instead of going to warp!")

        return swap_outcome, permanent_loss
