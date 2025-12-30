"""
AI strategies for Cosmic Encounter.
"""

from .base import AIStrategy
from .basic_ai import BasicAI
from .strategic_ai import StrategicAI
from .random_ai import RandomAI

__all__ = [
    "AIStrategy",
    "BasicAI",
    "StrategicAI",
    "RandomAI",
]
