"""
Game Replay and Recording System for Cosmic Encounter.

Provides functionality to:
- Record game events and state changes
- Save and load game recordings
- Replay games step by step
- Analyze game flow and key decision points
"""

import json
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Any
from pathlib import Path
from datetime import datetime
from enum import Enum

from ..types import GamePhase


class EventType(Enum):
    """Types of game events that can be recorded."""
    GAME_START = "game_start"
    TURN_START = "turn_start"
    PHASE_CHANGE = "phase_change"
    DESTINY_DRAWN = "destiny_drawn"
    SHIPS_COMMITTED = "ships_committed"
    ALLIANCE_INVITED = "alliance_invited"
    ALLIANCE_ACCEPTED = "alliance_accepted"
    CARD_PLAYED = "card_played"
    CARDS_REVEALED = "cards_revealed"
    COMBAT_RESOLVED = "combat_resolved"
    NEGOTIATION_RESULT = "negotiation_result"
    SHIPS_TO_WARP = "ships_to_warp"
    COLONY_ESTABLISHED = "colony_established"
    POWER_USED = "power_used"
    POWER_ZAPPED = "power_zapped"
    ARTIFACT_PLAYED = "artifact_played"
    FLARE_PLAYED = "flare_played"
    TECH_USED = "tech_used"
    HAZARD_DRAWN = "hazard_drawn"
    PLAYER_WINS = "player_wins"
    GAME_END = "game_end"


@dataclass
class GameEvent:
    """A single recorded game event."""
    timestamp: float  # Seconds since game start
    turn: int
    encounter: int
    phase: str
    event_type: str
    player: Optional[str]
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "turn": self.turn,
            "encounter": self.encounter,
            "phase": self.phase,
            "event_type": self.event_type,
            "player": self.player,
            "details": self.details,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameEvent":
        return cls(**data)


@dataclass
class GameSnapshot:
    """Snapshot of game state at a point in time."""
    turn: int
    encounter: int
    phase: str
    offense: str
    defense: str
    players: List[Dict[str, Any]]  # Simplified player states

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameSnapshot":
        return cls(**data)


