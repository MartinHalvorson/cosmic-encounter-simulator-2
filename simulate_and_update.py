#!/usr/bin/env python3
"""
Run simulations and update the README with cumulative statistics.

This script:
1. Loads existing cumulative statistics from JSON
2. Runs a batch of simulations
3. Updates the cumulative statistics
4. Regenerates the README table
5. Saves the updated statistics
"""

import argparse
import sys
import time
import random
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.aliens import AlienRegistry
from cosmic.simulation.cumulative_stats import CumulativeStats


STATS_FILE = "cumulative_stats.json"
README_FILE = "README.md"

# Markers for README table section
TABLE_START_MARKER = "<!-- SIMULATION_RESULTS_START -->"
TABLE_END_MARKER = "<!-- SIMULATION_RESULTS_END -->"


def run_simulation_batch(
    cumulative_stats: CumulativeStats,
    num_games: int = 1000,
    min_players: int = 3,
    max_players: int = 6,
    show_progress: bool = True,
    seed: int = None
) -> int:
    """
    Run a batch of simulations and record to cumulative stats.

    Returns number of games completed successfully.
    """
    rng = random.Random(seed)
    games_completed = 0
    errors = 0
    start_time = time.time()

    all_powers = AlienRegistry.get_names()

    for i in range(num_games):
        try:
            # Vary player count
            num_players = rng.randint(min_players, max_players)

            # Create game
            game_config = GameConfig(
                num_players=num_players,
                seed=rng.randint(0, 2**31),
            )
            game = Game(config=game_config)

            # Select random powers
            powers = rng.sample(all_powers, min(len(all_powers), num_players))

            # Play game
            game.setup(powers=powers)
            winners = game.play()

            # Record to cumulative stats
            winner_names = [w.name for w in winners]
            alien_map = {p.name: p.alien_name for p in game.players}
            final_colonies = {
                p.name: p.count_foreign_colonies(game.planets)
                for p in game.players
            }

            cumulative_stats.record_game(
                alien_map=alien_map,
                winner_names=winner_names,
                final_colonies=final_colonies,
                turn_count=game.current_turn,
                num_players=num_players,
                timed_out=game.current_turn >= game_config.max_turns,
            )

            games_completed += 1

        except Exception as e:
            errors += 1
            if errors <= 5:  # Only show first 5 errors
                print(f"  Error in game {i}: {e}")

        # Progress reporting
        if show_progress and (i + 1) % max(1, num_games // 20) == 0:
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            print(f"  Progress: {i + 1}/{num_games} ({rate:.1f} games/s)")

    cumulative_stats.simulation_runs += 1
    elapsed = time.time() - start_time

    if show_progress:
        print(f"\nBatch complete: {games_completed} games in {elapsed:.1f}s")
        if errors > 0:
            print(f"  Errors: {errors}")

    return games_completed


def update_readme(cumulative_stats: CumulativeStats, readme_path: str = README_FILE):
    """Update the README with the latest statistics table."""
    readme = Path(readme_path)

    if not readme.exists():
        print(f"Warning: {readme_path} not found")
        return

    content = readme.read_text()

    # Generate new table section
    table_content = f"""
{TABLE_START_MARKER}

## Simulation Results

{cumulative_stats.generate_summary()}

### Alien Power Rankings (by ELO)

{cumulative_stats.generate_readme_table(top_n=40)}

{TABLE_END_MARKER}"""

    # Check if markers exist
    if TABLE_START_MARKER in content and TABLE_END_MARKER in content:
        # Replace existing section
        start_idx = content.find(TABLE_START_MARKER)
        end_idx = content.find(TABLE_END_MARKER) + len(TABLE_END_MARKER)
        content = content[:start_idx] + table_content.strip() + content[end_idx:]
    else:
        # Append new section before any existing "## Legacy" section or at end
        legacy_idx = content.find("## Legacy")
        if legacy_idx != -1:
            content = content[:legacy_idx] + table_content + "\n\n" + content[legacy_idx:]
        else:
            content = content.rstrip() + "\n\n" + table_content + "\n"

    readme.write_text(content)
    print(f"Updated {readme_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Run Cosmic Encounter simulations and update README"
    )
    parser.add_argument(
        "-n", "--num-games",
        type=int,
        default=1000,
        help="Number of games to simulate (default: 1000)"
    )
    parser.add_argument(
        "--min-players",
        type=int,
        default=2,
        help="Minimum players per game (default: 2)"
    )
    parser.add_argument(
        "--max-players",
        type=int,
        default=6,
        help="Maximum players per game (default: 6)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress progress output"
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility"
    )
    parser.add_argument(
        "--no-update-readme",
        action="store_true",
        help="Don't update the README"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset cumulative stats before running"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("COSMIC ENCOUNTER SIMULATOR - Cumulative Statistics")
    print("=" * 60)

    # Load or create cumulative stats
    if args.reset:
        print("\nResetting cumulative statistics...")
        cumulative_stats = CumulativeStats()
    else:
        cumulative_stats = CumulativeStats.load(STATS_FILE)
        if cumulative_stats.total_games > 0:
            print(f"\nLoaded existing stats: {cumulative_stats.total_games:,} games")
        else:
            print("\nStarting fresh statistics")

    # Run simulation batch
    print(f"\nRunning {args.num_games} games ({args.min_players}-{args.max_players} players)...")

    games = run_simulation_batch(
        cumulative_stats,
        num_games=args.num_games,
        min_players=args.min_players,
        max_players=args.max_players,
        show_progress=not args.quiet,
        seed=args.seed,
    )

    # Save updated stats
    cumulative_stats.save(STATS_FILE)
    print(f"\nSaved cumulative stats to {STATS_FILE}")
    print(f"Total games now: {cumulative_stats.total_games:,}")

    # Update README
    if not args.no_update_readme:
        print(f"\nUpdating {README_FILE}...")
        update_readme(cumulative_stats)

    # Print top 10
    print("\n" + "-" * 60)
    print("TOP 10 ALIENS BY ELO")
    print("-" * 60)
    for i, stats in enumerate(cumulative_stats.get_rankings("elo")[:10], 1):
        print(
            f"{i:2}. {stats.name:20} ELO: {stats.elo_rating:7.1f}  "
            f"Win: {stats.win_rate_percent:5.1f}%  ({stats.games_won}/{stats.games_played})"
        )

    print("\n" + "=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
