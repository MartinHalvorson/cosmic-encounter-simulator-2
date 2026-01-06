#!/usr/bin/env python3
"""
Runs Cosmic Encounter simulations and updates the README with a sortable stats table.

Usage:
    python update_stats.py [--games N] [--sort COLUMN] [--order asc|desc]

Examples:
    python update_stats.py --games 1000
    python update_stats.py --sort elo --order desc
    python update_stats.py --sort 5p --order desc
"""

import json
import argparse
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from cosmic.simulation.runner import Simulator
from cosmic.types import SimulationConfig, GameConfig
from cosmic.aliens.official_aliens import get_alien_expansion

STATS_FILE = Path(__file__).parent / "stats.json"
README_FILE = Path(__file__).parent / "README.md"
PLAYER_COUNTS = [2, 3, 4, 5, 6]


def expected_score(rating_a: float, rating_b: float) -> float:
    """Calculate expected score for player A against player B."""
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))


def load_stats() -> dict:
    """Load existing stats from JSON file."""
    if STATS_FILE.exists():
        with open(STATS_FILE) as f:
            return json.load(f)
    return {"total_games": 0, "last_updated": None, "powers": {}}


def save_stats(stats: dict) -> None:
    """Save stats to JSON file."""
    stats["last_updated"] = datetime.now().isoformat()
    with open(STATS_FILE, "w") as f:
        json.dump(stats, f, indent=2)


