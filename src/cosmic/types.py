"""
Core types and enums for Cosmic Encounter simulator.
"""

from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .player import Player


class GamePhase(Enum):
    """Phases of an encounter in Cosmic Encounter."""
    START_TURN = auto()
    REGROUP = auto()
    DESTINY = auto()
    LAUNCH = auto()
    ALLIANCE = auto()
    PLANNING = auto()
    REVEAL = auto()
    RESOLUTION = auto()


class CardType(Enum):
    """Types of cards in the cosmic deck."""
    ATTACK = "attack"
    NEGOTIATE = "negotiate"
    MORPH = "morph"
    REINFORCEMENT = "reinforcement"
    ARTIFACT = "artifact"
    FLARE = "flare"
    KICKER = "kicker"


class EncounterCardType(Enum):
    """Types of encounter cards (subset of CardType)."""
    ATTACK = "attack"
    NEGOTIATE = "negotiate"
    MORPH = "morph"


class ArtifactType(Enum):
    """Types of artifact cards."""
    COSMIC_ZAP = "cosmic_zap"
    CARD_ZAP = "card_zap"
    MOBIUS_TUBES = "mobius_tubes"
    EMOTION_CONTROL = "emotion_control"
    FORCE_FIELD = "force_field"
    QUASH = "quash"
    IONIC_GAS = "ionic_gas"
    PLAGUE = "plague"
    OMNI_ZAP = "omni_zap"
    SOLAR_WIND = "solar_wind"
    REBIRTH = "rebirth"
    SHIP_ZAP = "ship_zap"
    HAND_ZAP = "hand_zap"
    SPACE_JUNK = "space_junk"
    VICTORY_BOON = "victory_boon"


class PowerTiming(Enum):
    """When an alien power can be used."""
    # Start of turn
    START_TURN = auto()
    # During regroup
    REGROUP = auto()
    # When destiny is drawn
    DESTINY = auto()
    # During launch phase
    LAUNCH = auto()
    # During alliance phase
    ALLIANCE = auto()
    # During planning phase
    PLANNING = auto()
    # When cards are revealed
    REVEAL = auto()
    # During resolution
    RESOLUTION = auto()
    # Any time
    ANY = auto()
    # When ships would go to warp
    SHIPS_TO_WARP = auto()
    # When winning encounter
    WIN_ENCOUNTER = auto()
    # When losing encounter
    LOSE_ENCOUNTER = auto()
    # When gaining cards
    GAIN_CARDS = auto()
    # Constant/passive effect
    CONSTANT = auto()
    # Start of an encounter
    START_ENCOUNTER = auto()
    # End of an encounter
    END_ENCOUNTER = auto()


class PowerType(Enum):
    """Classification of alien power type."""
    MANDATORY = auto()  # Must use when applicable
    OPTIONAL = auto()   # May choose to use


class Side(Enum):
    """Side in an encounter."""
    OFFENSE = auto()
    DEFENSE = auto()


class DealType(Enum):
    """Types of deals that can be negotiated."""
    COLONY_SWAP = "colony_swap"      # Both players exchange colonies
    CARD_TRADE = "card_trade"        # Players exchange cards
    ONE_COLONY = "one_colony"        # Only one player gets a colony
    CARD_FOR_COLONY = "card_colony"  # Cards traded for colony rights


class PlayerRole(Enum):
    """Role of a player in an encounter."""
    OFFENSE = auto()
    DEFENSE = auto()
    OFFENSIVE_ALLY = auto()
    DEFENSIVE_ALLY = auto()
    NOT_INVOLVED = auto()


class Color(Enum):
    """Player colors."""
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"
    YELLOW = "Yellow"
    PURPLE = "Purple"
    ORANGE = "Orange"
    BLACK = "Black"
    WHITE = "White"


class Expansion(Enum):
    """Cosmic Encounter expansions and content sources."""
    # Base game (2008) - always included
    BASE = "base"
    # Official FFG Expansions
    COSMIC_INCURSION = "cosmic_incursion"      # 2010 - Tech, Rewards, 20 aliens
    COSMIC_CONFLICT = "cosmic_conflict"        # 2011 - Hazards, 20 aliens
    COSMIC_ALLIANCE = "cosmic_alliance"        # 2012 - Team variant, 20 aliens
    COSMIC_STORM = "cosmic_storm"              # 2013 - Space stations, 25 aliens
    COSMIC_DOMINION = "cosmic_dominion"        # 2014 - Rewards, 30 aliens
    COSMIC_EONS = "cosmic_eons"                # 2016 - Essences, 30 aliens
    COSMIC_ODYSSEY = "cosmic_odyssey"          # 2022 - Lux, Rifts, 42 aliens
    # Homebrew/Custom content
    HOMEBREW = "homebrew"


# Mapping of expansion features to their source expansion
EXPANSION_FEATURES = {
    "flares": Expansion.BASE,
    "tech": Expansion.COSMIC_INCURSION,
    "rewards": Expansion.COSMIC_INCURSION,
    "hazards": Expansion.COSMIC_CONFLICT,
    "team_mode": Expansion.COSMIC_ALLIANCE,
    "space_stations": Expansion.COSMIC_STORM,
    "lux": Expansion.COSMIC_ODYSSEY,
    "rifts": Expansion.COSMIC_ODYSSEY,
}


@dataclass
class EncounterResult:
    """Result of an encounter."""
    winner: Side
    offense_total: int
    defense_total: int
    offense_card_value: int
    defense_card_value: int
    was_deal: bool = False
    deal_successful: bool = False