@dataclass
class GameRecording:
    """Complete recording of a game."""
    game_id: str
    recorded_at: str
    config: Dict[str, Any]
    players: List[Dict[str, str]]  # name, alien, color
    events: List[GameEvent] = field(default_factory=list)
    snapshots: List[GameSnapshot] = field(default_factory=list)
    result: Optional[Dict[str, Any]] = None

    def add_event(self, event: GameEvent) -> None:
        """Add an event to the recording."""
        self.events.append(event)

    def add_snapshot(self, snapshot: GameSnapshot) -> None:
        """Add a state snapshot."""
        self.snapshots.append(snapshot)

    def get_events_by_type(self, event_type: EventType) -> List[GameEvent]:
        """Get all events of a specific type."""
        return [e for e in self.events if e.event_type == event_type.value]

    def get_events_for_player(self, player_name: str) -> List[GameEvent]:
        """Get all events involving a specific player."""
        return [e for e in self.events if e.player == player_name]

    def get_turn_events(self, turn: int) -> List[GameEvent]:
        """Get all events from a specific turn."""
        return [e for e in self.events if e.turn == turn]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "game_id": self.game_id,
            "recorded_at": self.recorded_at,
            "config": self.config,
            "players": self.players,
            "events": [e.to_dict() for e in self.events],
            "snapshots": [s.to_dict() for s in self.snapshots],
            "result": self.result,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GameRecording":
        recording = cls(
            game_id=data["game_id"],
            recorded_at=data["recorded_at"],
            config=data["config"],
            players=data["players"],
            result=data.get("result"),
        )
        recording.events = [GameEvent.from_dict(e) for e in data.get("events", [])]
        recording.snapshots = [GameSnapshot.from_dict(s) for s in data.get("snapshots", [])]
        return recording

    def save(self, filepath: Path) -> None:
        """Save recording to JSON file."""
        with open(filepath, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load(cls, filepath: Path) -> "GameRecording":
        """Load recording from JSON file."""
        with open(filepath, 'r') as f:
            return cls.from_dict(json.load(f))


class GameRecorder:
    """
    Records game events as they happen.

    Usage:
        recorder = GameRecorder(game)
        recorder.start()
        # ... game plays ...
        recording = recorder.stop()
        recording.save("game_recording.json")
    """

    def __init__(self, game: Any):
        """
        Initialize recorder.

        Args:
            game: Game instance to record
        """
        self.game = game
        self.recording: Optional[GameRecording] = None
        self.start_time: float = 0.0
        self.is_recording: bool = False

    def start(self) -> None:
        """Start recording the game."""
        import time
        import uuid

        self.start_time = time.time()
        self.is_recording = True

        # Create recording
        self.recording = GameRecording(
            game_id=str(uuid.uuid4())[:8],
            recorded_at=datetime.now().isoformat(),
            config=asdict(self.game.config) if hasattr(self.game.config, '__dataclass_fields__') else {},
            players=[
                {
                    "name": p.name,
                    "alien": p.alien.name if p.alien else "None",
                    "color": p.color.value if hasattr(p, 'color') and p.color else "unknown",
                }
                for p in self.game.players
            ],
        )

        # Record game start
        self.record_event(EventType.GAME_START, details={
            "num_players": len(self.game.players),
            "aliens": [p.alien.name if p.alien else "None" for p in self.game.players],
        })

    def stop(self) -> GameRecording:
        """Stop recording and return the recording."""
        self.is_recording = False

        # Record game end
        self.record_event(EventType.GAME_END, details={
            "winners": [w.name for w in self.game.winners] if self.game.winners else [],
            "turns": self.game.current_turn,
        })

        # Set result
        if self.recording:
            self.recording.result = {
                "winners": [w.name for w in self.game.winners] if self.game.winners else [],
                "total_turns": self.game.current_turn,
                "final_colonies": {
                    p.name: p.count_foreign_colonies(self.game.planets)
                    for p in self.game.players
                },
            }

        return self.recording

    def record_event(
        self,
        event_type: EventType,
        player: Optional[str] = None,
        details: Optional[Dict[str, Any]] = None
    ) -> None:
        """Record a game event."""
        if not self.is_recording or not self.recording:
            return

        import time

        event = GameEvent(
            timestamp=time.time() - self.start_time,
            turn=self.game.current_turn,
            encounter=self.game.encounter_number,
            phase=self.game.phase.value if self.game.phase else "unknown",
            event_type=event_type.value,
            player=player,
            details=details or {},
        )

        self.recording.add_event(event)

    def record_snapshot(self) -> None:
        """Record current game state snapshot."""
        if not self.is_recording or not self.recording:
            return

        snapshot = GameSnapshot(
            turn=self.game.current_turn,
            encounter=self.game.encounter_number,
            phase=self.game.phase.value if self.game.phase else "unknown",
            offense=self.game.offense.name if self.game.offense else "None",
            defense=self.game.defense.name if self.game.defense else "None",
            players=[
                {
                    "name": p.name,
                    "hand_size": len(p.hand),
                    "ships_in_warp": p.ships_in_warp,
                    "foreign_colonies": p.count_foreign_colonies(self.game.planets),
                    "home_colonies": len([pl for pl in self.game.planets if pl.owner == p and pl.has_colony(p.name)]),
                    "power_active": p.power_active,
                }
                for p in self.game.players
            ],
        )

        self.recording.add_snapshot(snapshot)


class GameReplayer:
    """
    Replays a recorded game step by step.
    """

    def __init__(self, recording: GameRecording):
        """
        Initialize replayer.

        Args:
            recording: GameRecording to replay
        """
        self.recording = recording
        self.current_index = 0
        self.current_turn = 1

    def reset(self) -> None:
        """Reset to beginning of recording."""
        self.current_index = 0
        self.current_turn = 1

    def step(self) -> Optional[GameEvent]:
        """Advance to next event and return it."""
        if self.current_index >= len(self.recording.events):
            return None

        event = self.recording.events[self.current_index]
        self.current_index += 1
        self.current_turn = event.turn
        return event

    def step_back(self) -> Optional[GameEvent]:
        """Go back to previous event."""
        if self.current_index <= 1:
            return None

        self.current_index -= 1
        event = self.recording.events[self.current_index - 1] if self.current_index > 0 else None
        if event:
            self.current_turn = event.turn
        return event

    def go_to_turn(self, turn: int) -> Optional[GameEvent]:
        """Jump to start of a specific turn."""
        for i, event in enumerate(self.recording.events):
            if event.turn == turn:
                self.current_index = i
                self.current_turn = turn
                return event
        return None

    def get_remaining_events(self) -> int:
        """Get number of remaining events."""
        return len(self.recording.events) - self.current_index

    def get_progress(self) -> float:
        """Get replay progress as percentage."""
        if not self.recording.events:
            return 100.0
        return self.current_index / len(self.recording.events) * 100


class GameAnalyzer:
    """
    Analyzes recorded games for insights.
    """

    def __init__(self, recording: GameRecording):
        """
        Initialize analyzer.

        Args:
            recording: GameRecording to analyze
        """
        self.recording = recording

    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics of the game."""
        events = self.recording.events

        return {
            "game_id": self.recording.game_id,
            "total_events": len(events),
            "total_turns": max((e.turn for e in events), default=0),
            "players": len(self.recording.players),
            "winners": self.recording.result.get("winners", []) if self.recording.result else [],
            "alien_powers": [p["alien"] for p in self.recording.players],
        }

    def get_power_usage_stats(self) -> Dict[str, int]:
        """Get statistics on power usage."""
        power_events = self.recording.get_events_by_type(EventType.POWER_USED)

        usage = {}
        for event in power_events:
            player = event.player or "Unknown"
            usage[player] = usage.get(player, 0) + 1

        return usage

    def get_combat_stats(self) -> Dict[str, Any]:
        """Get combat statistics."""
        combat_events = self.recording.get_events_by_type(EventType.COMBAT_RESOLVED)

        total_combats = len(combat_events)
        offense_wins = sum(1 for e in combat_events if e.details.get("winner") == "offense")
        defense_wins = sum(1 for e in combat_events if e.details.get("winner") == "defense")

        return {
            "total_combats": total_combats,
            "offense_wins": offense_wins,
            "defense_wins": defense_wins,
            "offense_win_rate": offense_wins / total_combats if total_combats > 0 else 0,
        }

    def get_alliance_stats(self) -> Dict[str, int]:
        """Get alliance invitation and acceptance statistics."""
        invited = len(self.recording.get_events_by_type(EventType.ALLIANCE_INVITED))
        accepted = len(self.recording.get_events_by_type(EventType.ALLIANCE_ACCEPTED))

        return {
            "invitations": invited,
            "acceptances": accepted,
            "acceptance_rate": accepted / invited if invited > 0 else 0,
        }

    def get_turning_points(self) -> List[GameEvent]:
        """
        Identify key turning points in the game.

        Turning points include:
        - First colony established
        - Power zaps
        - Major combat victories
        - Winning moves
        """
        turning_points = []

        # First colony for each player
        seen_colonies = set()
        for event in self.recording.get_events_by_type(EventType.COLONY_ESTABLISHED):
            player = event.player
            if player and player not in seen_colonies:
                seen_colonies.add(player)
                turning_points.append(event)

        # All power zaps
        turning_points.extend(self.recording.get_events_by_type(EventType.POWER_ZAPPED))

        # Player wins
        turning_points.extend(self.recording.get_events_by_type(EventType.PLAYER_WINS))

        # Sort by timestamp
        turning_points.sort(key=lambda e: e.timestamp)

        return turning_points

    def generate_narrative(self) -> str:
        """Generate a narrative summary of the game."""
        lines = [
            f"=== Game {self.recording.game_id} ===",
            f"Recorded: {self.recording.recorded_at}",
            "",
            "Players:",
        ]

        for p in self.recording.players:
            lines.append(f"  - {p['name']}: {p['alien']}")

        lines.append("")

        summary = self.get_summary()
        lines.extend([
            f"Total turns: {summary['total_turns']}",
            f"Total events: {summary['total_events']}",
        ])

        # Key moments
        turning_points = self.get_turning_points()
        if turning_points:
            lines.extend(["", "Key Moments:"])
            for tp in turning_points[:10]:  # Show top 10
                lines.append(
                    f"  Turn {tp.turn}: {tp.event_type} - {tp.player or 'N/A'}"
                )

        # Result
        if self.recording.result:
            lines.extend([
                "",
                "Result:",
                f"  Winners: {', '.join(self.recording.result.get('winners', ['None']))}",
            ])

        return "\n".join(lines)


def record_game(game: Any) -> GameRecording:
    """
    Quick function to record a game.

    Args:
        game: Game instance (should be set up but not yet played)

    Returns:
        GameRecording of the completed game
    """
    recorder = GameRecorder(game)
    recorder.start()

    # Play the game
    game.play()

    return recorder.stop()


def analyze_recording(filepath: str) -> str:
    """
    Quick function to analyze a saved recording.

    Args:
        filepath: Path to recording JSON file

    Returns:
        Analysis report as string
    """
    recording = GameRecording.load(Path(filepath))
    analyzer = GameAnalyzer(recording)
    return analyzer.generate_narrative()


if __name__ == "__main__":
    print("Replay system module loaded")
    print("Use record_game(game) to record a game")
    print("Use analyze_recording('file.json') to analyze a saved recording")
