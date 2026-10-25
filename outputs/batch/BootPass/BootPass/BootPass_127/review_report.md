# Play-Annotation-Generator Annotation Review — BootPass_127

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_127`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 92
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 3
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `15` | `13` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `10` | `10` |
| ✅ EXACT | `Action_FakeHandoff` | CB1 | defense | `10` | `10` |
| ✅ EXACT | `Action_BootAway` | CB3 | defense | `11` | `11` |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `15` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 74 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `15` | `13` | 75 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | Position_Unknown | `12` | `12` | 116 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `10` | `10` | 127 | END | 75 | 127 |
| ✅ EXACT | `Action_FakeHandoff` | CB1 | `10` | `10` | 136 | START | 136 | 150 |
| ✅ EXACT | `Action_BootAway` | CB3 | `11` | `11` | 151 | START | 151 | 178 |
| ⚠️ START CHANGED | `Action_SecureCatch` | Position_Unknown | `15` | `13` | 157 | START | 183 | 183 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 389 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 198 | 124 | inferred_complete_timeline |
| `Action_None` | 201 | 365 | 165 | inferred_complete_timeline |
| `Action_None` | 368 | 389 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 389 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 189 | 115 | inferred_complete_timeline |
| `Action_None` | 194 | 389 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 389 | 315 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 289 | 215 | inferred_complete_timeline |
| `Action_None` | 293 | 310 | 18 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 362 | 288 | inferred_complete_timeline |
| `Action_None` | 365 | 367 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_SnapReceive` | 75 | 127 | 53 | inferred_complete_timeline |
| `Action_None` | 128 | 135 | 8 | inferred_complete_timeline |
| `Action_FakeHandoff` | 136 | 150 | 15 | inferred_complete_timeline |
| `Action_None` | 151 | 389 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 287 | 213 | inferred_complete_timeline |
| `Action_None` | 292 | 389 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_BootAway` | 151 | 178 | 28 | inferred_complete_timeline |
| `Action_None` | 179 | 227 | 49 | inferred_complete_timeline |
| `Action_None` | 230 | 389 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 339 | 265 | inferred_complete_timeline |
| `Action_None` | 342 | 379 | 38 | inferred_complete_timeline |
| `Action_None` | 381 | 386 | 6 | inferred_complete_timeline |
| `Action_None` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_None` | 75 | 389 | 315 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 14–32 | 19 | 1 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 183–265 | 61 | 5 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 195–264 | 57 | 6 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 195–244 | 43 | 3 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 204–253 | 50 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 206–318 | 111 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 206–264 | 54 | 3 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 207–266 | 60 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 207–264 | 57 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 223–265 | 36 | 2 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 336–338 | 3 | 1 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 343–389 | 36 | 3 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 361–362 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 364–389 | 25 | 2 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 375–385 | 11 | 1 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 377–389 | 13 | 1 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 378–379 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `15` (Position_Unknown)
- ❌ Missing segment for action `Action_ThrowPass` on target `12` (Position_Unknown)
- ⚠️ `Action_SecureCatch` for actor_track_id `15` (Position_Unknown): Annotated start 157 != Inferred start 183

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 121 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 52 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_ThrowPass' for track '12' has invalid range: start=116, end=32. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '13' has invalid range: start=183, end=127. Clamping end to start.
- ⚠️ Segment 'Action_SecureCatch' for track '13' has invalid range: start=183, end=175. Clamping end to start.
- ⚠️ Action 'Action_None' range [75-389] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-198] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-365] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-389] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-379] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-386] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-287] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-289] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-310] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-318] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-362] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-367] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-227] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-32] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-234] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-258] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-198] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-253] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-311] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-236] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-266] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-214] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-264] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-232] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-265] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-338] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-357] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-373] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-389] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-367] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-385] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '29' has 1 frames without a visible bounding box.
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

</details>