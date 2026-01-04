"""
Player representation for Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, TYPE_CHECKING

from .types import Color, PlayerRole, SpaceStation, StationType
from .cards.base import Card, EncounterCard, AttackCard, NegotiateCard, MorphCard
from .cards.tech_deck import PlayerTechState

if TYPE_CHECKING:
    from .planet import Planet
    from .aliens.base import AlienPower
    from .ai.base import AIStrategy


@dataclass
class Player:
    """
    A player in the Cosmic Encounter game.
    """
    name: str
    color: Color
    alien: Optional["AlienPower"] = None
    secondary_alien: Optional["AlienPower"] = None  # For 2-player dual power variant
    ai_strategy: Optional["AIStrategy"] = None

    # Hand of cards
    hand: List[Card] = field(default_factory=list)

    # Power state
    power_active: bool = True
    secondary_power_active: bool = True  # For 2-player variant

    # Special counters for specific alien powers
    warrior_tokens: int = 0
    tick_tock_tokens: int = 0

    # Ships in the warp
    ships_in_warp: int = 0

    # Technology research state (Cosmic Incursion expansion)
    tech_state: PlayerTechState = field(default_factory=PlayerTechState)

    # Space stations (Cosmic Storm expansion)
    space_stations: List[SpaceStation] = field(default_factory=list)
    available_stations: List[StationType] = field(default_factory=list)  # Unplaced stations

    # Reference to home planets (set by Game)
    _home_planets: List["Planet"] = field(default_factory=list)

    def __post_init__(self):
        # Validate color
        if isinstance(self.color, str):
            self.color = Color(self.color)

    @property
    def alien_name(self) -> str:
        """Get the alien power name, or 'None' if no power."""
        return self.alien.name if self.alien else "None"

    @property
    def home_planets(self) -> List["Planet"]:
        """Get planets owned by this player."""
        return self._home_planets

    @home_planets.setter
    def home_planets(self, planets: List["Planet"]) -> None:
        self._home_planets = planets

    def get_foreign_colonies(self, all_planets: List["Planet"]) -> List["Planet"]:
        """Get planets where this player has colonies but doesn't own."""
        return [p for p in all_planets if p.is_foreign_colony(self)]

    def count_foreign_colonies(self, all_planets: List["Planet"]) -> int:
        """Count the number of foreign colonies."""
        return len(self.get_foreign_colonies(all_planets))

    def total_ships_in_play(self, all_planets: List["Planet"]) -> int:
        """Count all ships this player has on planets."""
        return sum(p.get_ships(self.name) for p in all_planets)

    def total_ships(self, all_planets: List["Planet"]) -> int:
        """Total ships including those in the warp."""
        return self.total_ships_in_play(all_planets) + self.ships_in_warp

    # ========== Hand Management ==========

    def add_card(self, card: Card) -> None:
        """Add a card to hand."""
        self.hand.append(card)

    def add_cards(self, cards: List[Card]) -> None:
        """Add multiple cards to hand."""
        self.hand.extend(cards)

    def remove_card(self, card: Card) -> None:
        """Remove a specific card from hand."""
        self.hand.remove(card)

    def has_card(self, card: Card) -> bool:
        """Check if a specific card is in hand."""
        return card in self.hand

    def has_encounter_card(self) -> bool:
        """Check if player has at least one encounter card."""
        return any(card.is_encounter_card() for card in self.hand)

    def get_encounter_cards(self) -> List[EncounterCard]:
        """Get all encounter cards in hand."""
        return [card for card in self.hand if card.is_encounter_card()]

    def get_attack_cards(self) -> List[AttackCard]:
        """Get all attack cards in hand."""
        return [card for card in self.hand if isinstance(card, AttackCard)]

    def get_negotiate_cards(self) -> List[NegotiateCard]:
        """Get all negotiate cards in hand."""
        return [card for card in self.hand if isinstance(card, NegotiateCard)]

    def hand_size(self) -> int:
        """Number of cards in hand."""
        return len(self.hand)

    # ========== Card Selection Helpers ==========

    def select_highest_attack(self) -> Optional[AttackCard]:
        """Select the highest value attack card in hand."""
        attacks = self.get_attack_cards()
        if not attacks:
            return None
        return max(attacks, key=lambda c: c.value)

    def select_lowest_attack(self) -> Optional[AttackCard]:
        """Select the lowest value attack card in hand."""
        attacks = self.get_attack_cards()
        if not attacks:
            return None
        return min(attacks, key=lambda c: c.value)

    def select_nth_highest_attack(self, n: int) -> Optional[AttackCard]:
        """Select the nth highest attack card (1 = highest)."""
        attacks = sorted(self.get_attack_cards(), key=lambda c: c.value, reverse=True)
        if len(attacks) < n:
            return attacks[-1] if attacks else None
        return attacks[n - 1]

    def select_negotiate(self) -> Optional[NegotiateCard]:
        """Select a negotiate card if available."""
        negs = self.get_negotiate_cards()
        return negs[0] if negs else None

    def select_encounter_card_for_tripler(self) -> Optional[EncounterCard]:
        """
        Select best card for Tripler power.
        Cards <= 10 are tripled, cards > 10 are divided by 3.
        """
        encounters = self.get_encounter_cards()
        if not encounters:
            return None

        def tripler_value(card: EncounterCard) -> int:
            if isinstance(card, AttackCard):
                if card.value <= 10:
                    return card.value * 3
                return (card.value + 2) // 3
            return 0

        return max(encounters, key=tripler_value)

    # ========== Ship Management ==========

    def get_ships_from_colonies(
        self,
        count: int,
        planets: List["Planet"],
        exclude_last_ship: bool = True
    ) -> int:
        """
        Take ships from player's colonies.
        Returns actual number of ships taken.

        Args:
            count: Number of ships to take
            planets: All planets in the game
            exclude_last_ship: If True, won't take the last ship from a colony
        """
        taken = 0
        # Prefer taking from planets with more ships
        player_planets = [p for p in planets if p.has_colony(self.name)]
        player_planets.sort(key=lambda p: p.get_ships(self.name), reverse=True)

        for planet in player_planets:
            while taken < count:
                current = planet.get_ships(self.name)
                min_ships = 1 if exclude_last_ship else 0
                if current > min_ships:
                    planet.remove_ships(self.name, 1)
                    taken += 1
                else:
                    break
            if taken >= count:
                break

        return taken

    def return_ships_to_colonies(
        self,
        count: int,
        home_planets: List["Planet"]
    ) -> int:
        """
        Return ships to home colonies.
        Ships are distributed among planets that already have ships.
        """
        returned = 0
        # Prefer planets that already have ships
        valid_planets = [p for p in home_planets if p.get_ships(self.name) > 0]
        if not valid_planets:
            valid_planets = home_planets

        for i in range(count):
            if valid_planets:
                planet = valid_planets[i % len(valid_planets)]
                planet.add_ships(self.name, 1)
                returned += 1

        return returned

    def send_ships_to_warp(self, count: int) -> None:
        """Send ships to the warp."""
        self.ships_in_warp += count

    def retrieve_ships_from_warp(self, count: int) -> int:
        """
        Retrieve ships from the warp.
        Returns actual number retrieved.
        """
        to_retrieve = min(count, self.ships_in_warp)
        self.ships_in_warp -= to_retrieve
        return to_retrieve

    # ========== Power State ==========

    def check_power_status(self, home_planet_count: int) -> None:
        """
        Update power_active based on home colony count.
        Powers are lost when player has fewer than 3 home colonies.
        (Exception: Masochist keeps power)
        """
        if self.alien and self.alien.name == "Masochist":
            return
        self.power_active = home_planet_count >= 3

    def use_power(self) -> bool:
        """
        Attempt to use alien power.
        Returns True if power is active and can be used.
        """
        return self.power_active and self.alien is not None

    # ========== Space Station Management ==========

    def place_station(
        self,
        station_type: StationType,
        planet_id: int
    ) -> Optional[SpaceStation]:
        """
        Place a space station on a planet.
        Returns the station if successful, None otherwise.
        """
        # Check if we have this station type available
        if station_type not in self.available_stations:
            return None

        # Check if we already have a station on this planet
        for s in self.space_stations:
            if s.planet_id == planet_id:
                return None

        # Create and place the station
        station = SpaceStation(
            owner=self.name,
            station_type=station_type,
            planet_id=planet_id
        )
        self.available_stations.remove(station_type)
        self.space_stations.append(station)
        return station

    def get_station_on_planet(self, planet_id: int) -> Optional[SpaceStation]:
        """Get the station on a specific planet, if any."""
        for station in self.space_stations:
            if station.planet_id == planet_id and station.active:
                return station
        return None

    def has_station_on_planet(self, planet_id: int) -> bool:
        """Check if player has an active station on a planet."""
        return self.get_station_on_planet(planet_id) is not None

    def get_station_defense_bonus(self, planet_id: int) -> int:
        """Get defense bonus from station on a planet."""
        station = self.get_station_on_planet(planet_id)
        if station:
            return station.get_defense_bonus()
        return 0

    def station_provides_colony(self, planet_id: int) -> bool:
        """Check if station on planet counts as a colony."""
        station = self.get_station_on_planet(planet_id)
        return station.provides_colony_presence() if station else False

    def get_regroup_bonus_from_stations(self) -> int:
        """Get extra ships to retrieve during regroup from Gamma stations."""
        return sum(
            1 for s in self.space_stations
            if s.active and s.station_type == StationType.STATION_GAMMA
        )

    # ========== Comparison & Display ==========

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Player):
            return NotImplemented
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __str__(self) -> str:
        alien_str = self.alien_name
        return f"Player({self.name}, {self.color.value}, {alien_str})"

    def __repr__(self) -> str:
        return self.__str__()

    def detailed_str(self, show_hand: bool = True) -> str:
        """Detailed string representation including hand and planets."""
        lines = [f"Player: {self.name} | {self.color.value} | {self.alien_name}"]
        lines.append(f"  Power Active: {self.power_active}")
        lines.append(f"  Ships in Warp: {self.ships_in_warp}")

        if self.warrior_tokens > 0:
            lines.append(f"  Warrior Tokens: {self.warrior_tokens}")
        if self.tick_tock_tokens > 0:
            lines.append(f"  Tick-Tock Tokens: {self.tick_tock_tokens}")

        if show_hand:
            lines.append(f"  Hand ({len(self.hand)} cards):")
            for card in self.hand:
                lines.append(f"    - {card}")

        return "\n".join(lines)
