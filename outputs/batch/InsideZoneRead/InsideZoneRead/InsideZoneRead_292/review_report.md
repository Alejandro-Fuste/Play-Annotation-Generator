# Play-Annotation-Generator Annotation Review — InsideZoneRead_292

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_292`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_Keep` | QB | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 2 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `22` | `18` | 3 | START | 135 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `9` | 6 | START | 6 | 125 |
| ✅ EXACT | `Action_ZoneBlock` | C | `13` | `12` | 6 | START | 6 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `2` | `1` | 6 | START | 6 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `3` | 6 | START | 6 | 146 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `4` | 6 | START | 6 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 14 | END | 3 | 14 |
| ✅ EXACT | `Action_ReadDefender` | QB | `6` | `5` | 22 | START | 22 | 32 |
| ✅ EXACT | `Action_Keep` | QB | `6` | `5` | 33 | START | 33 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `6` | `5` | 50 | START | 50 | 104 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 146 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 14 | 12 | inferred_complete_timeline |
| `Action_None` | 15 | 21 | 7 | inferred_complete_timeline |
| `Action_ReadDefender` | 22 | 32 | 11 | inferred_complete_timeline |
| `Action_Keep` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 50 | 104 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 181 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 206 | 207 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 223 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 249 | 263 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 299 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 301 | 324 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 337 | 340 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 343 | 346 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 349 | 359 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 361 | 378 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 380 | 387 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 393 | 394 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 409 | 412 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 419 | 449 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 449 | 447 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_None` | 147 | 449 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_None` | 147 | 449 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_None` | 147 | 449 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 125 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 139 | 141 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 449 | 303 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 6 | 146 | 141 | inferred_complete_timeline |
| `Action_None` | 147 | 449 | 303 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 104 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 40 | 38 | inferred_complete_timeline |
| `Action_None` | 49 | 449 | 401 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 438

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 45 | 43 | inferred_complete_timeline |
| `Action_None` | 51 | 77 | 27 | inferred_complete_timeline |
| `Action_None` | 83 | 100 | 18 | inferred_complete_timeline |
| `Action_None` | 103 | 449 | 347 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 19 | 17 | inferred_complete_timeline |
| `Action_None` | 22 | 27 | 6 | inferred_complete_timeline |
| `Action_None` | 32 | 117 | 86 | inferred_complete_timeline |
| `Action_None` | 120 | 449 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 87 | 85 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 449 | 447 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 110 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–444
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 3 | 108 | 106 | inferred_complete_timeline |
| `Action_None` | 123 | 373 | 251 | inferred_complete_timeline |
| `Action_None` | 375 | 419 | 45 | inferred_complete_timeline |
| `Action_None` | 423 | 426 | 4 | inferred_complete_timeline |
| `Action_None` | 430 | 431 | 2 | inferred_complete_timeline |
| `Action_None` | 440 | 444 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `18` | Position_Unknown | Team_Unknown | 107–449 | 333 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 112–424 | 313 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 121–125 | 5 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 135–449 | 315 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 158–449 | 283 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 165–185 | 21 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 189–194 | 6 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 192–266 | 75 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 211–449 | 239 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 239–449 | 211 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 261–449 | 189 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 282–444 | 156 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 308–310 | 3 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `22` (Position_Unknown): Annotated start 3 != Inferred start 135
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (18 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 6 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '3' (LG) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '9' (RG) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '12' (C) duration 141 frames exceeds threshold 90 frames [start=6, end=146].
- ⚠️ Segment 'Action_BallSnap' for track '18' has invalid range: start=135, end=14. Clamping end to start.
- ⚠️ Action 'Action_None' range [3-110] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-87] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [50-104] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [189-197] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [206-207] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [214-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-247] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [249-263] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-324] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [337-340] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-346] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [349-359] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [361-378] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [380-387] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [393-394] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [409-412] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [6-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [139-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-45] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-77] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-100] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-373] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-419] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-444] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-40] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-449] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [3-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-424] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-449] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-270] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-422] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-185] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-266] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-328] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-419] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-444] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-310] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_292'; source metadata written as null.

</details>