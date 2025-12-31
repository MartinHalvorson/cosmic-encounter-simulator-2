"""
Warfare themed alien powers for Cosmic Encounter.

Powers themed around military tactics, siege warfare, and battlefield strategies.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ============================================================================
# SIEGE WARFARE
# ============================================================================

@dataclass
class Besieger(AlienPower):
    """Besieger - Power of the Siege. +2 per turn same target."""
    name: str = field(default="Besieger", init=False)
    description: str = field(default="+2 per consecutive attack on same target.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    siege_count: int = 0
    last_target: str = ""

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            target = game.defense.name if game.defense else ""
            if target == self.last_target:
                self.siege_count += 1
            else:
                self.siege_count = 0
                self.last_target = target
            return base_total + (self.siege_count * 2)
        return base_total


@dataclass
class Breacher(AlienPower):
    """Breacher - Power of Breaking. Destroy defenses first."""
    name: str = field(default="Breacher", init=False)
    description: str = field(default="Opponent loses 1 ship before combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Catapult(AlienPower):
    """Catapult - Power of Range. Strike from afar."""
    name: str = field(default="Catapult", init=False)
    description: str = field(default="Your ships cannot be lost in first round.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Rampart(AlienPower):
    """Rampart - Power of the Wall. Defense bonus at home."""
    name: str = field(default="Rampart", init=False)
    description: str = field(default="+4 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.target_planet and game.target_planet.owner == player:
                return base_total + 4
        return base_total


# ============================================================================
# TACTICAL WARFARE
# ============================================================================

@dataclass
class Flanker(AlienPower):
    """Flanker - Power of the Side Attack. Bonus vs larger forces."""
    name: str = field(default="Flanker", init=False)
    description: str = field(default="+3 if opponent has more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            my_ships = sum(game.offense_ships.values())
            opp_ships = sum(game.defense_ships.values())
        else:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
        if opp_ships > my_ships:
            return base_total + 3
        return base_total


@dataclass
class Ambusher(AlienPower):
    """Ambusher - Power of Surprise. First attack bonus."""
    name: str = field(default="Ambusher", init=False)
    description: str = field(default="+5 on first encounter vs each player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    ambushed: set = field(default_factory=set)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and opponent.name not in self.ambushed:
            self.ambushed.add(opponent.name)
            return base_total + 5
        return base_total


@dataclass
class Cavalry(AlienPower):
    """Cavalry - Power of the Charge. Bonus when attacking."""
    name: str = field(default="Cavalry", init=False)
    description: str = field(default="+1 per ship attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
            return base_total + ships
        return base_total


@dataclass
class Phalanx(AlienPower):
    """Phalanx - Power of Formation. Ships work together."""
    name: str = field(default="Phalanx", init=False)
    description: str = field(default="Ships count as +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        return base_total + ships  # Extra +1 per ship (on top of normal +1)


# ============================================================================
# MILITARY UNITS
# ============================================================================

@dataclass
class Infantry(AlienPower):
    """Infantry - Power of Numbers. More ships = more power."""
    name: str = field(default="Infantry", init=False)
    description: str = field(default="+3 with 4+ ships in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)
        if ships >= 4:
            return base_total + 3
        return base_total


@dataclass
class Artillery(AlienPower):
    """Artillery - Power of Bombardment. High damage from distance."""
    name: str = field(default="Artillery", init=False)
    description: str = field(default="Card value doubled, but -2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Scout(AlienPower):
    """Scout - Power of Reconnaissance. See opponent's card."""
    name: str = field(default="Scout", init=False)
    description: str = field(default="See opponent's card before playing yours.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Medic(AlienPower):
    """Medic - Power of Healing. Recover lost ships."""
    name: str = field(default="Medic", init=False)
    description: str = field(default="Retrieve 1 ship from warp after each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.END_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Engineer(AlienPower):
    """Engineer - Power of Construction. Build advantages."""
    name: str = field(default="Engineer", init=False)
    description: str = field(default="Defending with 4+ ships: +4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            ships = game.defense_ships.get(player.name, 0)
            if ships >= 4:
                return base_total + 4
        return base_total


# ============================================================================
# SPECIAL FORCES
# ============================================================================

@dataclass
class Commando(AlienPower):
    """Commando - Power of Precision. Bypass defenses."""
    name: str = field(default="Commando", init=False)
    description: str = field(default="Ignore 2 defense ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sniper(AlienPower):
    """Sniper - Power of Precision. Target specific threats."""
    name: str = field(default="Sniper", init=False)
    description: str = field(default="Choose 1 enemy ship to remove from encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Saboteur(AlienPower):
    """Saboteur - Power of Disruption. Weaken opponent."""
    name: str = field(default="Saboteur", init=False)
    description: str = field(default="Opponent's card value -4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Guerrilla(AlienPower):
    """Guerrilla - Power of Resistance. Stronger when outnumbered."""
    name: str = field(default="Guerrilla", init=False)
    description: str = field(default="+4 when defending with fewer ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.DEFENSE:
            my_ships = sum(game.defense_ships.values())
            opp_ships = sum(game.offense_ships.values())
            if my_ships < opp_ships:
                return base_total + 4
        return base_total


# ============================================================================
# STRATEGIC ROLES
# ============================================================================

@dataclass
class General(AlienPower):
    """General - Power of Command. +1 per ally."""
    name: str = field(default="General", init=False)
    description: str = field(default="+2 per ally on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        if side == Side.OFFENSE:
            allies = len([p for p in game.offense_ships if p != player.name])
        else:
            allies = len([p for p in game.defense_ships if p != player.name])
        return base_total + (allies * 2)


@dataclass
class Admiral(AlienPower):
    """Admiral - Power of the Fleet. Command multiple ships."""
    name: str = field(default="Admiral", init=False)
    description: str = field(default="May commit 5 ships instead of 4.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Marshal(AlienPower):
    """Marshal - Power of Order. Allies commit more ships."""
    name: str = field(default="Marshal", init=False)
    description: str = field(default="Each ally may send +1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tactician(AlienPower):
    """Tactician - Power of Planning. See cards in advance."""
    name: str = field(default="Tactician", init=False)
    description: str = field(default="Look at top 3 destiny cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Strategist(AlienPower):
    """Strategist - Power of Long Game. Bonus in late game."""
    name: str = field(default="Strategist", init=False)
    description: str = field(default="+1 per turn number (max +10).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(10, game.current_turn)
            return base_total + bonus
        return base_total


# Register all warfare powers
WARFARE_POWERS = [
    Besieger, Breacher, Catapult, Rampart,
    Flanker, Ambusher, Cavalry, Phalanx,
    Infantry, Artillery, Scout, Medic, Engineer,
    Commando, Sniper, Saboteur, Guerrilla,
    General, Admiral, Marshal, Tactician, Strategist,
]


# Auto-register all powers
for power_class in WARFARE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
