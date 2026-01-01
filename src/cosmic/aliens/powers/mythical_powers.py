"""
Mythical Powers - Aliens based on fantasy creatures and mythology.
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
class Centaur(AlienPower):
    """
    Centaur - Half-Human Half-Horse.
    You may commit ships from 2 different colonies.
    """
    name: str = field(default="Centaur", init=False)
    description: str = field(default="Commit from 2 colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Chimera(AlienPower):
    """
    Chimera - Multi-Headed Beast.
    Use powers of 3 different aliens from the discard pile.
    """
    name: str = field(default="Chimera", init=False)
    description: str = field(default="Use 3 discarded alien powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Cyclops(AlienPower):
    """
    Cyclops - One-Eyed Giant.
    Attack cards played against you are at -5.
    """
    name: str = field(default="Cyclops", init=False)
    description: str = field(default="Opponent attack cards -5.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Djinn(AlienPower):
    """
    Djinn - Wish Granter.
    Once per game, force any outcome for an encounter.
    """
    name: str = field(default="Djinn", init=False)
    description: str = field(default="Force encounter outcome once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Fairy(AlienPower):
    """
    Fairy - Tiny Magical Being.
    Negotiate cards in your hand become attack 12s.
    """
    name: str = field(default="Fairy", init=False)
    description: str = field(default="Negotiate cards become attack 12.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Giant(AlienPower):
    """
    Giant - Massive Humanoid.
    Each of your ships counts as 2.
    """
    name: str = field(default="Giant", init=False)
    description: str = field(default="Ships count as 2.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_ship_count(self, game: "Game", player: "Player", count: int, side: Side) -> int:
        """Double ship count."""
        return count * 2


@dataclass
class Gnome(AlienPower):
    """
    Gnome - Earth Spirit.
    When defending, retrieve 1 ship from warp automatically.
    """
    name: str = field(default="Gnome", init=False)
    description: str = field(default="Retrieve ship when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Griffin(AlienPower):
    """
    Griffin - Eagle-Lion.
    You may attack any player regardless of destiny.
    """
    name: str = field(default="Griffin", init=False)
    description: str = field(default="Attack any player.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Harpy(AlienPower):
    """
    Harpy - Winged Terror.
    Before cards are revealed, steal opponent's encounter card.
    """
    name: str = field(default="Harpy", init=False)
    description: str = field(default="Steal opponent's card before reveal.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hydra(AlienPower):
    """
    Hydra - Multi-Headed Serpent.
    When you lose ships, return half (rounded up) to colonies.
    """
    name: str = field(default="Hydra", init=False)
    description: str = field(default="Half ships return to colonies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Kraken(AlienPower):
    """
    Kraken - Sea Monster.
    Win ties and opponent must commit max ships.
    """
    name: str = field(default="Kraken", init=False)
    description: str = field(default="Win ties, opponent max ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Leprechaun(AlienPower):
    """
    Leprechaun - Lucky Trickster.
    When you play a negotiate, draw 2 cards.
    """
    name: str = field(default="Leprechaun", init=False)
    description: str = field(default="Draw 2 on negotiate.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Manticore(AlienPower):
    """
    Manticore - Scorpion-Lion.
    When you win, opponent loses 1 additional ship.
    """
    name: str = field(default="Manticore", init=False)
    description: str = field(default="Win: opponent loses 1 extra ship.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Medusa(AlienPower):
    """
    Medusa - Stone Gaze.
    Ships lost to you are removed from game instead of warp.
    """
    name: str = field(default="Medusa", init=False)
    description: str = field(default="Lost ships removed from game.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Mermaid(AlienPower):
    """
    Mermaid - Ocean Singer.
    Allies invited by you must join or lose a ship.
    """
    name: str = field(default="Mermaid", init=False)
    description: str = field(default="Invited allies must join.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Minotaur(AlienPower):
    """
    Minotaur - Labyrinth Dweller.
    When defending, +5 to your total.
    """
    name: str = field(default="Minotaur", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when defending."""
        if side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Nymph(AlienPower):
    """
    Nymph - Nature Spirit.
    Once per encounter, look at any player's hand.
    """
    name: str = field(default="Nymph", init=False)
    description: str = field(default="Look at hand once per encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ogre(AlienPower):
    """
    Ogre - Brutish Monster.
    Attack cards 06 or less become 10.
    """
    name: str = field(default="Ogre", init=False)
    description: str = field(default="Low attack cards become 10.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Pegasus(AlienPower):
    """
    Pegasus - Winged Horse.
    You may have a second encounter after any result.
    """
    name: str = field(default="Pegasus", init=False)
    description: str = field(default="Second encounter after any result.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Phoenix_Alt(AlienPower):
    """
    Phoenix_Alt - Reborn Bird.
    When you lose, retrieve all ships from warp.
    """
    name: str = field(default="Phoenix_Alt", init=False)
    description: str = field(default="Retrieve all ships on loss.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sphinx(AlienPower):
    """
    Sphinx - Riddle Keeper.
    Before reveal, opponent must state their card value.
    """
    name: str = field(default="Sphinx", init=False)
    description: str = field(default="Opponent states card value first.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Troll(AlienPower):
    """
    Troll - Bridge Guardian.
    When defending on home planet, +8 to total.
    """
    name: str = field(default="Troll", init=False)
    description: str = field(default="+8 defending home planet.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Unicorn(AlienPower):
    """
    Unicorn - Pure Creature.
    Immune to other players' powers.
    """
    name: str = field(default="Unicorn", init=False)
    description: str = field(default="Immune to powers.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vampire(AlienPower):
    """
    Vampire - Blood Drinker.
    When you win, take 1 card from opponent's hand.
    """
    name: str = field(default="Vampire", init=False)
    description: str = field(default="Take card on win.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Werewolf(AlienPower):
    """
    Werewolf - Shapeshifter.
    Once per turn, swap encounter cards with opponent.
    """
    name: str = field(default="Werewolf", init=False)
    description: str = field(default="Swap encounter cards once.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Yeti(AlienPower):
    """
    Yeti - Mountain Beast.
    Opponent cannot invite allies against you.
    """
    name: str = field(default="Yeti", init=False)
    description: str = field(default="Block opponent allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Centaur())
AlienRegistry.register(Chimera())
AlienRegistry.register(Cyclops())
AlienRegistry.register(Djinn())
AlienRegistry.register(Fairy())
AlienRegistry.register(Giant())
AlienRegistry.register(Gnome())
AlienRegistry.register(Griffin())
AlienRegistry.register(Harpy())
AlienRegistry.register(Hydra())
AlienRegistry.register(Kraken())
AlienRegistry.register(Leprechaun())
AlienRegistry.register(Manticore())
AlienRegistry.register(Medusa())
AlienRegistry.register(Mermaid())
AlienRegistry.register(Minotaur())
AlienRegistry.register(Nymph())
AlienRegistry.register(Ogre())
AlienRegistry.register(Pegasus())
AlienRegistry.register(Phoenix_Alt())
AlienRegistry.register(Sphinx())
AlienRegistry.register(Troll())
AlienRegistry.register(Unicorn())
AlienRegistry.register(Vampire())
AlienRegistry.register(Werewolf())
AlienRegistry.register(Yeti())
