# Play-Annotation-Generator Annotation Review — Draw_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_16`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 89
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `5` | `4` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 42 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 43 | START | 43 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `1` | `0` | 47 | START | 47 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `13` | `12` | 47 | START | 56 | 117 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `5` | `4` | 47 | START | 47 | 155 |
| ✅ EXACT | `Action_PassBlock` | LG | `6` | `5` | 47 | START | 47 | 155 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 55 | END | 43 | 55 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `7` | `6` | 59 | START | 59 | 86 |
| ✅ EXACT | `Action_BallCarry` | QB | `7` | `6` | 87 | START | 87 | 264 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 155 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_SnapReceive` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_None` | 56 | 58 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 59 | 86 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 264 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 77 | 35 | inferred_complete_timeline |
| `Action_None` | 112 | 121 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 155 | 109 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_BallSnap` | 43 | 55 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 117 | 62 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 129 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 155 | 109 | inferred_complete_timeline |
| `Action_None` | 156 | 232 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 47 | 81 | 35 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 117 | 31 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 126 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 128 | 155 | 28 | inferred_complete_timeline |
| `Action_None` | 156 | 191 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–93
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 93 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 242 | 200 | inferred_complete_timeline |
| `Action_None` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_None` | 257 | 269 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 125 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–111
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 69 | 27 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 81 | 88 | 8 | inferred_complete_timeline |
| `Action_None` | 90 | 111 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 122 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |
| `Action_None` | 43 | 211 | 169 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `10` | `11` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `13` | `17` | Position_Unknown | Team_Unknown | 37–69 | 24 | 4 | Undefined position; Undefined team |
| `14` | `19` | Position_Unknown | Team_Unknown | 50–51 | 2 | 1 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 51–65 | 15 | 1 | Undefined position; Undefined team |
| `16` | `23` | Position_Unknown | Team_Unknown | 76–269 | 194 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 98–103 | 6 | 1 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 104–202 | 51 | 2 | Undefined position; Undefined team |
| `19` | `27` | Position_Unknown | Team_Unknown | 114–269 | 156 | 1 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 131–266 | 126 | 6 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 147–269 | 118 | 3 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 155–173 | 19 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 156–176 | 21 | 1 | Undefined position; Undefined team |
| `24` | `36` | Position_Unknown | Team_Unknown | 174–269 | 96 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 182–269 | 88 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 200–261 | 62 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 209–212 | 4 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 228–269 | 42 | 1 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 234–263 | 30 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 243–269 | 27 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 262–269 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `1` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 34: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [43–55], lower_priority='Action_PassBlock' annotated_start=47, effective_Action_PassBlock_start=56.
- ⚠️ Action 'Action_PassBlock' range [47-81] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-126] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-191] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-77] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-242] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-253] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [47-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-232] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [87-264] for track '6' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-125] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-69] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-111] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-117] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-129] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 43, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [43-49] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-69] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-136] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-169] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-204] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-266] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-202] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-261] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
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