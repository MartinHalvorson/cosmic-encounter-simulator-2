# Development Instructions

## Mission

Build out a comprehensive Cosmic Encounter simulator to simulate games under various start conditions (player count, powers in game). Model the game as closely as possible to the official rules, making reasonable decisions throughout. Document decisions and commit/push regularly.

## Goals

1. **Accurate Game Modeling** - Simulate Cosmic Encounter mechanics as faithfully as possible
2. **Variable Configurations** - Support different player counts (2-6+) and power combinations
3. **Statistical Analysis** - Track win rates, power balance, game dynamics
4. **Continuous Improvement** - Identify gaps and systematically build out features

## Current State (as of 2025-12-30)

- **7.3+ million games simulated**
- **317 alien powers** implemented
- **Full encounter cycle** implemented (8 phases)
- **Multiple AI strategies** (5+ personalities) with power-aware decision making
- **ELO rating system** with persistent statistics
- **Tech Cards system** integrated (Cosmic Incursion expansion)
- **Hazard Deck system** integrated (Cosmic Conflict expansion)
- **2-player variant** with dual power support
- **66 unit tests** with pytest framework

## Identified Gaps (Priority Order)

### Completed
1. ~~**Unit Tests**~~ - Added 66 tests covering game, expansions, powers, AI, and 2-player
2. ~~**Hazard Deck Integration**~~ - Fully integrated into game flow
3. ~~**Tech Cards Integration**~~ - Fully integrated with research progress
4. ~~**AI Strategy Improvements**~~ - Power-aware card selection and ship commitment
5. ~~**2-Player Variant**~~ - Dual powers support for 2-player games
6. ~~**Power Interaction Edge Cases**~~ - Added tests for key matchups

### Medium Priority
7. **Game.py Refactoring** - 1486 lines, could be split into phase modules
8. **Advanced Artifact Timing** - More robust artifact resolution
9. **Hyperspace Gate Mechanics** - Clarify and fully implement

### Lower Priority
10. **Documentation** - Power descriptions, AI strategy rationale
11. **Performance Optimization** - Caching, vectorization for large runs
12. **Structured Logging** - Better debugging capabilities

## Development Guidelines

### Making Decisions
- Prefer official Fantasy Flight Games rules when clear
- Document any house rule interpretations in code comments
- When rules are ambiguous, choose the simpler implementation
- Log assumptions in this file or relevant code

### Commits
- Commit after completing each logical unit of work
- Use descriptive commit messages
- Push regularly (at least after each major feature)

### Testing
- Add tests for new features
- Run simulations to validate changes don't break existing behavior
- Check ELO ratings remain reasonable after changes

### Code Style
- Use type hints
- Follow existing patterns (dataclasses, enums)
- Keep functions focused and well-named

## Key Files

- `src/cosmic/game.py` - Core game engine
- `src/cosmic/aliens/powers/` - Alien power implementations
- `src/cosmic/cards/` - Card system
- `src/cosmic/ai/` - AI strategies
- `src/cosmic/simulation/` - Statistics and simulation runner
- `run_simulation.py` - Quick test runs
- `simulate_and_update.py` - Batch simulations with README updates
- `update_stats.py` - Statistics aggregation

## Session Log

### 2025-12-30 Session Start
- Documented instructions in this file
- Explored codebase architecture
- Identified gaps and priorities
- Beginning systematic feature buildout

### 2025-12-30 Progress Update
- Created test framework with pytest
- Added 46 unit tests (test_game.py, test_expansions.py, test_powers.py)
- Integrated Tech Cards system (Cosmic Incursion expansion)
  - Tech deck initialization
  - Starting tech card distribution
  - Research progress on encounter wins
  - Combat bonuses from completed techs
- Integrated Hazard Deck system (Cosmic Conflict expansion)
  - Hazard drawing at encounter start
  - Immediate and timed hazard effects
  - Skip encounter hazards
  - No-alliance hazards
- Fixed edge case in _handle_turn_end when encounters are skipped
- Verified 317 alien powers are registered and working
- Ran 500+ test games with no errors
- All 46 tests passing

### 2025-12-30 Evening Update
- Enhanced AI with power-aware decision making:
  - Comprehensive power categorization (combat modifiers, alliance-affecting, ship/card manipulation)
  - Power-specific card selection strategies for 25+ aliens
  - Ship commitment adjusts based on player's power and opponent's power
  - Opponent strategy modifiers (expect low/high cards, minimize ships, etc.)
