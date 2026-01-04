"""
Official Cosmic Encounter aliens organized by expansion.

This file documents all official Fantasy Flight Games aliens from:
- Base Game (2008): 50 aliens
- Cosmic Incursion (2010): 20 aliens
- Cosmic Conflict (2011): 20 aliens
- Cosmic Alliance (2012): 20 aliens
- Cosmic Storm (2013): 25 aliens
- Cosmic Dominion (2014): 30 aliens
- Cosmic Eons (2016): 30 aliens
- Cosmic Odyssey (2022): 42 aliens (31 new + 11 alternate timeline versions)
- Promos: 1 alien (Demon)

Total official: 238 aliens

Sources:
- https://cosmicencounter.fandom.com/wiki/Cosmic_Encounter_(FFG)
- https://futurepastimes.com/cosmicencounter
- Fantasy Flight Games official website
"""

from typing import Dict, List, Set, Optional

from ..types import Expansion

# Mapping from expansion string names to Expansion enum
EXPANSION_NAME_TO_ENUM: Dict[str, Expansion] = {
    "Base Game": Expansion.BASE,
    "Cosmic Incursion": Expansion.COSMIC_INCURSION,
    "Cosmic Conflict": Expansion.COSMIC_CONFLICT,
    "Cosmic Alliance": Expansion.COSMIC_ALLIANCE,
    "Cosmic Storm": Expansion.COSMIC_STORM,
    "Cosmic Dominion": Expansion.COSMIC_DOMINION,
    "Cosmic Eons": Expansion.COSMIC_EONS,
    "Cosmic Odyssey": Expansion.COSMIC_ODYSSEY,
    "Promo": Expansion.BASE,  # Promos count as base game
}

# Official aliens by expansion
OFFICIAL_ALIENS: Dict[str, List[str]] = {
    "Base Game": [
        "Amoeba", "Anti-Matter", "Barbarian", "Calculator", "Chosen", "Citadel",
        "Clone", "Cudgel", "Dictator", "Fido", "Filch", "Fodder", "Gambler",
        "Grudge", "Hacker", "Hate", "Healer", "Human", "Kamikaze", "Loser",
        "Machine", "Macron", "Masochist", "Mind", "Mirror", "Miser", "Mite",
        "Mutant", "Observer", "Oracle", "Pacifist", "Parasite", "Philanthropist",
        "Reincarnator", "Remora", "Reserve", "Shadow", "Sorcerer", "Spiff",
        "Tick-Tock", "Trader", "Tripler", "Vacuum", "Virus", "Void", "Vulch",
        "Warpish", "Warrior", "Will", "Zombie"
    ],

    "Cosmic Incursion": [
        "Bully", "Chronos", "Cryo", "Deuce", "Disease", "Ethic", "Fungus",
        "Fury", "Genius", "Ghoul", "Guerrilla", "Leviathan", "Locust",
        "Magician", "Mercenary", "Merchant", "Plant", "Seeker", "Sniveler",
        "Symbiote"
    ],

    "Cosmic Conflict": [
        "Cavalry", "Changeling", "Empath", "Filth", "Glutton", "Graviton",
        "Industrialist", "Invader", "Lunatic", "Mimic", "Prophet", "Relic",
        "Saboteur", "Sadist", "Siren", "The Claw", "Trickster", "Visionary",
        "Warhawk", "Xenophile"
    ],

    "Cosmic Alliance": [
        "Animal", "Bandit", "Butler", "Chrysalis", "Crystal", "Cyborg",
        "Extortionist", "General", "Gorgon", "Horde", "Lightning", "Poison",
        "Pygmy", "Reborn", "Remote", "Sapient", "Schizoid", "Skeptic",
        "Sting", "Winner"
    ],

    "Cosmic Storm": [
        "Arcade", "Brute", "Bulwark", "Converter", "Coordinator", "Dervish",
        "Grumpus", "Mouth", "Neighbor", "Outlaw", "Patriot", "Phantasm",
        "Porcupine", "Roach", "Scavenger", "Sloth", "Sneak", "Squee",
        "Swindler", "Sycophant", "Tide", "Tyrant", "Vox", "Worm", "Wormhole"
    ],

    "Cosmic Dominion": [
        "Ace", "Alchemist", "Angler", "Aristocrat", "Bride", "Daredevil",
        "Diplomat", "Doppelganger", "Engineer", "Explorer", "Greenhorn",
        "Host", "Joker", "Judge", "Laser", "Lizard", "Love", "Mesmer",
        "Mirage", "Muckraker", "Pentaform", "Pickpocket", "Pirate",
        "Quartermaster", "Reactor", "Tourist", "Usurper", "Voyager",
        "Whirligig", "Yin-Yang"
    ],

    "Cosmic Eons": [
        "AI", "Alien", "Anarchist", "Architect", "Assistant", "Bleeding Heart",
        "Cloak", "Coward", "Crusher", "Emperor", "Evil Twin", "Fire Dancer",
        "Hunger", "Hypochondriac", "Klutz", "Maven", "Moocher", "Multitude",
        "Nanny", "Nightmare", "Oligarch", "Pack Rat", "Particle", "Peddler",
        "Perfectionist", "Pretender", "Sheriff", "Surgeon", "The Cult", "Tortoise"
    ],

    "Cosmic Odyssey": [
        # Includes 12 alternate timeline versions of existing aliens
        "Assessor", "Aura", "Boomerang", "Booster", "Bubble", "Cosmos",
        "Decoy", "Delegator", "Dragon", "Extractor", "Force", "Geek",
        "Gremlin", "Guardian", "Hurtz", "Inferno", "Insect", "Lemming",
        "Lloyd", "Magnet", "Micron", "Negator", "Phantom", "Silencer",
        "Tentacle", "The Meek", "Throwback", "Vector", "Witch", "Wrack",
        "Zilch",
        # Alternate Timeline versions (same power name, different mechanics)
        "Brute (Alt)", "Daredevil (Alt)", "Demon (Alt)", "Grumpus (Alt)",
        "Locust (Alt)", "Masochist (Alt)", "Perfectionist (Alt)",
        "Sadist (Alt)", "Schizoid (Alt)", "Void (Alt)", "Zombie (Alt)"
    ],

    "Promo": [
        "Demon"  # CosmicCon 2014, later in 42nd Anniversary Edition
        # Note: Booster was originally an Escape Velocity convention promo
        # but is now officially included in Cosmic Odyssey expansion
    ]
}

