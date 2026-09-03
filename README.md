# Play-Annotation-Generator

A high-performance Python utility designed to merge spatial video tracking annotations (**CVAT for Video XML** or **MOT GT 1.0 format**) with temporal play-by-play action logs parsed from sparse **wide-format CSV spreadsheets**. 

This system acts as a key component in the FilmBreakdownAI football film breakdown pipeline, bridging human key action logs and object tracking algorithms to produce machine-learning-ready datasets (hierarchical JSON annotations, frame-dense flat CSVs, enriched CVAT XML files, and validation reports).

---

## Table of Contents
1. [System Overview & Purpose](#system-overview--purpose)
2. [Pipeline Execution Modes](#pipeline-execution-modes)
3. [Project Directory & File Map](#project-directory--file-map)
4. [Core Architectural Modules](#core-architectural-modules)
5. [Data Models & Type Definitions](#data-models--type-definitions)
6. [Input File Specification & Formatting Rules](#input-file-specification--formatting-rules)
7. [Action Rules & Temporal Inference Engine](#action-rules--temporal-inference-engine)
8. [Pipeline Validation & Quality Control Engine](#pipeline-validation--quality-control-engine)
9. [Generated Output Files](#generated-output-files)
10. [Configuration Reference (`configs/default_config.yaml`)](#configuration-reference-configsdefault_configyaml)
11. [CLI Command Reference & Examples](#cli-command-reference--examples)
12. [Batch Processing](#batch-processing)
13. [Testing & Verification](#testing--verification)

---

## System Overview & Purpose

Football film annotation requires tracking 22 players and the ball across frames while simultaneously annotating fine-grained temporal actions (e.g. `Action_PreSnap`, `Action_BallSnap`, `Action_SnapReceive`, `Action_ZoneBlock`, `Action_LeadBlock`, `Action_BallCarry`, `Action_PlayEnd`). Manual frame-by-frame labeling of all player actions is extremely time-consuming.

The **Play-Annotation-Generator** automates this by taking:
1. **Spatial Tracking Data**: CVAT for Video XML export OR raw MOT (Multiple Object Tracking) `gt.txt` files containing bounding boxes (`xtl, ytl, xbr, ybr`) and track IDs.
2. **Player Track Assignments**: A CSV sheet mapping MOT track IDs to positions (`QB`, `LT`, `LG`, `C`, `RG`, `RT`, `WR-X`, etc.) and team sides (`offense` vs `defense`).
3. **Key Action Logs**: A sparse wide-format CSV spreadsheet where human annotators mark key action start frames for individual players or position groups (`OL`, `SKILL`, `ALL_OFFENSE`).

Using configurable rule sets, the enricher infers start and end frames (`ActionSegment`) for every player on every frame, producing dense annotations while preserving bounding box geometry.

---

## Pipeline Execution Modes

The utility operates under three primary subcommands/workflows:

```
                      +------------------------------------------+
                      |         INPUT SOURCES                    |
                      |  - MOT gt.txt / zip archive             |
                      |  - Player Track ID Sheet                 |
                      |  - Wide Key Actions CSV                  |
                      |  - CVAT Template XML                     |
                      +--------------------+---------------------+
                                           |
                    +----------------------+----------------------+
                    |                                             |
                    v                                             v
        [ Mode B: generate-and-enrich ]                [ Mode A: enrich-existing ]
        - Parses MOT tracking gt.txt                   - Parses existing CVAT XML
        - Maps player positions                        - Parses wide action CSV
        - Generates base CVAT XML                      - Infers action segments
        - Enriches base CVAT XML                       - Generates multi-format outputs
                    |                                             |
                    +----------------------+----------------------+
                                           |
                                           v
                               +--------------------------+
                               |      OUTPUT FILES        |
                               |  - annotations.xml       |
                               |  - annotations.json       |
                               |  - dense_actions.csv     |
                               |  - validation_report.md  |
                               +------------+-------------+
                                           |
                                           v
                              [ Mode C: review tool ]
                              - Play Health Overview
                              - CSV vs Segment Checklist
                              - Per-Player Timeline
```

1. **Mode A: Enrich Existing CVAT XML (`enrich-existing`)**
   - **Use Case**: An annotated CVAT XML file already exists (with player boxes, positions, and track IDs). You want to enrich it with actions from a wide CSV sheet.
   - **Input**: Pre-existing CVAT XML + Wide CSV action spreadsheet.
   - **Output**: Injected `tapevision_action*` attributes inside XML boxes, JSON training annotations, dense CSVs, and validation reports.

2. **Mode B: Generate XML from MOT & Sheets & Enrich (`generate-and-enrich`)**
   - **Use Case**: Starting from raw MOT tracking outputs (`gt.txt` or zip archive like `JetSweep_1_cvat_mot.zip`) without a CVAT XML.
   - **Pipeline**:
     1. Parses MOT bounding boxes and track IDs (`gt.txt` / `labels.txt`).
     2. Parses Player Track ID assignment CSV (`QB,8;TE-Y,10;LG,2`).
     3. Uses an XML template (`JetSweepTemplate.xml`) to construct a valid base CVAT Video XML (`generated_base_cvat.xml`).
     4. Passes the generated XML into the core enrichment pipeline to apply key actions.

3. **Mode C: Interactive Review Tool (`review`)**
   - **Use Case**: Quick command-line inspection and sanity checking of generated play outputs without sifting through raw XML or thousands of JSON lines.
   - **Output**: Compact Markdown report (`review_report.md`) featuring collapsible audit sections, split identity (`Player / Track Mapping`) and timing (`Timing Mapping`) tables with both `actor_track_id` and `xml_track_id`, deterministic football-position player ordering, ball tracking summary, and issue review.

---

## Project Directory & File Map

```text
Play-Annotation-Generator/
├── pyproject.toml                        # Build system configuration & dependencies (PyYAML, pytest)
├── requirements.txt                      # PIP dependency list
├── README.md                             # Comprehensive technical documentation (this file)
├── configs/
│   └── default_config.yaml               # Default pipeline configuration, mappings, and rules engine settings
├── data/
│   ├── DatasetSummary.csv
│   ├── actions.json
│   ├── plays.json
│   ├── key_actions/
│   │   └── JetSweep.csv
│   ├── player_tracks/
│   │   └── JetSweep.csv
│   └── tracking/
│       ├── Counter/
│       └── JetSweep/
│           └── JetSweep_1_cvat_mot.zip
├── docs/
│   ├── JetSweepTemplate.xml              # Template CVAT XML file used by Mode B generator
│   ├── endOfPlayEventsShortHand.json     # Result shorthand mappings (e.g. "Tac" -> "Result_Tackle")
│   └── sampleJetSweepCVAT_video_2.xml    # Sample CVAT Video XML for testing Mode A
├── outputs/                              # Default destination directory for generated pipeline outputs
├── src/
│   ├── play_annotation_generator/        # Core package root
│   │   ├── __init__.py                   # Package initializer
│   │   ├── __main__.py                   # Entry point for python -m play_annotation_generator
│   │   ├── models.py                     # Dataclasses defining core domain data models
│   │   ├── config.py                     # YAML configuration loader & deep merger
│   │   ├── cvat_xml_parser.py            # ElementTree parser for CVAT Video XML files
│   │   ├── cvat_xml_generator.py         # Base CVAT XML generator from MOT tracks and assignments
│   │   ├── mot_parser.py                 # MOT gt.txt and zip archive extractor/parser
│   │   ├── player_track_sheet_parser.py  # Flexible parser for player track assignment CSV formats
│   │   ├── sheet_group_resolver.py       # Group target (OL, SKILL, ALL_OFFENSE) expansion logic
│   │   ├── action_event_normalizer.py    # Matches parsed CSV events to XML track IDs & expands groups
│   │   ├── action_rules.py               # Rule-based temporal segment start/end inference engine
│   │   ├── validators.py                 # Pipeline quality assurance and coordinate sanity validator
│   │   ├── enricher.py                   # Mode A pipeline orchestrator (`run_enrichment_pipeline`)
│   │   ├── pipeline_generate_and_enrich.py # Mode B pipeline orchestrator (`run_generate_and_enrich_pipeline`)
│   │   ├── reviewer.py                   # Interactive play report & verification tool
│   │   ├── cli.py                        # Argparse CLI entry point supporting subcommands and legacy flags
│   │   └── writers/                      # Output formatting subpackage
│       ├── __init__.py               # Writer exports
│       ├── enriched_xml_writer.py    # Injects action attributes into CVAT XML track boxes
│       ├── play_annotation_json_writer.py # Exports structured play annotation JSON
│       ├── dense_csv_writer.py       # Exports flat frame-by-frame dense actions and normalized events CSVs
│       ├── report_writer.py          # Exports markdown and JSON validation reports
│       └── batch_report_writer.py    # Exports batch manifests and summaries
│   └── tapevision_enricher/              # Backward-compatibility shim
│       └── __init__.py
└── tests/                                # Unit & integration test suite
    ├── __init__.py                       # Test package initializer
    ├── test_action_rules.py              # Tests action segment end inference & fallback rules
    ├── test_annotation_metadata.py       # Tests metadata enrichment from CSV/JSON taxonomies
    ├── test_batch_cli.py                 # Tests batch CLI arguments
    ├── test_batch_pipeline.py            # Tests batch execution engine
    ├── test_compat_shim.py               # Tests backward-compatibility import shim
    ├── test_cvat_xml_parser.py           # Tests CVAT XML metadata & track extraction
    ├── test_enricher.py                  # Tests full Mode A enrichment pipeline
    ├── test_mot_xml_pipeline.py          # Tests Mode B XML generation & MOT parsing
    ├── test_reviewer.py                  # Tests interactive reviewer report generation
    ├── test_validators.py                # Tests validation checks and coordinate sanity flags
    └── test_wide_action_csv_parser.py    # Tests wide CSV cell parsing & multi-entry splitting
```

---

## Core Architectural Modules

### Package Modules (`src/play_annotation_generator/`)

- **[`models.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/models.py)**: Defines strongly typed Python `@dataclass` objects: `TrackBox`, `Track`, `ActionEvent`, `ActionSegment`, `DenseActionAnnotation`.
- **[`config.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/config.py)**: Houses `DEFAULT_CONFIG` dictionary and provides `load_config(path)` to recursively merge YAML overrides with default settings.
- **[`cvat_xml_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/cvat_xml_parser.py)**: Parses `<meta>` video dimensions/frame counts and `<track>` elements with `<box>` nodes and custom `<attribute>` elements (`position`, `team_side`, `track_id`, `action`).
- **[`mot_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/mot_parser.py)**: Extracts MOT `.zip` archives or parses `gt.txt` files. Converts `[left, top, width, height]` to `[xtl, ytl, xbr, ybr]`, applies frame indexing offset (`cvat_base - mot_base`), and clamps coordinates.
- **[`player_track_sheet_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/player_track_sheet_parser.py)**: Flexible parser supporting three player assignment CSV layouts: Wide cells (`QB,8;TE-Y,10`), Normalized rows (`position,track_id`), and Positional grid layouts.
- **[`cvat_xml_generator.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/cvat_xml_generator.py)**: Combines parsed MOT tracks and player assignments into a new CVAT Video XML file using a template for root structure. Handles track visibility and `outside="1"` termination boxes.
- **[`sheet_group_resolver.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/sheet_group_resolver.py)**: Resolves group shorthand target strings (`ALL`, `ALL_OFFENSE`, `ALL_DEFENSE`, `OL`, `SKILL`) or individual position names (`QB`, `WR-F`) into lists of matching `Track` objects.
- **[`wide_action_csv_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/wide_action_csv_parser.py)**: Parses wide CSV action cells. Splits multi-entries (`semicolon`, `pipe`, `newline`), extracts `frame,track_id` pairs, maps result tags via shorthand JSON, and filters by target video name/ID.
- **[`action_event_normalizer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/action_event_normalizer.py)**: Maps parsed CSV `ActionEvent` records to actual XML track IDs, performs group expansions, and checks for ambiguous custom track IDs.
- **[`action_rules.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/action_rules.py)**: Inferences action start and end frames (`ActionSegment`) track-by-track. Applies event deduplication, collision resolution (later CSV columns take precedence), global triggers, max duration limits, and fallback rules.
- **[`validators.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/validators.py)**: Evaluates data integrity: coordinate sanity (`xbr > xtl`), actions starting on invisible/missing boxes, overlapping player segments, unknown action labels, and missing player metadata.
- **[`enricher.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/enricher.py)**: Primary orchestrator for Mode A (`run_enrichment_pipeline`).
- **[`pipeline_generate_and_enrich.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/pipeline_generate_and_enrich.py)**: Primary orchestrator for Mode B (`run_generate_and_enrich_pipeline`).
- **[`reviewer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/reviewer.py)**: Generates human-readable terminal review reports (`review_play_outputs`).
- **[`cli.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/cli.py)**: CLI entry point supporting subcommands `enrich-existing`, `generate-and-enrich`, `review`, and legacy `--xml`/`--csv` flags.

### Output Writer Modules (`src/play_annotation_generator/writers/`)

- **[`enriched_xml_writer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/writers/enriched_xml_writer.py)**: Injects action attributes and `<play_annotation_generator>` metadata into CVAT XML.
- **[`play_annotation_json_writer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/writers/play_annotation_json_writer.py)**: Formats hierarchical JSON output (`annotations.json`) containing clip metadata, clip source timing, play definitions, track samples, inferred action segments, used action definitions, and dense frame annotations.
- **[`dense_csv_writer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/writers/dense_csv_writer.py)**: Writes frame-by-frame flat CSV (`dense_actions.csv`) and debugging CSV (`normalized_action_events.csv`).
- **[`report_writer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/writers/report_writer.py)**: Writes structured pipeline execution reports (`validation_report.md` and `validation_report.json`).
- **[`batch_report_writer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/writers/batch_report_writer.py)**: Writes batch manifests (`batch_manifest.csv`, `batch_manifest.json`) and summary markdown (`batch_summary.md`).

---

## Data Models & Type Definitions

Defined in **[`src/play_annotation_generator/models.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/models.py)**:

```python
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
    label: str                           # "player" or "ball"
    source: str                          # "file" or "manual"
    attributes: Dict[str, str] = field(default_factory=dict)
    boxes_by_frame: Dict[int, TrackBox] = field(default_factory=dict)
    position: Optional[str] = None       # e.g., "QB", "LT", "WR-X"
    team_side: Optional[str] = None      # "offense" or "defense"
    custom_track_id: Optional[str] = None # Original track ID string (e.g., "16")

@dataclass
class ActionEvent:
    video_name: Optional[str] = None
    video_id: Optional[str] = None
    play_tag: Optional[str] = None
    result_tag: Optional[str] = None
    result_frame: Optional[int] = None
    action: str = ""                     # Config action label e.g., "Action_PreSnap"
    start_frame: int = 0
    actor_track_id: Optional[str] = None # Raw CSV actor target (e.g. "16", "OL", "ball")
    resolved_xml_track_id: Optional[str] = None # Internal CVAT XML track ID
    target_kind: str = "global_event"   # "track_id", "group", "global_event", "ball"
    source_column: str = ""
    actor_position: Optional[str] = None
    notes: Optional[str] = None

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
    bbox_xyxy: List[float]               # [xtl, ytl, xbr, ybr]
    bbox_xywh: List[float]               # [xtl, ytl, width, height]
    source: str = "xml_geometry_csv_action"
```

---

## Input File Specification & Formatting Rules

### 1. Wide Action CSV Spreadsheet
The action CSV uses a **wide format** where each row corresponds to a single video clip and columns represent specific action classes (`Action_PreSnap`, `Action_JetMotion`, `Action_BallSnap`, `Action_ZoneBlock`, `Action_SnapReceive`, `Action_Toss`, `Action_BallCarry`, `Action_SealBlock`, `Action_LeadBlock`, `Action_BlockSecondLevel`, `Action_PlayEnd`).

#### Cell Entry Syntax
- **Single Actor**: `frame,track_id` $\rightarrow$ `"33,16"`
- **Multiple Actors**: `frame,track_id;frame,track_id` $\rightarrow$ `"43,2;43,4"` (Separators: `;`, `|`, newline)
- **Group Target**: `frame,GROUP` $\rightarrow$ `"0,ALL_OFFENSE"`, `"43,OL"`, `"65,SKILL"`
- **Global / Frame Only Event**: `frame` $\rightarrow$ `"116"` under `end_play`
- **Result Shorthand / Text Override**: `"Tac"` $\rightarrow$ mapped via shorthand JSON to `"Result_Tackle"`

> [!IMPORTANT]
> Because cells contain commas (e.g. `33,16`), cell values **must** be enclosed in double quotes in raw CSV text (`"33,16"`).

### 2. MOT Ground Truth (`gt.txt` or `.zip` Archives)
Standard MOT Challenge 1.0 format (9 comma-separated values per line):
```text
<frame>, <track_id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <class_id>, <visibility>
```
- Coordinates are converted from `[left, top, width, height]` to `[xtl, ytl, xbr, ybr]` and clamped to video bounds (`1920x1080`).
- Frame numbers are adjusted using `frame_offset = cvat_frame_index_base - mot_frame_index_base` (converting MOT 1-based indexing to CVAT 0-based indexing).

### 3. Player Track ID Assignment CSV
Maps MOT track IDs to positions and team sides. Supported formats:
- **Wide Format**: `Video #`, `assignments` cell containing `"QB,8;TE-Y,10;LG,2;C,5;RG,14"`
- **Normalized Format**: Explicit columns `position`, `track_id`, `team_side`
- **Positional Grid Format**: Column 0 is `video_id`, subsequent columns contain `POSITION,TRACK_ID`

---

## Action Rules & Temporal Inference Engine

Implemented in **[`src/play_annotation_generator/action_rules.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/action_rules.py)**:

When inferring action segments `[start_frame, end_frame]` for each player track:
1. **Deduplication**: Identical actions at the same start frame for a player are deduplicated.
2. **Collision Resolution**: If multiple different actions start on the exact same frame for a player track, the later action (right-most column in CSV) overrides earlier ones.
3. **End-Frame Evaluation Order**:
   - **Same-Player Next Action**: If another action starts for the same player at frame $F_{next}$, current action ends at $F_{next} - 1$.
   - **Global Action Trigger**: If `ends_at_global_action` is specified (e.g. `Action_PreSnap` ends when global `Action_BallSnap` occurs), ends at $F_{global} - 1$.
   - **Any Action Trigger**: If `ends_when_any_action_starts` is specified (e.g. `Action_BallSnap` ends when `Action_SnapReceive` starts).
   - **Max Duration Limit**: If `max_duration_frames` is configured (e.g., `Action_BallSnap` max 3 frames, blocking actions max 60 frames), ends at $\min(\text{end}, \text{start} + \text{max\_duration} - 1)$.
   - **Result / Play End Trigger**: Actions with `ends_at_result_or_play_end` (e.g. `Action_BallCarry`, `Action_ZoneBlock`) extend to the play result frame or `Action_PlayEnd`.
   - **Visibility Clamping**: Action segments are clamped to the player track's visible frame range `[min_track_frame, max_track_frame]`.

---

## Pipeline Validation & Quality Control Engine

Implemented in **[`src/play_annotation_generator/validators.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/validators.py)**:

1. **Bounding Box Coordinate Sanity**: Verifies $x_{br} > x_{tl}$ and $y_{br} > y_{tl}$ for all visible track boxes. Flags inverted bounds or zero-area boxes.
2. **Action Start Visibility Check**: Flags any CSV action starting on a frame where the player track has no visible bounding box (`outside="1"` or missing).
3. **Action Range Bounding Box Coverage**: Measures total frames within an inferred action segment where a player box is missing.
4. **Overlapping Action Segments**: Detects illegal concurrent primary actions for the same player track on the same frame.
5. **Attribute & Label Compliance**: Checks for unknown action names or undefined player metadata (`position: "undefined"` or `team_side: "undefined"`).
6. **Strict Mode Handling**: When `validation.strict: true`, critical validation errors raise exceptions and halt execution.

---

## Generated Output Files

Running the pipeline populates the target output directory with the following artifacts:

1. **`generated_base_cvat.xml`** (Mode B Only): Base CVAT Video XML file compiled directly from raw MOT tracks and player assignments before action enrichment.
2. **`annotations.xml`** (Primary XML Output): Enriched CVAT XML with injected box-level attributes (`tapevision_action`, `tapevision_action_source`, `tapevision_action_segment_start`, `tapevision_action_segment_end`) and top-level `<play_annotation_generator>` clip/taxonomy metadata block while preserving original box geometry.
3. **`annotations.json`**: Hierarchical JSON dataset formatted for model training:
   - `clip`: Video name, frame start, frame stop, total frame count, and `source` timing (`start_time`, `end_time`, `clip_length`, `view`, `from_youtube`).
   - `play`: Play tag, play `definition`, result tag, result frame.
   - `tracks`: Bounding box keyframe samples for `players` and `ball`.
   - `actions`: Temporal `segments` and `dense_frame_annotations`.
   - `definitions`: Textual definitions registry (`actions`) for actions used in the clip.
4. **`dense_actions.csv`**: Flat, frame-by-frame tabular export mapping active actions to coordinates:
   `video_name, frame, actor_track_id, xml_track_id, position, team_side, action, xtl, ytl, xbr, ybr, w, h, source`
5. **`normalized_action_events.csv`**: Audit table listing all parsed, matched, and expanded CSV action events.
6. **`validation_report.md`**: Human-readable Markdown quality control report with status badge, metrics table, errors, warnings, and recommended fixes.
7. **`validation_report.json`**: Machine-readable JSON summary of metrics, warnings, and errors.
8. **`review_report.md`** (Created when running Mode C `review` or passing `--review`): Compact Markdown verification report with collapsible diagnostic sections, split `Player / Track Mapping` and `Timing Mapping` audit tables (showing both `actor_track_id` and `xml_track_id`), football-position ordered player timelines, ball tracking summary, and categorized review items.

---

## Configuration Reference (`configs/default_config.yaml`)

```yaml
input:
  cvat_xml: ""
  action_csv: ""
  gt_txt: ""
  labels_txt: ""
  xml_template: ""
  key_actions_csv: ""
  player_track_csv: ""

output:
  output_dir: "outputs/"
  write_generated_base_xml: true
  write_enriched_xml: true
  write_play_annotation_json: true
  write_tapevision_json: true
  write_dense_csv: true
  write_validation_report: true

frame_indexing:
  mot_frame_index_base: 1    # MOT tracking 1-based index
  cvat_frame_index_base: 0   # CVAT XML 0-based index

video:
  fps: 30
  width: 1920
  height: 1080

mot:
  class_id_to_label:
    1: "player"
    2: "ball"
  default_label: "player"

labels:
  player_label: "player"
  ball_label: "ball"

position_groups:
  OL: ["LT", "LG", "C", "RG", "RT"]
  ALL_OFFENSE: ["QB", "RB", "FB", "H-BACK", "LT", "LG", "C", "RG", "RT", "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F"]
  SKILL: ["QB", "RB", "FB", "H-BACK", "WR-X", "WR-Y", "WR-Z", "WR-F", "TE-Y", "TE-H", "TE-F"]

action_policy:
  default_unlabeled_offense_action: "Action_Unknown"
  default_unlabeled_defense_action: "Action_Defense_NotAnnotated"
  action_range_mode: "start_frame_only"
  one_primary_action_per_frame: true
  missing_box_policy: "skip"

action_end_rules:
  Action_PreSnap:
    ends_at_global_action: "Action_BallSnap"
    fallback_end: "snap_frame_minus_one"
  Action_BallSnap:
    max_duration_frames: 3
    ends_when_any_action_starts: ["Action_SnapReceive"]
  Action_SnapReceive:
    max_duration_frames: 10
    ends_when_same_actor_action_starts: true
  Action_BallCarry:
    ends_at_result_or_play_end: true
  Action_ZoneBlock:
    max_duration_frames: 60
    ends_when_same_actor_action_starts: true
    fallback_end: "play_end_frame"
```

---

## CLI Command Reference & Examples

The CLI entry point is **[`src/play_annotation_generator/cli.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/src/play_annotation_generator/cli.py)** (or via the installed entry point `play-annotation-generator` / `python -m play_annotation_generator`).

### Mode A: Enrich Existing CVAT XML (`enrich-existing`)
Enrich an existing CVAT XML using a wide CSV action sheet:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli enrich-existing \
  --xml docs/sampleJetSweepCVAT_video_2.xml \
  --csv data/actions/sample_sequence_logger.csv \
  --config configs/default_config.yaml \
  --output outputs/JetSweep_existing \
  --video-name JetSweep_69 \
  --review
```

### Mode B: Generate XML from MOT & Enrich (`generate-and-enrich`)
Compile a base CVAT XML directly from MOT tracking outputs and enrich it:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli generate-and-enrich \
  --gt data/tracking/JetSweep/JetSweep_1_cvat_mot.zip \
  --template docs/JetSweepTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/JetSweep_1 \
  --video-name JetSweep_1 \
  --video-id 1 \
  --review
```

### Mode C: Batch Generate and Enrich (`batch-generate-and-enrich`)
Process multiple MOT tracking inputs sequentially:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking \
  --template docs/UniversalTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/batch \
  --play JetSweep \
  --skip-existing
```

### Mode D: Review Output Tool (`review`)
Generate interactive review breakdown for an output directory:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli review --dir outputs/JetSweep_1
```

### Backward Compatibility (Legacy Flag Interface)
Running without a subcommand defaults to Mode A (`enrich-existing`):
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli \
  --xml docs/sampleJetSweepCVAT_video_2.xml \
  --csv data/actions/sample_sequence_logger.csv
```

---

## Batch Processing

### Purpose
Processes multiple MOT tracking inputs (zips or direct `gt.txt` files) sequentially through the single-clip `generate-and-enrich` pipeline without modifying underlying action inference rules or output formats.

### Supported Tracking Inputs
- Production MOT ZIP archives matching the naming convention: `<PlayName>_<VideoID>_cvat_mot.zip` (e.g., `JetSweep_1_cvat_mot.zip`).
- Direct `gt.txt` tracking files located in per-clip directory trees.

### Required Identity Matching
Tracking inputs are resolved against the Key Actions CSV and Player Track ID CSV prior to processing:
- `MATCHED`: Candidate identity uniquely matches exactly one logical clip in both CSV spreadsheets.
- `UNMATCHED`: Candidate identity is missing from one or both CSV spreadsheets.
- `AMBIGUOUS`: Candidate identity matches multiple logical entries or conflicts between source CSVs.

Unmatched and ambiguous clips are safely skipped from pipeline execution and recorded as failure entries in the batch manifest.

### Batch CLI (`batch-generate-and-enrich`)
Execute batch processing for a specific play type:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking/JetSweep \
  --template docs/UniversalTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/batch/JetSweep \
  --play JetSweep
```

### Smoke Test
Run a fast smoke test limiting execution to 5 matched clips:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking \
  --template docs/UniversalTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/batch \
  --limit 5
```

### Full Dataset Run
Batch processing V1 runs **one play type per invocation** to match the play-type-separated sheet structure. For a complete dataset across 31 play types, invoke `batch-generate-and-enrich` once per play type directory/sheet pair.

### Filtering
- `--play <PlayName>`: Filter resolved jobs by play type name or prefix (e.g. `JetSweep`).
- `--video-id <VideoID>`: Filter resolved jobs by exact video ID (e.g. `17`).
- `--limit <N>`: Process at most N matched jobs after deterministic sorting.

### Resume with `--skip-existing`
To resume an interrupted batch run without re-processing completed clips:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking \
  --template docs/UniversalTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/batch \
  --skip-existing
```
Completed clip output directories (containing parseable `annotations.json` and `validation_report.json`) are recorded as `SKIPPED` in the manifest without re-running. Partial or corrupt existing outputs will be marked as `FAILED` requiring explicit `--overwrite`.

### Reprocessing with `--overwrite`
To force reprocessing of existing output directories:
```bash
PYTHONPATH=src python3 -m play_annotation_generator.cli batch-generate-and-enrich \
  --gt-dir data/tracking \
  --template docs/UniversalTemplate.xml \
  --key-actions data/key_actions/JetSweep.csv \
  --player-tracks data/player_tracks/JetSweep.csv \
  --output outputs/batch \
  --overwrite
```

### Failure Isolation
Each clip processes inside an isolated try/except block. If a single clip fails (e.g., corrupted zip, validation error), the exception is logged to `<output_dir>/_failures/<clip_key>.traceback.txt`, recorded as `FAILED` in the batch manifest, and batch execution continues with the next clip.

### Per-Clip Output Layout
Each processed clip receives an isolated directory under the batch output root:
```text
outputs/batch/
├── batch_manifest.csv
├── batch_manifest.json
├── batch_summary.md
├── _failures/                       # (if exceptions occur)
│   └── BadClip.traceback.txt
├── JetSweep_1/
│   ├── generated_base_cvat.xml
│   ├── annotations.xml
│   ├── annotations.json
│   ├── dense_actions.csv
│   ├── normalized_action_events.csv
│   ├── validation_report.md
│   ├── validation_report.json
│   └── review_report.md             # (when --review is used)
└── JetSweep_2/
    └── ...
```

### Batch Manifest & Summary
- **`batch_manifest.csv` / `batch_manifest.json`**: Updated atomically after every clip. Contains clip identity, tracking input path, execution status (`SUCCESS`, `SUCCESS_WITH_WARNINGS`, `FAILED`, `SKIPPED`), validation status, warning/error counts, track/event metrics, elapsed time, and error messages.
- **`batch_summary.md`**: Provides high-level statistics including total discovered, matched, unmatched, attempted, success/failure counts, common failure reasons, and breakdown by play type.

### Review Reports
Pass `--review` to generate a per-clip compact Markdown `review_report.md` inside each clip output directory.

### Deterministic Ordering
Tracking inputs are scanned and sorted deterministically by case-folded relative POSIX path before filter/limit evaluation.

### Known Identity Assumptions
Production zip tracking files follow `<PlayName>_<VideoID>_cvat_mot.zip`. Unmatched or ambiguous files that do not conform to source CSV identifiers are never guessed.

---

## Testing & Verification

The repository features a complete unit test suite in `tests/`.

### Running Tests
Execute unit tests using standard `unittest`:
```bash
PYTHONPATH=src python3 -m unittest discover -s tests
```

Or using `pytest`:
```bash
pytest
```

### Test Suite Map
- **[`test_action_rules.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_action_rules.py)**: Verifies `infer_action_segments` end-frame rules, deduplication, collision override, and track range clamping.
- **[`test_annotation_metadata.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_annotation_metadata.py)**: Tests metadata enrichment from CSV/JSON taxonomies.
- **[`test_batch_cli.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_batch_cli.py)**: Tests CLI subcommand argument parsing and flag validations for batch commands.
- **[`test_batch_pipeline.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_batch_pipeline.py)**: Tests tracking discovery, identity resolution, sequential batch orchestration, limit, skip-existing, overwrite, failure isolation, and manifest/summary reporting.
- **[`test_compat_shim.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_compat_shim.py)**: Tests backward-compatibility import shim for `tapevision_enricher`.
- **[`test_cvat_xml_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_cvat_xml_parser.py)**: Verifies ElementTree CVAT XML header metadata parsing and track attribute extraction.
- **[`test_enricher.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_enricher.py)**: Tests end-to-end Mode A enrichment pipeline execution and JSON/CSV/XML output generation.
- **[`test_mot_xml_pipeline.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_mot_xml_pipeline.py)**: Tests MOT `gt.txt` parsing, coordinate conversion/clamping, base XML generation, and Mode B pipeline execution.
- **[`test_reviewer.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_reviewer.py)**: Tests interactive reviewer report generation.
- **[`test_validators.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_validators.py)**: Tests bounding box sanity checks (`xbr > xtl`), missing box flags, and overlapping segment detection.
- **[`test_wide_action_csv_parser.py`](file:///Users/alejandro/Desktop/Projects/FilmBreakdownAI/Utilities/Play-Annotation-Generator/tests/test_wide_action_csv_parser.py)**: Tests cell splitting (`semicolon`, `pipe`, `newline`), shorthand mapping, and group target extraction.


