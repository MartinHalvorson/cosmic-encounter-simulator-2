"""
Hazard Deck - Random events from Cosmic Conflict expansion.

Hazards are dangerous cosmic events that affect the game in unpredictable ways.
A hazard is drawn at the start of each encounter and affects that encounter.
"""

import random
from dataclasses import dataclass, field
from typing import List, Optional, Callable, Dict, Any, TYPE_CHECKING
from enum import Enum, auto

if TYPE_CHECKING:
    from ..game import Game
    from ..player import Player


class HazardTiming(Enum):
    """When the hazard takes effect."""
    START_ENCOUNTER = auto()  # Before destiny is drawn
    AFTER_DESTINY = auto()    # After defender is determined
    DURING_LAUNCH = auto()    # During ship commitment
    DURING_ALLIANCE = auto()  # During alliance phase
    DURING_REVEAL = auto()    # When cards are revealed
    DURING_RESOLUTION = auto()  # During combat resolution
    END_ENCOUNTER = auto()    # After encounter resolves


class HazardSeverity(Enum):
    """How dangerous the hazard is."""
    MILD = auto()      # Minor inconvenience
    MODERATE = auto()  # Significant effect
    SEVERE = auto()    # Major game impact
    EXTREME = auto()   # Game-changing event


@dataclass
class HazardCard:
    """
    A hazard card representing a cosmic event.
    """
    name: str
    description: str
    timing: HazardTiming
    severity: HazardSeverity
    affects_all: bool = False  # True if affects all players

    def __str__(self) -> str:
        return f"⚠️ {self.name}: {self.description}"


# Hazard definitions with their effects
HAZARD_EFFECTS: Dict[str, Dict[str, Any]] = {
    # Mild hazards
    "Cosmic Quake": {
        "description": "All ships in the warp return to their owners' colonies.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.MILD,
        "affects_all": True,
        "effect": "warp_release"
    },
    "Solar Flare": {
        "description": "All players draw 1 card.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.MILD,
        "affects_all": True,
        "effect": "everyone_draws"
    },
    "Meteor Shower": {
        "description": "Each player loses 1 ship from their largest colony.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.MILD,
        "affects_all": True,
        "effect": "meteor_damage"
    },
    "Communications Blackout": {
        "description": "No alliances this encounter.",
        "timing": HazardTiming.DURING_ALLIANCE,
        "severity": HazardSeverity.MILD,
        "affects_all": True,
        "effect": "no_alliances"
    },
    "Sensor Ghost": {
        "description": "Destiny must be redrawn.",
        "timing": HazardTiming.AFTER_DESTINY,
        "severity": HazardSeverity.MILD,
        "affects_all": False,
        "effect": "redraw_destiny"
    },

    # Moderate hazards
    "Warp Rift": {
        "description": "Ships lost this encounter are removed from game instead of going to warp.",
        "timing": HazardTiming.DURING_RESOLUTION,
        "severity": HazardSeverity.MODERATE,
        "affects_all": True,
        "effect": "permanent_loss"
    },
    "Temporal Anomaly": {
        "description": "Cards played are returned to hand; neither side reveals.",
        "timing": HazardTiming.DURING_REVEAL,
        "severity": HazardSeverity.MODERATE,
        "affects_all": True,
        "effect": "cards_return"
    },
    "Gravity Storm": {
        "description": "Each player must commit maximum ships or none.",
        "timing": HazardTiming.DURING_LAUNCH,
        "severity": HazardSeverity.MODERATE,
        "affects_all": True,
        "effect": "max_or_none"
    },
    "Power Surge": {
        "description": "All alien powers are enhanced - use twice this encounter.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.MODERATE,
        "affects_all": True,
        "effect": "double_powers"
    },
    "Nebula Cloud": {
        "description": "Attack card values are halved (round up).",
        "timing": HazardTiming.DURING_REVEAL,
        "severity": HazardSeverity.MODERATE,
        "affects_all": True,
        "effect": "halve_attacks"
    },

    # Severe hazards
    "Supernova": {
        "description": "Defender loses 1 home planet permanently if they lose.",
        "timing": HazardTiming.DURING_RESOLUTION,
        "severity": HazardSeverity.SEVERE,
        "affects_all": False,
        "effect": "destroy_planet"
    },
    "Dimensional Rift": {
        "description": "Winner and loser are swapped.",
        "timing": HazardTiming.DURING_RESOLUTION,
        "severity": HazardSeverity.SEVERE,
        "affects_all": True,
        "effect": "swap_outcome"
    },
    "Plague Ship": {
        "description": "Winner sends 2 ships to warp after landing.",
        "timing": HazardTiming.END_ENCOUNTER,
        "severity": HazardSeverity.SEVERE,
        "affects_all": False,
        "effect": "plague_winner"
    },
    "Ion Storm": {
        "description": "All reinforcements and artifacts are cancelled.",
        "timing": HazardTiming.DURING_REVEAL,
        "severity": HazardSeverity.SEVERE,
        "affects_all": True,
        "effect": "cancel_extras"
    },
    "Black Hole": {
        "description": "All losing ships are removed from game permanently.",
        "timing": HazardTiming.DURING_RESOLUTION,
        "severity": HazardSeverity.SEVERE,
        "affects_all": True,
        "effect": "permanent_loss"
    },

    # Extreme hazards
    "Cosmic Storm": {
        "description": "All players lose half their hand (round down).",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.EXTREME,
        "affects_all": True,
        "effect": "lose_half_hand"
    },
    "Gamma Ray Burst": {
        "description": "Each player loses ships from all colonies down to 2 per planet.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.EXTREME,
        "affects_all": True,
        "effect": "mass_casualties"
    },
    "Power Nullifier": {
        "description": "All alien powers are disabled for this encounter.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.EXTREME,
        "affects_all": True,
        "effect": "disable_all_powers"
    },
    "Galaxy Quake": {
        "description": "All colonies with 1 ship are destroyed; ships to warp.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.EXTREME,
        "affects_all": True,
        "effect": "destroy_weak_colonies"
    },
    "Time Warp": {
        "description": "Skip this encounter entirely. Turn passes.",
        "timing": HazardTiming.START_ENCOUNTER,
        "severity": HazardSeverity.EXTREME,
        "affects_all": True,
        "effect": "skip_encounter"
    }
}


