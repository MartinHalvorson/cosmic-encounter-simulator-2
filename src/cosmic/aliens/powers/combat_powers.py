"""
Combat-modifying alien powers for Cosmic Encounter.
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
class Virus(AlienPower):
    """
    Virus - Multiplies attack card value by number of ships.
    As a main player, multiply your attack card value by the number
    of your ships in the encounter instead of adding.
    """
    name: str = field(default="Virus", init=False)
    description: str = field(
        default="Multiply attack value by your ship count.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        base_value: int,
        side: Side
    ) -> int:
        """Multiply by ship count instead of adding."""
        if not player.power_active:
            return base_value

        # Get ship count for this player in the encounter
        if side == Side.OFFENSE:
            ships = game.offense_ships.get(player.name, 0)
        else:
            ships = game.defense_ships.get(player.name, 0)

        # Virus effect: value * ships (we return the multiplied value,
        # but the ship count shouldn't also be added)
        return base_value * ships

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Ship count doesn't add when Virus is active (already multiplied)."""
        if player.power_active:
            # Return 0 to not add ships (they were already multiplied)
            player_ships = game.offense_ships.get(player.name, 0) if side == Side.OFFENSE else game.defense_ships.get(player.name, 0)
            return base_count - player_ships  # Remove this player's ships from count
        return base_count


@dataclass
class Mirror(AlienPower):
    """
    Mirror - May reverse the digits on attack cards.
    As a main player, after cards are revealed, you may use this
    power to reverse the digits on each attack card (e.g., 15 becomes 51).
    """
    name: str = field(default="Mirror", init=False)
    description: str = field(
        default="Reverse digits on attack cards after reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use if mirroring improves our card."""
        offense_card = context.get("offense_card")
        defense_card = context.get("defense_card")
        is_offense = context.get("is_offense", False)

        if not offense_card or not defense_card:
            return False

        # Check if mirroring helps us
        from ...cards.base import AttackCard
        if isinstance(offense_card, AttackCard) and isinstance(defense_card, AttackCard):
            off_normal = offense_card.value
            off_mirrored = offense_card.mirrored_value()
            def_normal = defense_card.value
            def_mirrored = defense_card.mirrored_value()

            if is_offense:
                # Mirroring helps if it improves our margin
                margin_normal = off_normal - def_normal
                margin_mirrored = off_mirrored - def_mirrored
                return margin_mirrored > margin_normal
            else:
                margin_normal = def_normal - off_normal
                margin_mirrored = def_mirrored - off_mirrored
                return margin_mirrored > margin_normal

        return False


@dataclass
class Tripler(AlienPower):
    """
    Tripler - Triple cards under 10, divide cards over 10 by 3.
    As a main player, your attack card values 10 or less are tripled.
    Values over 10 are divided by 3 (rounding up).
    """
    name: str = field(default="Tripler", init=False)
    description: str = field(
        default="Cards ≤10 are tripled, >10 are divided by 3.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        base_value: int,
        side: Side
    ) -> int:
        """Triple low cards, divide high cards."""
        if not player.power_active:
            return base_value

        if base_value <= 10:
            return base_value * 3
        else:
            return (base_value + 2) // 3  # Round up


@dataclass
class Warpish(AlienPower):
    """
    Warpish - Add ships in warp to combat total.
    As a main player, add the total number of ships in the warp
    (from all players) to your side's total.
    """
    name: str = field(default="Warpish", init=False)
    description: str = field(
        default="Add all ships in warp to your combat total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        base_total: int,
        side: Side
    ) -> int:
        """Add warp ships to total."""
        if not player.power_active:
            return base_total

        warp_total = sum(p.ships_in_warp for p in game.players)
        return base_total + warp_total


@dataclass
class Cudgel(AlienPower):
    """
    Cudgel - When you win, opponent loses as many ships as you had.
    As a main player, when you win an encounter, your opponent
    loses ships equal to the number of ships you had in the encounter.
    """
    name: str = field(default="Cudgel", init=False)
    description: str = field(
        default="Win: opponent loses ships equal to your ship count.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Force opponent to lose extra ships."""
        if not as_main_player or not player.power_active:
            return

        # Determine our ship count and opponent
        if game.offense == player:
            my_ships = game.offense_ships.get(player.name, 0)
            opponent = game.defense
        else:
            my_ships = game.defense_ships.get(player.name, 0)
            opponent = game.offense

        # Remove ships from opponent's colonies
        opponent.get_ships_from_colonies(my_ships, game.planets, exclude_last_ship=False)


@dataclass
class Loser(AlienPower):
    """
    Loser - Lower total wins instead of higher.
    As a main player, you may use this power so that the lower
    total wins the encounter instead of the higher.
    """
    name: str = field(default="Loser", init=False)
    description: str = field(
        default="Lower total wins instead of higher.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Use if we have low cards in hand."""
        attacks = player.get_attack_cards()
        if not attacks:
            return False

        min_value = min(c.value for c in attacks)
        return min_value <= 4


@dataclass
class Antimatter(AlienPower):
    """
    Antimatter - Lowest card wins when you reveal an attack.
    As a main player, after you reveal an attack card, the lowest
    total wins the encounter.
    """
    name: str = field(default="Antimatter", init=False)
    description: str = field(
        default="When you reveal attack, lowest total wins.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Macron(AlienPower):
    """
    Macron - Power of Mass.
    Official FFG rules:
    - As offense or ally, you may only send ONE ship into the encounter
    - Each of your ships adds 4 to your side's total instead of 1
    - When collecting compensation/rewards, each Macron ship counts as 2
    """
    name: str = field(default="Macron", init=False)
    description: str = field(
        default="Send only 1 ship as offense/ally, but each ship counts as 4.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        base_count: int,
        side: Side
    ) -> int:
        """Each ship counts as 4 (but Macron only sends 1 ship as offense/ally)."""
        if not player.power_active:
            return base_count

        # Get this player's ships in the encounter
        if side == Side.OFFENSE:
            my_ships = game.offense_ships.get(player.name, 0)
        else:
            my_ships = game.defense_ships.get(player.name, 0)

        # Replace my ship contribution with 4x value
        other_ships = base_count - my_ships
        return other_ships + (my_ships * 4)


@dataclass
class Leviathan(AlienPower):
    """
    Leviathan - Stack ships on one planet, can commit all to encounter.
    You keep all your ships on one home planet. You may commit any
    number of ships to an encounter.
    """
    name: str = field(default="Leviathan", init=False)
    description: str = field(
        default="Stack all ships on one planet, commit any number.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )

    def on_game_start(self, game: "Game", player: "Player") -> None:
        """Stack all ships on first home planet."""
        if not player.home_planets:
            return

        total_ships = 0
        target_planet = player.home_planets[0]

        # Collect all ships
        for planet in player.home_planets:
            total_ships += planet.get_ships(player.name)
            planet.set_ships(player.name, 0)

        # Put all on first planet
        target_planet.set_ships(player.name, total_ships)


# Register all powers
AlienRegistry.register(Virus())
AlienRegistry.register(Mirror())
AlienRegistry.register(Tripler())
AlienRegistry.register(Warpish())
AlienRegistry.register(Cudgel())
AlienRegistry.register(Loser())
AlienRegistry.register(Antimatter())
AlienRegistry.register(Macron())
AlienRegistry.register(Leviathan())
