from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class TrackBox:
    frame: int
    xtl: float
    ytl: float
    xbr: float
    ybr: float
    outside: bool
    occluded: bool
    keyframe: bool
    attributes: Dict[str, str] = field(default_factory=dict)

@dataclass
class Track:
    xml_track_id: str
    label: str
    source: str
    attributes: Dict[str, str] = field(default_factory=dict)
    boxes_by_frame: Dict[int, TrackBox] = field(default_factory=dict)
    position: Optional[str] = None
    team_side: Optional[str] = None
    custom_track_id: Optional[str] = None

@dataclass
class ActionEvent:
    video_name: Optional[str] = None
    video_id: Optional[str] = None
    play_tag: Optional[str] = None
    result_tag: Optional[str] = None
    result_frame: Optional[int] = None
    action: str = ""
    start_frame: int = 0
    actor_track_id: Optional[str] = None
    resolved_xml_track_id: Optional[str] = None
    target_kind: str = "global_event"  # track_id, group, global_event, ball
    source_column: str = ""
    actor_position: Optional[str] = None
    notes: Optional[str] = None
    annotated_frame: int = 0
    annotated_frame_role: str = "START"  # "START", "END", "BOUNDARY", "INSTANT"
    event_type: str = "PRIMARY_ACTION"   # "PRIMARY_ACTION", "BOUNDARY", "PLAY_END"

    def __post_init__(self):
        if self.annotated_frame == 0 and self.start_frame != 0:
            self.annotated_frame = self.start_frame
        elif self.start_frame == 0 and self.annotated_frame != 0:
            self.start_frame = self.annotated_frame

@dataclass
class ActionSegment:
    actor_track_id: str
    xml_track_id: str
    position: Optional[str]
    team_side: Optional[str]
    action: str
    start_frame: int
    end_frame: int
    source: str
    confidence: Optional[float] = None

@dataclass
class DenseActionAnnotation:
    frame: int
    actor_track_id: str
    xml_track_id: str
    position: Optional[str]
    team_side: Optional[str]
    action: str
    bbox_xyxy: List[float]
    bbox_xywh: List[float]
    source: str = "xml_geometry_csv_action"
