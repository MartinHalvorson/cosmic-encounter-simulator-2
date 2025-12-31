# Cosmic Encounter Simulator

<!-- NOTE: Only update the stats table below or feature implementation status. Do not modify other sections unless specifically requested. -->

A simulation of the board game Cosmic Encounter for analyzing alien power balance. Features 200+ alien powers, multiple AI strategies, and comprehensive statistics tracking across 3-6 player games.

## Alien Power Rankings

> **54,000** games simulated | Last updated: 2025-12-30
>
> Sort table: `python update_stats.py --sort [elo|overall|3p|4p|5p|6p] --order [asc|desc]`

| Power | ELO | Overall | 3P | 4P | 5P | 6P |
|:------|----:|--------:|---:|---:|---:|---:|
| Machine | 1570 | 56.9% | 69.8% | 65.0% | 57.9% | 44.3% |
| Parasite | 1568 | 45.5% | 44.4% | 45.8% | 47.7% | 44.0% |
| Warpish | 1528 | 31.6% | 52.5% | 40.5% | 24.8% | 22.6% |
| Disease | 1526 | 28.1% | 41.6% | 29.1% | 21.6% | 25.4% |
| Symbiote | 1524 | 30.6% | 49.8% | 35.6% | 27.1% | 20.1% |
| Mutant | 1521 | 27.3% | 46.4% | 31.0% | 24.6% | 17.8% |
| Tripler | 1520 | 28.8% | 46.1% | 30.3% | 25.9% | 21.3% |
| Pacifist | 1516 | 27.9% | 49.7% | 36.2% | 19.3% | 18.8% |
| Macron | 1513 | 28.6% | 47.9% | 29.9% | 26.5% | 19.0% |
| Human | 1512 | 25.9% | 42.7% | 28.3% | 20.5% | 19.9% |
| Shadow | 1510 | 26.1% | 43.3% | 32.0% | 21.2% | 17.1% |
| Trader | 1510 | 26.4% | 44.1% | 29.8% | 23.4% | 17.4% |
| Virus | 1509 | 25.9% | 42.2% | 26.9% | 23.8% | 18.6% |
| Chronos | 1509 | 22.8% | 32.1% | 26.3% | 20.4% | 17.8% |
| Chrysalis | 1508 | 28.0% | 46.9% | 34.6% | 24.1% | 17.7% |
| Aristocrat | 1508 | 26.2% | 36.8% | 25.2% | 26.9% | 20.8% |
| Engineer | 1504 | 24.3% | 34.2% | 23.0% | 25.5% | 19.3% |
| Insect | 1504 | 25.0% | 37.9% | 26.5% | 22.4% | 18.7% |
| Bully | 1504 | 24.8% | 34.0% | 28.7% | 19.0% | 22.5% |
| Ghoul | 1504 | 27.0% | 42.7% | 34.3% | 23.2% | 17.4% |
| Connoisseur | 1503 | 23.3% | 37.5% | 25.0% | 21.7% | 15.8% |
| Bulwark | 1503 | 23.1% | 36.8% | 26.5% | 20.5% | 15.7% |
| Grudge | 1503 | 21.9% | 31.2% | 24.2% | 20.6% | 17.0% |
| Ghast | 1503 | 22.2% | 36.6% | 25.4% | 18.6% | 16.1% |
| Invader | 1502 | 23.2% | 37.7% | 24.5% | 18.6% | 18.7% |
| Tyrant | 1502 | 23.3% | 35.6% | 24.6% | 18.8% | 20.6% |
| Gambler | 1502 | 22.7% | 33.1% | 24.7% | 20.4% | 17.7% |
| Void | 1502 | 21.9% | 34.6% | 22.9% | 18.5% | 17.4% |
| Miser | 1502 | 23.6% | 29.2% | 29.1% | 23.9% | 16.5% |
| Diplomat | 1501 | 23.1% | 32.9% | 28.3% | 21.0% | 16.4% |
| Fury | 1501 | 21.8% | 29.6% | 27.7% | 18.6% | 16.3% |
| Electron | 1501 | 23.7% | 37.1% | 25.5% | 21.1% | 17.9% |
| Amoeba | 1501 | 22.1% | 35.9% | 24.1% | 19.8% | 15.6% |
| Oracle | 1501 | 22.2% | 38.8% | 22.2% | 19.3% | 15.9% |
| Delegator | 1501 | 23.1% | 38.3% | 24.6% | 22.4% | 14.5% |
| Grief | 1501 | 22.7% | 36.8% | 26.9% | 19.4% | 15.2% |
| Fungus | 1501 | 22.0% | 33.0% | 23.4% | 16.8% | 20.1% |
| Battlemaster | 1501 | 22.9% | 39.2% | 23.8% | 20.0% | 16.1% |
| Schizoid | 1501 | 21.8% | 34.0% | 22.3% | 20.7% | 15.8% |
| Filch | 1501 | 21.7% | 32.1% | 25.3% | 19.0% | 16.4% |
| Guardian | 1501 | 22.4% | 30.4% | 27.4% | 19.4% | 16.3% |
| Dictator | 1500 | 21.4% | 32.7% | 24.1% | 18.8% | 16.3% |
| Spiff | 1500 | 21.0% | 32.4% | 27.2% | 18.3% | 13.2% |
| Changeling | 1500 | 21.0% | 24.7% | 27.7% | 19.0% | 16.6% |
| Warlock | 1500 | 21.7% | 31.6% | 27.4% | 19.1% | 15.8% |
| Glutton | 1500 | 22.0% | 29.6% | 24.3% | 21.6% | 16.7% |
| Warrior | 1500 | 22.2% | 37.7% | 25.1% | 18.6% | 15.5% |
| Doppelganger | 1500 | 21.6% | 27.1% | 27.5% | 22.3% | 14.3% |
| Jester | 1499 | 22.6% | 35.0% | 27.1% | 17.6% | 17.3% |
| Extortionist | 1499 | 20.1% | 31.8% | 20.1% | 17.3% | 16.7% |
| Barbarian | 1499 | 22.6% | 30.0% | 25.6% | 22.4% | 17.2% |
| Pirate | 1499 | 21.8% | 32.2% | 21.7% | 20.7% | 17.4% |
| Nightmare | 1498 | 20.2% | 29.9% | 18.8% | 19.2% | 16.8% |
| Leviathan | 1498 | 20.4% | 34.4% | 23.6% | 16.7% | 14.6% |
| Dragon | 1498 | 21.7% | 32.8% | 20.4% | 20.2% | 17.4% |
| Mimic | 1498 | 22.1% | 34.2% | 24.3% | 20.6% | 15.8% |
| Roach | 1498 | 20.5% | 29.5% | 25.4% | 18.1% | 15.0% |
| Cavalry | 1498 | 22.0% | 30.2% | 26.9% | 21.7% | 15.1% |
| Prophet | 1498 | 22.0% | 37.0% | 22.3% | 23.1% | 14.6% |
| Poison | 1498 | 21.5% | 29.2% | 25.2% | 19.7% | 16.9% |
| Vox | 1498 | 21.3% | 33.0% | 24.7% | 17.5% | 16.6% |
| Cudgel | 1497 | 21.8% | 38.3% | 25.5% | 17.6% | 14.3% |
| Vacuum | 1497 | 22.7% | 37.5% | 24.8% | 18.8% | 16.9% |
| Reincarnator | 1497 | 20.8% | 32.3% | 23.4% | 18.0% | 15.8% |
| Foam | 1497 | 21.3% | 28.1% | 24.9% | 20.8% | 15.9% |
| Patriot | 1497 | 22.8% | 39.6% | 24.8% | 19.8% | 15.8% |
| Harbinger | 1497 | 19.8% | 26.4% | 22.5% | 16.4% | 17.7% |
| Architect | 1497 | 21.2% | 36.0% | 21.8% | 20.9% | 14.4% |
| Witch | 1497 | 21.0% | 34.5% | 19.9% | 17.5% | 17.3% |
| Fido | 1497 | 22.3% | 36.4% | 24.8% | 19.2% | 16.8% |
| Kamikazee | 1496 | 23.5% | 34.9% | 28.9% | 20.0% | 17.1% |
| Fodder | 1496 | 19.7% | 31.7% | 21.1% | 18.3% | 13.9% |
| Crystal | 1496 | 20.9% | 26.5% | 23.7% | 18.8% | 18.0% |
| Surge | 1496 | 20.5% | 33.1% | 23.4% | 18.6% | 14.3% |
| Magician | 1496 | 19.2% | 27.4% | 21.4% | 20.0% | 13.7% |
| Vulture | 1496 | 21.3% | 32.8% | 26.5% | 19.1% | 13.9% |
| Observer | 1496 | 21.6% | 34.5% | 24.9% | 17.0% | 17.4% |
| Giver | 1496 | 21.9% | 30.4% | 24.4% | 20.5% | 17.2% |
| Remora | 1496 | 21.8% | 29.9% | 24.6% | 23.0% | 14.5% |
| Crone | 1495 | 21.5% | 27.9% | 22.8% | 21.7% | 16.9% |
| Philanthropist | 1495 | 21.5% | 32.0% | 27.0% | 18.6% | 15.2% |
| Laser | 1495 | 20.7% | 30.3% | 22.1% | 18.5% | 16.9% |
| Visionary | 1495 | 20.2% | 31.5% | 20.8% | 20.0% | 14.5% |
| Seeker | 1495 | 20.4% | 29.7% | 23.8% | 17.6% | 15.9% |
| Feline | 1495 | 21.7% | 33.3% | 22.3% | 19.0% | 18.0% |
| Converter | 1495 | 19.8% | 30.6% | 26.0% | 14.0% | 14.7% |
| Sage | 1495 | 21.0% | 31.6% | 24.9% | 17.9% | 15.8% |
| Hate | 1495 | 22.2% | 33.7% | 24.8% | 22.2% | 14.9% |
| Boomerang | 1495 | 22.4% | 38.8% | 24.6% | 17.7% | 16.5% |
| Phantom | 1495 | 19.1% | 30.3% | 18.9% | 18.1% | 14.5% |
| Altruist | 1494 | 20.3% | 33.4% | 24.0% | 16.3% | 13.9% |
| Genius | 1494 | 21.6% | 37.4% | 24.3% | 18.6% | 15.0% |
| Brute | 1494 | 21.3% | 33.6% | 24.1% | 18.6% | 15.3% |
| Sheriff | 1494 | 21.3% | 32.4% | 26.2% | 17.4% | 16.5% |
| Horde | 1494 | 20.3% | 29.7% | 23.7% | 18.2% | 15.8% |
| Clone | 1494 | 21.2% | 29.9% | 22.4% | 19.2% | 18.0% |
| Thief | 1493 | 20.0% | 30.9% | 21.0% | 18.5% | 15.0% |
| Zombie | 1493 | 21.8% | 30.9% | 26.0% | 20.8% | 15.2% |
| Siren | 1493 | 18.9% | 27.7% | 21.2% | 15.1% | 16.2% |
| Infiltrator | 1493 | 19.3% | 30.7% | 18.9% | 17.1% | 15.6% |
| Ethic | 1493 | 22.0% | 33.3% | 27.6% | 20.1% | 14.2% |
| Pincushion | 1492 | 20.9% | 34.1% | 21.2% | 22.4% | 13.1% |
| Scout | 1492 | 20.7% | 30.4% | 20.9% | 21.2% | 15.5% |
| Rage | 1492 | 20.4% | 30.9% | 23.0% | 19.1% | 14.7% |
| Deuce | 1492 | 20.1% | 31.6% | 22.5% | 19.2% | 13.2% |
| Assassin | 1492 | 21.3% | 34.3% | 25.0% | 17.2% | 16.2% |
| Underdog | 1492 | 20.1% | 30.2% | 25.1% | 16.2% | 15.2% |
| Hacker | 1492 | 20.6% | 35.6% | 22.5% | 18.5% | 13.4% |
| Chosen | 1492 | 20.2% | 30.9% | 24.4% | 17.7% | 14.1% |
| Mirror | 1492 | 21.2% | 30.0% | 24.2% | 20.2% | 16.1% |
| Healer | 1492 | 22.6% | 33.1% | 26.0% | 21.0% | 16.8% |
| Empath | 1491 | 21.3% | 34.0% | 24.9% | 18.4% | 15.2% |
| Claw | 1491 | 20.5% | 32.5% | 21.8% | 17.0% | 16.7% |
| Loser | 1491 | 17.9% | 30.7% | 25.1% | 16.7% | 7.8% |
| Tick-Tock | 1491 | 21.0% | 33.0% | 22.8% | 18.4% | 16.4% |
| Pentaform | 1490 | 21.2% | 29.9% | 25.2% | 18.2% | 16.7% |
| Calculator | 1490 | 20.1% | 29.4% | 25.4% | 18.9% | 12.6% |
| Negator | 1490 | 21.5% | 34.9% | 24.8% | 16.4% | 16.6% |
| Silencer | 1490 | 22.0% | 35.1% | 23.9% | 20.0% | 15.1% |
| Yin | 1490 | 21.3% | 35.0% | 24.5% | 18.3% | 15.7% |
| Citadel | 1490 | 21.3% | 32.2% | 22.9% | 21.6% | 14.5% |
| Sorcerer | 1489 | 20.4% | 29.2% | 24.2% | 17.3% | 15.8% |
| Reserve | 1489 | 19.5% | 29.1% | 20.5% | 16.5% | 16.3% |
| Mite | 1489 | 20.9% | 32.5% | 24.7% | 18.4% | 14.4% |
| Antimatter | 1489 | 18.0% | 30.5% | 25.7% | 17.4% | 7.3% |
| Sniveler | 1488 | 21.0% | 27.6% | 24.5% | 20.2% | 15.9% |
| Masochist | 1488 | 20.3% | 27.3% | 23.7% | 16.2% | 17.6% |
| Butler | 1488 | 20.5% | 33.8% | 21.4% | 17.7% | 15.7% |
| Pickpocket | 1486 | 20.2% | 27.2% | 24.4% | 18.1% | 15.9% |