# Alternate name mappings for aliens with different registered names
ALIEN_NAME_MAPPINGS: Dict[str, str] = {
    # Official name -> Registered name variations
    "Anti-Matter": "Antimatter",
    "Tick-Tock": "TickTock",
    "The Claw": "Claw",
    "The Cult": "TheCult",
    "The Meek": "Meek",
    "Bleeding Heart": "BleedingHeart",
    "Evil Twin": "EvilTwin",
    "Fire Dancer": "FireDancer",
    "Pack Rat": "PackRat",
    "Yin-Yang": "YinYang",
    # Alt versions - normalized for lookup
    "Brute (Alt)": "Brute_Alt",
    "Daredevil (Alt)": "Daredevil_Alt",
    "Demon (Alt)": "Demon_Alt",
    "Grumpus (Alt)": "Grumpus_Alt",
    "Locust (Alt)": "Locust_Alt",
    "Masochist (Alt)": "Masochist_Alt",
    "Perfectionist (Alt)": "Perfectionist_Alt",
    "Sadist (Alt)": "Sadist_Alt",
    "Schizoid (Alt)": "Schizoid_Alt",
    "Void (Alt)": "Void_Alt",
    "Zombie (Alt)": "Zombie_Alt",
}

# Add reverse mappings (Registered -> Official)
REGISTERED_NAME_MAPPINGS = {
    "brutealt": "brute (alt)",
    "daredevilalt": "daredevil (alt)",
    "demonalt": "demon (alt)",
    "grumpusalt": "grumpus (alt)",
    "locustalt": "locust (alt)",
    "masochistalt": "masochist (alt)",
    "perfectionistalt": "perfectionist (alt)",
    "sadistalt": "sadist (alt)",
    "schizoidalt": "schizoid (alt)",
    "voidalt": "void (alt)",
    "zombiealt": "zombie (alt)",
}

# Reverse mapping for lookup
REGISTERED_TO_OFFICIAL: Dict[str, str] = {v: k for k, v in ALIEN_NAME_MAPPINGS.items()}

