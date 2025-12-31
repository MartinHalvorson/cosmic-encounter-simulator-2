# Cosmic Encounter Simulator 2

A comprehensive simulation of the board game Cosmic Encounter, designed to analyze alien power balance and game dynamics across various configurations.

## Features

- **200 Alien Powers** implemented with proper game mechanics
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
├── aliens/           # 129 alien power implementations
├── ai/               # AI strategies (Random, Basic, Strategic)
└── simulation/       # Simulation runner and statistics
```

## Implemented Alien Powers (90)

Altruist, Amoeba, Antimatter, Assassin, Barbarian, Boomerang, Brute, Butler, Calculator, Changeling, Chosen, Chronos, Citadel, Claw, Clone, Crone, Crystal, Cudgel, Deuce, Dictator, Disease, Dragon, Empath, Ethic, Fido, Filch, Fury, Gambler, Genius, Ghoul, Giver, Grudge, Hacker, Hate, Healer, Human, Kamikazee, Laser, Leviathan, Loser, Machine, Macron, Masochist, Mimic, Mirror, Mite, Mutant, Negator, Nightmare, Observer, Oracle, Pacifist, Parasite, Patriot, Pentaform, Philanthropist, Pickpocket, Pirate, Poison, Rage, Reincarnator, Remora, Reserve, Sage, Scout, Seeker, Shadow, Sheriff, Silencer, Sniveler, Sorcerer, Spiff, Surge, Symbiote, Thief, Tick-Tock, Trader, Tripler, Tyrant, Underdog, Vacuum, Virus, Visionary, Void, Vox, Warlock, Warpish, Warrior, Yin, Zombie

## Game Rules Reference

The simulator follows [Fantasy Flight Games Cosmic Encounter](https://www.fantasyflightgames.com/en/products/cosmic-encounter/) rules.

Key mechanics implemented:
- **Encounter Flow**: Full 8-phase encounter sequence
- **Alliances**: Strategic invitation and acceptance
- **Deals**: Colony swaps with failed deal penalties (3 ships to warp)
- **Compensation**: Cards from attacker when negotiate loses to attack
- **Alternate Win Conditions**: Masochist, Genius, Tick-Tock

## Alien Power Rankings

> **54,000** games simulated | Last updated: 2025-12-30 18:02
>
> **Tier Guide:** 🟣 S (1600+) | 🔵 A (1550+) | 🟢 B (1500+) | 🟡 C (1450+) | 🔴 D (<1450)


<table>
<thead>
<tr>
<th align="left">Rank</th>
<th align="left">Power</th>
<th align="right">ELO</th>
<th align="right">Overall</th>
<th align="right">3P</th>
<th align="right">4P</th>
<th align="right">5P</th>
<th align="right">6P</th>
<th align="right">Games</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">1</td>
<td align="left">🔵 Machine</td>
<td align="right"><b>1570</b></td>
<td align="right">56.9%</td>
<td align="right">69.8%</td>
<td align="right">65.0%</td>
<td align="right">57.9%</td>
<td align="right">44.3%</td>
<td align="right">2072</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🔵 Parasite</td>
<td align="right"><b>1568</b></td>
<td align="right">45.5%</td>
<td align="right">44.4%</td>
<td align="right">45.8%</td>
<td align="right">47.7%</td>
<td align="right">44.0%</td>
<td align="right">2144</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Warpish</td>
<td align="right"><b>1528</b></td>
<td align="right">31.6%</td>
<td align="right">52.5%</td>
<td align="right">40.5%</td>
<td align="right">24.8%</td>
<td align="right">22.6%</td>
<td align="right">2032</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Disease</td>
<td align="right"><b>1526</b></td>
<td align="right">28.1%</td>
<td align="right">41.6%</td>
<td align="right">29.1%</td>
<td align="right">21.6%</td>
<td align="right">25.4%</td>
<td align="right">2167</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Symbiote</td>
<td align="right"><b>1524</b></td>
<td align="right">30.6%</td>
<td align="right">49.8%</td>
<td align="right">35.6%</td>
<td align="right">27.1%</td>
<td align="right">20.1%</td>
<td align="right">2001</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Mutant</td>
<td align="right"><b>1521</b></td>
<td align="right">27.3%</td>
<td align="right">46.4%</td>
<td align="right">31.0%</td>
<td align="right">24.6%</td>
<td align="right">17.8%</td>
<td align="right">2171</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Tripler</td>
<td align="right"><b>1520</b></td>
<td align="right">28.8%</td>
<td align="right">46.1%</td>
<td align="right">30.3%</td>
<td align="right">25.9%</td>
<td align="right">21.3%</td>
<td align="right">2186</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Pacifist</td>
<td align="right"><b>1516</b></td>
<td align="right">27.9%</td>
<td align="right">49.7%</td>
<td align="right">36.2%</td>
<td align="right">19.3%</td>
<td align="right">18.8%</td>
<td align="right">2139</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Macron</td>
<td align="right"><b>1513</b></td>
<td align="right">28.6%</td>
<td align="right">47.9%</td>
<td align="right">29.9%</td>
<td align="right">26.5%</td>
<td align="right">19.0%</td>
<td align="right">2097</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Human</td>
<td align="right"><b>1512</b></td>
<td align="right">25.9%</td>
<td align="right">42.7%</td>
<td align="right">28.3%</td>
<td align="right">20.5%</td>
<td align="right">19.9%</td>
<td align="right">2081</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Shadow</td>
<td align="right"><b>1510</b></td>
<td align="right">26.1%</td>
<td align="right">43.3%</td>
<td align="right">32.0%</td>
<td align="right">21.2%</td>
<td align="right">17.1%</td>
<td align="right">2205</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Trader</td>
<td align="right"><b>1510</b></td>
<td align="right">26.4%</td>
<td align="right">44.1%</td>
<td align="right">29.8%</td>
<td align="right">23.4%</td>
<td align="right">17.4%</td>
<td align="right">2091</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Virus</td>
<td align="right"><b>1509</b></td>
<td align="right">25.9%</td>
<td align="right">42.2%</td>
<td align="right">26.9%</td>
<td align="right">23.8%</td>
<td align="right">18.6%</td>
<td align="right">2134</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Chronos</td>
<td align="right"><b>1509</b></td>
<td align="right">22.8%</td>
<td align="right">32.1%</td>
<td align="right">26.3%</td>
<td align="right">20.4%</td>
<td align="right">17.8%</td>
<td align="right">2179</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Chrysalis</td>
<td align="right"><b>1508</b></td>
<td align="right">28.0%</td>
<td align="right">46.9%</td>
<td align="right">34.6%</td>
<td align="right">24.1%</td>
<td align="right">17.7%</td>
<td align="right">1394</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Aristocrat</td>
<td align="right"><b>1508</b></td>
<td align="right">26.2%</td>
<td align="right">36.8%</td>
<td align="right">25.2%</td>
<td align="right">26.9%</td>
<td align="right">20.8%</td>
<td align="right">1380</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Engineer</td>
<td align="right"><b>1504</b></td>
<td align="right">24.3%</td>
<td align="right">34.2%</td>
<td align="right">23.0%</td>
<td align="right">25.5%</td>
<td align="right">19.3%</td>
<td align="right">1443</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Insect</td>
<td align="right"><b>1504</b></td>
<td align="right">25.0%</td>
<td align="right">37.9%</td>
<td align="right">26.5%</td>
<td align="right">22.4%</td>
<td align="right">18.7%</td>
<td align="right">1381</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Bully</td>
<td align="right"><b>1504</b></td>
<td align="right">24.8%</td>
<td align="right">34.0%</td>
<td align="right">28.7%</td>
<td align="right">19.0%</td>
<td align="right">22.5%</td>
<td align="right">1388</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Ghoul</td>
<td align="right"><b>1504</b></td>
<td align="right">27.0%</td>
<td align="right">42.7%</td>
<td align="right">34.3%</td>
<td align="right">23.2%</td>
<td align="right">17.4%</td>
<td align="right">2108</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Connoisseur</td>
<td align="right"><b>1503</b></td>
<td align="right">23.3%</td>
<td align="right">37.5%</td>
<td align="right">25.0%</td>
<td align="right">21.7%</td>
<td align="right">15.8%</td>
<td align="right">1409</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Bulwark</td>
<td align="right"><b>1503</b></td>
<td align="right">23.1%</td>
<td align="right">36.8%</td>
<td align="right">26.5%</td>
<td align="right">20.5%</td>
<td align="right">15.7%</td>
<td align="right">1361</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Grudge</td>
<td align="right"><b>1503</b></td>
<td align="right">21.9%</td>
<td align="right">31.2%</td>
<td align="right">24.2%</td>
<td align="right">20.6%</td>
<td align="right">17.0%</td>
<td align="right">2162</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Ghast</td>
<td align="right"><b>1503</b></td>
<td align="right">22.2%</td>
<td align="right">36.6%</td>
<td align="right">25.4%</td>
<td align="right">18.6%</td>
<td align="right">16.1%</td>
<td align="right">1362</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Invader</td>
<td align="right"><b>1502</b></td>
<td align="right">23.2%</td>
<td align="right">37.7%</td>
<td align="right">24.5%</td>
<td align="right">18.6%</td>
<td align="right">18.7%</td>
<td align="right">1445</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Tyrant</td>
<td align="right"><b>1502</b></td>
<td align="right">23.3%</td>
<td align="right">35.6%</td>
<td align="right">24.6%</td>
<td align="right">18.8%</td>
<td align="right">20.6%</td>
<td align="right">1994</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Gambler</td>
<td align="right"><b>1502</b></td>
<td align="right">22.7%</td>
<td align="right">33.1%</td>
<td align="right">24.7%</td>
<td align="right">20.4%</td>
<td align="right">17.7%</td>
<td align="right">2145</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Void</td>
<td align="right"><b>1502</b></td>
<td align="right">21.9%</td>
<td align="right">34.6%</td>
<td align="right">22.9%</td>
<td align="right">18.5%</td>
<td align="right">17.4%</td>
<td align="right">2109</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟢 Miser</td>
<td align="right"><b>1502</b></td>
<td align="right">23.6%</td>
<td align="right">29.2%</td>
<td align="right">29.1%</td>
<td align="right">23.9%</td>
<td align="right">16.5%</td>
<td align="right">1330</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟢 Diplomat</td>
<td align="right"><b>1501</b></td>
<td align="right">23.1%</td>
<td align="right">32.9%</td>
<td align="right">28.3%</td>
<td align="right">21.0%</td>
<td align="right">16.4%</td>
<td align="right">1357</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟢 Fury</td>
<td align="right"><b>1501</b></td>
<td align="right">21.8%</td>
<td align="right">29.6%</td>
<td align="right">27.7%</td>
<td align="right">18.6%</td>
<td align="right">16.3%</td>
<td align="right">2124</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟢 Electron</td>
<td align="right"><b>1501</b></td>
<td align="right">23.7%</td>
<td align="right">37.1%</td>
<td align="right">25.5%</td>
<td align="right">21.1%</td>
<td align="right">17.9%</td>
<td align="right">1424</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟢 Amoeba</td>
<td align="right"><b>1501</b></td>
<td align="right">22.1%</td>
<td align="right">35.9%</td>
<td align="right">24.1%</td>
<td align="right">19.8%</td>
<td align="right">15.6%</td>
<td align="right">2063</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟢 Oracle</td>
<td align="right"><b>1501</b></td>
<td align="right">22.2%</td>
<td align="right">38.8%</td>
<td align="right">22.2%</td>
<td align="right">19.3%</td>
<td align="right">15.9%</td>
<td align="right">2139</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟢 Delegator</td>
<td align="right"><b>1501</b></td>
<td align="right">23.1%</td>
<td align="right">38.3%</td>
<td align="right">24.6%</td>
<td align="right">22.4%</td>
<td align="right">14.5%</td>
<td align="right">1388</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟢 Grief</td>
<td align="right"><b>1501</b></td>
<td align="right">22.7%</td>
<td align="right">36.8%</td>
<td align="right">26.9%</td>
<td align="right">19.4%</td>
<td align="right">15.2%</td>
<td align="right">1378</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟢 Fungus</td>
<td align="right"><b>1501</b></td>
<td align="right">22.0%</td>
<td align="right">33.0%</td>
<td align="right">23.4%</td>
<td align="right">16.8%</td>
<td align="right">20.1%</td>
<td align="right">1453</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟢 Battlemaster</td>
<td align="right"><b>1501</b></td>
<td align="right">22.9%</td>
<td align="right">39.2%</td>
<td align="right">23.8%</td>
<td align="right">20.0%</td>
<td align="right">16.1%</td>
<td align="right">1376</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟢 Schizoid</td>
<td align="right"><b>1501</b></td>
<td align="right">21.8%</td>
<td align="right">34.0%</td>
<td align="right">22.3%</td>
<td align="right">20.7%</td>
<td align="right">15.8%</td>
<td align="right">1374</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟢 Filch</td>
<td align="right"><b>1501</b></td>
<td align="right">21.7%</td>
<td align="right">32.1%</td>
<td align="right">25.3%</td>
<td align="right">19.0%</td>
<td align="right">16.4%</td>
<td align="right">2131</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟢 Guardian</td>
<td align="right"><b>1501</b></td>
<td align="right">22.4%</td>
<td align="right">30.4%</td>
<td align="right">27.4%</td>
<td align="right">19.4%</td>
<td align="right">16.3%</td>
<td align="right">1400</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟢 Dictator</td>
<td align="right"><b>1500</b></td>
<td align="right">21.4%</td>
<td align="right">32.7%</td>
<td align="right">24.1%</td>
<td align="right">18.8%</td>
<td align="right">16.3%</td>
<td align="right">2041</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟢 Spiff</td>
<td align="right"><b>1500</b></td>
<td align="right">21.0%</td>
<td align="right">32.4%</td>
<td align="right">27.2%</td>
<td align="right">18.3%</td>
<td align="right">13.2%</td>
<td align="right">2145</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟢 Changeling</td>
<td align="right"><b>1500</b></td>
<td align="right">21.0%</td>
<td align="right">24.7%</td>
<td align="right">27.7%</td>
<td align="right">19.0%</td>
<td align="right">16.6%</td>
<td align="right">2142</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟢 Warlock</td>
<td align="right"><b>1500</b></td>
<td align="right">21.7%</td>
<td align="right">31.6%</td>
<td align="right">27.4%</td>
<td align="right">19.1%</td>
<td align="right">15.8%</td>
<td align="right">1998</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟡 Glutton</td>
<td align="right"><b>1500</b></td>
<td align="right">22.0%</td>
<td align="right">29.6%</td>
<td align="right">24.3%</td>
<td align="right">21.6%</td>
<td align="right">16.7%</td>
<td align="right">1425</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟡 Warrior</td>
<td align="right"><b>1500</b></td>
<td align="right">22.2%</td>
<td align="right">37.7%</td>
<td align="right">25.1%</td>
<td align="right">18.6%</td>
<td align="right">15.5%</td>
<td align="right">2145</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟡 Doppelganger</td>
<td align="right"><b>1500</b></td>
<td align="right">21.6%</td>
<td align="right">27.1%</td>
<td align="right">27.5%</td>
<td align="right">22.3%</td>
<td align="right">14.3%</td>
<td align="right">1387</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟡 Jester</td>
<td align="right"><b>1499</b></td>
<td align="right">22.6%</td>
<td align="right">35.0%</td>
<td align="right">27.1%</td>
<td align="right">17.6%</td>
<td align="right">17.3%</td>
<td align="right">1430</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟡 Extortionist</td>
<td align="right"><b>1499</b></td>
<td align="right">20.1%</td>
<td align="right">31.8%</td>
<td align="right">20.1%</td>
<td align="right">17.3%</td>
<td align="right">16.7%</td>
<td align="right">1453</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟡 Barbarian</td>
<td align="right"><b>1499</b></td>
<td align="right">22.6%</td>
<td align="right">30.0%</td>
<td align="right">25.6%</td>
<td align="right">22.4%</td>
<td align="right">17.2%</td>
<td align="right">1976</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟡 Pirate</td>
<td align="right"><b>1499</b></td>
<td align="right">21.8%</td>
<td align="right">32.2%</td>
<td align="right">21.7%</td>
<td align="right">20.7%</td>
<td align="right">17.4%</td>
<td align="right">2015</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟡 Nightmare</td>
<td align="right"><b>1498</b></td>
<td align="right">20.2%</td>
<td align="right">29.9%</td>
<td align="right">18.8%</td>
<td align="right">19.2%</td>
<td align="right">16.8%</td>
<td align="right">1973</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟡 Leviathan</td>
<td align="right"><b>1498</b></td>
<td align="right">20.4%</td>
<td align="right">34.4%</td>
<td align="right">23.6%</td>
<td align="right">16.7%</td>
<td align="right">14.6%</td>
<td align="right">2140</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟡 Dragon</td>
<td align="right"><b>1498</b></td>
<td align="right">21.7%</td>
<td align="right">32.8%</td>
<td align="right">20.4%</td>
<td align="right">20.2%</td>
<td align="right">17.4%</td>
<td align="right">2010</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟡 Mimic</td>
<td align="right"><b>1498</b></td>
<td align="right">22.1%</td>
<td align="right">34.2%</td>
<td align="right">24.3%</td>
<td align="right">20.6%</td>
<td align="right">15.8%</td>
<td align="right">2029</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟡 Roach</td>
<td align="right"><b>1498</b></td>
<td align="right">20.5%</td>
<td align="right">29.5%</td>
<td align="right">25.4%</td>
<td align="right">18.1%</td>
<td align="right">15.0%</td>
<td align="right">1368</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟡 Cavalry</td>
<td align="right"><b>1498</b></td>
<td align="right">22.0%</td>
<td align="right">30.2%</td>
<td align="right">26.9%</td>
<td align="right">21.7%</td>
<td align="right">15.1%</td>
<td align="right">1450</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟡 Prophet</td>
<td align="right"><b>1498</b></td>
<td align="right">22.0%</td>
<td align="right">37.0%</td>
<td align="right">22.3%</td>
<td align="right">23.1%</td>
<td align="right">14.6%</td>
<td align="right">1347</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟡 Poison</td>
<td align="right"><b>1498</b></td>
<td align="right">21.5%</td>
<td align="right">29.2%</td>
<td align="right">25.2%</td>
<td align="right">19.7%</td>
<td align="right">16.9%</td>
<td align="right">2025</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟡 Vox</td>
<td align="right"><b>1498</b></td>
<td align="right">21.3%</td>
<td align="right">33.0%</td>
<td align="right">24.7%</td>
<td align="right">17.5%</td>
<td align="right">16.6%</td>
<td align="right">1988</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟡 Cudgel</td>
<td align="right"><b>1497</b></td>
<td align="right">21.8%</td>
<td align="right">38.3%</td>
<td align="right">25.5%</td>
<td align="right">17.6%</td>
<td align="right">14.3%</td>
<td align="right">2080</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟡 Vacuum</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">37.5%</td>
<td align="right">24.8%</td>
<td align="right">18.8%</td>
<td align="right">16.9%</td>
<td align="right">2131</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟡 Reincarnator</td>
<td align="right"><b>1497</b></td>
<td align="right">20.8%</td>
<td align="right">32.3%</td>
<td align="right">23.4%</td>
<td align="right">18.0%</td>
<td align="right">15.8%</td>
<td align="right">2104</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟡 Foam</td>
<td align="right"><b>1497</b></td>
<td align="right">21.3%</td>
<td align="right">28.1%</td>
<td align="right">24.9%</td>
<td align="right">20.8%</td>
<td align="right">15.9%</td>
<td align="right">1373</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟡 Patriot</td>
<td align="right"><b>1497</b></td>
<td align="right">22.8%</td>
<td align="right">39.6%</td>
<td align="right">24.8%</td>
<td align="right">19.8%</td>
<td align="right">15.8%</td>
<td align="right">1997</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟡 Harbinger</td>
<td align="right"><b>1497</b></td>
<td align="right">19.8%</td>
<td align="right">26.4%</td>
<td align="right">22.5%</td>
<td align="right">16.4%</td>
<td align="right">17.7%</td>
<td align="right">1416</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟡 Architect</td>
<td align="right"><b>1497</b></td>
<td align="right">21.2%</td>
<td align="right">36.0%</td>
<td align="right">21.8%</td>
<td align="right">20.9%</td>
<td align="right">14.4%</td>
<td align="right">1399</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟡 Witch</td>
<td align="right"><b>1497</b></td>
<td align="right">21.0%</td>
<td align="right">34.5%</td>
<td align="right">19.9%</td>
<td align="right">17.5%</td>
<td align="right">17.3%</td>
<td align="right">1459</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟡 Fido</td>
<td align="right"><b>1497</b></td>
<td align="right">22.3%</td>
<td align="right">36.4%</td>
<td align="right">24.8%</td>
<td align="right">19.2%</td>
<td align="right">16.8%</td>
<td align="right">2181</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟡 Kamikazee</td>
<td align="right"><b>1496</b></td>
<td align="right">23.5%</td>
<td align="right">34.9%</td>
<td align="right">28.9%</td>
<td align="right">20.0%</td>
<td align="right">17.1%</td>
<td align="right">2126</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟡 Fodder</td>
<td align="right"><b>1496</b></td>
<td align="right">19.7%</td>
<td align="right">31.7%</td>
<td align="right">21.1%</td>
<td align="right">18.3%</td>
<td align="right">13.9%</td>
<td align="right">1445</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟡 Crystal</td>
<td align="right"><b>1496</b></td>
<td align="right">20.9%</td>
<td align="right">26.5%</td>
<td align="right">23.7%</td>
<td align="right">18.8%</td>
<td align="right">18.0%</td>
<td align="right">2021</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟡 Surge</td>
<td align="right"><b>1496</b></td>
<td align="right">20.5%</td>
<td align="right">33.1%</td>
<td align="right">23.4%</td>
<td align="right">18.6%</td>
<td align="right">14.3%</td>
<td align="right">2134</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟡 Magician</td>
<td align="right"><b>1496</b></td>
<td align="right">19.2%</td>
<td align="right">27.4%</td>
<td align="right">21.4%</td>
<td align="right">20.0%</td>
<td align="right">13.7%</td>
<td align="right">1361</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟡 Vulture</td>
<td align="right"><b>1496</b></td>
<td align="right">21.3%</td>
<td align="right">32.8%</td>
<td align="right">26.5%</td>
<td align="right">19.1%</td>
<td align="right">13.9%</td>
<td align="right">1374</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟡 Observer</td>
<td align="right"><b>1496</b></td>
<td align="right">21.6%</td>
<td align="right">34.5%</td>
<td align="right">24.9%</td>
<td align="right">17.0%</td>
<td align="right">17.4%</td>
<td align="right">2179</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟡 Giver</td>
<td align="right"><b>1496</b></td>
<td align="right">21.9%</td>
<td align="right">30.4%</td>
<td align="right">24.4%</td>
<td align="right">20.5%</td>
<td align="right">17.2%</td>
<td align="right">2245</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟡 Remora</td>
<td align="right"><b>1496</b></td>
<td align="right">21.8%</td>
<td align="right">29.9%</td>
<td align="right">24.6%</td>
<td align="right">23.0%</td>
<td align="right">14.5%</td>
<td align="right">2081</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟡 Crone</td>
<td align="right"><b>1495</b></td>
<td align="right">21.5%</td>
<td align="right">27.9%</td>
<td align="right">22.8%</td>
<td align="right">21.7%</td>
<td align="right">16.9%</td>
<td align="right">2118</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟡 Philanthropist</td>
<td align="right"><b>1495</b></td>
<td align="right">21.5%</td>
<td align="right">32.0%</td>
<td align="right">27.0%</td>
<td align="right">18.6%</td>
<td align="right">15.2%</td>
<td align="right">2156</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟡 Laser</td>
<td align="right"><b>1495</b></td>
<td align="right">20.7%</td>
<td align="right">30.3%</td>
<td align="right">22.1%</td>
<td align="right">18.5%</td>
<td align="right">16.9%</td>
<td align="right">1936</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟡 Visionary</td>
<td align="right"><b>1495</b></td>
<td align="right">20.2%</td>
<td align="right">31.5%</td>
<td align="right">20.8%</td>
<td align="right">20.0%</td>
<td align="right">14.5%</td>
<td align="right">2133</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟡 Seeker</td>
<td align="right"><b>1495</b></td>
<td align="right">20.4%</td>
<td align="right">29.7%</td>
<td align="right">23.8%</td>
<td align="right">17.6%</td>
<td align="right">15.9%</td>
<td align="right">2200</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟡 Feline</td>
<td align="right"><b>1495</b></td>
<td align="right">21.7%</td>
<td align="right">33.3%</td>
<td align="right">22.3%</td>
<td align="right">19.0%</td>
<td align="right">18.0%</td>
<td align="right">1328</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟡 Converter</td>
<td align="right"><b>1495</b></td>
<td align="right">19.8%</td>
<td align="right">30.6%</td>
<td align="right">26.0%</td>
<td align="right">14.0%</td>
<td align="right">14.7%</td>
<td align="right">1378</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟡 Sage</td>
<td align="right"><b>1495</b></td>
<td align="right">21.0%</td>
<td align="right">31.6%</td>
<td align="right">24.9%</td>
<td align="right">17.9%</td>
<td align="right">15.8%</td>
<td align="right">1974</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟡 Hate</td>
<td align="right"><b>1495</b></td>
<td align="right">22.2%</td>
<td align="right">33.7%</td>
<td align="right">24.8%</td>
<td align="right">22.2%</td>
<td align="right">14.9%</td>
<td align="right">1962</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟡 Boomerang</td>
<td align="right"><b>1495</b></td>
<td align="right">22.4%</td>
<td align="right">38.8%</td>
<td align="right">24.6%</td>
<td align="right">17.7%</td>
<td align="right">16.5%</td>
<td align="right">1988</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟡 Phantom</td>
<td align="right"><b>1495</b></td>
<td align="right">19.1%</td>
<td align="right">30.3%</td>
<td align="right">18.9%</td>
<td align="right">18.1%</td>
<td align="right">14.5%</td>
<td align="right">1375</td>
</tr>
<tr>
<td align="left">91</td>
<td align="left">🟡 Altruist</td>
<td align="right"><b>1494</b></td>
<td align="right">20.3%</td>
<td align="right">33.4%</td>
<td align="right">24.0%</td>
<td align="right">16.3%</td>
<td align="right">13.9%</td>
<td align="right">2115</td>
</tr>
<tr>
<td align="left">92</td>
<td align="left">🟡 Genius</td>
<td align="right"><b>1494</b></td>
<td align="right">21.6%</td>
<td align="right">37.4%</td>
<td align="right">24.3%</td>
<td align="right">18.6%</td>
<td align="right">15.0%</td>
<td align="right">2094</td>
</tr>
<tr>
<td align="left">93</td>
<td align="left">🟡 Brute</td>
<td align="right"><b>1494</b></td>
<td align="right">21.3%</td>
<td align="right">33.6%</td>
<td align="right">24.1%</td>
<td align="right">18.6%</td>
<td align="right">15.3%</td>
<td align="right">2040</td>
</tr>
<tr>
<td align="left">94</td>
<td align="left">🟡 Sheriff</td>
<td align="right"><b>1494</b></td>
<td align="right">21.3%</td>
<td align="right">32.4%</td>
<td align="right">26.2%</td>
<td align="right">17.4%</td>
<td align="right">16.5%</td>
<td align="right">2192</td>
</tr>
<tr>
<td align="left">95</td>
<td align="left">🟡 Horde</td>
<td align="right"><b>1494</b></td>
<td align="right">20.3%</td>
<td align="right">29.7%</td>
<td align="right">23.7%</td>
<td align="right">18.2%</td>
<td align="right">15.8%</td>
<td align="right">1412</td>
</tr>
<tr>
<td align="left">96</td>
<td align="left">🟡 Clone</td>
<td align="right"><b>1494</b></td>
<td align="right">21.2%</td>
<td align="right">29.9%</td>
<td align="right">22.4%</td>
<td align="right">19.2%</td>
<td align="right">18.0%</td>
<td align="right">2167</td>
</tr>
<tr>
<td align="left">97</td>
<td align="left">🟡 Thief</td>
<td align="right"><b>1493</b></td>
<td align="right">20.0%</td>
<td align="right">30.9%</td>
<td align="right">21.0%</td>
<td align="right">18.5%</td>
<td align="right">15.0%</td>
<td align="right">2001</td>
</tr>
<tr>
<td align="left">98</td>
<td align="left">🟡 Zombie</td>
<td align="right"><b>1493</b></td>
<td align="right">21.8%</td>
<td align="right">30.9%</td>
<td align="right">26.0%</td>
<td align="right">20.8%</td>
<td align="right">15.2%</td>
<td align="right">2082</td>
</tr>
<tr>
<td align="left">99</td>
<td align="left">🟡 Siren</td>
<td align="right"><b>1493</b></td>
<td align="right">18.9%</td>
<td align="right">27.7%</td>
<td align="right">21.2%</td>
<td align="right">15.1%</td>
<td align="right">16.2%</td>
<td align="right">1394</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">🟡 Infiltrator</td>
<td align="right"><b>1493</b></td>
<td align="right">19.3%</td>
<td align="right">30.7%</td>
<td align="right">18.9%</td>
<td align="right">17.1%</td>
<td align="right">15.6%</td>
<td align="right">1370</td>
</tr>
<tr>
<td align="left">101</td>
<td align="left">🟡 Ethic</td>
<td align="right"><b>1493</b></td>
<td align="right">22.0%</td>
<td align="right">33.3%</td>
<td align="right">27.6%</td>
<td align="right">20.1%</td>
<td align="right">14.2%</td>
<td align="right">2137</td>
</tr>
<tr>
<td align="left">102</td>
<td align="left">🟡 Pincushion</td>
<td align="right"><b>1492</b></td>
<td align="right">20.9%</td>
<td align="right">34.1%</td>
<td align="right">21.2%</td>
<td align="right">22.4%</td>
<td align="right">13.1%</td>
<td align="right">1389</td>
</tr>
<tr>
<td align="left">103</td>
<td align="left">🟡 Scout</td>
<td align="right"><b>1492</b></td>
<td align="right">20.7%</td>
<td align="right">30.4%</td>
<td align="right">20.9%</td>
<td align="right">21.2%</td>
<td align="right">15.5%</td>
<td align="right">1912</td>
</tr>
<tr>
<td align="left">104</td>
<td align="left">🟡 Rage</td>
<td align="right"><b>1492</b></td>
<td align="right">20.4%</td>
<td align="right">30.9%</td>
<td align="right">23.0%</td>
<td align="right">19.1%</td>
<td align="right">14.7%</td>
<td align="right">1995</td>
</tr>
<tr>
<td align="left">105</td>
<td align="left">🟡 Deuce</td>
<td align="right"><b>1492</b></td>
<td align="right">20.1%</td>
<td align="right">31.6%</td>
<td align="right">22.5%</td>
<td align="right">19.2%</td>
<td align="right">13.2%</td>
<td align="right">2051</td>
</tr>
<tr>
<td align="left">106</td>
<td align="left">🟡 Assassin</td>
<td align="right"><b>1492</b></td>
<td align="right">21.3%</td>
<td align="right">34.3%</td>
<td align="right">25.0%</td>
<td align="right">17.2%</td>
<td align="right">16.2%</td>
<td align="right">2077</td>
</tr>
<tr>
<td align="left">107</td>
<td align="left">🟡 Underdog</td>
<td align="right"><b>1492</b></td>
<td align="right">20.1%</td>
<td align="right">30.2%</td>
<td align="right">25.1%</td>
<td align="right">16.2%</td>
<td align="right">15.2%</td>
<td align="right">2041</td>
</tr>
<tr>
<td align="left">108</td>
<td align="left">🟡 Hacker</td>
<td align="right"><b>1492</b></td>
<td align="right">20.6%</td>
<td align="right">35.6%</td>
<td align="right">22.5%</td>
<td align="right">18.5%</td>
<td align="right">13.4%</td>
<td align="right">2111</td>
</tr>
<tr>
<td align="left">109</td>
<td align="left">🟡 Chosen</td>
<td align="right"><b>1492</b></td>
<td align="right">20.2%</td>
<td align="right">30.9%</td>
<td align="right">24.4%</td>
<td align="right">17.7%</td>
<td align="right">14.1%</td>
<td align="right">2127</td>
</tr>
<tr>
<td align="left">110</td>
<td align="left">🟡 Mirror</td>
<td align="right"><b>1492</b></td>
<td align="right">21.2%</td>
<td align="right">30.0%</td>
<td align="right">24.2%</td>
<td align="right">20.2%</td>
<td align="right">16.1%</td>
<td align="right">2054</td>
</tr>
<tr>
<td align="left">111</td>
<td align="left">🟡 Healer</td>
<td align="right"><b>1492</b></td>
<td align="right">22.6%</td>
<td align="right">33.1%</td>
<td align="right">26.0%</td>
<td align="right">21.0%</td>
<td align="right">16.8%</td>
<td align="right">2044</td>
</tr>
<tr>
<td align="left">112</td>
<td align="left">🟡 Empath</td>
<td align="right"><b>1491</b></td>
<td align="right">21.3%</td>
<td align="right">34.0%</td>
<td align="right">24.9%</td>
<td align="right">18.4%</td>
<td align="right">15.2%</td>
<td align="right">2115</td>
</tr>
<tr>
<td align="left">113</td>
<td align="left">🟡 Claw</td>
<td align="right"><b>1491</b></td>
<td align="right">20.5%</td>
<td align="right">32.5%</td>
<td align="right">21.8%</td>
<td align="right">17.0%</td>
<td align="right">16.7%</td>
<td align="right">2143</td>
</tr>
<tr>
<td align="left">114</td>
<td align="left">🟡 Loser</td>
<td align="right"><b>1491</b></td>
<td align="right">17.9%</td>
<td align="right">30.7%</td>
<td align="right">25.1%</td>
<td align="right">16.7%</td>
<td align="right">7.8%</td>
<td align="right">2186</td>
</tr>
<tr>
<td align="left">115</td>
<td align="left">🟡 Tick-Tock</td>
<td align="right"><b>1491</b></td>
<td align="right">21.0%</td>
<td align="right">33.0%</td>
<td align="right">22.8%</td>
<td align="right">18.4%</td>
<td align="right">16.4%</td>
<td align="right">2210</td>
</tr>
<tr>
<td align="left">116</td>
<td align="left">🟡 Pentaform</td>
<td align="right"><b>1490</b></td>
<td align="right">21.2%</td>
<td align="right">29.9%</td>
<td align="right">25.2%</td>
<td align="right">18.2%</td>
<td align="right">16.7%</td>
<td align="right">2087</td>
</tr>
<tr>
<td align="left">117</td>
<td align="left">🟡 Calculator</td>
<td align="right"><b>1490</b></td>
<td align="right">20.1%</td>
<td align="right">29.4%</td>
<td align="right">25.4%</td>
<td align="right">18.9%</td>
<td align="right">12.6%</td>
<td align="right">2123</td>
</tr>
<tr>
<td align="left">118</td>
<td align="left">🟡 Negator</td>
<td align="right"><b>1490</b></td>
<td align="right">21.5%</td>
<td align="right">34.9%</td>
<td align="right">24.8%</td>
<td align="right">16.4%</td>
<td align="right">16.6%</td>
<td align="right">2056</td>
</tr>
<tr>
<td align="left">119</td>
<td align="left">🟡 Silencer</td>
<td align="right"><b>1490</b></td>
<td align="right">22.0%</td>
<td align="right">35.1%</td>
<td align="right">23.9%</td>
<td align="right">20.0%</td>
<td align="right">15.1%</td>
<td align="right">2149</td>
</tr>
<tr>
<td align="left">120</td>
<td align="left">🟡 Yin</td>
<td align="right"><b>1490</b></td>
<td align="right">21.3%</td>
<td align="right">35.0%</td>
<td align="right">24.5%</td>
<td align="right">18.3%</td>
<td align="right">15.7%</td>
<td align="right">2117</td>
</tr>
<tr>
<td align="left">121</td>
<td align="left">🟡 Citadel</td>
<td align="right"><b>1490</b></td>
<td align="right">21.3%</td>
<td align="right">32.2%</td>
<td align="right">22.9%</td>
<td align="right">21.6%</td>
<td align="right">14.5%</td>
<td align="right">2171</td>
</tr>
<tr>
<td align="left">122</td>
<td align="left">🟡 Sorcerer</td>
<td align="right"><b>1489</b></td>
<td align="right">20.4%</td>
<td align="right">29.2%</td>
<td align="right">24.2%</td>
<td align="right">17.3%</td>
<td align="right">15.8%</td>
<td align="right">2161</td>
</tr>
<tr>
<td align="left">123</td>
<td align="left">🟡 Reserve</td>
<td align="right"><b>1489</b></td>
<td align="right">19.5%</td>
<td align="right">29.1%</td>
<td align="right">20.5%</td>
<td align="right">16.5%</td>
<td align="right">16.3%</td>
<td align="right">2072</td>
</tr>
<tr>
<td align="left">124</td>
<td align="left">🟡 Mite</td>
<td align="right"><b>1489</b></td>
<td align="right">20.9%</td>
<td align="right">32.5%</td>
<td align="right">24.7%</td>
<td align="right">18.4%</td>
<td align="right">14.4%</td>
<td align="right">2041</td>
</tr>
<tr>
<td align="left">125</td>
<td align="left">🟡 Antimatter</td>
<td align="right"><b>1489</b></td>
<td align="right">18.0%</td>
<td align="right">30.5%</td>
<td align="right">25.7%</td>
<td align="right">17.4%</td>
<td align="right">7.3%</td>
<td align="right">2213</td>
</tr>
<tr>
<td align="left">126</td>
<td align="left">🟡 Sniveler</td>
<td align="right"><b>1488</b></td>
<td align="right">21.0%</td>
<td align="right">27.6%</td>
<td align="right">24.5%</td>
<td align="right">20.2%</td>
<td align="right">15.9%</td>
<td align="right">2173</td>
</tr>
<tr>
<td align="left">127</td>
<td align="left">🟡 Masochist</td>
<td align="right"><b>1488</b></td>
<td align="right">20.3%</td>
<td align="right">27.3%</td>
<td align="right">23.7%</td>
<td align="right">16.2%</td>
<td align="right">17.6%</td>
<td align="right">2021</td>
</tr>
<tr>
<td align="left">128</td>
<td align="left">🟡 Butler</td>
<td align="right"><b>1488</b></td>
<td align="right">20.5%</td>
<td align="right">33.8%</td>
<td align="right">21.4%</td>
<td align="right">17.7%</td>
<td align="right">15.7%</td>
<td align="right">2163</td>
</tr>
<tr>
<td align="left">129</td>
<td align="left">🟡 Pickpocket</td>
<td align="right"><b>1486</b></td>
<td align="right">20.2%</td>
<td align="right">27.2%</td>
<td align="right">24.4%</td>
<td align="right">18.1%</td>
<td align="right">15.9%</td>
<td align="right">2136</td>
</tr>
</tbody>
</table>


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
```