## Game Rules Reference

The simulator follows [Fantasy Flight Games Cosmic Encounter](https://www.fantasyflightgames.com/en/products/cosmic-encounter/) rules.

### Implemented Rules

**Core Game Flow**
- Full 8-Phase Encounter Sequence: Start Turn → Regroup → Destiny → Launch → Alliance → Planning → Reveal → Resolution
- Variable Player Count: 3-6 players
- Victory Condition: 5 foreign colonies to win
- Shared Victory: Multiple players can win simultaneously

**Card System**
- Attack Cards: Values 0-40 for combat
- Negotiate Cards: Force deals or gain compensation
- Morph Cards: Copy opponent's attack card value
- Reinforcement Cards: +2 to +5 bonuses

**Artifact Cards**
- Cosmic Zap: Cancel alien power for one encounter
- Mobius Tubes: Free all your ships from the warp
- Force Field: End encounter with no winner/loser
- Card Zap: Cancel an encounter card
- Ionic Gas: Remove all allies from encounter
- Plague: Send ships from a colony to warp
- Emotion Control: Force opponent to play negotiate
- Quash: Cancel flare or artifact effects

**Combat Resolution**
- Attack vs Attack: Card value + ships = total; higher wins (defense wins ties)
- Negotiate vs Attack: Attack wins; negotiator gets compensation
- Negotiate vs Negotiate: Players must make a deal or both lose 3 ships

**Alliance Mechanics**
- Both offense and defense invite allies
- Allies commit 1-4 ships from colonies
- Offensive allies share in colony; defensive allies get cards or retrieve ships

**Special Mechanics**
- New Hand: Draw new hand when out of encounter cards
- Warp: Ships lost in encounters go to warp
- Regroup: Retrieve 1 ship from warp at turn start
- Second Encounter: Offense can take second encounter if they won first
- Power Loss: Lose alien power when reduced to 1-2 home colonies

### Not Yet Implemented

- Lucre (money system)
- Hidden Powers variant
- Multi-Power Mode (2 powers per player)
- Team Games (2v2, 3v3)
- Full Flare Effects (wild/super distinctions)
- Kicker Cards


<!-- SIMULATION_RESULTS_START -->

## Simulation Results

**Total Games Simulated:** 5,021,972
**Solo Victories:** 4,925,213
**Shared Victories:** 96,759
**Average Game Length:** 4.9 turns
**Last Updated:** 2025-12-30T22:35:33

### Alien Power Rankings (by ELO)

| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |
|------|-------|-----|----------|-------|-----------|--------|
| 1 | Ritualist | 173 | 33.8% | 293 | 99 | 0 |
| 2 | Parasite | 167 | 45.8% | 102032 | 46078 | 699 |
| 3 | Machine | 161 | 57.1% | 101666 | 56144 | 1899 |
| 4 | Yardmaster | 151 | 28.6% | 343 | 92 | 6 |
| 5 | Xenophobe | 147 | 23.3% | 101660 | 22826 | 846 |
| 6 | Recycler | 147 | 25.9% | 351 | 88 | 3 |
| 7 | Pincushion | 146 | 21.2% | 102045 | 20808 | 824 |
| 8 | Overlord | 146 | 21.5% | 101399 | 20952 | 844 |
| 9 | Extortionist | 143 | 21.5% | 101265 | 20951 | 850 |
| 10 | Fortress | 133 | 26.8% | 102250 | 26267 | 1141 |
| 11 | Engineer | 132 | 23.7% | 101607 | 23245 | 876 |
| 12 | Quake | 132 | 21.3% | 101812 | 20804 | 888 |
| 13 | Aristocrat | 132 | 24.8% | 101522 | 24339 | 872 |
| 14 | Insider | 132 | 25.7% | 354 | 90 | 1 |
| 15 | Guarantor | 131 | 24.0% | 334 | 72 | 8 |
| 16 | Veteran | 131 | 27.3% | 101878 | 26778 | 996 |
| 17 | Oracle | 131 | 21.6% | 101673 | 21111 | 893 |
| 18 | Jammer | 131 | 21.4% | 102204 | 21017 | 871 |
| 19 | Rage | 130 | 21.5% | 101270 | 20959 | 848 |
| 20 | Underdog | 130 | 21.2% | 102233 | 20819 | 876 |
| 21 | Crone | 130 | 21.4% | 101888 | 20933 | 882 |
| 22 | Decoy | 129 | 21.6% | 102181 | 21160 | 871 |
| 23 | Echo | 129 | 21.5% | 102692 | 21167 | 907 |
| 24 | Hate | 128 | 21.7% | 101625 | 21236 | 858 |
| 25 | Leviathan | 126 | 20.7% | 102638 | 20839 | 407 |
| 26 | Chronos | 118 | 21.4% | 102374 | 21019 | 883 |
| 27 | Shaman | 118 | 23.9% | 364 | 85 | 2 |
| 28 | Empath | 117 | 21.4% | 102037 | 20936 | 878 |
| 29 | Thief | 117 | 21.5% | 101938 | 21064 | 838 |
| 30 | Kamikaze | 117 | 21.4% | 102063 | 21022 | 810 |
| 31 | Ghast | 117 | 22.3% | 101880 | 21803 | 940 |
| 32 | Harbinger | 117 | 21.5% | 101660 | 21038 | 860 |
| 33 | Lancer | 117 | 24.6% | 101939 | 24142 | 917 |
| 34 | Grifter | 117 | 21.5% | 102075 | 21127 | 798 |
| 35 | Vanguard | 117 | 21.4% | 32126 | 6608 | 279 |
| 36 | Veto | 117 | 23.6% | 335 | 78 | 1 |
| 37 | Butler | 117 | 21.5% | 102398 | 21107 | 869 |
| 38 | Surge | 117 | 21.5% | 102172 | 21038 | 892 |
| 39 | Enchanter | 116 | 26.7% | 352 | 91 | 3 |
| 40 | Genius | 116 | 21.5% | 102019 | 21046 | 898 |
| ... | *222 more aliens* | ... | ... | ... | ... | ... |

<!-- SIMULATION_RESULTS_END -->
