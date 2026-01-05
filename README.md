# Cosmic Encounter Simulator

<!-- NOTE: Only update the stats table below or feature implementation status. Do not modify other sections unless specifically requested. -->

A simulation of the board game Cosmic Encounter for analyzing alien power balance. Features **5700+ alien powers**, multiple AI strategies (including AggressiveAI, CautiousAI, OpportunisticAI, SocialAI, AdaptiveAI, LearningAI), and comprehensive statistics tracking across 2-6 player games.

## Basic Game Rules / Flow of the Simulator


### Encounter Phases

Each encounter follows these sequential phases:

1. **START_TURN** - Checks if active player has encounter cards (minimum 1 required)
2. **REGROUP** - Offense retrieves 1 ship from warp to any home colony
3. **DESTINY** - Determine defender (draw destiny deck, or offense chooses in 2-player mode)
4. **LAUNCH** - Offense aims hyperspace gate at defender's planet, commits 1-4 ships
5. **ALLIANCE** - Both sides invite allies; allies commit ships to either side
6. **PLANNING** - Both sides secretly select encounter cards (and optional kicker cards)
7. **REVEAL** - Cards revealed; flare cards can be played
8. **RESOLUTION** - Winner determined, ships go to warp or establish colonies


### Combat Resolution

```
OFFENSE TOTAL = Card Value + Ship Count + Kickers + Power Mods + Reinforcements + Tech Bonus
DEFENSE TOTAL = Card Value + Ship Count + Kickers + Power Mods + Reinforcements + Tech Bonus + Station Bonus
```

- **Attack vs Attack**: Higher total wins (or lower if Loser/Antimatter power active)
- **Both Negotiate**: Deal phase triggered; failed deals send 3 ships each to warp
- **Negotiate vs Attack**: Attacker wins; negotiator receives compensation (1 card per ship committed)


### Win Conditions

- **Standard**: Establish 5 foreign colonies (4 in 2-player mode)
- **Alternate Wins**: Some alien powers have special victory conditions
- **Shared Victories**: Multiple players can win simultaneously


### Turn Progression

- One encounter per turn normally
- Second encounter allowed if offense won/dealt AND has encounter cards remaining
- Machine power allows multiple encounters regardless of outcome

---

## Feature Implementation Status


### Core Mechanics

| Feature | Status | Notes |
|---------|--------|-------|
| **Encounter Phases** | ✅ Full | All 8 phases implemented with proper sequencing |
| **Combat Resolution** | ✅ Full | Attack totals, ship counting, reinforcements, kickers |
| **Win Condition Checking** | ✅ Full | Standard wins + alternate win conditions per alien |
| **Warp System** | ✅ Full | Ships to warp on loss, regroup retrieval |
| **Colony System** | ✅ Full | Foreign colony tracking, home colony defense |
| **Second Encounters** | ✅ Full | Win/deal = second encounter opportunity |


### Card Types

| Card Type | Status | Implementation Details |
|-----------|--------|------------------------|
| **Attack Cards** | ✅ Full | Values 0-40 per official distribution (49 cards total) |
| **Negotiate Cards** | ✅ Full | 15 cards; triggers deal phase or compensation |
| **Morph Cards** | ✅ Full | 2 cards; copies opponent's card value |
| **Reinforcement Cards** | ✅ Full | 6 cards (+2, +3, +5); added during resolution |
| **Kicker Cards** | ✅ Full | Multipliers (×2, ×3, ×4, ×-1) applied to attack value |
| **Artifact Cards** | ✅ Full | 14 types with one-time special effects |
| **Flare Cards** | ✅ Full | Wild & Super effects; one per alien in game |


### Artifact Cards

