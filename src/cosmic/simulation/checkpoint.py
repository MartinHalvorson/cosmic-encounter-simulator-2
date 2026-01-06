"""
Checkpointing utilities for Cosmic Encounter simulations.

Allows saving and restoring simulation state for long-running simulations.
"""

import json
import pickle
import gzip
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from .stats import Statistics, AlienStats


@dataclass
class CheckpointMetadata:
    """Metadata about a checkpoint."""
    created_at: str
    games_completed: int
    total_games_target: int
    version: str = "1.0"
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CheckpointMetadata":
        return cls(**data)


class SimulationCheckpoint:
    """
    Handles saving and loading simulation checkpoints.

    Checkpoints include:
    - Statistics object with all collected data
    - RNG state for reproducibility
    - Progress information
    """

    VERSION = "1.0"

    @staticmethod
    def save(
        filepath: str,
        statistics: Statistics,
        games_completed: int,
        total_games: int,
        rng_state: Optional[tuple] = None,
        notes: str = "",
        compress: bool = True,
    ) -> None:
        """
        Save a simulation checkpoint.

        Args:
            filepath: Path to save checkpoint
            statistics: Statistics object to save
            games_completed: Number of games completed so far
            total_games: Total games target
            rng_state: Random number generator state (from random.getstate())
            notes: Optional notes about this checkpoint
            compress: Whether to compress the checkpoint
        """
        metadata = CheckpointMetadata(
            created_at=datetime.now().isoformat(),
            games_completed=games_completed,
            total_games_target=total_games,
            version=SimulationCheckpoint.VERSION,
            notes=notes,
        )

        checkpoint_data = {
            "metadata": metadata.to_dict(),
            "statistics": SimulationCheckpoint._serialize_statistics(statistics),
            "rng_state": rng_state,
        }

        path = Path(filepath)
        if compress:
            with gzip.open(path, "wb") as f:
                pickle.dump(checkpoint_data, f, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            with open(path, "wb") as f:
                pickle.dump(checkpoint_data, f, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load(filepath: str) -> Dict[str, Any]:
        """
        Load a simulation checkpoint.

        Args:
            filepath: Path to checkpoint file

        Returns:
            Dict with 'metadata', 'statistics', and 'rng_state'
        """
        path = Path(filepath)

        try:
            with gzip.open(path, "rb") as f:
                data = pickle.load(f)
        except gzip.BadGzipFile:
            with open(path, "rb") as f:
                data = pickle.load(f)

        # Reconstruct objects
        metadata = CheckpointMetadata.from_dict(data["metadata"])
        statistics = SimulationCheckpoint._deserialize_statistics(data["statistics"])

        return {
            "metadata": metadata,
            "statistics": statistics,
            "rng_state": data.get("rng_state"),
        }

    @staticmethod
    def _serialize_statistics(stats: Statistics) -> Dict[str, Any]:
        """Serialize Statistics to a dict."""
        # Serialize alien stats
        alien_stats_data = {}
        for name, alien_stat in stats.alien_stats.items():
            alien_stats_data[name] = {
                "name": alien_stat.name,
                "games_played": alien_stat.games_played,
                "games_won": alien_stat.games_won,
                "shared_wins": alien_stat.shared_wins,
                "solo_wins": alien_stat.solo_wins,
                "alternate_wins": alien_stat.alternate_wins,
                "total_turns": alien_stat.total_turns,
                "total_colonies_at_end": alien_stat.total_colonies_at_end,
                "total_power_activations": alien_stat.total_power_activations,
                "total_encounters_as_main": alien_stat.total_encounters_as_main,
                "encounters_as_offense": alien_stat.encounters_as_offense,
                "encounters_as_defense": alien_stat.encounters_as_defense,
                "encounters_won_as_offense": alien_stat.encounters_won_as_offense,
                "encounters_won_as_defense": alien_stat.encounters_won_as_defense,
                "encounters_with_deal": alien_stat.encounters_with_deal,
                "encounters_with_allies": alien_stat.encounters_with_allies,
                "times_allied": alien_stat.times_allied,
                "times_allied_offense": alien_stat.times_allied_offense,
                "times_allied_defense": alien_stat.times_allied_defense,
                "alliance_wins": alien_stat.alliance_wins,
            }

        return {
            "total_games": stats.total_games,
            "shared_victory_count": stats.shared_victory_count,
            "solo_victory_count": stats.solo_victory_count,
            "timeout_count": stats.timeout_count,
            "error_count": stats.error_count,
            "turn_counts": stats.turn_counts,
            "games_by_player_count": stats.games_by_player_count,
            "wins_by_player_count": stats.wins_by_player_count,
            "alien_stats": alien_stats_data,
        }

    @staticmethod
    def _deserialize_statistics(data: Dict[str, Any]) -> Statistics:
        """Deserialize Statistics from a dict."""
        stats = Statistics()

        stats.total_games = data["total_games"]
        stats.shared_victory_count = data["shared_victory_count"]
        stats.solo_victory_count = data["solo_victory_count"]
        stats.timeout_count = data["timeout_count"]
        stats.error_count = data["error_count"]
        stats.turn_counts = data["turn_counts"]
        stats.games_by_player_count = data["games_by_player_count"]
        stats.wins_by_player_count = data["wins_by_player_count"]

        # Deserialize alien stats
        for name, alien_data in data["alien_stats"].items():
            stats.alien_stats[name] = AlienStats(
                name=alien_data["name"],
                games_played=alien_data["games_played"],
                games_won=alien_data["games_won"],
                shared_wins=alien_data["shared_wins"],
                solo_wins=alien_data["solo_wins"],
                alternate_wins=alien_data["alternate_wins"],
                total_turns=alien_data["total_turns"],
                total_colonies_at_end=alien_data["total_colonies_at_end"],
                total_power_activations=alien_data["total_power_activations"],
                total_encounters_as_main=alien_data["total_encounters_as_main"],
                encounters_as_offense=alien_data["encounters_as_offense"],
                encounters_as_defense=alien_data["encounters_as_defense"],
                encounters_won_as_offense=alien_data["encounters_won_as_offense"],
                encounters_won_as_defense=alien_data["encounters_won_as_defense"],
                encounters_with_deal=alien_data["encounters_with_deal"],
                encounters_with_allies=alien_data["encounters_with_allies"],
                times_allied=alien_data.get("times_allied", 0),
                times_allied_offense=alien_data.get("times_allied_offense", 0),
                times_allied_defense=alien_data.get("times_allied_defense", 0),
                alliance_wins=alien_data.get("alliance_wins", 0),
            )

        return stats

    @staticmethod
    def get_info(filepath: str) -> Dict[str, Any]:
        """
        Get information about a checkpoint without fully loading it.

        Args:
            filepath: Path to checkpoint file

        Returns:
            Dict with checkpoint metadata
        """
        checkpoint = SimulationCheckpoint.load(filepath)
        metadata = checkpoint["metadata"]

        return {
            "created_at": metadata.created_at,
            "games_completed": metadata.games_completed,
            "total_games_target": metadata.total_games_target,
            "progress_percent": (metadata.games_completed / metadata.total_games_target * 100)
                if metadata.total_games_target > 0 else 0,
            "version": metadata.version,
            "notes": metadata.notes,
        }


def save_checkpoint(
    filepath: str,
    statistics: Statistics,
    games_completed: int,
    total_games: int,
    **kwargs,
) -> None:
    """
    Convenience function to save a checkpoint.

    Args:
        filepath: Path to save checkpoint
        statistics: Statistics object
        games_completed: Games completed so far
        total_games: Total games target
        **kwargs: Additional options (rng_state, notes, compress)
    """
    SimulationCheckpoint.save(
        filepath=filepath,
        statistics=statistics,
        games_completed=games_completed,
        total_games=total_games,
        **kwargs,
    )


def load_checkpoint(filepath: str) -> Dict[str, Any]:
    """
    Convenience function to load a checkpoint.

    Args:
        filepath: Path to checkpoint file

    Returns:
        Dict with metadata, statistics, and rng_state
    """
    return SimulationCheckpoint.load(filepath)


def checkpoint_info(filepath: str) -> Dict[str, Any]:
    """
    Get information about a checkpoint.

    Args:
        filepath: Path to checkpoint file

    Returns:
        Dict with checkpoint information
    """
    return SimulationCheckpoint.get_info(filepath)
