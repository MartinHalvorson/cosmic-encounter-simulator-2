"""
Stealth Powers - Aliens with sneaky and covert abilities.
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
class Ambusher(AlienPower):
    """
    Ambusher - Surprise Attack.
    +5 when attacking from hidden position.
    """
    name: str = field(default="Ambusher", init=False)
    description: str = field(default="+5 surprise attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        """Add +5 when attacking."""
        if side == Side.OFFENSE:
            return total + 5
        return total


@dataclass
class Cloaker(AlienPower):
    """
    Cloaker - Invisibility.
    Your ships are hidden until reveal.
    """
    name: str = field(default="Cloaker", init=False)
    description: str = field(default="Hidden ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Concealer(AlienPower):
    """
    Concealer - Hidden Card.
    Opponent doesn't see your card value.
    """
    name: str = field(default="Concealer", init=False)
    description: str = field(default="Hidden card value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Creeper(AlienPower):
    """
    Creeper - Silent Movement.
    Move ships without being noticed.
    """
    name: str = field(default="Creeper", init=False)
    description: str = field(default="Silent movement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Disguiser(AlienPower):
    """
    Disguiser - False Identity.
    Appear as different alien until reveal.
    """
    name: str = field(default="Disguiser", init=False)
    description: str = field(default="False identity.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Eavesdropper(AlienPower):
    """
    Eavesdropper - Listen In.
    Hear all deals and negotiations.
    """
    name: str = field(default="Eavesdropper", init=False)
    description: str = field(default="Hear all deals.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Fader(AlienPower):
    """
    Fader - Phase Out.
    Ships avoid warp by fading.
    """
    name: str = field(default="Fader", init=False)
    description: str = field(default="Avoid warp.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ghostly(AlienPower):
    """
    Ghostly - Ethereal Form.
    Pass through defenses.
    """
    name: str = field(default="Ghostly", init=False)
    description: str = field(default="Pass defenses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hider(AlienPower):
    """
    Hider - Stay Hidden.
    Cannot be targeted while hidden.
    """
    name: str = field(default="Hider", init=False)
    description: str = field(default="Cannot be targeted.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Infiltrate(AlienPower):
    """
    Infiltrate - Secret Entry.
    Place ships on opponent planets secretly.
    """
    name: str = field(default="Infiltrate", init=False)
    description: str = field(default="Secret placement.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Invisible(AlienPower):
    """
    Invisible - Cannot Be Seen.
    Opponent cannot count your ships.
    """
    name: str = field(default="Invisible", init=False)
    description: str = field(default="Ships uncountable.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Masked(AlienPower):
    """
    Masked - Hidden Face.
    Power identity hidden until used.
    """
    name: str = field(default="Masked", init=False)
    description: str = field(default="Hidden power.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Ninja(AlienPower):
    """
    Ninja - Silent Warrior.
    Strike and disappear.
    """
    name: str = field(default="Ninja", init=False)
    description: str = field(default="Strike and vanish.", init=False)
    timing: PowerTiming = field(default=PowerTiming.WIN_ENCOUNTER, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Obscurer(AlienPower):
    """
    Obscurer - Fog of War.
    Hide all battle information.
    """
    name: str = field(default="Obscurer", init=False)
    description: str = field(default="Hide battle info.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Phantom_Alt(AlienPower):
    """
    Phantom_Alt - Ghost Form.
    Ships return from warp instantly.
    """
    name: str = field(default="Phantom_Alt", init=False)
    description: str = field(default="Instant warp return.", init=False)
    timing: PowerTiming = field(default=PowerTiming.SHIPS_TO_WARP, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Shade(AlienPower):
    """
    Shade - Dark Form.
    +3 when opponent has more ships.
    """
    name: str = field(default="Shade", init=False)
    description: str = field(default="+3 vs more ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Skulker(AlienPower):
    """
    Skulker - Hide in Shadows.
    Avoid being chosen by destiny.
    """
    name: str = field(default="Skulker", init=False)
    description: str = field(default="Avoid destiny.", init=False)
    timing: PowerTiming = field(default=PowerTiming.DESTINY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Sneak(AlienPower):
    """
    Sneak - Quiet Movement.
    Attack without warning.
    """
    name: str = field(default="Sneak", init=False)
    description: str = field(default="Surprise attack.", init=False)
    timing: PowerTiming = field(default=PowerTiming.LAUNCH, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Specter(AlienPower):
    """
    Specter - Ghostly Presence.
    Exist on multiple planets.
    """
    name: str = field(default="Specter", init=False)
    description: str = field(default="Multiple presence.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Spy_Alt(AlienPower):
    """
    Spy_Alt - Intelligence.
    See opponent's cards and plans.
    """
    name: str = field(default="Spy_Alt", init=False)
    description: str = field(default="See opponent plans.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Stealthy(AlienPower):
    """
    Stealthy - Silent Approach.
    Opponent can't invite allies.
    """
    name: str = field(default="Stealthy", init=False)
    description: str = field(default="Block ally invites.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ALLIANCE, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Vanisher(AlienPower):
    """
    Vanisher - Disappear.
    Remove self from encounter.
    """
    name: str = field(default="Vanisher", init=False)
    description: str = field(default="Leave encounter.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


# Register all powers
AlienRegistry.register(Ambusher())
AlienRegistry.register(Cloaker())
AlienRegistry.register(Concealer())
AlienRegistry.register(Creeper())
AlienRegistry.register(Disguiser())
AlienRegistry.register(Eavesdropper())
AlienRegistry.register(Fader())
AlienRegistry.register(Ghostly())
AlienRegistry.register(Hider())
AlienRegistry.register(Infiltrate())
AlienRegistry.register(Invisible())
AlienRegistry.register(Masked())
AlienRegistry.register(Ninja())
AlienRegistry.register(Obscurer())
AlienRegistry.register(Phantom_Alt())
AlienRegistry.register(Shade())
AlienRegistry.register(Skulker())
AlienRegistry.register(Sneak())
AlienRegistry.register(Specter())
AlienRegistry.register(Spy_Alt())
AlienRegistry.register(Stealthy())
AlienRegistry.register(Vanisher())