| Artifact | Effect |
|----------|--------|
| Cosmic Zap | Disable an alien power for this encounter |
| Card Zap | Force opponent to discard their played card |
| Mobius Tubes | Return ships from warp |
| Force Field | Cancel the encounter entirely |
| Emotion Control | Take control of opponent's choice |
| Quash | Prevent power activation |
| Ionic Gas | Remove all allies from encounter |
| Plague | Opponent draws fewer cards |
| Omni Zap | Zap any cosmic deck card |
| Solar Wind | Re-aim the hyperspace gate |
| Rebirth | Return destroyed ships |
| Ship Zap | Remove opponent ships from encounter |
| Hand Zap | Force opponent to discard hand |
| Space Junk | Reduce opponent's ship count |
| Victory Boon | Gain extra colony toward win |


### Alliance & Negotiation

| Feature | Status | Notes |
|---------|--------|-------|
| **Alliance Invitations** | ✅ Full | Both sides can invite; allies commit ships |
| **Defensive Ally Rewards** | ✅ Full | Choice of cards OR ships from warp (1 per ship committed) |
| **Offensive Ally Rewards** | ✅ Full | Colony establishment on successful attack |
| **Compensation** | ✅ Full | 1 card per ship when negotiate loses to attack |
| **Failed Deal Penalty** | ✅ Full | Both negotiate cards = 3 ships to warp each |
| **Deal Types** | ✅ Full | Colony swap, card trade, one-sided colony, card-for-colony |
| **Parasite Exception** | ✅ Full | Can join alliances uninvited |


### Expansions

| Expansion | Status | Features Implemented |
|-----------|--------|---------------------|
| **Base Game** | ✅ Full | 50 official aliens, all core rules |
| **Cosmic Incursion** | ⚠️ Partial | Tech deck ✅, 20 aliens ✅ |
| **Cosmic Conflict** | ⚠️ Partial | Hazard deck ✅, 20 aliens ✅ |
| **Cosmic Alliance** | ⚠️ Partial | Team rules framework, 20 aliens ✅ |
| **Cosmic Storm** | ⚠️ Partial | Space Stations (Alpha, Beta, Delta, Gamma, Omega, Sigma, Theta, Kappa) ✅, 25 aliens ✅ |
| **Cosmic Dominion** | ⚠️ Partial | 30 aliens ✅ |
| **Cosmic Eons** | ⚠️ Partial | 30 aliens ✅ |
| **Cosmic Odyssey** | ⚠️ Partial | 42 aliens ✅, Lux/Rifts framework only |


### Tech Deck (Cosmic Incursion)

| Feature | Status | Notes |
|---------|--------|-------|
| Research Progress | ✅ Full | Per-player tracking |
| Tech Categories | ✅ Full | Combat, Defense, Economy, Movement, Special |
| Tech Cards | ✅ Full | 22+ cards with costs 2-4 research points |


### Hazard Deck (Cosmic Conflict)

| Feature | Status | Notes |
|---------|--------|-------|
| Random Hazards | ✅ Full | 20+ hazard cards with encounter effects |
| Combat Modifiers | ✅ Full | Value adjustments during combat |
| Alliance Disruption | ✅ Full | No-alliance hazards |
| Skip Encounters | ✅ Full | Automatic pass hazards |


### Space Stations (Cosmic Alliance)

| Station | Effect | Status |
|---------|--------|--------|
| Alpha | +2 defense bonus | ✅ |
| Beta | +2 offense bonus | ✅ |
| Delta | Counts as colony for alliance | ✅ |
| Gamma | +1 ship retrieval from warp | ✅ |
| Omega | Launch from empty planet with station | ✅ |
| Sigma | +1 card draw on win | ✅ |
| Theta | +1 max ships (5 instead of 4) | ✅ |
| Kappa | +1 ally invitation | ✅ |


### 2-Player Variant

| Feature | Status | Notes |
|---------|--------|-------|
| Dual Powers | ✅ Full | Each player gets 2 alien powers |
| Reduced Win Condition | ✅ Full | 4 colonies instead of 5 |
| Direct Targeting | ✅ Full | Offense chooses target (no destiny deck) |
| Alternating Turns | ✅ Full | Strict turn alternation |