@dataclass
class HazardDeck:
    """
    The hazard deck containing all hazard cards.
    Draw one at the start of each encounter when hazards are enabled.
    """
    draw_pile: List[HazardCard] = field(default_factory=list)
    discard_pile: List[HazardCard] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)
    enabled: bool = True

    # Track current hazard for the encounter
    current_hazard: Optional[HazardCard] = None

    def __post_init__(self):
        if not self.draw_pile:
            self._initialize_deck()
            self.shuffle()

    def _initialize_deck(self) -> None:
        """Create all hazard cards from definitions."""
        for name, data in HAZARD_EFFECTS.items():
            hazard = HazardCard(
                name=name,
                description=data["description"],
                timing=data["timing"],
                severity=data["severity"],
                affects_all=data.get("affects_all", False)
            )
            self.draw_pile.append(hazard)

    def shuffle(self) -> None:
        """Shuffle the hazard deck."""
        self._rng.shuffle(self.draw_pile)

    def draw(self) -> Optional[HazardCard]:
        """Draw a hazard card for this encounter."""
        if not self.enabled:
            return None

        if not self.draw_pile:
            self._reshuffle_discard()

        if not self.draw_pile:
            return None

        self.current_hazard = self.draw_pile.pop()
        return self.current_hazard

    def discard(self, hazard: Optional[HazardCard] = None) -> None:
        """Discard a hazard card."""
        card = hazard or self.current_hazard
        if card:
            self.discard_pile.append(card)
            if card == self.current_hazard:
                self.current_hazard = None

    def _reshuffle_discard(self) -> None:
        """Shuffle discard pile back into draw pile."""
        if not self.discard_pile:
            return
        self.draw_pile = self.discard_pile
        self.discard_pile = []
        self.shuffle()

    def get_effect(self, hazard: HazardCard) -> Dict[str, Any]:
        """Get the effect data for a hazard."""
        return HAZARD_EFFECTS.get(hazard.name, {})

    def cards_remaining(self) -> int:
        """Number of hazards remaining in deck."""
        return len(self.draw_pile)

    def set_rng(self, rng: random.Random) -> None:
        """Set random number generator for reproducibility."""
        self._rng = rng

    def enable(self) -> None:
        """Enable hazard system."""
        self.enabled = True

    def disable(self) -> None:
        """Disable hazard system."""
        self.enabled = False
        self.current_hazard = None


def apply_hazard_effect(game: "Game", hazard: HazardCard) -> bool:
    """
    Apply a hazard's effect to the game.

    Returns True if the hazard was successfully applied.
    """
    effect_data = HAZARD_EFFECTS.get(hazard.name, {})
    effect_type = effect_data.get("effect", "")

    if effect_type == "warp_release":
        # All ships return from warp
        for player in game.players:
            ships = player.ships_in_warp
            if ships > 0:
                player.retrieve_ships_from_warp(ships)
                player.return_ships_to_colonies(ships, player.home_planets)
        return True

    elif effect_type == "everyone_draws":
        # All players draw 1 card
        for player in game.players:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)
        return True

    elif effect_type == "meteor_damage":
        # Each player loses 1 ship from largest colony
        for player in game.players:
            colonies = [p for p in game.planets if p.has_colony(player.name)]
            if colonies:
                largest = max(colonies, key=lambda p: p.get_ships(player.name))
                ships = largest.get_ships(player.name)
                if ships > 0:
                    largest.remove_ships(player.name, 1)
                    player.send_ships_to_warp(1)
        return True

    elif effect_type == "no_alliances":
        # Will be checked during alliance phase
        return True

    elif effect_type == "redraw_destiny":
        # Destiny will be redrawn
        return True

    elif effect_type == "permanent_loss":
        # Ships removed instead of going to warp - tracked in resolution
        return True

    elif effect_type == "halve_attacks":
        # Attack values halved - applied during reveal
        return True

    elif effect_type == "swap_outcome":
        # Winner/loser swapped - applied during resolution
        return True

    elif effect_type == "disable_all_powers":
        # All powers zapped this encounter
        for player in game.players:
            if player not in game.zapped_powers:
                game.zapped_powers.append(player)
        return True

    elif effect_type == "lose_half_hand":
        # All players discard half their hand
        for player in game.players:
            count = len(player.hand) // 2
            for _ in range(count):
                if player.hand:
                    card = game._rng.choice(player.hand)
                    player.remove_card(card)
                    game.cosmic_deck.discard(card)
        return True

    elif effect_type == "mass_casualties":
        # Reduce all colonies to 2 ships max
        for planet in game.planets:
            for player in game.players:
                ships = planet.get_ships(player.name)
                if ships > 2:
                    excess = ships - 2
                    planet.remove_ships(player.name, excess)
                    player.send_ships_to_warp(excess)
        return True

    elif effect_type == "destroy_weak_colonies":
        # Remove colonies with only 1 ship
        for planet in game.planets:
            for player in game.players:
                ships = planet.get_ships(player.name)
                if ships == 1:
                    planet.remove_ships(player.name, 1)
                    player.send_ships_to_warp(1)
        return True

    elif effect_type == "skip_encounter":
        # Encounter is skipped entirely
        return True

    return False
