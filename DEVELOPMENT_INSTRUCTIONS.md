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
- **276 alien powers** implemented
- **Full encounter cycle** implemented (8 phases)
- **Multiple AI strategies** (5+ personalities)
- **ELO rating system** with persistent statistics

## Identified Gaps (Priority Order)

### High Priority
1. **Unit Tests** - No tests exist; add comprehensive test coverage
2. **Hazard Deck Integration** - File exists but not integrated into game flow
3. **Tech Cards Integration** - Cosmic Incursion expansion not fully implemented
4. **Power Interaction Edge Cases** - Complex power combos need testing

### Medium Priority
5. **Game.py Refactoring** - 1302 lines, could be split into phase modules
6. **Advanced Artifact Timing** - More robust artifact resolution
7. **Hyperspace Gate Mechanics** - Clarify and fully implement
8. **2-Player Variant** - Currently only 3-6 players supported

### Lower Priority
9. **Documentation** - Power descriptions, AI strategy rationale
10. **Performance Optimization** - Caching, vectorization for large runs
11. **Structured Logging** - Better debugging capabilities

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

---

*This document should be updated as development progresses.*