### AI Strategies

| AI Type | Strategy | Card Selection |
|---------|----------|----------------|
| BasicAI | Simple heuristics | Weighted random |
| RandomAI | No strategy | Completely random |
| StrategicAI | Optimal play | Game state analysis |
| AdaptiveAI | Learning | Adjusts mid-game |
| TacticalAI | Position-based | Territory analysis |
| PersonalityAI | Themed | Role-playing decisions |
| AggressiveAI | Maximum ships | High commitment |
| CautiousAI | Minimal risk | Conservative play |
| OpportunisticAI | Exploit weakness | Target weak players |
| SocialAI | Alliance-focused | Favor ally relationships |


### Alien Power System

| Feature | Status | Notes |
|---------|--------|-------|
| Power Hooks | ✅ Full | 40+ hook methods for phase-specific activation |
| Power Categories | ✅ Full | GREEN (simple), YELLOW (moderate), RED (complex) |
| Mandatory vs Optional | ✅ Full | Power type determines if activation is required |
| Role Restrictions | ✅ Full | Powers can restrict to offense/defense/ally/not-involved |
| Power Zapping | ✅ Full | Cosmic Zap disables powers for encounter |
| Power Loss | ✅ Full | Lose all home colonies = power deactivates |
| Total Powers | ✅ Full | 4509+ implemented (50 official base + expansions + custom) |

---

## Notable Implementation Decisions


### Faithful to Official Rules

- **Ship counts**: 1-4 ships per encounter (base rules)
- **Compensation**: Exactly 1 card per ship when negotiate loses
- **Failed deals**: 3 ship penalty per player (or all if fewer)
- **Rewards**: Defensive allies choose cards OR ships (1 per committed)
- **Second encounters**: Only if won/dealt AND have encounter cards
- **Colony definition**: Ships on opponent's planet = foreign colony


### Simplified from Official Rules

| Area | Simplification | Reason |
|------|---------------|--------|
| Destiny redraw | No timer for self-destiny | Simulation simplicity |
| Deal negotiation | Basic deal types only | AI complexity reduction |
| Ally invitations | Single round, no back-and-forth | Simulation speed |
| Flare timing | Single-phase activation | Reduced state complexity |
| Card counting | AI doesn't track played cards | Performance optimization |


### Architectural Decisions

| Decision | Rationale |
|----------|-----------|
| Event-driven power hooks | Allows clean phase-specific activation without monolithic switch statements |
| GamePhase enum state machine | Clear phase progression, easy debugging |
| Pluggable AI strategies | Enables strategy comparison and personality experiments |
| One file per alien power | Maintainability with 4500+ powers |
| Full type hints | Catches errors early, improves IDE support |


### Not Implemented

| Feature | Status | Notes |
|---------|--------|-------|
| Lux Currency (Odyssey) | Framework only | Economy system scaffolded but not active |
| Rift Cards (Odyssey) | Framework only | Trap system scaffolded but not active |
| Cross-power synergy tracking | Limited | Some power interactions may not fully compound |
| Tournament timing rules | Not implemented | Simulation doesn't enforce time limits |

---

## Alien Power Rankings

> **1,000,000** games simulated | Last updated: 2026-01-05 23:42
>
> Rankings based on overall win rate across 2-6 player games. See [STATISTICS.md](STATISTICS.md) for full rankings.

