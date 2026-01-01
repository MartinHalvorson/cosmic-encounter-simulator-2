"""
Milestone 3000 Powers for Cosmic Encounter.

Special aliens to commemorate reaching 3000 alien powers!
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
class Achiever(AlienPower):
    """Achiever - Power of Milestones."""
    name: str = field(default="Achiever", init=False)
    description: str = field(default="+1 per foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return base_total + colonies
        return base_total


@dataclass
class Completionist(AlienPower):
    """Completionist - Power of Perfection."""
    name: str = field(default="Completionist", init=False)
    description: str = field(default="Win all ties.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Perfecter(AlienPower):
    """Perfecter - Power of Excellence."""
    name: str = field(default="Perfecter", init=False)
    description: str = field(default="+3 in all encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Collector_M(AlienPower):
    """Collector - Power of Gathering."""
    name: str = field(default="Collector_M", init=False)
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
class Curator(AlienPower):
    """Curator - Power of Selection."""
    name: str = field(default="Curator", init=False)
    description: str = field(default="See top 3 cards of deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Historian(AlienPower):
    """Historian - Power of Memory."""
    name: str = field(default="Historian", init=False)
    description: str = field(default="+1 per turn this game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + min(10, game.current_turn)
        return base_total


@dataclass
class Triumphant(AlienPower):
    """Triumphant - Power of Victory."""
    name: str = field(default="Triumphant", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 4
        return base_total


@dataclass
class Victorious(AlienPower):
    """Victorious - Power of Success."""
    name: str = field(default="Victorious", init=False)
    description: str = field(default="Retrieve 2 ships on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(self, game: "Game", player: "Player", as_main_player: bool) -> None:
        if player.power_active and player.ships_in_warp >= 2:
            player.retrieve_ships_from_warp(2)


@dataclass
class Champion_M(AlienPower):
    """Champion - Power of Excellence."""
    name: str = field(default="Champion_M", init=False)
    description: str = field(default="Ships count double.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", base_count: int, side: Side) -> int:
        if player.power_active:
            return base_count * 2
        return base_count


@dataclass
class Legacy(AlienPower):
    """Legacy - Power of Inheritance."""
    name: str = field(default="Legacy", init=False)
    description: str = field(default="+1 per home colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            home_colonies = sum(1 for p in player.home_planets if p.has_colony(player.name))
            return base_total + home_colonies
        return base_total


@dataclass
class Pioneer(AlienPower):
    """Pioneer - Power of Firsts."""
    name: str = field(default="Pioneer", init=False)
    description: str = field(default="+3 attacking new planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            if game.defense_planet and not game.defense_planet.has_colony(player.name):
                return base_total + 3
        return base_total


@dataclass
class Innovator(AlienPower):
    """Innovator - Power of Ideas."""
    name: str = field(default="Innovator", init=False)
    description: str = field(default="+2 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 2
        return base_total


@dataclass
class ThreeThousand(AlienPower):
    """ThreeThousand - The 3000th alien!"""
    name: str = field(default="ThreeThousand", init=False)
    description: str = field(default="The 3000th alien! +3 always.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 3
        return base_total


@dataclass
class Milestone_3K(AlienPower):
    """Milestone_3K - Power of Achievement."""
    name: str = field(default="Milestone_3K", init=False)
    description: str = field(default="Extra encounter after winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Zenith(AlienPower):
    """Zenith - Power of Pinnacle."""
    name: str = field(default="Zenith", init=False)
    description: str = field(default="+5 on first encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Acme(AlienPower):
    """Acme - Power of Heights."""
    name: str = field(default="Acme", init=False)
    description: str = field(default="+3 defending home.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet in player.home_planets:
                return base_total + 3
        return base_total


@dataclass
class Pinnacle(AlienPower):
    """Pinnacle - Power of Summit."""
    name: str = field(default="Pinnacle", init=False)
    description: str = field(default="Retrieve all ships on major win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Supreme(AlienPower):
    """Supreme - Power of Dominance."""
    name: str = field(default="Supreme", init=False)
    description: str = field(default="Ships worth extra.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Apex_M(AlienPower):
    """Apex - Power of Peak."""
    name: str = field(default="Apex_M", init=False)
    description: str = field(default="+4 when ahead in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all 20 milestone aliens
for alien_class in [
    Achiever, Completionist, Perfecter, Collector_M, Curator,
    Historian, Triumphant, Victorious, Champion_M, Legacy,
    Pioneer, Innovator, ThreeThousand, Milestone_3K, Zenith,
    Acme, Pinnacle, Supreme, Apex_M,
]:
    AlienRegistry.register(alien_class())
