"""
Additional alien powers from Cosmic Encounter.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


@dataclass
class Barbarian(AlienPower):
    """
    Barbarian - Pillage losing colonies.
    When you win an encounter, take one card from each losing player.
    """
    name: str = field(default="Barbarian", init=False)
    description: str = field(
        default="Win: take a card from each losing player.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Boomerang(AlienPower):
    """
    Boomerang - Retrieve encounter card if you win.
    As a main player, if you win an encounter, add your encounter
    card back to your hand instead of discarding it.
    """
    name: str = field(default="Boomerang", init=False)
    description: str = field(
        default="Win: keep your encounter card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Brute(AlienPower):
    """
    Brute - Add reinforcement cards automatically.
    As a main player, after cards are revealed, you may add all
    reinforcement cards in your hand to your side's total.
    """
    name: str = field(default="Brute", init=False)
    description: str = field(
        default="Automatically play all reinforcement cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Crystal(AlienPower):
    """
    Crystal - See the future.
    You may look at the top card of any deck at any time.
    """
    name: str = field(default="Crystal", init=False)
    description: str = field(
        default="See top card of any deck.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Deuce(AlienPower):
    """
    Deuce - Take two turns in a row.
    After your first encounter each turn, you must have a second encounter.
    """
    name: str = field(default="Deuce", init=False)
    description: str = field(
        default="Always take two encounters per turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Dragon(AlienPower):
    """
    Dragon - Breathe fire on opponents.
    As a main player, before cards are revealed, you may discard
    a card to eliminate one of your opponent's ships.
    """
    name: str = field(default="Dragon", init=False)
    description: str = field(
        default="Discard card to remove opponent ship.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Fury(AlienPower):
    """
    Fury - Grow stronger when attacked.
    As the defense, add 2 to your total for each of your ships
    in the encounter.
    """
    name: str = field(default="Fury", init=False)
    description: str = field(
        default="As defense, +2 per ship in encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        if side == Side.DEFENSE and player.power_active:
            my_ships = game.defense_ships.get(player.name, 0)
            return base_count + my_ships  # Double effective ships
        return base_count


@dataclass
class Genius_Alt(AlienPower):
    """
    Sage - Draw extra cards after encounters.
    After each encounter, you may draw one card from the deck.
    """
    name: str = field(default="Sage", init=False)
    description: str = field(
        default="Draw 1 card after each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hate(AlienPower):
    """
    Hate - Obsess over one opponent.
    Choose one opponent. Add 4 to your total whenever you
    are in an encounter against them.
    """
    name: str = field(default="Hate", init=False)
    description: str = field(
        default="+4 against your chosen nemesis.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Laser(AlienPower):
    """
    Laser - Precision targeting.
    As offense, choose which planet to attack (ignore destiny).
    """
    name: str = field(default="Laser", init=False)
    description: str = field(
        default="Choose attack target regardless of destiny.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Mimic(AlienPower):
    """
    Mimic - Copy another alien's power.
    At the start of each encounter, you may use any one alien
    power belonging to another player.
    """
    name: str = field(default="Mimic", init=False)
    description: str = field(
        default="Use any other player's power each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Nightmare(AlienPower):
    """
    Nightmare - Terrify opponents.
    As a main player, your opponent must commit at least as many
    ships as you do.
    """
    name: str = field(default="Nightmare", init=False)
    description: str = field(
        default="Force opponent to match your ship count.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Patriot(AlienPower):
    """
    Patriot - Defend home system.
    As defense on your home planet, add 3 to your total.
    """
    name: str = field(default="Patriot", init=False)
    description: str = field(
        default="+3 when defending home planets.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        if side == Side.DEFENSE and player.power_active:
            if game.defense_planet and game.defense_planet.owner == player:
                return base_total + 3
        return base_total


@dataclass
class Pirate(AlienPower):
    """
    Pirate - Steal from the opposition.
    As offense, after winning, take one card from each opposing
    main player and ally.
    """
    name: str = field(default="Pirate", init=False)
    description: str = field(
        default="Win offense: take cards from defenders.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Poison(AlienPower):
    """
    Poison - Weaken opponents.
    Opponents in encounters with you have -2 to their total.
    """
    name: str = field(default="Poison", init=False)
    description: str = field(
        default="Opponents get -2 in encounters with you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Rage(AlienPower):
    """
    Rage - Power grows from losses.
    Each time you lose a ship, gain a rage token. Add tokens to total.
    """
    name: str = field(default="Rage", init=False)
    description: str = field(
        default="Gain tokens from lost ships, add to combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Scout(AlienPower):
    """
    Scout - Reconnaissance.
    Look at an opponent's hand before selecting your encounter card.
    """
    name: str = field(default="Scout", init=False)
    description: str = field(
        default="See opponent's hand before playing card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Thief(AlienPower):
    """
    Thief - Steal cards.
    Take a random card from any player once per encounter.
    """
    name: str = field(default="Thief", init=False)
    description: str = field(
        default="Steal one card per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Tyrant(AlienPower):
    """
    Tyrant - Dominate weaker players.
    Add 1 to your total for each foreign colony you have more
    than your opponent.
    """
    name: str = field(default="Tyrant", init=False)
    description: str = field(
        default="+1 per colony advantage over opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Underdog(AlienPower):
    """
    Underdog - Stronger when behind.
    Add 1 to your total for each foreign colony you have fewer
    than your opponent.
    """
    name: str = field(default="Underdog", init=False)
    description: str = field(
        default="+1 for each colony behind opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Vox(AlienPower):
    """
    Vox - Influence the vote.
    After alliances are declared, you may force one ally to switch sides.
    """
    name: str = field(default="Vox", init=False)
    description: str = field(
        default="Force one ally to switch sides.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Warlock(AlienPower):
    """
    Warlock - Cast spells.
    Once per encounter, force an opponent to discard their hand
    and draw a new one.
    """
    name: str = field(default="Warlock", init=False)
    description: str = field(
        default="Force opponent to redraw hand.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Barbarian())
AlienRegistry.register(Boomerang())
AlienRegistry.register(Brute())
AlienRegistry.register(Crystal())
AlienRegistry.register(Deuce())
AlienRegistry.register(Dragon())
AlienRegistry.register(Fury())
AlienRegistry.register(Genius_Alt())
AlienRegistry.register(Hate())
AlienRegistry.register(Laser())
AlienRegistry.register(Mimic())
AlienRegistry.register(Nightmare())
AlienRegistry.register(Patriot())
AlienRegistry.register(Pirate())
AlienRegistry.register(Poison())
AlienRegistry.register(Rage())
AlienRegistry.register(Scout())
AlienRegistry.register(Thief())
AlienRegistry.register(Tyrant())
AlienRegistry.register(Underdog())
AlienRegistry.register(Vox())
AlienRegistry.register(Warlock())
