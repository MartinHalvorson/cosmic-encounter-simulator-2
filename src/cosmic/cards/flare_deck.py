"""
The Flare Deck - special cards that provide alien power effects.

Each flare card has two effects:
- Wild: Can be used by any player
- Super: Can only be used by a player with the matching alien power
"""

import random
from typing import List, Dict, Optional, TYPE_CHECKING
from dataclasses import dataclass, field

from .base import Card, FlareCard
from ..aliens.registry import AlienRegistry

if TYPE_CHECKING:
    from ..player import Player


@dataclass
class FlareDeck:
    """
    The flare deck contains one flare for each alien in the game.
    Flares are shuffled into the cosmic deck at game start.
    """
    draw_pile: List[FlareCard] = field(default_factory=list)
    _rng: random.Random = field(default_factory=random.Random)

    def create_flares_for_game(self, alien_names: List[str]) -> List[FlareCard]:
        """
        Create flare cards for the aliens in the current game.
        Per rules: only include flares for aliens that are in the game.
        """
        flares = []
        for name in alien_names:
            flare = self._create_flare_for_alien(name)
            if flare:
                flares.append(flare)
        return flares

    def _create_flare_for_alien(self, alien_name: str) -> Optional[FlareCard]:
        """Create a flare card for a specific alien."""
        # Get flare effects based on the alien
        effects = FLARE_EFFECTS.get(alien_name)
        if effects:
            return FlareCard(
                alien_name=alien_name,
                wild_effect=effects.get('wild', f"Wild: Gain a minor {alien_name} benefit."),
                super_effect=effects.get('super', f"Super: Gain a major {alien_name} benefit.")
            )
        # Default flare for aliens without specific effects
        return FlareCard(
            alien_name=alien_name,
            wild_effect=f"Wild: Once per encounter, gain +2 to your total.",
            super_effect=f"Super: Once per encounter, gain +4 to your total."
        )

    def set_rng(self, rng: random.Random) -> None:
        """Set the random number generator for reproducibility."""
        self._rng = rng


