"""
Simulation runner and statistics for Cosmic Encounter.
"""

from .runner import Simulator, SimulationResult
from .stats import Statistics
from .cumulative_stats import CumulativeStats, AlienEloStats, EloCalculator
from .power_analysis import PowerBalanceAnalyzer, BalanceReport, PowerTier, run_analysis
from .matchup_analysis import (
    MatchupAnalyzer,
    MatchupMatrix,
    MatchupResult,
    run_quick_matchup,
    find_counters,
)
from .tournament import (
    Tournament,
    RoundRobinTournament,
    SwissTournament,
    MonteCarloEstimator,
    SynergyMatrix,
    TournamentResults,
    run_quick_tournament,
    run_monte_carlo_analysis,
)
from .visualization import (
    PerformanceChart,
    GameAnalysisReport,
    PowerComparisonReport,
    generate_quick_report,
    compare_aliens,
)
from .replay import (
    GameRecording,
    GameRecorder,
    GameReplayer,
    GameAnalyzer,
    GameEvent,
    EventType,
    record_game,
    analyze_recording,
)
from .analysis import (
    SimulationAnalyzer,
    PowerBalanceReport,
    GameLengthReport,
    EloDistributionReport,
    analyze_stats_file,
)

__all__ = [
    "Simulator",
    "SimulationResult",
    "Statistics",
    "CumulativeStats",
    "AlienEloStats",
    "EloCalculator",
    "PowerBalanceAnalyzer",
    "BalanceReport",
    "PowerTier",
    "run_analysis",
    "MatchupAnalyzer",
    "MatchupMatrix",
    "MatchupResult",
    "run_quick_matchup",
    "find_counters",
    "Tournament",
    "RoundRobinTournament",
    "SwissTournament",
    "MonteCarloEstimator",
    "SynergyMatrix",
    "TournamentResults",
    "run_quick_tournament",
    "run_monte_carlo_analysis",
    # Visualization
    "PerformanceChart",
    "GameAnalysisReport",
    "PowerComparisonReport",
    "generate_quick_report",
    "compare_aliens",
    # Replay
    "GameRecording",
    "GameRecorder",
    "GameReplayer",
    "GameAnalyzer",
    "GameEvent",
    "EventType",
    "record_game",
    "analyze_recording",
    # Analysis
    "SimulationAnalyzer",
    "PowerBalanceReport",
    "GameLengthReport",
    "EloDistributionReport",
    "analyze_stats_file",
]
