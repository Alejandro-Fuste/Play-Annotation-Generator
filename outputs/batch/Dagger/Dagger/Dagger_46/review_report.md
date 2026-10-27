# Play-Annotation-Generator Annotation Review — Dagger_46

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_46`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 328
- **Player Tracks:** 21
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | CB4 | defense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR3 | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ClearToEdge` | Position_Unknown | Team_Unknown | `13` | `12` |
| ✅ EXACT | `Action_ThrowPass` | CB4 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 203 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 191 | START | 191 | 196 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `10` | `10` | 194 | START | 197 | 200 |
| ✅ EXACT | `Action_SnapReceive` | CB4 | `2` | `2` | 196 | END | 191 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR3 | `6` | `6` | 204 | START | 204 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_ClearToEdge` | Position_Unknown | `13` | `12` | 204 | START | 218 | 241 |
| ✅ EXACT | `Action_ThrowPass` | CB4 | `2` | `2` | 271 | START | 271 | 280 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 273 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–278
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 197 | 7 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 278 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 301 | 111 | inferred_complete_timeline |
| `Action_None` | 303 | 328 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_BreakInside` | 204 | 235 | 32 | inferred_complete_timeline |
| `Action_BreakInside` | 237 | 303 | 67 | inferred_complete_timeline |
| `Action_None` | 304 | 310 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_BallSnap` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 197 | 200 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 47 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 51 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 190 | 135 | inferred_complete_timeline |
| `Action_None` | 191 | 328 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 66 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 125 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 139 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 190 | 46 | inferred_complete_timeline |
| `Action_None` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_None` | 222 | 328 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 328 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 296 | 106 | inferred_complete_timeline |
| `Action_None` | 298 | 300 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 328 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_SnapReceive` | 191 | 196 | 6 | inferred_complete_timeline |
| `Action_None` | 197 | 270 | 74 | inferred_complete_timeline |
| `Action_ThrowPass` | 271 | 280 | 10 | inferred_complete_timeline |
| `Action_None` | 281 | 328 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_None` | 191 | 328 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 218–305 | 78 | 5 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 235–239 | 4 | 2 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 299–308 | 10 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 301–328 | 26 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 310–328 | 18 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 320–328 | 7 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 324–328 | 5 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 324–328 | 5 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 327–328 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `10` (C): Annotated start 194 != Inferred start 197
- ⚠️ Ambiguous match for action `Action_BreakInside` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ClearToEdge` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [191–196], lower_priority='Action_PassBlock' annotated_start=194, effective_Action_PassBlock_start=197.
- ⚠️ Action 'Action_None' range [191-296] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-278] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-328] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [204-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-310] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-328] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-66] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [197-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [218-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-289] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-328] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-324] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-328] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '19' has 1 frames without a visible bounding box.
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

</details>