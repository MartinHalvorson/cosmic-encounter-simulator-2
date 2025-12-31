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
    max_turns: int = 200  # Prevent infinite games
    seed: Optional[int] = None  # For reproducibility
    required_aliens: Optional[List[str]] = None  # Aliens that must be in the game

    # 2-player variant settings
    two_player_mode: bool = False  # Enables 2-player variant rules
    dual_powers: bool = False  # Each player gets 2 alien powers (for 2P variant)


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
