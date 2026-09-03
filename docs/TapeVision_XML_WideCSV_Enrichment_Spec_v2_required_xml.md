# AI Specification Document

Use this template to clearly define tasks and expectations for any AI system.  
It follows the **GIRSOE framework** to ensure clarity and consistency.

---

## **1. Goal**

The goal of this project is to build a codebase that treats the **CVAT for Video XML export as the source of truth** for the FilmBreakdownAI / TapeVision annotation pipeline and uses an external **wide-format action CSV/spreadsheet only as a supplemental source for missing temporal action information**.

The XML file should remain the authoritative annotation record because it preserves the most important data for the project: player tracks, ball tracks, bounding boxes, frame numbers, object identities, player positions, team-side metadata, and clip-level annotation structure. The action CSV should not replace the XML or become a separate competing annotation source. Instead, the CSV should be used to enrich the XML-derived annotation data by adding action start points and action labels that were too slow to annotate directly inside CVAT.

The system should parse the CVAT XML file, extract all existing player and ball tracks, preserve each track’s identity across the full video, and build a frame-level lookup of each track’s bounding boxes and attributes. Then, the system should parse the wide-format action CSV and use each video row plus its action columns to add missing action information to the correct XML tracks by matching each CSV action entry to the appropriate player track ID and frame number.

The primary task is to automatically fill in frame-level player action labels using sparse action start-frame information from the wide CSV while keeping the XML track geometry unchanged. The codebase should use the **Option A: Start-frame only** convention as the default action-range strategy:

- Each action begins at the frame listed in the CSV.
- The action is assigned to the player track ID, group target, ball target, or global event target listed in the wide CSV cell.
- The action continues forward until the system determines that the action has ended.
- By default, an action ends one frame before the next listed action for the same player track.
- If no next action is listed for that player, the action continues until the end of the play, the end of the clip, or until an action-ending rule determines that the action should stop.

The codebase should also support a configurable **action-ending rules system**. These rules should allow the program to infer when certain football actions should end without requiring the annotator to manually provide an end frame for every action. For example, the system should be able to use rules such as:

- `Action_PreSnap` ends when `Action_BallSnap` begins.
- A player’s current action ends when a new action is listed for that same player track.
- `Action_BallSnap` may last for a short predefined frame window or end when `Action_SnapReceive` begins.
- `Action_Handoff` may end when `Action_TakeHandoff` or `Action_BallCarry` begins.
- Blocking actions such as `Action_ZoneBlock`, `Action_ReachBlock`, `Action_DownBlock`, or `Action_PullBlock` may end when another action begins for that player, when the play ends, or when a configured maximum duration is reached.
- `Action_BallCarry` may continue until the result frame, play-end frame, or another ball-status-changing event.
- `Action_PlayEnd` should end at the final frame of the clip.
- If the action ending cannot be inferred confidently, the system should either continue the action until the next known boundary or mark the uncertain range according to a configurable policy.

The AI/codebase is trying to accomplish the following:

- Keep the CVAT XML export as the authoritative source of truth.
- Preserve accurate player and ball tracks from the XML.
- Preserve correct track IDs, bounding boxes, frame numbers, positions, and team-side metadata.
- Use the wide CSV only to add missing temporal action labels to existing XML tracks.
- Avoid manually drawing action bounding boxes in CVAT.
- Convert sparse wide-format action start-frame entries into dense frame-level action annotations.
- Apply configurable rules to infer when actions end.
- Ensure each player has no more than one primary action label per frame.
- Allow defensive players or non-action-labeled players to remain in the XML as contextual tracks without requiring full action supervision.
- Validate that every CSV `actor_track_id` exists in the XML before applying action labels.
- Report missing track IDs, invalid frame numbers, overlapping action ranges, undefined actions, and other annotation issues.
- Produce an enriched output that can be used for TapeVision model training, evaluation, automated annotation, and structured JSON generation.

The expected outcome is a repeatable conversion/enrichment pipeline that takes:

```text
CVAT for Video XML export + sparse wide-format action CSV
```

and produces:

```text
an enriched TapeVision-ready annotation dataset
```

where the original XML track geometry remains intact, and the missing action information from the spreadsheet is added programmatically using track IDs, frame numbers, and football-specific action-ending rules.

---

## **2. Inputs**

The codebase should support the following inputs.

### **2.1 CVAT for Video XML Export**

The CVAT XML file is the source of truth. It contains the original annotation structure exported from CVAT for video tasks.

