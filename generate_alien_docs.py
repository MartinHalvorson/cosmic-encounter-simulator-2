#!/usr/bin/env python3
"""
Generate alphabetical alien documentation for README.
Extracts rules from docstrings and generates implementation descriptions.
"""

import sys
import re
import inspect
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from cosmic.aliens.registry import AlienRegistry
from cosmic.aliens.base import AlienPower, PowerCategory
from cosmic.types import PowerTiming, PowerType, PlayerRole

# Import all power modules to register them
import cosmic.aliens.powers.classic_powers
import cosmic.aliens.powers.special_powers
import cosmic.aliens.powers.more_powers
import cosmic.aliens.powers.advanced_powers
import cosmic.aliens.powers.exotic_powers
import cosmic.aliens.powers.legendary_powers
import cosmic.aliens.powers.cosmic_powers
import cosmic.aliens.powers.ultimate_powers
import cosmic.aliens.powers.combat_powers
import cosmic.aliens.powers.strategic_powers
import cosmic.aliens.powers.arcane_powers
import cosmic.aliens.powers.dominion_powers
import cosmic.aliens.powers.nature_powers
import cosmic.aliens.powers.tech_powers
import cosmic.aliens.powers.space_powers
import cosmic.aliens.powers.mythical_powers
import cosmic.aliens.powers.military_powers
import cosmic.aliens.powers.psychic_powers
import cosmic.aliens.powers.elemental_powers
import cosmic.aliens.powers.bonus_powers
import cosmic.aliens.powers.dimensional_powers
import cosmic.aliens.powers.time_powers
import cosmic.aliens.powers.energy_powers
import cosmic.aliens.powers.chaos_powers
import cosmic.aliens.powers.cosmic_entity_powers
import cosmic.aliens.powers.social_powers
import cosmic.aliens.powers.survival_powers
import cosmic.aliens.powers.stealth_powers
import cosmic.aliens.powers.economic_powers
import cosmic.aliens.powers.control_powers
import cosmic.aliens.powers.growth_powers
import cosmic.aliens.powers.destruction_powers
import cosmic.aliens.powers.defense_powers
import cosmic.aliens.powers.speed_powers
import cosmic.aliens.powers.luck_powers
import cosmic.aliens.powers.transformation_powers
import cosmic.aliens.powers.communication_powers
import cosmic.aliens.powers.deception_powers
import cosmic.aliens.powers.alliance_powers
import cosmic.aliens.powers.trap_powers
import cosmic.aliens.powers.territory_powers
import cosmic.aliens.powers.base_powers
import cosmic.aliens.powers.ancient_powers
import cosmic.aliens.powers.void_powers
import cosmic.aliens.powers.champion_powers
import cosmic.aliens.powers.predator_powers
import cosmic.aliens.powers.artifact_powers
import cosmic.aliens.powers.machine_powers
import cosmic.aliens.powers.beast_powers
import cosmic.aliens.powers.spirit_powers
import cosmic.aliens.powers.royal_powers
import cosmic.aliens.powers.card_powers

# Try to import additional modules if they exist
optional_modules = [
    "odyssey_alt_powers", "sky_powers", "gem_powers", "milestone_powers",
    "phenomenon_powers", "ocean_powers", "food_powers", "plant_powers",
    "insect_powers", "quantum_powers", "weather_alt_powers", "cosmic_horror_powers",
    "sound_powers", "science_powers", "sport_powers", "gravity_powers",
    "light_powers", "gaming_powers", "memory_powers", "math_powers",
    "magic_powers", "strategy_powers", "metal_powers", "gambling_powers",
    "mythology_powers", "direction_powers", "shape_powers", "cooking_powers",
    "celebration_powers", "architecture_powers", "philosophy_powers", "medical_powers",
    "theater_powers", "missing_official_powers", "expansion_powers", "age_powers",
    "color_powers", "number_powers", "climate_powers", "combat_modifier_powers",
    "card_manipulation_powers", "language_powers", "astronomy_powers", "texture_powers",
    "fauna_powers", "geography_powers", "action_powers", "weather_extreme_powers",
]

