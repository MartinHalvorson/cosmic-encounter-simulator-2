"""
Mythology-themed alien powers.

Aliens inspired by mythological figures and creatures from
various world cultures and traditions.
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
# GREEK MYTHOLOGY
# ==============================================================================

@dataclass
class Zeus(AlienPower):
    """Zeus - Power of the Sky."""
    name: str = field(default="Zeus", init=False)
    description: str = field(
        default="When winning as offense, zap 1 opponent ally ship to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Poseidon(AlienPower):
    """Poseidon - Power of the Sea."""
    name: str = field(default="Poseidon", init=False)
    description: str = field(
        default="Commit ships from any number of your colonies.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Hades(AlienPower):
    """Hades - Power of the Underworld."""
    name: str = field(default="Hades", init=False)
    description: str = field(
        default="Use ships from warp for encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Athena(AlienPower):
    """Athena - Power of Wisdom."""
    name: str = field(default="Athena", init=False)
    description: str = field(
        default="See opponent's top 3 cards before selecting.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Apollo(AlienPower):
    """Apollo - Power of Light."""
    name: str = field(default="Apollo", init=False)
    description: str = field(
        default="Attack cards gain +2 per card in hand (max +8).",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ares(AlienPower):
    """Ares - Power of War."""
    name: str = field(default="Ares", init=False)
    description: str = field(
        default="Win: draw 1 card. Lose: retrieve 1 ship from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Medusa(AlienPower):
    """Medusa - Power to Petrify."""
    name: str = field(default="Medusa", init=False)
    description: str = field(
        default="After reveal, opponents cannot use reinforcements.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# NORSE MYTHOLOGY
# ==============================================================================

@dataclass
class Odin(AlienPower):
    """Odin - Power of All-Knowledge."""
    name: str = field(default="Odin", init=False)
    description: str = field(
        default="See destiny deck's top card before each encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Thor(AlienPower):
    """Thor - Power of Thunder."""
    name: str = field(default="Thor", init=False)
    description: str = field(
        default="Attack cards 20+ get +5 bonus.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Loki(AlienPower):
    """Loki - Power of Mischief."""
    name: str = field(default="Loki", init=False)
    description: str = field(
        default="Swap your encounter card with random opponent card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Freya(AlienPower):
    """Freya - Power of Love."""
    name: str = field(default="Freya", init=False)
    description: str = field(
        default="Allies who join your side draw 1 card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fenrir(AlienPower):
    """Fenrir - Power of the Wolf."""
    name: str = field(default="Fenrir", init=False)
    description: str = field(
        default="When winning as offense, devour 1 opponent ship forever.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Valkyrie(AlienPower):
    """Valkyrie - Power to Choose."""
    name: str = field(default="Valkyrie", init=False)
    description: str = field(
        default="Redirect 1 ship from warp to any colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# EGYPTIAN MYTHOLOGY
# ==============================================================================

@dataclass
class Ra(AlienPower):
    """Ra - Power of the Sun."""
    name: str = field(default="Ra", init=False)
    description: str = field(
        default="At turn start, all opponents discard lowest attack.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Anubis(AlienPower):
    """Anubis - Power of Death."""
    name: str = field(default="Anubis", init=False)
    description: str = field(
        default="Use ships from warp in encounters.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Isis_Myth(AlienPower):
    """Isis - Power of Magic."""
    name: str = field(default="Isis_Myth", init=False)
    description: str = field(
        default="Copy any alien power for one encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Osiris(AlienPower):
    """Osiris - Power of Resurrection."""
    name: str = field(default="Osiris", init=False)
    description: str = field(
        default="When losing, retrieve 2 ships from warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Sphinx(AlienPower):
    """Sphinx - Power of Riddles."""
    name: str = field(default="Sphinx", init=False)
    description: str = field(
        default="Name a value; if opponent played it, they discard it.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# ASIAN MYTHOLOGY
# ==============================================================================

@dataclass
class Dragon_Myth(AlienPower):
    """Dragon - Power of the Serpent."""
    name: str = field(default="Dragon_Myth", init=False)
    description: str = field(
        default="Ships count as 2 each, but max 2 ships per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kitsune(AlienPower):
    """Kitsune - Power of the Fox Spirit."""
    name: str = field(default="Kitsune", init=False)
    description: str = field(
        default="Swap attack and negotiate after cards are played.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Oni(AlienPower):
    """Oni - Power of the Demon."""
    name: str = field(default="Oni", init=False)
    description: str = field(
        default="Opponents must commit 2+ ships or auto-lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Tengu(AlienPower):
    """Tengu - Power of the Crow."""
    name: str = field(default="Tengu", init=False)
    description: str = field(
        default="When winning, steal 1 random card from loser.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kappa_Myth(AlienPower):
    """Kappa - Power of Water."""
    name: str = field(default="Kappa_Myth", init=False)
    description: str = field(
        default="Defending on home: +4 to total.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# CELTIC MYTHOLOGY
# ==============================================================================

@dataclass
class Morrigan(AlienPower):
    """Morrigan - Power of Battle."""
    name: str = field(default="Morrigan", init=False)
    description: str = field(
        default="See both players' top cards before encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Cernunnos(AlienPower):
    """Cernunnos - Power of the Wild."""
    name: str = field(default="Cernunnos", init=False)
    description: str = field(
        default="Turn start: place 1 ship from warp on colony.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Banshee(AlienPower):
    """Banshee - Power of the Wail."""
    name: str = field(default="Banshee", init=False)
    description: str = field(
        default="Redirect ships from warp to colony once per encounter.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# HINDU MYTHOLOGY
# ==============================================================================

@dataclass
class Vishnu(AlienPower):
    """Vishnu - Power of Preservation."""
    name: str = field(default="Vishnu", init=False)
    description: str = field(
        default="Prevent 1 ship per encounter from going to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shiva(AlienPower):
    """Shiva - Power of Destruction."""
    name: str = field(default="Shiva", init=False)
    description: str = field(
        default="When winning, remove 1 opponent ship from game entirely.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Ganesha(AlienPower):
    """Ganesha - Power of Obstacles."""
    name: str = field(default="Ganesha", init=False)
    description: str = field(
        default="Once per encounter, opponent must discard 1 card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Kali(AlienPower):
    """Kali - Power of Time."""
    name: str = field(default="Kali", init=False)
    description: str = field(
        default="Destroy all reinforcement cards after they are played.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Hanuman(AlienPower):
    """Hanuman - Power of Devotion."""
    name: str = field(default="Hanuman", init=False)
    description: str = field(
        default="+2 for each ally on your side.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# MESOAMERICAN MYTHOLOGY
# ==============================================================================

@dataclass
class Quetzalcoatl(AlienPower):
    """Quetzalcoatl - Power of the Feathered Serpent."""
    name: str = field(default="Quetzalcoatl", init=False)
    description: str = field(
        default="Ships count double in encounters you initiate.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    usable_as: List[PlayerRole] = field(
        default_factory=lambda: [PlayerRole.OFFENSE], init=False
    )


@dataclass
class Tezcatlipoca(AlienPower):
    """Tezcatlipoca - Power of the Smoking Mirror."""
    name: str = field(default="Tezcatlipoca", init=False)
    description: str = field(
        default="See opponent's hand before selecting your card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Huitzilopochtli(AlienPower):
    """Huitzilopochtli - Power of War."""
    name: str = field(default="Huitzilopochtli", init=False)
    description: str = field(
        default="Draw 1 card for each ship sent to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# SLAVIC MYTHOLOGY
# ==============================================================================

@dataclass
class Baba_Yaga(AlienPower):
    """Baba Yaga - Power of the Witch."""
    name: str = field(default="Baba_Yaga", init=False)
    description: str = field(
        default="Force opponent to play their lowest or highest card.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Perun(AlienPower):
    """Perun - Power of Thunder."""
    name: str = field(default="Perun", init=False)
    description: str = field(
        default="+3 when you have more cards than opponent.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# ==============================================================================
# POLYNESIAN MYTHOLOGY
# ==============================================================================

@dataclass
class Maui(AlienPower):
    """Maui - Power of the Trickster."""
    name: str = field(default="Maui", init=False)
    description: str = field(
        default="Steal 1 card from opponent when you lose.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pele(AlienPower):
    """Pele - Power of Volcanoes."""
    name: str = field(default="Pele", init=False)
    description: str = field(
        default="When losing, send 1 opponent ally ship to warp.",
        init=False
    )
    timing: PowerTiming = field(default=PowerTiming.LOSE_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# ==============================================================================
# REGISTER ALL MYTHOLOGY POWERS
# ==============================================================================

# Greek
AlienRegistry.register(Zeus())
AlienRegistry.register(Poseidon())
AlienRegistry.register(Hades())
AlienRegistry.register(Athena())
AlienRegistry.register(Apollo())
AlienRegistry.register(Ares())
AlienRegistry.register(Medusa())

# Norse
AlienRegistry.register(Odin())
AlienRegistry.register(Thor())
AlienRegistry.register(Loki())
AlienRegistry.register(Freya())
AlienRegistry.register(Fenrir())
AlienRegistry.register(Valkyrie())

# Egyptian
AlienRegistry.register(Ra())
AlienRegistry.register(Anubis())
AlienRegistry.register(Isis_Myth())
AlienRegistry.register(Osiris())
AlienRegistry.register(Sphinx())

# Asian
AlienRegistry.register(Dragon_Myth())
AlienRegistry.register(Kitsune())
AlienRegistry.register(Oni())
AlienRegistry.register(Tengu())
AlienRegistry.register(Kappa_Myth())

# Celtic
AlienRegistry.register(Morrigan())
AlienRegistry.register(Cernunnos())
AlienRegistry.register(Banshee())

# Hindu
AlienRegistry.register(Vishnu())
AlienRegistry.register(Shiva())
AlienRegistry.register(Ganesha())
AlienRegistry.register(Kali())
AlienRegistry.register(Hanuman())

# Mesoamerican
AlienRegistry.register(Quetzalcoatl())
AlienRegistry.register(Tezcatlipoca())
AlienRegistry.register(Huitzilopochtli())

# Slavic
AlienRegistry.register(Baba_Yaga())
AlienRegistry.register(Perun())

# Polynesian
AlienRegistry.register(Maui())
AlienRegistry.register(Pele())
