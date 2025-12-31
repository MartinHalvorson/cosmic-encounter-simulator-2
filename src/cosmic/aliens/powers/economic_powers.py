"""
Economic Powers - Aliens with trade, commerce, and resource abilities.
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
class Banker(AlienPower):
    """
    Banker - Card Storage.
    Store cards for later use.
    """
    name: str = field(default="Banker", init=False)
    description: str = field(default="Store cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Buyer(AlienPower):
    """
    Buyer - Purchase Power.
    Trade cards for ships.
    """
    name: str = field(default="Buyer", init=False)
    description: str = field(default="Trade cards for ships.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Capitalist(AlienPower):
    """
    Capitalist - Wealth Builder.
    Draw extra card per colony.
    """
    name: str = field(default="Capitalist", init=False)
    description: str = field(default="Card per colony.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Dealer(AlienPower):
    """
    Dealer - Card Dealer.
    Exchange cards with deck.
    """
    name: str = field(default="Dealer", init=False)
    description: str = field(default="Exchange with deck.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Entrepreneur(AlienPower):
    """
    Entrepreneur - Business Mind.
    +1 per card in hand.
    """
    name: str = field(default="Entrepreneur", init=False)
    description: str = field(default="+1 per card.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Exchanger(AlienPower):
    """
    Exchanger - Trade Master.
    Swap cards with any player.
    """
    name: str = field(default="Exchanger", init=False)
    description: str = field(default="Swap with anyone.", init=False)
    timing: PowerTiming = field(default=PowerTiming.PLANNING, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Hoarder(AlienPower):
    """
    Hoarder - Keep Everything.
    No hand limit.
    """
    name: str = field(default="Hoarder", init=False)
    description: str = field(default="No hand limit.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Importer(AlienPower):
    """
    Importer - Bring In Goods.
    Draw from any discard pile.
    """
    name: str = field(default="Importer", init=False)
    description: str = field(default="Draw from discards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Investor(AlienPower):
    """
    Investor - Long-term Gains.
    Cards grow in value over time.
    """
    name: str = field(default="Investor", init=False)
    description: str = field(default="Cards gain value.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Lender(AlienPower):
    """
    Lender - Give Cards.
    Loan cards with interest.
    """
    name: str = field(default="Lender", init=False)
    description: str = field(default="Loan cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Magnate(AlienPower):
    """
    Magnate - Business Leader.
    Control card flow.
    """
    name: str = field(default="Magnate", init=False)
    description: str = field(default="Control cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.GAIN_CARDS, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Moneylender(AlienPower):
    """
    Moneylender - Debt Collector.
    Take cards as payment.
    """
    name: str = field(default="Moneylender", init=False)
    description: str = field(default="Collect debts.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Monopolist(AlienPower):
    """
    Monopolist - Control Market.
    Limit opponent card draws.
    """
    name: str = field(default="Monopolist", init=False)
    description: str = field(default="Limit draws.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Pawnbroker(AlienPower):
    """
    Pawnbroker - Trade Items.
    Exchange anything for cards.
    """
    name: str = field(default="Pawnbroker", init=False)
    description: str = field(default="Trade for cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.ANY, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Profiteer(AlienPower):
    """
    Profiteer - Take Advantage.
    Gain from others' losses.
    """
    name: str = field(default="Profiteer", init=False)
    description: str = field(default="Gain from losses.", init=False)
    timing: PowerTiming = field(default=PowerTiming.RESOLUTION, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Seller(AlienPower):
    """
    Seller - Trade Ships.
    Exchange ships for cards.
    """
    name: str = field(default="Seller", init=False)
    description: str = field(default="Ships for cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REGROUP, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Speculator(AlienPower):
    """
    Speculator - Risk Taker.
    Double or nothing on cards.
    """
    name: str = field(default="Speculator", init=False)
    description: str = field(default="Double or nothing.", init=False)
    timing: PowerTiming = field(default=PowerTiming.REVEAL, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.RED, init=False)


@dataclass
class Taxman(AlienPower):
    """
    Taxman - Collect Taxes.
    Take card from each player per turn.
    """
    name: str = field(default="Taxman", init=False)
    description: str = field(default="Tax all players.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.YELLOW, init=False)


@dataclass
class Treasurer(AlienPower):
    """
    Treasurer - Card Manager.
    Organize and optimize hand.
    """
    name: str = field(default="Treasurer", init=False)
    description: str = field(default="Optimize hand.", init=False)
    timing: PowerTiming = field(default=PowerTiming.START_TURN, init=False)
    power_type: PowerType = field(default=PowerType.OPTIONAL, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


@dataclass
class Wealthy(AlienPower):
    """
    Wealthy - Rich Resources.
    Start with extra cards.
    """
    name: str = field(default="Wealthy", init=False)
    description: str = field(default="Extra starting cards.", init=False)
    timing: PowerTiming = field(default=PowerTiming.CONSTANT, init=False)
    power_type: PowerType = field(default=PowerType.MANDATORY, init=False)
    category: PowerCategory = field(default=PowerCategory.GREEN, init=False)


# Register all powers
AlienRegistry.register(Banker())
AlienRegistry.register(Buyer())
AlienRegistry.register(Capitalist())
AlienRegistry.register(Dealer())
AlienRegistry.register(Entrepreneur())
AlienRegistry.register(Exchanger())
AlienRegistry.register(Hoarder())
AlienRegistry.register(Importer())
AlienRegistry.register(Investor())
AlienRegistry.register(Lender())
AlienRegistry.register(Magnate())
AlienRegistry.register(Moneylender())
AlienRegistry.register(Monopolist())
AlienRegistry.register(Pawnbroker())
AlienRegistry.register(Profiteer())
AlienRegistry.register(Seller())
AlienRegistry.register(Speculator())
AlienRegistry.register(Taxman())
AlienRegistry.register(Treasurer())
AlienRegistry.register(Wealthy())