The XML is expected to contain:

- Video/task metadata.
- Label definitions.
- `<track>` elements for players and the ball.
- `<box>` elements inside each track, one per visible/interpolated frame.
- Frame numbers.
- Bounding box coordinates:
  - `xtl`
  - `ytl`
  - `xbr`
  - `ybr`
- Track-level or box-level attributes, such as:
  - `position`
  - `team_side`
  - `track_id`
  - `ball_status`
  - `occluded`
  - `outside`
  - `keyframe`

The XML should be parsed as the authoritative geometry and identity source. The program must not rewrite or reinterpret player identity from the CSV when the XML provides the official track structure.

### **2.2 Action CSV / Spreadsheet Export**

The action CSV is a supplemental annotation file that adds sparse temporal action information. The CSV should be designed for fast human entry during film review, so the required input format should be a **wide spreadsheet format**, not a long row-per-action format.

The wide CSV should have **one row per video/clip** and **one column per key action or event**. Each action cell should contain the frame number where the action starts and the player track ID that performs the action. This matches the manual sequence-logging workflow and avoids requiring the annotator to write many repeated long-format rows.

#### **Required Wide Format**

Recommended columns:

```csv
video_name,video_id,play_tag,result_tag,result_frame,pre_snap,jet_motion,ball_snap,zone_block,snap_receive,toss,ball_carry,seal_block,lead_block,block_second_level,end_ol_block,end_play,notes
```

Recommended action cell format:

```text
frame_number, player_track_id
```

Examples:

```text
jet_motion = 23,16
ball_snap = 34,33
zone_block = 43,2
snap_receive = 49,8
toss = 55,8
ball_carry = 65,16
lead_block = 35,11
block_second_level = 67,2
end_ol_block = 100,OL
end_play = 116
```

The program should parse each non-empty action column, map the column name to a configured TapeVision action label, and convert the cell value into an internal action event. Internally, the codebase may normalize the wide CSV into an `ActionEvent` list, but the user-facing input requirement must remain wide format. The annotator should not be required to manually create a long-format CSV.

#### **Wide Cell Parsing Rules**

The parser should support these cell patterns:

```text
frame,track_id          # example: 43,2
frame,track_id;frame,track_id   # example: 43,2;43,4 for multiple players doing same action
frame,ALL_OFFENSE      # example: 0,ALL_OFFENSE for pre-snap
frame,OL               # example: 100,OL for all offensive linemen or configured position group
frame                  # example: 116 for global/end-of-play event
blank                  # no action/event for this video/action column
```

The parser should trim whitespace and accept common separators such as comma, semicolon, pipe, or newline for multiple entries in a single cell.

#### **Action Column Mapping**

The config file should define how wide CSV column names map to canonical TapeVision action labels. Example:

```yaml
csv:
  format: wide
  action_columns:
    pre_snap: Action_PreSnap
    jet_motion: Action_JetMotion
    ball_snap: Action_BallSnap
    zone_block: Action_ZoneBlock
    snap_receive: Action_SnapReceive
    toss: Action_Toss
    ball_carry: Action_BallCarry
    seal_block: Action_SealBlock
    lead_block: Action_LeadBlock
    block_second_level: Action_BlockSecondLevel
    end_ol_block: Action_None
    end_play: Action_PlayEnd
```

#### **Optional Long Format**

The codebase may optionally support long format for debugging or generated intermediate files, but long format should not be required from the annotator. If long format support is implemented, it should be treated as an internal normalized representation or advanced input mode only.

### **2.3 Optional Configuration File**

The codebase should support a YAML or JSON configuration file for project-specific settings.

The configuration should define:

- Input XML path.
- Input CSV path.
- Output directory.
- Expected label names:
  - player label name, usually `player` or `Player`
  - ball label name, usually `ball` or `Ball`
- CSV column mappings.
- Whether to include defensive players in dense output.
- Whether to include ball tracks in dense output.
- Global play-end behavior.
- Action-ending rules.
- Default actions for unlabeled frames.
- Maximum durations for specific action types.
- Validation strictness level.

Example:

