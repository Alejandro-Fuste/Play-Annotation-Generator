# Play-Annotation-Generator Annotation Review — Power_289

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_289`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 479
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ EXACT | `Action_DownBlock` | TE | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `3` | `3` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 23 | START | 23 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 23 | START | 23 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `11` | `Group` | 23 | START | 23 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `14` | `Group` | 23 | START | 23 | 332 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 23 | START | 23 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `17` | `Group` | 23 | START | 23 | 445 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 23 | START | 23 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 23 | START | 23 | 479 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 23 | START | 23 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 23 | START | 23 | 301 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 23 | START | 23 | 301 |
| ✅ EXACT | `Action_DownBlock` | TE | `1` | `1` | 302 | START | 302 | 350 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `18` | `18` | 302 | START | 302 | 306 |
| ✅ EXACT | `Action_DownBlock` | LT | `3` | `3` | 302 | START | 302 | 350 |
| ✅ EXACT | `Action_DownBlock` | C | `5` | `5` | 302 | START | 302 | 350 |
| ✅ EXACT | `Action_PullBlock` | RG | `10` | `10` | 302 | START | 302 | 350 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–374
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 374 | 352 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 332 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 479 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 301 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 350 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 414 | 64 | inferred_complete_timeline |
| `Action_None` | 432 | 479 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 301 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 350 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 477 | 127 | inferred_complete_timeline |
| `Action_None` | 479 | 479 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–323
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 301 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 306 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 322 | 323 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 301 | 279 | inferred_complete_timeline |
| `Action_DownBlock` | 302 | 350 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 479 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 23–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 301 | 279 | inferred_complete_timeline |
| `Action_PullBlock` | 302 | 350 | 49 | inferred_complete_timeline |
| `Action_None` | 351 | 376 | 26 | inferred_complete_timeline |
| `Action_None` | 381 | 479 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 23–445
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 445 | 423 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 23–345
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 338 | 316 | inferred_complete_timeline |
| `Action_PreSnap` | 340 | 345 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 453

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 78 | 56 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 331 | 252 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 420 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 479 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–472
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 387 | 365 | inferred_complete_timeline |
| `Action_PreSnap` | 390 | 448 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 457 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 459 | 472 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–333
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 333 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 433 | 411 | inferred_complete_timeline |
| `Action_PreSnap` | 435 | 442 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 444 | 447 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 455 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 459 | 461 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 466 | 479 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 23–462
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 372 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 462 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 479 | 457 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 364 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 425 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 467 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 469 | 479 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 23–479
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 398 | 376 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 414 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 420 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 445 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 451 | 457 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 461 | 479 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 330–479 | 143 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 377–479 | 103 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 393–398 | 6 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 397–479 | 83 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 411–424 | 12 | 2 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 437–479 | 43 | 1 | Undefined position; Undefined team |
| `28` | `29` | Position_Unknown | Team_Unknown | 455–469 | 11 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)

### Track Identity Issues

- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 51 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [23-479] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-414] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-477] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-350] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-479] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-372] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-462] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-433] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [435-442] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [444-447] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-455] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-461] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-331] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-420] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-479] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-338] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-345] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-376] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-479] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-364] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-425] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-467] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-333] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-332] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-387] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-448] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-457] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [459-472] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-445] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [302-306] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [319-320] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [322-323] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-398] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-414] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-420] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-445] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-457] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-374] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-370] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-398] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-424] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-479] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-462] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [467-469] for track '28' has 1 frames without a visible bounding box.
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

</details>