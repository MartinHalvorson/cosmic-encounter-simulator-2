"""
Extended Emotion Powers for Cosmic Encounter.

Aliens inspired by emotional states and feelings.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# POSITIVE EMOTIONS
# ============================================================================

@dataclass
class Happiness(AlienPower):
    """Happiness - Power of Joy. +1 for each colony you have."""
    name: str = field(default="Happiness", init=False)
    description: str = field(default="+1 for each colony you have.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + colonies
        return base_total


@dataclass
class Excitement(AlienPower):
    """Excitement - Power of Energy. +3 on first encounter of turn."""
    name: str = field(default="Excitement", init=False)
    description: str = field(default="+3 on first encounter of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        encounter_count = getattr(game.logger, 'encounter_count', 0) if hasattr(game, 'logger') else 0
        if player.power_active and encounter_count == 1:
            return base_total + 3
        return base_total


@dataclass
class Gratitude(AlienPower):
    """Gratitude - Power of Thanks. Allies draw 1 card after helping."""
    name: str = field(default="Gratitude", init=False)
    description: str = field(default="Allies draw 1 card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Serenity(AlienPower):
    """Serenity - Power of Calm. Ignore negative effects."""
    name: str = field(default="Serenity", init=False)
    description: str = field(default="Ignore negative card effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Optimism(AlienPower):
    """Optimism - Power of Hope. +2 when losing by 5 or more."""
    name: str = field(default="Optimism", init=False)
    description: str = field(default="+2 when losing by 5 or more.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# NEGATIVE EMOTIONS
# ============================================================================

@dataclass
class Anger_Alt(AlienPower):
    """Anger - Power of Fury. +4 attack, -2 defense."""
    name: str = field(default="Anger_Alt", init=False)
    description: str = field(default="+4 attack, -2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 4
        return base_total - 2


@dataclass
class Sadness(AlienPower):
    """Sadness - Power of Tears. Draw card when ships go to warp."""
    name: str = field(default="Sadness", init=False)
    description: str = field(default="Draw 1 card when losing ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jealousy(AlienPower):
    """Jealousy - Power of Envy. Copy opponent's card value."""
    name: str = field(default="Jealousy", init=False)
    description: str = field(default="Use opponent's card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Disgust(AlienPower):
    """Disgust - Power of Rejection. Refuse to accept compensation."""
    name: str = field(default="Disgust", init=False)
    description: str = field(default="Draw from deck instead of compensation.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shame(AlienPower):
    """Shame - Power of Hiding. Ships can't be targeted by artifacts."""
    name: str = field(default="Shame", init=False)
    description: str = field(default="Ships immune to artifact effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# COMPLEX EMOTIONS
# ============================================================================

@dataclass
class Nostalgia(AlienPower):
    """Nostalgia - Power of Memory. Use cards from discard pile."""
    name: str = field(default="Nostalgia", init=False)
    description: str = field(default="Play cards from discard.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Anticipation(AlienPower):
    """Anticipation - Power of Foresight. See destiny card before drawn."""
    name: str = field(default="Anticipation", init=False)
    description: str = field(default="Preview destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Confusion(AlienPower):
    """Confusion - Power of Chaos. Randomize card effects."""
    name: str = field(default="Confusion", init=False)
    description: str = field(default="Randomize encounter outcomes.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Awe(AlienPower):
    """Awe - Power of Wonder. +5 when facing stronger opponent."""
    name: str = field(default="Awe", init=False)
    description: str = field(default="+5 when outmatched.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Boredom(AlienPower):
    """Boredom - Power of Disinterest. Skip encounters against same player."""
    name: str = field(default="Boredom", init=False)
    description: str = field(default="Skip repeat encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# SOCIAL EMOTIONS
# ============================================================================

@dataclass
class Compassion(AlienPower):
    """Compassion - Power of Empathy. Help losing players."""
    name: str = field(default="Compassion", init=False)
    description: str = field(default="Give cards to losing players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Loneliness(AlienPower):
    """Loneliness - Power of Isolation. +3 when no allies."""
    name: str = field(default="Loneliness", init=False)
    description: str = field(default="+3 when fighting alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        allies = len(game.offense_allies) if side == Side.OFFENSE else len(game.defense_allies)
        if allies == 0:
            return base_total + 3
        return base_total


@dataclass
class Belonging(AlienPower):
    """Belonging - Power of Unity. +1 for each ally."""
    name: str = field(default="Belonging", init=False)
    description: str = field(default="+1 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Guilt(AlienPower):
    """Guilt - Power of Remorse. Lose 1 ship on win."""
    name: str = field(default="Guilt", init=False)
    description: str = field(default="Lose 1 ship when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Relief(AlienPower):
    """Relief - Power of Release. Retrieve 2 ships from warp on win."""
    name: str = field(default="Relief", init=False)
    description: str = field(default="Retrieve 2 ships from warp on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        if player.power_active and player.ships_in_warp >= 2:
            player.retrieve_ships_from_warp(2)


# Register all aliens
for alien_class in [
    Happiness, Excitement, Gratitude, Serenity, Optimism,
    Anger_Alt, Sadness, Jealousy, Disgust, Shame,
    Nostalgia, Anticipation, Confusion, Awe, Boredom,
    Compassion, Loneliness, Belonging, Guilt, Relief,
]:
    AlienRegistry.register(alien_class())
