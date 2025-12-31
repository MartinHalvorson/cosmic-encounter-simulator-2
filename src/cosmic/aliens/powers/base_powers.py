"""
Base/simple alien powers for Cosmic Encounter.
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
class Zombie(AlienPower):
    """
    Zombie - Power of Undeath.
    Each time you lose ships to the warp, you may prevent ONE of your ships
    from going to the warp, instead returning it to one of your colonies.
    (Official FFG rules - optional, saves only one ship per loss event)
    """
    name: str = field(default="Zombie", init=False)
    description: str = field(
        default="Prevent one ship from going to warp each time you lose ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        source: str
    ) -> int:
        """Prevent ONE ship from going to warp, return it to colonies."""
        if player.power_active and count > 0:
            # Return ONE ship to home colonies (official rules)
            player.return_ships_to_colonies(1, player.home_planets)
            return count - 1  # One fewer ship goes to warp
        return count


@dataclass
class Healer(AlienPower):
    """
    Healer - Can heal other players' ships from the warp.
    When any other player's ships would go to the warp, you may use this
    power to heal them instead. You draw 1 card per ship healed.
    """
    name: str = field(default="Healer", init=False)
    description: str = field(
        default="Heal other players' ships for cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def should_use(
        self,
        game: "Game",
        player: "Player",
        context: Dict[str, Any]
    ) -> bool:
        """Healer usually wants to heal for cards."""
        return player.hand_size() < 10  # Heal if we want more cards


@dataclass
class Symbiote(AlienPower):
    """
    Symbiote - Starts with double the normal number of ships.
    You have 8 ships on each of your home planets instead of 4.
    """
    name: str = field(default="Symbiote", init=False)
    description: str = field(
        default="Start with double the normal ships (8 per planet).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_game_start(self, game: "Game", player: "Player") -> None:
        """Double the ships on each home planet."""
        for planet in player.home_planets:
            current = planet.get_ships(player.name)
            planet.set_ships(player.name, current * 2)


@dataclass
class Pacifist(AlienPower):
    """
    Pacifist - Wins encounter if you play negotiate and opponent plays attack.
    As a main player, if you reveal a negotiate card and your opponent
    reveals an attack card, you win the encounter.
    """
    name: str = field(default="Pacifist", init=False)
    description: str = field(
        default="Win if you play negotiate against an attack card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


@dataclass
class Shadow(AlienPower):
    """
    Shadow - When destiny is drawn, remove one ship from that player.
    Whenever another player is determined to be a defense by the
    destiny draw, you may remove one ship of your choice from any
    colony belonging to that player.
    """
    name: str = field(default="Shadow", init=False)
    description: str = field(
        default="Remove a ship from the defense when destiny is drawn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_destiny(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        destiny_player: "Player"
    ) -> Optional["Player"]:
        """Remove a ship from the defense player."""
        if player.power_active and destiny_player != player:
            # Remove one ship strategically (prefer single-ship colonies)
            all_planets = game.planets
            target_colonies = [
                p for p in all_planets
                if p.has_colony(destiny_player.name)
            ]
            if target_colonies:
                # Prefer removing from single-ship foreign colonies
                target_colonies.sort(
                    key=lambda p: (
                        not p.is_foreign_colony(destiny_player),
                        p.get_ships(destiny_player.name)
                    )
                )
                target = target_colonies[0]
                target.remove_ships(destiny_player.name, 1)
        return None


@dataclass
class Parasite(AlienPower):
    """
    Parasite - Can join either side whether invited or not.
    You may ally on either side of any encounter, even if you
    are not invited.
    """
    name: str = field(default="Parasite", init=False)
    description: str = field(
        default="Join any encounter as ally, invited or not.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_alliance_invite(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole,
        invited_to: Side
    ) -> Optional[bool]:
        """Can join even if not invited."""
        if player.power_active:
            return True  # Always allowed to join
        return None


@dataclass
class Machine(AlienPower):
    """
    Machine - May continue taking encounters as long as you have encounter cards.
    At the start of any encounter, if you have at least one encounter
    card in your hand, you may have another encounter.
    """
    name: str = field(default="Machine", init=False)
    description: str = field(
        default="Take extra encounters while you have encounter cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Warrior(AlienPower):
    """
    Warrior - Accumulate tokens that add to combat totals.
    Start with 0 tokens. Gain 1 on wins, 2 on losses/failed deals.
    Add tokens to your side's total in encounters.
    """
    name: str = field(default="Warrior", init=False)
    description: str = field(
        default="Accumulate tokens (+1 win, +2 loss) that add to combat.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
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
        """Add warrior tokens to combat total."""
        if player.power_active:
            return base_total + player.warrior_tokens
        return base_total

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Gain 1 token on win."""
        if as_main_player:
            player.warrior_tokens += 1

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """Gain 2 tokens on loss."""
        if as_main_player:
            player.warrior_tokens += 2

    def on_deal_failure(
        self,
        game: "Game",
        player: "Player",
        opponent: "Player"
    ) -> None:
        """Gain 2 tokens on failed deal."""
        player.warrior_tokens += 2