| Rank | Power | Set | Overall | 2P | 3P | 4P | 5P | 6P | Games |
|-----:|:------|:----|--------:|---:|---:|---:|---:|---:|------:|
| 1 | Machine | Base Game | 56.5% | 72.7% | 66.6% | 62.1% | 53.3% | 45.3% | 8,289 |
| 2 | Parasite | Base Game | 46.1% | 49.0% | 45.9% | 48.3% | 46.5% | 43.1% | 8,547 |
| 3 | Pacifist | Base Game | 34.3% | 73.7% | 53.6% | 36.0% | 24.2% | 18.4% | 8,464 |
| 4 | Neighbor | Cosmic Storm | 34.0% | 73.5% | 50.2% | 31.5% | 25.3% | 21.8% | 8,427 |
| 5 | Dervish | Cosmic Storm | 33.0% | 76.8% | 49.1% | 33.3% | 22.6% | 18.5% | 8,399 |
| 6 | Disease | Cosmic Incursion | 31.6% | 49.5% | 42.9% | 32.3% | 26.2% | 23.5% | 8,252 |
| 7 | Dragon | Cosmic Odyssey | 31.5% | 69.0% | 46.8% | 29.9% | 22.5% | 19.8% | 8,268 |
| 8 | Industrialist | Cosmic Conflict | 31.1% | 67.0% | 47.2% | 30.1% | 23.5% | 18.6% | 8,432 |
| 9 | Winner | Cosmic Alliance | 30.0% | 61.4% | 42.2% | 30.0% | 22.8% | 18.9% | 8,334 |
| 10 | Locust_Alt | Cosmic Odyssey | 29.5% | 63.6% | 40.7% | 30.7% | 22.5% | 17.5% | 8,271 |
| 11 | Pygmy | Cosmic Alliance | 29.4% | 62.8% | 42.3% | 27.1% | 23.2% | 18.1% | 8,294 |
| 12 | Usurper | Cosmic Dominion | 29.0% | 57.5% | 41.4% | 28.7% | 22.6% | 18.8% | 8,375 |
| 13 | Mutant | Base Game | 28.9% | 58.3% | 40.6% | 30.3% | 21.8% | 18.8% | 8,602 |
| 14 | Tortoise | Cosmic Eons | 28.3% | 55.8% | 40.8% | 28.5% | 22.2% | 18.0% | 8,348 |
| 15 | Arcade | Cosmic Storm | 27.9% | 53.4% | 39.9% | 27.8% | 20.9% | 18.9% | 8,471 |
| 16 | Bulwark | Cosmic Storm | 27.8% | 60.0% | 39.4% | 27.8% | 21.0% | 17.1% | 8,453 |
| 17 | Symbiote | Cosmic Incursion | 27.8% | 59.2% | 38.3% | 26.4% | 21.3% | 17.5% | 8,345 |
| 18 | Masochist_Alt | Cosmic Odyssey | 27.7% | 59.5% | 37.0% | 28.7% | 20.5% | 17.7% | 8,372 |
| 19 | Hunger | Cosmic Eons | 27.5% | 53.6% | 41.2% | 25.9% | 20.4% | 19.3% | 8,411 |
| 20 | Lightning | Cosmic Alliance | 27.5% | 56.9% | 39.6% | 25.8% | 21.4% | 17.5% | 8,444 |
| 21 | Tyrant | Cosmic Storm | 27.4% | 54.3% | 35.2% | 27.5% | 22.1% | 18.7% | 8,407 |
| 22 | Angler | Cosmic Dominion | 27.4% | 55.1% | 37.5% | 28.2% | 20.9% | 16.9% | 8,403 |
| 23 | Patriot | Cosmic Storm | 27.3% | 58.4% | 39.6% | 26.3% | 21.1% | 16.9% | 8,372 |
| 24 | Invader | Cosmic Conflict | 27.3% | 52.2% | 36.7% | 28.4% | 23.0% | 17.2% | 8,364 |
| 25 | Gorgon | Cosmic Alliance | 27.1% | 57.7% | 36.3% | 28.5% | 20.0% | 17.9% | 8,245 |
| 26 | Cyborg | Cosmic Alliance | 27.0% | 56.7% | 36.6% | 27.7% | 21.3% | 17.0% | 8,493 |
| 27 | Brute | Cosmic Storm | 26.9% | 51.0% | 37.1% | 26.0% | 23.3% | 17.5% | 8,399 |
| 28 | Voyager | Cosmic Dominion | 26.8% | 53.8% | 36.6% | 26.3% | 20.8% | 18.4% | 8,365 |
| 29 | Outlaw | Cosmic Storm | 26.8% | 50.0% | 37.0% | 26.8% | 21.9% | 17.7% | 8,377 |
| 30 | Guerrilla | Cosmic Incursion | 26.8% | 53.1% | 38.2% | 26.0% | 21.5% | 17.3% | 8,372 |
| 31 | Citadel | Base Game | 26.5% | 58.0% | 37.7% | 25.6% | 20.9% | 15.7% | 8,358 |
| 32 | Reactor | Cosmic Dominion | 26.4% | 58.5% | 35.4% | 27.6% | 19.5% | 15.5% | 8,327 |
| 33 | Cavalry | Cosmic Conflict | 26.2% | 54.3% | 34.6% | 25.5% | 21.4% | 18.1% | 8,282 |
| 34 | Engineer | Cosmic Dominion | 26.2% | 52.0% | 36.0% | 27.0% | 20.2% | 17.2% | 8,405 |
| 35 | Void | Base Game | 26.1% | 51.7% | 34.5% | 25.7% | 20.9% | 18.0% | 8,353 |
| 36 | Porcupine | Cosmic Storm | 26.1% | 52.6% | 36.0% | 25.9% | 20.3% | 17.4% | 8,454 |
| 37 | Reincarnator | Base Game | 26.0% | 52.8% | 35.7% | 25.2% | 20.4% | 17.2% | 8,390 |
| 38 | Hurtz | Cosmic Odyssey | 26.0% | 51.9% | 33.8% | 28.4% | 20.3% | 16.5% | 8,421 |
| 39 | Sheriff | Cosmic Eons | 25.9% | 55.9% | 34.5% | 27.0% | 19.7% | 16.5% | 8,418 |
| 40 | Reborn | Cosmic Alliance | 25.8% | 52.1% | 35.9% | 25.8% | 19.7% | 16.5% | 8,475 |
| 41 | Grumpus_Alt | Cosmic Odyssey | 25.8% | 50.3% | 34.0% | 26.1% | 22.7% | 16.4% | 8,359 |
| 42 | Healer | Base Game | 25.8% | 52.7% | 37.3% | 26.4% | 20.0% | 16.1% | 8,442 |
| 43 | FireDancer | Cosmic Eons | 25.7% | 48.2% | 35.0% | 26.1% | 21.0% | 17.4% | 8,453 |
| 44 | Remora | Base Game | 25.7% | 48.0% | 33.6% | 26.0% | 20.7% | 17.8% | 8,387 |
| 45 | Laser | Cosmic Dominion | 25.6% | 55.1% | 34.3% | 22.9% | 21.4% | 17.0% | 8,258 |
| 46 | Greenhorn | Cosmic Dominion | 25.6% | 49.3% | 34.8% | 27.3% | 19.2% | 16.7% | 8,506 |
| 47 | Dictator | Base Game | 25.6% | 50.5% | 33.7% | 25.6% | 20.3% | 17.9% | 8,398 |
| 48 | Squee | Cosmic Storm | 25.6% | 47.2% | 32.3% | 26.6% | 22.7% | 17.0% | 8,384 |
| 49 | Gremlin | Cosmic Odyssey | 25.6% | 47.9% | 33.8% | 27.2% | 21.1% | 16.3% | 8,401 |
| 50 | Chrysalis | Cosmic Alliance | 25.5% | 48.8% | 32.2% | 27.4% | 20.2% | 17.4% | 8,393 |