# Build a lookup set of all official alien names (normalized)
def _normalize_name(name: str) -> str:
    """Normalize alien name for comparison."""
    return name.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").lower()

_OFFICIAL_NAMES_SET: Set[str] = set()
_OFFICIAL_EXPANSION_MAP: Dict[str, str] = {}

for expansion, aliens in OFFICIAL_ALIENS.items():
    for alien in aliens:
        normalized = _normalize_name(alien)
        _OFFICIAL_NAMES_SET.add(normalized)
        _OFFICIAL_EXPANSION_MAP[normalized] = expansion
        # Also add mapped version
        if alien in ALIEN_NAME_MAPPINGS:
            mapped_normalized = _normalize_name(ALIEN_NAME_MAPPINGS[alien])
            _OFFICIAL_NAMES_SET.add(mapped_normalized)
            _OFFICIAL_EXPANSION_MAP[mapped_normalized] = expansion


def is_official_alien(name: str) -> bool:
    """Check if an alien is from an official FFG expansion."""
    normalized = _normalize_name(name)
    return normalized in _OFFICIAL_NAMES_SET


def get_alien_expansion(name: str) -> Optional[str]:
    """Get the expansion an alien is from, or None if custom/unofficial."""
    normalized = _normalize_name(name)
    return _OFFICIAL_EXPANSION_MAP.get(normalized)


def get_alien_expansion_enum(name: str) -> Expansion:
    """Get the Expansion enum for an alien. Returns HOMEBREW if not official."""
    expansion_str = get_alien_expansion(name)
    if expansion_str is None:
        return Expansion.HOMEBREW
    return EXPANSION_NAME_TO_ENUM.get(expansion_str, Expansion.HOMEBREW)


def get_aliens_by_expansion(expansion: str) -> List[str]:
    """Get all aliens from a specific expansion."""
    return OFFICIAL_ALIENS.get(expansion, [])


def get_all_official_aliens() -> List[str]:
    """Get a flat list of all official alien names."""
    all_aliens = []
    for aliens in OFFICIAL_ALIENS.values():
        all_aliens.extend(aliens)
    return all_aliens


def get_expansion_names() -> List[str]:
    """Get list of all expansion names."""
    return list(OFFICIAL_ALIENS.keys())


def count_official_aliens() -> int:
    """Count total number of official aliens."""
    return sum(len(aliens) for aliens in OFFICIAL_ALIENS.values())


def categorize_registered_aliens(registered_names: List[str]) -> Dict[str, List[str]]:
    """
    Categorize a list of registered alien names by expansion.

    Returns a dict mapping expansion names to lists of aliens,
    plus a "Custom" key for non-official aliens.
    """
    result: Dict[str, List[str]] = {exp: [] for exp in OFFICIAL_ALIENS.keys()}
    result["Custom"] = []

    for name in registered_names:
        expansion = get_alien_expansion(name)
        if expansion:
            result[expansion].append(name)
        else:
            result["Custom"].append(name)

    return result


def get_official_alien_count_by_expansion() -> Dict[str, int]:
    """Get count of official aliens per expansion."""
    return {exp: len(aliens) for exp, aliens in OFFICIAL_ALIENS.items()}