# Flare effects for various aliens
# Wild effects are weaker versions usable by anyone
# Super effects are stronger and only usable by the matching alien
FLARE_EFFECTS: Dict[str, Dict[str, str]] = {
    "Machine": {
        "wild": "Wild: Take one extra encounter this turn.",
        "super": "Super: Take two extra encounters this turn."
    },
    "Virus": {
        "wild": "Wild: Add your ships to your total (instead of your opponent adding theirs).",
        "super": "Super: Triple your ship count when adding to total."
    },
    "Zombie": {
        "wild": "Wild: Return 2 ships from the warp to any of your colonies.",
        "super": "Super: Return all your ships from the warp."
    },
    "Oracle": {
        "wild": "Wild: Look at your opponent's encounter card before playing yours.",
        "super": "Super: Look at opponent's card and force them to play a different one."
    },
    "Sorcerer": {
        "wild": "Wild: Swap encounter cards with any player after reveal.",
        "super": "Super: Swap hands with any player."
    },
    "Loser": {
        "wild": "Wild: If you would lose, win instead (once).",
        "super": "Super: Automatically lose the encounter and win."
    },
    "Macron": {
        "wild": "Wild: Your ships count as 2 each this encounter.",
        "super": "Super: Your ships count as 5 each this encounter."
    },
    "Clone": {
        "wild": "Wild: Copy the card you just played from the discard.",
        "super": "Super: Play the same card again without discarding."
    },
    "Trader": {
        "wild": "Wild: Draw 2 cards from the deck.",
        "super": "Super: Trade hands with any player."
    },
    "Pacifist": {
        "wild": "Wild: If you play a Negotiate, add 10 to your total.",
        "super": "Super: If you play a Negotiate and win, gain an extra colony."
    },
    "Human": {
        "wild": "Wild: Add +3 to your total.",
        "super": "Super: Add +6 to your total."
    },
    "Parasite": {
        "wild": "Wild: Join an encounter as an ally without invitation.",
        "super": "Super: Join both sides of an encounter."
    },
    "Warpish": {
        "wild": "Wild: Send 2 opponent ships to the warp.",
        "super": "Super: Send 4 opponent ships to the warp."
    },
    "Symbiote": {
        "wild": "Wild: Double the ships on one of your colonies.",
        "super": "Super: Triple the ships on one of your colonies."
    },
    "Void": {
        "wild": "Wild: Remove one opposing ship from the game (to the void).",
        "super": "Super: Remove all ships from one planet to the void."
    },
    "Assassin": {
        "wild": "Wild: Eliminate 1 opponent ship from the encounter.",
        "super": "Super: Eliminate up to 3 opponent ships from the encounter."
    },
    "Healer": {
        "wild": "Wild: Return 3 ships from any warp to colonies.",
        "super": "Super: Return all ships from the warp to colonies."
    },
    "Warrior": {
        "wild": "Wild: Add +1 for each of your ships in the warp.",
        "super": "Super: Add +2 for each of your ships in the warp."
    },
    "Chosen": {
        "wild": "Wild: Add the top card of the deck to your total.",
        "super": "Super: Add the top 2 cards of the deck to your total."
    },
    "Filch": {
        "wild": "Wild: Steal a random card from one opponent.",
        "super": "Super: Steal 2 cards from one opponent."
    },
    "Gambler": {
        "wild": "Wild: Flip a coin. If heads, double your card value.",
        "super": "Super: Triple your card value on heads, normal on tails."
    },
    "Shadow": {
        "wild": "Wild: Add 2 ships from colonies to the encounter.",
        "super": "Super: Add 4 ships from colonies to the encounter."
    },
    "Tripler": {
        "wild": "Wild: Triple a single digit on your attack card.",
        "super": "Super: Triple your entire attack card value."
    },
    "Spiff": {
        "wild": "Wild: Draw 1 card from the rewards deck.",
        "super": "Super: Draw 2 cards from the rewards deck."
    },
    "Remora": {
        "wild": "Wild: Draw 1 card whenever another player draws.",
        "super": "Super: Draw 2 cards whenever another player draws."
    },
    "Calculator": {
        "wild": "Wild: Increase your card value by the number of cards in your hand.",
        "super": "Super: Double your card value based on cards in hand."
    },
    "Chronos": {
        "wild": "Wild: Take another turn after this one.",
        "super": "Super: Take two additional turns."
    },
    "Disease": {
        "wild": "Wild: Spread 1 of your ships to an opponent's colony.",
        "super": "Super: Spread 2 ships to different opponent colonies."
    },
    "Mutant": {
        "wild": "Wild: Draw 2 cards, keep 1, discard 1.",
        "super": "Super: Draw 4 cards, keep 2, discard 2."
    },
    "Mirror": {
        "wild": "Wild: Reverse the digits of your attack card.",
        "super": "Super: Reverse opponent's attack card digits too."
    },
    "Grudge": {
        "wild": "Wild: Add +3 against a player who attacked you.",
        "super": "Super: Add +6 against any player who has attacked you."
    },
    "Ethic": {
        "wild": "Wild: Force all players to play face-up this encounter.",
        "super": "Super: See all cards before choosing yours."
    },
    "Mite": {
        "wild": "Wild: Look at the top 3 cards of any deck.",
        "super": "Super: Rearrange the top 3 cards of any deck."
    },
    "Negator": {
        "wild": "Wild: Cancel one alien power this encounter.",
        "super": "Super: Cancel all alien powers this encounter."
    },
    "Sniveler": {
        "wild": "Wild: Force one player to give you 1 card.",
        "super": "Super: Force each opponent to give you 1 card."
    },
    "Tick-Tock": {
        "wild": "Wild: Add 1 token to any player's Tick-Tock counter.",
        "super": "Super: Win immediately if you have 10+ tokens."
    },
    "Masochist": {
        "wild": "Wild: Lose 1 ship to gain 1 card.",
        "super": "Super: Lose ships to gain equal cards, then win if you have 0 ships."
    },
    "Reincarnator": {
        "wild": "Wild: Draw a new alien power from the unused pile.",
        "super": "Super: Choose any alien power from the unused pile."
    },
    "Hate": {
        "wild": "Wild: Add +4 against your nemesis.",
        "super": "Super: Add +8 against your nemesis."
    },
    "Phantom": {
        "wild": "Wild: Return lost ships to colonies instead of warp.",
        "super": "Super: Ships never go to warp, always return home."
    },
    "Diplomat": {
        "wild": "Wild: Force a deal to succeed.",
        "super": "Super: Gain 2 colonies from a forced deal."
    },
    "Vulture": {
        "wild": "Wild: Draw 1 card when any ship goes to warp.",
        "super": "Super: Draw 2 cards when any ship goes to warp."
    },
    "Grief": {
        "wild": "Wild: When you lose ships, one opponent loses 1.",
        "super": "Super: When you lose ships, all opponents lose 1 each."
    },
    "Fodder": {
        "wild": "Wild: Sacrifice 1 ship for +2 to total.",
        "super": "Super: Sacrifice any ships for +3 each."
    },
    "Horde": {
        "wild": "Wild: Return 1 ship from warp at encounter start.",
        "super": "Super: Return 2 ships from warp at encounter start."
    },
    "Roach": {
        "wild": "Wild: Return 2 ships when losing last colony.",
        "super": "Super: Return 4 ships when losing last colony."
    },
    # Base Game Aliens (Fantasy Flight 2008 Edition)
    "Anti-Matter": {
        "wild": "Wild: Reverse the outcome - lower total wins this encounter.",
        "super": "Super: Your 0 attack cards count as 40."
    },
    "Citadel": {
        "wild": "Wild: One of your colonies cannot be attacked this encounter.",
        "super": "Super: All your home colonies are protected this encounter."
    },
    "Cudgel": {
        "wild": "Wild: Force one opponent to commit all 4 ships.",
        "super": "Super: Force all opponents to commit maximum ships."
    },
    "Dictator": {
        "wild": "Wild: Choose which card one opponent must play.",
        "super": "Super: Choose the encounter cards for both main players."
    },
    "Fido": {
        "wild": "Wild: Retrieve one card from the discard pile.",
        "super": "Super: Retrieve up to 3 cards from the discard pile."
    },
    "Finder": {
        "wild": "Wild: Look at any player's hand.",
        "super": "Super: Take one card from any player's hand."
    },
    "Genius": {
        "wild": "Wild: Draw 3 cards, keep 1.",
        "super": "Super: Draw 5 cards, keep 2."
    },
    "Laser": {
        "wild": "Wild: Destroy 1 opposing ship before totals.",
        "super": "Super: Destroy up to 3 opposing ships before totals."
    },
    "Miser": {
        "wild": "Wild: Play a card from your stash without revealing.",
        "super": "Super: Your entire stash adds to your total."
    },
    # Note: Mutant flare defined earlier in file
    "Observer": {
        "wild": "Wild: Look at all face-down cards in the encounter.",
        "super": "Super: Look at all hands and choose your card last."
    },
    "Philanthropist": {
        "wild": "Wild: Give 2 cards to any player to gain 1 colony.",
        "super": "Super: Give 4 cards to gain 2 colonies."
    },
    "Reserve": {
        "wild": "Wild: Add reinforcements from reserve to total.",
        "super": "Super: Double all reinforcement card values."
    },
    "Seeker": {
        "wild": "Wild: Search deck for any attack card.",
        "super": "Super: Search deck for any card."
    },
    # Note: Tick-Tock, Tripler, Warpish flares defined earlier in file
    "Will": {
        "wild": "Wild: Use your power even when zapped.",
        "super": "Super: Your power cannot be zapped this encounter."
    },
    # Cosmic Incursion Expansion
    "Cavalry": {
        "wild": "Wild: Add 2 ships from reserves to the encounter.",
        "super": "Super: Add all ships from reserves to the encounter."
    },
    "Claw": {
        "wild": "Wild: Steal 1 card from encounter winner.",
        "super": "Super: Steal 3 cards from encounter winner."
    },
    # Note: Cudgel flare defined earlier in file
    "Daredevil": {
        "wild": "Wild: Double your attack card if you committed 4 ships.",
        "super": "Super: Triple attack if you committed 4 ships."
    },
    "Emigre": {
        "wild": "Wild: Move 2 ships to any colony.",
        "super": "Super: Move all your ships freely between colonies."
    },
    "Extortionist": {
        "wild": "Wild: Force a player to give you 1 card or lose a ship.",
        "super": "Super: Force all players to give 1 card each."
    },
    "Grumpus": {
        "wild": "Wild: Discard to make opponent discard equally.",
        "super": "Super: Opponent discards double what you discard."
    },
    "Locust": {
        "wild": "Wild: Draw 1 card for each ship you lost.",
        "super": "Super: Draw 2 cards for each ship you lost."
    },
    "Mouth": {
        "wild": "Wild: Negotiate cannot fail this encounter.",
        "super": "Super: All negotiations give you double colonies."
    },
    "Quartermaster": {
        "wild": "Wild: Discard to retrieve equal cards from discard.",
        "super": "Super: Retrieve any cards from discard pile."
    },
    "Saboteur": {
        "wild": "Wild: Reduce one attack card by 10.",
        "super": "Super: Reduce opponent's card to 0."
    },
    "Silencer": {
        "wild": "Wild: Cancel one alien power use.",
        "super": "Super: Cancel all alien powers this encounter."
    },
    "Sniveler": {
        "wild": "Wild: Complain to force a redraw of destiny.",
        "super": "Super: Choose any player as defender."
    },
    "Spiff": {
        "wild": "Wild: Draw 1 from rewards deck.",
        "super": "Super: Draw 3 from rewards deck."
    },
    "Sting": {
        "wild": "Wild: Opponent loses 1 ship for each of your ships lost.",
        "super": "Super: Opponent loses 2 ships for each of yours lost."
    },
    "Trickster": {
        "wild": "Wild: Play a negotiate as a 20 attack.",
        "super": "Super: Negotiate counts as 30 attack."
    },
    "Warhawk": {
        "wild": "Wild: Add +5 when attacking.",
        "super": "Super: Add +10 when attacking."
    },
    # Cosmic Conflict Expansion
    "Amoeba": {
        "wild": "Wild: Add 2 ships to the encounter from warp.",
        "super": "Super: Add 4 ships from anywhere to encounter."
    },
    "Barbarian": {
        "wild": "Wild: Pillage 1 card from loser.",
        "super": "Super: Pillage 3 cards from loser."
    },
    "Butler": {
        "wild": "Wild: Serve 1 card to each player.",
        "super": "Super: Choose who gets served and who doesn't."
    },
    "Changeling": {
        "wild": "Wild: Copy one alien power for this encounter.",
        "super": "Super: Copy two alien powers for this encounter."
    },
    "Cryo": {
        "wild": "Wild: Freeze 1 opponent ship (can't be used).",
        "super": "Super: Freeze up to 3 opponent ships."
    },
    # Note: Ethic flare defined earlier in file
    "Fungus": {
        "wild": "Wild: Spread to 1 additional colony.",
        "super": "Super: Spread to all opponent colonies."
    },
    "Gambler": {
        "wild": "Wild: Flip for double or nothing on attack value.",
        "super": "Super: Choose the coin flip result."
    },
    "Grudge": {
        "wild": "Wild: +4 against someone who attacked you.",
        "super": "Super: +8 against anyone who has attacked you."
    },
    "Hate": {
        "wild": "Wild: +5 against your nemesis.",
        "super": "Super: +10 against your nemesis."
    },
    "Kamikaze": {
        "wild": "Wild: Sacrifice ships for +4 each.",
        "super": "Super: Sacrifice all ships for instant win."
    },
    "Leviathan": {
        "wild": "Wild: Add +10 but lose 2 ships to warp.",
        "super": "Super: Add +20, no ship loss."
    },
    "Magician": {
        "wild": "Wild: Swap hands with one player.",
        "super": "Super: Take best cards from all hands."
    },
    "Masochist": {
        "wild": "Wild: Lose to gain cards equal to ships lost.",
        "super": "Super: Win by having 0 ships on board."
    },
    "Miser": {
        "wild": "Wild: Stash adds +2 per card to total.",
        "super": "Super: Stash cards count as double value."
    },
    "Nightmare": {
        "wild": "Wild: Opponent must discard 2 cards.",
        "super": "Super: Opponent discards half their hand."
    },
    "Pentaform": {
        "wild": "Wild: Use 5 different aliens' powers once each.",
        "super": "Super: Combine any 2 alien powers permanently."
    },
    "Reincarnator": {
        "wild": "Wild: Draw a new alien power.",
        "super": "Super: Choose any alien power to become."
    },
    "Sadist": {
        "wild": "Wild: Gain +2 for each opponent ship destroyed.",
        "super": "Super: Gain +4 for each opponent ship destroyed."
    },
    "Siren": {
        "wild": "Wild: Lure 2 opponent ships to join your side.",
        "super": "Super: Lure all opponent allies to your side."
    },
    # Cosmic Alliance Expansion
    "Admiral": {
        "wild": "Wild: Move your ships freely during regroup.",
        "super": "Super: Move any player's ships during regroup."
    },
    "Aristocrat": {
        "wild": "Wild: Draw 1 card per colony you have.",
        "super": "Super: Draw 2 cards per colony you have."
    },
    "Bazaar": {
        "wild": "Wild: Trade 1 card with any player.",
        "super": "Super: Trade any number of cards with any players."
    },
    "Bride": {
        "wild": "Wild: Force one player to ally with you.",
        "super": "Super: Force all invited players to ally with you."
    },
    "Bully": {
        "wild": "Wild: +4 against players with fewer colonies.",
        "super": "Super: +8 against players with fewer colonies."
    },
    "Chief": {
        "wild": "Wild: Choose alliance order.",
        "super": "Super: Choose who can and cannot ally."
    },
    "Connoisseur": {
        "wild": "Wild: Look at top 5 cards, take 1.",
        "super": "Super: Look at top 10 cards, take 3."
    },
    "Crawler": {
        "wild": "Wild: Escape to a colony when ships would go to warp.",
        "super": "Super: All your ships escape to colonies."
    },
    "Critic": {
        "wild": "Wild: Force card replay.",
        "super": "Super: Cancel and replay entire planning phase."
    },
    "Crystal": {
        "wild": "Wild: Reveal attack cards before commit.",
        "super": "Super: Opponent must reveal and you can change."
    },
    "Dervish": {
        "wild": "Wild: Spin - random good or bad effect.",
        "super": "Super: Choose the spin result."
    },
    "Empath": {
        "wild": "Wild: Know opponent's card type.",
        "super": "Super: Know opponent's exact card."
    },
    "Ghoul": {
        "wild": "Wild: Retrieve 2 ships from warp as ally.",
        "super": "Super: Retrieve all your ships from warp."
    },
    "Industrialist": {
        "wild": "Wild: Build 2 free ships.",
        "super": "Super: Build ships equal to your colonies."
    },
    "Investigator": {
        "wild": "Wild: Look at one player's hand.",
        "super": "Super: Look at all players' hands."
    },
    "Lunatic": {
        "wild": "Wild: Random player becomes defender.",
        "super": "Super: You choose defender regardless of destiny."
    },
    "Muckraker": {
        "wild": "Wild: Expose one player's hidden card.",
        "super": "Super: Expose all hidden cards."
    },
    "Oligarch": {
        "wild": "Wild: Rich players (5+ cards) give you 1.",
        "super": "Super: Rich players give you 2 each."
    },
    "Outlaw": {
        "wild": "Wild: Rob 2 cards from encounter winner.",
        "super": "Super: Rob winner's entire hand."
    },
    "Plant": {
        "wild": "Wild: Root into colony - cannot be removed.",
        "super": "Super: Root into 3 colonies."
    },
    # Cosmic Storm Expansion
    "Arcade": {
        "wild": "Wild: Play minigame for bonus.",
        "super": "Super: Auto-win minigame."
    },
    "Beast": {
        "wild": "Wild: Rampage - destroy 1 ship per colony.",
        "super": "Super: Destroy 2 ships per colony."
    },
    "Berserker": {
        "wild": "Wild: +6 but can't retreat.",
        "super": "Super: +12 and destroy all losing ships."
    },
    "Booster": {
        "wild": "Wild: Double an ally's ship contribution.",
        "super": "Super: Triple all allies' contributions."
    },
    "Brain": {
        "wild": "Wild: Intelligence - see top 3 deck cards.",
        "super": "Super: Rearrange top 5 deck cards."
    },
    "Bulwark": {
        "wild": "Wild: +5 defense bonus.",
        "super": "Super: +10 defense bonus and immune to powers."
    },
    "Collector": {
        "wild": "Wild: Gain 1 of each card type.",
        "super": "Super: Complete your collection - draw until full set."
    },
    "Coordinator": {
        "wild": "Wild: Allies act in unison.",
        "super": "Super: All allies get your alien power."
    },
    "Deuce": {
        "wild": "Wild: Play 2 cards, use better one.",
        "super": "Super: Play 2 cards, use both values."
    },
    "Doubler": {
        "wild": "Wild: Double one card's value.",
        "super": "Super: Double all your cards' values."
    },
    "Electron": {
        "wild": "Wild: +1 per card in all hands.",
        "super": "Super: +2 per card in all hands."
    },
    "Entangler": {
        "wild": "Wild: Link fates with one opponent.",
        "super": "Super: All opponents share your fate."
    },
    "Equilibrium": {
        "wild": "Wild: Equalize ship counts.",
        "super": "Super: Equalize everything (cards, colonies, ships)."
    },
    "Expert": {
        "wild": "Wild: Reroll any die or flip.",
        "super": "Super: Choose any die/flip result."
    },
    "Grudge": {
        "wild": "Wild: +4 against prior attackers.",
        "super": "Super: +8 against all who wronged you."
    },
    "Inflator": {
        "wild": "Wild: All attack cards +5.",
        "super": "Super: All your attack cards doubled."
    },
    "Insurance": {
        "wild": "Wild: Recover half losses.",
        "super": "Super: Recover all losses and gain bonus."
    },
    "Interrupter": {
        "wild": "Wild: Cancel one action.",
        "super": "Super: Cancel entire phase."
    },
    "Investor": {
        "wild": "Wild: Invest ships for later return with interest.",
        "super": "Super: Double invested ships return."
    },
    "Jinx": {
        "wild": "Wild: Curse - opponent's next action fails.",
        "super": "Super: Permanent curse until removed."
    },
    "Joker": {
        "wild": "Wild: Wild card effect - copy any flare.",
        "super": "Super: Copy any super flare effect."
    },
    # Cosmic Dominion Expansion
    "Anarchist": {
        "wild": "Wild: Cancel all rules for one phase.",
        "super": "Super: You make the rules this encounter."
    },
    "Capitalist": {
        "wild": "Wild: Buy extra cards at 1 ship each.",
        "super": "Super: Buy anything at ship cost."
    },
    "Colonist": {
        "wild": "Wild: Establish free colony.",
        "super": "Super: Establish 2 free colonies."
    },
    "Elitist": {
        "wild": "Wild: Only high cards count (20+).",
        "super": "Super: Low cards become high cards."
    },
    "Glutton": {
        "wild": "Wild: Absorb opponent's power for encounter.",
        "super": "Super: Permanently absorb opponent's power."
    },
    "Guerrilla": {
        "wild": "Wild: Ambush - surprise attack bonus.",
        "super": "Super: Major ambush - double surprise bonus."
    },
    "Herald": {
        "wild": "Wild: Announce - know results before commit.",
        "super": "Super: Change results after announcement."
    },
    "Informer": {
        "wild": "Wild: Spy - see all hidden info.",
        "super": "Super: Control what others see."
    },
    "Klutz": {
        "wild": "Wild: Accidentally beneficial fumble.",
        "super": "Super: Controlled chaos in your favor."
    },
    "Manifold": {
        "wild": "Wild: Split into multiple encounters.",
        "super": "Super: Fight on all fronts simultaneously."
    },
    "Merchant": {
        "wild": "Wild: Trade cards freely.",
        "super": "Super: Monopolize trading."
    },
    "Minimalist": {
        "wild": "Wild: Less is more - 1 ship = 4.",
        "super": "Super: 1 ship = 10."
    },
    "Nano": {
        "wild": "Wild: Tiny ships infiltrate.",
        "super": "Super: Nano-swarm overwhelms."
    },
    "Outcast": {
        "wild": "Wild: Exile power - remove one alien.",
        "super": "Super: Exile multiple aliens."
    },
    "Pacifist": {
        "wild": "Wild: Peace bonus if negotiate.",
        "super": "Super: Force peace - no combat this encounter."
    },
    "Patriot": {
        "wild": "Wild: Home bonus +5.",
        "super": "Super: Home bonus +15."
    },
    "Porcupine": {
        "wild": "Wild: Damage attackers.",
        "super": "Super: Devastating counter-attack."
    },
    "Pragmatist": {
        "wild": "Wild: Choose optimal outcome.",
        "super": "Super: Guarantee best outcome."
    },
    "Prodigy": {
        "wild": "Wild: Learn one power.",
        "super": "Super: Master multiple powers."
    },
    "Schemer": {
        "wild": "Wild: Plot - set up future advantage.",
        "super": "Super: Execute master plan."
    },
    "Sergeant": {
        "wild": "Wild: Command allies.",
        "super": "Super: Override ally decisions."
    },
    "Skeptic": {
        "wild": "Wild: Doubt - force proof of claims.",
        "super": "Super: Deny any claim or action."
    },
    "Squatter": {
        "wild": "Wild: Refuse to leave colony.",
        "super": "Super: Spread to adjacent colonies."
    },
    "Standardizer": {
        "wild": "Wild: All cards become 10s.",
        "super": "Super: All cards become 20s."
    },
    "Surgeon": {
        "wild": "Wild: Surgical strike - precise damage.",
        "super": "Super: Total surgical control."
    },
    "Tyrant": {
        "wild": "Wild: Oppress - reduce opponent options.",
        "super": "Super: Total control of opponents."
    },
    "Usurper": {
        "wild": "Wild: Steal one benefit.",
        "super": "Super: Steal victory condition."
    },
    "Visionary": {
        "wild": "Wild: See future - know next 3 cards.",
        "super": "Super: Control the future."
    },
    "Witch": {
        "wild": "Wild: Hex - negative effect on opponent.",
        "super": "Super: Mass hex on all opponents."
    },
    # Cosmic Eons Expansion
    "Assessor": {
        "wild": "Wild: Evaluate hands.",
        "super": "Super: Adjust based on evaluation."
    },
    "Busybody": {
        "wild": "Wild: Interfere in other encounters.",
        "super": "Super: Control other encounters."
    },
    "Doppelganger": {
        "wild": "Wild: Mirror one player.",
        "super": "Super: Become any player."
    },
    "Extremist": {
        "wild": "Wild: All or nothing gamble.",
        "super": "Super: Control the extreme outcome."
    },
    "Nanny": {
        "wild": "Wild: Protect one player.",
        "super": "Super: Protect all allies."
    },
    "Nomad": {
        "wild": "Wild: Wander - gain temporary colonies.",
        "super": "Super: Permanent nomadic settlements."
    },
    "Perfectionist": {
        "wild": "Wild: Redo if imperfect.",
        "super": "Super: Achieve perfection."
    },
    "Poison": {
        "wild": "Wild: Toxic - lingering damage.",
        "super": "Super: Lethal toxin."
    },
    "Recruiter": {
        "wild": "Wild: Conscript ships.",
        "super": "Super: Mass conscription."
    },
    "Sloth": {
        "wild": "Wild: Slow but steady bonus.",
        "super": "Super: Patience rewarded greatly."
    },
    "Soothsayer": {
        "wild": "Wild: Predict outcome.",
        "super": "Super: Make prediction come true."
    },
    "Temporal": {
        "wild": "Wild: Time manipulation.",
        "super": "Super: Full time control."
    },
    "Twin": {
        "wild": "Wild: Split ships equally.",
        "super": "Super: Double presence everywhere."
    },
    "Virus": {
        "wild": "Wild: Infect - spread to opponent.",
        "super": "Super: Pandemic - spread everywhere."
    },
    "Witness": {
        "wild": "Wild: Testify - reveal truths.",
        "super": "Super: Uncover all secrets."
    },
}