@dataclass
class Guerrilla(AlienPower):
    """
    Guerrilla - Power of Attrition.
    Official FFG rules: As a main player, after you lose an encounter,
    all other players who had ships in the encounter (your opponent and
    their allies) lose all but one of their ships to the warp.
    """
    name: str = field(default="Guerrilla", init=False)
    description: str = field(
        default="When you lose, opponents lose all but one ship each.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_main_player: bool
    ) -> None:
        """When we lose, opponents lose all but one ship."""
        if not as_main_player or not player.power_active:
            return

        # Determine which side won
        if game.offense == player:
            # We were offense, defense won
            winner_ships = game.defense_ships
        else:
            # We were defense, offense won
            winner_ships = game.offense_ships

        # Each player on winning side loses all but 1 ship to warp
        for player_name, ship_count in winner_ships.items():
            if ship_count > 1:
                ships_to_lose = ship_count - 1
                target_player = game.get_player_by_name(player_name)
                if target_player:
                    target_player.ships_in_warp += ships_to_lose


@dataclass
class Mind(AlienPower):
    """
    Mind - Power of Knowledge.
    Official FFG rules: As a main player, before allies are invited,
    you may use this power to look at the entire hand of your opponent.
    You may not reveal what you see to other players.
    """
    name: str = field(default="Mind", init=False)
    description: str = field(
        default="Look at opponent's hand before allies are invited.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )

    def on_before_alliance(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Look at opponent's hand. AI can use this information."""
        if not player.power_active:
            return

        # Determine opponent
        if game.offense == player:
            opponent = game.defense
        else:
            opponent = game.offense

        # Store opponent's hand info for AI decision-making
        if hasattr(player, 'ai') and player.ai:
            player.ai.observed_hand = list(opponent.hand)


@dataclass
class Vulch(AlienPower):
    """
    Vulch - Power to Salvage.
    Official FFG rules: Whenever any other player discards an artifact
    card (whether after playing it or not), use this power to add the
    artifact to your hand. Your own discarded artifacts cannot be salvaged.
    """
    name: str = field(default="Vulch", init=False)
    description: str = field(
        default="Collect artifacts discarded by other players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_card_discarded(
        self,
        game: "Game",
        player: "Player",
        discarding_player: "Player",
        card: Any
    ) -> bool:
        """Salvage artifact cards discarded by others."""
        if not player.power_active:
            return False

        # Don't salvage own cards
        if discarding_player == player:
            return False

        # Check if it's an artifact card
        from ...cards.base import ArtifactCard
        if isinstance(card, ArtifactCard):
            player.add_card(card)
            return True  # Card was salvaged, don't discard

        return False


@dataclass
class Will(AlienPower):
    """
    Will - Power of Choice.
    Official FFG rules: After drawing destiny, encounter any alien on any planet
    of your choice instead of the destiny-mandated one.
    """
    name: str = field(default="Will", init=False)
    description: str = field(default="Choose any target instead of destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE],
        init=False
    )


@dataclass
class Demon(AlienPower):
    """
    Demon - Power to Possess.
    Official FFG rules: As main player before alliances, take possession of
    another player's hand. Use their cards as if your own.
    """
    name: str = field(default="Demon", init=False)
    description: str = field(default="Possess another player's hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE, PlayerRole.DEFENSE],
        init=False
    )


# Register all powers
AlienRegistry.register(Zombie())
AlienRegistry.register(Healer())
AlienRegistry.register(Symbiote())
AlienRegistry.register(Pacifist())
AlienRegistry.register(Shadow())
AlienRegistry.register(Parasite())
AlienRegistry.register(Machine())
AlienRegistry.register(Warrior())
AlienRegistry.register(Guerrilla())
AlienRegistry.register(Mind())
AlienRegistry.register(Vulch())
AlienRegistry.register(Will())
AlienRegistry.register(Demon())