</details>


<!-- SIMULATION_RESULTS_START -->

## Simulation Results

**Total Games Simulated:** 499,998
**Solo Victories:** 491,282
**Shared Victories:** 8,716
**Average Game Length:** 4.8 turns
**Last Updated:** 2025-12-30T18:35:39

### Alien Power Rankings (by ELO)

| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |
|------|-------|-----|----------|-------|-----------|--------|
| 1 | Machine | -98127 | 57.9% | 11123 | 6260 | 184 |
| 2 | Predator | -98252 | 24.1% | 11257 | 2626 | 92 |
| 3 | Horde | -98271 | 21.3% | 11283 | 2321 | 82 |
| 4 | Battlemaster | -98278 | 25.0% | 11263 | 2737 | 78 |
| 5 | Tempest | -98279 | 21.4% | 11360 | 2353 | 77 |
| 6 | Parasite | -98283 | 46.2% | 11321 | 5153 | 79 |
| 7 | Insect | -98293 | 25.0% | 11084 | 2679 | 88 |
| 8 | Trader | -98295 | 26.1% | 11338 | 2857 | 99 |
| 9 | Exile | -98297 | 28.5% | 11244 | 3106 | 98 |
| 10 | Dragon | -98303 | 21.1% | 11275 | 2286 | 94 |
| 11 | Grudge | -98303 | 21.3% | 11336 | 2335 | 83 |
| 12 | Assassin | -98311 | 20.9% | 11246 | 2265 | 85 |
| 13 | Fury | -98318 | 22.2% | 11301 | 2434 | 78 |
| 14 | Zenith | -98320 | 23.7% | 11368 | 2609 | 88 |
| 15 | Pentaform | -98324 | 20.9% | 11391 | 2289 | 89 |
| 16 | Hunter | -98324 | 20.9% | 11208 | 2262 | 84 |
| 17 | Kamikazee | -98324 | 23.7% | 11221 | 2615 | 44 |
| 18 | Masochist | -98326 | 21.7% | 11251 | 2341 | 95 |
| 19 | Vacuum | -98328 | 23.5% | 11250 | 2555 | 94 |
| 20 | Disease | -98330 | 28.0% | 11305 | 3045 | 123 |
| 21 | Gambit | -98332 | 21.3% | 11357 | 2337 | 79 |
| 22 | Overlord | -98333 | 21.6% | 11096 | 2320 | 74 |
| 23 | Illusionist | -98337 | 21.8% | 11204 | 2345 | 94 |
| 24 | Nightmare | -98338 | 21.8% | 11175 | 2363 | 69 |
| 25 | Xenophobe | -98339 | 23.2% | 11192 | 2508 | 92 |
| 26 | Laser | -98340 | 21.6% | 11253 | 2337 | 94 |
| 27 | Symbiote | -98341 | 30.1% | 11252 | 3265 | 126 |
| 28 | Fanatic | -98343 | 21.7% | 11249 | 2355 | 86 |
| 29 | Coordinator | -98343 | 20.7% | 11340 | 2257 | 93 |
| 30 | Witch | -98345 | 21.5% | 11212 | 2320 | 96 |
| 31 | Sheriff | -98346 | 20.7% | 11378 | 2276 | 77 |
| 32 | Aura | -98346 | 21.7% | 11220 | 2346 | 86 |
| 33 | Noble | -98347 | 21.9% | 11156 | 2345 | 97 |
| 34 | Ranger | -98347 | 31.5% | 11206 | 3428 | 104 |
| 35 | Remora | -98348 | 21.5% | 11266 | 2321 | 96 |
| 36 | Hate | -98348 | 21.1% | 11216 | 2300 | 71 |
| 37 | Silencer | -98350 | 21.2% | 11203 | 2296 | 82 |
| 38 | Mimic | -98351 | 21.5% | 11264 | 2341 | 84 |
| 39 | Decoy | -98352 | 21.1% | 11341 | 2294 | 95 |
| 40 | Glutton | -98353 | 21.2% | 11342 | 2324 | 79 |
| ... | *160 more aliens* | ... | ... | ... | ... | ... |

<!-- SIMULATION_RESULTS_END -->

## Legacy Version

The original 2016 simulator is preserved in `Simulator.py` and `main.py` for reference.
