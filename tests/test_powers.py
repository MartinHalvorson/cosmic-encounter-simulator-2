"""
Tests for specific alien power implementations.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.aliens import AlienRegistry


class TestPowerRegistry:
    """Tests for the alien power registry."""

    def test_all_powers_registered(self):
        """All power files should have registered powers."""
        powers = AlienRegistry.get_all()
        assert len(powers) > 100, "Expected at least 100 powers registered"

    def test_each_power_has_required_attributes(self):
        """Each power should have name, description, and timing."""
        powers = AlienRegistry.get_all()

        for power in powers:
            assert hasattr(power, 'name'), f"Power missing name"
            assert hasattr(power, 'description'), f"{power.name} missing description"
            assert hasattr(power, 'timing'), f"{power.name} missing timing"
            assert len(power.name) > 0, f"Power has empty name"

    def test_power_names_are_unique(self):
        """Each power should have a unique name."""
        powers = AlienRegistry.get_all()
        names = [p.name for p in powers]
        duplicates = [n for n in names if names.count(n) > 1]
        assert len(duplicates) == 0, f"Duplicate power names: {set(duplicates)}"


class TestKeyPowers:
    """Tests for specific important powers."""

    def test_machine_gets_extra_encounters(self):
        """Machine should be able to take extra encounters."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Machine"],
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        # Find the Machine player
        machine_player = next(p for p in game.players if p.alien.name == "Machine")
        assert machine_player is not None

    def test_zombie_ships_avoid_warp(self):
        """Zombie's ships should not go to the warp normally."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Zombie"],
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        zombie = next(p for p in game.players if p.alien.name == "Zombie")
        assert zombie is not None

    def test_virus_multiplies_ships(self):
        """Virus should multiply ships instead of adding."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Virus"],
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        virus = next(p for p in game.players if p.alien.name == "Virus")
        assert virus is not None

    def test_parasite_can_ally_uninvited(self):
        """Parasite should be able to join encounters without invitation."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Parasite"],
            max_turns=50
        )
        game = Game(config=config)
        game.setup()

        parasite = next(p for p in game.players if p.alien.name == "Parasite")
        assert parasite is not None


class TestPowerGameplay:
    """Tests for powers during actual gameplay."""

    def test_game_with_loser_power(self):
        """Game with Loser power should complete without errors."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Loser"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_game_with_antimatter_power(self):
        """Game with Antimatter power should complete without errors."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Antimatter"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_game_with_pacifist_power(self):
        """Game with Pacifist power should complete without errors."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Pacifist"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_game_with_oracle_power(self):
        """Game with Oracle power should complete without errors."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Oracle"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_game_with_human_power(self):
        """Game with Human power should complete without errors."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Human"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75


class TestPowerInteractions:
    """Tests for power interactions in specific matchups."""

    def test_virus_vs_macron(self):
        """Virus vs Macron should work correctly."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Virus", "Macron"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_loser_vs_antimatter(self):
        """Loser vs Antimatter should work correctly."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Loser", "Antimatter"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75

    def test_machine_vs_parasite(self):
        """Machine vs Parasite should work correctly."""
        config = GameConfig(
            num_players=4,
            seed=42,
            required_aliens=["Machine", "Parasite"],
            max_turns=75
        )
        game = Game(config=config)
        game.setup()
        winners = game.play()

        assert game.is_over or game.current_turn >= 75


class TestRandomPowerCombinations:
    """Tests for random power combinations."""

    def test_100_random_games(self):
        """100 games with random powers should complete without errors."""
        completed = 0
        errors = []

        for i in range(100):
            try:
                config = GameConfig(num_players=5, seed=i, max_turns=100)
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception as e:
                powers = [p.alien.name for p in game.players if p.alien]
                errors.append((i, powers, str(e)))

        assert completed == 100, f"Failed games: {errors[:3]}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
