"""
Milestone alien powers - Adding 50+ new aliens to reach 1000+ total.

These are creative, unique aliens with interesting game mechanics
inspired by various themes and concepts.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING

from ..base import AlienPower, PowerCategory
from ...types import PowerTiming, PowerType, Side, PlayerRole

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player

from ..registry import AlienRegistry


# ==============================================================================
# THEME: QUANTUM & PHYSICS
# ==============================================================================

@dataclass
class Superposition(AlienPower):
    """
    Superposition - Power of Uncertainty.
    Until cards are revealed, you are considered to be both winning
    and losing simultaneously. After reveal, collapse to winning if
    you would win, or draw 2 cards if you would lose.
    """
    name: str = field(default="Superposition", init=False)
    description: str = field(
        default="Exist in quantum state - draw 2 cards when losing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """When the quantum state collapses to losing, gain cards."""
        if player.power_active:
            cards = game.cosmic_deck.draw_multiple(2)
            player.add_cards(cards)


@dataclass
class Entangler(AlienPower):
    """
    Entangler - Power to Bind.
    When you commit ships, entangle them with an opponent's ships.
    If your entangled ships go to the warp, their ships go too.
    """
    name: str = field(default="Entangler", init=False)
    description: str = field(
        default="When your ships go to warp, opponent loses ships too.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_ships_to_warp(
        self,
        game: "Game",
        player: "Player",
        count: int,
        reason: str
    ) -> int:
        """When ships go to warp, opponent loses ships too."""
        if player.power_active and count > 0:
            # Entangle opponent's ships
            opponent = game.defense if player == game.offense else game.offense
            if opponent:
                entangled = min(count, opponent.ships_in_warp + sum(
                    game.offense_ships.values() if player == game.defense
                    else game.defense_ships.values()
                ))
                opponent.send_ships_to_warp(min(count, 2))
        return count


@dataclass
class WaveFunction(AlienPower):
    """
    Wave Function - Power to Propagate.
    Your influence spreads. When you win an encounter, you may
    place 1 ship on any planet where you already have a colony.
    """
    name: str = field(default="WaveFunction", init=False)
    description: str = field(
        default="When winning, add 1 ship to any existing colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """After winning, spread to existing colonies."""
        if player.power_active:
            colonies = [p for p in game.planets if p.has_colony(player.name)]
            if colonies:
                import random
                target = random.choice(colonies)
                target.add_ships(player.name, 1)


@dataclass
class Higgs(AlienPower):
    """
    Higgs - Power of Mass.
    Your ships have extra mass. Each of your ships counts as 1.5
    in encounters (round down for total).
    """
    name: str = field(default="Higgs", init=False)
    description: str = field(
        default="Ships count as 1.5 each (round down).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(
        self,
        game: "Game",
        player: "Player",
        ship_count: int,
        side: Side
    ) -> int:
        """Each ship counts as 1.5."""
        if player.power_active:
            return int(ship_count * 1.5)
        return ship_count


@dataclass
class Singularity(AlienPower):
    """
    Singularity - Power to Collapse.
    Once per encounter, you may collapse all ships in the encounter
    to a single point. Total becomes: highest single attack card value.
    """
    name: str = field(default="Singularity", init=False)
    description: str = field(
        default="Ships don't count - only attack card values matter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        total: int,
        side: Side
    ) -> int:
        """Collapse to just card value."""
        if player.power_active:
            # Get the card value
            if side == Side.OFFENSE and game.offense_card:
                if hasattr(game.offense_card, 'value'):
                    return game.offense_card.value
            elif side == Side.DEFENSE and game.defense_card:
                if hasattr(game.defense_card, 'value'):
                    return game.defense_card.value
        return total


# ==============================================================================
# THEME: NATURE & BIOLOGY
# ==============================================================================

@dataclass
class Mycelia(AlienPower):
    """
    Mycelia - Power of the Network.
    You spread through the underground network. When you gain a colony,
    you may place 1 ship on an adjacent planet (same owner).
    """
    name: str = field(default="Mycelia", init=False)
    description: str = field(
        default="When gaining a colony, spread 1 ship to adjacent planet.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_gain_colony(
        self,
        game: "Game",
        player: "Player",
        planet: Any
    ) -> None:
        """Spread to adjacent planet when gaining colony."""
        if player.power_active:
            # Find another planet owned by same player
            adjacent = [p for p in game.planets
                       if p.owner == planet.owner and p != planet]
            if adjacent:
                import random
                target = random.choice(adjacent)
                target.add_ships(player.name, 1)


@dataclass
class Pollinator(AlienPower):
    """
    Pollinator - Power to Spread.
    After any encounter you're involved in, you may move 1 ship
    from the encounter to any of your home planets.
    """
    name: str = field(default="Pollinator", init=False)
    description: str = field(
        default="After encounters, move 1 ship to home.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_end(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Move ship to home after encounter."""
        if player.power_active and player.home_planets:
            import random
            target = random.choice(player.home_planets)
            target.add_ships(player.name, 1)