```yaml
input:
  cvat_xml: data/xml/sampleJetSweepCVAT_video_2.xml
  action_csv: data/actions/sample_sequence_logger.csv

output:
  output_dir: outputs/
  write_enriched_xml: true
  write_tapevision_json: true
  write_validation_report: true

labels:
  player_label: player
  ball_label: ball

csv:
  format: wide
  columns:
    video_name: video_name
    video_id: video_id
    play_tag: play_tag
    result_tag: result_tag
    result_frame: result_frame
    notes: notes
  action_columns:
    pre_snap: Action_PreSnap
    jet_motion: Action_JetMotion
    ball_snap: Action_BallSnap
    zone_block: Action_ZoneBlock
    snap_receive: Action_SnapReceive
    toss: Action_Toss
    ball_carry: Action_BallCarry
    seal_block: Action_SealBlock
    lead_block: Action_LeadBlock
    block_second_level: Action_BlockSecondLevel
    end_ol_block: Action_None
    end_play: Action_PlayEnd
  cell_parsing:
    pair_separator: ","
    multi_entry_separators: [";", "|", "\n"]
    allow_global_frame_only_events: true
    allow_position_group_targets: true

action_policy:
  default_unlabeled_offense_action: Action_Unknown
  default_unlabeled_defense_action: Action_Defense_NotAnnotated
  action_range_mode: start_frame_only
  one_primary_action_per_frame: true

play_end:
  source: csv_result_or_end_of_play
  fallback: final_xml_frame
```

---

## **3. Rules/Constraints**

### **3.1 XML Source-of-Truth Rule**

The CVAT XML file is the source of truth for:

- Track identity.
- Player and ball track structure.
- Bounding boxes.
- Frame numbers.
- Position attributes.
- Team-side attributes.
- Ball annotations.
- Existing CVAT tags and metadata.

The CSV must never overwrite XML geometry or create a new identity system. The CSV may only enrich existing XML tracks with missing temporal action data.

### **3.2 Track Matching Rule**

Each parsed action event from the wide CSV must reference an existing XML player track unless it is explicitly configured as a global event, ball event, or group-target action.

The codebase should support matching by:

1. The CVAT `<track id="...">` value.
2. A custom XML attribute named `track_id`, if present.
3. A configurable mapping file if CVAT display IDs and exported XML track IDs differ.

If a parsed CSV `actor_track_id` does not match any XML track, the system must report the error and either skip the event or stop execution based on the configured validation mode. If a wide CSV cell uses a group target such as `OL`, `ALL_OFFENSE`, or `SKILL`, the system must expand the group using XML `position` and `team_side` attributes before action ranges are inferred.

### **3.3 Start-Frame Only Action Rule**

The wide action CSV should provide action start frames only. End frames are inferred by the program.

Default rule:

```text
For the same resolved actor_track_id:
current_action.end_frame = next_action.start_frame - 1
```

If there is no next action for that player, then the current action should end at the earliest valid boundary from:

1. configured action-ending rule,
2. play-end frame,
3. final visible frame for the track,
4. final frame of the clip.

### **3.4 Wide CSV Input Rule**

The user-facing CSV format must be wide format. The codebase should not require the annotator to write a separate row for every action event.

Required behavior:

- One row represents one video/clip.
- Each configured action column represents one football action or global event.
- Each non-empty action cell is parsed into one or more internal `ActionEvent` records.
- Multiple players can be listed in one cell when they perform the same action at the same start frame.
- Group targets can be used to reduce manual work when the same action applies to a position group.
- Blank cells mean that action was not logged for that video and should not create an event.

Example accepted cell values:

```text
43,2
43,2;43,4
0,ALL_OFFENSE
100,OL
116
```

The program may write an optional normalized long-format debug file, but this must be generated automatically. Long format must not be required as the primary annotation input.

### **3.5 One Primary Action Per Player Per Frame**

Each player track may have no more than one primary action per frame.

If overlapping actions are generated for the same player and frame, the system must resolve the conflict using a deterministic priority policy.

Recommended priority order:

1. Explicit CSV start-frame action for that player.
2. Later action overrides earlier action from its start frame forward.
3. Configured action priority table.
4. If unresolved, mark the frame as invalid and report it.

### **3.6 Do Not Draw or Generate New Geometry Unless Requested**

The codebase should not invent bounding boxes. For action-labeled output, it should copy the existing bounding boxes from the XML player track.

If the player has no visible XML box on a frame inside an action range, the program should follow the configured missing-box policy:

- skip the frame,
- mark the action as missing geometry,
- use the nearest valid box only if explicitly enabled,
- or stop with a validation error.

Default behavior should be to **skip the missing frame and report it**.

### **3.7 Offensive-First Annotation Policy**