# Flare Power Rankings (1-5 scale, 5 being most powerful)
# Rankings consider both Wild and Super effects
FLARE_POWER_RANKINGS = {
    # Tier S (5.0) - Game-changing flares
    "Anarchist": 5.0,  # Can ignore rules entirely
    "Machine": 5.0,    # Extra encounters are extremely powerful
    "Virus": 5.0,      # Ship multiplication is devastating
    "Loser": 5.0,      # Auto-win mechanic
    "Chronos": 5.0,    # Extra turns
    "Tick-Tock": 5.0,  # Alternate win condition

    # Tier A (4.5) - Very powerful flares
    "Zombie": 4.5,     # Warp recovery is always useful
    "Oracle": 4.5,     # Information advantage
    "Sorcerer": 4.5,   # Card/hand swapping
    "Macron": 4.5,     # Ship multiplier
    "Trader": 4.5,     # Hand swapping
    "Clone": 4.5,      # Card reuse
    "Reincarnator": 4.5,  # Power changing
    "Silencer": 4.5,   # Power cancellation
    "Magician": 4.5,   # Hand control
    "Pentaform": 4.5,  # Multiple powers

    # Tier B (4.0) - Strong flares
    "Human": 4.0,      # Solid bonus
    "Warrior": 4.0,    # Warp-based bonus
    "Pacifist": 4.0,   # Negotiate bonus
    "Parasite": 4.0,   # Alliance manipulation
    "Healer": 4.0,     # Mass ship recovery
    "Void": 4.0,       # Permanent removal
    "Filch": 4.0,      # Card theft
    "Assassin": 4.0,   # Ship elimination
    "Saboteur": 4.0,   # Card reduction
    "Kamikaze": 4.0,   # High risk/reward
    "Tripler": 4.0,    # Value multiplication
    "Dictator": 4.0,   # Card control
    "Glutton": 4.0,    # Power absorption

    # Tier C (3.5) - Good flares
    "Shadow": 3.5,     # Ship addition
    "Warpish": 3.5,    # Ship removal
    "Symbiote": 3.5,   # Ship doubling
    "Chosen": 3.5,     # Deck bonus
    "Gambler": 3.5,    # Risk/reward
    "Mutant": 3.5,     # Card filtering
    "Grudge": 3.5,     # Conditional bonus
    "Spiff": 3.5,      # Rewards deck
    "Calculator": 3.5, # Hand-size bonus
    "Negator": 3.5,    # Power cancellation
    "Claw": 3.5,       # Card theft
    "Locust": 3.5,     # Loss compensation
    "Sting": 3.5,      # Retaliation
    "Leviathan": 3.5,  # High bonus
    "Deuce": 3.5,      # Card options

    # Tier D (3.0) - Average flares
    "Fodder": 3.0,     # Ship sacrifice
    "Horde": 3.0,      # Limited recovery
    "Roach": 3.0,      # Situational recovery
    "Remora": 3.0,     # Passive draw
    "Disease": 3.0,    # Ship spreading
    "Mirror": 3.0,     # Value manipulation
    "Ethic": 3.0,      # Information reveal
    "Sniveler": 3.0,   # Card/destiny manipulation
    "Mite": 3.0,       # Deck manipulation
    "Vulture": 3.0,    # Conditional draw
    "Grief": 3.0,      # Shared damage
    "Phantom": 3.0,    # Warp avoidance
    "Diplomat": 3.0,   # Deal manipulation
    "Hate": 3.0,       # Nemesis bonus
    "Grumpus": 3.0,    # Mutual discard
    "Mouth": 3.0,      # Negotiate enhancement
    "Barbarian": 3.0,  # Pillage cards
    "Cryo": 3.0,       # Ship freezing

    # Tier E (2.5) - Below average flares
    "Masochist": 2.5,  # Very situational
    "Fido": 2.5,       # Discard retrieval
    "Genius": 2.5,     # Card draw
    "Reserve": 2.5,    # Reinforcement bonus
    "Quartermaster": 2.5,  # Card retrieval
    "Emigre": 2.5,     # Ship movement
    "Butler": 2.5,     # Card distribution
    "Aristocrat": 2.5, # Colony-based draw
    "Crawler": 2.5,    # Warp escape
    "Ghoul": 2.5,      # Ally warp recovery
    "Industrialist": 2.5,  # Ship building

    # Default rating for unranked flares
    "_default": 3.0,
}