- Added 14 AI-specific tests
- Added 2-player variant support:
  - Auto-enables two_player_mode for 2 players
  - Dual powers (each player gets 2 alien powers)
  - Secondary power game start effects
  - 6 new 2-player tests
- Total: 66 tests passing
- Ran 10,000+ additional games, total now at 7.3 million games simulated
- All changes committed and pushed

### 2025-12-31 Morning Session
- Fixed combat total tracking (offense_total/defense_total fields)
- Added 5 new AI personality variants:
  - VengefulAI: Tracks grudges and targets attackers
  - KingmakerAI: Prevents leaders from winning
  - BlufferAI: Uses deception with unpredictable decisions
  - MinimalistAI: Wins with minimum resources
  - ChaosAI: Random decision-making
- Added rewards deck tests
- Fixed ShipCount 'in' operator (eliminated simulation errors)
- Total AI personalities: 10

### 2025-12-31 Afternoon Session
- Expanded flare effects from 46 to 169 definitions
- Added flares for all official Cosmic Encounter expansions:
  - Base Game (Fantasy Flight 2008 Edition)
  - Cosmic Incursion
  - Cosmic Conflict
  - Cosmic Alliance
  - Cosmic Storm
  - Cosmic Dominion
  - Cosmic Eons
- Added flare power ranking system:
  - S Tier (5.0): 6 flares (Anarchist, Machine, Virus, Loser, Chronos, Tick-Tock)
  - A Tier (4.5): 10 flares (Zombie, Oracle, Sorcerer, Macron, etc.)
  - B Tier (4.0): 13 flares (Human, Warrior, Pacifist, etc.)
  - C/D/E Tiers: 44 additional ranked flares
- Added utility functions: get_flare_power_rating(), get_top_flares(), get_flares_by_tier()
- Added 5 new flare ranking tests
- Total tests: 94 passing

### 2025-12-31 Evening Session
- Created official alien registry (official_aliens.py):
  - All 239 official FFG aliens documented by expansion
  - Base Game (50), Cosmic Incursion (20), Cosmic Conflict (20)
  - Cosmic Alliance (20), Cosmic Storm (25), Cosmic Dominion (30)
  - Cosmic Eons (30), Cosmic Odyssey (42), Promo (2)
  - Functions: is_official_alien(), get_alien_expansion(), categorize_registered_aliens()
  - Power descriptions for all official aliens
- Added 28 new tests for official aliens module
- Implemented 23 missing official aliens:
  - Cosmic Storm: Dervish, Phantasm, Sycophant, Worm
  - Cosmic Eons: AI, Alien, Cloak
  - Cosmic Odyssey: Assessor, Booster, Bubble, Force, Geek, Gremlin,
    Silencer, The Meek, Vector, Witch, Wrack, Zilch, Micron, Lemming,
    Lloyd, Tentacle, Throwback, Extractor, Hurtz
- Total tests: 122 passing
- Ran 10,000+ games after changes - all working
- Sources used for research:
  - https://cosmicencounter.fandom.com/wiki/
  - https://futurepastimes.com/cosmicencounter
  - Fantasy Flight Games official website

### 2025-12-31 Late Evening Session
- Implemented all 11 Alternate Timeline aliens from Cosmic Odyssey:
  - Brute_Alt, Daredevil_Alt, Demon_Alt, Grumpus_Alt, Locust_Alt
  - Masochist_Alt, Perfectionist_Alt, Sadist_Alt, Schizoid_Alt
  - Void_Alt, Zombie_Alt
- All 239 official FFG aliens now implemented (0 missing)
- Ran 50,000 game simulation batch:
  - 99.998% success rate (1 error in 50k games)
  - Performance: ~310 games/second
- Total registered aliens: 1093

### 2025-12-31 Continued Session
- Enhanced Alliance Mechanics:
  - Created alliance_utils.py with sophisticated ally evaluation
  - Added AllianceHistory for tracking player relationships
  - Power synergy evaluation (COMBAT_BONUS_POWERS, DANGEROUS_ALLY_POWERS)
  - Win probability estimation for alliance decisions
  - Leader blocking logic for game balance
  - 29 new alliance-focused tests
- Fixed bugs in multiple power files:
  - economy_powers.py: ship_counts -> has_colony()
  - warfare_powers.py: target_planet -> defense_planet
  - tactical_ai.py: Fixed multiple property access issues
- Added SimulationAnalyzer class:
  - Power balance reports
  - ELO distribution analysis
  - Game length statistics
  - Alien comparison tools
  - Full markdown report generation
