"""
Card system for Cosmic Encounter.
"""

from .base import Card, EncounterCard, AttackCard, NegotiateCard, MorphCard
from .base import ReinforcementCard, ArtifactCard, FlareCard, KickerCard
from .cosmic_deck import CosmicDeck
from .destiny_deck import DestinyDeck, DestinyCard
from .rewards_deck import RewardsDeck
from .flare_deck import FlareDeck, FLARE_EFFECTS
from .tech_deck import TechDeck, TechCard, TechCategory, PlayerTechState, TECH_EFFECTS
from .hazard_deck import HazardDeck, HazardCard, HazardTiming, HazardSeverity, HAZARD_EFFECTS, apply_hazard_effect
from .lux_system import LuxAction, LUX_COSTS, LuxToken, PlayerLuxState, LuxManager, LuxIncome
from .rift_cards import RiftCard, RiftType, RiftDeck, is_rift_card, handle_card_taken

__all__ = [
    "Card",
    "EncounterCard",
    "AttackCard",
    "NegotiateCard",
    "MorphCard",
    "ReinforcementCard",
    "ArtifactCard",
    "FlareCard",
    "KickerCard",
    "CosmicDeck",
    "DestinyDeck",
    "DestinyCard",
    "RewardsDeck",
    "FlareDeck",
    "FLARE_EFFECTS",
    "TechDeck",
    "TechCard",
    "TechCategory",
    "PlayerTechState",
    "TECH_EFFECTS",
    "HazardDeck",
    "HazardCard",
    "HazardTiming",
    "HazardSeverity",
    "HAZARD_EFFECTS",
    "apply_hazard_effect",
    # Lux system (Cosmic Odyssey)
    "LuxAction",
    "LUX_COSTS",
    "LuxToken",
    "PlayerLuxState",
    "LuxManager",
    "LuxIncome",
    # Rift cards (Cosmic Odyssey)
    "RiftCard",
    "RiftType",
    "RiftDeck",
    "is_rift_card",
    "handle_card_taken",
]
