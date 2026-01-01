"""
Martial Powers for Cosmic Encounter.

Aliens inspired by martial arts and combat disciplines.
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
# STRIKING ARTS
# ============================================================================

@dataclass
class Karate(AlienPower):
    """Karate - Power of Strikes. +3 on attack."""
    name: str = field(default="Karate", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 3
        return base_total


@dataclass
class Taekwondo(AlienPower):
    """Taekwondo - Power of Kicks. +4 attack, -1 defense."""
    name: str = field(default="Taekwondo", init=False)
    description: str = field(default="+4 attack, -1 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            return base_total + 4
        return base_total - 1


@dataclass
class Boxing(AlienPower):
    """Boxing - Power of Punches. +2 for each ship in encounter."""
    name: str = field(default="Boxing", init=False)
    description: str = field(default="+1 per 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Muay(AlienPower):
    """Muay - Power of Eight Limbs. +2 attack and defense."""
    name: str = field(default="Muay", init=False)
    description: str = field(default="+2 in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class Kickboxing(AlienPower):
    """Kickboxing - Power of Combinations. Win ties."""
    name: str = field(default="Kickboxing", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ============================================================================
# GRAPPLING ARTS
# ============================================================================

@dataclass
class Judo(AlienPower):
    """Judo - Power of Throws. Use opponent's strength."""
    name: str = field(default="Judo", init=False)
    description: str = field(default="+1 per opponent's ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Jujitsu(AlienPower):
    """Jujitsu - Power of Locks. Immobilize opponents."""
    name: str = field(default="Jujitsu", init=False)
    description: str = field(default="Opponent can't use reinforcements.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Wrestling_MA(AlienPower):
    """Wrestling - Power of Takedowns. Ships count double on defense."""
    name: str = field(default="Wrestling_MA", init=False)
    description: str = field(default="Ships count double defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_count * 2
        return base_count


@dataclass
class Sumo(AlienPower):
    """Sumo - Power of Mass. +5 defending home."""
    name: str = field(default="Sumo", init=False)
    description: str = field(default="+5 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE and game.defense_planet in player.home_planets:
            return base_total + 5
        return base_total


@dataclass
class Sambo(AlienPower):
    """Sambo - Power of Combat. +3 always."""
    name: str = field(default="Sambo", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


# ============================================================================
# TRADITIONAL ARTS
# ============================================================================

@dataclass
class Aikido(AlienPower):
    """Aikido - Power of Redirection. Swap card values."""
    name: str = field(default="Aikido", init=False)
    description: str = field(default="Swap attack values after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kendo(AlienPower):
    """Kendo - Power of the Sword. +4 attack."""
    name: str = field(default="Kendo", init=False)
    description: str = field(default="+4 attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class KungFu(AlienPower):
    """KungFu - Power of Skill. +1 per card in hand."""
    name: str = field(default="KungFu", init=False)
    description: str = field(default="+1 per 2 cards in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (len(player.hand) // 2)
        return base_total


@dataclass
class WingChun(AlienPower):
    """WingChun - Power of Centerline. Direct attacks."""
    name: str = field(default="WingChun", init=False)
    description: str = field(default="Ignore opponent's ship bonus.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class TaiChi(AlienPower):
    """TaiChi - Power of Flow. Draw card each turn."""
    name: str = field(default="TaiChi", init=False)
    description: str = field(default="Draw 1 card at start of turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


# ============================================================================
# WEAPON ARTS
# ============================================================================

@dataclass
class Ninjutsu(AlienPower):
    """Ninjutsu - Power of Stealth. Hide card until reveal."""
    name: str = field(default="Ninjutsu", init=False)
    description: str = field(default="Card hidden until resolution.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Iaido(AlienPower):
    """Iaido - Power of Quick Draw. First strike advantage."""
    name: str = field(default="Iaido", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Escrima(AlienPower):
    """Escrima - Power of Sticks. Dual wielding bonus."""
    name: str = field(default="Escrima", init=False)
    description: str = field(default="Play 2 cards, use highest.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Fencing_MA(AlienPower):
    """Fencing - Power of Precision. Win narrow victories."""
    name: str = field(default="Fencing_MA", init=False)
    description: str = field(default="Win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Archery(AlienPower):
    """Archery - Power of Range. Attack from distance."""
    name: str = field(default="Archery", init=False)
    description: str = field(default="+2 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + (home_colonies * 2)
        return base_total


# Register all aliens
for alien_class in [
    Karate, Taekwondo, Boxing, Muay, Kickboxing,
    Judo, Jujitsu, Wrestling_MA, Sumo, Sambo,
    Aikido, Kendo, KungFu, WingChun, TaiChi,
    Ninjutsu, Iaido, Escrima, Fencing_MA, Archery,
]:
    AlienRegistry.register(alien_class())
