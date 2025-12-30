# Cosmic Encounter Simulator 2

A comprehensive simulation of the board game Cosmic Encounter, designed to analyze alien power balance and game dynamics across various configurations.

## Features

- **129 Alien Powers** implemented with proper game mechanics
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

> **22,000** games simulated | Last updated: 2025-12-30 17:58
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
<td align="right"><b>1554</b></td>
<td align="right">57.3%</td>
<td align="right">71.2%</td>
<td align="right">64.6%</td>
<td align="right">58.8%</td>
<td align="right">44.6%</td>
<td align="right">973</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🔵 Parasite</td>
<td align="right"><b>1554</b></td>
<td align="right">47.5%</td>
<td align="right">46.6%</td>
<td align="right">49.8%</td>
<td align="right">47.8%</td>
<td align="right">46.2%</td>
<td align="right">1018</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Disease</td>
<td align="right"><b>1522</b></td>
<td align="right">28.5%</td>
<td align="right">39.4%</td>
<td align="right">30.8%</td>
<td align="right">24.0%</td>
<td align="right">24.1%</td>
<td align="right">1057</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Warpish</td>
<td align="right"><b>1521</b></td>
<td align="right">31.7%</td>
<td align="right">46.3%</td>
<td align="right">43.0%</td>
<td align="right">25.5%</td>
<td align="right">24.3%</td>
<td align="right">939</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Symbiote</td>
<td align="right"><b>1519</b></td>
<td align="right">29.0%</td>
<td align="right">53.9%</td>
<td align="right">32.4%</td>
<td align="right">23.4%</td>
<td align="right">18.6%</td>
<td align="right">933</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Mutant</td>
<td align="right"><b>1518</b></td>
<td align="right">27.6%</td>
<td align="right">45.4%</td>
<td align="right">32.2%</td>
<td align="right">27.7%</td>
<td align="right">16.4%</td>
<td align="right">1005</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Tripler</td>
<td align="right"><b>1516</b></td>
<td align="right">30.1%</td>
<td align="right">53.7%</td>
<td align="right">28.1%</td>
<td align="right">25.6%</td>
<td align="right">23.1%</td>
<td align="right">1035</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Pacifist</td>
<td align="right"><b>1512</b></td>
<td align="right">29.0%</td>
<td align="right">52.6%</td>
<td align="right">34.1%</td>
<td align="right">21.1%</td>
<td align="right">20.8%</td>
<td align="right">1012</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Human</td>
<td align="right"><b>1510</b></td>
<td align="right">24.8%</td>
<td align="right">39.8%</td>
<td align="right">31.6%</td>
<td align="right">18.6%</td>
<td align="right">16.7%</td>
<td align="right">994</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Macron</td>
<td align="right"><b>1509</b></td>
<td align="right">27.6%</td>
<td align="right">45.7%</td>
<td align="right">25.4%</td>
<td align="right">26.1%</td>
<td align="right">20.1%</td>
<td align="right">965</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Chronos</td>
<td align="right"><b>1508</b></td>
<td align="right">24.2%</td>
<td align="right">29.1%</td>
<td align="right">28.2%</td>
<td align="right">21.5%</td>
<td align="right">21.2%</td>
<td align="right">1056</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Shadow</td>
<td align="right"><b>1508</b></td>
<td align="right">25.8%</td>
<td align="right">44.7%</td>
<td align="right">29.2%</td>
<td align="right">21.6%</td>
<td align="right">16.8%</td>
<td align="right">1052</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Trader</td>
<td align="right"><b>1507</b></td>
<td align="right">26.8%</td>
<td align="right">44.0%</td>
<td align="right">32.9%</td>
<td align="right">20.9%</td>
<td align="right">18.1%</td>
<td align="right">995</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Virus</td>
<td align="right"><b>1507</b></td>
<td align="right">25.2%</td>
<td align="right">42.9%</td>
<td align="right">28.4%</td>
<td align="right">21.0%</td>
<td align="right">16.2%</td>
<td align="right">1058</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Aristocrat</td>
<td align="right"><b>1504</b></td>
<td align="right">28.9%</td>
<td align="right">35.7%</td>
<td align="right">26.4%</td>
<td align="right">33.3%</td>
<td align="right">23.7%</td>
<td align="right">263</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Grudge</td>
<td align="right"><b>1503</b></td>
<td align="right">21.6%</td>
<td align="right">30.8%</td>
<td align="right">20.6%</td>
<td align="right">21.7%</td>
<td align="right">17.9%</td>
<td align="right">1088</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Connoisseur</td>
<td align="right"><b>1503</b></td>
<td align="right">27.2%</td>
<td align="right">41.0%</td>
<td align="right">29.1%</td>
<td align="right">27.6%</td>
<td align="right">17.3%</td>
<td align="right">301</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Engineer</td>
<td align="right"><b>1503</b></td>
<td align="right">27.0%</td>
<td align="right">38.2%</td>
<td align="right">24.3%</td>
<td align="right">25.7%</td>
<td align="right">22.9%</td>
<td align="right">282</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Chrysalis</td>
<td align="right"><b>1503</b></td>
<td align="right">26.8%</td>
<td align="right">55.6%</td>
<td align="right">33.3%</td>
<td align="right">19.7%</td>
<td align="right">12.2%</td>
<td align="right">276</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Void</td>
<td align="right"><b>1503</b></td>
<td align="right">22.5%</td>
<td align="right">36.3%</td>
<td align="right">21.7%</td>
<td align="right">17.9%</td>
<td align="right">19.8%</td>
<td align="right">1004</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Ghast</td>
<td align="right"><b>1502</b></td>
<td align="right">26.1%</td>
<td align="right">48.9%</td>
<td align="right">28.6%</td>
<td align="right">20.0%</td>
<td align="right">18.6%</td>
<td align="right">268</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Gambler</td>
<td align="right"><b>1502</b></td>
<td align="right">21.6%</td>
<td align="right">27.8%</td>
<td align="right">23.6%</td>
<td align="right">20.8%</td>
<td align="right">17.5%</td>
<td align="right">1030</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Tyrant</td>
<td align="right"><b>1502</b></td>
<td align="right">22.7%</td>
<td align="right">38.8%</td>
<td align="right">23.5%</td>
<td align="right">16.5%</td>
<td align="right">19.5%</td>
<td align="right">858</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Insect</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">34.6%</td>
<td align="right">28.1%</td>
<td align="right">24.6%</td>
<td align="right">20.2%</td>
<td align="right">269</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Bulwark</td>
<td align="right"><b>1502</b></td>
<td align="right">25.6%</td>
<td align="right">32.7%</td>
<td align="right">32.8%</td>
<td align="right">21.5%</td>
<td align="right">19.6%</td>
<td align="right">273</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Invader</td>
<td align="right"><b>1502</b></td>
<td align="right">25.4%</td>
<td align="right">36.2%</td>
<td align="right">33.8%</td>
<td align="right">17.4%</td>
<td align="right">18.6%</td>
<td align="right">295</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Fury</td>
<td align="right"><b>1502</b></td>
<td align="right">23.3%</td>
<td align="right">28.9%</td>
<td align="right">28.2%</td>
<td align="right">19.3%</td>
<td align="right">20.4%</td>
<td align="right">947</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Amoeba</td>
<td align="right"><b>1502</b></td>
<td align="right">22.3%</td>
<td align="right">34.9%</td>
<td align="right">26.3%</td>
<td align="right">19.1%</td>
<td align="right">15.6%</td>
<td align="right">963</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟢 Schizoid</td>
<td align="right"><b>1502</b></td>
<td align="right">24.9%</td>
<td align="right">41.2%</td>
<td align="right">26.8%</td>
<td align="right">22.1%</td>
<td align="right">14.7%</td>
<td align="right">261</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟢 Battlemaster</td>
<td align="right"><b>1501</b></td>
<td align="right">24.7%</td>
<td align="right">50.0%</td>
<td align="right">16.4%</td>
<td align="right">22.7%</td>
<td align="right">19.3%</td>
<td align="right">255</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟢 Changeling</td>
<td align="right"><b>1501</b></td>
<td align="right">21.8%</td>
<td align="right">24.5%</td>
<td align="right">27.4%</td>
<td align="right">20.6%</td>
<td align="right">18.0%</td>
<td align="right">1019</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟢 Oracle</td>
<td align="right"><b>1501</b></td>
<td align="right">22.6%</td>
<td align="right">38.3%</td>
<td align="right">24.3%</td>
<td align="right">20.1%</td>
<td align="right">15.9%</td>
<td align="right">1009</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟢 Filch</td>
<td align="right"><b>1501</b></td>
<td align="right">21.9%</td>
<td align="right">34.1%</td>
<td align="right">26.4%</td>
<td align="right">18.9%</td>
<td align="right">15.1%</td>
<td align="right">991</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟢 Delegator</td>
<td align="right"><b>1501</b></td>
<td align="right">24.5%</td>
<td align="right">39.6%</td>
<td align="right">22.7%</td>
<td align="right">24.6%</td>
<td align="right">15.6%</td>
<td align="right">261</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟢 Fungus</td>
<td align="right"><b>1501</b></td>
<td align="right">24.3%</td>
<td align="right">33.3%</td>
<td align="right">30.8%</td>
<td align="right">18.3%</td>
<td align="right">22.4%</td>
<td align="right">280</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟢 Dictator</td>
<td align="right"><b>1501</b></td>
<td align="right">22.8%</td>
<td align="right">32.2%</td>
<td align="right">28.7%</td>
<td align="right">21.0%</td>
<td align="right">16.2%</td>
<td align="right">930</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟢 Ghoul</td>
<td align="right"><b>1501</b></td>
<td align="right">26.6%</td>
<td align="right">39.9%</td>
<td align="right">34.6%</td>
<td align="right">22.0%</td>
<td align="right">16.9%</td>
<td align="right">1000</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟢 Spiff</td>
<td align="right"><b>1501</b></td>
<td align="right">22.8%</td>
<td align="right">33.1%</td>
<td align="right">31.2%</td>
<td align="right">18.0%</td>
<td align="right">16.3%</td>
<td align="right">986</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟢 Bully</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">38.0%</td>
<td align="right">33.3%</td>
<td align="right">17.3%</td>
<td align="right">17.9%</td>
<td align="right">262</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟢 Diplomat</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">26.1%</td>
<td align="right">28.1%</td>
<td align="right">23.9%</td>
<td align="right">21.1%</td>
<td align="right">279</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟢 Miser</td>
<td align="right"><b>1501</b></td>
<td align="right">24.0%</td>
<td align="right">31.0%</td>
<td align="right">24.1%</td>
<td align="right">21.9%</td>
<td align="right">22.3%</td>
<td align="right">263</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟢 Warlock</td>
<td align="right"><b>1501</b></td>
<td align="right">21.2%</td>
<td align="right">28.8%</td>
<td align="right">28.0%</td>
<td align="right">18.6%</td>
<td align="right">15.2%</td>
<td align="right">867</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟢 Grief</td>
<td align="right"><b>1501</b></td>
<td align="right">23.8%</td>
<td align="right">45.5%</td>
<td align="right">23.7%</td>
<td align="right">19.5%</td>
<td align="right">17.0%</td>
<td align="right">273</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟢 Extortionist</td>
<td align="right"><b>1501</b></td>
<td align="right">23.6%</td>
<td align="right">28.9%</td>
<td align="right">13.8%</td>
<td align="right">28.6%</td>
<td align="right">24.5%</td>
<td align="right">275</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟢 Electron</td>
<td align="right"><b>1501</b></td>
<td align="right">23.4%</td>
<td align="right">32.7%</td>
<td align="right">29.2%</td>
<td align="right">15.4%</td>
<td align="right">20.4%</td>
<td align="right">295</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟢 Guardian</td>
<td align="right"><b>1500</b></td>
<td align="right">23.3%</td>
<td align="right">20.5%</td>
<td align="right">30.8%</td>
<td align="right">21.4%</td>
<td align="right">19.3%</td>
<td align="right">275</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟢 Glutton</td>
<td align="right"><b>1500</b></td>
<td align="right">23.2%</td>
<td align="right">30.6%</td>
<td align="right">30.9%</td>
<td align="right">21.7%</td>
<td align="right">15.0%</td>
<td align="right">267</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟡 Nightmare</td>
<td align="right"><b>1500</b></td>
<td align="right">20.7%</td>
<td align="right">29.9%</td>
<td align="right">15.3%</td>
<td align="right">21.3%</td>
<td align="right">18.6%</td>
<td align="right">907</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟡 Doppelganger</td>
<td align="right"><b>1500</b></td>
<td align="right">22.6%</td>
<td align="right">29.1%</td>
<td align="right">30.0%</td>
<td align="right">21.4%</td>
<td align="right">15.3%</td>
<td align="right">297</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟡 Leviathan</td>
<td align="right"><b>1500</b></td>
<td align="right">20.4%</td>
<td align="right">36.6%</td>
<td align="right">20.3%</td>
<td align="right">16.9%</td>
<td align="right">16.7%</td>
<td align="right">1054</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟡 Prophet</td>
<td align="right"><b>1500</b></td>
<td align="right">22.1%</td>
<td align="right">32.4%</td>
<td align="right">33.3%</td>
<td align="right">26.1%</td>
<td align="right">5.0%</td>
<td align="right">249</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟡 Warrior</td>
<td align="right"><b>1500</b></td>
<td align="right">23.7%</td>
<td align="right">39.1%</td>
<td align="right">24.4%</td>
<td align="right">19.5%</td>
<td align="right">18.7%</td>
<td align="right">995</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟡 Harbinger</td>
<td align="right"><b>1500</b></td>
<td align="right">21.9%</td>
<td align="right">36.6%</td>
<td align="right">21.4%</td>
<td align="right">18.6%</td>
<td align="right">18.3%</td>
<td align="right">279</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟡 Magician</td>
<td align="right"><b>1499</b></td>
<td align="right">21.8%</td>
<td align="right">27.8%</td>
<td align="right">23.7%</td>
<td align="right">22.5%</td>
<td align="right">17.6%</td>
<td align="right">266</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟡 Roach</td>
<td align="right"><b>1499</b></td>
<td align="right">21.6%</td>
<td align="right">25.0%</td>
<td align="right">24.6%</td>
<td align="right">26.2%</td>
<td align="right">15.1%</td>
<td align="right">259</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟡 Jester</td>
<td align="right"><b>1499</b></td>
<td align="right">21.4%</td>
<td align="right">41.7%</td>
<td align="right">25.9%</td>
<td align="right">17.9%</td>
<td align="right">9.5%</td>
<td align="right">257</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟡 Barbarian</td>
<td align="right"><b>1499</b></td>
<td align="right">21.6%</td>
<td align="right">28.2%</td>
<td align="right">25.4%</td>
<td align="right">20.0%</td>
<td align="right">17.2%</td>
<td align="right">872</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟡 Vox</td>
<td align="right"><b>1499</b></td>
<td align="right">21.7%</td>
<td align="right">35.4%</td>
<td align="right">24.2%</td>
<td align="right">19.7%</td>
<td align="right">14.7%</td>
<td align="right">905</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟡 Dragon</td>
<td align="right"><b>1499</b></td>
<td align="right">22.1%</td>
<td align="right">32.7%</td>
<td align="right">20.6%</td>
<td align="right">20.8%</td>
<td align="right">17.7%</td>
<td align="right">832</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟡 Foam</td>
<td align="right"><b>1499</b></td>
<td align="right">20.7%</td>
<td align="right">12.8%</td>
<td align="right">30.8%</td>
<td align="right">21.7%</td>
<td align="right">16.7%</td>
<td align="right">285</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟡 Mimic</td>
<td align="right"><b>1499</b></td>
<td align="right">22.0%</td>
<td align="right">35.5%</td>
<td align="right">24.4%</td>
<td align="right">23.0%</td>
<td align="right">14.0%</td>
<td align="right">877</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟡 Pirate</td>
<td align="right"><b>1499</b></td>
<td align="right">22.7%</td>
<td align="right">35.5%</td>
<td align="right">21.5%</td>
<td align="right">20.6%</td>
<td align="right">18.9%</td>
<td align="right">912</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟡 Fodder</td>
<td align="right"><b>1499</b></td>
<td align="right">20.5%</td>
<td align="right">31.5%</td>
<td align="right">26.2%</td>
<td align="right">16.5%</td>
<td align="right">15.0%</td>
<td align="right">317</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟡 Reincarnator</td>
<td align="right"><b>1499</b></td>
<td align="right">21.0%</td>
<td align="right">36.2%</td>
<td align="right">22.6%</td>
<td align="right">16.4%</td>
<td align="right">17.2%</td>
<td align="right">1010</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟡 Poison</td>
<td align="right"><b>1499</b></td>
<td align="right">21.9%</td>
<td align="right">32.1%</td>
<td align="right">27.1%</td>
<td align="right">19.5%</td>
<td align="right">16.5%</td>
<td align="right">940</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟡 Cavalry</td>
<td align="right"><b>1499</b></td>
<td align="right">20.5%</td>
<td align="right">21.3%</td>
<td align="right">28.8%</td>
<td align="right">23.2%</td>
<td align="right">13.3%</td>
<td align="right">293</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟡 Architect</td>
<td align="right"><b>1498</b></td>
<td align="right">20.3%</td>
<td align="right">45.2%</td>
<td align="right">15.2%</td>
<td align="right">19.3%</td>
<td align="right">15.5%</td>
<td align="right">251</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟡 Witch</td>
<td align="right"><b>1498</b></td>
<td align="right">19.8%</td>
<td align="right">40.0%</td>
<td align="right">22.4%</td>
<td align="right">14.8%</td>
<td align="right">14.0%</td>
<td align="right">298</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟡 Crystal</td>
<td align="right"><b>1498</b></td>
<td align="right">20.0%</td>
<td align="right">28.0%</td>
<td align="right">22.0%</td>
<td align="right">16.1%</td>
<td align="right">17.1%</td>
<td align="right">878</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟡 Phantom</td>
<td align="right"><b>1498</b></td>
<td align="right">19.4%</td>
<td align="right">26.8%</td>
<td align="right">18.1%</td>
<td align="right">23.9%</td>
<td align="right">12.5%</td>
<td align="right">289</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟡 Converter</td>
<td align="right"><b>1498</b></td>
<td align="right">19.2%</td>
<td align="right">24.5%</td>
<td align="right">22.4%</td>
<td align="right">16.7%</td>
<td align="right">15.3%</td>
<td align="right">276</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟡 Vacuum</td>
<td align="right"><b>1498</b></td>
<td align="right">21.1%</td>
<td align="right">32.6%</td>
<td align="right">23.7%</td>
<td align="right">17.6%</td>
<td align="right">15.7%</td>
<td align="right">1009</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟡 Cudgel</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">36.4%</td>
<td align="right">25.9%</td>
<td align="right">19.9%</td>
<td align="right">14.9%</td>
<td align="right">1000</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟡 Vulture</td>
<td align="right"><b>1498</b></td>
<td align="right">19.0%</td>
<td align="right">27.5%</td>
<td align="right">25.0%</td>
<td align="right">14.1%</td>
<td align="right">14.8%</td>
<td align="right">248</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟡 Surge</td>
<td align="right"><b>1497</b></td>
<td align="right">20.9%</td>
<td align="right">33.3%</td>
<td align="right">22.5%</td>
<td align="right">21.0%</td>
<td align="right">13.8%</td>
<td align="right">1033</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟡 Patriot</td>
<td align="right"><b>1497</b></td>
<td align="right">20.9%</td>
<td align="right">38.4%</td>
<td align="right">21.3%</td>
<td align="right">18.6%</td>
<td align="right">13.9%</td>
<td align="right">911</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟡 Feline</td>
<td align="right"><b>1497</b></td>
<td align="right">17.9%</td>
<td align="right">27.5%</td>
<td align="right">25.9%</td>
<td align="right">16.3%</td>
<td align="right">11.4%</td>
<td align="right">285</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟡 Laser</td>
<td align="right"><b>1497</b></td>
<td align="right">20.6%</td>
<td align="right">26.7%</td>
<td align="right">21.6%</td>
<td align="right">18.8%</td>
<td align="right">18.3%</td>
<td align="right">821</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟡 Horde</td>
<td align="right"><b>1497</b></td>
<td align="right">17.7%</td>
<td align="right">34.0%</td>
<td align="right">9.4%</td>
<td align="right">15.8%</td>
<td align="right">16.3%</td>
<td align="right">288</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟡 Siren</td>
<td align="right"><b>1497</b></td>
<td align="right">17.6%</td>
<td align="right">22.0%</td>
<td align="right">16.0%</td>
<td align="right">19.1%</td>
<td align="right">15.7%</td>
<td align="right">289</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟡 Fido</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">40.8%</td>
<td align="right">24.5%</td>
<td align="right">17.8%</td>
<td align="right">17.0%</td>
<td align="right">1055</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟡 Crone</td>
<td align="right"><b>1497</b></td>
<td align="right">19.9%</td>
<td align="right">23.7%</td>
<td align="right">20.1%</td>
<td align="right">20.0%</td>
<td align="right">17.7%</td>
<td align="right">1015</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟡 Observer</td>
<td align="right"><b>1496</b></td>
<td align="right">21.0%</td>
<td align="right">33.3%</td>
<td align="right">25.7%</td>
<td align="right">17.0%</td>
<td align="right">15.3%</td>
<td align="right">1033</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟡 Infiltrator</td>
<td align="right"><b>1496</b></td>
<td align="right">17.2%</td>
<td align="right">30.0%</td>
<td align="right">14.6%</td>
<td align="right">10.5%</td>
<td align="right">18.6%</td>
<td align="right">261</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟡 Visionary</td>
<td align="right"><b>1496</b></td>
<td align="right">21.3%</td>
<td align="right">37.7%</td>
<td align="right">20.4%</td>
<td align="right">20.8%</td>
<td align="right">14.5%</td>
<td align="right">1018</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟡 Seeker</td>
<td align="right"><b>1496</b></td>
<td align="right">20.7%</td>
<td align="right">28.0%</td>
<td align="right">27.2%</td>
<td align="right">17.3%</td>
<td align="right">15.6%</td>
<td align="right">1061</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟡 Remora</td>
<td align="right"><b>1496</b></td>
<td align="right">21.0%</td>
<td align="right">33.7%</td>
<td align="right">21.3%</td>
<td align="right">23.5%</td>
<td align="right">11.4%</td>
<td align="right">992</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟡 Kamikazee</td>
<td align="right"><b>1496</b></td>
<td align="right">22.5%</td>
<td align="right">31.2%</td>
<td align="right">30.0%</td>
<td align="right">19.2%</td>
<td align="right">16.2%</td>
<td align="right">1011</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟡 Philanthropist</td>
<td align="right"><b>1496</b></td>
<td align="right">21.5%</td>
<td align="right">31.6%</td>
<td align="right">24.9%</td>
<td align="right">22.1%</td>
<td align="right">14.0%</td>
<td align="right">968</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟡 Sage</td>
<td align="right"><b>1496</b></td>
<td align="right">20.2%</td>
<td align="right">31.6%</td>
<td align="right">26.5%</td>
<td align="right">17.1%</td>
<td align="right">12.6%</td>
<td align="right">913</td>
</tr>
<tr>
<td align="left">91</td>
<td align="left">🟡 Giver</td>
<td align="right"><b>1496</b></td>
<td align="right">22.7%</td>
<td align="right">28.6%</td>
<td align="right">27.8%</td>
<td align="right">22.6%</td>
<td align="right">16.4%</td>
<td align="right">1070</td>
</tr>
<tr>
<td align="left">92</td>
<td align="left">🟡 Altruist</td>
<td align="right"><b>1496</b></td>
<td align="right">19.9%</td>
<td align="right">31.9%</td>
<td align="right">22.4%</td>
<td align="right">16.9%</td>
<td align="right">13.6%</td>
<td align="right">1012</td>
</tr>
<tr>
<td align="left">93</td>
<td align="left">🟡 Brute</td>
<td align="right"><b>1496</b></td>
<td align="right">21.5%</td>
<td align="right">34.6%</td>
<td align="right">25.5%</td>
<td align="right">17.5%</td>
<td align="right">14.4%</td>
<td align="right">875</td>
</tr>
<tr>
<td align="left">94</td>
<td align="left">🟡 Hate</td>
<td align="right"><b>1496</b></td>
<td align="right">19.4%</td>
<td align="right">29.6%</td>
<td align="right">22.4%</td>
<td align="right">20.1%</td>
<td align="right">12.6%</td>
<td align="right">901</td>
</tr>
<tr>
<td align="left">95</td>
<td align="left">🟡 Genius</td>
<td align="right"><b>1495</b></td>
<td align="right">21.9%</td>
<td align="right">43.7%</td>
<td align="right">22.7%</td>
<td align="right">16.9%</td>
<td align="right">15.7%</td>
<td align="right">976</td>
</tr>
<tr>
<td align="left">96</td>
<td align="left">🟡 Sheriff</td>
<td align="right"><b>1495</b></td>
<td align="right">19.6%</td>
<td align="right">30.4%</td>
<td align="right">23.6%</td>
<td align="right">15.6%</td>
<td align="right">16.2%</td>
<td align="right">1080</td>
</tr>
<tr>
<td align="left">97</td>
<td align="left">🟡 Pincushion</td>
<td align="right"><b>1495</b></td>
<td align="right">15.3%</td>
<td align="right">20.0%</td>
<td align="right">16.1%</td>
<td align="right">16.9%</td>
<td align="right">11.8%</td>
<td align="right">261</td>
</tr>
<tr>
<td align="left">98</td>
<td align="left">🟡 Clone</td>
<td align="right"><b>1495</b></td>
<td align="right">21.1%</td>
<td align="right">29.0%</td>
<td align="right">22.2%</td>
<td align="right">19.6%</td>
<td align="right">18.1%</td>
<td align="right">1051</td>
</tr>
<tr>
<td align="left">99</td>
<td align="left">🟡 Boomerang</td>
<td align="right"><b>1495</b></td>
<td align="right">21.2%</td>
<td align="right">40.1%</td>
<td align="right">19.6%</td>
<td align="right">18.7%</td>
<td align="right">14.6%</td>
<td align="right">883</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">🟡 Thief</td>
<td align="right"><b>1495</b></td>
<td align="right">19.4%</td>
<td align="right">32.5%</td>
<td align="right">15.3%</td>
<td align="right">16.7%</td>
<td align="right">17.1%</td>
<td align="right">866</td>
</tr>
<tr>
<td align="left">101</td>
<td align="left">🟡 Rage</td>
<td align="right"><b>1494</b></td>
<td align="right">19.6%</td>
<td align="right">29.1%</td>
<td align="right">22.8%</td>
<td align="right">19.4%</td>
<td align="right">13.5%</td>
<td align="right">927</td>
</tr>
<tr>
<td align="left">102</td>
<td align="left">🟡 Zombie</td>
<td align="right"><b>1494</b></td>
<td align="right">20.8%</td>
<td align="right">28.1%</td>
<td align="right">24.3%</td>
<td align="right">20.1%</td>
<td align="right">14.8%</td>
<td align="right">1005</td>
</tr>
<tr>
<td align="left">103</td>
<td align="left">🟡 Loser</td>
<td align="right"><b>1494</b></td>
<td align="right">17.8%</td>
<td align="right">31.9%</td>
<td align="right">19.7%</td>
<td align="right">19.4%</td>
<td align="right">8.5%</td>
<td align="right">1031</td>
</tr>
<tr>
<td align="left">104</td>
<td align="left">🟡 Scout</td>
<td align="right"><b>1494</b></td>
<td align="right">19.7%</td>
<td align="right">25.5%</td>
<td align="right">23.1%</td>
<td align="right">21.1%</td>
<td align="right">13.4%</td>
<td align="right">860</td>
</tr>
<tr>
<td align="left">105</td>
<td align="left">🟡 Deuce</td>
<td align="right"><b>1494</b></td>
<td align="right">20.1%</td>
<td align="right">31.0%</td>
<td align="right">22.8%</td>
<td align="right">20.7%</td>
<td align="right">12.9%</td>
<td align="right">907</td>
</tr>
<tr>
<td align="left">106</td>
<td align="left">🟡 Underdog</td>
<td align="right"><b>1494</b></td>
<td align="right">19.7%</td>
<td align="right">32.6%</td>
<td align="right">25.0%</td>
<td align="right">15.4%</td>
<td align="right">13.5%</td>
<td align="right">888</td>
</tr>
<tr>
<td align="left">107</td>
<td align="left">🟡 Chosen</td>
<td align="right"><b>1493</b></td>
<td align="right">19.6%</td>
<td align="right">35.3%</td>
<td align="right">23.1%</td>
<td align="right">16.6%</td>
<td align="right">11.5%</td>
<td align="right">1001</td>
</tr>
<tr>
<td align="left">108</td>
<td align="left">🟡 Ethic</td>
<td align="right"><b>1493</b></td>
<td align="right">20.9%</td>
<td align="right">29.9%</td>
<td align="right">24.1%</td>
<td align="right">22.0%</td>
<td align="right">13.5%</td>
<td align="right">1070</td>
</tr>
<tr>
<td align="left">109</td>
<td align="left">🟡 Hacker</td>
<td align="right"><b>1493</b></td>
<td align="right">21.2%</td>
<td align="right">33.7%</td>
<td align="right">24.0%</td>
<td align="right">18.4%</td>
<td align="right">15.4%</td>
<td align="right">982</td>
</tr>
<tr>
<td align="left">110</td>
<td align="left">🟡 Assassin</td>
<td align="right"><b>1493</b></td>
<td align="right">21.1%</td>
<td align="right">34.0%</td>
<td align="right">25.2%</td>
<td align="right">15.8%</td>
<td align="right">16.1%</td>
<td align="right">971</td>
</tr>
<tr>
<td align="left">111</td>
<td align="left">🟡 Mirror</td>
<td align="right"><b>1493</b></td>
<td align="right">20.1%</td>
<td align="right">30.1%</td>
<td align="right">23.0%</td>
<td align="right">17.8%</td>
<td align="right">15.4%</td>
<td align="right">955</td>
</tr>
<tr>
<td align="left">112</td>
<td align="left">🟡 Claw</td>
<td align="right"><b>1492</b></td>
<td align="right">19.7%</td>
<td align="right">31.4%</td>
<td align="right">23.4%</td>
<td align="right">16.2%</td>
<td align="right">14.2%</td>
<td align="right">1059</td>
</tr>
<tr>
<td align="left">113</td>
<td align="left">🟡 Healer</td>
<td align="right"><b>1492</b></td>
<td align="right">21.4%</td>
<td align="right">31.4%</td>
<td align="right">23.9%</td>
<td align="right">18.7%</td>
<td align="right">17.4%</td>
<td align="right">973</td>
</tr>
<tr>
<td align="left">114</td>
<td align="left">🟡 Empath</td>
<td align="right"><b>1492</b></td>
<td align="right">20.0%</td>
<td align="right">32.1%</td>
<td align="right">29.0%</td>
<td align="right">14.6%</td>
<td align="right">13.9%</td>
<td align="right">983</td>
</tr>
<tr>
<td align="left">115</td>
<td align="left">🟡 Calculator</td>
<td align="right"><b>1492</b></td>
<td align="right">20.6%</td>
<td align="right">26.7%</td>
<td align="right">24.7%</td>
<td align="right">21.0%</td>
<td align="right">14.0%</td>
<td align="right">1018</td>
</tr>
<tr>
<td align="left">116</td>
<td align="left">🟡 Yin</td>
<td align="right"><b>1492</b></td>
<td align="right">20.7%</td>
<td align="right">34.0%</td>
<td align="right">23.0%</td>
<td align="right">20.1%</td>
<td align="right">13.8%</td>
<td align="right">1005</td>
</tr>
<tr>
<td align="left">117</td>
<td align="left">🟡 Pentaform</td>
<td align="right"><b>1492</b></td>
<td align="right">19.6%</td>
<td align="right">25.3%</td>
<td align="right">22.4%</td>
<td align="right">18.6%</td>
<td align="right">15.8%</td>
<td align="right">1004</td>
</tr>
<tr>
<td align="left">118</td>
<td align="left">🟡 Citadel</td>
<td align="right"><b>1491</b></td>
<td align="right">20.2%</td>
<td align="right">31.3%</td>
<td align="right">20.8%</td>
<td align="right">21.8%</td>
<td align="right">13.3%</td>
<td align="right">1014</td>
</tr>
<tr>
<td align="left">119</td>
<td align="left">🟡 Antimatter</td>
<td align="right"><b>1491</b></td>
<td align="right">18.3%</td>
<td align="right">33.3%</td>
<td align="right">24.3%</td>
<td align="right">17.5%</td>
<td align="right">8.0%</td>
<td align="right">1098</td>
</tr>
<tr>
<td align="left">120</td>
<td align="left">🟡 Reserve</td>
<td align="right"><b>1491</b></td>
<td align="right">20.0%</td>
<td align="right">33.7%</td>
<td align="right">18.9%</td>
<td align="right">17.5%</td>
<td align="right">15.3%</td>
<td align="right">976</td>
</tr>
<tr>
<td align="left">121</td>
<td align="left">🟡 Tick-Tock</td>
<td align="right"><b>1491</b></td>
<td align="right">22.3%</td>
<td align="right">34.1%</td>
<td align="right">22.5%</td>
<td align="right">18.3%</td>
<td align="right">19.5%</td>
<td align="right">1027</td>
</tr>
<tr>
<td align="left">122</td>
<td align="left">🟡 Sorcerer</td>
<td align="right"><b>1491</b></td>
<td align="right">19.7%</td>
<td align="right">28.0%</td>
<td align="right">21.6%</td>
<td align="right">17.8%</td>
<td align="right">16.1%</td>
<td align="right">1009</td>
</tr>
<tr>
<td align="left">123</td>
<td align="left">🟡 Negator</td>
<td align="right"><b>1491</b></td>
<td align="right">20.8%</td>
<td align="right">37.0%</td>
<td align="right">23.8%</td>
<td align="right">15.8%</td>
<td align="right">15.0%</td>
<td align="right">1005</td>
</tr>
<tr>
<td align="left">124</td>
<td align="left">🟡 Silencer</td>
<td align="right"><b>1490</b></td>
<td align="right">22.3%</td>
<td align="right">32.0%</td>
<td align="right">26.9%</td>
<td align="right">22.3%</td>
<td align="right">13.7%</td>
<td align="right">999</td>
</tr>
<tr>
<td align="left">125</td>
<td align="left">🟡 Masochist</td>
<td align="right"><b>1490</b></td>
<td align="right">20.3%</td>
<td align="right">25.5%</td>
<td align="right">20.5%</td>
<td align="right">16.2%</td>
<td align="right">20.4%</td>
<td align="right">946</td>
</tr>
<tr>
<td align="left">126</td>
<td align="left">🟡 Mite</td>
<td align="right"><b>1490</b></td>
<td align="right">19.2%</td>
<td align="right">29.3%</td>
<td align="right">27.3%</td>
<td align="right">16.4%</td>
<td align="right">11.8%</td>
<td align="right">950</td>
</tr>
<tr>
<td align="left">127</td>
<td align="left">🟡 Butler</td>
<td align="right"><b>1490</b></td>
<td align="right">19.7%</td>
<td align="right">35.8%</td>
<td align="right">22.2%</td>
<td align="right">14.2%</td>
<td align="right">14.6%</td>
<td align="right">1005</td>
</tr>
<tr>
<td align="left">128</td>
<td align="left">🟡 Sniveler</td>
<td align="right"><b>1489</b></td>
<td align="right">20.4%</td>
<td align="right">26.3%</td>
<td align="right">25.4%</td>
<td align="right">18.0%</td>
<td align="right">15.7%</td>
<td align="right">1036</td>
</tr>
<tr>
<td align="left">129</td>
<td align="left">🟡 Pickpocket</td>
<td align="right"><b>1488</b></td>
<td align="right">18.6%</td>
<td align="right">24.9%</td>
<td align="right">23.4%</td>
<td align="right">14.7%</td>
<td align="right">15.5%</td>
<td align="right">1055</td>
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

