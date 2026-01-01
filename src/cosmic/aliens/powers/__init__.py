"""
Official Fantasy Flight Games Cosmic Encounter alien powers.

Only imports files containing official FFG aliens from:
- Base Game (2008): 50 aliens
- Cosmic Incursion (2009): 20 aliens  
- Cosmic Conflict (2011): 20 aliens
- Cosmic Alliance (2012): 20 aliens
- Cosmic Storm (2013): 25 aliens
- Cosmic Dominion (2014): 30 aliens
- Cosmic Eons (2016): 30 aliens
- Cosmic Odyssey (2022): 42 aliens
- Promos: 2 aliens

Total: ~238 official aliens
"""

# Core official alien files
from .base_powers import *  # noqa: F401, F403
from .combat_powers import *  # noqa: F401, F403
from .special_powers import *  # noqa: F401, F403
from .missing_official_powers import *  # noqa: F401, F403
from .odyssey_alt_powers import *  # noqa: F401, F403
from .expansion_powers import *  # noqa: F401, F403