@dataclass
class Apex(AlienPower):
    """
    Apex - Power of the Predator.
    When you win as offense, you may consume 1 opposing ship
    permanently (removed from game instead of warp).
    """
    name: str = field(default="Apex", init=False)
    description: str = field(
        default="When winning, permanently remove 1 opponent ship.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Consume one enemy ship permanently."""
        if player.power_active and as_offense:
            # Remove 1 ship permanently (don't send to warp, just gone)
            if game.defense:
                game.defense.eliminated_ships = getattr(game.defense, 'eliminated_ships', 0) + 1


@dataclass
class Hibernator(AlienPower):
    """
    Hibernator - Power to Sleep.
    At the start of your turn, you may skip it to retrieve
    all your ships from the warp and draw 3 cards.
    """
    name: str = field(default="Hibernator", init=False)
    description: str = field(
        default="Skip turn to retrieve all ships from warp + draw 3.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_turn_start(
        self,
        game: "Game",
        player: "Player"
    ) -> bool:
        """May hibernate to restore ships and cards."""
        if player.power_active and player.ships_in_warp >= 3:
            # Hibernate: retrieve all ships, draw cards
            ships = player.ships_in_warp
            player.retrieve_ships_from_warp(ships)
            player.return_ships_to_colonies(ships, player.home_planets)

            cards = game.cosmic_deck.draw_multiple(3)
            player.add_cards(cards)
            return True  # Signal turn skip
        return False


@dataclass
class Camouflage(AlienPower):
    """
    Camouflage - Power to Hide.
    Opponents cannot see your encounter card before reveal.
    Additionally, you may bluff: announce any card value.
    """
    name: str = field(default="Camouflage", init=False)
    description: str = field(
        default="Your encounter card is hidden until reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mimic(AlienPower):
    """
    Mimic - Power to Copy.
    At the start of each encounter, you may copy any other
    alien power in the game for that encounter only.
    """
    name: str = field(default="Mimic", init=False)
    description: str = field(
        default="Copy another player's alien power each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    mimicked_power: Optional[str] = None

    def on_encounter_start(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Copy another player's power."""
        if player.power_active:
            # Pick a random other player's power to mimic
            others = [p for p in game.players if p != player and p.alien]
            if others:
                import random
                target = random.choice(others)
                self.mimicked_power = target.alien.name


# ==============================================================================
# THEME: TECHNOLOGY & MACHINES
# ==============================================================================

@dataclass
class Compiler(AlienPower):
    """
    Compiler - Power to Process.
    Once per encounter, you may discard 2 cards to draw 3 cards.
    Optimizing your hand.
    """
    name: str = field(default="Compiler", init=False)
    description: str = field(
        default="Discard 2 cards to draw 3 cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_planning(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Optimize hand by exchanging cards."""
        if player.power_active and len(player.hand) >= 2:
            import random
            # Discard 2 random cards
            discards = random.sample(player.hand, 2)
            for card in discards:
                player.remove_card(card)
                game.cosmic_deck.discard(card)
            # Draw 3
            cards = game.cosmic_deck.draw_multiple(3)
            player.add_cards(cards)


@dataclass
class Firewall(AlienPower):
    """
    Firewall - Power to Block.
    Opponents cannot play artifacts or flares against you.
    """
    name: str = field(default="Firewall", init=False)
    description: str = field(
        default="Immune to artifacts and flares targeting you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Debugger(AlienPower):
    """
    Debugger - Power to Fix.
    Once per encounter, after reveal, you may change a digit
    on your attack card (e.g., 08 to 18, or 20 to 40).
    """
    name: str = field(default="Debugger", init=False)
    description: str = field(
        default="Change one digit on your attack card after reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        value: int,
        side: Side
    ) -> int:
        """Modify attack value by changing a digit."""
        if player.power_active and value < 40:
            return value + 10  # Simplification: just add 10
        return value


@dataclass
class Overclocked(AlienPower):
    """
    Overclocked - Power to Surge.
    You may commit up to 6 ships to an encounter instead of 4.
    """
    name: str = field(default="Overclocked", init=False)
    description: str = field(
        default="Commit up to 6 ships to encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Recursive(AlienPower):
    """
    Recursive - Power to Loop.
    When you win an encounter, if you played an attack 10 or less,
    you may immediately have another encounter without drawing destiny.
    """
    name: str = field(default="Recursive", init=False)
    description: str = field(
        default="Win with attack 10 or less: take another encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Check for extra encounter."""
        if player.power_active and as_offense:
            if game.offense_card and hasattr(game.offense_card, 'value'):
                if game.offense_card.value <= 10:
                    game.extra_encounter_granted = True


# ==============================================================================
# THEME: SOCIAL & PSYCHOLOGICAL
# ==============================================================================

@dataclass
class Empath(AlienPower):
    """
    Empath - Power to Sense.
    Before cards are selected, you may look at one opponent's hand
    and see what encounter cards they have.
    """
    name: str = field(default="Empath", init=False)
    description: str = field(
        default="See opponent's encounter cards before playing.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Manipulator(AlienPower):
    """
    Manipulator - Power to Control.
    After alliances are formed, you may force one ally to switch sides.
    """
    name: str = field(default="Manipulator", init=False)
    description: str = field(
        default="Force one ally to switch sides after alliance phase.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pacifier(AlienPower):
    """
    Pacifier - Power of Peace.
    If both players play negotiate cards, you automatically
    succeed in making a deal (no failed deal penalty possible).
    """
    name: str = field(default="Pacifier", init=False)
    description: str = field(
        default="Negotiate-Negotiate always succeeds for you.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Provocateur(AlienPower):
    """
    Provocateur - Power to Incite.
    Once per turn, you may force another player to draw destiny
    and have an encounter, even if it's not their turn.
    """
    name: str = field(default="Provocateur", init=False)
    description: str = field(
        default="Force another player to have an encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Gaslighter(AlienPower):
    """
    Gaslighter - Power to Confuse.
    Once per encounter, you may swap your encounter card with
    your opponent's after both are selected but before reveal.
    """
    name: str = field(default="Gaslighter", init=False)
    description: str = field(
        default="Swap encounter cards with opponent before reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_reveal(
        self,
        game: "Game",
        player: "Player",
        role: PlayerRole
    ) -> None:
        """Swap cards with opponent."""
        if player.power_active:
            if role == PlayerRole.OFFENSE:
                game.offense_card, game.defense_card = game.defense_card, game.offense_card
            elif role == PlayerRole.DEFENSE:
                game.offense_card, game.defense_card = game.defense_card, game.offense_card


# ==============================================================================
# THEME: COSMIC & CELESTIAL
# ==============================================================================

@dataclass
class Nebula(AlienPower):
    """
    Nebula - Power of the Cloud.
    Your ships in the encounter are obscured. Ships you commit
    are unknown to opponents until reveal.
    """
    name: str = field(default="Nebula", init=False)
    description: str = field(
        default="Ship count hidden from opponents until reveal.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pulsar(AlienPower):
    """
    Pulsar - Power to Pulse.
    At regular intervals (every 3rd encounter you're in), all other
    players must discard their highest attack card if able.
    """
    name: str = field(default="Pulsar", init=False)
    description: str = field(
        default="Every 3rd encounter, opponents discard highest attack.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    encounter_count: int = 0

    def on_encounter_start(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Check if it's pulse time."""
        if player.power_active:
            self.encounter_count += 1
            if self.encounter_count >= 3:
                self.encounter_count = 0
                # Force opponents to discard highest attack
                for other in game.players:
                    if other != player:
                        attacks = [c for c in other.hand
                                  if hasattr(c, 'value') and c.value is not None]
                        if attacks:
                            highest = max(attacks, key=lambda c: c.value)
                            other.remove_card(highest)
                            game.cosmic_deck.discard(highest)


@dataclass
class Quasar(AlienPower):
    """
    Quasar - Power of Energy.
    When you play an attack card, you may add +5 for each card
    in your discard pile (max +15).
    """
    name: str = field(default="Quasar", init=False)
    description: str = field(
        default="Add +5 per card in discard pile (max +15).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_attack_value(
        self,
        game: "Game",
        player: "Player",
        value: int,
        side: Side
    ) -> int:
        """Add bonus based on discards."""
        if player.power_active:
            discards = len(game.cosmic_deck.discard_pile)
            bonus = min(15, (discards // 5) * 5)
            return value + bonus
        return value


@dataclass
class Eclipse(AlienPower):
    """
    Eclipse - Power to Darken.
    When you are defense, all attack cards have their values halved
    (round down).
    """
    name: str = field(default="Eclipse", init=False)
    description: str = field(
        default="As defense, all attack values are halved.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Supernova(AlienPower):
    """
    Supernova - Power to Explode.
    Once per game, when you lose as offense, you may explode:
    All ships in the encounter go to the warp (both sides).
    """
    name: str = field(default="Supernova", init=False)
    description: str = field(
        default="Once per game: when losing, send ALL ships to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    used: bool = False

    def on_lose_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Explode and take everyone with you."""
        if player.power_active and not self.used and as_offense:
            self.used = True
            # Send all ships to warp
            for name, count in game.offense_ships.items():
                p = game.get_player_by_name(name)
                if p:
                    p.send_ships_to_warp(count)
            for name, count in game.defense_ships.items():
                p = game.get_player_by_name(name)
                if p:
                    p.send_ships_to_warp(count)


# ==============================================================================
# THEME: ELEMENTAL & PRIMORDIAL
# ==============================================================================

@dataclass
class Erosion(AlienPower):
    """
    Erosion - Power to Wear Down.
    Each encounter you're involved in, your opponent's attack card
    loses 1 value. This stacks over the game.
    """
    name: str = field(default="Erosion", init=False)
    description: str = field(
        default="Opponent attack cards lose accumulated value.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    erosion_level: int = 0

    def on_encounter_start(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Increase erosion each encounter."""
        if player.power_active:
            self.erosion_level = min(10, self.erosion_level + 1)


@dataclass
class Crystalline(AlienPower):
    """
    Crystalline - Power of Structure.
    Your attack cards have fixed values that cannot be modified
    by any game effect (reinforcements, powers, etc.).
    """
    name: str = field(default="Crystalline", init=False)
    description: str = field(
        default="Your attack values cannot be modified.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magma(AlienPower):
    """
    Magma - Power of Heat.
    When you win as offense, you may "burn" the planet:
    Remove all ships there and gain a fresh colony with your ships only.
    """
    name: str = field(default="Magma", init=False)
    description: str = field(
        default="When winning, may clear planet of all other ships.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_win_encounter(
        self,
        game: "Game",
        player: "Player",
        as_offense: bool
    ) -> None:
        """Burn the planet clean."""
        if player.power_active and as_offense and game.defense_planet:
            # Remove all other players' ships
            for p in game.players:
                if p != player:
                    ships = game.defense_planet.get_ships(p.name)
                    if ships > 0:
                        game.defense_planet.remove_ships(p.name, ships)
                        p.send_ships_to_warp(ships)


@dataclass
class Tempest(AlienPower):
    """
    Tempest - Power of the Storm.
    Once per encounter, you may shuffle all encounter cards
    back to hands and force both players to select again.
    """
    name: str = field(default="Tempest", init=False)
    description: str = field(
        default="Force both players to pick encounter cards again.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Permafrost(AlienPower):
    """
    Permafrost - Power to Freeze.
    Ships you defeat are frozen. They go to a special frozen zone
    instead of the warp and cannot be retrieved until you lose.
    """
    name: str = field(default="Permafrost", init=False)
    description: str = field(
        default="Defeated ships are frozen instead of going to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# THEME: ECONOMIC & MERCANTILE
# ==============================================================================

@dataclass
class Investor(AlienPower):
    """
    Investor - Power to Grow Wealth.
    At the start of each of your turns, draw 1 card for each
    foreign colony you have (max 3).
    """
    name: str = field(default="Investor", init=False)
    description: str = field(
        default="Draw 1 card per foreign colony at turn start (max 3).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Collect investment returns."""
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            draw_count = min(3, colonies)
            if draw_count > 0:
                cards = game.cosmic_deck.draw_multiple(draw_count)
                player.add_cards(cards)


@dataclass
class Monopolist(AlienPower):
    """
    Monopolist - Power to Corner Markets.
    When you gain your 3rd colony on a player's home system,
    you may claim all of that player's cards.
    """
    name: str = field(default="Monopolist", init=False)
    description: str = field(
        default="3 colonies on one system: take target's cards.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Liquidator(AlienPower):
    """
    Liquidator - Power to Convert.
    You may discard any number of cards to retrieve that many
    ships from the warp at the start of your turn.
    """
    name: str = field(default="Liquidator", init=False)
    description: str = field(
        default="Discard cards to retrieve ships from warp 1:1.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(
        self,
        game: "Game",
        player: "Player"
    ) -> None:
        """Convert cards to ships."""
        if player.power_active and player.ships_in_warp > 0 and player.hand:
            # Trade cards for ships (up to available)
            trade_count = min(len(player.hand), player.ships_in_warp)
            if trade_count > 0:
                import random
                discards = random.sample(player.hand, trade_count)
                for card in discards:
                    player.remove_card(card)
                    game.cosmic_deck.discard(card)
                player.retrieve_ships_from_warp(trade_count)
                player.return_ships_to_colonies(trade_count, player.home_planets)


@dataclass
class Arbiter(AlienPower):
    """
    Arbiter - Power to Judge.
    When two players make a deal, you may veto it. The deal fails
    but neither player loses ships.
    """
    name: str = field(default="Arbiter", init=False)
    description: str = field(
        default="Veto any deal between other players.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# THEME: MYSTICAL & ARCANE
# ==============================================================================

@dataclass
class Augur(AlienPower):
    """
    Augur - Power to Divine.
    At the start of each encounter, look at the top 3 cards
    of the cosmic deck. Put them back in any order.
    """
    name: str = field(default="Augur", init=False)
    description: str = field(
        default="Scry top 3 cards of deck and reorder them.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hexcaster(AlienPower):
    """
    Hexcaster - Power to Curse.
    Once per encounter, you may hex an opponent. Until the end of
    your next turn, they cannot use their alien power.
    """
    name: str = field(default="Hexcaster", init=False)
    description: str = field(
        default="Curse opponent's power for one full turn.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Summoner(AlienPower):
    """
    Summoner - Power to Call.
    Instead of taking ships from colonies, you may summon ships
    directly from the warp to the encounter.
    """
    name: str = field(default="Summoner", init=False)
    description: str = field(
        default="Use ships from warp for encounters instead of colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ritualist(AlienPower):
    """
    Ritualist - Power of Sacrifice.
    Before reveal, you may sacrifice 1 of your ships in the encounter
    to add +10 to your total.
    """
    name: str = field(default="Ritualist", init=False)
    description: str = field(
        default="Sacrifice 1 ship for +10 to total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(
        self,
        game: "Game",
        player: "Player",
        total: int,
        side: Side
    ) -> int:
        """Sacrifice ship for bonus."""
        if player.power_active:
            if side == Side.OFFENSE and game.offense_ships.get(player.name, 0) > 1:
                game.offense_ships[player.name] -= 1
                player.send_ships_to_warp(1)
                return total + 10
            elif side == Side.DEFENSE and game.defense_ships.get(player.name, 0) > 1:
                game.defense_ships[player.name] -= 1
                player.send_ships_to_warp(1)
                return total + 10
        return total


@dataclass
class Alchemist(AlienPower):
    """
    Alchemist - Power to Transform.
    Once per encounter, you may transform a Negotiate card
    into an Attack 20, or an Attack into a Negotiate.
    """
    name: str = field(default="Alchemist", init=False)
    description: str = field(
        default="Transform Negotiate to Attack 20 or vice versa.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# REGISTER ALL NEW POWERS
# ==============================================================================

# Quantum & Physics
AlienRegistry.register(Superposition())
AlienRegistry.register(Entangler())
AlienRegistry.register(WaveFunction())
AlienRegistry.register(Higgs())
AlienRegistry.register(Singularity())

# Nature & Biology
AlienRegistry.register(Mycelia())
AlienRegistry.register(Pollinator())
AlienRegistry.register(Apex())
AlienRegistry.register(Hibernator())
AlienRegistry.register(Camouflage())
AlienRegistry.register(Mimic())

# Technology & Machines
AlienRegistry.register(Compiler())
AlienRegistry.register(Firewall())
AlienRegistry.register(Debugger())
AlienRegistry.register(Overclocked())
AlienRegistry.register(Recursive())

# Social & Psychological
AlienRegistry.register(Empath())
AlienRegistry.register(Manipulator())
AlienRegistry.register(Pacifier())
AlienRegistry.register(Provocateur())
AlienRegistry.register(Gaslighter())

# Cosmic & Celestial
AlienRegistry.register(Nebula())
AlienRegistry.register(Pulsar())
AlienRegistry.register(Quasar())
AlienRegistry.register(Eclipse())
AlienRegistry.register(Supernova())

# Elemental & Primordial
AlienRegistry.register(Erosion())
AlienRegistry.register(Crystalline())
AlienRegistry.register(Magma())
AlienRegistry.register(Tempest())
AlienRegistry.register(Permafrost())

# Economic & Mercantile
AlienRegistry.register(Investor())
AlienRegistry.register(Monopolist())
AlienRegistry.register(Liquidator())
AlienRegistry.register(Arbiter())

# Mystical & Arcane
AlienRegistry.register(Augur())
AlienRegistry.register(Hexcaster())
AlienRegistry.register(Summoner())
AlienRegistry.register(Ritualist())
AlienRegistry.register(Alchemist())