# Alien power descriptions (brief summaries)
ALIEN_POWER_DESCRIPTIONS: Dict[str, str] = {
    # Base Game
    "Amoeba": "Power to Ooze - Adds ships from other colonies to encounters",
    "Anti-Matter": "Power of Negation - Lower totals win instead of higher",
    "Barbarian": "Power to Pillage - Takes rewards even when losing",
    "Calculator": "Power to Calculate - Announces encounter total before cards played",
    "Chosen": "Power of Destiny - May choose encounter target instead of drawing destiny",
    "Citadel": "Power to Fortify - Ships on home planets count double",
    "Clone": "Power to Replicate - Gets played encounter card back to hand",
    "Cudgel": "Power to Stun - Forces opponent to play lowest encounter card",
    "Dictator": "Power of Oppression - Controls allies' ships in encounters",
    "Fido": "Power to Retrieve - May retrieve cards from discard pile",
    "Filch": "Power to Steal - Takes random card from opponent before encounter",
    "Fodder": "Power to Throw - May use ships as card substitutes",
    "Gambler": "Power to Risk - May draw random card to replace played card",
    "Grudge": "Power of Vendetta - Gains tokens marking enemies, bonuses against them",
    "Hacker": "Power to Peek - Looks at opponent's hand and selects card",
    "Hate": "Power of Vengeance - Gets stronger against players who attacked them",
    "Healer": "Power to Heal - May save ships from going to warp",
    "Human": "Power of Humanity - Gets +4 combat bonus",
    "Kamikaze": "Power of Self-Destruction - Ships count for more if willing to die",
    "Loser": "Power to Win by Losing - Wins encounters when would normally lose",
    "Machine": "Power of Continuity - May have extra encounters",
    "Macron": "Power of Mass - Ships worth 4 each instead of 1",
    "Masochist": "Power to Enjoy Pain - Benefits from losing ships",
    "Mind": "Power of Foresight - Knows opponent's card before playing own",
    "Mirror": "Power to Copy - Uses opponent's power",
    "Miser": "Power to Hoard - Keeps best card from each hand",
    "Mite": "Power of the Small - Can't ally normally but has other advantages",
    "Mutant": "Power to Mutate - May draw new hand anytime",
    "Observer": "Power to Watch - Gains cards when not in encounter",
    "Oracle": "Power to Foresee - Forces opponent to play card first",
    "Pacifist": "Power of Peace - Wins if both sides play negotiate",
    "Parasite": "Power to Infest - May join either side uninvited",
    "Philanthropist": "Power to Give - Must give cards away, benefits from it",
    "Reincarnator": "Power to be Reborn - Gets new alien when loses all bases",
    "Remora": "Power to Suck - Takes compensation whenever anyone receives cards",
    "Reserve": "Power to Reserve - May call for allies before playing card",
    "Shadow": "Power to Shadow - May join winning side after cards revealed",
    "Sorcerer": "Power to Switch - May swap encounter cards with opponent",
    "Spiff": "Power to Crash Land - Ships survive even on lost encounters",
    "Tick-Tock": "Power of Time - Wins if game reaches certain turn count",
    "Trader": "Power to Trade - May swap hands with any player",
    "Tripler": "Power to Triple - Encounter card value tripled",
    "Vacuum": "Power to Suck In - Takes losing ships prisoner",
    "Virus": "Power to Multiply - Multiplies card value by ships instead of adding",
    "Void": "Power to Eradicate - Sends ships to void instead of warp",
    "Vulch": "Power to Scrounge - Takes artifacts played by others",
    "Warpish": "Power of Warp Speed - Uses ships in warp for encounters",
    "Warrior": "Power of Bonus - Gets +1 for each ship in warp",
    "Will": "Power of Willfulness - May force same card to be played",
    "Zombie": "Power of Immortality - Ships never go to warp",

    # Cosmic Incursion
    "Bully": "Power to Intimidate - Forces weaker opponents to negotiate",
    "Chronos": "Power of Time Travel - May undo and redo encounters",
    "Cryo": "Power to Preserve - Ships frozen instead of going to warp",
    "Deuce": "Power of Duality - May play two encounter cards",
    "Disease": "Power of Contagion - Spreads tokens that weaken opponents",
    "Ethic": "Power of Guilt - Opponents must help or feel guilty",
    "Fungus": "Power to Adhere - Ships stick together across encounters",
    "Fury": "Power of Vengeance - Gets stronger when attacked",
    "Genius": "Power to Outwit - Predicts opponent's card and benefits if right",
    "Ghoul": "Power to Feast - Takes cards from discards when ships go to warp",
    "Guerrilla": "Power of Attrition - Slowly erodes opponent's forces",
    "Leviathan": "Power of Worldships - Home planets can move",
    "Locust": "Power to Devour - Consumes colonies for benefits",
    "Magician": "Power of Prestidigitation - Makes cards disappear and reappear",
    "Mercenary": "Power of Bounty Hunting - Paid to join encounters",
    "Merchant": "Power to Hire - Buys ships and cards",
    "Plant": "Power of Grafting - Roots ships on planets",
    "Seeker": "Power of Truth - Forces honest answers to questions",
    "Sniveler": "Power to Whine - Complains to get benefits",
    "Symbiote": "Power of Bonding - Shares colonies with another player",

    # Cosmic Conflict
    "Cavalry": "Power to Reinforce - Adds ships after cards revealed",
    "Changeling": "Power to Change Form - Becomes different alien each encounter",
    "Empath": "Power of Harmony - Both sides benefit when using negotiate",
    "Filth": "Power to Reek - Opponents disgusted and weakened",
    "Glutton": "Power to Gorge - Consumes cards for power",
    "Graviton": "Power of Gravity - Pulls ships to encounters",
    "Industrialist": "Power to Build - Creates colony tokens",
    "Invader": "Power of Invasion - Always attacks, never defends",
    "Lunatic": "Power of Lunacy - Randomly changes game rules",
    "Mimic": "Power to Mimic - Copies other alien powers",
    "Prophet": "Power of Prophecy - Predicts encounter outcomes",
    "Relic": "Power of Antiquity - Uses ancient artifacts",
    "Saboteur": "Power to Booby Trap - Plants traps on planets",
    "Sadist": "Power to Torment - Benefits from opponent's suffering",
    "Siren": "Power to Lure - Draws ships to bad situations",
    "The Claw": "Power to Snatch - Steals planets",
    "Trickster": "Power of Deception - Plays cards face-down",
    "Visionary": "Power of Vision - Sees future card draws",
    "Warhawk": "Power to Escalate - Increases conflict intensity",
    "Xenophile": "Power to Love - Benefits from having diverse allies",

    # Cosmic Alliance
    "Animal": "Power to Tame - Controls wild game elements",
    "Bandit": "Power to Ambush - Attacks from hiding",
    "Butler": "Power to Serve - Helps others but secretly benefits",
    "Chrysalis": "Power to Emerge - Transforms during game",
    "Crystal": "Power to Reflect - Reflects attacks back",
    "Cyborg": "Power of Bionics - Enhanced mechanical abilities",
    "Extortionist": "Power to Extort - Demands payment for cooperation",
    "General": "Power to Command - Controls allied ship placement",
    "Gorgon": "Power to Petrify - Freezes opponent actions",
    "Horde": "Power of Numbers - Overwhelms with quantity",
    "Lightning": "Power to Strike - Fast, unexpected attacks",
    "Poison": "Power to Toxify - Weakens opponents over time",
    "Pygmy": "Power of Smallness - Small but numerous",
    "Reborn": "Power of Rebirth - Returns from defeat",
    "Remote": "Power to Control - Operates from distance",
    "Sapient": "Power of Intelligence - Knows optimal plays",
    "Schizoid": "Power to Alter Reality - Changes win conditions",
    "Skeptic": "Power to Doubt - Denies other powers",
    "Sting": "Power to Strike - Quick painful attacks",
    "Winner": "Power to Win - Wins ties and close encounters",

    # Cosmic Storm
    "Arcade": "Power to Play - Uses mini-game mechanics",
    "Brute": "Power to Smash - Raw strength attacks",
    "Bulwark": "Power to Defend - Strong defensive capabilities",
    "Converter": "Power to Convert - Changes card types",
    "Coordinator": "Power to Organize - Coordinates ally actions",
    "Dervish": "Power to Spin - Confuses with rapid movement",
    "Grumpus": "Power to Complain - Benefits from bad situations",
    "Mouth": "Power to Talk - Convinces others through speech",
    "Neighbor": "Power of Proximity - Benefits from adjacent players",
    "Outlaw": "Power to Break Rules - Ignores certain restrictions",
    "Patriot": "Power of Loyalty - Stronger on home turf",
    "Phantasm": "Power to Haunt - Ghostly presence affects play",
    "Porcupine": "Power to Bristle - Hurts those who attack",
    "Roach": "Power to Survive - Hard to eliminate",
    "Scavenger": "Power to Scrounge - Collects from discards",
    "Sloth": "Power to Delay - Slows down game pace",
    "Sneak": "Power to Sneak - Hidden movements",
    "Squee": "Power to Annoy - Irritates opponents",
    "Swindler": "Power to Cheat - Bends rules for benefit",
    "Sycophant": "Power to Flatter - Gains favor through flattery",
    "Tide": "Power to Ebb and Flow - Power varies cyclically",
    "Tyrant": "Power to Oppress - Controls other players",
    "Vox": "Power to Speak - Voice affects gameplay",
    "Worm": "Power to Burrow - Underground movement",
    "Wormhole": "Power to Transport - Instant movement across galaxy",

    # Cosmic Dominion
    "Ace": "Power to Triumph - Exceptional at winning",
    "Alchemist": "Power of Transmutation - Changes card values",
    "Angler": "Power to Fish - Draws specific cards",
    "Aristocrat": "Power of Nobility - Superior status benefits",
    "Bride": "Power to Wed - Joins with other players",
    "Daredevil": "Power to Risk - High-risk high-reward plays",
    "Diplomat": "Power of Diplomacy - Negotiates advantageous deals",
    "Doppelganger": "Power to Impersonate - Copies other players",
    "Engineer": "Power to Build - Constructs advantages",
    "Explorer": "Power to Discover - Finds hidden opportunities",
    "Greenhorn": "Power of Inexperience - Benefits from being new",
    "Host": "Power to Entertain - Benefits from hosting encounters",
    "Joker": "Power of Jest - Unpredictable card effects",
    "Judge": "Power to Rule - Makes binding decisions",
    "Laser": "Power to Focus - Concentrated attacks",
    "Lizard": "Power to Regenerate - Recovers from losses",
    "Love": "Power to Attract - Draws others to them",
    "Mesmer": "Power to Hypnotize - Controls opponent choices",
    "Mirage": "Power of Illusion - Creates false appearances",
    "Muckraker": "Power to Expose - Reveals hidden information",
    "Pentaform": "Power of Five - Five different abilities",
    "Pickpocket": "Power to Pilfer - Steals from others",
    "Pirate": "Power to Plunder - Takes from encounters",
    "Quartermaster": "Power to Supply - Provides resources",
    "Reactor": "Power to Respond - Reactive abilities",
    "Tourist": "Power to Visit - Benefits from visiting",
    "Usurper": "Power to Overthrow - Takes others' positions",
    "Voyager": "Power to Travel - Movement advantages",
    "Whirligig": "Power to Spin - Rotates positions/cards",
    "Yin-Yang": "Power of Balance - Benefits from equilibrium",

    # Cosmic Eons
    "AI": "Power to Compute - Calculates optimal outcomes",
    "Alien": "Power of Otherness - Different from all others",
    "Anarchist": "Power of Chaos - Ignores rules",
    "Architect": "Power to Design - Plans complex strategies",
    "Assistant": "Power to Help - Aids other players",
    "Bleeding Heart": "Power of Empathy - Affected by others' losses",
    "Cloak": "Power to Hide - Conceals information",
    "Coward": "Power to Flee - Avoids confrontation",
    "Crusher": "Power to Crush - Overwhelming force",
    "Emperor": "Power to Rule - Commands others",
    "Evil Twin": "Power to Mirror Darkly - Dark copy of opponent",
    "Fire Dancer": "Power of Fire - Burns opponents",
    "Hunger": "Power to Consume - Must feed on resources",
    "Hypochondriac": "Power of Illness - Benefits from perceived weakness",
    "Klutz": "Power of Clumsiness - Accidents help them",
    "Maven": "Power of Expertise - Master of specific domain",
    "Moocher": "Power to Mooch - Takes from others freely",
    "Multitude": "Power of Many - Represents multiple beings",
    "Nanny": "Power to Protect - Guards weaker players",
    "Nightmare": "Power to Terrify - Fear-based attacks",
    "Oligarch": "Power of Wealth - Buys advantages",
    "Pack Rat": "Power to Collect - Hoards resources",
    "Particle": "Power of Smallness - Tiny but significant",
    "Peddler": "Power to Sell - Trades for advantage",
    "Perfectionist": "Power of Perfection - Demands exact outcomes",
    "Pretender": "Power to Pretend - Fakes having powers",
    "Sheriff": "Power to Enforce - Punishes rule violations",
    "Surgeon": "Power to Operate - Precise manipulations",
    "The Cult": "Power of Devotion - Followers grant power",
    "Tortoise": "Power of Slowness - Slow but steady progress",

    # Cosmic Odyssey (new aliens, not alternates)
    "Assessor": "Power to Evaluate - Determines values",
    "Aura": "Power of Presence - Passive area effects",
    "Boomerang": "Power to Return - Actions come back",
    "Booster": "Power to Boost - Enhances other effects",
    "Bubble": "Power to Protect - Shields from harm",
    "Cosmos": "Power of the Universe - Universal effects",
    "Decoy": "Power to Distract - Misleads opponents",
    "Delegator": "Power to Delegate - Assigns tasks to others",
    "Dragon": "Power to Devastate - Powerful destruction",
    "Extractor": "Power to Extract - Removes specific elements",
    "Force": "Power of Strength - Raw power",
    "Geek": "Power of Knowledge - Obscure information",
    "Gremlin": "Power to Sabotage - Causes malfunctions",
    "Guardian": "Power to Guard - Protects assets",
    "Hurtz": "Power to Pain - Inflicts damage",
    "Inferno": "Power of Fire - Burning attacks",
    "Insect": "Power of Swarm - Many small ships",
    "Lemming": "Power to Follow - Copies others' actions",
    "Lloyd": "Power to Protect - Guards player assets",
    "Magnet": "Power to Attract - Draws things to it",
    "Micron": "Power of Tiny - Extremely small ships",
    "Negator": "Power to Negate - Cancels effects",
    "Phantom": "Power to Phase - Intangible presence",
    "Silencer": "Power to Quiet - Stops powers/effects",
    "Tentacle": "Power to Grasp - Grabs multiple things",
    "The Meek": "Power to Win by Losing - Different victory path",
    "Throwback": "Power of Nostalgia - Uses old mechanics",
    "Vector": "Power of Direction - Controls movement",
    "Witch": "Power to Curse - Hexes opponents",
    "Wrack": "Power to Damage - Causes ongoing harm",
    "Zilch": "Power of Nothing - Benefits from having nothing",

    # Promo
    "Demon": "Power to Possess - Takes control of opponents",
}