for mod_name in optional_modules:
    try:
        __import__(f"cosmic.aliens.powers.{mod_name}")
    except ImportError:
        pass


def get_timing_desc(timing: PowerTiming) -> str:
    """Get human-readable timing description."""
    timing_map = {
        PowerTiming.START_TURN: "at turn start",
        PowerTiming.REGROUP: "during regroup",
        PowerTiming.DESTINY: "when destiny is drawn",
        PowerTiming.LAUNCH: "during launch",
        PowerTiming.ALLIANCE: "during alliance",
        PowerTiming.PLANNING: "during planning",
        PowerTiming.REVEAL: "when cards are revealed",
        PowerTiming.RESOLUTION: "during resolution",
        PowerTiming.SHIPS_TO_WARP: "when ships go to warp",
        PowerTiming.ANY: "at any time",
        PowerTiming.WIN_ENCOUNTER: "when winning encounter",
        PowerTiming.LOSE_ENCOUNTER: "when losing encounter",
        PowerTiming.GAIN_CARDS: "when gaining cards",
        PowerTiming.CONSTANT: "constantly (passive)",
    }
    return timing_map.get(timing, "at appropriate time")


def get_role_desc(roles: list) -> str:
    """Get human-readable role description."""
    if len(roles) >= 5:
        return "in any role"
    role_names = []
    for r in roles:
        if r == PlayerRole.OFFENSE:
            role_names.append("offense")
        elif r == PlayerRole.DEFENSE:
            role_names.append("defense")
        elif r == PlayerRole.OFFENSIVE_ALLY:
            role_names.append("offensive ally")
        elif r == PlayerRole.DEFENSIVE_ALLY:
            role_names.append("defensive ally")
        elif r == PlayerRole.NOT_INVOLVED:
            role_names.append("bystander")
    if not role_names:
        return ""
    return "as " + "/".join(role_names)


def generate_implementation_desc(power: AlienPower) -> str:
    """Generate a 20-40 word implementation description."""
    timing_desc = get_timing_desc(power.timing)
    role_desc = get_role_desc(power.usable_as)
    power_kind = "mandatory" if power.power_type == PowerType.MANDATORY else "optional"
    category = power.category.name.lower()

    # Build description
    parts = []
    parts.append(f"Implemented as a {category}-tier {power_kind} power that triggers {timing_desc}")
    if role_desc and "any role" not in role_desc:
        parts.append(role_desc)
    parts.append(f". {power.description}")

    desc = " ".join(parts)

    # Ensure 20-40 words
    words = desc.split()
    if len(words) > 45:
        desc = " ".join(words[:42]) + "..."

    return desc


def extract_rules(power: AlienPower) -> str:
    """Extract rules from docstring."""
    doc = power.__class__.__doc__
    if not doc:
        return power.description

    # Clean up docstring
    lines = doc.strip().split('\n')
    # Skip the first line (name - subtitle)
    if len(lines) > 1:
        rules = ' '.join(line.strip() for line in lines[1:] if line.strip())
    else:
        rules = lines[0].strip()

    return rules or power.description


def main():
    # Get all registered aliens
    aliens = AlienRegistry.get_all()

    # Sort alphabetically by name
    sorted_aliens = sorted(aliens, key=lambda a: a.name.lower())

    print(f"Found {len(sorted_aliens)} aliens")

    # Generate markdown
    lines = []
    lines.append("\n## Alien Power Reference\n")
    lines.append(f"> Alphabetical listing of all {len(sorted_aliens)} alien powers with rules and implementation details.\n")
    lines.append("")

    for power in sorted_aliens:
        rules = extract_rules(power)
        impl_desc = generate_implementation_desc(power)

        lines.append(f"### {power.name}\n")
        lines.append(f"**Rules:** {rules}\n")
        lines.append(f"**Implementation:** {impl_desc}\n")
        lines.append("")

    # Write to file
    output = "\n".join(lines)
    output_file = Path(__file__).parent / "alien_reference.md"
    output_file.write_text(output)
    print(f"Written to {output_file}")

    # Also print first few for verification
    print("\n--- First 5 entries ---")
    print("\n".join(lines[:30]))


if __name__ == "__main__":
    main()
