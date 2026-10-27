# Play-Annotation-Generator Annotation Review — Counter_44

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_44`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `16` | `15` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 21 | START | 21 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `12` | `Group` | 21 | START | 21 | 83 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 21 | START | 21 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 21 | START | 21 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 21 | START | 21 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 21 | START | 21 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 21 | START | 21 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `9` | `Group` | 21 | START | 21 | 33 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 34 | START | 34 | 48 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `10` | `9` | 37 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `16` | `15` | 37 | START | 37 | 86 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `10` | `9` | 37 | START | 49 | 128 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `2` | `1` | 37 | START | 37 | 128 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `11` | `10` | 48 | END | 34 | 48 |
| ✅ EXACT | `Action_Handoff` | DE2 | `11` | `10` | 58 | START | 58 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB2 | `12` | `11` | 84 | START | 84 | 110 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 21–72
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 72 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 21–210
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 83 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 84 | 110 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 112 | 113 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 210 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 21–210
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 36 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 37 | 128 | 92 | inferred_complete_timeline |
| `Action_None` | 129 | 149 | 21 | inferred_complete_timeline |
| `Action_None` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 210 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 21–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 36 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 37 | 86 | 50 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 128 | 41 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 21–151
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 63 | 30 | inferred_complete_timeline |
| `Action_None` | 65 | 151 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 21–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_PullBlock` | 49 | 128 | 80 | inferred_complete_timeline |
| `Action_None` | 129 | 150 | 22 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 21–208
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 55 | 22 | inferred_complete_timeline |
| `Action_None` | 60 | 208 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 21–153
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 136 | 103 | inferred_complete_timeline |
| `Action_None` | 139 | 143 | 5 | inferred_complete_timeline |
| `Action_None` | 149 | 153 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 141 | 108 | inferred_complete_timeline |
| `Action_None` | 150 | 210 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 48 | 15 | inferred_complete_timeline |
| `Action_None` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 58 | 83 | 26 | inferred_complete_timeline |
| `Action_None` | 84 | 210 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 21–152
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 144 | 111 | inferred_complete_timeline |
| `Action_None` | 146 | 152 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 86 | 53 | inferred_complete_timeline |
| `Action_None` | 89 | 94 | 6 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 134 | 101 | inferred_complete_timeline |
| `Action_None` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 210 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 21–210
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 210 | 177 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 21–102
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 21 | 33 | 13 | inferred_complete_timeline |
| `Action_None` | 34 | 102 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 21–210 | 190 | 2 | Undefined position; Undefined team |
| `3` | `4` | Position_Unknown | Team_Unknown | 21–210 | 176 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 43–210 | 168 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 88–210 | 123 | 1 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 134–210 | 77 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 149–210 | 62 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 163–210 | 31 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 165–210 | 46 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 171–210 | 40 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 174–208 | 35 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 180–210 | 31 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 191–206 | 13 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_DownBlock` on target `10` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `10` (C): Annotated start 37 != Inferred start 49
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 90: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 37 for track '9': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (C) duration 92 frames exceeds threshold 90 frames [start=37, end=128].
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_PullBlock' annotated_start=37, effective_Action_PullBlock_start=49.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LT) duration 92 frames exceeds threshold 90 frames [start=37, end=128].
- ⚠️ Action 'Action_None' range [34-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-149] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-116] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-155] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-63] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-136] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-134] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-72] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [58-83] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [84-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [112-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [116-123] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-55] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-208] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-86] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-141] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [37-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-173] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-210] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.

</details>