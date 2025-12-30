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

## Alien Power Rankings

> **2,000** games simulated | Last updated: 2025-12-30 17:48
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
<td align="left">🟢 Parasite</td>
<td align="right"><b>1516</b></td>
<td align="right">47.0%</td>
<td align="right">39.1%</td>
<td align="right">51.4%</td>
<td align="right">56.8%</td>
<td align="right">38.3%</td>
<td align="right">149</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🟢 Machine</td>
<td align="right"><b>1516</b></td>
<td align="right">55.8%</td>
<td align="right">69.2%</td>
<td align="right">55.6%</td>
<td align="right">58.3%</td>
<td align="right">50.0%</td>
<td align="right">129</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Disease</td>
<td align="right"><b>1510</b></td>
<td align="right">37.1%</td>
<td align="right">54.8%</td>
<td align="right">32.1%</td>
<td align="right">25.0%</td>
<td align="right">38.6%</td>
<td align="right">143</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Mutant</td>
<td align="right"><b>1508</b></td>
<td align="right">34.2%</td>
<td align="right">62.5%</td>
<td align="right">33.3%</td>
<td align="right">29.7%</td>
<td align="right">20.0%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Warpish</td>
<td align="right"><b>1506</b></td>
<td align="right">31.4%</td>
<td align="right">38.1%</td>
<td align="right">29.2%</td>
<td align="right">33.3%</td>
<td align="right">27.0%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Tripler</td>
<td align="right"><b>1506</b></td>
<td align="right">30.8%</td>
<td align="right">63.6%</td>
<td align="right">19.0%</td>
<td align="right">20.0%</td>
<td align="right">27.7%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Human</td>
<td align="right"><b>1505</b></td>
<td align="right">30.6%</td>
<td align="right">38.1%</td>
<td align="right">42.9%</td>
<td align="right">24.4%</td>
<td align="right">25.0%</td>
<td align="right">134</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Symbiote</td>
<td align="right"><b>1505</b></td>
<td align="right">30.0%</td>
<td align="right">68.2%</td>
<td align="right">28.6%</td>
<td align="right">25.6%</td>
<td align="right">15.9%</td>
<td align="right">140</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Chronos</td>
<td align="right"><b>1504</b></td>
<td align="right">29.0%</td>
<td align="right">25.0%</td>
<td align="right">44.1%</td>
<td align="right">25.8%</td>
<td align="right">22.4%</td>
<td align="right">138</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Grudge</td>
<td align="right"><b>1504</b></td>
<td align="right">28.4%</td>
<td align="right">34.8%</td>
<td align="right">21.2%</td>
<td align="right">35.0%</td>
<td align="right">25.0%</td>
<td align="right">148</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Gambler</td>
<td align="right"><b>1503</b></td>
<td align="right">27.5%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">38.7%</td>
<td align="right">18.8%</td>
<td align="right">138</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Leviathan</td>
<td align="right"><b>1503</b></td>
<td align="right">27.4%</td>
<td align="right">48.1%</td>
<td align="right">32.4%</td>
<td align="right">18.4%</td>
<td align="right">21.3%</td>
<td align="right">157</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Trader</td>
<td align="right"><b>1502</b></td>
<td align="right">25.7%</td>
<td align="right">26.3%</td>
<td align="right">37.1%</td>
<td align="right">22.5%</td>
<td align="right">19.6%</td>
<td align="right">140</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Dictator</td>
<td align="right"><b>1502</b></td>
<td align="right">25.0%</td>
<td align="right">50.0%</td>
<td align="right">16.7%</td>
<td align="right">25.7%</td>
<td align="right">17.1%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Shadow</td>
<td align="right"><b>1501</b></td>
<td align="right">24.8%</td>
<td align="right">50.0%</td>
<td align="right">25.8%</td>
<td align="right">20.7%</td>
<td align="right">14.6%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Pacifist</td>
<td align="right"><b>1501</b></td>
<td align="right">24.8%</td>
<td align="right">54.5%</td>
<td align="right">23.3%</td>
<td align="right">17.2%</td>
<td align="right">13.9%</td>
<td align="right">117</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Macron</td>
<td align="right"><b>1501</b></td>
<td align="right">24.7%</td>
<td align="right">40.0%</td>
<td align="right">24.0%</td>
<td align="right">26.8%</td>
<td align="right">16.4%</td>
<td align="right">146</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Changeling</td>
<td align="right"><b>1501</b></td>
<td align="right">24.4%</td>
<td align="right">33.3%</td>
<td align="right">28.1%</td>
<td align="right">21.2%</td>
<td align="right">21.2%</td>
<td align="right">135</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Filch</td>
<td align="right"><b>1501</b></td>
<td align="right">24.3%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">19.4%</td>
<td align="right">5.9%</td>
<td align="right">115</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Virus</td>
<td align="right"><b>1501</b></td>
<td align="right">24.3%</td>
<td align="right">45.5%</td>
<td align="right">32.3%</td>
<td align="right">12.8%</td>
<td align="right">10.8%</td>
<td align="right">140</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Spiff</td>
<td align="right"><b>1501</b></td>
<td align="right">23.8%</td>
<td align="right">28.0%</td>
<td align="right">32.5%</td>
<td align="right">18.4%</td>
<td align="right">18.8%</td>
<td align="right">151</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Reincarnator</td>
<td align="right"><b>1501</b></td>
<td align="right">23.8%</td>
<td align="right">55.6%</td>
<td align="right">13.8%</td>
<td align="right">11.4%</td>
<td align="right">27.5%</td>
<td align="right">122</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Remora</td>
<td align="right"><b>1501</b></td>
<td align="right">23.5%</td>
<td align="right">33.3%</td>
<td align="right">18.2%</td>
<td align="right">35.1%</td>
<td align="right">11.9%</td>
<td align="right">136</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Void</td>
<td align="right"><b>1500</b></td>
<td align="right">23.4%</td>
<td align="right">45.0%</td>
<td align="right">36.7%</td>
<td align="right">13.5%</td>
<td align="right">14.0%</td>
<td align="right">137</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Loser</td>
<td align="right"><b>1500</b></td>
<td align="right">23.3%</td>
<td align="right">40.9%</td>
<td align="right">20.6%</td>
<td align="right">20.0%</td>
<td align="right">20.4%</td>
<td align="right">150</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Amoeba</td>
<td align="right"><b>1500</b></td>
<td align="right">23.0%</td>
<td align="right">29.4%</td>
<td align="right">28.6%</td>
<td align="right">21.1%</td>
<td align="right">18.6%</td>
<td align="right">126</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Oracle</td>
<td align="right"><b>1500</b></td>
<td align="right">22.9%</td>
<td align="right">30.0%</td>
<td align="right">17.4%</td>
<td align="right">28.6%</td>
<td align="right">16.1%</td>
<td align="right">109</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Crone</td>
<td align="right"><b>1500</b></td>
<td align="right">22.8%</td>
<td align="right">19.0%</td>
<td align="right">29.7%</td>
<td align="right">20.5%</td>
<td align="right">20.5%</td>
<td align="right">136</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟡 Vacuum</td>
<td align="right"><b>1500</b></td>
<td align="right">22.6%</td>
<td align="right">18.2%</td>
<td align="right">43.3%</td>
<td align="right">18.8%</td>
<td align="right">11.9%</td>
<td align="right">115</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟡 Surge</td>
<td align="right"><b>1499</b></td>
<td align="right">21.7%</td>
<td align="right">40.9%</td>
<td align="right">25.0%</td>
<td align="right">11.5%</td>
<td align="right">17.5%</td>
<td align="right">129</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟡 Altruist</td>
<td align="right"><b>1499</b></td>
<td align="right">21.6%</td>
<td align="right">33.3%</td>
<td align="right">30.8%</td>
<td align="right">17.6%</td>
<td align="right">12.2%</td>
<td align="right">125</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟡 Fido</td>
<td align="right"><b>1499</b></td>
<td align="right">21.6%</td>
<td align="right">39.1%</td>
<td align="right">30.0%</td>
<td align="right">10.0%</td>
<td align="right">17.4%</td>
<td align="right">139</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟡 Visionary</td>
<td align="right"><b>1499</b></td>
<td align="right">21.5%</td>
<td align="right">40.9%</td>
<td align="right">24.3%</td>
<td align="right">21.4%</td>
<td align="right">9.3%</td>
<td align="right">144</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟡 Philanthropist</td>
<td align="right"><b>1499</b></td>
<td align="right">21.3%</td>
<td align="right">9.1%</td>
<td align="right">29.4%</td>
<td align="right">26.5%</td>
<td align="right">14.0%</td>
<td align="right">122</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟡 Seeker</td>
<td align="right"><b>1499</b></td>
<td align="right">20.9%</td>
<td align="right">29.4%</td>
<td align="right">27.6%</td>
<td align="right">20.9%</td>
<td align="right">13.3%</td>
<td align="right">134</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟡 Chosen</td>
<td align="right"><b>1499</b></td>
<td align="right">20.7%</td>
<td align="right">48.4%</td>
<td align="right">17.5%</td>
<td align="right">10.7%</td>
<td align="right">10.9%</td>
<td align="right">145</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟡 Observer</td>
<td align="right"><b>1499</b></td>
<td align="right">20.6%</td>
<td align="right">50.0%</td>
<td align="right">36.0%</td>
<td align="right">12.5%</td>
<td align="right">7.4%</td>
<td align="right">131</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟡 Cudgel</td>
<td align="right"><b>1498</b></td>
<td align="right">20.5%</td>
<td align="right">41.2%</td>
<td align="right">22.0%</td>
<td align="right">14.3%</td>
<td align="right">15.4%</td>
<td align="right">132</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟡 Sheriff</td>
<td align="right"><b>1498</b></td>
<td align="right">20.0%</td>
<td align="right">36.0%</td>
<td align="right">15.2%</td>
<td align="right">18.4%</td>
<td align="right">16.9%</td>
<td align="right">155</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟡 Pentaform</td>
<td align="right"><b>1498</b></td>
<td align="right">20.0%</td>
<td align="right">25.0%</td>
<td align="right">19.2%</td>
<td align="right">16.7%</td>
<td align="right">20.9%</td>
<td align="right">125</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟡 Antimatter</td>
<td align="right"><b>1498</b></td>
<td align="right">19.8%</td>
<td align="right">44.0%</td>
<td align="right">11.8%</td>
<td align="right">19.4%</td>
<td align="right">11.1%</td>
<td align="right">131</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟡 Warrior</td>
<td align="right"><b>1498</b></td>
<td align="right">19.7%</td>
<td align="right">29.4%</td>
<td align="right">25.9%</td>
<td align="right">13.8%</td>
<td align="right">10.8%</td>
<td align="right">127</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟡 Empath</td>
<td align="right"><b>1498</b></td>
<td align="right">19.6%</td>
<td align="right">38.9%</td>
<td align="right">16.0%</td>
<td align="right">15.0%</td>
<td align="right">16.3%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟡 Clone</td>
<td align="right"><b>1498</b></td>
<td align="right">19.4%</td>
<td align="right">35.0%</td>
<td align="right">20.7%</td>
<td align="right">12.8%</td>
<td align="right">17.6%</td>
<td align="right">139</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟡 Zombie</td>
<td align="right"><b>1498</b></td>
<td align="right">19.3%</td>
<td align="right">16.7%</td>
<td align="right">25.0%</td>
<td align="right">24.4%</td>
<td align="right">11.1%</td>
<td align="right">135</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟡 Kamikazee</td>
<td align="right"><b>1498</b></td>
<td align="right">19.2%</td>
<td align="right">17.4%</td>
<td align="right">21.7%</td>
<td align="right">28.9%</td>
<td align="right">10.9%</td>
<td align="right">130</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟡 Mirror</td>
<td align="right"><b>1498</b></td>
<td align="right">19.2%</td>
<td align="right">28.6%</td>
<td align="right">23.1%</td>
<td align="right">19.4%</td>
<td align="right">11.9%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟡 Citadel</td>
<td align="right"><b>1497</b></td>
<td align="right">19.0%</td>
<td align="right">25.0%</td>
<td align="right">14.3%</td>
<td align="right">17.9%</td>
<td align="right">18.8%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟡 Ethic</td>
<td align="right"><b>1497</b></td>
<td align="right">18.8%</td>
<td align="right">19.2%</td>
<td align="right">23.1%</td>
<td align="right">20.5%</td>
<td align="right">14.6%</td>
<td align="right">144</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟡 Ghoul</td>
<td align="right"><b>1497</b></td>
<td align="right">18.4%</td>
<td align="right">55.6%</td>
<td align="right">19.4%</td>
<td align="right">11.9%</td>
<td align="right">10.0%</td>
<td align="right">141</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟡 Mite</td>
<td align="right"><b>1497</b></td>
<td align="right">18.0%</td>
<td align="right">36.8%</td>
<td align="right">23.1%</td>
<td align="right">18.9%</td>
<td align="right">7.8%</td>
<td align="right">133</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟡 Genius</td>
<td align="right"><b>1497</b></td>
<td align="right">17.8%</td>
<td align="right">23.1%</td>
<td align="right">21.4%</td>
<td align="right">9.8%</td>
<td align="right">22.2%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟡 Hacker</td>
<td align="right"><b>1497</b></td>
<td align="right">17.6%</td>
<td align="right">22.7%</td>
<td align="right">21.7%</td>
<td align="right">18.2%</td>
<td align="right">9.7%</td>
<td align="right">131</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟡 Masochist</td>
<td align="right"><b>1497</b></td>
<td align="right">17.6%</td>
<td align="right">9.1%</td>
<td align="right">17.2%</td>
<td align="right">17.1%</td>
<td align="right">22.2%</td>
<td align="right">131</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟡 Giver</td>
<td align="right"><b>1496</b></td>
<td align="right">17.5%</td>
<td align="right">18.2%</td>
<td align="right">24.2%</td>
<td align="right">13.8%</td>
<td align="right">15.1%</td>
<td align="right">137</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟡 Reserve</td>
<td align="right"><b>1496</b></td>
<td align="right">17.5%</td>
<td align="right">20.8%</td>
<td align="right">16.0%</td>
<td align="right">18.8%</td>
<td align="right">16.1%</td>
<td align="right">137</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟡 Sorcerer</td>
<td align="right"><b>1496</b></td>
<td align="right">17.5%</td>
<td align="right">21.7%</td>
<td align="right">15.8%</td>
<td align="right">25.5%</td>
<td align="right">3.2%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟡 Healer</td>
<td align="right"><b>1496</b></td>
<td align="right">17.4%</td>
<td align="right">26.3%</td>
<td align="right">16.0%</td>
<td align="right">13.3%</td>
<td align="right">17.1%</td>
<td align="right">109</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟡 Claw</td>
<td align="right"><b>1496</b></td>
<td align="right">17.4%</td>
<td align="right">18.2%</td>
<td align="right">28.0%</td>
<td align="right">21.9%</td>
<td align="right">9.3%</td>
<td align="right">144</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟡 Assassin</td>
<td align="right"><b>1496</b></td>
<td align="right">17.3%</td>
<td align="right">20.8%</td>
<td align="right">21.1%</td>
<td align="right">15.0%</td>
<td align="right">12.9%</td>
<td align="right">133</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟡 Negator</td>
<td align="right"><b>1496</b></td>
<td align="right">17.0%</td>
<td align="right">34.5%</td>
<td align="right">22.2%</td>
<td align="right">6.7%</td>
<td align="right">12.5%</td>
<td align="right">141</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟡 Calculator</td>
<td align="right"><b>1496</b></td>
<td align="right">17.0%</td>
<td align="right">25.0%</td>
<td align="right">22.9%</td>
<td align="right">12.5%</td>
<td align="right">13.2%</td>
<td align="right">141</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟡 Pickpocket</td>
<td align="right"><b>1495</b></td>
<td align="right">15.9%</td>
<td align="right">26.3%</td>
<td align="right">25.0%</td>
<td align="right">4.8%</td>
<td align="right">16.3%</td>
<td align="right">138</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟡 Yin</td>
<td align="right"><b>1495</b></td>
<td align="right">15.6%</td>
<td align="right">31.6%</td>
<td align="right">17.1%</td>
<td align="right">2.9%</td>
<td align="right">17.0%</td>
<td align="right">141</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟡 Butler</td>
<td align="right"><b>1495</b></td>
<td align="right">15.4%</td>
<td align="right">26.1%</td>
<td align="right">24.4%</td>
<td align="right">5.9%</td>
<td align="right">7.9%</td>
<td align="right">136</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟡 Sniveler</td>
<td align="right"><b>1494</b></td>
<td align="right">14.5%</td>
<td align="right">39.1%</td>
<td align="right">16.7%</td>
<td align="right">10.5%</td>
<td align="right">4.3%</td>
<td align="right">131</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟡 Tick-Tock</td>
<td align="right"><b>1494</b></td>
<td align="right">14.3%</td>
<td align="right">20.0%</td>
<td align="right">14.3%</td>
<td align="right">9.7%</td>
<td align="right">15.4%</td>
<td align="right">126</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟡 Silencer</td>
<td align="right"><b>1494</b></td>
<td align="right">14.2%</td>
<td align="right">12.0%</td>
<td align="right">26.3%</td>
<td align="right">20.0%</td>
<td align="right">6.2%</td>
<td align="right">127</td>
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

