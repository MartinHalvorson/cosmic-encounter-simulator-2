"""
Chess Powers for Cosmic Encounter.

Aliens inspired by chess pieces and strategies.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Pawn_Piece(AlienPower):
    """Pawn_Piece - Power of Advance. +3 on offense."""
    name: str = field(default="Pawn_Piece", init=False)
    description: str = field(default="+3 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 3
        return total


@dataclass
class Rook_Piece(AlienPower):
    """Rook_Piece - Power of Lines. +4 on defense."""
    name: str = field(default="Rook_Piece", init=False)
    description: str = field(default="+4 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 4
        return total


@dataclass
class Knight_Piece(AlienPower):
    """Knight_Piece - Power of Leap. Attack any planet, ignore destiny."""
    name: str = field(default="Knight_Piece", init=False)
    description: str = field(default="Attack any planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Bishop_Piece(AlienPower):
    """Bishop_Piece - Power of Diagonals. +2 and win ties."""
    name: str = field(default="Bishop_Piece", init=False)
    description: str = field(default="+2 and win ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Queen_Piece(AlienPower):
    """Queen_Piece - Power of Range. +3 always."""
    name: str = field(default="Queen_Piece", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class King_Piece(AlienPower):
    """King_Piece - Power of Importance. Cannot lose more than 2 ships."""
    name: str = field(default="King_Piece", init=False)
    description: str = field(default="Lose max 2 ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Checkmate(AlienPower):
    """Checkmate - Power of Victory. +5 at 4 colonies."""
    name: str = field(default="Checkmate", init=False)
    description: str = field(default="+5 at 4 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            if colonies >= 4:
                return total + 5
        return total


@dataclass
class Castling(AlienPower):
    """Castling - Power of Swap. Swap ships between colonies."""
    name: str = field(default="Castling", init=False)
    description: str = field(default="Swap ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class En_Passant(AlienPower):
    """En_Passant - Power of Capture. Take 1 card from defeated opponent."""
    name: str = field(default="En_Passant", init=False)
    description: str = field(default="Take card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Promotion(AlienPower):
    """Promotion - Power of Upgrade. +3 after first win."""
    name: str = field(default="Promotion", init=False)
    description: str = field(default="+3 after first win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fork(AlienPower):
    """Fork - Power of Dual Threat. +2 for each ally in encounter."""
    name: str = field(default="Fork", init=False)
    description: str = field(default="+2 per ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pin(AlienPower):
    """Pin - Power of Restriction. Opponent cannot invite allies."""
    name: str = field(default="Pin", init=False)
    description: str = field(default="Block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Stalemate(AlienPower):
    """Stalemate - Power of Draws. Force tie when losing."""
    name: str = field(default="Stalemate", init=False)
    description: str = field(default="Force tie when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gambit(AlienPower):
    """Gambit - Power of Sacrifice. Sacrifice ships for +2 each."""
    name: str = field(default="Gambit", init=False)
    description: str = field(default="Sacrifice ships for +2 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Tempo(AlienPower):
    """Tempo - Power of Speed. +1 per turn game has lasted."""
    name: str = field(default="Tempo", init=False)
    description: str = field(default="+1 per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + game.current_turn
        return total


# Register all chess powers
AlienRegistry.register(Pawn_Piece())
AlienRegistry.register(Rook_Piece())
AlienRegistry.register(Knight_Piece())
AlienRegistry.register(Bishop_Piece())
AlienRegistry.register(Queen_Piece())
AlienRegistry.register(King_Piece())
AlienRegistry.register(Checkmate())
AlienRegistry.register(Castling())
AlienRegistry.register(En_Passant())
AlienRegistry.register(Promotion())
AlienRegistry.register(Fork())
AlienRegistry.register(Pin())
AlienRegistry.register(Stalemate())
AlienRegistry.register(Gambit())
AlienRegistry.register(Tempo())