**Total Games Simulated:** 5,000
**Solo Victories:** 4,917
**Shared Victories:** 83
**Average Game Length:** 4.9 turns
**Last Updated:** 2025-12-30T17:59:07

### Alien Power Rankings (by ELO)

| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |
|------|-------|-----|----------|-------|-----------|--------|
| 1 | Machine | 327 | 58.1% | 155 | 87 | 3 |
| 2 | Aristocrat | 137 | 31.6% | 177 | 55 | 1 |
| 3 | Parasite | 82 | 41.8% | 182 | 75 | 1 |
| 4 | Mutant | 63 | 30.3% | 165 | 50 | 0 |
| 5 | Tripler | 62 | 31.2% | 160 | 50 | 0 |
| 6 | Vacuum | 55 | 23.1% | 143 | 33 | 0 |
| 7 | Ethic | 40 | 23.9% | 176 | 40 | 2 |
| 8 | Observer | 38 | 25.6% | 168 | 43 | 0 |
| 9 | Grudge | 25 | 24.5% | 184 | 45 | 0 |
| 10 | Seeker | 22 | 24.4% | 176 | 43 | 0 |
| 11 | Connoisseur | 10 | 25.9% | 185 | 46 | 2 |
| 12 | Doppelganger | 10 | 23.5% | 170 | 40 | 0 |
| 13 | Patriot | 8 | 29.7% | 185 | 48 | 7 |
| 14 | Invader | 3 | 23.4% | 175 | 41 | 0 |
| 15 | Grief | 2 | 25.4% | 181 | 46 | 0 |
| 16 | Altruist | -0 | 23.5% | 183 | 42 | 1 |
| 17 | Rage | -2 | 23.2% | 168 | 38 | 1 |
| 18 | Chronos | -3 | 22.4% | 161 | 32 | 4 |
| 19 | Gambler | -6 | 24.8% | 157 | 38 | 1 |
| 20 | Disease | -6 | 31.7% | 180 | 57 | 0 |
| 21 | Siren | -7 | 24.4% | 176 | 41 | 2 |
| 22 | Electron | -7 | 23.0% | 161 | 37 | 0 |
| 23 | Zombie | -10 | 20.9% | 172 | 35 | 1 |
| 24 | Spiff | -11 | 19.9% | 201 | 40 | 0 |
| 25 | Prophet | -12 | 22.3% | 175 | 39 | 0 |
| 26 | Mite | -18 | 19.0% | 147 | 27 | 1 |
| 27 | Macron | -19 | 29.5% | 166 | 49 | 0 |
| 28 | Glutton | -20 | 23.6% | 182 | 42 | 1 |
| 29 | Delegator | -22 | 20.6% | 175 | 32 | 4 |
| 30 | Miser | -23 | 23.6% | 178 | 41 | 1 |
| 31 | Silencer | -24 | 23.8% | 160 | 36 | 2 |
| 32 | Scout | -24 | 20.8% | 149 | 29 | 2 |
| 33 | Sage | -25 | 20.1% | 189 | 37 | 1 |
| 34 | Dragon | -26 | 19.0% | 174 | 32 | 1 |
| 35 | Cavalry | -27 | 22.5% | 160 | 36 | 0 |
| 36 | Vox | -28 | 20.5% | 176 | 34 | 2 |
| 37 | Chrysalis | -28 | 23.8% | 164 | 39 | 0 |
| 38 | Thief | -33 | 22.6% | 190 | 42 | 1 |
| 39 | Jester | -33 | 26.0% | 169 | 42 | 2 |
| 40 | Warpish | -33 | 26.3% | 186 | 48 | 1 |
| ... | *89 more aliens* | ... | ... | ... | ... | ... |

<!-- SIMULATION_RESULTS_END -->

## Legacy Version

The original 2016 simulator is preserved in `Simulator.py` and `main.py` for reference.
