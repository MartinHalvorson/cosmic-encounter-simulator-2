"""
Registry for alien powers.
"""

from typing import Dict, List, Optional, Type
from .base import AlienPower


class AlienRegistry:
    """
    Registry for all available alien powers.
    Aliens are registered by name and can be retrieved for game setup.
    """
    _aliens: Dict[str, AlienPower] = {}

    @classmethod
    def register(cls, alien: AlienPower) -> None:
        """Register an alien power."""
        cls._aliens[alien.name.lower()] = alien

    @classmethod
    def get(cls, name: str) -> Optional[AlienPower]:
        """Get an alien power by name (case-insensitive)."""
        return cls._aliens.get(name.lower())

    @classmethod
    def get_all(cls) -> List[AlienPower]:
        """Get all registered alien powers."""
        return list(cls._aliens.values())

    @classmethod
    def get_names(cls) -> List[str]:
        """Get names of all registered alien powers."""
        return [a.name for a in cls._aliens.values()]

    @classmethod
    def count(cls) -> int:
        """Number of registered aliens."""
        return len(cls._aliens)

    @classmethod
    def clear(cls) -> None:
        """Clear all registered aliens (for testing)."""
        cls._aliens.clear()


def get_all_aliens() -> List[AlienPower]:
    """Get all registered alien powers."""
    return AlienRegistry.get_all()


def get_alien(name: str) -> Optional[AlienPower]:
    """Get an alien power by name."""
    return AlienRegistry.get(name)


# Import all power implementations to register them
from .powers import *  # noqa: F401, F403, E402