The current project phase focuses on offensive player actions.

Defensive players should remain in the XML as context tracks. They should not be deleted.

If dense action output requires an action value for defensive players, use:

```text
Action_Defense_NotAnnotated
```

unless a different value is configured.

### **3.8 Undefined Values Rule**

The system should avoid using `undefined` as a final training label.

If XML or CSV values contain `undefined`, the codebase should treat them as incomplete annotation values and either:

- replace them with a configured default value,
- mark the record as incomplete,
- or report a validation warning/error.

Recommended replacements:

```text
undefined offensive action -> Action_Unknown
undefined defensive action -> Action_Defense_NotAnnotated
undefined position -> Position_Unknown
undefined team_side -> Team_Unknown
```

### **3.9 Preserve Original Files**

The codebase must not overwrite the original CVAT XML or CSV files. All enriched outputs must be written to a new output directory.

### **3.10 Reproducibility Rule**

The conversion process should be deterministic. Running the same XML, CSV, and config should produce the same output every time.

### **3.11 Validation and Logging Rule**

The codebase must produce clear logs and validation reports that help identify annotation mistakes before training data is generated.

The validation report should include:

- Number of XML tracks parsed.
- Number of player tracks.
- Number of ball tracks.
- Number of wide CSV rows parsed.
- Number of non-empty action cells parsed.
- Number of internal action events generated from wide cells.
- Number of group-target events expanded.
- Number of CSV actions successfully matched to XML tracks.
- Missing track IDs.
- Malformed wide CSV cells.
- Unresolved group targets.
- Invalid frames.
- Undefined values.
- Overlapping actions.
- Missing bounding boxes inside action ranges.
- Per-video summary.

---

## **4. Steps/Logic (Optional)**

The codebase should be organized as a clean, modular Python project.

### **4.1 Recommended Folder Structure**

```text
tapevision_xml_action_enricher/
├── README.md
├── requirements.txt
├── pyproject.toml
├── configs/
│   └── default_config.yaml
├── data/
│   ├── xml/
│   └── csv/
├── outputs/
├── src/
│   └── tapevision_enricher/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── cvat_xml_parser.py
│       ├── wide_wide_action_csv_parser.py
│       ├── action_event_normalizer.py
│       ├── action_rules.py
│       ├── enricher.py
│       ├── validators.py
│       ├── writers/
│       │   ├── __init__.py
│       │   ├── enriched_xml_writer.py
│       │   ├── tapevision_json_writer.py
│       │   ├── dense_csv_writer.py
│       │   └── report_writer.py
│       └── models.py
└── tests/
    ├── test_cvat_xml_parser.py
    ├── test_wide_wide_action_csv_parser.py
    ├── test_action_rules.py
    ├── test_enricher.py
    └── test_validators.py
```

### **4.2 Data Models**

Use Python dataclasses or Pydantic models for internal data structures.

Suggested models:

```python
TrackBox:
    frame: int
    xtl: float
    ytl: float
    xbr: float
    ybr: float
    outside: bool
    occluded: bool
    keyframe: bool
    attributes: dict

Track:
    xml_track_id: str
    label: str
    source: str
    attributes: dict
    boxes_by_frame: dict[int, TrackBox]
    position: str | None
    team_side: str | None
    custom_track_id: str | None

ActionEvent:
    video_name: str | None
    video_id: str | None
    play_tag: str | None
    result_tag: str | None
    result_frame: int | None
    action: str
    start_frame: int
    actor_track_id: str | None
    target_kind: str  # track_id, group, global_event, ball
    source_column: str
    actor_position: str | None
    notes: str | None

ActionSegment:
    actor_track_id: str
    action: str
    start_frame: int
    end_frame: int
    source: str
    confidence: float | None

DenseActionAnnotation:
    frame: int
    actor_track_id: str
    action: str
    bbox_xyxy: list[float]
    bbox_xywh: list[float]
    position: str | None
    team_side: str | None
    source_xml_track_id: str
```

### **4.3 Parse CVAT XML**

The XML parser should:

1. Load the CVAT for Video XML file.
2. Extract metadata such as task name, frame count, labels, and original video name if available.
3. Extract all `<track>` elements.
4. For each track:
   - read the XML track ID,
   - read the label,
   - read all boxes,
   - read box attributes,
   - identify `position`, `team_side`, and custom `track_id` values,
   - build a frame-indexed box lookup.
