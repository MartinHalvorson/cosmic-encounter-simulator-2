# Cosmic Encounter Simulator 2

A comprehensive simulation of the board game Cosmic Encounter, designed to analyze alien power balance and game dynamics across various configurations.

## Features

- **90 Alien Powers** implemented with proper game mechanics
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
├── aliens/           # 90 alien power implementations
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

> **14,000** games simulated | Last updated: 2025-12-30 17:53
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
<td align="left">🟢 Machine</td>
<td align="right"><b>1543</b></td>
<td align="right">57.8%</td>
<td align="right">69.8%</td>
<td align="right">63.6%</td>
<td align="right">59.2%</td>
<td align="right">46.9%</td>
<td align="right">683</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🟢 Parasite</td>
<td align="right"><b>1542</b></td>
<td align="right">47.9%</td>
<td align="right">48.4%</td>
<td align="right">52.3%</td>
<td align="right">44.0%</td>
<td align="right">47.6%</td>
<td align="right">739</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Disease</td>
<td align="right"><b>1519</b></td>
<td align="right">29.9%</td>
<td align="right">45.8%</td>
<td align="right">28.6%</td>
<td align="right">26.6%</td>
<td align="right">23.7%</td>
<td align="right">755</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Warpish</td>
<td align="right"><b>1517</b></td>
<td align="right">32.0%</td>
<td align="right">45.5%</td>
<td align="right">43.1%</td>
<td align="right">26.1%</td>
<td align="right">25.5%</td>
<td align="right">671</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Symbiote</td>
<td align="right"><b>1516</b></td>
<td align="right">30.0%</td>
<td align="right">55.9%</td>
<td align="right">34.0%</td>
<td align="right">24.8%</td>
<td align="right">18.9%</td>
<td align="right">676</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Mutant</td>
<td align="right"><b>1516</b></td>
<td align="right">28.1%</td>
<td align="right">51.4%</td>
<td align="right">35.0%</td>
<td align="right">27.4%</td>
<td align="right">14.2%</td>
<td align="right">740</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Tripler</td>
<td align="right"><b>1513</b></td>
<td align="right">28.0%</td>
<td align="right">51.7%</td>
<td align="right">24.4%</td>
<td align="right">24.5%</td>
<td align="right">21.7%</td>
<td align="right">740</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Pacifist</td>
<td align="right"><b>1509</b></td>
<td align="right">28.1%</td>
<td align="right">52.8%</td>
<td align="right">32.9%</td>
<td align="right">20.9%</td>
<td align="right">19.7%</td>
<td align="right">747</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Human</td>
<td align="right"><b>1509</b></td>
<td align="right">25.4%</td>
<td align="right">40.8%</td>
<td align="right">35.7%</td>
<td align="right">17.5%</td>
<td align="right">16.1%</td>
<td align="right">741</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Chronos</td>
<td align="right"><b>1508</b></td>
<td align="right">24.4%</td>
<td align="right">28.7%</td>
<td align="right">28.0%</td>
<td align="right">23.3%</td>
<td align="right">20.6%</td>
<td align="right">753</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Macron</td>
<td align="right"><b>1507</b></td>
<td align="right">26.4%</td>
<td align="right">44.0%</td>
<td align="right">24.6%</td>
<td align="right">24.1%</td>
<td align="right">18.9%</td>
<td align="right">698</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Shadow</td>
<td align="right"><b>1507</b></td>
<td align="right">26.0%</td>
<td align="right">42.0%</td>
<td align="right">32.5%</td>
<td align="right">22.5%</td>
<td align="right">15.9%</td>
<td align="right">750</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Virus</td>
<td align="right"><b>1505</b></td>
<td align="right">25.8%</td>
<td align="right">43.9%</td>
<td align="right">30.2%</td>
<td align="right">21.1%</td>
<td align="right">15.1%</td>
<td align="right">748</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Trader</td>
<td align="right"><b>1505</b></td>
<td align="right">26.6%</td>
<td align="right">44.0%</td>
<td align="right">31.5%</td>
<td align="right">22.8%</td>
<td align="right">17.2%</td>
<td align="right">726</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Grudge</td>
<td align="right"><b>1504</b></td>
<td align="right">22.7%</td>
<td align="right">33.6%</td>
<td align="right">23.9%</td>
<td align="right">19.7%</td>
<td align="right">19.5%</td>
<td align="right">779</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Gambler</td>
<td align="right"><b>1503</b></td>
<td align="right">21.3%</td>
<td align="right">25.0%</td>
<td align="right">20.9%</td>
<td align="right">21.2%</td>
<td align="right">19.8%</td>
<td align="right">747</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Void</td>
<td align="right"><b>1503</b></td>
<td align="right">24.0%</td>
<td align="right">38.1%</td>
<td align="right">25.6%</td>
<td align="right">18.3%</td>
<td align="right">20.2%</td>
<td align="right">718</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Tyrant</td>
<td align="right"><b>1502</b></td>
<td align="right">24.0%</td>
<td align="right">37.4%</td>
<td align="right">24.6%</td>
<td align="right">19.9%</td>
<td align="right">20.1%</td>
<td align="right">550</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Amoeba</td>
<td align="right"><b>1502</b></td>
<td align="right">23.4%</td>
<td align="right">35.7%</td>
<td align="right">25.7%</td>
<td align="right">21.7%</td>
<td align="right">16.9%</td>
<td align="right">714</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Changeling</td>
<td align="right"><b>1502</b></td>
<td align="right">21.9%</td>
<td align="right">23.6%</td>
<td align="right">25.6%</td>
<td align="right">22.0%</td>
<td align="right">18.9%</td>
<td align="right">735</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Filch</td>
<td align="right"><b>1502</b></td>
<td align="right">22.3%</td>
<td align="right">34.6%</td>
<td align="right">26.2%</td>
<td align="right">18.8%</td>
<td align="right">16.0%</td>
<td align="right">730</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Warlock</td>
<td align="right"><b>1502</b></td>
<td align="right">22.8%</td>
<td align="right">30.9%</td>
<td align="right">29.2%</td>
<td align="right">20.0%</td>
<td align="right">16.4%</td>
<td align="right">571</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Fury</td>
<td align="right"><b>1501</b></td>
<td align="right">23.6%</td>
<td align="right">25.0%</td>
<td align="right">29.4%</td>
<td align="right">19.1%</td>
<td align="right">22.5%</td>
<td align="right">628</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Oracle</td>
<td align="right"><b>1501</b></td>
<td align="right">23.3%</td>
<td align="right">35.8%</td>
<td align="right">23.8%</td>
<td align="right">23.6%</td>
<td align="right">16.6%</td>
<td align="right">724</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Nightmare</td>
<td align="right"><b>1501</b></td>
<td align="right">21.6%</td>
<td align="right">30.7%</td>
<td align="right">16.5%</td>
<td align="right">22.7%</td>
<td align="right">18.7%</td>
<td align="right">610</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Dictator</td>
<td align="right"><b>1501</b></td>
<td align="right">21.4%</td>
<td align="right">29.0%</td>
<td align="right">26.0%</td>
<td align="right">19.5%</td>
<td align="right">16.4%</td>
<td align="right">674</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Spiff</td>
<td align="right"><b>1501</b></td>
<td align="right">22.7%</td>
<td align="right">32.2%</td>
<td align="right">28.9%</td>
<td align="right">19.7%</td>
<td align="right">16.5%</td>
<td align="right">727</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Leviathan</td>
<td align="right"><b>1501</b></td>
<td align="right">20.5%</td>
<td align="right">38.9%</td>
<td align="right">18.6%</td>
<td align="right">16.5%</td>
<td align="right">17.8%</td>
<td align="right">765</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟡 Barbarian</td>
<td align="right"><b>1500</b></td>
<td align="right">23.0%</td>
<td align="right">31.8%</td>
<td align="right">31.9%</td>
<td align="right">19.6%</td>
<td align="right">16.4%</td>
<td align="right">600</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟡 Reincarnator</td>
<td align="right"><b>1499</b></td>
<td align="right">21.1%</td>
<td align="right">34.6%</td>
<td align="right">21.2%</td>
<td align="right">16.2%</td>
<td align="right">19.1%</td>
<td align="right">703</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟡 Crystal</td>
<td align="right"><b>1499</b></td>
<td align="right">20.0%</td>
<td align="right">31.6%</td>
<td align="right">19.6%</td>
<td align="right">15.9%</td>
<td align="right">16.7%</td>
<td align="right">611</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟡 Vox</td>
<td align="right"><b>1499</b></td>
<td align="right">20.4%</td>
<td align="right">33.7%</td>
<td align="right">23.0%</td>
<td align="right">19.1%</td>
<td align="right">13.2%</td>
<td align="right">631</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟡 Warrior</td>
<td align="right"><b>1499</b></td>
<td align="right">22.9%</td>
<td align="right">36.9%</td>
<td align="right">23.1%</td>
<td align="right">17.7%</td>
<td align="right">19.6%</td>
<td align="right">724</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟡 Ghoul</td>
<td align="right"><b>1499</b></td>
<td align="right">25.0%</td>
<td align="right">36.1%</td>
<td align="right">32.7%</td>
<td align="right">22.4%</td>
<td align="right">15.7%</td>
<td align="right">696</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟡 Dragon</td>
<td align="right"><b>1499</b></td>
<td align="right">22.8%</td>
<td align="right">35.7%</td>
<td align="right">18.9%</td>
<td align="right">21.8%</td>
<td align="right">18.7%</td>
<td align="right">578</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟡 Mimic</td>
<td align="right"><b>1499</b></td>
<td align="right">21.8%</td>
<td align="right">36.6%</td>
<td align="right">25.2%</td>
<td align="right">24.5%</td>
<td align="right">12.2%</td>
<td align="right">577</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟡 Poison</td>
<td align="right"><b>1499</b></td>
<td align="right">21.0%</td>
<td align="right">31.2%</td>
<td align="right">23.3%</td>
<td align="right">19.4%</td>
<td align="right">16.7%</td>
<td align="right">634</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟡 Pirate</td>
<td align="right"><b>1499</b></td>
<td align="right">22.7%</td>
<td align="right">35.2%</td>
<td align="right">18.4%</td>
<td align="right">22.4%</td>
<td align="right">19.4%</td>
<td align="right">622</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟡 Vacuum</td>
<td align="right"><b>1498</b></td>
<td align="right">21.0%</td>
<td align="right">30.5%</td>
<td align="right">24.7%</td>
<td align="right">16.9%</td>
<td align="right">16.1%</td>
<td align="right">718</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟡 Surge</td>
<td align="right"><b>1498</b></td>
<td align="right">22.5%</td>
<td align="right">40.3%</td>
<td align="right">24.2%</td>
<td align="right">20.2%</td>
<td align="right">14.5%</td>
<td align="right">730</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟡 Patriot</td>
<td align="right"><b>1498</b></td>
<td align="right">21.2%</td>
<td align="right">42.6%</td>
<td align="right">19.0%</td>
<td align="right">17.3%</td>
<td align="right">14.6%</td>
<td align="right">603</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟡 Laser</td>
<td align="right"><b>1498</b></td>
<td align="right">21.2%</td>
<td align="right">25.7%</td>
<td align="right">23.4%</td>
<td align="right">19.5%</td>
<td align="right">18.5%</td>
<td align="right">581</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟡 Crone</td>
<td align="right"><b>1498</b></td>
<td align="right">21.6%</td>
<td align="right">24.1%</td>
<td align="right">22.6%</td>
<td align="right">17.9%</td>
<td align="right">22.4%</td>
<td align="right">741</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟡 Cudgel</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">35.7%</td>
<td align="right">24.4%</td>
<td align="right">20.8%</td>
<td align="right">15.7%</td>
<td align="right">720</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟡 Sage</td>
<td align="right"><b>1497</b></td>
<td align="right">19.8%</td>
<td align="right">30.2%</td>
<td align="right">27.7%</td>
<td align="right">16.2%</td>
<td align="right">12.7%</td>
<td align="right">640</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟡 Seeker</td>
<td align="right"><b>1497</b></td>
<td align="right">21.5%</td>
<td align="right">26.2%</td>
<td align="right">29.9%</td>
<td align="right">17.1%</td>
<td align="right">17.1%</td>
<td align="right">745</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟡 Hate</td>
<td align="right"><b>1497</b></td>
<td align="right">19.3%</td>
<td align="right">29.5%</td>
<td align="right">23.0%</td>
<td align="right">19.4%</td>
<td align="right">12.4%</td>
<td align="right">615</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟡 Observer</td>
<td align="right"><b>1497</b></td>
<td align="right">21.5%</td>
<td align="right">38.6%</td>
<td align="right">26.9%</td>
<td align="right">15.5%</td>
<td align="right">14.7%</td>
<td align="right">740</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟡 Altruist</td>
<td align="right"><b>1497</b></td>
<td align="right">20.5%</td>
<td align="right">31.1%</td>
<td align="right">22.8%</td>
<td align="right">19.1%</td>
<td align="right">14.1%</td>
<td align="right">716</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟡 Remora</td>
<td align="right"><b>1497</b></td>
<td align="right">20.1%</td>
<td align="right">32.6%</td>
<td align="right">20.1%</td>
<td align="right">21.5%</td>
<td align="right">11.7%</td>
<td align="right">718</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟡 Visionary</td>
<td align="right"><b>1497</b></td>
<td align="right">21.5%</td>
<td align="right">38.5%</td>
<td align="right">21.7%</td>
<td align="right">19.0%</td>
<td align="right">14.6%</td>
<td align="right">750</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟡 Philanthropist</td>
<td align="right"><b>1497</b></td>
<td align="right">20.8%</td>
<td align="right">30.1%</td>
<td align="right">24.2%</td>
<td align="right">23.0%</td>
<td align="right">12.7%</td>
<td align="right">682</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟡 Thief</td>
<td align="right"><b>1497</b></td>
<td align="right">18.9%</td>
<td align="right">32.4%</td>
<td align="right">15.7%</td>
<td align="right">14.5%</td>
<td align="right">17.7%</td>
<td align="right">599</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟡 Sheriff</td>
<td align="right"><b>1497</b></td>
<td align="right">19.7%</td>
<td align="right">30.7%</td>
<td align="right">21.5%</td>
<td align="right">16.5%</td>
<td align="right">16.7%</td>
<td align="right">804</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟡 Fido</td>
<td align="right"><b>1497</b></td>
<td align="right">21.6%</td>
<td align="right">37.3%</td>
<td align="right">23.6%</td>
<td align="right">17.0%</td>
<td align="right">16.2%</td>
<td align="right">774</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟡 Kamikazee</td>
<td align="right"><b>1496</b></td>
<td align="right">22.6%</td>
<td align="right">29.4%</td>
<td align="right">30.2%</td>
<td align="right">19.9%</td>
<td align="right">17.0%</td>
<td align="right">717</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟡 Brute</td>
<td align="right"><b>1496</b></td>
<td align="right">20.1%</td>
<td align="right">32.7%</td>
<td align="right">25.7%</td>
<td align="right">12.1%</td>
<td align="right">14.5%</td>
<td align="right">582</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟡 Loser</td>
<td align="right"><b>1496</b></td>
<td align="right">18.4%</td>
<td align="right">31.2%</td>
<td align="right">19.6%</td>
<td align="right">22.6%</td>
<td align="right">7.7%</td>
<td align="right">750</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟡 Clone</td>
<td align="right"><b>1496</b></td>
<td align="right">21.6%</td>
<td align="right">30.6%</td>
<td align="right">20.6%</td>
<td align="right">22.1%</td>
<td align="right">17.9%</td>
<td align="right">735</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟡 Boomerang</td>
<td align="right"><b>1496</b></td>
<td align="right">19.7%</td>
<td align="right">43.9%</td>
<td align="right">18.3%</td>
<td align="right">16.6%</td>
<td align="right">10.9%</td>
<td align="right">619</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟡 Rage</td>
<td align="right"><b>1496</b></td>
<td align="right">19.5%</td>
<td align="right">27.8%</td>
<td align="right">23.6%</td>
<td align="right">19.0%</td>
<td align="right">13.5%</td>
<td align="right">645</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟡 Giver</td>
<td align="right"><b>1496</b></td>
<td align="right">23.3%</td>
<td align="right">30.2%</td>
<td align="right">26.5%</td>
<td align="right">24.8%</td>
<td align="right">16.3%</td>
<td align="right">782</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟡 Genius</td>
<td align="right"><b>1496</b></td>
<td align="right">21.3%</td>
<td align="right">43.6%</td>
<td align="right">22.2%</td>
<td align="right">14.9%</td>
<td align="right">16.1%</td>
<td align="right">717</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟡 Scout</td>
<td align="right"><b>1495</b></td>
<td align="right">20.3%</td>
<td align="right">24.5%</td>
<td align="right">24.0%</td>
<td align="right">21.5%</td>
<td align="right">15.1%</td>
<td align="right">585</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟡 Underdog</td>
<td align="right"><b>1495</b></td>
<td align="right">18.6%</td>
<td align="right">30.8%</td>
<td align="right">22.8%</td>
<td align="right">16.7%</td>
<td align="right">12.0%</td>
<td align="right">622</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟡 Deuce</td>
<td align="right"><b>1495</b></td>
<td align="right">19.6%</td>
<td align="right">31.4%</td>
<td align="right">23.1%</td>
<td align="right">18.1%</td>
<td align="right">12.7%</td>
<td align="right">629</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟡 Chosen</td>
<td align="right"><b>1495</b></td>
<td align="right">20.3%</td>
<td align="right">37.8%</td>
<td align="right">21.7%</td>
<td align="right">18.0%</td>
<td align="right">11.7%</td>
<td align="right">738</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟡 Zombie</td>
<td align="right"><b>1495</b></td>
<td align="right">21.3%</td>
<td align="right">29.9%</td>
<td align="right">23.1%</td>
<td align="right">22.4%</td>
<td align="right">14.0%</td>
<td align="right">734</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟡 Ethic</td>
<td align="right"><b>1494</b></td>
<td align="right">21.4%</td>
<td align="right">29.8%</td>
<td align="right">25.7%</td>
<td align="right">23.0%</td>
<td align="right">13.2%</td>
<td align="right">796</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟡 Mirror</td>
<td align="right"><b>1494</b></td>
<td align="right">20.7%</td>
<td align="right">30.8%</td>
<td align="right">24.4%</td>
<td align="right">19.3%</td>
<td align="right">14.4%</td>
<td align="right">681</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟡 Claw</td>
<td align="right"><b>1494</b></td>
<td align="right">19.9%</td>
<td align="right">30.8%</td>
<td align="right">25.4%</td>
<td align="right">15.8%</td>
<td align="right">14.2%</td>
<td align="right">749</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟡 Hacker</td>
<td align="right"><b>1494</b></td>
<td align="right">21.4%</td>
<td align="right">31.5%</td>
<td align="right">25.0%</td>
<td align="right">21.6%</td>
<td align="right">13.6%</td>
<td align="right">719</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟡 Assassin</td>
<td align="right"><b>1494</b></td>
<td align="right">20.7%</td>
<td align="right">29.1%</td>
<td align="right">26.5%</td>
<td align="right">17.3%</td>
<td align="right">14.8%</td>
<td align="right">690</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟡 Empath</td>
<td align="right"><b>1493</b></td>
<td align="right">19.9%</td>
<td align="right">36.8%</td>
<td align="right">27.8%</td>
<td align="right">12.4%</td>
<td align="right">14.0%</td>
<td align="right">694</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟡 Antimatter</td>
<td align="right"><b>1493</b></td>
<td align="right">18.5%</td>
<td align="right">33.8%</td>
<td align="right">24.9%</td>
<td align="right">17.6%</td>
<td align="right">7.4%</td>
<td align="right">804</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟡 Pentaform</td>
<td align="right"><b>1493</b></td>
<td align="right">18.5%</td>
<td align="right">21.8%</td>
<td align="right">20.6%</td>
<td align="right">17.2%</td>
<td align="right">16.7%</td>
<td align="right">745</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟡 Healer</td>
<td align="right"><b>1493</b></td>
<td align="right">21.2%</td>
<td align="right">29.7%</td>
<td align="right">22.6%</td>
<td align="right">18.6%</td>
<td align="right">18.8%</td>
<td align="right">694</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟡 Calculator</td>
<td align="right"><b>1493</b></td>
<td align="right">20.2%</td>
<td align="right">23.1%</td>
<td align="right">23.7%</td>
<td align="right">21.2%</td>
<td align="right">14.6%</td>
<td align="right">742</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟡 Yin</td>
<td align="right"><b>1493</b></td>
<td align="right">20.6%</td>
<td align="right">32.4%</td>
<td align="right">24.1%</td>
<td align="right">18.6%</td>
<td align="right">14.9%</td>
<td align="right">732</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟡 Citadel</td>
<td align="right"><b>1492</b></td>
<td align="right">18.9%</td>
<td align="right">31.1%</td>
<td align="right">17.9%</td>
<td align="right">21.2%</td>
<td align="right">12.1%</td>
<td align="right">757</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟡 Reserve</td>
<td align="right"><b>1492</b></td>
<td align="right">19.1%</td>
<td align="right">29.7%</td>
<td align="right">18.8%</td>
<td align="right">16.0%</td>
<td align="right">16.2%</td>
<td align="right">697</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟡 Sorcerer</td>
<td align="right"><b>1492</b></td>
<td align="right">20.1%</td>
<td align="right">27.9%</td>
<td align="right">22.4%</td>
<td align="right">18.8%</td>
<td align="right">15.9%</td>
<td align="right">758</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟡 Mite</td>
<td align="right"><b>1492</b></td>
<td align="right">18.6%</td>
<td align="right">30.7%</td>
<td align="right">24.2%</td>
<td align="right">17.6%</td>
<td align="right">10.8%</td>
<td align="right">689</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟡 Negator</td>
<td align="right"><b>1492</b></td>
<td align="right">20.4%</td>
<td align="right">33.6%</td>
<td align="right">25.2%</td>
<td align="right">15.5%</td>
<td align="right">14.5%</td>
<td align="right">727</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟡 Masochist</td>
<td align="right"><b>1491</b></td>
<td align="right">19.3%</td>
<td align="right">23.7%</td>
<td align="right">20.1%</td>
<td align="right">17.8%</td>
<td align="right">17.5%</td>
<td align="right">690</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟡 Butler</td>
<td align="right"><b>1491</b></td>
<td align="right">19.8%</td>
<td align="right">34.2%</td>
<td align="right">26.3%</td>
<td align="right">13.3%</td>
<td align="right">13.0%</td>
<td align="right">718</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟡 Tick-Tock</td>
<td align="right"><b>1491</b></td>
<td align="right">20.7%</td>
<td align="right">31.7%</td>
<td align="right">22.4%</td>
<td align="right">16.3%</td>
<td align="right">17.8%</td>
<td align="right">765</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟡 Silencer</td>
<td align="right"><b>1491</b></td>
<td align="right">21.0%</td>
<td align="right">31.2%</td>
<td align="right">26.7%</td>
<td align="right">19.0%</td>
<td align="right">13.1%</td>
<td align="right">720</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟡 Sniveler</td>
<td align="right"><b>1490</b></td>
<td align="right">19.5%</td>
<td align="right">24.6%</td>
<td align="right">23.8%</td>
<td align="right">16.8%</td>
<td align="right">15.9%</td>
<td align="right">739</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟡 Pickpocket</td>
<td align="right"><b>1490</b></td>
<td align="right">17.9%</td>
<td align="right">22.0%</td>
<td align="right">23.2%</td>
<td align="right">15.5%</td>
<td align="right">14.6%</td>
<td align="right">748</td>
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

## Legacy Version

The original 2016 simulator is preserved in `Simulator.py` and `main.py` for reference.