*See [STATISTICS.md](STATISTICS.md) for complete rankings of all 238 aliens.*


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


<!-- SIMULATION_RESULTS_START -->

## Simulation Results

**Total Games Simulated:** 999,996
**Solo Victories:** 982,755
**Shared Victories:** 17,241
**Average Game Length:** 4.9 turns
**Last Updated:** 2026-01-05T00:23:07

### Alien Power Rankings (by ELO)

| Rank | Alien | ELO | Win Rate | Games | Solo Wins | Shared |
|------|-------|-----|----------|-------|-----------|--------|
| 1 | Assistant | 163 | 25.3% | 16736 | 4112 | 129 |
| 2 | Clone | 160 | 25.2% | 16776 | 4054 | 167 |
| 3 | Remora | 148 | 25.5% | 16736 | 4127 | 136 |
| 4 | Virus | 147 | 25.4% | 16775 | 4101 | 163 |
| 5 | Moocher | 146 | 25.4% | 16697 | 4110 | 125 |
| 6 | Vox | 146 | 25.7% | 16667 | 4151 | 139 |
| 7 | Gorgon | 142 | 24.9% | 16663 | 4021 | 133 |
| 8 | Chosen | 142 | 25.1% | 16675 | 4047 | 139 |
| 9 | Guardian | 132 | 25.1% | 17014 | 4137 | 131 |
| 10 | Fido | 132 | 24.9% | 17021 | 4104 | 137 |
| 11 | Spiff | 132 | 25.8% | 17035 | 4226 | 161 |
| 12 | PackRat | 132 | 24.9% | 16734 | 4044 | 127 |
| 13 | Schizoid_Alt | 132 | 24.8% | 16745 | 3998 | 153 |
| 14 | Patriot | 132 | 24.9% | 16909 | 4061 | 156 |
| 15 | Bride | 131 | 24.8% | 16832 | 4054 | 126 |
| 16 | Nightmare | 131 | 25.4% | 16847 | 4125 | 154 |
| 17 | Tortoise | 129 | 25.3% | 16912 | 4122 | 156 |
| 18 | Force | 129 | 25.1% | 16722 | 4050 | 139 |
| 19 | Masochist | 120 | 25.8% | 16888 | 4189 | 160 |
| 20 | Extractor | 118 | 25.2% | 16948 | 4137 | 126 |
| 21 | BleedingHeart | 118 | 25.3% | 16681 | 4070 | 142 |
| 22 | Surgeon | 117 | 25.8% | 16804 | 4194 | 149 |
| 23 | Hurtz | 117 | 25.0% | 16802 | 4040 | 154 |
| 24 | Multitude | 117 | 24.9% | 16834 | 4069 | 126 |
| 25 | Greenhorn | 117 | 24.8% | 16901 | 4028 | 162 |
| 26 | Relic | 117 | 25.5% | 16939 | 4170 | 149 |
| 27 | Mind | 117 | 25.5% | 16752 | 4115 | 158 |
| 28 | Cavalry | 117 | 25.7% | 16842 | 4199 | 131 |
| 29 | Cosmos | 117 | 24.9% | 16810 | 4069 | 118 |
| 30 | Magnet | 117 | 25.2% | 17013 | 4127 | 154 |
| 31 | Maven | 116 | 24.6% | 16814 | 4016 | 127 |
| 32 | Boomerang | 116 | 24.6% | 16712 | 3979 | 132 |
| 33 | Claw | 116 | 25.1% | 16670 | 4048 | 131 |
| 34 | Saboteur | 116 | 25.0% | 16780 | 4043 | 144 |
| 35 | Void | 116 | 26.4% | 16618 | 4237 | 148 |
| 36 | FireDancer | 116 | 24.8% | 17081 | 4080 | 154 |
| 37 | Dervish | 116 | 24.4% | 16462 | 3864 | 158 |
| 38 | Coordinator | 116 | 25.7% | 16817 | 4172 | 143 |
| 39 | Voyager | 116 | 25.2% | 16703 | 4063 | 151 |
| 40 | Seeker | 116 | 24.8% | 16575 | 3979 | 129 |
| ... | *198 more aliens* | ... | ... | ... | ... | ... |

<!-- SIMULATION_RESULTS_END -->