5. Separate tracks into player tracks, ball tracks, and other tracks.

### **4.4 Parse Wide Action CSV**

The CSV parser should:

1. Load the wide CSV.
2. Treat each row as one video/clip.
3. Read video-level fields such as `video_name`, `video_id`, `play_tag`, `result_tag`, `result_frame`, and `notes`.
4. Read configured action columns from the row.
5. Ignore blank action cells.
6. Map each non-empty action column name to a canonical TapeVision action label using the config.
7. Parse each action cell into one or more action events using the supported cell patterns.
8. Convert frame numbers to integers.
9. Convert actor track IDs to strings for consistent matching.
10. Expand configured group targets such as `ALL_OFFENSE`, `OL`, or `SKILL` into concrete XML player track IDs when possible.
11. Return a normalized internal list of `ActionEvent` records.

The code may use an internal normalized long representation, but this must be generated by the program. The human annotator should only need to maintain the wide CSV.

### **4.5 Match CSV Events to XML Tracks**

The enricher should:

1. Build a track lookup from the XML.
2. Try to match each `ActionEvent.actor_track_id` to:
   - XML custom `track_id` attribute,
   - XML `<track id>` value,
   - optional user-provided mapping.
3. Validate that the matched XML track is a player track unless the action is explicitly a ball action.
4. Report unmatched events.

### **4.6 Infer Action Segments**

For each player track:

1. Collect all matched `ActionEvent` records.
2. Sort them by `start_frame`.
3. Create action segments using the start-frame-only convention.
4. Set each segment’s default end frame to one frame before the next action for the same player.
5. For the final action, use the configured action-ending rules to determine the end frame.
6. Clamp all segments to the valid video frame range and the visible track frame range.

Default pseudocode:

```python
for track_id, events in events_by_track.items():
    events = sorted(events, key=lambda e: e.start_frame)

    for i, event in enumerate(events):
        start = event.start_frame

        if i + 1 < len(events):
            end = events[i + 1].start_frame - 1
        else:
            end = infer_final_end_frame(event, xml_track, play_end_frame, final_clip_frame, config)

        segment = ActionSegment(
            actor_track_id=track_id,
            action=event.action,
            start_frame=start,
            end_frame=end,
            source="csv_start_frame_only"
        )
```

### **4.7 Apply Action-Ending Rules**

Implement a configurable rules engine.

Recommended default rules:

```yaml
action_end_rules:
  Action_PreSnap:
    ends_at_global_action: Action_BallSnap
    fallback_end: snap_frame_minus_one

  Action_BallSnap:
    max_duration_frames: 3
    ends_when_any_action_starts:
      - Action_SnapReceive

  Action_SnapReceive:
    max_duration_frames: 10
    ends_when_same_actor_action_starts: true

  Action_Handoff:
    max_duration_frames: 10
    ends_when_any_action_starts:
      - Action_TakeHandoff
      - Action_BallCarry

  Action_TakeHandoff:
    max_duration_frames: 10
    ends_when_same_actor_action_starts: true

  Action_BallCarry:
    ends_at_result_or_play_end: true

  Action_ZoneBlock:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_ReachBlock:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_DownBlock:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_PullBlock:
    max_duration_frames: 50
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_LeadBlock:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_BlockSecondLevel:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: play_end_frame

  Action_PlayEnd:
    ends_at_final_frame: true
```

The rule engine should always prefer explicit same-player next actions over generic max-duration rules.

Recommended rule priority:

1. Next action for the same actor.
2. Explicit global event boundary, such as snap, result, or play end.
3. Action-specific rule.
4. Maximum duration.
5. Final visible frame for track.
6. Final clip frame.

### **4.8 Generate Dense Frame-Level Annotations**

For each inferred `ActionSegment`:

1. Iterate from `start_frame` to `end_frame`.
2. Look up the XML player box for that frame.
3. If a visible box exists, create a dense action annotation using the XML geometry.
4. Attach metadata:
   - action label,
   - actor track ID,
   - position,
   - team side,
   - XML track ID,
   - source = `xml_geometry_csv_action`.
5. If no visible box exists, follow the missing-box policy.

### **4.9 Validate Output**

Before writing files, run validation checks:

- Every CSV action is matched or explicitly skipped.
- Every generated dense annotation has a valid frame number.
- Every generated dense annotation has a valid bounding box.
- No player has two primary actions in the same frame.
- No generated action range has `end_frame < start_frame`.
- No undefined action labels are used in final training output unless explicitly allowed.
- All generated boxes stay within the expected frame dimensions when dimensions are known.