def get_alien_description(name: str) -> Optional[str]:
    """Get the power description for an alien."""
    # Try direct lookup
    if name in ALIEN_POWER_DESCRIPTIONS:
        return ALIEN_POWER_DESCRIPTIONS[name]

    # Try normalized lookup
    for official_name, desc in ALIEN_POWER_DESCRIPTIONS.items():
        if _normalize_name(official_name) == _normalize_name(name):
            return desc

    return None


def get_missing_official_aliens(registered_names: List[str]) -> List[str]:
    """Find official aliens that are not registered."""
    registered_normalized = {_normalize_name(n) for n in registered_names}
    missing = []

    for expansion, aliens in OFFICIAL_ALIENS.items():
        for alien in aliens:
            normalized = _normalize_name(alien)
            # Check both the official name and mapped name
            mapped = ALIEN_NAME_MAPPINGS.get(alien)
            mapped_normalized = _normalize_name(mapped) if mapped else None

            # Also check underscored version for Alt aliens
            underscored_normalized = _normalize_name(alien.replace(" (Alt)", "_Alt").replace("(", "").replace(")", ""))

            if normalized not in registered_normalized:
                if not mapped_normalized or mapped_normalized not in registered_normalized:
                    # Also check underscored version
                    if underscored_normalized not in registered_normalized:
                        missing.append(f"{alien} ({expansion})")

    return missing


def print_official_alien_summary():
    """Print a summary of official aliens by expansion."""
    print("=" * 60)
    print("OFFICIAL COSMIC ENCOUNTER ALIENS BY EXPANSION")
    print("=" * 60)

    total = 0
    for expansion, aliens in OFFICIAL_ALIENS.items():
        count = len(aliens)
        total += count
        print(f"\n{expansion} ({count} aliens):")
        print("-" * 40)
        for i, alien in enumerate(sorted(aliens), 1):
            desc = get_alien_description(alien)
            if desc:
                print(f"  {i:2}. {alien}: {desc}")
            else:
                print(f"  {i:2}. {alien}")

    print(f"\n{'=' * 60}")
    print(f"TOTAL OFFICIAL ALIENS: {total}")
    print("=" * 60)


if __name__ == "__main__":
    print_official_alien_summary()
