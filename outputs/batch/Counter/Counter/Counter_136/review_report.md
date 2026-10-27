# Play-Annotation-Generator Annotation Review — Counter_136

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_136`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 85
- **Validation Warnings:** 99
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `16` | `13` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB1 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `4` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 68 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 66 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `16` | `13` | 67 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `16` | `13` | 69 | START | 77 | 82 |
| ✅ EXACT | `Action_DownBlock` | RG | `8` | `7` | 69 | START | 69 | 168 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `6` | `5` | 69 | START | 69 | 92 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `3` | `2` | 69 | START | 69 | 168 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 80 | END | 67 | 80 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 103 | START | 103 | 115 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB1 | `4` | `3` | 116 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 168 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SnapReceive` | 67 | 80 | 14 | inferred_complete_timeline |
| `Action_None` | 81 | 102 | 22 | inferred_complete_timeline |
| `Action_Handoff` | 103 | 115 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–109
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 69 | 168 | 100 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_PullBlock` | 69 | 92 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 95 | 104 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_DownBlock` | 69 | 168 | 100 | inferred_complete_timeline |
| `Action_None` | 169 | 186 | 18 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 119 | 53 | inferred_complete_timeline |
| `Action_None` | 122 | 159 | 38 | inferred_complete_timeline |
| `Action_None` | 166 | 239 | 74 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 88 | 22 | inferred_complete_timeline |
| `Action_None` | 125 | 127 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 137 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 95 | 29 | inferred_complete_timeline |
| `Action_None` | 186 | 239 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 66 | 11 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_None` | 102 | 110 | 9 | inferred_complete_timeline |
| `Action_None` | 114 | 148 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 168 | 19 | inferred_complete_timeline |
| `Action_None` | 172 | 239 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 104 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 126 | 60 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_None` | 67 | 133 | 67 | inferred_complete_timeline |
| `Action_None` | 211 | 227 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–222 | 223 | 2 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 13–119 | 36 | 4 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 92–239 | 143 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 111–239 | 97 | 4 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 118–160 | 43 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 123–239 | 110 | 4 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 145–239 | 94 | 2 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 146–239 | 77 | 2 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 146–168 | 20 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 156–207 | 52 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 157–228 | 72 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 166–176 | 11 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 177–237 | 55 | 6 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 181–220 | 39 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 182–232 | 51 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 187–239 | 53 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 234–239 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `16` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `4` (RB1)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 55 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 274: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '3' has invalid range: start=116, end=109. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (RG) duration 100 frames exceeds threshold 90 frames [start=69, end=168].
- ⚠️ Action 'Action_None' range [67-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-133] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-227] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [69-168] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-126] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [69-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [95-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-104] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [69-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-119] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-159] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-110] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-148] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-168] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-14] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [77-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [100-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-141] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-143] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-160] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-147] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-168] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-168] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-207] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-201] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-228] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-220] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.

</details>