### **4.10 Write Outputs**

The codebase should write multiple useful outputs:

1. **Enriched TapeVision JSON** for model training and future structured output.
2. **Dense action CSV** for human review.
3. **Validation report** in Markdown and/or JSON.
4. **Required enriched CVAT XML** that preserves the original XML structure and adds action metadata in a safe, non-destructive way. This is a required primary output of the codebase, not an optional output.

---

## **5. Output**

The codebase should produce an output directory for each processed video.

Example:

```text
outputs/
└── JetSweep_69/
    ├── tapevision_annotations.json
    ├── dense_actions.csv
    ├── normalized_action_events.csv
    ├── validation_report.md
    ├── validation_report.json
    └── enriched_cvat.xml
```

### **5.1 TapeVision JSON Output**

The primary output should be a structured JSON file that can be used for TapeVision training and downstream processing.

Recommended structure:

```json
{
  "schema_version": "tapevision_annotation_enrichment_v1.0",
  "source": {
    "xml_file": "sampleJetSweepCVAT_video_2.xml",
    "csv_file": "sample_sequence_logger.csv",
    "source_of_truth": "cvat_video_xml",
    "action_source": "csv_start_frame_only"
  },
  "clip": {
    "video_name": "JetSweep_69",
    "frame_start": 0,
    "frame_end": 116,
    "num_frames": 117
  },
  "play": {
    "play_tag": "Play_Run_JetSweep",
    "result_tag": "Result_Tackle",
    "result_frame": 116
  },
  "tracks": {
    "players": [
      {
        "xml_track_id": "0",
        "actor_track_id": "2",
        "position": "FS",
        "team_side": "defense",
        "samples": [
          {
            "frame": 0,
            "bbox_xyxy": [100.0, 200.0, 150.0, 300.0],
            "bbox_xywh": [100.0, 200.0, 50.0, 100.0],
            "visible": true
          }
        ]
      }
    ],
    "ball": []
  },
  "actions": {
    "segments": [
      {
        "actor_track_id": "16",
        "xml_track_id": "12",
        "position": "WR-F",
        "team_side": "offense",
        "action": "Action_BallCarry",
        "start_frame": 65,
        "end_frame": 116,
        "source": "csv_start_frame_only_plus_rules"
      }
    ],
    "dense_frame_annotations": [
      {
        "frame": 65,
        "actor_track_id": "16",
        "xml_track_id": "12",
        "position": "WR-F",
        "team_side": "offense",
        "action": "Action_BallCarry",
        "bbox_xyxy": [400.0, 300.0, 455.0, 410.0],
        "bbox_xywh": [400.0, 300.0, 55.0, 110.0]
      }
    ]
  }
}
```

### **5.2 Dense Action CSV Output**

The dense CSV should be easy to inspect manually and should be generated from the wide CSV plus XML geometry.

Recommended columns:

```csv
video_name,frame,actor_track_id,xml_track_id,position,team_side,action,xtl,ytl,xbr,ybr,w,h,source
```

Example:

```csv
JetSweep_69,65,16,12,WR-F,offense,Action_BallCarry,400.0,300.0,455.0,410.0,55.0,110.0,xml_geometry_csv_action
```

### **5.3 Normalized Action Events CSV Output**

The codebase should optionally write a generated normalized action-events CSV for debugging. This file is not the required human input format. It is produced by the parser after reading the wide CSV.

Recommended columns:

```csv
video_name,video_id,source_column,action,start_frame,actor_track_id,target_kind,play_tag,result_tag,result_frame,notes
```

This output helps verify that wide cells such as `43,2;43,4` or `100,OL` were expanded correctly before dense annotation generation.

### **5.4 Validation Report**

The validation report should summarize the conversion and identify issues.

Recommended sections:

- Input files.
- XML track summary.
- CSV action summary.
- Matched actions.
- Unmatched actions.
- Generated action segments.
- Generated dense annotations.
- Warnings.
- Errors.
- Recommended fixes.

### **5.5 Required Enriched CVAT XML Output**

The enriched CVAT XML is a **required primary output** of the codebase. This output is not optional. The main purpose of the codebase is to take the original CVAT for Video XML export as the source of truth and produce a new enriched CVAT XML file that adds the missing action information from the wide-format CSV while preserving the original track geometry and identity structure.

