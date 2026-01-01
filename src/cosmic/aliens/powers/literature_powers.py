"""
Literature Powers for Cosmic Encounter.

Aliens inspired by writing and literary concepts.
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
# WRITERS
# ============================================================================

@dataclass
class Novelist(AlienPower):
    """Novelist - Power of Story. Build narrative advantage."""
    name: str = field(default="Novelist", init=False)
    description: str = field(default="+1 for each encounter this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Poet(AlienPower):
    """Poet - Power of Verse. Compact but powerful."""
    name: str = field(default="Poet", init=False)
    description: str = field(default="+5 when hand has 4 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 4:
            return base_total + 5
        return base_total


@dataclass
class Playwright(AlienPower):
    """Playwright - Power of Drama. Big encounters matter more."""
    name: str = field(default="Playwright", init=False)
    description: str = field(default="+3 when 4+ ships involved.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Journalist(AlienPower):
    """Journalist - Power of News. Know opponent's card."""
    name: str = field(default="Journalist", init=False)
    description: str = field(default="See opponent's chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Screenwriter(AlienPower):
    """Screenwriter - Power of Scenes. Control encounter flow."""
    name: str = field(default="Screenwriter", init=False)
    description: str = field(default="Reorder encounter phases.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# LITERARY GENRES
# ============================================================================

@dataclass
class Mystery(AlienPower):
    """Mystery - Power of Secrets. Hide card information."""
    name: str = field(default="Mystery", init=False)
    description: str = field(default="Card stays hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thriller(AlienPower):
    """Thriller - Power of Tension. Last-minute changes."""
    name: str = field(default="Thriller", init=False)
    description: str = field(default="Swap card at last moment.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Romance(AlienPower):
    """Romance - Power of Connection. Allies matter more."""
    name: str = field(default="Romance", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Horror(AlienPower):
    """Horror - Power of Fear. Opponent loses ships."""
    name: str = field(default="Horror", init=False)
    description: str = field(default="Opponent uses 1 less ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Comedy(AlienPower):
    """Comedy - Power of Laughter. Recover from losses."""
    name: str = field(default="Comedy", init=False)
    description: str = field(default="Retrieve 1 ship on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# LITERARY ELEMENTS
# ============================================================================

@dataclass
class Protagonist(AlienPower):
    """Protagonist - Power of the Hero. +3 when attacking."""
    name: str = field(default="Protagonist", init=False)
    description: str = field(default="+3 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Antagonist(AlienPower):
    """Antagonist - Power of Opposition. +3 when defending."""
    name: str = field(default="Antagonist", init=False)
    description: str = field(default="+3 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 3
        return base_total


@dataclass
class Narrator(AlienPower):
    """Narrator - Power of Voice. Control information flow."""
    name: str = field(default="Narrator", init=False)
    description: str = field(default="See all hidden cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Epilogue(AlienPower):
    """Epilogue - Power of Ending. Bonus on last encounter."""
    name: str = field(default="Epilogue", init=False)
    description: str = field(default="+5 on final encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Prologue(AlienPower):
    """Prologue - Power of Beginning. +5 on first encounter."""
    name: str = field(default="Prologue", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# STORYTELLING
# ============================================================================

@dataclass
class Fable(AlienPower):
    """Fable - Power of Morals. Win teaches lessons."""
    name: str = field(default="Fable", init=False)
    description: str = field(default="Opponent loses card on your win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Myth(AlienPower):
    """Myth - Power of Legend. Ships worth more."""
    name: str = field(default="Myth", init=False)
    description: str = field(default="Ships count as 1.5x.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Saga(AlienPower):
    """Saga - Power of Epic. Long game advantage."""
    name: str = field(default="Saga", init=False)
    description: str = field(default="+1 per turn that has passed.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fairytale(AlienPower):
    """Fairytale - Power of Magic. Unexpected outcomes."""
    name: str = field(default="Fairytale", init=False)
    description: str = field(default="Win ties automatically.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chronicle(AlienPower):
    """Chronicle - Power of History. Remember past encounters."""
    name: str = field(default="Chronicle", init=False)
    description: str = field(default="+1 for each previous win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all aliens
for alien_class in [
    Novelist, Poet, Playwright, Journalist, Screenwriter,
    Mystery, Thriller, Romance, Horror, Comedy,
    Protagonist, Antagonist, Narrator, Epilogue, Prologue,
    Fable, Myth, Saga, Fairytale, Chronicle,
]:
    AlienRegistry.register(alien_class())
