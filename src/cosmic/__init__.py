"""
Cosmic Encounter Simulator

A comprehensive simulation of the board game Cosmic Encounter.
"""

__version__ = "2.0.0"

from .game import Game
from .player import Player
from .simulation.runner import Simulator

__all__ = ["Game", "Player", "Simulator"]
