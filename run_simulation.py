#!/usr/bin/env python3
"""
Cosmic Encounter Simulator - Main Entry Point

This script runs simulations of the board game Cosmic Encounter
and outputs statistics about alien power win rates.
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from cosmic.simulation.runner import Simulator, run_quick_simulation
from cosmic.types import GameConfig, SimulationConfig
from cosmic.aliens import AlienRegistry


def main():
    parser = argparse.ArgumentParser(
        description="Simulate Cosmic Encounter games"
    )
    parser.add_argument(
        "-n", "--num-games",
        type=int,
        default=1000,
        help="Number of games to simulate (default: 1000)"
    )
    parser.add_argument(
        "-p", "--players",
        type=int,
        default=5,
        help="Number of players per game (default: 5)"
    )
    parser.add_argument(
        "--min-players",
        type=int,
        help="Minimum players for varying player count simulation"
    )
    parser.add_argument(
        "--max-players",
        type=int,
        help="Maximum players for varying player count simulation"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output file path (csv or json based on extension)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress progress output"
    )
    parser.add_argument(
        "--list-powers",
        action="store_true",
        help="List all available alien powers and exit"
    )
    parser.add_argument(
        "--seed",
        type=int,
        help="Random seed for reproducibility"
    )

    args = parser.parse_args()

    # List powers if requested
    if args.list_powers:
        print("Available Alien Powers:")
        print("-" * 40)
        for power in sorted(AlienRegistry.get_names()):
            print(f"  - {power}")
        print(f"\nTotal: {AlienRegistry.count()} powers")
        return 0

    # Create configuration
    game_config = GameConfig(
        num_players=args.players,
        seed=args.seed,
    )

    sim_config = SimulationConfig(
        num_games=args.num_games,
        game_config=game_config,
        show_progress=not args.quiet,
        progress_interval=max(1, args.num_games // 20),
    )

    simulator = Simulator(config=sim_config)

    # Run simulation
    print(f"\nCosmic Encounter Simulator")
    print(f"=" * 40)
    print(f"Running {args.num_games} games with {args.players} players...")
    print()

    if args.min_players and args.max_players:
        # Varying player count simulation
        player_counts = list(range(args.min_players, args.max_players + 1))
        games_per_count = args.num_games // len(player_counts)
        result = simulator.run_with_varying_players(player_counts, games_per_count)
    else:
        # Standard simulation
        result = simulator.run()

    # Print results
    print("\n" + result.summary())

    # Save output if requested
    if args.output:
        output_path = Path(args.output)
        if output_path.suffix.lower() == ".json":
            result.statistics.save_json(args.output)
            print(f"\nResults saved to {args.output}")
        elif output_path.suffix.lower() == ".csv":
            result.statistics.save_csv(args.output)
            print(f"\nResults saved to {args.output}")
        else:
            print(f"Warning: Unknown output format, saving as JSON")
            result.statistics.save_json(args.output + ".json")

    return 0


if __name__ == "__main__":
    sys.exit(main())
