"""
Extended Mythology Powers for Cosmic Encounter.

Aliens inspired by mythological figures from various cultures.
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
# GREEK MYTHOLOGY
# ============================================================================

@dataclass
class Zeus_Power(AlienPower):
    """Zeus - Power of Thunder. +5 when attacking with 4 ships."""
    name: str = field(default="Zeus_Power", init=False)
    description: str = field(default="+5 when attacking with 4 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active or side != Side.OFFENSE:
            return base_total
        ships = sum(game.offense_ships.values())
        if ships >= 4:
            return base_total + 5
        return base_total


@dataclass
class Hera(AlienPower):
    """Hera - Power of Marriage. +2 for each allied player."""
    name: str = field(default="Hera", init=False)
    description: str = field(default="+2 for each allied player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        allies = len(game.offense_allies) if side == Side.OFFENSE else len(game.defense_allies)
        return base_total + (allies * 2)


@dataclass
class Poseidon_Power(AlienPower):
    """Poseidon - Power of the Sea. Ships can't go to warp when defending home."""
    name: str = field(default="Poseidon_Power", init=False)
    description: str = field(default="Ships protected when defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_ships_to_warp(self, game: "Game", player: "Player", count: int, source: str) -> int:
        if not player.power_active:
            return count
        if game.defense == player and game.defense_planet in player.home_planets:
            return 0
        return count


@dataclass
class Athena_Power(AlienPower):
    """Athena - Power of Wisdom. See opponent's card before playing yours."""
    name: str = field(default="Athena_Power", init=False)
    description: str = field(default="See opponent's card before choosing yours.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ares_Power(AlienPower):
    """Ares - Power of War. +3 to attack, -2 to defense."""
    name: str = field(default="Ares_Power", init=False)
    description: str = field(default="+3 attack, -2 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 3
        return base_total - 2


@dataclass
class Aphrodite(AlienPower):
    """Aphrodite - Power of Love. Can force any player to ally with you."""
    name: str = field(default="Aphrodite", init=False)
    description: str = field(default="Force one player to ally with you.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hermes_Power(AlienPower):
    """Hermes - Power of Speed. Take an extra encounter if you win quickly."""
    name: str = field(default="Hermes_Power", init=False)
    description: str = field(default="Extra encounter on quick wins.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Apollo_Power(AlienPower):
    """Apollo - Power of Light. See destiny before it's drawn."""
    name: str = field(default="Apollo_Power", init=False)
    description: str = field(default="Preview destiny before drawing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hades_Power(AlienPower):
    """Hades - Power of the Underworld. Retrieve ships from warp each turn."""
    name: str = field(default="Hades_Power", init=False)
    description: str = field(default="Retrieve 2 ships from warp each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role) -> None:
        if player.power_active:
            ships = min(2, player.ships_in_warp)
            if ships > 0:
                player.retrieve_ships_from_warp(ships)


# ============================================================================
# NORSE MYTHOLOGY
# ============================================================================

@dataclass
class Odin_Power(AlienPower):
    """Odin - Power of Wisdom. Draw 2 cards at start of each encounter."""
    name: str = field(default="Odin_Power", init=False)
    description: str = field(default="Draw 2 cards each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Thor_Power(AlienPower):
    """Thor - Power of Thunder. +4 when attacking."""
    name: str = field(default="Thor_Power", init=False)
    description: str = field(default="+4 to attack total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Loki_Power(AlienPower):
    """Loki - Power of Mischief. Swap your card with opponent after reveal."""
    name: str = field(default="Loki_Power", init=False)
    description: str = field(default="Swap cards with opponent after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Freya(AlienPower):
    """Freya - Power of Beauty. Allies contribute double ships."""
    name: str = field(default="Freya", init=False)
    description: str = field(default="Allied ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fenrir(AlienPower):
    """Fenrir - Power of the Wolf. +1 for each ship in warp."""
    name: str = field(default="Fenrir", init=False)
    description: str = field(default="+1 for each ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + player.ships_in_warp
        return base_total


@dataclass
class Valkyrie(AlienPower):
    """Valkyrie - Power of Selection. Choose which ships go to warp."""
    name: str = field(default="Valkyrie", init=False)
    description: str = field(default="Choose which ships go to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# EGYPTIAN MYTHOLOGY
# ============================================================================

@dataclass
class Ra_Power(AlienPower):
    """Ra - Power of the Sun. +3 on your turn, -1 on others' turns."""
    name: str = field(default="Ra_Power", init=False)
    description: str = field(default="+3 on your turn, -1 otherwise.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if game.offense == player:
            return base_total + 3
        return base_total - 1


@dataclass
class Anubis_Power(AlienPower):
    """Anubis - Power of Death. Ships in warp count as +1 each."""
    name: str = field(default="Anubis_Power", init=False)
    description: str = field(default="Warp ships add +1 each to total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Isis_Power(AlienPower):
    """Isis - Power of Magic. Copy any active alien power for this encounter."""
    name: str = field(default="Isis_Power", init=False)
    description: str = field(default="Copy another alien's power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Osiris_Power(AlienPower):
    """Osiris - Power of Rebirth. Ships return from warp instead of going."""
    name: str = field(default="Osiris_Power", init=False)
    description: str = field(default="Ships return from warp on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Set_Power(AlienPower):
    """Set - Power of Chaos. Reverse the outcome of the encounter."""
    name: str = field(default="Set_Power", init=False)
    description: str = field(default="Reverse encounter outcome once per game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all aliens
for alien_class in [
    Zeus_Power, Hera, Poseidon_Power, Athena_Power, Ares_Power,
    Aphrodite, Hermes_Power, Apollo_Power, Hades_Power,
    Odin_Power, Thor_Power, Loki_Power, Freya, Fenrir, Valkyrie,
    Ra_Power, Anubis_Power, Isis_Power, Osiris_Power, Set_Power,
]:
    AlienRegistry.register(alien_class())
