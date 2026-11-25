# Play-Annotation-Generator Annotation Review — InsideZoneRead_157

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_157`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 45
- **Validation Warnings:** 74
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 0
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 9
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 20
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `21` | `17` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `4` | `3` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | offense | `9` | `8` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | DT2 | defense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DT2 | defense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT2 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 2 | START | 0 | 187 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 2 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 0 | 261 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 2 | START | 0 | 218 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 2 | START | 0 | 249 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 2 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 2 | START | 0 | 299 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `21` | `17` | 324 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `13` | `12` | 327 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RT | `2` | `1` | 327 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `4` | `3` | 327 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LT | `6` | `5` | 327 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | LG | `9` | `8` | 327 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | DT2 | `11` | `10` | 337 | END | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_ReadDefender` | DT2 | `11` | `10` | 343 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | DT2 | `11` | `10` | 362 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 391 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 269 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 160 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 249 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–286
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 187 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 191 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 274 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 286 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–285
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 218 | 219 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 276 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 278 | 285 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–261
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 261 | 262 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 207 | 208 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 218 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 299 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 296 | 297 | inferred_complete_timeline |
| `Action_PreSnap` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 299 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 195–299 | 77 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 203–221 | 19 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 234–279 | 45 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 234–299 | 63 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 235–299 | 65 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 246–299 | 54 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 256–299 | 17 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 277–299 | 23 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 290–299 | 10 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 294–299 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `21` (Position_Unknown)
- ❌ Missing segment for action `Action_ZoneBlock` on target `13` (C)
- ❌ Missing segment for action `Action_ZoneBlock` on target `2` (RT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `4` (RG)
- ❌ Missing segment for action `Action_ZoneBlock` on target `6` (LT)
- ❌ Missing segment for action `Action_ZoneBlock` on target `9` (LG)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (DT2)
- ❌ Missing segment for action `Action_ReadDefender` on target `11` (DT2)
- ❌ Missing segment for action `Action_BallCarry` on target `11` (DT2)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 9 |
| Other | 12 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '1' has invalid range: start=327, end=261. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '3' has invalid range: start=327, end=285. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '5' has invalid range: start=327, end=299. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '8' has invalid range: start=327, end=299. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '10' has invalid range: start=324, end=299. Clamping end to start.
- ⚠️ Segment 'Action_ReadDefender' for track '10' has invalid range: start=343, end=299. Clamping end to start.
- ⚠️ Segment 'Action_BallCarry' for track '10' has invalid range: start=362, end=299. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '12' has invalid range: start=327, end=286. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=324, end=279. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-261] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-218] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-276] for track '3' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-285] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-249] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-296] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-299] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-187] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-191] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-202] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-274] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-221] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-279] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-278] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-262] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '24' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_BallSnap' has invalid start frame 324. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
- ⚠️ Action event 'Action_ZoneBlock' has invalid start frame 327. Video range is [0, 299].
- ⚠️ Action event 'Action_SnapReceive' has invalid start frame 337. Video range is [0, 299].
- ⚠️ Action event 'Action_ReadDefender' has invalid start frame 343. Video range is [0, 299].
- ⚠️ Action event 'Action_BallCarry' has invalid start frame 362. Video range is [0, 299].
- ⚠️ Action event 'Action_None' has invalid start frame 391. Video range is [0, 299].
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_157'; source metadata written as null.

</details>