@dataclass
class ShipCount:
    """Ships on a planet or in an encounter."""
    counts: Dict[str, int] = field(default_factory=dict)

    def get(self, player_name: str) -> int:
        return self.counts.get(player_name, 0)

    def set(self, player_name: str, count: int) -> None:
        if count <= 0:
            self.counts.pop(player_name, None)
        else:
            self.counts[player_name] = count

    def add(self, player_name: str, count: int) -> None:
        current = self.get(player_name)
        self.set(player_name, current + count)

    def remove(self, player_name: str, count: int) -> int:
        """Remove ships, returns actual number removed."""
        current = self.get(player_name)
        to_remove = min(current, count)
        self.set(player_name, current - to_remove)
        return to_remove

    def total(self) -> int:
        return sum(self.counts.values())

    def players_present(self) -> List[str]:
        return [name for name, count in self.counts.items() if count > 0]

    def copy(self) -> "ShipCount":
        return ShipCount(counts=dict(self.counts))

    def __contains__(self, player_name: str) -> bool:
        """Support 'in' operator: check if player has ships."""
        return self.get(player_name) > 0

    def __getitem__(self, player_name: str) -> int:
        """Support bracket notation: ships[player_name]."""
        return self.get(player_name)


class StationType(Enum):
    """Types of space stations (Cosmic Alliance expansion)."""
    # Defensive stations
    STATION_ALPHA = "alpha"      # +2 to defensive total
    STATION_DELTA = "delta"      # Counts as having a colony for alliance purposes

    # Offensive stations
    STATION_BETA = "beta"        # +2 to offensive total
    STATION_OMEGA = "omega"      # May use planet for launch even without ships

    # Resource stations
    STATION_GAMMA = "gamma"      # Return 1 extra ship from warp during regroup
    STATION_SIGMA = "sigma"      # Draw 1 extra card when winning encounter

    # Strategic stations
    STATION_THETA = "theta"      # Commit up to 5 ships instead of 4
    STATION_KAPPA = "kappa"      # May invite 1 extra ally


@dataclass
class SpaceStation:
    """
    A space station placed on a planet (Cosmic Alliance expansion).
    Stations provide benefits even without ships present.
    """
    owner: str  # Player name
    station_type: StationType
    planet_id: int  # Which planet it's on
    active: bool = True  # Can be disabled by certain effects

    def get_defense_bonus(self) -> int:
        """Get defensive combat bonus from this station."""
        if self.active and self.station_type == StationType.STATION_ALPHA:
            return 2
        return 0

    def get_offense_bonus(self) -> int:
        """Get offensive combat bonus from this station."""
        if self.active and self.station_type == StationType.STATION_BETA:
            return 2
        return 0

    def get_warp_retrieval_bonus(self) -> int:
        """Get bonus ships retrieved from warp during regroup."""
        if self.active and self.station_type == StationType.STATION_GAMMA:
            return 1
        return 0

    def get_max_ships_bonus(self) -> int:
        """Get bonus to max ships that can be committed."""
        if self.active and self.station_type == StationType.STATION_THETA:
            return 1
        return 0

    def get_ally_invite_bonus(self) -> int:
        """Get bonus to number of allies that can be invited."""
        if self.active and self.station_type == StationType.STATION_KAPPA:
            return 1
        return 0

    def provides_colony_presence(self) -> bool:
        """Whether this station counts as a colony presence."""
        return self.active and self.station_type == StationType.STATION_DELTA

    def allows_empty_launch(self) -> bool:
        """Whether this station allows launching from planet with no ships."""
        return self.active and self.station_type == StationType.STATION_OMEGA

    def grants_card_on_win(self) -> bool:
        """Whether this station grants an extra card when winning."""
        return self.active and self.station_type == StationType.STATION_SIGMA


@dataclass
class GameConfig:
    """Configuration options for a game."""
    num_players: int = 5
    colonies_to_win: int = 5
    starting_ships_per_planet: int = 4
    starting_planets: int = 5
    starting_hand_size: int = 8
    max_ships_per_encounter: int = 4
    allow_shared_victory: bool = True
    use_flares: bool = False
    use_tech: bool = False
    use_hazards: bool = False
    use_space_stations: bool = False  # Cosmic Storm expansion
    use_lux: bool = False  # Cosmic Odyssey expansion (currency system)
    use_rifts: bool = False  # Cosmic Odyssey expansion (trap cards)
    starting_lux: int = 5  # Lux each player starts with
    max_turns: int = 200  # Prevent infinite games
    seed: Optional[int] = None  # For reproducibility
    required_aliens: Optional[List[str]] = None  # Aliens that must be in the game

    # Expansion selection (None = random selection per game)
    expansions: Optional[List[Expansion]] = None  # Specific expansions to use
    random_expansions: bool = True  # Randomly select expansions per game
    min_expansions: int = 0  # Minimum number of expansions (besides base)
    max_expansions: int = 3  # Maximum number of expansions (besides base)
    include_homebrew: bool = True  # Include homebrew aliens in random selection

    # 2-player variant settings
    two_player_mode: bool = False  # Enables 2-player variant rules
    dual_powers: bool = False  # Each player gets 2 alien powers (for 2P variant)
    two_player_colonies_to_win: int = 4  # Reduced colonies needed in 2P
    two_player_alternate_turns: bool = True  # Players take turns as offense
    two_player_choose_target: bool = True  # Offense can choose target (no destiny)


@dataclass
class SimulationConfig:
    """Configuration for running simulations."""
    num_games: int = 1000
    game_config: GameConfig = field(default_factory=GameConfig)
    powers_to_test: Optional[List[str]] = None  # None = all powers
    show_progress: bool = True
    progress_interval: int = 100
    catch_errors: bool = True
    log_errors: bool = True