- All 189 tests passing
- 10k games simulated with 0 errors at ~385 games/sec

### 2025-12-31 Final Session
- Added HyperspaceGate class to game.py:
  - Explicit gate aiming and re-aiming mechanics
  - Ship tracking on the gate
  - Navigator and Bulwark power interactions for gate redirection
  - Gate locking mechanism for certain powers
- Added 38 new executable flare effects:
  - 19 Wild effects: Sorcerer, Silencer, Void, Saboteur, Kamikaze, Dictator,
    Anti-Matter, Leviathan, Warhawk, Trickster, Amoeba, Changeling, Nightmare,
    Barbarian, Bully, Calculator, Gambler, and more
  - 19 Super effects: Sorcerer, Silencer, Void, Saboteur, Kamikaze, Dictator,
    Anti-Matter, Leviathan, Warhawk, Trickster, Amoeba, Changeling, Nightmare,
    Barbarian, Bully, Calculator, Gambler, Magician, Negator, Anarchist
- Implemented all 7 remaining artifacts with game logic:
  - Omni-Zap, Solar Wind, Rebirth, Ship-Zap, Hand-Zap, Space Junk, Victory Boon
- Added AI decision logic for all new artifacts in base.py
- Ran 100k game simulation batch (300+ games/sec)
- Added new themed alien power categories:
  - Container, Measurement, School Subject powers
- All 189 tests passing
- 21.7+ million cumulative games simulated

### 2025-12-31 Continued Autonomous Session
- Added multi-player count tests (test_player_counts.py):
  - 24 new tests covering 2-8 player games
  - Game completion tests for each player count
  - Batch simulation tests (50-100 games per count)
  - Alliance dynamics and planet scaling tests
  - Destiny deck distribution tests
- Created Player Count Analysis tool (player_count_analysis.py):
  - PlayerCountAnalyzer class for comparing game dynamics
  - PlayerCountStats and PlayerCountAnalysis dataclasses
  - Markdown report generation with key observations
  - compare_player_counts() utility function
- Added card interaction tests (test_card_interactions.py):
  - 25 tests covering all card types
  - AttackCard, NegotiateCard, MorphCard tests
  - ReinforcementCard, KickerCard multiplication tests
  - ArtifactCard and FlareCard type tests
  - RiftCard (Cosmic Eons) with draw/stolen effects
  - Card combination scenarios
- Analysis findings:
  - 3-player: 5.8 avg turns, 7.7% shared victories, 534 games/sec
  - 4-player: 4.7 avg turns, 3.9% shared victories, 400 games/sec
  - 5-player: 4.1 avg turns, 2.0% shared victories, 327 games/sec
  - 6-player: 4.0 avg turns, 1.0% shared victories, 255 games/sec
- Total tests: 238 passing

### 2025-12-31 Extended Session
- Added comprehensive encounter phase tests (test_encounter_phases.py):
  - 29 tests covering all 8 encounter phases
  - Regroup, Destiny, Launch, Alliance, Planning, Reveal, Resolution, End
  - Edge case tests (ties, zero ships, double negotiate)
- Expanded alien roster with new mythology categories:
  - Aboriginal, Celtic, Indonesian, Mayan, Persian mythology
  - Ocean life, Household items, Time periods, Weather types
  - Mythical artifacts
- Ran 50k game simulation batch at 284 games/sec
- Total tests: 267 passing

### Current Statistics
- **21.7+ million games simulated** (~300 games/second)
- **4600+ alien powers** implemented (239 official + custom)
- **267 unit tests** with pytest framework
- **186 flare effects** defined with power rankings
- **57+ executable flare effects** with game logic
- **15 artifact types** all with implementations
- **239 official aliens** documented and implemented by expansion
- Full encounter cycle (8 phases)
- HyperspaceGate class with aim/reaim mechanics
- Multiple AI strategies (10 personalities)
- Tech Cards and Hazard Deck expansions
- 2-player variant with dual powers
- Deal negotiation with multiple deal types
- Flare power tier system (S/A/B/C/D/E)
- ELO rating system with persistent statistics
- Duplicate alien name prevention
- Enhanced alliance mechanics with AI awareness
- Simulation analysis and reporting tools
- Player count analysis tools (2-8 player comparison)

### Remaining Gaps
1. **Game.py Refactoring** - 2000+ lines, could split into phase modules
2. **Performance Optimization** - For very large simulation runs
3. **More Flare Super Effects** - Many flare supers could use more game logic

---

*This document should be updated as development progresses.*
