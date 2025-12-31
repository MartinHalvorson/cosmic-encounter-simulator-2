# Cosmic Encounter Simulator 2 - Development Instructions

## Project Goals

Build a comprehensive simulator for the board game Cosmic Encounter with the following objectives:

1. **Simulate games under various start conditions**
   - Variable number of players (3-8)
   - Configurable alien powers per game
   - Different game variants and rules

2. **Model the game as closely as possible**
   - Full encounter flow (Regroup, Destiny, Launch, Alliance, Planning, Reveal, Resolution)
   - All card types (Attack, Negotiate, Morph, Reinforcement, Artifact, Flare)
   - Destiny deck mechanics
   - Rewards deck mechanics
   - Ship management (colonies, warp, hyperspace gate)
   - Win conditions (5 foreign colonies, alternate win conditions)

3. **Implement comprehensive alien powers**
   - Target: 50+ alien powers from base game and expansions
   - Properly handle power timing and interactions
   - Support for power activation/deactivation

4. **Intelligent AI decision-making**
   - Strategic card selection
   - Alliance invitation and acceptance logic
   - Power usage optimization
   - Multiple AI strategy profiles

5. **Robust statistics and analysis**
   - Win rates by alien power
   - Win rates by player count
   - Power interaction matrices
   - Game length statistics
   - Export capabilities (CSV, JSON)

## Key Design Decisions

### Architecture
- Modern Python package structure with clear separation of concerns
- Type hints throughout for better code quality
- Dataclasses for game state representation
- Event-driven system for power triggers
- Pluggable AI strategy system

### Game Modeling
- Follow FFG Cosmic Encounter (2008+) rules as primary reference
- Support house rules as optional configuration
- Handle shared victories
- Support alternate win conditions

### Simulation
- Configurable random seed for reproducibility
- Batch simulation support
- Progress reporting for long simulations
- Error handling with game state logging

## File Structure

```
cosmic-encounter-simulator/
├── src/
│   └── cosmic/
│       ├── __init__.py
│       ├── game.py           # Main Game class
│       ├── player.py         # Player class
│       ├── cards/
│       │   ├── __init__.py
│       │   ├── base.py       # Card base classes
│       │   ├── cosmic_deck.py
│       │   ├── destiny_deck.py
│       │   ├── rewards_deck.py
│       │   └── flare_deck.py
│       ├── aliens/
│       │   ├── __init__.py
│       │   ├── base.py       # Alien power base class
│       │   ├── registry.py   # Power registration
│       │   └── powers/       # Individual power implementations
│       ├── phases/
│       │   ├── __init__.py
│       │   ├── regroup.py
│       │   ├── destiny.py
│       │   ├── launch.py
│       │   ├── alliance.py
│       │   ├── planning.py
│       │   ├── reveal.py
│       │   └── resolution.py
│       ├── ai/
│       │   ├── __init__.py
│       │   ├── base.py       # AI strategy interface
│       │   ├── random_ai.py
│       │   ├── basic_ai.py
│       │   └── strategic_ai.py
│       ├── simulation/
│       │   ├── __init__.py
│       │   ├── runner.py     # Simulation runner
│       │   └── stats.py      # Statistics collection
│       └── utils/
│           ├── __init__.py
│           └── logging.py
├── tests/
│   └── ...
├── main.py
├── INSTRUCTIONS.md
└── README.md
```

## Commit and Push Schedule

- Commit after completing each major component
- Push regularly to preserve progress
- Use descriptive commit messages

## Reference Materials

- Cosmic Encounter Rulebook (FFG 2008)
- BoardGameGeek Cosmic Encounter page
- Existing simulator code in Simulator.py

## Progress Tracking

Use the todo list to track progress through each component. Mark tasks complete as they are finished.

---

## Autonomous Development Session (2025-12-30)

### Instructions from User
1. **Work autonomously for extended period** - Build out the simulator comprehensively
2. **Model the game as closely as possible** - Research and implement accurate rules
3. **Use best judgment for AI decision-making** - Build intelligent, strategic AI
4. **Regularly run simulations** - Update the README table with fresh statistics
5. **Commit and push regularly** - Preserve progress frequently
6. **Document decisions** - Keep track of reasoning and changes

### Session Goals
- [x] Create cumulative statistics system with JSON persistence
- [x] Add ELO rating system for alien power balance tracking
- [x] Create simulate_and_update.py for automated README updates
- [x] Update README with simulation results table
- [x] Implement Reinforcement card usage during combat
- [x] Improve alliance and negotiation mechanics (defensive ally reward choice)
- [x] Enhance AI decision making (reinforcement strategy, ally rewards)
- [x] Add more alien powers - NOW AT 129 POWERS!
- [x] Regular simulation runs with statistics updates (22,000 games)
- [x] Commit and push after each major milestone
- [ ] Add Artifact card timing and usage
- [ ] Add Flare card system

### Key Rules Researched
From official FFG rules and BoardGameGeek:

**Eight Encounter Phases:**
1. Start Turn - Check for encounter cards, draw if needed
2. Regroup - Retrieve one ship from warp to any colony
3. Destiny - Draw destiny card to determine defender
4. Launch - Select planet and commit 1-4 ships
5. Alliance - Both sides invite, players accept in clockwise order
6. Planning - Secretly select encounter cards
7. Reveal - Reveal cards and trigger powers
8. Resolution - Determine winner, move ships, award rewards

**Alliance Rewards (Defense Only):**
- For each ship committed: draw 1 card OR retrieve 1 ship from warp

**Compensation:**
- When losing with Negotiate vs Attack: draw cards equal to ships lost to warp

**Failed Deal Penalty:**
- Both Negotiate cards: 1 minute to deal, or both lose 3 ships to warp

**Second Encounter:**
- Allowed if: (1) won or dealt first encounter, AND (2) have encounter cards

### Session Progress Log

**Session Start (2025-12-30):**
- Began with 68 alien powers
- Created update_stats.py and ELO rating system
- Ran initial simulations

**Mid-Session:**
- Added reinforcement card support to combat
- Implemented defensive ally reward choices (cards OR ships)
- Added 61 new alien powers (now at 129 total)
- Ran 22,000+ simulated games

**Current Stats:**
- 129 alien powers implemented
- 22,000+ games simulated across 3-6 players
- ELO ratings stable with meaningful tier differentiation
- Top powers: Machine, Parasite, Disease, Warpish
