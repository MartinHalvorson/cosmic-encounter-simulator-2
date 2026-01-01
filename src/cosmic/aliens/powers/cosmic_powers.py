"""
Cosmic alien powers - final batch of unique abilities.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Anchor(AlienPower):
    """
    Anchor - Steadfast presence.
    Your colonies cannot be removed by enemy powers.
    """
    name: str = field(default="Anchor", init=False)
    description: str = field(
        default="Colonies protected from powers.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Beacon(AlienPower):
    """
    Beacon - Attracts allies.
    All players may ally with you without invitation.
    """
    name: str = field(default="Beacon", init=False)
    description: str = field(
        default="Anyone can ally with you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Cyborg(AlienPower):
    """
    Cyborg - Machine enhanced.
    +3 to attack card value.
    """
    name: str = field(default="Cyborg", init=False)
    description: str = field(
        default="+3 to attack card value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        return value + 3


@dataclass
class Drone(AlienPower):
    """
    Drone - Expendable forces.
    Ships return from warp at end of each encounter.
    """
    name: str = field(default="Drone", init=False)
    description: str = field(
        default="Ships return from warp quickly.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_end(self, game: "Game", player: "Player") -> None:
        if player.ships_in_warp > 0:
            ships = min(2, player.ships_in_warp)
            player.retrieve_ships_from_warp(ships)
            player.return_ships_to_colonies(ships, player.home_planets)


@dataclass
class Exile(AlienPower):
    """
    Exile - Banished wanderer.
    Gain +2 for each foreign colony you have.
    """
    name: str = field(default="Exile", init=False)
    description: str = field(
        default="Bonus per foreign colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        colonies = player.count_foreign_colonies(game.planets)
        return value + (colonies * 2)


@dataclass
class Flash(AlienPower):
    """
    Flash - Lightning fast.
    Can take two encounters in a row.
    """
    name: str = field(default="Flash", init=False)
    description: str = field(
        default="Take second encounter without winning first.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Ghost(AlienPower):
    """
    Ghost - Ethereal presence.
    Can observe but not participate in encounters.
    """
    name: str = field(default="Ghost", init=False)
    description: str = field(
        default="Watch encounters without participating.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hunter(AlienPower):
    """
    Hunter - Tracks prey.
    +4 when attacking someone you attacked last turn.
    """
    name: str = field(default="Hunter", init=False)
    description: str = field(
        default="Bonus vs recently attacked players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Inventor(AlienPower):
    """
    Inventor - Creates new abilities.
    Can copy any other alien's power for one encounter.
    """
    name: str = field(default="Inventor", init=False)
    description: str = field(
        default="Copy another alien's power temporarily.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Jammer(AlienPower):
    """
    Jammer - Blocks signals.
    Prevent one ally from joining opponent.
    """
    name: str = field(default="Jammer", init=False)
    description: str = field(
        default="Block one potential ally.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Keeper(AlienPower):
    """
    Keeper - Protects treasures.
    Cannot lose cards to other players.
    """
    name: str = field(default="Keeper", init=False)
    description: str = field(
        default="Cards protected from theft.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lancer(AlienPower):
    """
    Lancer - Cavalry charge.
    +1 for each ship in the encounter.
    """
    name: str = field(default="Lancer", init=False)
    description: str = field(
        default="Bonus per ship in encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        ships = sum(game.offense_ships.values()) if side == Side.OFFENSE else sum(game.defense_ships.values())
        return total + ships


@dataclass
class Mechanic(AlienPower):
    """
    Mechanic - Repairs damage.
    Retrieve 2 ships from warp at turn start.
    """
    name: str = field(default="Mechanic", init=False)
    description: str = field(
        default="Retrieve extra ships from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_regroup(self, game: "Game", player: "Player", role: PlayerRole) -> None:
        if player.ships_in_warp > 0 and role == PlayerRole.OFFENSE:
            extra = min(2, player.ships_in_warp)
            player.retrieve_ships_from_warp(extra)
            player.return_ships_to_colonies(extra, player.home_planets)


@dataclass
class Navigator(AlienPower):
    """
    Navigator - Master of space travel.
    Can attack any planet, even with ships present.
    """
    name: str = field(default="Navigator", init=False)
    description: str = field(
        default="Attack any planet freely.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Opportunist(AlienPower):
    """
    Opportunist - Seizes chances.
    +3 when opponent has fewer cards.
    """
    name: str = field(default="Opportunist", init=False)
    description: str = field(
        default="Bonus vs players with fewer cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent and len(player.hand) > len(opponent.hand):
            return value + 3
        return value


@dataclass
class Pioneer(AlienPower):
    """
    Pioneer - Explores new territory.
    Gain extra colony when winning.
    """
    name: str = field(default="Pioneer", init=False)
    description: str = field(
        default="Extra colony on winning.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Quake(AlienPower):
    """
    Quake - Seismic force.
    Remove 2 ships from each planet when you win.
    """
    name: str = field(default="Quake", init=False)
    description: str = field(
        default="Shake ships off planets on win.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Ranger(AlienPower):
    """
    Ranger - Forest guardian.
    +2 for each home planet you control.
    """
    name: str = field(default="Ranger", init=False)
    description: str = field(
        default="Bonus per home planet controlled.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        home_controlled = sum(1 for p in player.home_planets if p.has_colony(player.name))
        return value + (home_controlled * 2)


@dataclass
class Scavenger(AlienPower):
    """
    Scavenger - Collects discards.
    Take cards from discard pile.
    """
    name: str = field(default="Scavenger", init=False)
    description: str = field(
        default="Collect discarded cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Titan(AlienPower):
    """
    Titan - Massive force.
    Each ship counts as 2 for total.
    """
    name: str = field(default="Titan", init=False)
    description: str = field(
        default="Ships count double.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        return count * 2


@dataclass
class Ultra(AlienPower):
    """
    Ultra - Supreme power.
    All attack cards treated as their value + 5.
    """
    name: str = field(default="Ultra", init=False)
    description: str = field(
        default="+5 to all attack cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        return value + 5


@dataclass
class Veteran(AlienPower):
    """
    Veteran - Battle-hardened.
    +1 for each encounter won this game.
    """
    name: str = field(default="Veteran", init=False)
    description: str = field(
        default="Bonus from past victories.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    _wins: int = field(default=0, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_win_encounter(self, game: "Game", player: "Player", as_main: bool) -> None:
        if as_main:
            self._wins += 1

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        return value + min(5, self._wins)


@dataclass
class Warden(AlienPower):
    """
    Warden - Prison keeper.
    Opponent's ships cannot leave warp.
    """
    name: str = field(default="Warden", init=False)
    description: str = field(
        default="Trap opponent's ships in warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Xeno(AlienPower):
    """
    Xeno - Foreign agent.
    Can use any alien power once per game.
    """
    name: str = field(default="Xeno", init=False)
    description: str = field(
        default="Use any power once.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


# Register all powers
AlienRegistry.register(Anchor())
AlienRegistry.register(Beacon())
AlienRegistry.register(Cyborg())
AlienRegistry.register(Drone())
AlienRegistry.register(Exile())
AlienRegistry.register(Flash())
AlienRegistry.register(Ghost())
AlienRegistry.register(Hunter())
AlienRegistry.register(Inventor())
AlienRegistry.register(Jammer())
AlienRegistry.register(Keeper())
AlienRegistry.register(Lancer())
AlienRegistry.register(Mechanic())
AlienRegistry.register(Navigator())
AlienRegistry.register(Opportunist())
AlienRegistry.register(Pioneer())
AlienRegistry.register(Quake())
AlienRegistry.register(Ranger())
AlienRegistry.register(Scavenger())
AlienRegistry.register(Titan())
AlienRegistry.register(Ultra())
AlienRegistry.register(Veteran())
AlienRegistry.register(Warden())
AlienRegistry.register(Xeno())


@dataclass
class Zenith(AlienPower):
    """
    Zenith - Peak of power.
    Win all ties and +2 to total.
    """
    name: str = field(default="Zenith", init=False)
    description: str = field(
        default="Win ties and +2 bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        return total + 2


AlienRegistry.register(Zenith())