def run_simulations(games_per_player_count: int = 500) -> dict:
    """Run simulations for each player count and return results."""
    results = {}

    for num_players in PLAYER_COUNTS:
        print(f"\nSimulating {games_per_player_count} games with {num_players} players...")

        config = SimulationConfig(
            num_games=games_per_player_count,
            game_config=GameConfig(num_players=num_players),
            show_progress=True,
            progress_interval=max(1, games_per_player_count // 10),
            catch_errors=True,
        )

        simulator = Simulator(config=config)
        result = simulator.run()

        # Extract stats
        power_data = {}
        for alien_name, alien_stats in result.statistics.alien_stats.items():
            power_data[alien_name] = {
                "games": alien_stats.games_played,
                "wins": alien_stats.games_won,
            }

        results[num_players] = {
            "power_data": power_data,
            "games": result.games_completed,
        }

    return results


def normalize_power_name(name: str, existing_powers: dict) -> str:
    """Normalize power name to prevent duplicates with different casings."""
    # Check if a case-insensitive match already exists
    name_lower = name.lower()
    for existing in existing_powers:
        if existing.lower() == name_lower:
            return existing  # Use existing casing
    return name  # New power, use as-is


def update_stats(stats: dict, new_results: dict) -> dict:
    """Merge new simulation results into existing stats."""
    for num_players, data in new_results.items():
        player_key = f"{num_players}p"

        for power_name, power_data in data["power_data"].items():
            # Normalize name to prevent case-insensitive duplicates
            power_name = normalize_power_name(power_name, stats["powers"])

            if power_name not in stats["powers"]:
                stats["powers"][power_name] = {
                    "elo": 1500,
                    "total_games": 0,
                    "total_wins": 0,
                    "by_player_count": {}
                }

            power = stats["powers"][power_name]

            # Update totals
            games = power_data.get("games", 0)
            wins = power_data.get("wins", 0)
            power["total_games"] += games
            power["total_wins"] += wins

            # Update per-player-count stats
            if player_key not in power["by_player_count"]:
                power["by_player_count"][player_key] = {"games": 0, "wins": 0}

            power["by_player_count"][player_key]["games"] += games
            power["by_player_count"][player_key]["wins"] += wins

        stats["total_games"] += data["games"]

    # Update ELO ratings based on win rates
    update_elo_ratings(stats)

    return stats


def update_elo_ratings(stats: dict) -> None:
    """Update ELO ratings based on accumulated statistics."""
    powers = stats["powers"]

    # Calculate average win rate
    total_games = sum(p["total_games"] for p in powers.values())
    if total_games == 0:
        return

    avg_win_rate = sum(p["total_wins"] for p in powers.values()) / total_games

    # Update ELO for each power based on performance vs expected
    for power_name, power_data in powers.items():
        if power_data["total_games"] < 10:
            continue

        win_rate = power_data["total_wins"] / power_data["total_games"]

        # Compare to expected (avg_win_rate) and adjust ELO
        # K-factor decreases with more games for stability
        games = power_data["total_games"]
        k = max(8, 32 - games // 100)

        expected = 0.5  # Expected to win 50% against average
        actual = win_rate / (avg_win_rate * 2) if avg_win_rate > 0 else 0.5
        actual = min(1.0, max(0.0, actual))  # Clamp to [0, 1]

        power_data["elo"] = power_data["elo"] + k * (actual - expected)


def get_win_rate(power_data: dict, player_key: str = None) -> float:
    """Calculate win rate for a power, optionally for specific player count."""
    if player_key:
        pc_data = power_data["by_player_count"].get(player_key, {})
        games = pc_data.get("games", 0)
        wins = pc_data.get("wins", 0)
    else:
        games = power_data["total_games"]
        wins = power_data["total_wins"]

    return (wins / games * 100) if games > 0 else 0


def generate_table(stats: dict, sort_by: str = "elo", ascending: bool = False) -> str:
    """Generate HTML table for README."""
    powers = stats["powers"]

    # Deduplicate powers (case-insensitive) - keep the one with most games
    seen = {}
    for name, data in powers.items():
        lower_name = name.lower()
        if lower_name not in seen or data["total_games"] > seen[lower_name][1]["total_games"]:
            seen[lower_name] = (name, data)

    # Abbreviations for expansions to keep table compact
    EXPANSION_ABBREV = {
        "Base Game": "Base",
        "Cosmic Incursion": "Incursion",
        "Cosmic Conflict": "Conflict",
        "Cosmic Alliance": "Alliance",
        "Cosmic Storm": "Storm",
        "Cosmic Dominion": "Dominion",
        "Cosmic Eons": "Eons",
        "Cosmic Odyssey": "Odyssey",
        None: "Custom",
    }

    # Build sortable data from deduplicated powers
    table_data = []
    for lower_name, (name, data) in seen.items():
        if data["total_games"] < 5:  # Skip powers with very few games
            continue
        expansion = get_alien_expansion(name)
        row = {
            "name": name,
            "elo": data["elo"],
            "overall": get_win_rate(data),
            "games": data["total_games"],
            "source": EXPANSION_ABBREV.get(expansion, "Custom"),
        }
        for pc in PLAYER_COUNTS:
            row[f"{pc}p"] = get_win_rate(data, f"{pc}p")
        table_data.append(row)

    # Sort
    if sort_by == "power":
        table_data.sort(key=lambda x: x["name"].lower(), reverse=not ascending)
    elif sort_by == "source":
        table_data.sort(key=lambda x: x["source"].lower(), reverse=not ascending)
    else:
        table_data.sort(key=lambda x: x.get(sort_by, 0), reverse=not ascending)

    # Generate HTML table
    html = """
<table>
<thead>
<tr>
<th align="left">Rank</th>
<th align="left">Power</th>
<th align="left">Source</th>
<th align="right">ELO</th>
<th align="right">Overall</th>
<th align="right">2P</th>
<th align="right">3P</th>
<th align="right">4P</th>
<th align="right">5P</th>
<th align="right">6P</th>
<th align="right">Games</th>
</tr>
</thead>
<tbody>
"""

    for i, row in enumerate(table_data, 1):
        # Determine tier based on ELO
        elo = row["elo"]
        if elo >= 1600:
            tier = "🟣"  # S tier
        elif elo >= 1550:
            tier = "🔵"  # A tier
        elif elo >= 1500:
            tier = "🟢"  # B tier
        elif elo >= 1450:
            tier = "🟡"  # C tier
        else:
            tier = "🔴"  # D tier

        html += f"""<tr>
<td align="left">{i}</td>
<td align="left">{tier} {row['name']}</td>
<td align="left">{row['source']}</td>
<td align="right"><b>{row['elo']:.0f}</b></td>
<td align="right">{row['overall']:.1f}%</td>
<td align="right">{row['2p']:.1f}%</td>
<td align="right">{row['3p']:.1f}%</td>
<td align="right">{row['4p']:.1f}%</td>
<td align="right">{row['5p']:.1f}%</td>
<td align="right">{row['6p']:.1f}%</td>
<td align="right">{row['games']}</td>
</tr>
"""

    html += """</tbody>
</table>
"""
    return html


def update_readme(stats: dict, sort_by: str = "elo", ascending: bool = False) -> None:
    """Update README.md with the new stats table."""
    table = generate_table(stats, sort_by, ascending)

    # Create the stats section
    last_updated = stats.get("last_updated", "Never")
    if last_updated and last_updated != "Never":
        last_updated = datetime.fromisoformat(last_updated).strftime("%Y-%m-%d %H:%M")

    stats_section = f"""## Alien Power Rankings

> **{stats['total_games']:,}** games simulated | Last updated: {last_updated}
>
> **Tier Guide:** 🟣 S (1600+) | 🔵 A (1550+) | 🟢 B (1500+) | 🟡 C (1450+) | 🔴 D (<1450)

{table}

<details>
<summary>How to update this table</summary>

```bash
# Run more simulations (adds to existing data)
python update_stats.py --games 1000

# Sort by ELO (default)
python update_stats.py --sort elo --order desc

# Sort by overall win rate
python update_stats.py --sort overall --order desc

# Sort by 5-player win rate
python update_stats.py --sort 5p --order desc

# Sort alphabetically by power name
python update_stats.py --sort power --order asc

# Sort by source/expansion
python update_stats.py --sort source --order asc
```

</details>

"""

    # Read current README
    readme_content = README_FILE.read_text(encoding='utf-8')

    # Find and replace the stats section, or insert before Legacy Version
    marker_start = "## Alien Power Rankings"
    marker_end = "## Legacy Version"

    if marker_start in readme_content:
        # Replace existing section
        start_idx = readme_content.find(marker_start)
        end_idx = readme_content.find(marker_end, start_idx)
        if end_idx != -1:
            readme_content = readme_content[:start_idx] + stats_section + readme_content[end_idx:]
        else:
            readme_content = readme_content[:start_idx] + stats_section
    else:
        # Insert before Legacy Version or at end
        legacy_idx = readme_content.find("## Legacy Version")
        if legacy_idx != -1:
            readme_content = readme_content[:legacy_idx] + stats_section + readme_content[legacy_idx:]
        else:
            readme_content += "\n" + stats_section

    README_FILE.write_text(readme_content, encoding='utf-8')
    print(f"\nREADME.md updated!")


def main():
    parser = argparse.ArgumentParser(description="Update Cosmic Encounter simulation stats")
    parser.add_argument("--games", type=int, default=0,
                        help="Number of games to simulate per player count (0 = just regenerate table)")
    parser.add_argument("--sort", type=str, default="elo",
                        choices=["power", "source", "elo", "overall", "2p", "3p", "4p", "5p", "6p", "games"],
                        help="Column to sort by")
    parser.add_argument("--order", type=str, default="desc",
                        choices=["asc", "desc"],
                        help="Sort order")

    args = parser.parse_args()

    # Load existing stats
    stats = load_stats()
    print(f"Loaded stats: {stats['total_games']:,} total games")

    # Run new simulations if requested
    if args.games > 0:
        print(f"\nRunning {args.games} games per player count...")
        results = run_simulations(args.games)
        stats = update_stats(stats, results)
        save_stats(stats)
        print(f"\nTotal games now: {stats['total_games']:,}")

    if stats['total_games'] > 0:
        # Update README
        ascending = args.order == "asc"
        update_readme(stats, args.sort, ascending)
        print(f"Table sorted by: {args.sort} ({args.order})")
    else:
        print("No games simulated yet. Run with --games N to simulate games.")


if __name__ == "__main__":
    main()
