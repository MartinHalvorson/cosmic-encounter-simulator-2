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

> **2,500** games simulated | Last updated: 2025-12-31 21:07
>
> **Tier Guide:** 🟣 S (1600+) | 🔵 A (1550+) | 🟢 B (1500+) | 🟡 C (1450+) | 🔴 D (<1450)


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
<tr>
<td align="left">1</td>
<td align="left">🟢 Machine</td>
<td align="left">Base</td>
<td align="right"><b>1516</b></td>
<td align="right">52.7%</td>
<td align="right">80.0%</td>
<td align="right">50.0%</td>
<td align="right">60.0%</td>
<td align="right">50.0%</td>
<td align="right">43.8%</td>
<td align="right">110</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🟢 Force</td>
<td align="left">Odyssey</td>
<td align="right"><b>1514</b></td>
<td align="right">47.4%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">75.0%</td>
<td align="right">50.0%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Zombie_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1513</b></td>
<td align="right">45.5%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">80.0%</td>
<td align="right">25.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Ethic</td>
<td align="left">Incursion</td>
<td align="right"><b>1512</b></td>
<td align="right">45.2%</td>
<td align="right">66.7%</td>
<td align="right">66.7%</td>
<td align="right">50.0%</td>
<td align="right">42.9%</td>
<td align="right">25.0%</td>
<td align="right">31</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Trickster</td>
<td align="left">Conflict</td>
<td align="right"><b>1511</b></td>
<td align="right">42.1%</td>
<td align="right">100.0%</td>
<td align="right">40.0%</td>
<td align="right">66.7%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Warhawk</td>
<td align="left">Conflict</td>
<td align="right"><b>1510</b></td>
<td align="right">41.7%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">66.7%</td>
<td align="right">12</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Ghoul</td>
<td align="left">Incursion</td>
<td align="right"><b>1510</b></td>
<td align="right">40.9%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">27.3%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Parasite</td>
<td align="left">Base</td>
<td align="right"><b>1510</b></td>
<td align="right">41.3%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">50.0%</td>
<td align="right">40.6%</td>
<td align="right">35.3%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Moocher</td>
<td align="left">Eons</td>
<td align="right"><b>1509</b></td>
<td align="right">38.9%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">14.3%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Genius</td>
<td align="left">Incursion</td>
<td align="right"><b>1509</b></td>
<td align="right">38.9%</td>
<td align="right">100.0%</td>
<td align="right">25.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 General</td>
<td align="left">Alliance</td>
<td align="right"><b>1508</b></td>
<td align="right">38.1%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 YinYang</td>
<td align="left">Dominion</td>
<td align="right"><b>1508</b></td>
<td align="right">37.5%</td>
<td align="right">100.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">66.7%</td>
<td align="right">20.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Wormhole</td>
<td align="left">Storm</td>
<td align="right"><b>1508</b></td>
<td align="right">37.5%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Dervish</td>
<td align="left">Storm</td>
<td align="right"><b>1508</b></td>
<td align="right">37.5%</td>
<td align="right">80.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">33.3%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Visionary</td>
<td align="left">Conflict</td>
<td align="right"><b>1508</b></td>
<td align="right">37.5%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">100.0%</td>
<td align="right">25.0%</td>
<td align="right">14.3%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Pacifist</td>
<td align="left">Base</td>
<td align="right"><b>1507</b></td>
<td align="right">37.3%</td>
<td align="right">90.5%</td>
<td align="right">27.3%</td>
<td align="right">37.5%</td>
<td align="right">22.2%</td>
<td align="right">20.0%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Console_Cowboy</td>
<td align="left">Custom</td>
<td align="right"><b>1507</b></td>
<td align="right">36.8%</td>
<td align="right">64.7%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">18.2%</td>
<td align="right">33.3%</td>
<td align="right">125</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Symbiote</td>
<td align="left">Incursion</td>
<td align="right"><b>1507</b></td>
<td align="right">36.4%</td>
<td align="right">100.0%</td>
<td align="right">66.7%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Seeker</td>
<td align="left">Incursion</td>
<td align="right"><b>1507</b></td>
<td align="right">36.4%</td>
<td align="right">100.0%</td>
<td align="right">40.0%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">14.3%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Sheriff</td>
<td align="left">Eons</td>
<td align="right"><b>1506</b></td>
<td align="right">35.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">66.7%</td>
<td align="right">60.0%</td>
<td align="right">14.3%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 Perfectionist</td>
<td align="left">Eons</td>
<td align="right"><b>1506</b></td>
<td align="right">35.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">16.7%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Mutant</td>
<td align="left">Base</td>
<td align="right"><b>1506</b></td>
<td align="right">34.8%</td>
<td align="right">66.7%</td>
<td align="right">38.5%</td>
<td align="right">40.7%</td>
<td align="right">21.4%</td>
<td align="right">25.0%</td>
<td align="right">115</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Mimic</td>
<td align="left">Conflict</td>
<td align="right"><b>1506</b></td>
<td align="right">34.5%</td>
<td align="right">66.7%</td>
<td align="right">44.4%</td>
<td align="right">33.3%</td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
<td align="right">29</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Drone_Pilot</td>
<td align="left">Custom</td>
<td align="right"><b>1505</b></td>
<td align="right">33.7%</td>
<td align="right">87.5%</td>
<td align="right">50.0%</td>
<td align="right">19.0%</td>
<td align="right">37.0%</td>
<td align="right">17.2%</td>
<td align="right">101</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Warpish</td>
<td align="left">Base</td>
<td align="right"><b>1505</b></td>
<td align="right">33.6%</td>
<td align="right">80.0%</td>
<td align="right">30.0%</td>
<td align="right">28.0%</td>
<td align="right">37.5%</td>
<td align="right">23.7%</td>
<td align="right">125</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Sycophant</td>
<td align="left">Storm</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">25.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Cloak</td>
<td align="left">Eons</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">100.0%</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Neighbor</td>
<td align="left">Storm</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">100.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">15</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟢 Angler</td>
<td align="left">Dominion</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">100.0%</td>
<td align="right">42.9%</td>
<td align="right">16.7%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟢 Hypochondriac</td>
<td align="left">Eons</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">33.3%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟢 Maven</td>
<td align="left">Eons</td>
<td align="right"><b>1505</b></td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟢 Cudgel</td>
<td align="left">Base</td>
<td align="right"><b>1505</b></td>
<td align="right">33.0%</td>
<td align="right">66.7%</td>
<td align="right">33.3%</td>
<td align="right">29.2%</td>
<td align="right">29.0%</td>
<td align="right">30.0%</td>
<td align="right">109</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟢 Macron</td>
<td align="left">Base</td>
<td align="right"><b>1505</b></td>
<td align="right">33.0%</td>
<td align="right">75.0%</td>
<td align="right">53.3%</td>
<td align="right">27.8%</td>
<td align="right">18.2%</td>
<td align="right">30.8%</td>
<td align="right">100</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟢 Klutz</td>
<td align="left">Eons</td>
<td align="right"><b>1504</b></td>
<td align="right">31.8%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">28.6%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟢 Reborn</td>
<td align="left">Alliance</td>
<td align="right"><b>1504</b></td>
<td align="right">31.6%</td>
<td align="right">66.7%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟢 Industrialist</td>
<td align="left">Conflict</td>
<td align="right"><b>1504</b></td>
<td align="right">31.6%</td>
<td align="right">0.0%</td>
<td align="right">60.0%</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟢 Megacorp</td>
<td align="left">Custom</td>
<td align="right"><b>1504</b></td>
<td align="right">31.6%</td>
<td align="right">75.0%</td>
<td align="right">35.3%</td>
<td align="right">33.3%</td>
<td align="right">27.0%</td>
<td align="right">16.7%</td>
<td align="right">117</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟢 Zombie</td>
<td align="left">Base</td>
<td align="right"><b>1504</b></td>
<td align="right">31.6%</td>
<td align="right">64.3%</td>
<td align="right">54.2%</td>
<td align="right">25.0%</td>
<td align="right">16.7%</td>
<td align="right">22.7%</td>
<td align="right">136</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟢 Pentaform</td>
<td align="left">Dominion</td>
<td align="right"><b>1504</b></td>
<td align="right">31.2%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟢 Empath</td>
<td align="left">Conflict</td>
<td align="right"><b>1504</b></td>
<td align="right">31.2%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟢 Citadel</td>
<td align="left">Base</td>
<td align="right"><b>1503</b></td>
<td align="right">31.0%</td>
<td align="right">50.0%</td>
<td align="right">26.7%</td>
<td align="right">35.7%</td>
<td align="right">29.4%</td>
<td align="right">21.2%</td>
<td align="right">116</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟢 FireDancer</td>
<td align="left">Eons</td>
<td align="right"><b>1503</b></td>
<td align="right">30.8%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">13</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟢 Hacker</td>
<td align="left">Base</td>
<td align="right"><b>1503</b></td>
<td align="right">30.6%</td>
<td align="right">75.0%</td>
<td align="right">47.1%</td>
<td align="right">40.0%</td>
<td align="right">25.7%</td>
<td align="right">9.7%</td>
<td align="right">111</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟢 Hunger</td>
<td align="left">Eons</td>
<td align="right"><b>1503</b></td>
<td align="right">30.4%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">16.7%</td>
<td align="right">23</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟢 Pygmy</td>
<td align="left">Alliance</td>
<td align="right"><b>1503</b></td>
<td align="right">30.4%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">23</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟢 PackRat</td>
<td align="left">Eons</td>
<td align="right"><b>1503</b></td>
<td align="right">30.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟢 Perfectionist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1503</b></td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">16.7%</td>
<td align="right">40.0%</td>
<td align="right">25.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟢 Synthetic</td>
<td align="left">Custom</td>
<td align="right"><b>1503</b></td>
<td align="right">29.8%</td>
<td align="right">60.0%</td>
<td align="right">52.6%</td>
<td align="right">25.0%</td>
<td align="right">31.2%</td>
<td align="right">3.3%</td>
<td align="right">124</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟢 Bubble</td>
<td align="left">Odyssey</td>
<td align="right"><b>1503</b></td>
<td align="right">29.6%</td>
<td align="right">60.0%</td>
<td align="right">40.0%</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">27</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟢 Dictator</td>
<td align="left">Base</td>
<td align="right"><b>1503</b></td>
<td align="right">29.7%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">35.3%</td>
<td align="right">17.4%</td>
<td align="right">27.3%</td>
<td align="right">101</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟢 Bride</td>
<td align="left">Dominion</td>
<td align="right"><b>1503</b></td>
<td align="right">29.4%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟢 Guerrilla</td>
<td align="left">Incursion</td>
<td align="right"><b>1503</b></td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
<td align="right">57.1%</td>
<td align="right">75.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">34</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟢 Porcupine</td>
<td align="left">Storm</td>
<td align="right"><b>1503</b></td>
<td align="right">29.4%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">37.5%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟢 Neon</td>
<td align="left">Custom</td>
<td align="right"><b>1502</b></td>
<td align="right">29.4%</td>
<td align="right">40.0%</td>
<td align="right">42.1%</td>
<td align="right">40.0%</td>
<td align="right">13.0%</td>
<td align="right">23.3%</td>
<td align="right">102</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟢 Virus</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">28.8%</td>
<td align="right">71.4%</td>
<td align="right">45.8%</td>
<td align="right">24.0%</td>
<td align="right">22.6%</td>
<td align="right">16.1%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟢 Hacker_Cyber</td>
<td align="left">Custom</td>
<td align="right"><b>1502</b></td>
<td align="right">28.7%</td>
<td align="right">72.7%</td>
<td align="right">42.9%</td>
<td align="right">35.0%</td>
<td align="right">20.0%</td>
<td align="right">12.1%</td>
<td align="right">108</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟢 Vacuum</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">28.7%</td>
<td align="right">75.0%</td>
<td align="right">52.4%</td>
<td align="right">25.9%</td>
<td align="right">16.1%</td>
<td align="right">5.9%</td>
<td align="right">129</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟢 Grumpus</td>
<td align="left">Storm</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">16.7%</td>
<td align="right">12.5%</td>
<td align="right">40.0%</td>
<td align="right">28</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟢 Negator</td>
<td align="left">Odyssey</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟢 Love</td>
<td align="left">Dominion</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟢 Silencer</td>
<td align="left">Odyssey</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">50.0%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟢 Cryo</td>
<td align="left">Incursion</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟢 Assessor</td>
<td align="left">Odyssey</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟢 Observer</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">28.6%</td>
<td align="right">71.4%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">22.2%</td>
<td align="right">21.6%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟢 Warrior</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">28.4%</td>
<td align="right">50.0%</td>
<td align="right">41.2%</td>
<td align="right">17.9%</td>
<td align="right">32.1%</td>
<td align="right">21.2%</td>
<td align="right">116</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟢 TheCult</td>
<td align="left">Eons</td>
<td align="right"><b>1502</b></td>
<td align="right">28.0%</td>
<td align="right">100.0%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">25.0%</td>
<td align="right">25</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟢 Tripler</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">28.0%</td>
<td align="right">85.7%</td>
<td align="right">45.0%</td>
<td align="right">29.4%</td>
<td align="right">12.5%</td>
<td align="right">12.0%</td>
<td align="right">93</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟢 Daredevil_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1502</b></td>
<td align="right">27.8%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">16.7%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟢 Lemming</td>
<td align="left">Odyssey</td>
<td align="right"><b>1502</b></td>
<td align="right">27.8%</td>
<td align="right">0.0%</td>
<td align="right">66.7%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟢 Human</td>
<td align="left">Base</td>
<td align="right"><b>1501</b></td>
<td align="right">27.4%</td>
<td align="right">58.8%</td>
<td align="right">33.3%</td>
<td align="right">15.4%</td>
<td align="right">25.8%</td>
<td align="right">15.8%</td>
<td align="right">117</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟢 Disease</td>
<td align="left">Incursion</td>
<td align="right"><b>1501</b></td>
<td align="right">27.3%</td>
<td align="right">60.0%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟢 Host</td>
<td align="left">Dominion</td>
<td align="right"><b>1501</b></td>
<td align="right">27.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">60.0%</td>
<td align="right">11</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟢 Oracle</td>
<td align="left">Base</td>
<td align="right"><b>1501</b></td>
<td align="right">27.3%</td>
<td align="right">50.0%</td>
<td align="right">31.2%</td>
<td align="right">33.3%</td>
<td align="right">25.7%</td>
<td align="right">12.9%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟢 Extractor</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">26.9%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">14.3%</td>
<td align="right">26</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟢 Tourist</td>
<td align="left">Dominion</td>
<td align="right"><b>1501</b></td>
<td align="right">26.7%</td>
<td align="right">66.7%</td>
<td align="right">50.0%</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">15</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟢 Masochist</td>
<td align="left">Base</td>
<td align="right"><b>1501</b></td>
<td align="right">26.4%</td>
<td align="right">33.3%</td>
<td align="right">31.8%</td>
<td align="right">33.3%</td>
<td align="right">26.9%</td>
<td align="right">16.1%</td>
<td align="right">106</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟢 Coward</td>
<td align="left">Eons</td>
<td align="right"><b>1501</b></td>
<td align="right">26.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟢 Neural_Link</td>
<td align="left">Custom</td>
<td align="right"><b>1501</b></td>
<td align="right">26.3%</td>
<td align="right">36.4%</td>
<td align="right">40.0%</td>
<td align="right">42.3%</td>
<td align="right">22.6%</td>
<td align="right">12.5%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟢 Chosen</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">26.1%</td>
<td align="right">46.7%</td>
<td align="right">25.0%</td>
<td align="right">26.3%</td>
<td align="right">15.2%</td>
<td align="right">28.6%</td>
<td align="right">111</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟢 Street_Samurai</td>
<td align="left">Custom</td>
<td align="right"><b>1500</b></td>
<td align="right">26.0%</td>
<td align="right">75.0%</td>
<td align="right">29.4%</td>
<td align="right">38.1%</td>
<td align="right">25.9%</td>
<td align="right">12.0%</td>
<td align="right">123</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟢 Chronos</td>
<td align="left">Incursion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.8%</td>
<td align="right">57.1%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">14.3%</td>
<td align="right">10.0%</td>
<td align="right">31</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟢 Tick-Tock</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.8%</td>
<td align="right">33.3%</td>
<td align="right">38.1%</td>
<td align="right">19.2%</td>
<td align="right">26.7%</td>
<td align="right">20.0%</td>
<td align="right">124</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟢 Filch</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.7%</td>
<td align="right">68.8%</td>
<td align="right">30.8%</td>
<td align="right">17.6%</td>
<td align="right">12.5%</td>
<td align="right">13.6%</td>
<td align="right">113</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟢 Mite</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">38.5%</td>
<td align="right">40.0%</td>
<td align="right">19.4%</td>
<td align="right">22.2%</td>
<td align="right">21.2%</td>
<td align="right">110</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟢 Spiff</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">9.1%</td>
<td align="right">61.9%</td>
<td align="right">22.2%</td>
<td align="right">25.0%</td>
<td align="right">12.5%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟢 Shadow</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">56.2%</td>
<td align="right">40.0%</td>
<td align="right">21.4%</td>
<td align="right">21.4%</td>
<td align="right">14.0%</td>
<td align="right">130</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟢 Wrack</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">60.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">5</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟡 Reserve</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.2%</td>
<td align="right">50.0%</td>
<td align="right">37.5%</td>
<td align="right">19.0%</td>
<td align="right">19.2%</td>
<td align="right">22.2%</td>
<td align="right">107</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟡 Trader</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">55.6%</td>
<td align="right">40.0%</td>
<td align="right">19.0%</td>
<td align="right">16.7%</td>
<td align="right">21.2%</td>
<td align="right">108</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟡 Lunatic</td>
<td align="left">Conflict</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">20.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">91</td>
<td align="left">🟡 Nanny</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">33.3%</td>
<td align="right">12</td>
</tr>
<tr>
<td align="left">92</td>
<td align="left">🟡 Particle</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">93</td>
<td align="left">🟡 Whirligig</td>
<td align="left">Dominion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">50.0%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">94</td>
<td align="left">🟡 Grumpus_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">95</td>
<td align="left">🟡 Vector</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">96</td>
<td align="left">🟡 Reincarnator</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">53.8%</td>
<td align="right">55.6%</td>
<td align="right">20.0%</td>
<td align="right">9.7%</td>
<td align="right">14.3%</td>
<td align="right">124</td>
</tr>
<tr>
<td align="left">97</td>
<td align="left">🟡 Fixer</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">30.0%</td>
<td align="right">42.9%</td>
<td align="right">38.5%</td>
<td align="right">20.0%</td>
<td align="right">8.3%</td>
<td align="right">116</td>
</tr>
<tr>
<td align="left">98</td>
<td align="left">🟡 Black_Ice</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">54.5%</td>
<td align="right">35.7%</td>
<td align="right">36.7%</td>
<td align="right">12.9%</td>
<td align="right">3.8%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">99</td>
<td align="left">🟡 Butler</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">66.7%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">12.5%</td>
<td align="right">25</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">🟡 Netrunner</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">50.0%</td>
<td align="right">39.1%</td>
<td align="right">26.1%</td>
<td align="right">19.2%</td>
<td align="right">11.4%</td>
<td align="right">126</td>
</tr>
<tr>
<td align="left">101</td>
<td align="left">🟡 Saboteur</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">28.6%</td>
<td align="right">16.7%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">102</td>
<td align="left">🟡 Chromed</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">43.8%</td>
<td align="right">27.8%</td>
<td align="right">29.2%</td>
<td align="right">19.4%</td>
<td align="right">12.1%</td>
<td align="right">127</td>
</tr>
<tr>
<td align="left">103</td>
<td align="left">🟡 Brute_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">104</td>
<td align="left">🟡 Voyager</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">50.0%</td>
<td align="right">100.0%</td>
<td align="right">16.7%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">105</td>
<td align="left">🟡 Sting</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">106</td>
<td align="left">🟡 Relic</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">107</td>
<td align="left">🟡 Lizard</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">108</td>
<td align="left">🟡 Demon</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">23.1%</td>
<td align="right">45.5%</td>
<td align="right">40.0%</td>
<td align="right">16.7%</td>
<td align="right">21.9%</td>
<td align="right">11.1%</td>
<td align="right">117</td>
</tr>
<tr>
<td align="left">109</td>
<td align="left">🟡 Virus_Cyber</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">42.9%</td>
<td align="right">27.8%</td>
<td align="right">31.8%</td>
<td align="right">24.0%</td>
<td align="right">10.6%</td>
<td align="right">126</td>
</tr>
<tr>
<td align="left">110</td>
<td align="left">🟡 Sorcerer</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">7.1%</td>
<td align="right">31.8%</td>
<td align="right">14.3%</td>
<td align="right">33.3%</td>
<td align="right">22.9%</td>
<td align="right">113</td>
</tr>
<tr>
<td align="left">111</td>
<td align="left">🟡 Amoeba</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">55.6%</td>
<td align="right">15.8%</td>
<td align="right">36.4%</td>
<td align="right">9.1%</td>
<td align="right">23.1%</td>
<td align="right">122</td>
</tr>
<tr>
<td align="left">112</td>
<td align="left">🟡 Remora</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">22.8%</td>
<td align="right">28.6%</td>
<td align="right">31.6%</td>
<td align="right">17.9%</td>
<td align="right">13.3%</td>
<td align="right">30.0%</td>
<td align="right">114</td>
</tr>
<tr>
<td align="left">113</td>
<td align="left">🟡 Fido</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">64.7%</td>
<td align="right">21.1%</td>
<td align="right">20.0%</td>
<td align="right">12.0%</td>
<td align="right">14.6%</td>
<td align="right">132</td>
</tr>
<tr>
<td align="left">114</td>
<td align="left">🟡 Void</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">12.5%</td>
<td align="right">30.8%</td>
<td align="right">16.7%</td>
<td align="right">29.3%</td>
<td align="right">20.0%</td>
<td align="right">132</td>
</tr>
<tr>
<td align="left">115</td>
<td align="left">🟡 Plant</td>
<td align="left">Incursion</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">116</td>
<td align="left">🟡 Crusher</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">117</td>
<td align="left">🟡 Changeling</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">22.7%</td>
<td align="right">0.0%</td>
<td align="right">30.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">118</td>
<td align="left">🟡 Antimatter</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">22.5%</td>
<td align="right">71.4%</td>
<td align="right">26.1%</td>
<td align="right">14.8%</td>
<td align="right">19.0%</td>
<td align="right">8.6%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">119</td>
<td align="left">🟡 Hologram_Cyber</td>
<td align="left">Custom</td>
<td align="right"><b>1498</b></td>
<td align="right">22.1%</td>
<td align="right">57.1%</td>
<td align="right">40.0%</td>
<td align="right">25.0%</td>
<td align="right">15.2%</td>
<td align="right">14.0%</td>
<td align="right">122</td>
</tr>
<tr>
<td align="left">120</td>
<td align="left">🟡 Gorgon</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">22.2%</td>
<td align="right">40.0%</td>
<td align="right">42.9%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">27</td>
</tr>
<tr>
<td align="left">121</td>
<td align="left">🟡 Pickpocket</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
<td align="right">16.7%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">122</td>
<td align="left">🟡 Skeptic</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">22.2%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
<td align="right">7.7%</td>
<td align="right">27</td>
</tr>
<tr>
<td align="left">123</td>
<td align="left">🟡 Corpo</td>
<td align="left">Custom</td>
<td align="right"><b>1498</b></td>
<td align="right">21.8%</td>
<td align="right">28.6%</td>
<td align="right">26.7%</td>
<td align="right">13.3%</td>
<td align="right">11.1%</td>
<td align="right">29.7%</td>
<td align="right">101</td>
</tr>
<tr>
<td align="left">124</td>
<td align="left">🟡 Loser</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">21.6%</td>
<td align="right">50.0%</td>
<td align="right">25.0%</td>
<td align="right">27.3%</td>
<td align="right">12.9%</td>
<td align="right">11.4%</td>
<td align="right">116</td>
</tr>
<tr>
<td align="left">125</td>
<td align="left">🟡 Will</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">21.5%</td>
<td align="right">28.6%</td>
<td align="right">25.0%</td>
<td align="right">21.1%</td>
<td align="right">17.9%</td>
<td align="right">18.9%</td>
<td align="right">121</td>
</tr>
<tr>
<td align="left">126</td>
<td align="left">🟡 Vulch</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">21.4%</td>
<td align="right">62.5%</td>
<td align="right">37.5%</td>
<td align="right">17.2%</td>
<td align="right">12.5%</td>
<td align="right">14.8%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">127</td>
<td align="left">🟡 Zilch</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">128</td>
<td align="left">🟡 Alien</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">21.4%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">129</td>
<td align="left">🟡 Filth</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">21.4%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">130</td>
<td align="left">🟡 Mind</td>
<td align="left">Base</td>
<td align="right"><b>1497</b></td>
<td align="right">21.1%</td>
<td align="right">60.0%</td>
<td align="right">15.8%</td>
<td align="right">19.0%</td>
<td align="right">23.5%</td>
<td align="right">10.0%</td>
<td align="right">114</td>
</tr>
<tr>
<td align="left">131</td>
<td align="left">🟡 Muckraker</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">21.1%</td>
<td align="right">40.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">132</td>
<td align="left">🟡 Peddler</td>
<td align="left">Eons</td>
<td align="right"><b>1497</b></td>
<td align="right">21.1%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">19</td>
</tr>
<tr>
<td align="left">133</td>
<td align="left">🟡 Healer</td>
<td align="left">Base</td>
<td align="right"><b>1497</b></td>
<td align="right">20.8%</td>
<td align="right">50.0%</td>
<td align="right">19.0%</td>
<td align="right">23.1%</td>
<td align="right">14.8%</td>
<td align="right">17.1%</td>
<td align="right">106</td>
</tr>
<tr>
<td align="left">134</td>
<td align="left">🟡 Swindler</td>
<td align="left">Storm</td>
<td align="right"><b>1497</b></td>
<td align="right">20.8%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">135</td>
<td align="left">🟡 Cyborg</td>
<td align="left">Alliance</td>
<td align="right"><b>1497</b></td>
<td align="right">20.8%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">16.7%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">136</td>
<td align="left">🟡 Sadist</td>
<td align="left">Conflict</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">22.2%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">137</td>
<td align="left">🟡 Greenhorn</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">25.0%</td>
<td align="right">20.0%</td>
<td align="right">33.3%</td>
<td align="right">16.7%</td>
<td align="right">11.1%</td>
<td align="right">30</td>
</tr>
<tr>
<td align="left">138</td>
<td align="left">🟡 Joker</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">28.6%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">139</td>
<td align="left">🟡 Throwback</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">140</td>
<td align="left">🟡 Cosmos</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">44.4%</td>
<td align="right">0.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">141</td>
<td align="left">🟡 Gambler</td>
<td align="left">Base</td>
<td align="right"><b>1497</b></td>
<td align="right">19.6%</td>
<td align="right">70.0%</td>
<td align="right">26.3%</td>
<td align="right">20.0%</td>
<td align="right">8.7%</td>
<td align="right">8.6%</td>
<td align="right">112</td>
</tr>
<tr>
<td align="left">142</td>
<td align="left">🟡 Remote</td>
<td align="left">Alliance</td>
<td align="right"><b>1496</b></td>
<td align="right">19.0%</td>
<td align="right">66.7%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">11.1%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">143</td>
<td align="left">🟡 Void_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1496</b></td>
<td align="right">19.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">144</td>
<td align="left">🟡 Witch</td>
<td align="left">Odyssey</td>
<td align="right"><b>1496</b></td>
<td align="right">19.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">12.5%</td>
<td align="right">20.0%</td>
<td align="right">20.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">145</td>
<td align="left">🟡 Daredevil</td>
<td align="left">Dominion</td>
<td align="right"><b>1496</b></td>
<td align="right">18.8%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">20.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">146</td>
<td align="left">🟡 The Meek</td>
<td align="left">Odyssey</td>
<td align="right"><b>1496</b></td>
<td align="right">18.8%</td>
<td align="right">50.0%</td>
<td align="right">100.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">147</td>
<td align="left">🟡 Schizoid_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">18.2%</td>
<td align="right">60.0%</td>
<td align="right">0.0%</td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">148</td>
<td align="left">🟡 Geek</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">18.2%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">149</td>
<td align="left">🟡 Decker</td>
<td align="left">Custom</td>
<td align="right"><b>1495</b></td>
<td align="right">17.5%</td>
<td align="right">0.0%</td>
<td align="right">42.9%</td>
<td align="right">12.5%</td>
<td align="right">14.7%</td>
<td align="right">19.4%</td>
<td align="right">114</td>
</tr>
<tr>
<td align="left">150</td>
<td align="left">🟡 BleedingHeart</td>
<td align="left">Eons</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">151</td>
<td align="left">🟡 Phantasm</td>
<td align="left">Storm</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">152</td>
<td align="left">🟡 Winner</td>
<td align="left">Alliance</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">153</td>
<td align="left">🟡 Micron</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">154</td>
<td align="left">🟡 Squee</td>
<td align="left">Storm</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">155</td>
<td align="left">🟡 Lloyd</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">156</td>
<td align="left">🟡 Graviton</td>
<td align="left">Conflict</td>
<td align="right"><b>1495</b></td>
<td align="right">17.6%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">157</td>
<td align="left">🟡 Calculator</td>
<td align="left">Base</td>
<td align="right"><b>1495</b></td>
<td align="right">17.1%</td>
<td align="right">36.4%</td>
<td align="right">33.3%</td>
<td align="right">22.7%</td>
<td align="right">5.3%</td>
<td align="right">5.7%</td>
<td align="right">105</td>
</tr>
<tr>
<td align="left">158</td>
<td align="left">🟡 Sadist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">17.4%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">23</td>
</tr>
<tr>
<td align="left">159</td>
<td align="left">🟡 Booster</td>
<td align="left">Custom</td>
<td align="right"><b>1495</b></td>
<td align="right">16.9%</td>
<td align="right">33.3%</td>
<td align="right">10.0%</td>
<td align="right">30.4%</td>
<td align="right">14.8%</td>
<td align="right">10.3%</td>
<td align="right">118</td>
</tr>
<tr>
<td align="left">160</td>
<td align="left">🟡 Clone</td>
<td align="left">Base</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">62.5%</td>
<td align="right">11.1%</td>
<td align="right">17.9%</td>
<td align="right">20.8%</td>
<td align="right">7.1%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">161</td>
<td align="left">🟡 Grudge</td>
<td align="left">Base</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">11.1%</td>
<td align="right">17.4%</td>
<td align="right">13.6%</td>
<td align="right">14.3%</td>
<td align="right">21.1%</td>
<td align="right">120</td>
</tr>
<tr>
<td align="left">162</td>
<td align="left">🟡 Mirror</td>
<td align="left">Base</td>
<td align="right"><b>1495</b></td>
<td align="right">16.5%</td>
<td align="right">27.3%</td>
<td align="right">13.3%</td>
<td align="right">11.8%</td>
<td align="right">18.8%</td>
<td align="right">14.3%</td>
<td align="right">103</td>
</tr>
<tr>
<td align="left">163</td>
<td align="left">🟡 Reflex_Booster</td>
<td align="left">Custom</td>
<td align="right"><b>1495</b></td>
<td align="right">16.4%</td>
<td align="right">37.5%</td>
<td align="right">18.2%</td>
<td align="right">25.9%</td>
<td align="right">6.9%</td>
<td align="right">11.9%</td>
<td align="right">128</td>
</tr>
<tr>
<td align="left">164</td>
<td align="left">🟡 Mesmer</td>
<td align="left">Dominion</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">12</td>
</tr>
<tr>
<td align="left">165</td>
<td align="left">🟡 Demon_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">166</td>
<td align="left">🟡 Masochist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">167</td>
<td align="left">🟡 Lightning</td>
<td align="left">Alliance</td>
<td align="right"><b>1495</b></td>
<td align="right">16.7%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">50.0%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">168</td>
<td align="left">🟡 Bandit</td>
<td align="left">Alliance</td>
<td align="right"><b>1494</b></td>
<td align="right">15.4%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">16.7%</td>
<td align="right">11.1%</td>
<td align="right">14.3%</td>
<td align="right">26</td>
</tr>
<tr>
<td align="left">169</td>
<td align="left">🟡 Alchemist</td>
<td align="left">Dominion</td>
<td align="right"><b>1494</b></td>
<td align="right">15.4%</td>
<td align="right">50.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">13</td>
</tr>
<tr>
<td align="left">170</td>
<td align="left">🟡 Explorer</td>
<td align="left">Dominion</td>
<td align="right"><b>1494</b></td>
<td align="right">15.4%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">26</td>
</tr>
<tr>
<td align="left">171</td>
<td align="left">🟡 Worm</td>
<td align="left">Storm</td>
<td align="right"><b>1493</b></td>
<td align="right">14.8%</td>
<td align="right">40.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
<td align="right">27</td>
</tr>
<tr>
<td align="left">172</td>
<td align="left">🟡 Surgeon</td>
<td align="left">Eons</td>
<td align="right"><b>1493</b></td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">33.3%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">173</td>
<td align="left">🟡 Oligarch</td>
<td align="left">Eons</td>
<td align="right"><b>1493</b></td>
<td align="right">14.3%</td>
<td align="right">50.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">14</td>
</tr>
<tr>
<td align="left">174</td>
<td align="left">🟡 Leviathan</td>
<td align="left">Incursion</td>
<td align="right"><b>1493</b></td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">175</td>
<td align="left">🟡 Mirage</td>
<td align="left">Dominion</td>
<td align="right"><b>1493</b></td>
<td align="right">14.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">28.6%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">176</td>
<td align="left">🟡 Merchant</td>
<td align="left">Incursion</td>
<td align="right"><b>1493</b></td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">7.1%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">177</td>
<td align="left">🟡 Animal</td>
<td align="left">Alliance</td>
<td align="right"><b>1493</b></td>
<td align="right">13.6%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">50.0%</td>
<td align="right">12.5%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">178</td>
<td align="left">🟡 Philanthropist</td>
<td align="left">Base</td>
<td align="right"><b>1492</b></td>
<td align="right">12.6%</td>
<td align="right">30.0%</td>
<td align="right">18.8%</td>
<td align="right">6.7%</td>
<td align="right">7.7%</td>
<td align="right">13.8%</td>
<td align="right">111</td>
</tr>
<tr>
<td align="left">179</td>
<td align="left">🟡 Gremlin</td>
<td align="left">Odyssey</td>
<td align="right"><b>1492</b></td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">180</td>
<td align="left">🟡 AI</td>
<td align="left">Eons</td>
<td align="right"><b>1492</b></td>
<td align="right">12.5%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">181</td>
<td align="left">🟡 Arcade</td>
<td align="left">Storm</td>
<td align="right"><b>1492</b></td>
<td align="right">12.5%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">12.5%</td>
<td align="right">20.0%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">182</td>
<td align="left">🟡 Anarchist</td>
<td align="left">Eons</td>
<td align="right"><b>1492</b></td>
<td align="right">12.5%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">16.7%</td>
<td align="right">0.0%</td>
<td align="right">24</td>
</tr>
<tr>
<td align="left">183</td>
<td align="left">🟡 Mouth</td>
<td align="left">Storm</td>
<td align="right"><b>1492</b></td>
<td align="right">12.5%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">184</td>
<td align="left">🟡 EvilTwin</td>
<td align="left">Eons</td>
<td align="right"><b>1491</b></td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">185</td>
<td align="left">🟡 Tortoise</td>
<td align="left">Eons</td>
<td align="right"><b>1491</b></td>
<td align="right">11.8%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">40.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">186</td>
<td align="left">🟡 Locust_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1491</b></td>
<td align="right">11.1%</td>
<td align="right">0.0%</td>
<td align="right">100.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">187</td>
<td align="left">🟡 Mercenary</td>
<td align="left">Incursion</td>
<td align="right"><b>1490</b></td>
<td align="right">10.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">188</td>
<td align="left">🟡 Sapient</td>
<td align="left">Alliance</td>
<td align="right"><b>1490</b></td>
<td align="right">10.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">20</td>
</tr>
<tr>
<td align="left">189</td>
<td align="left">🟡 Pretender</td>
<td align="left">Eons</td>
<td align="right"><b>1490</b></td>
<td align="right">9.5%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">14.3%</td>
<td align="right">21</td>
</tr>
<tr>
<td align="left">190</td>
<td align="left">🟡 Locust</td>
<td align="left">Incursion</td>
<td align="right"><b>1490</b></td>
<td align="right">9.1%</td>
<td align="right">0.0%</td>
<td align="right">50.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">22</td>
</tr>
<tr>
<td align="left">191</td>
<td align="left">🟡 Outlaw</td>
<td align="left">Storm</td>
<td align="right"><b>1489</b></td>
<td align="right">8.3%</td>
<td align="right">0.0%</td>
<td align="right">25.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">12</td>
</tr>
<tr>
<td align="left">192</td>
<td align="left">🟡 Magnet</td>
<td align="left">Odyssey</td>
<td align="right"><b>1488</b></td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">193</td>
<td align="left">🟡 Claw</td>
<td align="left">Conflict</td>
<td align="right"><b>1488</b></td>
<td align="right">6.2%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">16</td>
</tr>
<tr>
<td align="left">194</td>
<td align="left">🟡 Sniveler</td>
<td align="left">Incursion</td>
<td align="right"><b>1488</b></td>
<td align="right">5.9%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">33.3%</td>
<td align="right">17</td>
</tr>
<tr>
<td align="left">195</td>
<td align="left">🟡 Sloth</td>
<td align="left">Storm</td>
<td align="right"><b>1488</b></td>
<td align="right">5.6%</td>
<td align="right">20.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">18</td>
</tr>
<tr>
<td align="left">196</td>
<td align="left">🟡 Hurtz</td>
<td align="left">Odyssey</td>
<td align="right"><b>1486</b></td>
<td align="right">3.8%</td>
<td align="right">33.3%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">26</td>
</tr>
<tr>
<td align="left">197</td>
<td align="left">🟡 Tentacle</td>
<td align="left">Odyssey</td>
<td align="right"><b>1484</b></td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">0.0%</td>
<td align="right">18</td>
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

# Sort by source/expansion
python update_stats.py --sort source --order asc
```

</details>

