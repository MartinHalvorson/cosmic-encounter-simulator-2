"""
Cosmic Phenomenon alien powers.

These aliens represent cosmic events and phenomena.
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
class Aurora(AlienPower):
    """Aurora - Power of Light. Add +2 for each different color ship in the encounter."""
    name: str = field(default="Aurora", init=False)
    description: str = field(default="+2 for each different player's ships in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ship_dict = game.offense_ships if side == Side.OFFENSE else game.defense_ships
        unique_players = len([k for k, v in ship_dict.items() if v > 0])
        return total + (unique_players * 2)


@dataclass
class Supermassive(AlienPower):
    """Supermassive - Power of Gravity. Pull 2 ships from each opponent's colonies to the warp at turn start."""
    name: str = field(default="Supermassive", init=False)
    description: str = field(default="At turn start, each opponent loses 2 ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        if not player.power_active or player != game.offense:
            return
        for p in game.players:
            if p != player:
                taken = p.get_ships_from_colonies(2, game.planets, exclude_last_ship=True)
                p.send_ships_to_warp(taken)


@dataclass
class Flare_Entity(AlienPower):
    """Flare - Power of Eruption. +5 to total but lose 2 ships to warp."""
    name: str = field(default="Flare_Entity", init=False)
    description: str = field(default="+5 to total but lose 2 ships to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        # Trade ships for power
        if player.total_ships_in_play(game.planets) >= 2:
            player.get_ships_from_colonies(2, game.planets)
            player.send_ships_to_warp(2)
            return total + 5
        return total


@dataclass
class Radiation(AlienPower):
    """Radiation - Power of Decay. Opponent's ships count as 0.5 each (rounded down)."""
    name: str = field(default="Radiation", init=False)
    description: str = field(default="Opponent's ships count as half value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class GammaRay(AlienPower):
    """GammaRay - Power of Burst. Double attack card value but discard hand after."""
    name: str = field(default="GammaRay", init=False)
    description: str = field(default="Double attack card value, then discard hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)

    def modify_attack_value(self, game: "Game", player: "Player", value: int, side: Side) -> int:
        if not player.power_active:
            return value
        return value * 2


@dataclass
class Magnetar(AlienPower):
    """Magnetar - Power of Attraction. Draw 1 card at start of each encounter."""
    name: str = field(default="Magnetar", init=False)
    description: str = field(default="Draw 1 card at start of each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        if player.power_active:
            card = game.cosmic_deck.draw()
            if card:
                player.add_card(card)


@dataclass
class Cosmic_Ray(AlienPower):
    """Cosmic_Ray - Power of Penetration. Ignore 5 points of opponent's attack value."""
    name: str = field(default="Cosmic_Ray", init=False)
    description: str = field(default="Reduce opponent's attack value by 5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class DarkMatter(AlienPower):
    """DarkMatter - Power of Mystery. Opponent cannot see your encounter card until reveal."""
    name: str = field(default="DarkMatter", init=False)
    description: str = field(default="Your encounter card is hidden from all effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class DarkEnergy(AlienPower):
    """DarkEnergy - Power of Expansion. +1 per foreign colony you have."""
    name: str = field(default="DarkEnergy", init=False)
    description: str = field(default="+1 to total for each foreign colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        colonies = player.count_foreign_colonies(game.planets)
        return total + colonies


@dataclass
class Neutrino(AlienPower):
    """Neutrino - Power of Passage. Your ships cannot be stopped from landing on planets."""
    name: str = field(default="Neutrino", init=False)
    description: str = field(default="Ships always land even on lost encounters.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Antimatter_Cosmic(AlienPower):
    """Antimatter_Cosmic - Power of Annihilation. When you win, loser's ships are eliminated, not sent to warp."""
    name: str = field(default="Antimatter_Cosmic", init=False)
    description: str = field(default="Losing ships are eliminated, not sent to warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Photon(AlienPower):
    """Photon - Power of Speed. Take two encounters per turn instead of one."""
    name: str = field(default="Photon", init=False)
    description: str = field(default="Always have two encounters per turn.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Quark(AlienPower):
    """Quark - Power of Duality. Ships count as 2 when alone, 0.5 when in groups."""
    name: str = field(default="Quark", init=False)
    description: str = field(default="Ships count as 2 when you're the only one on your side.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        if not player.power_active:
            return count
        ship_dict = game.offense_ships if side == Side.OFFENSE else game.defense_ships
        unique_players = len([k for k, v in ship_dict.items() if v > 0])
        if unique_players == 1:
            return count * 2
        return count


@dataclass
class Boson(AlienPower):
    """Boson - Power of Force. Ships committed to encounter cannot be removed by any effect."""
    name: str = field(default="Boson", init=False)
    description: str = field(default="Committed ships cannot be removed by effects.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fermion(AlienPower):
    """Fermion - Power of Exclusion. Only you can have ships on planets you occupy."""
    name: str = field(default="Fermion", init=False)
    description: str = field(default="Other players cannot land on your colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Gluon(AlienPower):
    """Gluon - Power of Binding. Allied ships cannot leave your side once committed."""
    name: str = field(default="Gluon", init=False)
    description: str = field(default="Allies cannot switch sides or withdraw.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lepton(AlienPower):
    """Lepton - Power of Light Mass. Ships count as 0 but you may commit up to 8."""
    name: str = field(default="Lepton", init=False)
    description: str = field(default="Commit up to 8 ships but they count as 0.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hadron(AlienPower):
    """Hadron - Power of Mass. Your ships each count as 3 in combat."""
    name: str = field(default="Hadron", init=False)
    description: str = field(default="Ships count as 3 each in combat.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        if not player.power_active:
            return count
        return count * 3


@dataclass
class Tachyon(AlienPower):
    """Tachyon - Power of Future. See opponent's card before playing your own."""
    name: str = field(default="Tachyon", init=False)
    description: str = field(default="Opponent must reveal card first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Graviton_Wave(AlienPower):
    """Graviton_Wave - Power of Waves. Move 1 ship from warp to any colony at encounter start."""
    name: str = field(default="Graviton_Wave", init=False)
    description: str = field(default="Retrieve 1 ship from warp at encounter start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        if player.power_active and player.ships_in_warp > 0:
            player.retrieve_ships_from_warp(1)
            player.return_ships_to_colonies(1, player.home_planets)


@dataclass
class Entropy(AlienPower):
    """Entropy - Power of Decay. At end of each turn, all players lose 1 ship from largest colony."""
    name: str = field(default="Entropy", init=False)
    description: str = field(default="At end of turn, all players lose 1 ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Higgs(AlienPower):
    """Higgs - Power of Mass Generation. Give any player's ships +1 value each."""
    name: str = field(default="Higgs", init=False)
    description: str = field(default="Your ships always count as +1 each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        if not player.power_active:
            return count
        return count + count  # Double the ship bonus


@dataclass
class Helix(AlienPower):
    """Helix - Power of Spirals. Draw 2 cards, discard 1 at start of each encounter."""
    name: str = field(default="Helix", init=False)
    description: str = field(default="Draw 2 cards, discard 1 each encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_encounter_start(self, game: "Game", player: "Player") -> None:
        if not player.power_active:
            return
        cards = game.cosmic_deck.draw_multiple(2)
        if cards:
            player.add_cards(cards)
            # Discard worst card
            if player.hand:
                worst = min(player.hand, key=lambda c: getattr(c, 'value', 0) if hasattr(c, 'value') else 0)
                player.remove_card(worst)
                game.cosmic_deck.discard(worst)


@dataclass
class Prism(AlienPower):
    """Prism - Power of Splitting. May split attack card value between offense and defense."""
    name: str = field(default="Prism", init=False)
    description: str = field(default="Split card value to add half to each side's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Mirror_Alt(AlienPower):
    """Mirror_Alt - Power of Reflection. Copy opponent's attack card value."""
    name: str = field(default="Mirror_Alt", init=False)
    description: str = field(default="Use opponent's attack card value instead of yours.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Lens(AlienPower):
    """Lens - Power of Focus. +10 if you have only 1 ship in encounter."""
    name: str = field(default="Lens", init=False)
    description: str = field(default="+10 if you have exactly 1 ship in encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ship_dict = game.offense_ships if side == Side.OFFENSE else game.defense_ships
        my_ships = ship_dict.get(player.name, 0)
        if my_ships == 1:
            return total + 10
        return total


@dataclass
class Spectrum(AlienPower):
    """Spectrum - Power of Variety. +1 for each different card type in hand."""
    name: str = field(default="Spectrum", init=False)
    description: str = field(default="+1 for each different card type in hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        card_types = set(type(c).__name__ for c in player.hand)
        return total + len(card_types)


@dataclass
class Parallax_Alt(AlienPower):
    """Parallax_Alt - Power of Perspective. See both encounter cards before resolution."""
    name: str = field(default="Parallax_Alt", init=False)
    description: str = field(default="May change your card after seeing opponent's.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Zenith(AlienPower):
    """Zenith - Power of Peak. Double your total if you're at 4 foreign colonies."""
    name: str = field(default="Zenith", init=False)
    description: str = field(default="Double total when at 4 foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        colonies = player.count_foreign_colonies(game.planets)
        if colonies == 4:
            return total * 2
        return total


@dataclass
class Nadir(AlienPower):
    """Nadir - Power of Low. Double total when at 0 foreign colonies."""
    name: str = field(default="Nadir", init=False)
    description: str = field(default="Double total when at 0 foreign colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        colonies = player.count_foreign_colonies(game.planets)
        if colonies == 0:
            return total * 2
        return total


@dataclass
class Corona(AlienPower):
    """Corona - Power of Halo. +3 for each home planet with colonies intact."""
    name: str = field(default="Corona", init=False)
    description: str = field(default="+3 for each home planet you still control.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        home_count = sum(1 for p in player.home_planets if p.has_colony(player.name))
        return total + (home_count * 3)


@dataclass
class Prominence(AlienPower):
    """Prominence - Power of Reach. Attack any planet, ignoring destiny."""
    name: str = field(default="Prominence", init=False)
    description: str = field(default="Choose any planet to attack, ignore destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all phenomenon powers
AlienRegistry.register(Aurora())
AlienRegistry.register(Supermassive())
AlienRegistry.register(Flare_Entity())
AlienRegistry.register(Radiation())
AlienRegistry.register(GammaRay())
AlienRegistry.register(Magnetar())
AlienRegistry.register(Cosmic_Ray())
AlienRegistry.register(DarkMatter())
AlienRegistry.register(DarkEnergy())
AlienRegistry.register(Neutrino())
AlienRegistry.register(Antimatter_Cosmic())
AlienRegistry.register(Photon())
AlienRegistry.register(Quark())
AlienRegistry.register(Boson())
AlienRegistry.register(Fermion())
AlienRegistry.register(Gluon())
AlienRegistry.register(Lepton())
AlienRegistry.register(Hadron())
AlienRegistry.register(Tachyon())
AlienRegistry.register(Graviton_Wave())
AlienRegistry.register(Entropy())
AlienRegistry.register(Higgs())
AlienRegistry.register(Helix())
AlienRegistry.register(Prism())
AlienRegistry.register(Mirror_Alt())
AlienRegistry.register(Lens())
AlienRegistry.register(Spectrum())
AlienRegistry.register(Parallax_Alt())
AlienRegistry.register(Zenith())
AlienRegistry.register(Nadir())
AlienRegistry.register(Corona())
AlienRegistry.register(Prominence())