The enriched XML must be written as a separate file, for example:

```text
enriched_cvat.xml
```

The program must never overwrite the original CVAT XML file.

The enriched XML must preserve the original XML structure as much as possible, including:

- original `<track>` elements,
- original XML track IDs,
- original labels,
- original `<box>` elements,
- original frame numbers,
- original bounding box coordinates,
- original `outside`, `occluded`, and `keyframe` values,
- original player and ball attributes,
- original task/video metadata when present.

The enriched XML should add action metadata to existing player tracks/boxes without changing player/ball geometry. The exact representation can be implemented in one of the following safe ways, with the recommended approach listed first:

#### **Recommended Enrichment Method: Add Box-Level Action Attributes**

For each visible player `<box>` frame covered by an inferred action segment, add one or more new `<attribute>` entries such as:

```xml
<attribute name="tapevision_action">Action_ZoneBlock</attribute>
<attribute name="tapevision_action_source">wide_csv_start_frame_only</attribute>
<attribute name="tapevision_action_segment_start">43</attribute>
<attribute name="tapevision_action_segment_end">66</attribute>
```

This method keeps the action attached directly to the same box that CVAT already uses for the player track. It avoids creating duplicate action tracks and preserves the original player identity.

#### **Allowed Alternative: Add Track-Level Action Summary Metadata**

The enriched XML may also add a track-level action summary as metadata or comments if box-level action attributes are not convenient. For example, the enriched XML may include a serialized action segment summary for each player track. However, this should not replace the box-level action attributes if the downstream workflow needs frame-level action labels.

#### **Required Action Metadata Fields**

The enriched XML should include enough metadata for downstream tools to recover the action timeline without using the CSV again. At minimum, each enriched frame-level action annotation should include:

- canonical action label, such as `Action_ZoneBlock`,
- action source, such as `wide_csv_start_frame_only`,
- action segment start frame,
- action segment end frame,
- actor track ID used for matching,
- XML track ID when useful,
- optional confidence or validation status if available.

#### **Non-Destructive XML Rule**

The enriched XML must not:

- delete any original player or ball tracks,
- delete any original boxes,
- change any original bounding box coordinates,
- change original track IDs,
- change player/ball labels,
- overwrite the original XML file,
- create duplicate action geometry unless explicitly configured.

#### **Relationship to Other Outputs**

The enriched CVAT XML is the required main output. The other outputs must still be kept because they support debugging, model training, and validation:

- `tapevision_annotations.json` for TapeVision training and structured downstream processing,
- `dense_actions.csv` for human review,
- `normalized_action_events.csv` for debugging the wide CSV parser,
- `validation_report.md` and/or `validation_report.json` for quality control.

The JSON and CSV outputs should be generated from the same enriched action segments used to write the enriched XML so all outputs remain consistent.

---

## **6. Edge Cases**

The codebase must handle the following edge cases safely and report them clearly.

### **6.1 Blank Action Cell in Wide CSV**

If a wide CSV action cell is blank, treat it as intentionally not logged. Do not create an action event and do not report it as an error.

### **6.2 Malformed Wide CSV Cell**

If a cell cannot be parsed, such as `abc`, `43`, in a player-action column that requires a track ID, or `43,,2`, report a validation error with the video row, column name, and raw cell value.

Default behavior:

```text
Skip the malformed cell and continue processing the rest of the video row.
```

Strict mode:

```text
Stop execution.
```

### **6.3 Group Target Cannot Be Resolved**

If a wide CSV cell uses a group target such as `OL`, `ALL_OFFENSE`, or `SKILL`, but the XML does not contain enough `position` or `team_side` metadata to resolve the group, report a validation error.

Default behavior:

```text
Skip the unresolved group event and continue.
```

Strict mode:

```text
Stop execution.
```

### **6.4 CSV Track ID Does Not Exist in XML**

If an action row references a track ID that is not found in the XML, report it.

Default behavior:

```text
Skip the action row and add an error to the validation report.
```

Strict mode:

```text
Stop execution.
```

### **6.5 CSV Frame Number Is Outside the Video Range**

If an action start frame is less than 0 or greater than the final XML frame, report it.

Default behavior:

```text
Skip the action row.
```

### **6.6 CSV Action Starts on a Frame Where the Player Has No Box**

If the player track does not have a visible bounding box at the action start frame, report it.

Default behavior:

```text
Keep the action segment, but skip dense annotations for frames without visible XML boxes.
```

