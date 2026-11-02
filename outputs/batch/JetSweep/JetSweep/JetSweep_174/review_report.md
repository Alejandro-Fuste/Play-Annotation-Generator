# Play-Annotation-Generator Annotation Review — JetSweep_174

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_174`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 8
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `18` | `17` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `8` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Toss` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 140 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 140 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `18` | `17` | 139 | START | 139 | 162 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 141 | START | 141 | 147 |
| ✅ EXACT | `Action_LeadBlock` | TE | `8` | `7` | 143 | START | 143 | 194 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `0` | 143 | START | 143 | 196 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `11` | 143 | START | 143 | 196 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `15` | `14` | 143 | START | 148 | 196 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 143 | START | 143 | 196 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 147 | END | 141 | 147 |
| ✅ EXACT | `Action_Toss` | QB | `9` | `8` | 162 | START | 162 | 162 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `18` | `17` | 163 | START | 163 | 166 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 196 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_SnapReceive` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_Toss` | 162 | 162 | 1 | inferred_complete_timeline |
| `Action_None` | 163 | 215 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_LeadBlock` | 143 | 194 | 52 | inferred_complete_timeline |
| `Action_None` | 201 | 207 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 196 | 54 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 196 | 54 | inferred_complete_timeline |
| `Action_None` | 197 | 299 | 103 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_BallSnap` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 148 | 196 | 49 | inferred_complete_timeline |
| `Action_None` | 197 | 231 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_ZoneBlock` | 143 | 196 | 54 | inferred_complete_timeline |
| `Action_None` | 197 | 203 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 198 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 150 | 10 | inferred_complete_timeline |
| `Action_None` | 157 | 159 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 84 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 87 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 99 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 111 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 114 | 115 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 140 | 8 | inferred_complete_timeline |
| `Action_None` | 141 | 147 | 7 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 201 | 61 | inferred_complete_timeline |
| `Action_None` | 232 | 257 | 26 | inferred_complete_timeline |
| `Action_None` | 259 | 299 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 127 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 140 | 11 | inferred_complete_timeline |
| `Action_None` | 141 | 256 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 140 | 141 | inferred_complete_timeline |
| `Action_None` | 141 | 193 | 53 | inferred_complete_timeline |
| `Action_None` | 197 | 297 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–222 | 223 | 2 | Undefined position; Undefined team |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 17–18 | 2 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 127–285 | 156 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 139–272 | 132 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 157–166 | 10 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 157–162 | 6 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 174–299 | 126 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 180–267 | 43 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 192–299 | 40 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 195–279 | 84 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 200–201 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 202–299 | 79 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 218–278 | 61 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 233–299 | 67 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 279–299 | 21 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `15` (C): Annotated start 143 != Inferred start 148
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 350: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [141–147], lower_priority='Action_ZoneBlock' annotated_start=143, effective_Action_ZoneBlock_start=148.
- ⚠️ Action 'Action_None' range [197-203] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-222] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-297] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-201] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-257] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [143-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-87] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-99] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-147] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-159] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-299] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-127] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-256] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-140] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-279] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-166] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [169-272] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-299] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-267] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-270] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-278] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>