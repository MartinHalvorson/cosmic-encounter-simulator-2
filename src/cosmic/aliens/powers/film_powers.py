"""
Film Powers for Cosmic Encounter.

Aliens inspired by cinema and movie concepts.
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
# FILM CREW
# ============================================================================

@dataclass
class Producer(AlienPower):
    """Producer - Power of Resources. Extra cards each turn."""
    name: str = field(default="Producer", init=False)
    description: str = field(default="Draw 1 extra card per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Cinematographer(AlienPower):
    """Cinematographer - Power of Vision. See opponent's cards."""
    name: str = field(default="Cinematographer", init=False)
    description: str = field(default="View opponent's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Editor(AlienPower):
    """Editor - Power of Cutting. Remove cards from play."""
    name: str = field(default="Editor", init=False)
    description: str = field(default="Discard opponent's reinforcement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stuntman(AlienPower):
    """Stuntman - Power of Risk. High stakes plays."""
    name: str = field(default="Stuntman", init=False)
    description: str = field(default="+6 but lose extra ship on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Composer_Film(AlienPower):
    """Composer - Power of Score. Set the mood."""
    name: str = field(default="Composer_Film", init=False)
    description: str = field(default="+2 for each ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# FILM GENRES
# ============================================================================

@dataclass
class ActionFilm(AlienPower):
    """ActionFilm - Power of Explosion. +4 on attack."""
    name: str = field(default="ActionFilm", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Documentary(AlienPower):
    """Documentary - Power of Truth. All cards revealed."""
    name: str = field(default="Documentary", init=False)
    description: str = field(default="All hidden cards shown.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Animation(AlienPower):
    """Animation - Power of Creation. Ships can be created."""
    name: str = field(default="Animation", init=False)
    description: str = field(default="Add 1 virtual ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count + 1
        return base_count


@dataclass
class SciFiFilm(AlienPower):
    """SciFiFilm - Power of Future. See destiny before draw."""
    name: str = field(default="SciFiFilm", init=False)
    description: str = field(default="Preview destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Western(AlienPower):
    """Western - Power of Showdown. Win ties."""
    name: str = field(default="Western", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# FILM TECHNIQUES
# ============================================================================

@dataclass
class Montage(AlienPower):
    """Montage - Power of Sequence. Chain encounters."""
    name: str = field(default="Montage", init=False)
    description: str = field(default="+1 for each encounter this turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Flashback(AlienPower):
    """Flashback - Power of Past. Use cards from discard."""
    name: str = field(default="Flashback", init=False)
    description: str = field(default="Play from discard pile.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class CloseUp(AlienPower):
    """CloseUp - Power of Focus. See one card in detail."""
    name: str = field(default="CloseUp", init=False)
    description: str = field(default="See opponent's chosen card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class SlowMotion(AlienPower):
    """SlowMotion - Power of Delay. Extend encounter phases."""
    name: str = field(default="SlowMotion", init=False)
    description: str = field(default="Change card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class TimeLapse(AlienPower):
    """TimeLapse - Power of Speed. Quick encounters."""
    name: str = field(default="TimeLapse", init=False)
    description: str = field(default="Skip alliance phase.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ============================================================================
# FILM ELEMENTS
# ============================================================================

@dataclass
class Sequel(AlienPower):
    """Sequel - Power of Continuation. +2 if won last encounter."""
    name: str = field(default="Sequel", init=False)
    description: str = field(default="+2 after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Prequel(AlienPower):
    """Prequel - Power of Origin. +3 on first encounter."""
    name: str = field(default="Prequel", init=False)
    description: str = field(default="+3 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Remake(AlienPower):
    """Remake - Power of Redo. Replay last encounter."""
    name: str = field(default="Remake", init=False)
    description: str = field(default="Redo encounter once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Blockbuster(AlienPower):
    """Blockbuster - Power of Scale. Big ships, big wins."""
    name: str = field(default="Blockbuster", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count * 2
        return base_count


@dataclass
class Indie(AlienPower):
    """Indie - Power of Independence. +5 with no allies."""
    name: str = field(default="Indie", init=False)
    description: str = field(default="+5 when no allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        allies = len(game.offense_allies) if side == Side.OFFENSE else len(game.defense_allies)
        if allies == 0:
            return base_total + 5
        return base_total


# Register all aliens
for alien_class in [
    Producer, Cinematographer, Editor, Stuntman, Composer_Film,
    ActionFilm, Documentary, Animation, SciFiFilm, Western,
    Montage, Flashback, CloseUp, SlowMotion, TimeLapse,
    Sequel, Prequel, Remake, Blockbuster, Indie,
]:
    AlienRegistry.register(alien_class())
