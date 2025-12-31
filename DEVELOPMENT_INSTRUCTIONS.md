# Development Instructions

## Mission

Build out a comprehensive Cosmic Encounter simulator to simulate games under various start conditions (player count, powers in game). Model the game as closely as possible to the official rules, making reasonable decisions throughout. Document decisions and commit/push regularly.

## Goals

1. **Accurate Game Modeling** - Simulate Cosmic Encounter mechanics as faithfully as possible
2. **Variable Configurations** - Support different player counts (2-6+) and power combinations
3. **Statistical Analysis** - Track win rates, power balance, game dynamics
4. **Continuous Improvement** - Identify gaps and systematically build out features

## Current State (as of 2025-12-30)

- **5+ million games simulated**
- **317 alien powers** implemented
- **Full encounter cycle** implemented (8 phases)
- **Multiple AI strategies** (5+ personalities)
- **ELO rating system** with persistent statistics
- **Tech Cards system** integrated (Cosmic Incursion expansion)
- **Hazard Deck system** integrated (Cosmic Storm expansion)
- **46 unit tests** with pytest framework

## Identified Gaps (Priority Order)

### Completed
1. ~~**Unit Tests**~~ - Added 46 tests covering game, expansions, and powers
2. ~~**Hazard Deck Integration**~~ - Fully integrated into game flow
3. ~~**Tech Cards Integration**~~ - Fully integrated with research progress
4. ~~**Power Interaction Edge Cases**~~ - Added tests for key matchups

### Medium Priority
5. **Game.py Refactoring** - 1486 lines, could be split into phase modules
6. **Advanced Artifact Timing** - More robust artifact resolution
7. **Hyperspace Gate Mechanics** - Clarify and fully implement
8. **2-Player Variant** - Currently only 3-6 players supported
9. **AI Strategy Improvements** - More power-aware decision making

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
- Integrated Hazard Deck system (Cosmic Storm expansion)
  - Hazard drawing at encounter start
  - Immediate and timed hazard effects
  - Skip encounter hazards
  - No-alliance hazards
- Fixed edge case in _handle_turn_end when encounters are skipped
- Verified 317 alien powers are registered and working
- Ran 500+ test games with no errors
- All 46 tests passing

---

*This document should be updated as development progresses.*
