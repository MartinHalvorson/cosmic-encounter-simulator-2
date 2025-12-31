"""
Arcane Powers - Mystical and magical alien abilities.

These powers focus on manipulation, prediction, and supernatural effects.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, PlayerRole, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Alchemist(AlienPower):
    """
    Alchemist - Transmuter.
    Once per encounter, you may treat your attack card as having +10 value.
    """
    name: str = field(default="Alchemist", init=False)
    description: str = field(default="Boost attack card by +10 once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +10 to attack."""
        return total + 10


@dataclass
class Astrologer(AlienPower):
    """
    Astrologer - Star Reader.
    Before the encounter card reveal, you may look at your opponent's card.
    """
    name: str = field(default="Astrologer", init=False)
    description: str = field(default="See opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Conjurer(AlienPower):
    """
    Conjurer - Summoner.
    When you win an encounter, you may retrieve 2 ships from the warp.
    """
    name: str = field(default="Conjurer", init=False)
    description: str = field(default="Retrieve 2 ships when winning.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Diviner(AlienPower):
    """
    Diviner - Future Seer.
    At the start of each encounter, look at the top destiny card.
    """
    name: str = field(default="Diviner", init=False)
    description: str = field(default="Peek at next destiny card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Enchanter(AlienPower):
    """
    Enchanter - Charmer.
    When inviting allies, one player you invite must accept.
    """
    name: str = field(default="Enchanter", init=False)
    description: str = field(default="Force one invited player to ally.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Exorcist(AlienPower):
    """
    Exorcist - Spirit Banisher.
    Once per encounter, cancel the effects of one alien power.
    """
    name: str = field(default="Exorcist", init=False)
    description: str = field(default="Cancel one alien power per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Geomancer(AlienPower):
    """
    Geomancer - Earth Shaper.
    Ships on your home planets count +1 each for defense.
    """
    name: str = field(default="Geomancer", init=False)
    description: str = field(default="Home planet ships count +1 for defense.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        """Boost ships on home planets."""
        if side == Side.DEFENSE and game.defense_planet and game.defense_planet.owner == player:
            # Each ship counts as 1.5 (rounded)
            return int(count * 1.5)
        return count


@dataclass
class Hexer(AlienPower):
    """
    Hexer - Curse Layer.
    Before reveal, curse one player to reduce their total by 3.
    """
    name: str = field(default="Hexer", init=False)
    description: str = field(default="Reduce one player's total by 3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Illusory(AlienPower):
    """
    Illusory - False Image.
    Your encounter card is revealed last, after seeing opponent's.
    """
    name: str = field(default="Illusory", init=False)
    description: str = field(default="Reveal encounter card last.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Jinx(AlienPower):
    """
    Jinx - Bad Luck Bringer.
    Once per encounter, force opponent to discard their encounter card and play another.
    """
    name: str = field(default="Jinx", init=False)
    description: str = field(default="Force opponent to change encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kineticist(AlienPower):
    """
    Kineticist - Mind Mover.
    Once per encounter, move 2 ships from any planet to any colony you have.
    """
    name: str = field(default="Kineticist", init=False)
    description: str = field(default="Move 2 ships between colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Luminary(AlienPower):
    """
    Luminary - Light Bringer.
    Your allies get +1 to their ship count contribution.
    """
    name: str = field(default="Luminary", init=False)
    description: str = field(default="Allies contribute +1 ship each.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Mesmerist(AlienPower):
    """
    Mesmerist - Hypnotist.
    Once per encounter, look at and rearrange top 3 cards of cosmic deck.
    """
    name: str = field(default="Mesmerist", init=False)
    description: str = field(default="Rearrange top 3 cards of cosmic deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Necromancer(AlienPower):
    """
    Necromancer - Dead Raiser.
    Once per encounter, retrieve a discarded encounter card to your hand.
    """
    name: str = field(default="Necromancer", init=False)
    description: str = field(default="Take discarded encounter card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Occultist(AlienPower):
    """
    Occultist - Secret Keeper.
    When you lose, you may keep your encounter card secret (don't discard).
    """
    name: str = field(default="Occultist", init=False)
    description: str = field(default="Keep encounter card when losing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Prestidigitator(AlienPower):
    """
    Prestidigitator - Sleight of Hand.
    After cards are revealed, swap your encounter card with one from your hand.
    """
    name: str = field(default="Prestidigitator", init=False)
    description: str = field(default="Swap encounter card after reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pyromancer(AlienPower):
    """
    Pyromancer - Fire Wielder.
    When you win, destroy one opponent's ship permanently (to box, not warp).
    """
    name: str = field(default="Pyromancer", init=False)
    description: str = field(default="Destroy one ship permanently on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ritualist(AlienPower):
    """
    Ritualist - Ceremony Performer.
    At the start of your turn, you may discard 2 cards to draw 3.
    """
    name: str = field(default="Ritualist", init=False)
    description: str = field(default="Discard 2, draw 3 at turn start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def on_turn_start(self, game: "Game", player: "Player") -> None:
        """Optionally swap cards."""
        if len(player.hand) >= 2:
            # Discard 2 random cards
            for _ in range(2):
                if player.hand:
                    card = random.choice(player.hand)
                    player.hand.remove(card)
                    game.cosmic_deck.discard(card)
            # Draw 3
            for _ in range(3):
                card = game.cosmic_deck.draw()
                if card:
                    player.add_card(card)


@dataclass
class Shaman(AlienPower):
    """
    Shaman - Spirit Guide.
    Your allies may draw 1 card when joining your side.
    """
    name: str = field(default="Shaman", init=False)
    description: str = field(default="Allies draw 1 card when joining.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sorcerer(AlienPower):
    """
    Sorcerer - Spell Caster.
    Once per encounter, swap your encounter card with opponent's.
    """
    name: str = field(default="Sorcerer", init=False)
    description: str = field(default="Swap encounter cards with opponent.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Spellbinder(AlienPower):
    """
    Spellbinder - Magic Sealer.
    When defending, opponent cannot use their alien power.
    """
    name: str = field(default="Spellbinder", init=False)
    description: str = field(default="Block opponent's power when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Thaumaturge(AlienPower):
    """
    Thaumaturge - Wonder Worker.
    Once per encounter, add +4 to any side's total.
    """
    name: str = field(default="Thaumaturge", init=False)
    description: str = field(default="Add +4 to any side's total.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Warlock(AlienPower):
    """
    Warlock - Dark Pact Maker.
    Once per encounter, force one player to discard a card.
    """
    name: str = field(default="Warlock", init=False)
    description: str = field(default="Force player to discard one card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Witch(AlienPower):
    """
    Witch - Potion Brewer.
    At the start of each encounter, you may heal 1 ship from the warp.
    """
    name: str = field(default="Witch", init=False)
    description: str = field(default="Retrieve 1 ship at encounter start.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wizard(AlienPower):
    """
    Wizard - Arcane Master.
    You may play two encounter cards, using the higher value.
    """
    name: str = field(default="Wizard", init=False)
    description: str = field(default="Play two cards, use higher value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Alchemist())
AlienRegistry.register(Astrologer())
AlienRegistry.register(Conjurer())
AlienRegistry.register(Diviner())
AlienRegistry.register(Enchanter())
AlienRegistry.register(Exorcist())
AlienRegistry.register(Geomancer())
AlienRegistry.register(Hexer())
AlienRegistry.register(Illusory())
AlienRegistry.register(Jinx())
AlienRegistry.register(Kineticist())
AlienRegistry.register(Luminary())
AlienRegistry.register(Mesmerist())
AlienRegistry.register(Necromancer())
AlienRegistry.register(Occultist())
AlienRegistry.register(Prestidigitator())
AlienRegistry.register(Pyromancer())
AlienRegistry.register(Ritualist())
AlienRegistry.register(Shaman())
AlienRegistry.register(Sorcerer())
AlienRegistry.register(Spellbinder())
AlienRegistry.register(Thaumaturge())
AlienRegistry.register(Warlock())
AlienRegistry.register(Witch())
AlienRegistry.register(Wizard())