def get_flare_power_rating(alien_name: str) -> float:
    """Get the power rating for a flare (1-5 scale)."""
    return FLARE_POWER_RANKINGS.get(alien_name, FLARE_POWER_RANKINGS["_default"])


def get_top_flares(n: int = 20) -> List[tuple]:
    """Get the top N most powerful flares."""
    ranked = [(name, rating) for name, rating in FLARE_POWER_RANKINGS.items()
              if name != "_default"]
    ranked.sort(key=lambda x: x[1], reverse=True)
    return ranked[:n]


def get_flares_by_tier() -> Dict[str, List[str]]:
    """Get flares organized by power tier."""
    tiers = {
        "S (5.0)": [],
        "A (4.5)": [],
        "B (4.0)": [],
        "C (3.5)": [],
        "D (3.0)": [],
        "E (2.5)": [],
    }
    for name, rating in FLARE_POWER_RANKINGS.items():
        if name == "_default":
            continue
        if rating == 5.0:
            tiers["S (5.0)"].append(name)
        elif rating == 4.5:
            tiers["A (4.5)"].append(name)
        elif rating == 4.0:
            tiers["B (4.0)"].append(name)
        elif rating == 3.5:
            tiers["C (3.5)"].append(name)
        elif rating == 3.0:
            tiers["D (3.0)"].append(name)
        else:
            tiers["E (2.5)"].append(name)
    return tiers
