"""
Social media platform themed alien powers.
"""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING
import random

from ..base import AlienPower, PowerCategory
from ..registry import AlienRegistry
from ...types import PowerTiming, PowerType, Side

if TYPE_CHECKING:
    from ...game import Game
    from ...player import Player


@dataclass
class Tweet(AlienPower):
    """Tweet - Power of Brevity. Short but impactful."""
    name: str = field(default="Tweet", init=False)
    description: str = field(default="+4 with 3 or fewer cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) <= 3:
            return total + 4
        return total


@dataclass
class Post(AlienPower):
    """Post - Power of Content. Share with all."""
    name: str = field(default="Post_Social", init=False)
    description: str = field(default="+3 constant.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3
        return total


@dataclass
class Story(AlienPower):
    """Story - Power of Ephemera. Temporary impact."""
    name: str = field(default="Story_Social", init=False)
    description: str = field(default="+5 on odd turns.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and game.current_turn % 2 == 1:
            return total + 5
        return total


@dataclass
class Reel(AlienPower):
    """Reel - Power of Virality. Spread quickly."""
    name: str = field(default="Reel", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Like(AlienPower):
    """Like - Power of Approval. Gain support."""
    name: str = field(default="Like", init=False)
    description: str = field(default="+2 per ally (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        return total + min(8, ally_count * 2)


@dataclass
class Share(AlienPower):
    """Share - Power of Distribution. Spread the word."""
    name: str = field(default="Share_Social", init=False)
    description: str = field(default="+3 with allies.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count > 0:
            return total + 3
        return total


@dataclass
class Follow(AlienPower):
    """Follow - Power of Connection. Build network."""
    name: str = field(default="Follow", init=False)
    description: str = field(default="+1 per colony (max +5).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            colonies = player.count_foreign_colonies(game.planets)
            return total + min(5, colonies)
        return total


@dataclass
class Hashtag(AlienPower):
    """Hashtag - Power of Trending. Gain momentum."""
    name: str = field(default="Hashtag", init=False)
    description: str = field(default="+1 per turn (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, game.current_turn)
        return total


@dataclass
class DM(AlienPower):
    """DM - Power of Privacy. Secret communication."""
    name: str = field(default="DM", init=False)
    description: str = field(default="+4 when alone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if not player.power_active:
            return total
        ally_count = 0
        if side == Side.OFFENSE:
            ally_count = len([p for p in game.offense_allies if p != player.name])
        else:
            ally_count = len([p for p in game.defense_allies if p != player.name])
        if ally_count == 0:
            return total + 4
        return total


@dataclass
class Viral(AlienPower):
    """Viral - Power of Spread. Exponential growth."""
    name: str = field(default="Viral", init=False)
    description: str = field(default="+2 that doubles each turn (max +8).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)
    bonus: int = 2

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            result = total + self.bonus
            self.bonus = min(8, self.bonus * 2)
            return result
        return total


@dataclass
class Block(AlienPower):
    """Block - Power of Exclusion. Keep enemies out."""
    name: str = field(default="Block_Social", init=False)
    description: str = field(default="+5 when defending.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.DEFENSE:
            return total + 5
        return total


@dataclass
class Meme(AlienPower):
    """Meme - Power of Humor. Unexpected impact."""
    name: str = field(default="Meme", init=False)
    description: str = field(default="+3 plus random +0-3.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + 3 + random.randint(0, 3)
        return total


@dataclass
class Influencer(AlienPower):
    """Influencer - Power of Sway. Shape opinions."""
    name: str = field(default="Influencer", init=False)
    description: str = field(default="+4 with 5+ cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and len(player.hand) >= 5:
            return total + 4
        return total


@dataclass
class Troll(AlienPower):
    """Troll - Power of Disruption. Cause chaos."""
    name: str = field(default="Troll_Social", init=False)
    description: str = field(default="+4 when attacking.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active and side == Side.OFFENSE:
            return total + 4
        return total


@dataclass
class Feed(AlienPower):
    """Feed - Power of Stream. Constant flow."""
    name: str = field(default="Feed", init=False)
    description: str = field(default="+1 per card (max +6).", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)

    def modify_total(self, game: "Game", player: "Player", total: int, side: Side) -> int:
        if player.power_active:
            return total + min(6, len(player.hand))
        return total


SOCIAL_MEDIA_PLATFORM_POWERS = [
    Tweet, Post, Story, Reel, Like, Share, Follow, Hashtag, DM, Viral,
    Block, Meme, Influencer, Troll, Feed
]

for power_class in SOCIAL_MEDIA_PLATFORM_POWERS:
    try:
        AlienRegistry.register(power_class())
    except ValueError:
        pass
