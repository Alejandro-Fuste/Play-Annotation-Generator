# Play-Annotation-Generator Annotation Review — Dagger_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_38`
- **Frame Range:** 0 to 538 (539 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 538
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 165
- **Validation Warnings:** 221
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 142
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `16` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | WR2 | offense | `14` | `14` |
| ✅ EXACT | `Action_BreakInside` | WR3 | offense | `9` | `9` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `11` | `11` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | WR2 | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `0` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 0 | START | 0 | 339 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 328 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 353 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `18` | `16` | 329 | START | 329 | 329 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | LT | `15` | `15` | 332 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | WR2 | `14` | `14` | 333 | END | N/A | N/A |
| ✅ EXACT | `Action_BreakInside` | WR3 | `9` | `9` | 354 | START | 354 | 475 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `11` | `11` | 354 | START | 354 | 406 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | WR2 | `14` | `14` | 418 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 491 | 163 | inferred_complete_timeline |
| `Action_None` | 493 | 494 | 2 | inferred_complete_timeline |
| `Action_None` | 498 | 499 | 2 | inferred_complete_timeline |
| `Action_None` | 501 | 538 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 389 | 61 | inferred_complete_timeline |
| `Action_None` | 392 | 455 | 64 | inferred_complete_timeline |
| `Action_None` | 458 | 472 | 15 | inferred_complete_timeline |
| `Action_None` | 476 | 538 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–471
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 339 | 340 | inferred_complete_timeline |
| `Action_PreSnap` | 346 | 347 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 353 | 5 | inferred_complete_timeline |
| `Action_ClearToEdge` | 354 | 406 | 53 | inferred_complete_timeline |
| `Action_None` | 443 | 447 | 5 | inferred_complete_timeline |
| `Action_None` | 449 | 467 | 19 | inferred_complete_timeline |
| `Action_None` | 470 | 471 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–7
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–538
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 353 | 354 | inferred_complete_timeline |
| `Action_BreakInside` | 354 | 475 | 122 | inferred_complete_timeline |
| `Action_None` | 476 | 538 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–403
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 70 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 328 | 203 | inferred_complete_timeline |
| `Action_None` | 329 | 403 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 58 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 87 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 93 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 150 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 47 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 150 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 538 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 421 | 93 | inferred_complete_timeline |
| `Action_None` | 424 | 428 | 5 | inferred_complete_timeline |
| `Action_None` | 431 | 439 | 9 | inferred_complete_timeline |
| `Action_None` | 443 | 444 | 2 | inferred_complete_timeline |
| `Action_None` | 446 | 538 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 375 | 47 | inferred_complete_timeline |
| `Action_None` | 381 | 479 | 99 | inferred_complete_timeline |
| `Action_None` | 482 | 483 | 2 | inferred_complete_timeline |
| `Action_None` | 489 | 538 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 377 | 49 | inferred_complete_timeline |
| `Action_None` | 380 | 538 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–538
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 538 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–537
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_None` | 329 | 467 | 139 | inferred_complete_timeline |
| `Action_None` | 471 | 521 | 51 | inferred_complete_timeline |
| `Action_None` | 524 | 537 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–538 | 539 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 10–329 | 293 | 5 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 127–150 | 22 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 127–150 | 24 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 127–150 | 22 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 127–451 | 146 | 9 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 127–150 | 18 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 136–149 | 6 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 251–410 | 89 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 342–410 | 62 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 346–403 | 40 | 3 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 351–355 | 5 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 351–459 | 48 | 7 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 351–401 | 49 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 352–451 | 53 | 3 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 355–538 | 180 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 379–387 | 9 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 382–406 | 24 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 446–447 | 2 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 447–471 | 21 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 450–498 | 25 | 4 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 451–462 | 10 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 451–520 | 53 | 4 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 451–455 | 5 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 457–458 | 2 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 473–534 | 60 | 3 | Undefined position; Undefined team |
| `41` | `56` | Position_Unknown | Team_Unknown | 481–538 | 48 | 5 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 482–491 | 8 | 2 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 482–508 | 26 | 2 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 483–484 | 2 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 488–511 | 17 | 4 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 489–501 | 13 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 490–538 | 27 | 4 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 490–503 | 14 | 1 | Undefined position; Undefined team |
| `49` | `68` | Position_Unknown | Team_Unknown | 490–503 | 13 | 2 | Undefined position; Undefined team |
| `50` | `69` | Position_Unknown | Team_Unknown | 491–496 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PassBlock` on target `15` (LT)
- ❌ Missing segment for action `Action_SnapReceive` on target `14` (WR2)
- ❌ Missing segment for action `Action_ThrowPass` on target `14` (WR2)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 144 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 40: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 538 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '14' has invalid range: start=329, end=7. Clamping end to start.
- ⚠️ Segment 'Action_ThrowPass' for track '14' has invalid range: start=418, end=7. Clamping end to start.
- ⚠️ Segment 'Action_PassBlock' for track '15' has invalid range: start=332, end=150. Clamping end to start.
- ⚠️ Action 'Action_None' range [329-389] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-455] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-472] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-538] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-421] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-428] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-439] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-375] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-479] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-491] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-499] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-467] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-521] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-537] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-377] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BreakInside' range [354-475] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-49] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-87] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-150] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-339] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ClearToEdge' range [354-406] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-447] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-467] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-471] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-70] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-403] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-47] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-105] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-30] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-56] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-82] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' for track '16' starts at frame 329, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallSnap' range [329-329] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-145] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-150] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-145] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-161] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-251] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-367] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-426] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-141] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-150] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-259] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-271] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-279] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-395] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-403] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-410] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-349] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-403] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-375] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-387] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-398] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-455] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-401] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-367] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-403] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-451] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-434] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-538] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-387] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-406] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-447] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-455] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-471] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-455] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-464] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-498] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-462] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-479] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-520] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-455] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-458] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-475] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-489] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-534] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-501] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-513] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-491] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-486] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-508] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-511] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-501] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-495] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-519] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-503] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-503] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-496] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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

</details>