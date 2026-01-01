"""
Percussion Instrument Powers - Percussion themed aliens.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Drum_Kit_Percussion(AlienPower):
    """Drum_Kit_Percussion - Full rhythm."""
    name: str = field(default="Drum_Kit_Percussion", init=False)
    description: str = field(default="+5 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 5
        return total


@dataclass
class Snare_Drum_Percussion(AlienPower):
    """Snare_Drum_Percussion - Marching beat."""
    name: str = field(default="Snare_Drum_Percussion", init=False)
    description: str = field(default="+5 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Bass_Drum_Percussion(AlienPower):
    """Bass_Drum_Percussion - Deep thump."""
    name: str = field(default="Bass_Drum_Percussion", init=False)
    description: str = field(default="+6 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 6
        return total


@dataclass
class Cymbal_Percussion(AlienPower):
    """Cymbal_Percussion - Crashing accent."""
    name: str = field(default="Cymbal_Percussion", init=False)
    description: str = field(default="+2 plus random +0-4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2 + random.randint(0, 4)
        return total


@dataclass
class Xylophone_Percussion(AlienPower):
    """Xylophone_Percussion - Wooden melody."""
    name: str = field(default="Xylophone_Percussion", init=False)
    description: str = field(default="+1 per card (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, len(player.hand))
        return total


@dataclass
class Timpani_Percussion(AlienPower):
    """Timpani_Percussion - Orchestral thunder."""
    name: str = field(default="Timpani_Percussion", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Bongo_Percussion(AlienPower):
    """Bongo_Percussion - Hand drums."""
    name: str = field(default="Bongo_Percussion", init=False)
    description: str = field(default="+4 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count > 0:
            return total + 4
        return total


@dataclass
class Conga_Percussion(AlienPower):
    """Conga_Percussion - Latin beat."""
    name: str = field(default="Conga_Percussion", init=False)
    description: str = field(default="+4 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 4
        return total


@dataclass
class Maracas_Percussion(AlienPower):
    """Maracas_Percussion - Shaking rhythm."""
    name: str = field(default="Maracas_Percussion", init=False)
    description: str = field(default="+3 on even turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 0:
            return total + 3
        return total


@dataclass
class Tambourine_Percussion(AlienPower):
    """Tambourine_Percussion - Jingling beat."""
    name: str = field(default="Tambourine_Percussion", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Triangle_Percussion(AlienPower):
    """Triangle_Percussion - Bright ting."""
    name: str = field(default="Triangle_Percussion", init=False)
    description: str = field(default="+5 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 5
        return total


@dataclass
class Vibraphone_Percussion(AlienPower):
    """Vibraphone_Percussion - Metallic melody."""
    name: str = field(default="Vibraphone_Percussion", init=False)
    description: str = field(default="+5 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 5
        return total


@dataclass
class Glockenspiel_Percussion(AlienPower):
    """Glockenspiel_Percussion - Bell tones."""
    name: str = field(default="Glockenspiel_Percussion", init=False)
    description: str = field(default="+1 per turn (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(5, game.current_turn)
        return total


@dataclass
class Cowbell_Percussion(AlienPower):
    """Cowbell_Percussion - More cowbell."""
    name: str = field(default="Cowbell_Percussion", init=False)
    description: str = field(default="+5 with 3+ colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 3:
                return total + 5
        return total


@dataclass
class Djembe_Percussion(AlienPower):
    """Djembe_Percussion - African rhythm."""
    name: str = field(default="Djembe_Percussion", init=False)
    description: str = field(default="+2 per ally (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        return total + min(6, ally_count * 2)


PERCUSSION_INSTRUMENT_POWERS = [
    Drum_Kit_Percussion, Snare_Drum_Percussion, Bass_Drum_Percussion,
    Cymbal_Percussion, Xylophone_Percussion, Timpani_Percussion,
    Bongo_Percussion, Conga_Percussion, Maracas_Percussion, Tambourine_Percussion,
    Triangle_Percussion, Vibraphone_Percussion, Glockenspiel_Percussion,
    Cowbell_Percussion, Djembe_Percussion
]

for power_class in PERCUSSION_INSTRUMENT_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
