# Cosmic Encounter Simulator 2

A comprehensive simulation of the board game Cosmic Encounter, designed to analyze alien power balance and game dynamics across various configurations.

## Features

- **68 Alien Powers** implemented with proper game mechanics
- **Multiple AI Strategies**: Random, Basic, and Strategic AI for realistic gameplay
- **Full Game Flow**: All 8 encounter phases (Start Turn, Regroup, Destiny, Launch, Alliance, Planning, Reveal, Resolution)
- **Comprehensive Statistics**: Win rates, game length analysis, CSV/JSON export
- **Configurable Simulations**: Variable player counts (3-8), custom power sets, reproducible seeds

## Installation

```bash
# Clone the repository
git clone https://github.com/MartinHalvorson/cosmic-encounter-simulator-2.git
cd cosmic-encounter-simulator-2

# No dependencies required - uses Python standard library only
python3 run_simulation.py --help
```

## Usage

### Basic Simulation

```bash
# Run 1000 games with 5 players
python3 run_simulation.py -n 1000 -p 5

# Quick 100-game test
python3 run_simulation.py -n 100

# Quiet mode (no progress output)
python3 run_simulation.py -n 1000 -q
```

### List Available Powers

```bash
python3 run_simulation.py --list-powers
```

### Export Results

```bash
# Export to CSV
python3 run_simulation.py -n 1000 -o results.csv

# Export to JSON
python3 run_simulation.py -n 1000 -o results.json
```

### Advanced Options

```bash
# Variable player counts (3-6 players)
python3 run_simulation.py -n 1000 --min-players 3 --max-players 6

# Set random seed for reproducibility
python3 run_simulation.py -n 1000 --seed 42
```

## Example Output

```
============================================================
COSMIC ENCOUNTER SIMULATION RESULTS
============================================================

Total Games: 1000
Solo Victories: 986
Shared Victories: 14
Timeouts: 0
Errors: 0

Average Game Length: 4.8 turns
Shortest Game: 1 turns
Longest Game: 32 turns

------------------------------------------------------------
ALIEN POWER WIN RATES
------------------------------------------------------------
  1. Parasite              52.3% (32/61)
  2. Machine               41.2% (28/68)
  3. Symbiote              35.7% (25/70)
  ...
```

## Project Structure

```
src/cosmic/
├── game.py           # Main game logic
├── player.py         # Player class
├── planet.py         # Planet and colony mechanics
├── types.py          # Type definitions and enums
├── cards/            # Card system (Cosmic, Destiny, Rewards decks)
├── aliens/           # 68 alien power implementations
├── ai/               # AI strategies (Random, Basic, Strategic)
└── simulation/       # Simulation runner and statistics
```

## Implemented Alien Powers (68)

Amoeba, Altruist, Antimatter, Assassin, Butler, Calculator, Changeling, Chosen, Chronos, Citadel, Claw, Clone, Crone, Cudgel, Dictator, Disease, Empath, Ethic, Fido, Filch, Gambler, Genius, Ghoul, Giver, Grudge, Hacker, Healer, Human, Kamikazee, Leviathan, Loser, Machine, Macron, Masochist, Mirror, Mite, Mutant, Negator, Observer, Oracle, Pacifist, Parasite, Pentaform, Philanthropist, Pickpocket, Reincarnator, Remora, Reserve, Seeker, Shadow, Sheriff, Silencer, Sniveler, Sorcerer, Spiff, Surge, Symbiote, Tick-Tock, Trader, Tripler, Vacuum, Virus, Visionary, Void, Warpish, Warrior, Yin, Zombie

## Game Rules Reference

The simulator follows [Fantasy Flight Games Cosmic Encounter](https://www.fantasyflightgames.com/en/products/cosmic-encounter/) rules.

Key mechanics implemented:
- **Encounter Flow**: Full 8-phase encounter sequence
- **Alliances**: Strategic invitation and acceptance
- **Deals**: Colony swaps with failed deal penalties (3 ships to warp)
- **Compensation**: Cards from attacker when negotiate loses to attack
- **Alternate Win Conditions**: Masochist, Genius, Tick-Tock

## Legacy Version

The original 2016 simulator is preserved in `Simulator.py` and `main.py` for reference.
