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

> **299,997** games simulated | Last updated: 2026-01-05 20:30
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
<td align="right"><b>1512</b></td>
<td align="right">53.0%</td>
<td align="right">70.3%</td>
<td align="right">62.8%</td>
<td align="right">58.5%</td>
<td align="right">49.4%</td>
<td align="right">41.4%</td>
<td align="right">15080</td>
</tr>
<tr>
<td align="left">2</td>
<td align="left">🟢 Parasite</td>
<td align="left">Base</td>
<td align="right"><b>1512</b></td>
<td align="right">53.7%</td>
<td align="right">45.7%</td>
<td align="right">45.2%</td>
<td align="right">51.3%</td>
<td align="right">56.9%</td>
<td align="right">59.7%</td>
<td align="right">14566</td>
</tr>
<tr>
<td align="left">3</td>
<td align="left">🟢 Tripler</td>
<td align="left">Base</td>
<td align="right"><b>1507</b></td>
<td align="right">41.9%</td>
<td align="right">80.8%</td>
<td align="right">61.6%</td>
<td align="right">43.3%</td>
<td align="right">32.5%</td>
<td align="right">25.7%</td>
<td align="right">15141</td>
</tr>
<tr>
<td align="left">4</td>
<td align="left">🟢 Pacifist</td>
<td align="left">Base</td>
<td align="right"><b>1504</b></td>
<td align="right">34.5%</td>
<td align="right">75.6%</td>
<td align="right">52.1%</td>
<td align="right">36.4%</td>
<td align="right">25.5%</td>
<td align="right">18.2%</td>
<td align="right">15001</td>
</tr>
<tr>
<td align="left">5</td>
<td align="left">🟢 Virus</td>
<td align="left">Base</td>
<td align="right"><b>1504</b></td>
<td align="right">33.7%</td>
<td align="right">68.3%</td>
<td align="right">44.7%</td>
<td align="right">32.1%</td>
<td align="right">26.0%</td>
<td align="right">24.2%</td>
<td align="right">15006</td>
</tr>
<tr>
<td align="left">6</td>
<td align="left">🟢 Macron</td>
<td align="left">Base</td>
<td align="right"><b>1503</b></td>
<td align="right">33.1%</td>
<td align="right">70.6%</td>
<td align="right">47.1%</td>
<td align="right">32.8%</td>
<td align="right">24.7%</td>
<td align="right">21.2%</td>
<td align="right">15163</td>
</tr>
<tr>
<td align="left">7</td>
<td align="left">🟢 Fury</td>
<td align="left">Incursion</td>
<td align="right"><b>1503</b></td>
<td align="right">27.6%</td>
<td align="right">52.1%</td>
<td align="right">40.5%</td>
<td align="right">28.4%</td>
<td align="right">21.0%</td>
<td align="right">17.4%</td>
<td align="right">2465</td>
</tr>
<tr>
<td align="left">8</td>
<td align="left">🟢 Visionary</td>
<td align="left">Conflict</td>
<td align="right"><b>1502</b></td>
<td align="right">26.2%</td>
<td align="right">42.7%</td>
<td align="right">34.9%</td>
<td align="right">24.3%</td>
<td align="right">23.5%</td>
<td align="right">19.5%</td>
<td align="right">2477</td>
</tr>
<tr>
<td align="left">9</td>
<td align="left">🟢 Masochist</td>
<td align="left">Base</td>
<td align="right"><b>1502</b></td>
<td align="right">29.7%</td>
<td align="right">67.7%</td>
<td align="right">40.4%</td>
<td align="right">29.7%</td>
<td align="right">22.3%</td>
<td align="right">17.7%</td>
<td align="right">14977</td>
</tr>
<tr>
<td align="left">10</td>
<td align="left">🟢 Schizoid_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">26.9%</td>
<td align="right">50.9%</td>
<td align="right">36.5%</td>
<td align="right">24.9%</td>
<td align="right">23.2%</td>
<td align="right">18.2%</td>
<td align="right">2128</td>
</tr>
<tr>
<td align="left">11</td>
<td align="left">🟢 Perfectionist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">25.8%</td>
<td align="right">49.5%</td>
<td align="right">32.7%</td>
<td align="right">24.1%</td>
<td align="right">22.6%</td>
<td align="right">18.4%</td>
<td align="right">2149</td>
</tr>
<tr>
<td align="left">12</td>
<td align="left">🟢 Neighbor</td>
<td align="left">Storm</td>
<td align="right"><b>1501</b></td>
<td align="right">26.1%</td>
<td align="right">50.2%</td>
<td align="right">37.6%</td>
<td align="right">26.1%</td>
<td align="right">20.6%</td>
<td align="right">17.4%</td>
<td align="right">2416</td>
</tr>
<tr>
<td align="left">13</td>
<td align="left">🟢 Human</td>
<td align="left">Base</td>
<td align="right"><b>1501</b></td>
<td align="right">29.0%</td>
<td align="right">60.4%</td>
<td align="right">39.6%</td>
<td align="right">28.0%</td>
<td align="right">22.8%</td>
<td align="right">18.9%</td>
<td align="right">15022</td>
</tr>
<tr>
<td align="left">14</td>
<td align="left">🟢 Patriot</td>
<td align="left">Storm</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">54.2%</td>
<td align="right">36.3%</td>
<td align="right">24.4%</td>
<td align="right">21.3%</td>
<td align="right">15.6%</td>
<td align="right">2444</td>
</tr>
<tr>
<td align="left">15</td>
<td align="left">🟢 Plant</td>
<td align="left">Incursion</td>
<td align="right"><b>1501</b></td>
<td align="right">25.1%</td>
<td align="right">51.5%</td>
<td align="right">35.9%</td>
<td align="right">25.1%</td>
<td align="right">19.9%</td>
<td align="right">14.3%</td>
<td align="right">2535</td>
</tr>
<tr>
<td align="left">16</td>
<td align="left">🟢 Pentaform</td>
<td align="left">Dominion</td>
<td align="right"><b>1501</b></td>
<td align="right">26.1%</td>
<td align="right">50.2%</td>
<td align="right">38.6%</td>
<td align="right">23.8%</td>
<td align="right">19.4%</td>
<td align="right">18.7%</td>
<td align="right">2299</td>
</tr>
<tr>
<td align="left">17</td>
<td align="left">🟢 Usurper</td>
<td align="left">Dominion</td>
<td align="right"><b>1501</b></td>
<td align="right">27.1%</td>
<td align="right">54.5%</td>
<td align="right">36.4%</td>
<td align="right">27.3%</td>
<td align="right">21.4%</td>
<td align="right">18.0%</td>
<td align="right">2278</td>
</tr>
<tr>
<td align="left">18</td>
<td align="left">🟢 Demon_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">49.8%</td>
<td align="right">34.4%</td>
<td align="right">25.0%</td>
<td align="right">18.2%</td>
<td align="right">18.1%</td>
<td align="right">2086</td>
</tr>
<tr>
<td align="left">19</td>
<td align="left">🟢 Symbiote</td>
<td align="left">Incursion</td>
<td align="right"><b>1501</b></td>
<td align="right">27.2%</td>
<td align="right">62.4%</td>
<td align="right">34.7%</td>
<td align="right">25.5%</td>
<td align="right">20.5%</td>
<td align="right">17.9%</td>
<td align="right">2383</td>
</tr>
<tr>
<td align="left">20</td>
<td align="left">🟢 Pretender</td>
<td align="left">Eons</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">52.9%</td>
<td align="right">32.8%</td>
<td align="right">26.3%</td>
<td align="right">22.9%</td>
<td align="right">14.8%</td>
<td align="right">2404</td>
</tr>
<tr>
<td align="left">21</td>
<td align="left">🟢 TheCult</td>
<td align="left">Eons</td>
<td align="right"><b>1501</b></td>
<td align="right">25.7%</td>
<td align="right">48.9%</td>
<td align="right">35.9%</td>
<td align="right">28.1%</td>
<td align="right">19.8%</td>
<td align="right">16.0%</td>
<td align="right">2305</td>
</tr>
<tr>
<td align="left">22</td>
<td align="left">🟢 Warrior</td>
<td align="left">Base</td>
<td align="right"><b>1501</b></td>
<td align="right">27.1%</td>
<td align="right">54.9%</td>
<td align="right">38.6%</td>
<td align="right">26.6%</td>
<td align="right">21.6%</td>
<td align="right">17.3%</td>
<td align="right">14852</td>
</tr>
<tr>
<td align="left">23</td>
<td align="left">🟢 Scavenger</td>
<td align="left">Storm</td>
<td align="right"><b>1501</b></td>
<td align="right">25.0%</td>
<td align="right">47.7%</td>
<td align="right">35.6%</td>
<td align="right">24.5%</td>
<td align="right">20.5%</td>
<td align="right">17.0%</td>
<td align="right">2416</td>
</tr>
<tr>
<td align="left">24</td>
<td align="left">🟢 Masochist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">25.5%</td>
<td align="right">53.5%</td>
<td align="right">32.8%</td>
<td align="right">24.1%</td>
<td align="right">20.2%</td>
<td align="right">17.3%</td>
<td align="right">2101</td>
</tr>
<tr>
<td align="left">25</td>
<td align="left">🟢 Force</td>
<td align="left">Odyssey</td>
<td align="right"><b>1501</b></td>
<td align="right">26.6%</td>
<td align="right">54.3%</td>
<td align="right">37.0%</td>
<td align="right">23.8%</td>
<td align="right">23.2%</td>
<td align="right">17.0%</td>
<td align="right">2142</td>
</tr>
<tr>
<td align="left">26</td>
<td align="left">🟢 Lightning</td>
<td align="left">Alliance</td>
<td align="right"><b>1501</b></td>
<td align="right">25.2%</td>
<td align="right">48.7%</td>
<td align="right">31.8%</td>
<td align="right">25.1%</td>
<td align="right">21.4%</td>
<td align="right">16.2%</td>
<td align="right">2498</td>
</tr>
<tr>
<td align="left">27</td>
<td align="left">🟢 Mouth</td>
<td align="left">Storm</td>
<td align="right"><b>1501</b></td>
<td align="right">24.9%</td>
<td align="right">49.6%</td>
<td align="right">29.9%</td>
<td align="right">27.7%</td>
<td align="right">19.5%</td>
<td align="right">16.2%</td>
<td align="right">2372</td>
</tr>
<tr>
<td align="left">28</td>
<td align="left">🟢 Diplomat</td>
<td align="left">Dominion</td>
<td align="right"><b>1501</b></td>
<td align="right">25.6%</td>
<td align="right">47.7%</td>
<td align="right">33.4%</td>
<td align="right">27.3%</td>
<td align="right">20.2%</td>
<td align="right">17.5%</td>
<td align="right">2227</td>
</tr>
<tr>
<td align="left">29</td>
<td align="left">🟢 Voyager</td>
<td align="left">Dominion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.2%</td>
<td align="right">51.9%</td>
<td align="right">29.0%</td>
<td align="right">25.8%</td>
<td align="right">20.6%</td>
<td align="right">16.3%</td>
<td align="right">2352</td>
</tr>
<tr>
<td align="left">30</td>
<td align="left">🟢 Zilch</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.6%</td>
<td align="right">53.8%</td>
<td align="right">33.0%</td>
<td align="right">26.7%</td>
<td align="right">19.6%</td>
<td align="right">15.9%</td>
<td align="right">2004</td>
</tr>
<tr>
<td align="left">31</td>
<td align="left">🟢 Bulwark</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">26.4%</td>
<td align="right">52.9%</td>
<td align="right">34.8%</td>
<td align="right">27.1%</td>
<td align="right">21.3%</td>
<td align="right">18.1%</td>
<td align="right">2375</td>
</tr>
<tr>
<td align="left">32</td>
<td align="left">🟢 Wrack</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">26.1%</td>
<td align="right">49.4%</td>
<td align="right">33.9%</td>
<td align="right">23.1%</td>
<td align="right">18.5%</td>
<td align="right">21.1%</td>
<td align="right">2180</td>
</tr>
<tr>
<td align="left">33</td>
<td align="left">🟢 Nightmare</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">25.6%</td>
<td align="right">52.8%</td>
<td align="right">40.0%</td>
<td align="right">23.3%</td>
<td align="right">21.7%</td>
<td align="right">16.0%</td>
<td align="right">2378</td>
</tr>
<tr>
<td align="left">34</td>
<td align="left">🟢 Micron</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">48.1%</td>
<td align="right">33.0%</td>
<td align="right">25.2%</td>
<td align="right">20.4%</td>
<td align="right">16.8%</td>
<td align="right">2162</td>
</tr>
<tr>
<td align="left">35</td>
<td align="left">🟢 Guardian</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">26.9%</td>
<td align="right">44.6%</td>
<td align="right">38.8%</td>
<td align="right">33.0%</td>
<td align="right">19.3%</td>
<td align="right">17.2%</td>
<td align="right">2185</td>
</tr>
<tr>
<td align="left">36</td>
<td align="left">🟢 Vox</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">26.0%</td>
<td align="right">50.6%</td>
<td align="right">36.2%</td>
<td align="right">23.9%</td>
<td align="right">21.7%</td>
<td align="right">17.7%</td>
<td align="right">2367</td>
</tr>
<tr>
<td align="left">37</td>
<td align="left">🟢 Horde</td>
<td align="left">Alliance</td>
<td align="right"><b>1500</b></td>
<td align="right">25.8%</td>
<td align="right">53.6%</td>
<td align="right">33.2%</td>
<td align="right">27.6%</td>
<td align="right">19.9%</td>
<td align="right">16.3%</td>
<td align="right">2489</td>
</tr>
<tr>
<td align="left">38</td>
<td align="left">🟢 Loser</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.9%</td>
<td align="right">50.1%</td>
<td align="right">35.8%</td>
<td align="right">29.3%</td>
<td align="right">21.2%</td>
<td align="right">14.8%</td>
<td align="right">15267</td>
</tr>
<tr>
<td align="left">39</td>
<td align="left">🟢 FireDancer</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">24.2%</td>
<td align="right">48.6%</td>
<td align="right">31.7%</td>
<td align="right">24.5%</td>
<td align="right">17.3%</td>
<td align="right">17.2%</td>
<td align="right">2350</td>
</tr>
<tr>
<td align="left">40</td>
<td align="left">🟢 Sadist</td>
<td align="left">Conflict</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">49.4%</td>
<td align="right">35.7%</td>
<td align="right">24.0%</td>
<td align="right">21.8%</td>
<td align="right">16.8%</td>
<td align="right">2504</td>
</tr>
<tr>
<td align="left">41</td>
<td align="left">🟢 Coordinator</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">25.7%</td>
<td align="right">44.8%</td>
<td align="right">34.9%</td>
<td align="right">26.0%</td>
<td align="right">22.7%</td>
<td align="right">16.5%</td>
<td align="right">2423</td>
</tr>
<tr>
<td align="left">42</td>
<td align="left">🟢 Mesmer</td>
<td align="left">Dominion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">50.0%</td>
<td align="right">36.9%</td>
<td align="right">24.7%</td>
<td align="right">20.8%</td>
<td align="right">16.3%</td>
<td align="right">2280</td>
</tr>
<tr>
<td align="left">43</td>
<td align="left">🟢 Oligarch</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">24.9%</td>
<td align="right">49.4%</td>
<td align="right">32.8%</td>
<td align="right">23.2%</td>
<td align="right">20.2%</td>
<td align="right">17.0%</td>
<td align="right">2335</td>
</tr>
<tr>
<td align="left">44</td>
<td align="left">🟢 Brute_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.2%</td>
<td align="right">50.5%</td>
<td align="right">37.2%</td>
<td align="right">26.1%</td>
<td align="right">18.8%</td>
<td align="right">15.9%</td>
<td align="right">2127</td>
</tr>
<tr>
<td align="left">45</td>
<td align="left">🟡 Grumpus</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">26.0%</td>
<td align="right">51.3%</td>
<td align="right">36.8%</td>
<td align="right">24.4%</td>
<td align="right">20.7%</td>
<td align="right">18.6%</td>
<td align="right">2438</td>
</tr>
<tr>
<td align="left">46</td>
<td align="left">🟡 Tyrant</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">24.9%</td>
<td align="right">45.2%</td>
<td align="right">35.3%</td>
<td align="right">24.0%</td>
<td align="right">20.6%</td>
<td align="right">17.5%</td>
<td align="right">2352</td>
</tr>
<tr>
<td align="left">47</td>
<td align="left">🟡 Poison</td>
<td align="left">Alliance</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">49.6%</td>
<td align="right">36.6%</td>
<td align="right">21.3%</td>
<td align="right">21.0%</td>
<td align="right">17.3%</td>
<td align="right">2580</td>
</tr>
<tr>
<td align="left">48</td>
<td align="left">🟡 Arcade</td>
<td align="left">Storm</td>
<td align="right"><b>1500</b></td>
<td align="right">25.7%</td>
<td align="right">54.6%</td>
<td align="right">34.2%</td>
<td align="right">24.2%</td>
<td align="right">18.8%</td>
<td align="right">18.6%</td>
<td align="right">2400</td>
</tr>
<tr>
<td align="left">49</td>
<td align="left">🟡 Antimatter</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.9%</td>
<td align="right">51.3%</td>
<td align="right">35.9%</td>
<td align="right">29.1%</td>
<td align="right">21.3%</td>
<td align="right">14.6%</td>
<td align="right">14685</td>
</tr>
<tr>
<td align="left">50</td>
<td align="left">🟡 BleedingHeart</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">24.6%</td>
<td align="right">54.0%</td>
<td align="right">31.5%</td>
<td align="right">27.3%</td>
<td align="right">17.4%</td>
<td align="right">15.8%</td>
<td align="right">2314</td>
</tr>
<tr>
<td align="left">51</td>
<td align="left">🟡 Citadel</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">51.1%</td>
<td align="right">33.5%</td>
<td align="right">25.0%</td>
<td align="right">20.5%</td>
<td align="right">17.5%</td>
<td align="right">14967</td>
</tr>
<tr>
<td align="left">52</td>
<td align="left">🟡 Vector</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">51.8%</td>
<td align="right">31.6%</td>
<td align="right">26.8%</td>
<td align="right">17.3%</td>
<td align="right">19.0%</td>
<td align="right">2166</td>
</tr>
<tr>
<td align="left">53</td>
<td align="left">🟡 Bandit</td>
<td align="left">Alliance</td>
<td align="right"><b>1500</b></td>
<td align="right">25.8%</td>
<td align="right">53.8%</td>
<td align="right">35.0%</td>
<td align="right">26.0%</td>
<td align="right">22.5%</td>
<td align="right">14.5%</td>
<td align="right">2523</td>
</tr>
<tr>
<td align="left">54</td>
<td align="left">🟡 Chrysalis</td>
<td align="left">Alliance</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">50.6%</td>
<td align="right">31.6%</td>
<td align="right">22.8%</td>
<td align="right">22.2%</td>
<td align="right">17.9%</td>
<td align="right">2592</td>
</tr>
<tr>
<td align="left">55</td>
<td align="left">🟡 Laser</td>
<td align="left">Dominion</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">53.4%</td>
<td align="right">33.2%</td>
<td align="right">24.6%</td>
<td align="right">20.6%</td>
<td align="right">18.0%</td>
<td align="right">2296</td>
</tr>
<tr>
<td align="left">56</td>
<td align="left">🟡 Graviton</td>
<td align="left">Conflict</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">48.9%</td>
<td align="right">34.1%</td>
<td align="right">21.2%</td>
<td align="right">23.2%</td>
<td align="right">18.5%</td>
<td align="right">2434</td>
</tr>
<tr>
<td align="left">57</td>
<td align="left">🟡 Hate</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.4%</td>
<td align="right">58.1%</td>
<td align="right">34.8%</td>
<td align="right">24.7%</td>
<td align="right">19.4%</td>
<td align="right">15.3%</td>
<td align="right">14816</td>
</tr>
<tr>
<td align="left">58</td>
<td align="left">🟡 Empath</td>
<td align="left">Conflict</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">52.6%</td>
<td align="right">31.9%</td>
<td align="right">25.2%</td>
<td align="right">17.6%</td>
<td align="right">19.6%</td>
<td align="right">2567</td>
</tr>
<tr>
<td align="left">59</td>
<td align="left">🟡 Silencer</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">50.2%</td>
<td align="right">33.7%</td>
<td align="right">25.3%</td>
<td align="right">20.2%</td>
<td align="right">15.3%</td>
<td align="right">2129</td>
</tr>
<tr>
<td align="left">60</td>
<td align="left">🟡 Warpish</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.1%</td>
<td align="right">47.7%</td>
<td align="right">34.0%</td>
<td align="right">25.1%</td>
<td align="right">19.7%</td>
<td align="right">17.3%</td>
<td align="right">14885</td>
</tr>
<tr>
<td align="left">61</td>
<td align="left">🟡 Particle</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">42.7%</td>
<td align="right">30.7%</td>
<td align="right">25.8%</td>
<td align="right">21.6%</td>
<td align="right">17.1%</td>
<td align="right">2302</td>
</tr>
<tr>
<td align="left">62</td>
<td align="left">🟡 Hypochondriac</td>
<td align="left">Eons</td>
<td align="right"><b>1500</b></td>
<td align="right">24.9%</td>
<td align="right">47.1%</td>
<td align="right">36.2%</td>
<td align="right">22.9%</td>
<td align="right">18.9%</td>
<td align="right">18.4%</td>
<td align="right">2278</td>
</tr>
<tr>
<td align="left">63</td>
<td align="left">🟡 Grudge</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.3%</td>
<td align="right">55.4%</td>
<td align="right">35.9%</td>
<td align="right">23.5%</td>
<td align="right">18.9%</td>
<td align="right">16.4%</td>
<td align="right">14949</td>
</tr>
<tr>
<td align="left">64</td>
<td align="left">🟡 Assessor</td>
<td align="left">Odyssey</td>
<td align="right"><b>1500</b></td>
<td align="right">25.5%</td>
<td align="right">44.9%</td>
<td align="right">38.1%</td>
<td align="right">26.0%</td>
<td align="right">18.7%</td>
<td align="right">17.8%</td>
<td align="right">2093</td>
</tr>
<tr>
<td align="left">65</td>
<td align="left">🟡 Healer</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">48.5%</td>
<td align="right">32.8%</td>
<td align="right">24.2%</td>
<td align="right">21.7%</td>
<td align="right">16.4%</td>
<td align="right">15054</td>
</tr>
<tr>
<td align="left">66</td>
<td align="left">🟡 Miser</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">49.1%</td>
<td align="right">32.2%</td>
<td align="right">24.3%</td>
<td align="right">19.6%</td>
<td align="right">16.3%</td>
<td align="right">14920</td>
</tr>
<tr>
<td align="left">67</td>
<td align="left">🟡 Industrialist</td>
<td align="left">Conflict</td>
<td align="right"><b>1500</b></td>
<td align="right">24.4%</td>
<td align="right">48.3%</td>
<td align="right">31.5%</td>
<td align="right">25.4%</td>
<td align="right">18.4%</td>
<td align="right">18.0%</td>
<td align="right">2460</td>
</tr>
<tr>
<td align="left">68</td>
<td align="left">🟡 Void</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">24.9%</td>
<td align="right">52.1%</td>
<td align="right">33.8%</td>
<td align="right">24.8%</td>
<td align="right">19.2%</td>
<td align="right">16.0%</td>
<td align="right">15035</td>
</tr>
<tr>
<td align="left">69</td>
<td align="left">🟡 Remote</td>
<td align="left">Alliance</td>
<td align="right"><b>1500</b></td>
<td align="right">25.0%</td>
<td align="right">50.4%</td>
<td align="right">32.9%</td>
<td align="right">24.0%</td>
<td align="right">21.7%</td>
<td align="right">16.3%</td>
<td align="right">2499</td>
</tr>
<tr>
<td align="left">70</td>
<td align="left">🟡 Zombie</td>
<td align="left">Base</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">50.9%</td>
<td align="right">34.5%</td>
<td align="right">24.3%</td>
<td align="right">19.1%</td>
<td align="right">16.2%</td>
<td align="right">14926</td>
</tr>
<tr>
<td align="left">71</td>
<td align="left">🟡 Cryo</td>
<td align="left">Incursion</td>
<td align="right"><b>1500</b></td>
<td align="right">24.7%</td>
<td align="right">47.3%</td>
<td align="right">34.1%</td>
<td align="right">22.8%</td>
<td align="right">21.3%</td>
<td align="right">16.5%</td>
<td align="right">2409</td>
</tr>
<tr>
<td align="left">72</td>
<td align="left">🟡 Mind</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">48.3%</td>
<td align="right">32.1%</td>
<td align="right">24.8%</td>
<td align="right">18.6%</td>
<td align="right">17.6%</td>
<td align="right">14677</td>
</tr>
<tr>
<td align="left">73</td>
<td align="left">🟡 Siren</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">55.2%</td>
<td align="right">27.7%</td>
<td align="right">23.0%</td>
<td align="right">20.4%</td>
<td align="right">15.9%</td>
<td align="right">2482</td>
</tr>
<tr>
<td align="left">74</td>
<td align="left">🟡 Shadow</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.6%</td>
<td align="right">48.6%</td>
<td align="right">31.8%</td>
<td align="right">24.7%</td>
<td align="right">20.4%</td>
<td align="right">16.2%</td>
<td align="right">14961</td>
</tr>
<tr>
<td align="left">75</td>
<td align="left">🟡 Inferno</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">50.2%</td>
<td align="right">32.0%</td>
<td align="right">26.0%</td>
<td align="right">17.2%</td>
<td align="right">17.4%</td>
<td align="right">2128</td>
</tr>
<tr>
<td align="left">76</td>
<td align="left">🟡 Skeptic</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">25.7%</td>
<td align="right">53.4%</td>
<td align="right">35.7%</td>
<td align="right">25.0%</td>
<td align="right">20.7%</td>
<td align="right">15.8%</td>
<td align="right">2502</td>
</tr>
<tr>
<td align="left">77</td>
<td align="left">🟡 Cosmos</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.6%</td>
<td align="right">52.7%</td>
<td align="right">31.7%</td>
<td align="right">25.5%</td>
<td align="right">19.7%</td>
<td align="right">17.7%</td>
<td align="right">2104</td>
</tr>
<tr>
<td align="left">78</td>
<td align="left">🟡 Claw</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">53.5%</td>
<td align="right">33.1%</td>
<td align="right">25.3%</td>
<td align="right">19.3%</td>
<td align="right">15.3%</td>
<td align="right">2568</td>
</tr>
<tr>
<td align="left">79</td>
<td align="left">🟡 Mutant</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.6%</td>
<td align="right">48.8%</td>
<td align="right">32.2%</td>
<td align="right">24.5%</td>
<td align="right">20.8%</td>
<td align="right">15.8%</td>
<td align="right">15048</td>
</tr>
<tr>
<td align="left">80</td>
<td align="left">🟡 Observer</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">48.7%</td>
<td align="right">33.1%</td>
<td align="right">23.3%</td>
<td align="right">20.0%</td>
<td align="right">15.8%</td>
<td align="right">14917</td>
</tr>
<tr>
<td align="left">81</td>
<td align="left">🟡 Disease</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">44.4%</td>
<td align="right">34.8%</td>
<td align="right">25.4%</td>
<td align="right">18.8%</td>
<td align="right">15.6%</td>
<td align="right">2369</td>
</tr>
<tr>
<td align="left">82</td>
<td align="left">🟡 Klutz</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">25.4%</td>
<td align="right">51.1%</td>
<td align="right">32.9%</td>
<td align="right">26.0%</td>
<td align="right">19.9%</td>
<td align="right">17.2%</td>
<td align="right">2307</td>
</tr>
<tr>
<td align="left">83</td>
<td align="left">🟡 Emperor</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">45.9%</td>
<td align="right">31.7%</td>
<td align="right">24.9%</td>
<td align="right">21.0%</td>
<td align="right">18.5%</td>
<td align="right">2298</td>
</tr>
<tr>
<td align="left">84</td>
<td align="left">🟡 Relic</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">50.2%</td>
<td align="right">33.0%</td>
<td align="right">26.5%</td>
<td align="right">18.1%</td>
<td align="right">16.5%</td>
<td align="right">2503</td>
</tr>
<tr>
<td align="left">85</td>
<td align="left">🟡 Spiff</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">47.5%</td>
<td align="right">32.4%</td>
<td align="right">24.7%</td>
<td align="right">19.0%</td>
<td align="right">17.2%</td>
<td align="right">14835</td>
</tr>
<tr>
<td align="left">86</td>
<td align="left">🟡 Philanthropist</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">49.7%</td>
<td align="right">31.2%</td>
<td align="right">24.0%</td>
<td align="right">18.4%</td>
<td align="right">17.4%</td>
<td align="right">14834</td>
</tr>
<tr>
<td align="left">87</td>
<td align="left">🟡 Gremlin</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.6%</td>
<td align="right">45.2%</td>
<td align="right">39.3%</td>
<td align="right">27.1%</td>
<td align="right">19.6%</td>
<td align="right">15.6%</td>
<td align="right">2110</td>
</tr>
<tr>
<td align="left">88</td>
<td align="left">🟡 Remora</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">48.6%</td>
<td align="right">31.2%</td>
<td align="right">24.6%</td>
<td align="right">19.5%</td>
<td align="right">16.2%</td>
<td align="right">15048</td>
</tr>
<tr>
<td align="left">89</td>
<td align="left">🟡 Ghoul</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">42.5%</td>
<td align="right">33.6%</td>
<td align="right">24.8%</td>
<td align="right">22.2%</td>
<td align="right">14.1%</td>
<td align="right">2492</td>
</tr>
<tr>
<td align="left">90</td>
<td align="left">🟡 Fodder</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">48.4%</td>
<td align="right">31.2%</td>
<td align="right">24.0%</td>
<td align="right">20.1%</td>
<td align="right">16.8%</td>
<td align="right">14830</td>
</tr>
<tr>
<td align="left">91</td>
<td align="left">🟡 Gambler</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">48.0%</td>
<td align="right">32.8%</td>
<td align="right">25.3%</td>
<td align="right">19.2%</td>
<td align="right">15.8%</td>
<td align="right">15040</td>
</tr>
<tr>
<td align="left">92</td>
<td align="left">🟡 Perfectionist</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">48.7%</td>
<td align="right">36.0%</td>
<td align="right">24.8%</td>
<td align="right">19.6%</td>
<td align="right">15.5%</td>
<td align="right">2390</td>
</tr>
<tr>
<td align="left">93</td>
<td align="left">🟡 Fido</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.6%</td>
<td align="right">49.3%</td>
<td align="right">32.9%</td>
<td align="right">24.5%</td>
<td align="right">20.1%</td>
<td align="right">16.0%</td>
<td align="right">14917</td>
</tr>
<tr>
<td align="left">94</td>
<td align="left">🟡 Multitude</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">49.8%</td>
<td align="right">34.2%</td>
<td align="right">22.4%</td>
<td align="right">18.3%</td>
<td align="right">15.4%</td>
<td align="right">2250</td>
</tr>
<tr>
<td align="left">95</td>
<td align="left">🟡 Whirligig</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">47.2%</td>
<td align="right">33.3%</td>
<td align="right">24.0%</td>
<td align="right">20.7%</td>
<td align="right">17.5%</td>
<td align="right">2259</td>
</tr>
<tr>
<td align="left">96</td>
<td align="left">🟡 Clone</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">50.4%</td>
<td align="right">31.8%</td>
<td align="right">24.3%</td>
<td align="right">18.7%</td>
<td align="right">15.6%</td>
<td align="right">14963</td>
</tr>
<tr>
<td align="left">97</td>
<td align="left">🟡 Sorcerer</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">47.6%</td>
<td align="right">31.8%</td>
<td align="right">24.0%</td>
<td align="right">19.7%</td>
<td align="right">16.2%</td>
<td align="right">15017</td>
</tr>
<tr>
<td align="left">98</td>
<td align="left">🟡 Mirror</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">46.9%</td>
<td align="right">33.2%</td>
<td align="right">25.8%</td>
<td align="right">19.3%</td>
<td align="right">14.9%</td>
<td align="right">14881</td>
</tr>
<tr>
<td align="left">99</td>
<td align="left">🟡 Sting</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">53.0%</td>
<td align="right">32.2%</td>
<td align="right">22.2%</td>
<td align="right">19.9%</td>
<td align="right">16.8%</td>
<td align="right">2558</td>
</tr>
<tr>
<td align="left">100</td>
<td align="left">🟡 Changeling</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">46.5%</td>
<td align="right">33.2%</td>
<td align="right">21.7%</td>
<td align="right">18.6%</td>
<td align="right">17.0%</td>
<td align="right">2518</td>
</tr>
<tr>
<td align="left">101</td>
<td align="left">🟡 Filch</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">48.9%</td>
<td align="right">31.4%</td>
<td align="right">23.7%</td>
<td align="right">19.0%</td>
<td align="right">15.6%</td>
<td align="right">15109</td>
</tr>
<tr>
<td align="left">102</td>
<td align="left">🟡 Reincarnator</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">50.9%</td>
<td align="right">31.5%</td>
<td align="right">23.8%</td>
<td align="right">19.6%</td>
<td align="right">14.5%</td>
<td align="right">15063</td>
</tr>
<tr>
<td align="left">103</td>
<td align="left">🟡 Demon</td>
<td align="left">Custom</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">46.0%</td>
<td align="right">32.8%</td>
<td align="right">23.1%</td>
<td align="right">18.6%</td>
<td align="right">16.3%</td>
<td align="right">14885</td>
</tr>
<tr>
<td align="left">104</td>
<td align="left">🟡 Joker</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">55.4%</td>
<td align="right">30.6%</td>
<td align="right">22.9%</td>
<td align="right">19.0%</td>
<td align="right">17.1%</td>
<td align="right">2328</td>
</tr>
<tr>
<td align="left">105</td>
<td align="left">🟡 Prophet</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.9%</td>
<td align="right">48.2%</td>
<td align="right">32.6%</td>
<td align="right">26.2%</td>
<td align="right">19.3%</td>
<td align="right">17.2%</td>
<td align="right">2453</td>
</tr>
<tr>
<td align="left">106</td>
<td align="left">🟡 Locust_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">49.0%</td>
<td align="right">31.8%</td>
<td align="right">25.8%</td>
<td align="right">19.9%</td>
<td align="right">15.3%</td>
<td align="right">2123</td>
</tr>
<tr>
<td align="left">107</td>
<td align="left">🟡 Vacuum</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">50.4%</td>
<td align="right">32.2%</td>
<td align="right">24.7%</td>
<td align="right">19.3%</td>
<td align="right">15.9%</td>
<td align="right">15015</td>
</tr>
<tr>
<td align="left">108</td>
<td align="left">🟡 Hacker</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">49.3%</td>
<td align="right">32.4%</td>
<td align="right">23.5%</td>
<td align="right">18.6%</td>
<td align="right">16.0%</td>
<td align="right">14899</td>
</tr>
<tr>
<td align="left">109</td>
<td align="left">🟡 Dictator</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">46.2%</td>
<td align="right">31.7%</td>
<td align="right">24.0%</td>
<td align="right">18.4%</td>
<td align="right">16.8%</td>
<td align="right">15119</td>
</tr>
<tr>
<td align="left">110</td>
<td align="left">🟡 Genius</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">50.6%</td>
<td align="right">34.8%</td>
<td align="right">20.3%</td>
<td align="right">17.6%</td>
<td align="right">18.6%</td>
<td align="right">2385</td>
</tr>
<tr>
<td align="left">111</td>
<td align="left">🟡 Tide</td>
<td align="left">Storm</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">41.1%</td>
<td align="right">36.5%</td>
<td align="right">25.9%</td>
<td align="right">20.5%</td>
<td align="right">15.1%</td>
<td align="right">2454</td>
</tr>
<tr>
<td align="left">112</td>
<td align="left">🟡 Vulch</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">47.4%</td>
<td align="right">33.2%</td>
<td align="right">23.9%</td>
<td align="right">19.1%</td>
<td align="right">16.8%</td>
<td align="right">15015</td>
</tr>
<tr>
<td align="left">113</td>
<td align="left">🟡 Decoy</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.1%</td>
<td align="right">48.8%</td>
<td align="right">28.8%</td>
<td align="right">24.4%</td>
<td align="right">19.8%</td>
<td align="right">16.7%</td>
<td align="right">2103</td>
</tr>
<tr>
<td align="left">114</td>
<td align="left">🟡 Chosen</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">47.7%</td>
<td align="right">31.3%</td>
<td align="right">24.0%</td>
<td align="right">19.1%</td>
<td align="right">15.7%</td>
<td align="right">15187</td>
</tr>
<tr>
<td align="left">115</td>
<td align="left">🟡 Sneak</td>
<td align="left">Storm</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">48.2%</td>
<td align="right">31.1%</td>
<td align="right">24.8%</td>
<td align="right">17.5%</td>
<td align="right">15.5%</td>
<td align="right">2317</td>
</tr>
<tr>
<td align="left">116</td>
<td align="left">🟡 Calculator</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">47.1%</td>
<td align="right">31.0%</td>
<td align="right">24.6%</td>
<td align="right">18.5%</td>
<td align="right">15.9%</td>
<td align="right">14927</td>
</tr>
<tr>
<td align="left">117</td>
<td align="left">🟡 Dragon</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.5%</td>
<td align="right">53.3%</td>
<td align="right">32.9%</td>
<td align="right">25.6%</td>
<td align="right">20.3%</td>
<td align="right">16.6%</td>
<td align="right">2069</td>
</tr>
<tr>
<td align="left">118</td>
<td align="left">🟡 Will</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">47.6%</td>
<td align="right">32.5%</td>
<td align="right">24.0%</td>
<td align="right">18.2%</td>
<td align="right">16.2%</td>
<td align="right">15074</td>
</tr>
<tr>
<td align="left">119</td>
<td align="left">🟡 Fungus</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">46.3%</td>
<td align="right">31.4%</td>
<td align="right">28.8%</td>
<td align="right">19.1%</td>
<td align="right">15.3%</td>
<td align="right">2426</td>
</tr>
<tr>
<td align="left">120</td>
<td align="left">🟡 Saboteur</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.0%</td>
<td align="right">48.3%</td>
<td align="right">30.1%</td>
<td align="right">24.5%</td>
<td align="right">18.4%</td>
<td align="right">17.6%</td>
<td align="right">2415</td>
</tr>
<tr>
<td align="left">121</td>
<td align="left">🟡 Xenophile</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">23.9%</td>
<td align="right">47.0%</td>
<td align="right">31.8%</td>
<td align="right">24.8%</td>
<td align="right">20.6%</td>
<td align="right">14.5%</td>
<td align="right">2472</td>
</tr>
<tr>
<td align="left">122</td>
<td align="left">🟡 Void_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">54.3%</td>
<td align="right">33.5%</td>
<td align="right">22.4%</td>
<td align="right">18.7%</td>
<td align="right">15.4%</td>
<td align="right">2033</td>
</tr>
<tr>
<td align="left">123</td>
<td align="left">🟡 Mite</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">46.6%</td>
<td align="right">32.3%</td>
<td align="right">23.3%</td>
<td align="right">19.5%</td>
<td align="right">16.2%</td>
<td align="right">14885</td>
</tr>
<tr>
<td align="left">124</td>
<td align="left">🟡 Reserve</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">48.8%</td>
<td align="right">31.0%</td>
<td align="right">23.5%</td>
<td align="right">18.3%</td>
<td align="right">15.6%</td>
<td align="right">15018</td>
</tr>
<tr>
<td align="left">125</td>
<td align="left">🟡 Trader</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">46.8%</td>
<td align="right">32.4%</td>
<td align="right">24.9%</td>
<td align="right">18.0%</td>
<td align="right">16.2%</td>
<td align="right">15043</td>
</tr>
<tr>
<td align="left">126</td>
<td align="left">🟡 Alchemist</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">51.2%</td>
<td align="right">35.6%</td>
<td align="right">25.8%</td>
<td align="right">17.8%</td>
<td align="right">17.3%</td>
<td align="right">2319</td>
</tr>
<tr>
<td align="left">127</td>
<td align="left">🟡 Cudgel</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">46.3%</td>
<td align="right">32.2%</td>
<td align="right">23.0%</td>
<td align="right">18.6%</td>
<td align="right">16.1%</td>
<td align="right">14864</td>
</tr>
<tr>
<td align="left">128</td>
<td align="left">🟡 Tortoise</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">24.8%</td>
<td align="right">45.6%</td>
<td align="right">32.3%</td>
<td align="right">28.6%</td>
<td align="right">16.2%</td>
<td align="right">19.2%</td>
<td align="right">2313</td>
</tr>
<tr>
<td align="left">129</td>
<td align="left">🟡 Oracle</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.5%</td>
<td align="right">49.3%</td>
<td align="right">31.4%</td>
<td align="right">23.4%</td>
<td align="right">18.3%</td>
<td align="right">15.4%</td>
<td align="right">14852</td>
</tr>
<tr>
<td align="left">130</td>
<td align="left">🟡 TickTock</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.4%</td>
<td align="right">48.5%</td>
<td align="right">31.9%</td>
<td align="right">23.1%</td>
<td align="right">18.5%</td>
<td align="right">15.5%</td>
<td align="right">14813</td>
</tr>
<tr>
<td align="left">131</td>
<td align="left">🟡 Pygmy</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">52.4%</td>
<td align="right">35.8%</td>
<td align="right">24.3%</td>
<td align="right">19.8%</td>
<td align="right">14.6%</td>
<td align="right">2467</td>
</tr>
<tr>
<td align="left">132</td>
<td align="left">🟡 Trickster</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">46.5%</td>
<td align="right">34.9%</td>
<td align="right">23.6%</td>
<td align="right">20.8%</td>
<td align="right">16.0%</td>
<td align="right">2391</td>
</tr>
<tr>
<td align="left">133</td>
<td align="left">🟡 Negator</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.0%</td>
<td align="right">45.6%</td>
<td align="right">31.7%</td>
<td align="right">27.7%</td>
<td align="right">17.3%</td>
<td align="right">18.9%</td>
<td align="right">2028</td>
</tr>
<tr>
<td align="left">134</td>
<td align="left">🟡 Pickpocket</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.6%</td>
<td align="right">50.4%</td>
<td align="right">30.0%</td>
<td align="right">24.8%</td>
<td align="right">19.7%</td>
<td align="right">14.3%</td>
<td align="right">2353</td>
</tr>
<tr>
<td align="left">135</td>
<td align="left">🟡 Magician</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">48.1%</td>
<td align="right">31.9%</td>
<td align="right">26.8%</td>
<td align="right">20.9%</td>
<td align="right">16.3%</td>
<td align="right">2553</td>
</tr>
<tr>
<td align="left">136</td>
<td align="left">🟡 Locust</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">46.1%</td>
<td align="right">33.3%</td>
<td align="right">24.9%</td>
<td align="right">20.9%</td>
<td align="right">15.9%</td>
<td align="right">2499</td>
</tr>
<tr>
<td align="left">137</td>
<td align="left">🟡 Lunatic</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">24.7%</td>
<td align="right">48.7%</td>
<td align="right">33.6%</td>
<td align="right">24.4%</td>
<td align="right">18.1%</td>
<td align="right">17.2%</td>
<td align="right">2501</td>
</tr>
<tr>
<td align="left">138</td>
<td align="left">🟡 Cavalry</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">48.7%</td>
<td align="right">31.9%</td>
<td align="right">27.2%</td>
<td align="right">20.1%</td>
<td align="right">17.2%</td>
<td align="right">2513</td>
</tr>
<tr>
<td align="left">139</td>
<td align="left">🟡 Grumpus_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.3%</td>
<td align="right">49.5%</td>
<td align="right">34.4%</td>
<td align="right">22.2%</td>
<td align="right">24.6%</td>
<td align="right">14.6%</td>
<td align="right">2113</td>
</tr>
<tr>
<td align="left">140</td>
<td align="left">🟡 Warhawk</td>
<td align="left">Conflict</td>
<td align="right"><b>1499</b></td>
<td align="right">25.0%</td>
<td align="right">47.6%</td>
<td align="right">31.5%</td>
<td align="right">25.4%</td>
<td align="right">20.0%</td>
<td align="right">18.0%</td>
<td align="right">2482</td>
</tr>
<tr>
<td align="left">141</td>
<td align="left">🟡 Aristocrat</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">23.3%</td>
<td align="right">46.8%</td>
<td align="right">30.8%</td>
<td align="right">22.2%</td>
<td align="right">20.4%</td>
<td align="right">15.4%</td>
<td align="right">2330</td>
</tr>
<tr>
<td align="left">142</td>
<td align="left">🟡 Animal</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">25.0%</td>
<td align="right">55.4%</td>
<td align="right">32.5%</td>
<td align="right">22.5%</td>
<td align="right">19.0%</td>
<td align="right">18.3%</td>
<td align="right">2505</td>
</tr>
<tr>
<td align="left">143</td>
<td align="left">🟡 Roach</td>
<td align="left">Storm</td>
<td align="right"><b>1499</b></td>
<td align="right">24.9%</td>
<td align="right">49.0%</td>
<td align="right">35.9%</td>
<td align="right">23.5%</td>
<td align="right">21.0%</td>
<td align="right">15.4%</td>
<td align="right">2413</td>
</tr>
<tr>
<td align="left">144</td>
<td align="left">🟡 Anarchist</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">23.8%</td>
<td align="right">44.7%</td>
<td align="right">33.7%</td>
<td align="right">23.4%</td>
<td align="right">18.5%</td>
<td align="right">16.4%</td>
<td align="right">2315</td>
</tr>
<tr>
<td align="left">145</td>
<td align="left">🟡 Kamikaze</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.0%</td>
<td align="right">46.3%</td>
<td align="right">30.6%</td>
<td align="right">24.3%</td>
<td align="right">18.4%</td>
<td align="right">14.6%</td>
<td align="right">14907</td>
</tr>
<tr>
<td align="left">146</td>
<td align="left">🟡 Barbarian</td>
<td align="left">Base</td>
<td align="right"><b>1499</b></td>
<td align="right">23.1%</td>
<td align="right">40.0%</td>
<td align="right">31.5%</td>
<td align="right">23.0%</td>
<td align="right">19.5%</td>
<td align="right">16.3%</td>
<td align="right">14973</td>
</tr>
<tr>
<td align="left">147</td>
<td align="left">🟡 Boomerang</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">25.1%</td>
<td align="right">50.0%</td>
<td align="right">35.2%</td>
<td align="right">23.8%</td>
<td align="right">20.1%</td>
<td align="right">16.3%</td>
<td align="right">2101</td>
</tr>
<tr>
<td align="left">148</td>
<td align="left">🟡 Seeker</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">25.2%</td>
<td align="right">50.0%</td>
<td align="right">33.0%</td>
<td align="right">26.6%</td>
<td align="right">20.7%</td>
<td align="right">15.7%</td>
<td align="right">2457</td>
</tr>
<tr>
<td align="left">149</td>
<td align="left">🟡 Extractor</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.7%</td>
<td align="right">46.8%</td>
<td align="right">30.7%</td>
<td align="right">22.4%</td>
<td align="right">22.9%</td>
<td align="right">16.8%</td>
<td align="right">2104</td>
</tr>
<tr>
<td align="left">150</td>
<td align="left">🟡 Pirate</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.5%</td>
<td align="right">49.8%</td>
<td align="right">30.4%</td>
<td align="right">23.0%</td>
<td align="right">21.2%</td>
<td align="right">16.3%</td>
<td align="right">2274</td>
</tr>
<tr>
<td align="left">151</td>
<td align="left">🟡 Surgeon</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">23.7%</td>
<td align="right">52.2%</td>
<td align="right">29.6%</td>
<td align="right">21.5%</td>
<td align="right">19.5%</td>
<td align="right">16.3%</td>
<td align="right">2322</td>
</tr>
<tr>
<td align="left">152</td>
<td align="left">🟡 Geek</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.3%</td>
<td align="right">48.1%</td>
<td align="right">33.7%</td>
<td align="right">23.2%</td>
<td align="right">18.1%</td>
<td align="right">16.3%</td>
<td align="right">2140</td>
</tr>
<tr>
<td align="left">153</td>
<td align="left">🟡 Throwback</td>
<td align="left">Odyssey</td>
<td align="right"><b>1499</b></td>
<td align="right">24.7%</td>
<td align="right">51.3%</td>
<td align="right">33.6%</td>
<td align="right">23.8%</td>
<td align="right">18.2%</td>
<td align="right">17.2%</td>
<td align="right">2129</td>
</tr>
<tr>
<td align="left">154</td>
<td align="left">🟡 Guerrilla</td>
<td align="left">Incursion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.6%</td>
<td align="right">51.6%</td>
<td align="right">35.3%</td>
<td align="right">21.8%</td>
<td align="right">18.4%</td>
<td align="right">17.3%</td>
<td align="right">2557</td>
</tr>
<tr>
<td align="left">155</td>
<td align="left">🟡 Brute</td>
<td align="left">Storm</td>
<td align="right"><b>1499</b></td>
<td align="right">25.4%</td>
<td align="right">50.6%</td>
<td align="right">34.7%</td>
<td align="right">24.3%</td>
<td align="right">20.3%</td>
<td align="right">17.5%</td>
<td align="right">2408</td>
</tr>
<tr>
<td align="left">156</td>
<td align="left">🟡 Extortionist</td>
<td align="left">Alliance</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">45.8%</td>
<td align="right">33.1%</td>
<td align="right">24.8%</td>
<td align="right">20.4%</td>
<td align="right">15.6%</td>
<td align="right">2470</td>
</tr>
<tr>
<td align="left">157</td>
<td align="left">🟡 Alien</td>
<td align="left">Eons</td>
<td align="right"><b>1499</b></td>
<td align="right">24.4%</td>
<td align="right">51.0%</td>
<td align="right">33.7%</td>
<td align="right">25.1%</td>
<td align="right">16.9%</td>
<td align="right">17.0%</td>
<td align="right">2356</td>
</tr>
<tr>
<td align="left">158</td>
<td align="left">🟡 Judge</td>
<td align="left">Dominion</td>
<td align="right"><b>1499</b></td>
<td align="right">24.2%</td>
<td align="right">47.5%</td>
<td align="right">30.5%</td>
<td align="right">23.4%</td>
<td align="right">19.9%</td>
<td align="right">17.1%</td>
<td align="right">2247</td>
</tr>
<tr>
<td align="left">159</td>
<td align="left">🟡 Mercenary</td>
<td align="left">Incursion</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">47.2%</td>
<td align="right">31.6%</td>
<td align="right">23.7%</td>
<td align="right">16.1%</td>
<td align="right">18.4%</td>
<td align="right">2547</td>
</tr>
<tr>
<td align="left">160</td>
<td align="left">🟡 Angler</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">51.4%</td>
<td align="right">34.1%</td>
<td align="right">25.1%</td>
<td align="right">18.1%</td>
<td align="right">15.5%</td>
<td align="right">2297</td>
</tr>
<tr>
<td align="left">161</td>
<td align="left">🟡 Swindler</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">49.0%</td>
<td align="right">35.1%</td>
<td align="right">22.6%</td>
<td align="right">18.1%</td>
<td align="right">15.2%</td>
<td align="right">2440</td>
</tr>
<tr>
<td align="left">162</td>
<td align="left">🟡 PackRat</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">46.7%</td>
<td align="right">30.4%</td>
<td align="right">21.5%</td>
<td align="right">21.4%</td>
<td align="right">15.9%</td>
<td align="right">2304</td>
</tr>
<tr>
<td align="left">163</td>
<td align="left">🟡 Crystal</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">43.8%</td>
<td align="right">38.2%</td>
<td align="right">23.8%</td>
<td align="right">21.5%</td>
<td align="right">15.5%</td>
<td align="right">2497</td>
</tr>
<tr>
<td align="left">164</td>
<td align="left">🟡 Butler</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">25.0%</td>
<td align="right">52.6%</td>
<td align="right">32.1%</td>
<td align="right">24.5%</td>
<td align="right">18.3%</td>
<td align="right">17.3%</td>
<td align="right">2487</td>
</tr>
<tr>
<td align="left">165</td>
<td align="left">🟡 Phantasm</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">24.4%</td>
<td align="right">45.4%</td>
<td align="right">29.8%</td>
<td align="right">25.6%</td>
<td align="right">21.9%</td>
<td align="right">15.3%</td>
<td align="right">2385</td>
</tr>
<tr>
<td align="left">166</td>
<td align="left">🟡 Glutton</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">24.0%</td>
<td align="right">51.6%</td>
<td align="right">31.7%</td>
<td align="right">24.0%</td>
<td align="right">16.7%</td>
<td align="right">16.6%</td>
<td align="right">2508</td>
</tr>
<tr>
<td align="left">167</td>
<td align="left">🟡 Gorgon</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">52.3%</td>
<td align="right">30.7%</td>
<td align="right">22.6%</td>
<td align="right">19.8%</td>
<td align="right">17.1%</td>
<td align="right">2455</td>
</tr>
<tr>
<td align="left">168</td>
<td align="left">🟡 Bride</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">45.5%</td>
<td align="right">38.8%</td>
<td align="right">21.5%</td>
<td align="right">18.9%</td>
<td align="right">14.7%</td>
<td align="right">2362</td>
</tr>
<tr>
<td align="left">169</td>
<td align="left">🟡 Reactor</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">49.8%</td>
<td align="right">32.9%</td>
<td align="right">22.2%</td>
<td align="right">22.8%</td>
<td align="right">15.3%</td>
<td align="right">2297</td>
</tr>
<tr>
<td align="left">170</td>
<td align="left">🟡 Tourist</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">49.1%</td>
<td align="right">29.8%</td>
<td align="right">26.4%</td>
<td align="right">20.0%</td>
<td align="right">17.2%</td>
<td align="right">2385</td>
</tr>
<tr>
<td align="left">171</td>
<td align="left">🟡 Host</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.0%</td>
<td align="right">52.5%</td>
<td align="right">32.8%</td>
<td align="right">24.3%</td>
<td align="right">17.7%</td>
<td align="right">15.1%</td>
<td align="right">2337</td>
</tr>
<tr>
<td align="left">172</td>
<td align="left">🟡 Mimic</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">43.8%</td>
<td align="right">31.6%</td>
<td align="right">22.7%</td>
<td align="right">19.2%</td>
<td align="right">16.6%</td>
<td align="right">2575</td>
</tr>
<tr>
<td align="left">173</td>
<td align="left">🟡 Cyborg</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">25.2%</td>
<td align="right">49.6%</td>
<td align="right">34.3%</td>
<td align="right">26.1%</td>
<td align="right">20.5%</td>
<td align="right">16.8%</td>
<td align="right">2538</td>
</tr>
<tr>
<td align="left">174</td>
<td align="left">🟡 Doppelganger</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.4%</td>
<td align="right">49.6%</td>
<td align="right">26.7%</td>
<td align="right">26.9%</td>
<td align="right">20.2%</td>
<td align="right">16.1%</td>
<td align="right">2243</td>
</tr>
<tr>
<td align="left">175</td>
<td align="left">🟡 Aura</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">47.3%</td>
<td align="right">35.4%</td>
<td align="right">23.2%</td>
<td align="right">19.5%</td>
<td align="right">16.8%</td>
<td align="right">2070</td>
</tr>
<tr>
<td align="left">176</td>
<td align="left">🟡 Worm</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">48.2%</td>
<td align="right">33.1%</td>
<td align="right">24.7%</td>
<td align="right">17.2%</td>
<td align="right">16.0%</td>
<td align="right">2402</td>
</tr>
<tr>
<td align="left">177</td>
<td align="left">🟡 Mirage</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.2%</td>
<td align="right">48.9%</td>
<td align="right">30.7%</td>
<td align="right">24.2%</td>
<td align="right">19.2%</td>
<td align="right">16.8%</td>
<td align="right">2352</td>
</tr>
<tr>
<td align="left">178</td>
<td align="left">🟡 Witch</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">24.8%</td>
<td align="right">47.2%</td>
<td align="right">32.2%</td>
<td align="right">25.2%</td>
<td align="right">18.7%</td>
<td align="right">18.6%</td>
<td align="right">2125</td>
</tr>
<tr>
<td align="left">179</td>
<td align="left">🟡 Maven</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">25.4%</td>
<td align="right">48.7%</td>
<td align="right">36.2%</td>
<td align="right">25.4%</td>
<td align="right">19.5%</td>
<td align="right">17.1%</td>
<td align="right">2317</td>
</tr>
<tr>
<td align="left">180</td>
<td align="left">🟡 Bully</td>
<td align="left">Incursion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">47.3%</td>
<td align="right">36.1%</td>
<td align="right">24.5%</td>
<td align="right">20.2%</td>
<td align="right">16.5%</td>
<td align="right">2510</td>
</tr>
<tr>
<td align="left">181</td>
<td align="left">🟡 Wormhole</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">45.4%</td>
<td align="right">34.9%</td>
<td align="right">21.7%</td>
<td align="right">16.0%</td>
<td align="right">18.5%</td>
<td align="right">2328</td>
</tr>
<tr>
<td align="left">182</td>
<td align="left">🟡 Merchant</td>
<td align="left">Incursion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.3%</td>
<td align="right">48.3%</td>
<td align="right">31.8%</td>
<td align="right">24.4%</td>
<td align="right">20.0%</td>
<td align="right">16.0%</td>
<td align="right">2585</td>
</tr>
<tr>
<td align="left">183</td>
<td align="left">🟡 Converter</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">24.2%</td>
<td align="right">45.0%</td>
<td align="right">30.0%</td>
<td align="right">26.8%</td>
<td align="right">20.5%</td>
<td align="right">15.8%</td>
<td align="right">2338</td>
</tr>
<tr>
<td align="left">184</td>
<td align="left">🟡 Magnet</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">23.3%</td>
<td align="right">39.0%</td>
<td align="right">32.5%</td>
<td align="right">25.1%</td>
<td align="right">21.3%</td>
<td align="right">13.9%</td>
<td align="right">2143</td>
</tr>
<tr>
<td align="left">185</td>
<td align="left">🟡 Deuce</td>
<td align="left">Incursion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.0%</td>
<td align="right">45.8%</td>
<td align="right">30.2%</td>
<td align="right">24.2%</td>
<td align="right">20.5%</td>
<td align="right">16.7%</td>
<td align="right">2572</td>
</tr>
<tr>
<td align="left">186</td>
<td align="left">🟡 Moocher</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">46.1%</td>
<td align="right">32.2%</td>
<td align="right">21.9%</td>
<td align="right">22.6%</td>
<td align="right">15.4%</td>
<td align="right">2280</td>
</tr>
<tr>
<td align="left">187</td>
<td align="left">🟡 Explorer</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">50.2%</td>
<td align="right">34.4%</td>
<td align="right">22.0%</td>
<td align="right">19.0%</td>
<td align="right">16.4%</td>
<td align="right">2347</td>
</tr>
<tr>
<td align="left">188</td>
<td align="left">🟡 Sycophant</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">25.4%</td>
<td align="right">55.8%</td>
<td align="right">35.8%</td>
<td align="right">23.8%</td>
<td align="right">20.3%</td>
<td align="right">15.9%</td>
<td align="right">2329</td>
</tr>
<tr>
<td align="left">189</td>
<td align="left">🟡 Assistant</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">43.6%</td>
<td align="right">31.0%</td>
<td align="right">23.5%</td>
<td align="right">20.0%</td>
<td align="right">15.3%</td>
<td align="right">2359</td>
</tr>
<tr>
<td align="left">190</td>
<td align="left">🟡 Amoeba</td>
<td align="left">Base</td>
<td align="right"><b>1498</b></td>
<td align="right">21.4%</td>
<td align="right">48.4%</td>
<td align="right">22.1%</td>
<td align="right">21.0%</td>
<td align="right">16.5%</td>
<td align="right">16.5%</td>
<td align="right">15207</td>
</tr>
<tr>
<td align="left">191</td>
<td align="left">🟡 Quartermaster</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">57.0%</td>
<td align="right">28.9%</td>
<td align="right">25.7%</td>
<td align="right">16.2%</td>
<td align="right">15.5%</td>
<td align="right">2260</td>
</tr>
<tr>
<td align="left">192</td>
<td align="left">🟡 Sapient</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">24.4%</td>
<td align="right">43.4%</td>
<td align="right">33.6%</td>
<td align="right">25.3%</td>
<td align="right">21.5%</td>
<td align="right">15.9%</td>
<td align="right">2528</td>
</tr>
<tr>
<td align="left">193</td>
<td align="left">🟡 Bubble</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">54.9%</td>
<td align="right">32.0%</td>
<td align="right">25.2%</td>
<td align="right">17.9%</td>
<td align="right">14.6%</td>
<td align="right">2092</td>
</tr>
<tr>
<td align="left">194</td>
<td align="left">🟡 Booster</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">54.1%</td>
<td align="right">31.7%</td>
<td align="right">25.3%</td>
<td align="right">19.2%</td>
<td align="right">13.2%</td>
<td align="right">2118</td>
</tr>
<tr>
<td align="left">195</td>
<td align="left">🟡 Muckraker</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.5%</td>
<td align="right">50.2%</td>
<td align="right">31.8%</td>
<td align="right">22.0%</td>
<td align="right">20.7%</td>
<td align="right">16.6%</td>
<td align="right">2337</td>
</tr>
<tr>
<td align="left">196</td>
<td align="left">🟡 Daredevil</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.7%</td>
<td align="right">50.2%</td>
<td align="right">30.8%</td>
<td align="right">25.0%</td>
<td align="right">20.7%</td>
<td align="right">16.6%</td>
<td align="right">2275</td>
</tr>
<tr>
<td align="left">197</td>
<td align="left">🟡 Peddler</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">45.3%</td>
<td align="right">30.5%</td>
<td align="right">23.8%</td>
<td align="right">19.4%</td>
<td align="right">16.6%</td>
<td align="right">2306</td>
</tr>
<tr>
<td align="left">198</td>
<td align="left">🟡 Love</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">24.5%</td>
<td align="right">47.2%</td>
<td align="right">33.0%</td>
<td align="right">25.2%</td>
<td align="right">21.2%</td>
<td align="right">14.6%</td>
<td align="right">2293</td>
</tr>
<tr>
<td align="left">199</td>
<td align="left">🟡 Cloak</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">23.9%</td>
<td align="right">50.5%</td>
<td align="right">30.1%</td>
<td align="right">24.9%</td>
<td align="right">20.1%</td>
<td align="right">16.0%</td>
<td align="right">2294</td>
</tr>
<tr>
<td align="left">200</td>
<td align="left">🟡 AI</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">24.3%</td>
<td align="right">45.0%</td>
<td align="right">31.6%</td>
<td align="right">23.7%</td>
<td align="right">20.0%</td>
<td align="right">17.2%</td>
<td align="right">2367</td>
</tr>
<tr>
<td align="left">201</td>
<td align="left">🟡 Squee</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">54.7%</td>
<td align="right">28.7%</td>
<td align="right">22.5%</td>
<td align="right">19.8%</td>
<td align="right">16.5%</td>
<td align="right">2387</td>
</tr>
<tr>
<td align="left">202</td>
<td align="left">🟡 Lizard</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">23.7%</td>
<td align="right">46.8%</td>
<td align="right">29.7%</td>
<td align="right">24.6%</td>
<td align="right">18.7%</td>
<td align="right">16.5%</td>
<td align="right">2287</td>
</tr>
<tr>
<td align="left">203</td>
<td align="left">🟡 Sadist_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">44.0%</td>
<td align="right">33.3%</td>
<td align="right">27.0%</td>
<td align="right">18.0%</td>
<td align="right">17.6%</td>
<td align="right">2144</td>
</tr>
<tr>
<td align="left">204</td>
<td align="left">🟡 Filth</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">24.3%</td>
<td align="right">46.4%</td>
<td align="right">30.0%</td>
<td align="right">26.2%</td>
<td align="right">18.5%</td>
<td align="right">18.0%</td>
<td align="right">2533</td>
</tr>
<tr>
<td align="left">205</td>
<td align="left">🟡 Invader</td>
<td align="left">Conflict</td>
<td align="right"><b>1498</b></td>
<td align="right">23.8%</td>
<td align="right">43.8%</td>
<td align="right">33.6%</td>
<td align="right">23.4%</td>
<td align="right">20.6%</td>
<td align="right">15.2%</td>
<td align="right">2449</td>
</tr>
<tr>
<td align="left">206</td>
<td align="left">🟡 Sheriff</td>
<td align="left">Eons</td>
<td align="right"><b>1498</b></td>
<td align="right">24.1%</td>
<td align="right">41.7%</td>
<td align="right">34.7%</td>
<td align="right">25.8%</td>
<td align="right">18.9%</td>
<td align="right">16.7%</td>
<td align="right">2241</td>
</tr>
<tr>
<td align="left">207</td>
<td align="left">🟡 Winner</td>
<td align="left">Alliance</td>
<td align="right"><b>1498</b></td>
<td align="right">23.2%</td>
<td align="right">46.9%</td>
<td align="right">31.5%</td>
<td align="right">24.1%</td>
<td align="right">19.8%</td>
<td align="right">13.8%</td>
<td align="right">2601</td>
</tr>
<tr>
<td align="left">208</td>
<td align="left">🟡 Dervish</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">24.6%</td>
<td align="right">53.1%</td>
<td align="right">31.1%</td>
<td align="right">25.2%</td>
<td align="right">21.6%</td>
<td align="right">15.3%</td>
<td align="right">2434</td>
</tr>
<tr>
<td align="left">209</td>
<td align="left">🟡 Engineer</td>
<td align="left">Dominion</td>
<td align="right"><b>1498</b></td>
<td align="right">23.5%</td>
<td align="right">50.5%</td>
<td align="right">30.1%</td>
<td align="right">24.5%</td>
<td align="right">17.5%</td>
<td align="right">15.8%</td>
<td align="right">2240</td>
</tr>
<tr>
<td align="left">210</td>
<td align="left">🟡 Lloyd</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">24.0%</td>
<td align="right">47.0%</td>
<td align="right">31.2%</td>
<td align="right">20.8%</td>
<td align="right">20.1%</td>
<td align="right">17.6%</td>
<td align="right">2065</td>
</tr>
<tr>
<td align="left">211</td>
<td align="left">🟡 Hurtz</td>
<td align="left">Odyssey</td>
<td align="right"><b>1498</b></td>
<td align="right">24.8%</td>
<td align="right">43.1%</td>
<td align="right">37.0%</td>
<td align="right">27.8%</td>
<td align="right">18.4%</td>
<td align="right">16.3%</td>
<td align="right">2102</td>
</tr>
<tr>
<td align="left">212</td>
<td align="left">🟡 Outlaw</td>
<td align="left">Storm</td>
<td align="right"><b>1498</b></td>
<td align="right">22.6%</td>
<td align="right">40.3%</td>
<td align="right">29.3%</td>
<td align="right">22.6%</td>
<td align="right">20.0%</td>
<td align="right">14.4%</td>
<td align="right">2404</td>
</tr>
<tr>
<td align="left">213</td>
<td align="left">🟡 Insect</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">25.2%</td>
<td align="right">50.9%</td>
<td align="right">36.1%</td>
<td align="right">25.2%</td>
<td align="right">20.3%</td>
<td align="right">15.2%</td>
<td align="right">2100</td>
</tr>
<tr>
<td align="left">214</td>
<td align="left">🟡 Reborn</td>
<td align="left">Alliance</td>
<td align="right"><b>1497</b></td>
<td align="right">24.0%</td>
<td align="right">49.8%</td>
<td align="right">30.8%</td>
<td align="right">26.2%</td>
<td align="right">16.3%</td>
<td align="right">17.6%</td>
<td align="right">2487</td>
</tr>
<tr>
<td align="left">215</td>
<td align="left">🟡 Sniveler</td>
<td align="left">Incursion</td>
<td align="right"><b>1497</b></td>
<td align="right">23.2%</td>
<td align="right">46.9%</td>
<td align="right">30.9%</td>
<td align="right">23.0%</td>
<td align="right">19.6%</td>
<td align="right">15.0%</td>
<td align="right">2493</td>
</tr>
<tr>
<td align="left">216</td>
<td align="left">🟡 General</td>
<td align="left">Alliance</td>
<td align="right"><b>1497</b></td>
<td align="right">23.3%</td>
<td align="right">49.2%</td>
<td align="right">31.2%</td>
<td align="right">23.5%</td>
<td align="right">19.7%</td>
<td align="right">14.9%</td>
<td align="right">2576</td>
</tr>
<tr>
<td align="left">217</td>
<td align="left">🟡 Porcupine</td>
<td align="left">Storm</td>
<td align="right"><b>1497</b></td>
<td align="right">22.6%</td>
<td align="right">44.9%</td>
<td align="right">28.0%</td>
<td align="right">24.6%</td>
<td align="right">17.7%</td>
<td align="right">15.5%</td>
<td align="right">2462</td>
</tr>
<tr>
<td align="left">218</td>
<td align="left">🟡 Ace</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">23.2%</td>
<td align="right">44.5%</td>
<td align="right">31.9%</td>
<td align="right">24.1%</td>
<td align="right">17.9%</td>
<td align="right">16.6%</td>
<td align="right">2324</td>
</tr>
<tr>
<td align="left">219</td>
<td align="left">🟡 EvilTwin</td>
<td align="left">Eons</td>
<td align="right"><b>1497</b></td>
<td align="right">23.9%</td>
<td align="right">47.8%</td>
<td align="right">33.2%</td>
<td align="right">24.9%</td>
<td align="right">17.1%</td>
<td align="right">15.7%</td>
<td align="right">2226</td>
</tr>
<tr>
<td align="left">220</td>
<td align="left">🟡 Leviathan</td>
<td align="left">Incursion</td>
<td align="right"><b>1497</b></td>
<td align="right">24.1%</td>
<td align="right">47.1%</td>
<td align="right">31.0%</td>
<td align="right">26.8%</td>
<td align="right">19.3%</td>
<td align="right">15.9%</td>
<td align="right">2478</td>
</tr>
<tr>
<td align="left">221</td>
<td align="left">🟡 The Meek</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">24.3%</td>
<td align="right">49.5%</td>
<td align="right">29.2%</td>
<td align="right">26.0%</td>
<td align="right">19.3%</td>
<td align="right">17.0%</td>
<td align="right">2155</td>
</tr>
<tr>
<td align="left">222</td>
<td align="left">🟡 Crusher</td>
<td align="left">Eons</td>
<td align="right"><b>1497</b></td>
<td align="right">23.6%</td>
<td align="right">49.5%</td>
<td align="right">29.8%</td>
<td align="right">22.9%</td>
<td align="right">17.8%</td>
<td align="right">17.9%</td>
<td align="right">2249</td>
</tr>
<tr>
<td align="left">223</td>
<td align="left">🟡 Tentacle</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">23.4%</td>
<td align="right">43.3%</td>
<td align="right">31.1%</td>
<td align="right">23.7%</td>
<td align="right">20.5%</td>
<td align="right">15.0%</td>
<td align="right">2122</td>
</tr>
<tr>
<td align="left">224</td>
<td align="left">🟡 Greenhorn</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">24.0%</td>
<td align="right">44.3%</td>
<td align="right">32.1%</td>
<td align="right">23.9%</td>
<td align="right">20.2%</td>
<td align="right">16.1%</td>
<td align="right">2351</td>
</tr>
<tr>
<td align="left">225</td>
<td align="left">🟡 Sloth</td>
<td align="left">Storm</td>
<td align="right"><b>1497</b></td>
<td align="right">23.4%</td>
<td align="right">52.9%</td>
<td align="right">36.1%</td>
<td align="right">23.1%</td>
<td align="right">17.7%</td>
<td align="right">13.6%</td>
<td align="right">2382</td>
</tr>
<tr>
<td align="left">226</td>
<td align="left">🟡 Chronos</td>
<td align="left">Incursion</td>
<td align="right"><b>1497</b></td>
<td align="right">24.6%</td>
<td align="right">45.9%</td>
<td align="right">35.6%</td>
<td align="right">23.3%</td>
<td align="right">21.0%</td>
<td align="right">16.6%</td>
<td align="right">2439</td>
</tr>
<tr>
<td align="left">227</td>
<td align="left">🟡 Hunger</td>
<td align="left">Eons</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">49.1%</td>
<td align="right">32.4%</td>
<td align="right">21.8%</td>
<td align="right">16.9%</td>
<td align="right">15.2%</td>
<td align="right">2319</td>
</tr>
<tr>
<td align="left">228</td>
<td align="left">🟡 Architect</td>
<td align="left">Eons</td>
<td align="right"><b>1497</b></td>
<td align="right">23.4%</td>
<td align="right">45.1%</td>
<td align="right">32.4%</td>
<td align="right">24.9%</td>
<td align="right">16.1%</td>
<td align="right">15.9%</td>
<td align="right">2264</td>
</tr>
<tr>
<td align="left">229</td>
<td align="left">🟡 Schizoid</td>
<td align="left">Alliance</td>
<td align="right"><b>1497</b></td>
<td align="right">23.1%</td>
<td align="right">41.7%</td>
<td align="right">33.6%</td>
<td align="right">20.8%</td>
<td align="right">18.5%</td>
<td align="right">16.6%</td>
<td align="right">2454</td>
</tr>
<tr>
<td align="left">230</td>
<td align="left">🟡 Phantom</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">24.2%</td>
<td align="right">46.8%</td>
<td align="right">33.3%</td>
<td align="right">25.8%</td>
<td align="right">18.0%</td>
<td align="right">15.4%</td>
<td align="right">2149</td>
</tr>
<tr>
<td align="left">231</td>
<td align="left">🟡 Daredevil_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">23.6%</td>
<td align="right">44.6%</td>
<td align="right">29.9%</td>
<td align="right">20.4%</td>
<td align="right">20.4%</td>
<td align="right">17.8%</td>
<td align="right">2148</td>
</tr>
<tr>
<td align="left">232</td>
<td align="left">🟡 YinYang</td>
<td align="left">Dominion</td>
<td align="right"><b>1497</b></td>
<td align="right">22.7%</td>
<td align="right">44.8%</td>
<td align="right">28.7%</td>
<td align="right">23.5%</td>
<td align="right">18.5%</td>
<td align="right">17.1%</td>
<td align="right">2305</td>
</tr>
<tr>
<td align="left">233</td>
<td align="left">🟡 Lemming</td>
<td align="left">Odyssey</td>
<td align="right"><b>1497</b></td>
<td align="right">23.8%</td>
<td align="right">47.2%</td>
<td align="right">32.3%</td>
<td align="right">21.6%</td>
<td align="right">18.2%</td>
<td align="right">17.7%</td>
<td align="right">2064</td>
</tr>
<tr>
<td align="left">234</td>
<td align="left">🟡 Ethic</td>
<td align="left">Incursion</td>
<td align="right"><b>1496</b></td>
<td align="right">22.6%</td>
<td align="right">49.3%</td>
<td align="right">32.0%</td>
<td align="right">22.3%</td>
<td align="right">18.7%</td>
<td align="right">13.3%</td>
<td align="right">2483</td>
</tr>
<tr>
<td align="left">235</td>
<td align="left">🟡 Delegator</td>
<td align="left">Odyssey</td>
<td align="right"><b>1496</b></td>
<td align="right">23.6%</td>
<td align="right">46.6%</td>
<td align="right">29.3%</td>
<td align="right">23.5%</td>
<td align="right">18.1%</td>
<td align="right">17.0%</td>
<td align="right">2114</td>
</tr>
<tr>
<td align="left">236</td>
<td align="left">🟡 Nanny</td>
<td align="left">Eons</td>
<td align="right"><b>1496</b></td>
<td align="right">23.5%</td>
<td align="right">55.6%</td>
<td align="right">29.8%</td>
<td align="right">23.4%</td>
<td align="right">20.5%</td>
<td align="right">12.9%</td>
<td align="right">2275</td>
</tr>
<tr>
<td align="left">237</td>
<td align="left">🟡 Coward</td>
<td align="left">Eons</td>
<td align="right"><b>1496</b></td>
<td align="right">23.6%</td>
<td align="right">48.1%</td>
<td align="right">34.1%</td>
<td align="right">23.5%</td>
<td align="right">17.8%</td>
<td align="right">14.7%</td>
<td align="right">2279</td>
</tr>
<tr>
<td align="left">238</td>
<td align="left">🟡 Zombie_Alt</td>
<td align="left">Odyssey</td>
<td align="right"><b>1495</b></td>
<td align="right">23.6%</td>
<td align="right">41.7%</td>
<td align="right">34.3%</td>
<td align="right">23.3%</td>
<td align="right">20.9%</td>
<td align="right">14.6%</td>
<td align="right">2142</td>
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

