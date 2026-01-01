"""
Detective-themed alien powers for Cosmic Encounter.

Powers inspired by investigation and mystery solving.
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
class Sleuth(AlienPower):
    """Sleuth - Power of Investigation. Master detective."""
    name: str = field(default="Sleuth", init=False)
    description: str = field(default="See opponent's card before playing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Inspector(AlienPower):
    """Inspector - Power of Scrutiny. Official investigator."""
    name: str = field(default="Inspector", init=False)
    description: str = field(default="+4 offense, +4 defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + 4
        return base_total


@dataclass
class Forensic(AlienPower):
    """Forensic - Power of Evidence. Scientific analysis."""
    name: str = field(default="Forensic", init=False)
    description: str = field(default="+1 per card in hand (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(6, player.hand_size())
            return base_total + bonus
        return base_total


@dataclass
class Witness(AlienPower):
    """Witness - Power of Testimony. Key observer."""
    name: str = field(default="Witness", init=False)
    description: str = field(default="+3 per ally.", init=False)
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
        return base_total + (allies * 3)


@dataclass
class Alibi(AlienPower):
    """Alibi - Power of Excuse. Proof of innocence."""
    name: str = field(default="Alibi", init=False)
    description: str = field(default="+4 on defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return base_total + 4
        return base_total


@dataclass
class Suspect(AlienPower):
    """Suspect - Power of Accusation. Under suspicion."""
    name: str = field(default="Suspect", init=False)
    description: str = field(default="+5 when behind in colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if not player.power_active:
            return base_total
        my_colonies = player.count_foreign_colonies(game.planets)
        opponent = game.defense if side == Side.OFFENSE else game.offense
        if opponent:
            opp_colonies = opponent.count_foreign_colonies(game.planets)
            if my_colonies < opp_colonies:
                return base_total + 5
        return base_total


@dataclass
class Clue(AlienPower):
    """Clue - Power of Evidence. Trail of hints."""
    name: str = field(default="Clue", init=False)
    description: str = field(default="+1 per turn (max +7).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            bonus = min(7, game.current_turn)
            return base_total + bonus
        return base_total


@dataclass
class Magnifier(AlienPower):
    """Magnifier - Power of Examination. Close inspection."""
    name: str = field(default="Magnifier", init=False)
    description: str = field(default="+5 with 1-2 ships.", init=False)
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
        if ships in (1, 2):
            return base_total + 5
        return base_total


@dataclass
class Deduction(AlienPower):
    """Deduction - Power of Logic. Reasoned conclusions."""
    name: str = field(default="Deduction", init=False)
    description: str = field(default="+2 per ship.", init=False)
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
        return base_total + (ships * 2)


@dataclass
class Interrogator(AlienPower):
    """Interrogator - Power of Questions. Extracting truth."""
    name: str = field(default="Interrogator", init=False)
    description: str = field(default="+5 on offense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return base_total + 5
        return base_total


@dataclass
class Cold_Case(AlienPower):
    """Cold_Case - Power of Persistence. Unsolved mysteries."""
    name: str = field(default="Cold_Case", init=False)
    description: str = field(default="+3 per ship in warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            return base_total + (player.ships_in_warp * 3)
        return base_total


@dataclass
class Stakeout(AlienPower):
    """Stakeout - Power of Patience. Waiting observation."""
    name: str = field(default="Stakeout", init=False)
    description: str = field(default="+5 defending home planets.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 5
        return base_total


@dataclass
class Verdict(AlienPower):
    """Verdict - Power of Judgment. Final decision."""
    name: str = field(default="Verdict", init=False)
    description: str = field(default="+6 on second encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active and game.encounter_number == 2:
            return base_total + 6
        return base_total


@dataclass
class Case_File(AlienPower):
    """Case_File - Power of Records. Documented cases."""
    name: str = field(default="Case_File", init=False)
    description: str = field(default="+2 per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", base_total: int, side: Side) -> int:
        if player.power_active:
            colonies = sum(1 for p in game.planets if p.has_colony(player.name))
            return base_total + (colonies * 2)
        return base_total


# Register all detective powers
DETECTIVE_POWERS = [
    Sleuth, Inspector, Forensic, Witness, Alibi,
    Suspect, Clue, Magnifier, Deduction, Interrogator,
    Cold_Case, Stakeout, Verdict, Case_File,
]

for power_class in DETECTIVE_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass  # Already registered
