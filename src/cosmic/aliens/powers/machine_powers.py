"""
Machine Powers - Mechanical and technological aliens.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Automaton(AlienPower):
    """Automaton - Mechanical precision. +2 to attack cards."""
    name: str = field(default="Automaton", init=False)
    description: str = field(default="+2 to attack cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 2
        return total


@dataclass
class Clockwork(AlienPower):
    """Clockwork - Precise timing. Gain extra encounter each turn."""
    name: str = field(default="Clockwork", init=False)
    description: str = field(default="Extra encounter each turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cyborg(AlienPower):
    """Cyborg - Hybrid strength. +1 per ship in encounter."""
    name: str = field(default="Cyborg", init=False)
    description: str = field(default="+1 per ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if side == Side.OFFENSE:
            ships = sum(game.offense_ships.values())
        else:
            ships = sum(game.defense_ships.values())
        return total + ships


@dataclass
class Android(AlienPower):
    """Android - Perfect copy. Copy opponent's revealed attack card value."""
    name: str = field(default="Android", init=False)
    description: str = field(default="Copy opponent's attack value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Robot(AlienPower):
    """Robot - Efficient worker. Draw extra card when gaining colony."""
    name: str = field(default="Robot", init=False)
    description: str = field(default="Draw card when colonizing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Processor(AlienPower):
    """Processor - Calculate outcomes. Look at top 3 deck cards, reorder."""
    name: str = field(default="Processor", init=False)
    description: str = field(default="View and reorder top 3 deck cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mainframe(AlienPower):
    """Mainframe - Central control. View all other players' hands."""
    name: str = field(default="Mainframe", init=False)
    description: str = field(default="See all other players' hands.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Server(AlienPower):
    """Server - Data storage. Keep discarded encounter cards."""
    name: str = field(default="Server", init=False)
    description: str = field(default="Keep discarded encounter cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Database(AlienPower):
    """Database - Information storage. Draw 2 cards when getting new hand."""
    name: str = field(default="Database", init=False)
    description: str = field(default="Draw 2 extra when getting new hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Terminal(AlienPower):
    """Terminal - Interface access. Take random card from opponent after winning."""
    name: str = field(default="Terminal", init=False)
    description: str = field(default="Take random card from loser.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Scanner(AlienPower):
    """Scanner - Detection systems. See opponent's encounter card before selecting yours."""
    name: str = field(default="Scanner", init=False)
    description: str = field(default="See opponent's card before selecting.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sensor(AlienPower):
    """Sensor - Advanced detection. Know opponent's ally count before alliances."""
    name: str = field(default="Sensor", init=False)
    description: str = field(default="Know ally intentions in advance.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Network(AlienPower):
    """Network - Connected systems. Allied ships count double."""
    name: str = field(default="Network", init=False)
    description: str = field(default="Allied ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Interface(AlienPower):
    """Interface - Connection bridge. Trade cards freely with allies."""
    name: str = field(default="Interface", init=False)
    description: str = field(default="Trade cards with allies freely.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Generator(AlienPower):
    """Generator - Power source. +3 when defending home system."""
    name: str = field(default="Generator", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        if side == Side.DEFENSE and game.defense == player:
            if game.defense_planet and game.defense_planet.is_home_planet:
                return total + 3
        return total


# Register all powers
AlienRegistry.register(Automaton())
AlienRegistry.register(Clockwork())
AlienRegistry.register(Cyborg())
AlienRegistry.register(Android())
AlienRegistry.register(Robot())
AlienRegistry.register(Processor())
AlienRegistry.register(Mainframe())
AlienRegistry.register(Server())
AlienRegistry.register(Database())
AlienRegistry.register(Terminal())
AlienRegistry.register(Scanner())
AlienRegistry.register(Sensor())
AlienRegistry.register(Network())
AlienRegistry.register(Interface())
AlienRegistry.register(Generator())
