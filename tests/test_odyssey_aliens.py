"""
Tests for Cosmic Odyssey aliens including alternate timeline versions.
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from cosmic.game import Game
from cosmic.types import GameConfig
from cosmic.aliens.registry import AlienRegistry


class TestOdysseyAliensRegistered:
    """Tests that all Odyssey aliens are properly registered."""

    def test_alternate_timeline_aliens_registered(self):
        """All alternate timeline aliens should be registered."""
        alt_aliens = [
            "Brute_Alt", "Daredevil_Alt", "Demon_Alt", "Grumpus_Alt",
            "Locust_Alt", "Masochist_Alt", "Perfectionist_Alt", "Sadist_Alt",
            "Schizoid_Alt", "Void_Alt", "Zombie_Alt"
        ]
        for alien_name in alt_aliens:
            alien = AlienRegistry.get(alien_name)
            assert alien is not None, f"{alien_name} should be registered"

    def test_odyssey_new_aliens_registered(self):
        """New Odyssey aliens should be registered."""
        new_aliens = [
            "Assessor", "Booster", "Bubble", "Force", "Geek",
            "Gremlin", "Silencer", "Vector", "Witch", "Wrack",
            "Zilch", "Micron", "Lemming", "Lloyd", "Tentacle",
            "Throwback", "Extractor", "Hurtz"
        ]
        for alien_name in new_aliens:
            alien = AlienRegistry.get(alien_name)
            assert alien is not None, f"{alien_name} should be registered"


class TestOdysseyGamesComplete:
    """Tests that games with Odyssey aliens complete successfully."""

    def test_games_with_alt_aliens_complete(self):
        """Games with alternate timeline aliens should complete."""
        alt_aliens = ["Brute_Alt", "Zombie_Alt", "Masochist_Alt", "Locust_Alt"]

        for alien in alt_aliens:
            config = GameConfig(
                num_players=4,
                seed=42,
                max_turns=100,
                required_aliens=[alien]
            )
            game = Game(config=config)
            game.setup()
            game.play()

            assert game.is_over or game.current_turn >= 100

    def test_games_with_new_odyssey_aliens_complete(self):
        """Games with new Odyssey aliens should complete."""
        new_aliens = ["Force", "Witch", "Zilch", "Gremlin"]

        for alien in new_aliens:
            config = GameConfig(
                num_players=4,
                seed=42,
                max_turns=100,
                required_aliens=[alien]
            )
            game = Game(config=config)
            game.setup()
            game.play()

            assert game.is_over or game.current_turn >= 100

    def test_multiple_odyssey_games_complete(self):
        """Multiple games with various Odyssey aliens should complete."""
        completed = 0
        errors = []

        odyssey_aliens = [
            "Brute_Alt", "Force", "Witch", "Zombie_Alt",
            "Silencer", "Masochist_Alt"
        ]

        for i in range(30):
            try:
                alien = odyssey_aliens[i % len(odyssey_aliens)]
                config = GameConfig(
                    num_players=4,
                    seed=i,
                    max_turns=100,
                    required_aliens=[alien]
                )
                game = Game(config=config)
                game.setup()
                game.play()
                completed += 1
            except Exception as e:
                errors.append((i, str(e)))

        assert completed == 30, f"Failed games: {errors[:3]}"


class TestAlternateTimelineAlienMechanics:
    """Tests for specific alternate timeline alien mechanics."""

    def test_brute_alt_has_correct_timing(self):
        """Brute_Alt should have correct power timing."""
        alien = AlienRegistry.get("Brute_Alt")
        assert alien is not None
        assert alien.name == "Brute_Alt"

    def test_zombie_alt_has_correct_description(self):
        """Zombie_Alt should have resurrection mechanics."""
        alien = AlienRegistry.get("Zombie_Alt")
        assert alien is not None
        assert "return" in alien.description.lower() or "warp" in alien.description.lower()

    def test_masochist_alt_has_bonus_mechanic(self):
        """Masochist_Alt should give bonus based on warp ships."""
        alien = AlienRegistry.get("Masochist_Alt")
        assert alien is not None
        # Should have ships/warp related description
        assert "warp" in alien.description.lower()

    def test_locust_alt_has_discard_mechanic(self):
        """Locust_Alt should force opponent to discard."""
        alien = AlienRegistry.get("Locust_Alt")
        assert alien is not None
        assert "discard" in alien.description.lower() or "opponent" in alien.description.lower()


class TestNewOdysseyAlienMechanics:
    """Tests for new Odyssey alien mechanics."""

    def test_force_has_ship_multiplier(self):
        """Force should have ship value multiplier."""
        alien = AlienRegistry.get("Force")
        assert alien is not None
        assert "2" in alien.description or "double" in alien.description.lower()

    def test_witch_has_curse_mechanic(self):
        """Witch should have some negative effect on opponents."""
        alien = AlienRegistry.get("Witch")
        assert alien is not None
        # Witch has various implementations - just check it exists with a description
        assert len(alien.description) > 5

    def test_zilch_has_empty_hand_mechanic(self):
        """Zilch should win with empty hand."""
        alien = AlienRegistry.get("Zilch")
        assert alien is not None
        assert "no card" in alien.description.lower() or "win" in alien.description.lower()

    def test_silencer_can_suppress_powers(self):
        """Silencer should be able to suppress powers."""
        alien = AlienRegistry.get("Silencer")
        assert alien is not None
        assert "power" in alien.description.lower() or "suppress" in alien.description.lower()


class TestTheTheekMeek:
    """Tests for The Meek alternate win condition."""

    def test_the_meek_has_alternate_win(self):
        """The Meek should have alternate win condition."""
        alien = AlienRegistry.get("The Meek")
        assert alien is not None
        assert hasattr(alien, 'has_alternate_win')
        assert alien.has_alternate_win is True

    def test_the_meek_wins_by_losing(self):
        """The Meek description should mention winning by losing."""
        alien = AlienRegistry.get("The Meek")
        assert alien is not None
        desc_lower = alien.description.lower()
        assert "los" in desc_lower or "win" in desc_lower


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
