# Play-Annotation-Generator Annotation Review — Draw_36

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_36`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 26 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `17` | `15` | 24 | START | 100 | 100 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `1` | `0` | 27 | START | 27 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `3` | 27 | START | 27 | 108 |
| ✅ EXACT | `Action_PassBlock` | RG | `5` | `4` | 27 | START | 27 | 89 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `8` | `7` | 27 | START | 27 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `8` | `7` | 27 | START | 27 | 45 |
| ✅ EXACT | `Action_SnapReceive` | C | `7` | `6` | 39 | END | 24 | 39 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | C | `7` | `6` | 43 | START | 43 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `7` | `6` | 51 | START | 51 | 165 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 108 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 199 | 176 | inferred_complete_timeline |
| `Action_None` | 210 | 224 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 76 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_None` | 109 | 165 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 45 | 19 | inferred_complete_timeline |
| `Action_PassBlock` | 48 | 108 | 61 | inferred_complete_timeline |
| `Action_None` | 109 | 138 | 30 | inferred_complete_timeline |
| `Action_None` | 142 | 179 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 39 | 16 | inferred_complete_timeline |
| `Action_None` | 40 | 42 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 43 | 50 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 51 | 165 | 115 | inferred_complete_timeline |
| `Action_BallCarry` | 172 | 191 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 89 | 63 | inferred_complete_timeline |
| `Action_None` | 109 | 187 | 79 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 207 | 274 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 108 | 82 | inferred_complete_timeline |
| `Action_None` | 109 | 138 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 109 | 86 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 129 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 28 | 5 | inferred_complete_timeline |
| `Action_None` | 96 | 231 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 41 | 69 | 29 | inferred_complete_timeline |
| `Action_None` | 73 | 78 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 182 | 159 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 26–299 | 211 | 7 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 37–164 | 101 | 2 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 37–165 | 123 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 94–221 | 82 | 4 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 100–243 | 101 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 116–120 | 5 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 121–184 | 55 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 127–171 | 45 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 166–299 | 94 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 169–278 | 105 | 3 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 172–187 | 16 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 177–299 | 123 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 190–299 | 110 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 206–299 | 56 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 213–299 | 87 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 224–229 | 6 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 251–299 | 49 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `17` (Position_Unknown): Annotated start 24 != Inferred start 100
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 71: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_PassBlock' for track '6' has invalid range: start=27, end=23. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=100, end=39. Clamping end to start.
- ⚠️ Action 'Action_PassBlock' range [27-76] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-199] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-138] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-89] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-187] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-274] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-182] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [51-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [172-191] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-45] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-179] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-38] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-28] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-231] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-129] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-201] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-242] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-116] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-54] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-80] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-165] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-158] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-172] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-171] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-195] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-230] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-299] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-274] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-299] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>