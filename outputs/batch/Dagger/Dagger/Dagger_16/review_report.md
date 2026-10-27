# Play-Annotation-Generator Annotation Review — Dagger_16

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Dagger_16`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Pass_Dagger`
- **Result:** `Result_Rec`
- **Result Frame:** 509
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_BreakInside` | WR2 | offense | `2` | `2` |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | offense | `5` | `5` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `19` | `Group` | 0 | START | 0 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 189 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 190 | START | 190 | 204 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `12` | `12` | 193 | START | 205 | 425 |
| ✅ EXACT | `Action_PassBlock` | LG | `17` | `17` | 193 | START | 193 | 428 |
| ✅ EXACT | `Action_PassBlock` | RT | `18` | `18` | 193 | START | 193 | 472 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 193 | START | 193 | 448 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `4` | `4` | 193 | START | 193 | 318 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `13` | 204 | END | 190 | 204 |
| ✅ EXACT | `Action_BreakInside` | WR2 | `2` | `2` | 215 | START | 215 | 311 |
| ✅ EXACT | `Action_ClearToEdge` | WR1 | `5` | `5` | 215 | START | 215 | 358 |
| ✅ EXACT | `Action_ThrowPass` | QB | `13` | `13` | 291 | START | 291 | 299 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–304
- **Visible Samples:** 305

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_SnapReceive` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_None` | 205 | 290 | 86 | inferred_complete_timeline |
| `Action_ThrowPass` | 291 | 299 | 9 | inferred_complete_timeline |
| `Action_None` | 300 | 304 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 509 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–390
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_ClearToEdge` | 215 | 358 | 144 | inferred_complete_timeline |
| `Action_None` | 359 | 361 | 3 | inferred_complete_timeline |
| `Action_None` | 370 | 390 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_BreakInside` | 215 | 311 | 97 | inferred_complete_timeline |
| `Action_None` | 312 | 509 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 509 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 435 | 246 | inferred_complete_timeline |
| `Action_None` | 437 | 463 | 27 | inferred_complete_timeline |
| `Action_None` | 466 | 468 | 3 | inferred_complete_timeline |
| `Action_None` | 470 | 477 | 8 | inferred_complete_timeline |
| `Action_None` | 480 | 509 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 318 | 126 | inferred_complete_timeline |
| `Action_PassBlock` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–428
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 428 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_BallSnap` | 190 | 204 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 205 | 425 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–448
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 448 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–472
- **Visible Samples:** 473

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PassBlock` | 193 | 472 | 280 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 424 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–503
- **Visible Samples:** 504

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 503 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–507
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 507 | 318 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 463 | 274 | inferred_complete_timeline |
| `Action_None` | 466 | 467 | 2 | inferred_complete_timeline |
| `Action_None` | 475 | 482 | 8 | inferred_complete_timeline |
| `Action_None` | 484 | 509 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 340 | 151 | inferred_complete_timeline |
| `Action_None` | 342 | 509 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–409
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 393 | 204 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |
| `Action_None` | 408 | 409 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–407
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 301 | 112 | inferred_complete_timeline |
| `Action_None` | 304 | 313 | 10 | inferred_complete_timeline |
| `Action_None` | 315 | 363 | 49 | inferred_complete_timeline |
| `Action_None` | 365 | 403 | 39 | inferred_complete_timeline |
| `Action_None` | 405 | 407 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 502

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 349 | 160 | inferred_complete_timeline |
| `Action_None` | 353 | 369 | 17 | inferred_complete_timeline |
| `Action_None` | 375 | 509 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 509 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–412
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 400 | 211 | inferred_complete_timeline |
| `Action_None` | 406 | 412 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 493

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_None` | 190 | 463 | 274 | inferred_complete_timeline |
| `Action_None` | 466 | 476 | 11 | inferred_complete_timeline |
| `Action_None` | 480 | 481 | 2 | inferred_complete_timeline |
| `Action_None` | 486 | 487 | 2 | inferred_complete_timeline |
| `Action_None` | 496 | 509 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 259–267 | 5 | 2 | Undefined position; Undefined team |
| `24` | `43` | Position_Unknown | Team_Unknown | 305–379 | 4 | 2 | Undefined position; Undefined team |
| `25` | `45` | Position_Unknown | Team_Unknown | 315–482 | 168 | 1 | Undefined position; Undefined team |
| `26` | `48` | Position_Unknown | Team_Unknown | 324–404 | 81 | 1 | Undefined position; Undefined team |
| `27` | `53` | Position_Unknown | Team_Unknown | 354–361 | 4 | 2 | Undefined position; Undefined team |
| `28` | `56` | Position_Unknown | Team_Unknown | 411–508 | 76 | 8 | Undefined position; Undefined team |
| `29` | `60` | Position_Unknown | Team_Unknown | 457–459 | 3 | 1 | Undefined position; Undefined team |
| `30` | `61` | Position_Unknown | Team_Unknown | 490–509 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `12` (C): Annotated start 193 != Inferred start 205
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [190–204], lower_priority='Action_PassBlock' annotated_start=193, effective_Action_PassBlock_start=205.
- ⚠️ Action 'Action_None' range [190-424] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-503] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-507] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [324-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-390] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-301] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-313] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-363] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-403] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-349] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-369] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-463] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-467] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-482] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-400] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-412] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [205-425] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-509] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-463] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-476] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-481] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-509] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-340] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-509] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-428] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-472] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-435] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-463] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-477] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-509] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-393] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [193-448] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-482] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-404] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-447] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-452] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-460] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-472] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-480] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-497] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-508] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-459] for track '29' has 1 frames without a visible bounding box.
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

</details>