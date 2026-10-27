# Play-Annotation-Generator Annotation Review — CrackToss_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_2`
- **Frame Range:** 0 to 538 (539 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 538
- **Player Tracks:** 51
- **Ball Tracks:** 2
- **Action Segments:** 137
- **Validation Warnings:** 193
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 5
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 120
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_CrackBlock` | TE1 | offense | `2` | `1` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `18` | `15` |
| ℹ️ GLOBAL EVENT | `Action_CrackBlock` | N/A | N/A | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB1 | offense | `13` | `12` |
| ✅ EXACT | `Action_PullBlock` | TE2 | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LT | offense | `8` | `7` |
| ❌ MISSING SEGMENT | `Action_Toss` | QB1 | offense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB2 | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB1 | `13` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 4 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB2 | `7` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ EXACT | `Action_CrackBlock` | TE1 | `2` | `1` | 5 | START | 5 | 128 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `18` | `15` | 42 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_CrackBlock` | N/A | N/A | N/A | 51 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | QB1 | `13` | `12` | 51 | END | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | TE2 | `3` | `2` | 52 | START | 52 | 128 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | LT | `8` | `7` | 52 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_Toss` | QB1 | `13` | `12` | 59 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_BallCarry` | QB2 | `7` | `6` | 79 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 128 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 5 | 41 | 37 | inferred_complete_timeline |
| `Action_None` | 42 | 338 | 297 | inferred_complete_timeline |
| `Action_None` | 340 | 380 | 41 | inferred_complete_timeline |
| `Action_None` | 382 | 383 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 479 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_CrackBlock` | 5 | 128 | 124 | inferred_complete_timeline |
| `Action_None` | 129 | 350 | 222 | inferred_complete_timeline |
| `Action_None` | 355 | 362 | 8 | inferred_complete_timeline |
| `Action_None` | 365 | 370 | 6 | inferred_complete_timeline |
| `Action_None` | 373 | 538 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 51 | 52 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 128 | 77 | inferred_complete_timeline |
| `Action_None` | 129 | 192 | 64 | inferred_complete_timeline |
| `Action_None` | 199 | 310 | 112 | inferred_complete_timeline |
| `Action_None` | 368 | 486 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–5
- **Visible Samples:** 6

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 338 | 297 | inferred_complete_timeline |
| `Action_None` | 342 | 347 | 6 | inferred_complete_timeline |
| `Action_None` | 350 | 353 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 4–10
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 10 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 448 | 407 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–503
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_None` | 42 | 503 | 462 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `20` | Position_Unknown | Team_Unknown | 5–7 | 3 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 8–352 | 345 | 2 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 11–538 | 528 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 11–310 | 300 | 2 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 11–538 | 528 | 2 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 11–454 | 444 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 11–425 | 415 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 11–308 | 296 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 11–413 | 399 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 11–304 | 286 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 11–528 | 514 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 11–324 | 314 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 11–515 | 395 | 11 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 11–508 | 444 | 7 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 34–434 | 392 | 6 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 259–272 | 10 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 314–500 | 178 | 3 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 320–368 | 43 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 329–386 | 58 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 331–355 | 16 | 4 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 354–443 | 69 | 5 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 364–374 | 11 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 376–442 | 64 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 378–457 | 79 | 2 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 408–433 | 11 | 3 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 408–419 | 7 | 2 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 408–411 | 4 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 412–490 | 39 | 4 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 415–453 | 7 | 2 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 416–420 | 5 | 1 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 416–452 | 19 | 5 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 426–427 | 2 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 451–452 | 2 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 453–463 | 5 | 2 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 476–486 | 10 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `31` | `38` | 143 | 143 | 1 | 100.0% | None |
| `32` | `39` | 160 | 193 | 12 | 35.3% | 169–182, 184–185, 187–192 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `18` (C)
- ❌ Missing segment for action `Action_SnapReceive` on target `13` (QB1)
- ❌ Missing segment for action `Action_PullBlock` on target `8` (LT)
- ❌ Missing segment for action `Action_Toss` on target `13` (QB1)
- ❌ Missing segment for action `Action_BallCarry` on target `7` (QB2)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 9 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 538 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '6' has invalid range: start=79, end=10. Clamping end to start.
- ⚠️ Segment 'Action_PullBlock' for track '7' has invalid range: start=52, end=5. Clamping end to start.
- ⚠️ Segment 'Action_SnapReceive' for track '12' has invalid range: start=42, end=10. Clamping end to start.
- ⚠️ Segment 'Action_Toss' for track '12' has invalid range: start=59, end=10. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '15' has invalid range: start=42, end=10. Clamping end to start.
- ⚠️ Action 'Action_None' range [42-448] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-350] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-362] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-370] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-192] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-310] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-486] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-338] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-347] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-503] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-338] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-380] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-479] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-10] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-352] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-538] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-310] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-454] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-425] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-308] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-320] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-407] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-413] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-287] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-173] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-528] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-324] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-80] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-85] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-111] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-147] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-183] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-304] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-473] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-515] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-135] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-212] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-227] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-322] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-395] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-508] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-371] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-398] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-426] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-268] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-331] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-500] for track '34' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-350] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-386] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-337] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-349] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-396] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-443] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-374] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-442] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-392] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-457] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-414] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-418] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-419] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-411] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-430] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-455] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-490] for track '45' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-453] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-420] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-422] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-481] for track '52' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>