### **6.7 Player Track Has Gaps**

If a player disappears and reappears, the XML may have frames with `outside="1"` or missing boxes.

Default behavior:

```text
Do not invent boxes. Generate dense action annotations only for visible frames.
```

### **6.8 Overlapping Actions for the Same Player**

If two actions overlap for the same player after applying rules, resolve using priority rules and report the conflict.

Default behavior:

```text
The later action start overrides the earlier action from that frame forward.
```

### **6.9 Missing Play-End Frame**

If the CSV does not contain a play-end or result frame, use the final XML frame as the fallback play end.

Report a warning:

```text
No play-end frame found. Used final XML frame as fallback.
```

### **6.10 Missing Result Tag**

If no result tag is provided, set:

```text
result_tag = Result_Unknown
```

and report a warning.

### **6.11 Missing Play Tag**

If no play tag is provided, set:

```text
play_tag = Play_Unknown
```

and report a warning.

### **6.12 Undefined Position or Team Side**

If `position` or `team_side` is `undefined`, replace it with a configured default and report a warning.

Recommended defaults:

```text
position = Position_Unknown
team_side = Team_Unknown
```

### **6.13 Defensive Tracks Without Action Labels**

Defensive tracks may have no action annotations in the CSV during the offense-first annotation phase.

Default behavior:

```text
Keep defensive tracks in the track output.
Do not generate supervised defensive action labels unless configured.
If dense labels are required, assign Action_Defense_NotAnnotated.
```

### **6.14 Ball Track Has No Action CSV Entries**

The ball track may be present in XML without action entries in the CSV.

Default behavior:

```text
Preserve the ball track in the output.
Do not require ball action labels.
```

### **6.15 Duplicate Action Entries in Wide CSV**

If the wide CSV creates duplicate internal action events with the same `actor_track_id`, `action`, `start_frame`, and `source_column`, deduplicate them and report a warning. This may happen when the same player is listed twice in one action cell or appears in both an individual and group-target cell.

### **6.16 Multiple XML Tracks Share the Same Custom Track ID**

If more than one XML track has the same custom `track_id` attribute, report an error because action matching becomes ambiguous.

Default behavior:

```text
Stop execution in strict mode.
Use XML <track id> matching only if configured.
```

### **6.17 Invalid Bounding Boxes**

If any XML box has invalid coordinates, such as `xbr <= xtl` or `ybr <= ytl`, report it and skip that box.

### **6.18 Unknown Action Label**

If the CSV contains an action label not listed in the configured action vocabulary, report it.

Default behavior:

```text
Map to Action_Unknown or stop in strict mode.
```

---

## **Implementation Requirements**

- Use Python 3.10+.
- Use standard libraries where possible:
  - `xml.etree.ElementTree` or `lxml` for XML parsing.
  - `csv` or `pandas` for wide CSV parsing and optional normalized output writing.
  - `dataclasses` or `pydantic` for internal models.
  - `pyyaml` for YAML config support.
- Provide a command-line interface.
- Provide unit tests for parsing, matching, action range inference, validation, and output writing.
- Write clear logs to the console and to the output directory.
- Do not require internet access.
- Do not require CVAT to be running.
- Do not modify original input files.

### **Example CLI Commands**

```bash
python -m tapevision_enricher \
  --xml data/xml/sampleJetSweepCVAT_video_2.xml \
  --csv data/actions/sample_sequence_logger.csv \
  --config configs/default_config.yaml \
  --output outputs/JetSweep_69
```

```bash
python -m tapevision_enricher.validate \
  --xml data/xml/sampleJetSweepCVAT_video_2.xml \
  --csv data/actions/sample_sequence_logger.csv
```

### **Definition of Done**

The codebase is complete when it can:

1. Parse a CVAT for Video XML file.
2. Preserve XML player and ball tracks exactly as the geometry source of truth.
3. Parse a wide-format sparse action CSV.
4. Expand wide CSV action cells into internal action events and match them to XML player tracks.
5. Infer action end frames using start-frame-only logic and configurable rules.
6. Generate dense frame-level action annotations using copied XML bounding boxes.
7. Validate the results and report issues clearly.
8. Write TapeVision-ready JSON, dense CSV, and validation reports.
9. Write a required enriched CVAT XML file that adds action metadata while preserving original XML tracks and box geometry.
10. Run from a CLI command.
11. Pass unit tests for the core workflow.