**Total Games Simulated:** 500
**Solo Victories:** 490
**Shared Victories:** 10
**Average Game Length:** 5.2 turns
**Last Updated:** 2025-12-30T17:48:47

### Alien Power Rankings (by ELO)

| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |
|------|-------|-----|----------|-------|-----------|--------|
| 1 | Machine | 1374 | 50.0% | 24 | 11 | 1 |
| 2 | Macron | 1331 | 34.5% | 29 | 10 | 0 |
| 3 | Sheriff | 1331 | 37.0% | 27 | 10 | 0 |
| 4 | Masochist | 1283 | 28.6% | 21 | 4 | 2 |
| 5 | Parasite | 1276 | 41.2% | 34 | 14 | 0 |
| 6 | Genius | 1275 | 26.1% | 23 | 6 | 0 |
| 7 | Citadel | 1275 | 26.1% | 23 | 6 | 0 |
| 8 | Hacker | 1267 | 33.3% | 27 | 8 | 1 |
| 9 | Pentaform | 1266 | 23.1% | 26 | 6 | 0 |
| 10 | Disease | 1265 | 34.2% | 38 | 13 | 0 |
| 11 | Human | 1264 | 28.1% | 32 | 9 | 0 |
| 12 | Oracle | 1263 | 26.9% | 26 | 6 | 1 |
| 13 | Silencer | 1253 | 28.1% | 32 | 9 | 0 |
| 14 | Tick-Tock | 1252 | 25.0% | 24 | 6 | 0 |
| 15 | Butler | 1251 | 27.6% | 29 | 8 | 0 |
| 16 | Cudgel | 1249 | 25.0% | 32 | 8 | 0 |
| 17 | Warpish | 1240 | 25.8% | 31 | 7 | 1 |
| 18 | Giver | 1239 | 23.3% | 30 | 7 | 0 |
| 19 | Vacuum | 1239 | 30.3% | 33 | 9 | 1 |
| 20 | Pacifist | 1238 | 33.3% | 48 | 16 | 0 |
| 21 | Remora | 1232 | 31.7% | 41 | 12 | 1 |
| 22 | Ethic | 1226 | 13.0% | 23 | 3 | 0 |
| 23 | Shadow | 1220 | 19.2% | 26 | 5 | 0 |
| 24 | Mutant | 1218 | 26.5% | 34 | 9 | 0 |
| 25 | Kamikazee | 1216 | 18.2% | 33 | 5 | 1 |
| 26 | Crone | 1214 | 25.0% | 32 | 8 | 0 |
| 27 | Grudge | 1212 | 23.5% | 34 | 6 | 2 |
| 28 | Chronos | 1211 | 17.6% | 34 | 6 | 0 |
| 29 | Sorcerer | 1209 | 25.8% | 31 | 7 | 1 |
| 30 | Filch | 1207 | 22.9% | 35 | 8 | 0 |
| 31 | Pickpocket | 1206 | 29.7% | 37 | 11 | 0 |
| 32 | Tripler | 1206 | 29.3% | 41 | 12 | 0 |
| 33 | Reincarnator | 1202 | 20.7% | 29 | 6 | 0 |
| 34 | Visionary | 1202 | 20.7% | 29 | 6 | 0 |
| 35 | Trader | 1201 | 30.0% | 40 | 12 | 0 |
| 36 | Ghoul | 1198 | 26.3% | 38 | 10 | 0 |
| 37 | Seeker | 1197 | 22.2% | 36 | 8 | 0 |
| 38 | Observer | 1188 | 25.0% | 36 | 9 | 0 |
| 39 | Leviathan | 1187 | 15.6% | 32 | 5 | 0 |
| 40 | Chosen | 1182 | 26.3% | 38 | 9 | 1 |
| ... | *28 more aliens* | ... | ... | ... | ... | ... |

<!-- SIMULATION_RESULTS_END -->

## Legacy Version

The original 2016 simulator is preserved in `Simulator.py` and `main.py` for reference.
