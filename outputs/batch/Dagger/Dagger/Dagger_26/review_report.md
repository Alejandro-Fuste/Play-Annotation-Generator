# Play-Annotation-Generator Annotation Review — Dagger_26

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_26`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Fum`
- **Result Frame:** 479
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR2 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ClearToEdge` | WR1 | offense | `6` | `6` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 204 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 6 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 10 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 204 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 180 | START | 180 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 183 | START | 231 | 237 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB | `14` | `14` | 185 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BreakInside` | WR2 | `0` | `0` | 205 | START | 205 | 325 |
| ⚠️ AMBIGUOUS MATCH | `Action_ClearToEdge` | WR1 | `6` | `6` | 205 | START | 205 | 285 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `14` | `14` | 279 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 10 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 63 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 67 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 220 | 41 | inferred_complete_timeline |
| `Action_None` | 223 | 230 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_ClearToEdge` | 205 | 285 | 81 | inferred_complete_timeline |
| `Action_ClearToEdge` | 289 | 289 | 1 | inferred_complete_timeline |
| `Action_None` | 290 | 479 | 190 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 204 | 205 | inferred_complete_timeline |
| `Action_BreakInside` | 205 | 325 | 121 | inferred_complete_timeline |
| `Action_BreakInside` | 327 | 332 | 6 | inferred_complete_timeline |
| `Action_None` | 333 | 336 | 4 | inferred_complete_timeline |
| `Action_None` | 350 | 368 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–17
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 17 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 10–261
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 63 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 179 | 113 | inferred_complete_timeline |
| `Action_BallSnap` | 180 | 185 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 231 | 237 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 259 | 261 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 49 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–392
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 335 | 156 | inferred_complete_timeline |
| `Action_None` | 337 | 340 | 4 | inferred_complete_timeline |
| `Action_None` | 354 | 392 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 395 | 216 | inferred_complete_timeline |
| `Action_None` | 433 | 479 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 323 | 144 | inferred_complete_timeline |
| `Action_None` | 325 | 343 | 19 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 81 | 179 | 99 | inferred_complete_timeline |
| `Action_None` | 180 | 194 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 471 | 292 | inferred_complete_timeline |
| `Action_None` | 473 | 479 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 438 | 259 | inferred_complete_timeline |
| `Action_None` | 445 | 479 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 383 | 204 | inferred_complete_timeline |
| `Action_None` | 386 | 479 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 412 | 233 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–13 | 14 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–11 | 12 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–192 | 193 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 115–207 | 61 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 180–307 | 124 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 204–225 | 22 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 246–383 | 138 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 271–457 | 175 | 3 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 297–301 | 5 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 303–308 | 6 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 303–348 | 25 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 303–306 | 4 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 346–350 | 5 | 1 | Undefined position; Undefined team |
| `29` | `54` | Position_Unknown | Team_Unknown | 362–363 | 2 | 1 | Undefined position; Undefined team |
| `30` | `57` | Position_Unknown | Team_Unknown | 369–376 | 8 | 1 | Undefined position; Undefined team |
| `31` | `59` | Position_Unknown | Team_Unknown | 372–378 | 7 | 1 | Undefined position; Undefined team |
| `32` | `60` | Position_Unknown | Team_Unknown | 376–468 | 54 | 6 | Undefined position; Undefined team |
| `33` | `62` | Position_Unknown | Team_Unknown | 415–479 | 54 | 3 | Undefined position; Undefined team |
| `34` | `65` | Position_Unknown | Team_Unknown | 424–479 | 56 | 1 | Undefined position; Undefined team |
| `35` | `66` | Position_Unknown | Team_Unknown | 435–479 | 45 | 1 | Undefined position; Undefined team |
| `36` | `67` | Position_Unknown | Team_Unknown | 439–465 | 27 | 1 | Undefined position; Undefined team |
| `37` | `70` | Position_Unknown | Team_Unknown | 448–479 | 32 | 1 | Undefined position; Undefined team |
| `38` | `71` | Position_Unknown | Team_Unknown | 458–479 | 22 | 1 | Undefined position; Undefined team |
| `39` | `72` | Position_Unknown | Team_Unknown | 461–477 | 17 | 1 | Undefined position; Undefined team |
| `40` | `73` | Position_Unknown | Team_Unknown | 475–479 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `14` (QB)
- ⚠️ Ambiguous match for action `Action_BreakInside` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ClearToEdge` and target `6` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `14` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 74 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '14' has invalid range: start=180, end=67. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '14' has invalid range: start=279, end=67. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [180–185], lower_priority='Action_PassBlock' annotated_start=183, effective_Action_PassBlock_start=186.
- ⚠️ Action 'Action_BreakInside' range [205-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-368] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-343] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-383] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-220] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-438] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-395] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-479] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [205-285] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-194] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-471] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-412] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-335] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-340] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-392] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-63] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-17] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-29] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-63] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [180-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [231-237] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [259-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-207] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-301] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-383] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-280] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-447] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-301] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-348] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-376] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-380] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-388] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-427] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-440] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-468] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-429] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-479] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-465] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-477] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-479] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>