# Play-Annotation-Generator Annotation Review — StopAndGo_17

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_17`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `21` | `21` |
| ✅ EXACT | `Action_VerticalStem` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `17` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 4 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 5 | START | 5 | 19 |
| ✅ EXACT | `Action_PassBlock` | LT | `12` | `12` | 8 | START | 8 | 173 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `13` | `13` | 8 | START | 8 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `16` | `16` | 8 | START | 8 | 64 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `19` | `19` | 8 | START | 20 | 32 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 8 | START | 8 | 213 |
| ✅ EXACT | `Action_SnapReceive` | QB | `21` | `21` | 19 | END | 5 | 19 |
| ✅ EXACT | `Action_VerticalStem` | WR1 | `0` | `0` | 19 | START | 19 | 49 |
| ✅ EXACT | `Action_SellStop` | WR1 | `0` | `0` | 50 | START | 50 | 73 |
| ✅ EXACT | `Action_RunGoRoute` | WR1 | `0` | `0` | 74 | START | 74 | 299 |
| ✅ EXACT | `Action_ThrowPass` | QB | `21` | `21` | 98 | START | 98 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_None` | 20 | 97 | 78 | inferred_complete_timeline |
| `Action_ThrowPass` | 98 | 109 | 12 | inferred_complete_timeline |
| `Action_None` | 110 | 180 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 162 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 174 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_VerticalStem` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_SellStop` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_RunGoRoute` | 74 | 299 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 201 | 197 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 299 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 173 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 213 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_BallSnap` | 5 | 19 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 20 | 32 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 91 | 84 | inferred_complete_timeline |
| `Action_PassBlock` | 93 | 193 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 8 | 64 | 57 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 165 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 40 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 143 | 139 | inferred_complete_timeline |
| `Action_None` | 145 | 239 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 157 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–257
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 257 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 71 | 67 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 104 | 4 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 299 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 89 | 85 | inferred_complete_timeline |
| `Action_None` | 98 | 238 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 299 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 99 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 5 | 299 | 295 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–299 | 300 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 46–65 | 14 | 4 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 93–168 | 69 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 137–233 | 97 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 142–176 | 35 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 146–299 | 154 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 232–233 | 2 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 259–260 | 2 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 262–299 | 38 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 297–299 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ `Action_PassBlock` for actor_track_id `19` (C): Annotated start 8 != Inferred start 20

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 30: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [5–19], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=20.
- ⚠️ Action 'Action_None' range [5-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-89] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-143] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-71] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-104] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-91] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [93-193] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-162] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [5-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [20-32] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [8-213] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-233] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-176] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>