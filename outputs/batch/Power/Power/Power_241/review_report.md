# Play-Annotation-Generator Annotation Review — Power_241

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_241`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 569
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_DownBlock` | WR1 | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `23` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 10 | START | 10 | 551 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 10 | START | 10 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 10 | START | 10 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 10 | START | 10 | 376 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 10 | START | 10 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 10 | START | 10 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `3` | `Group` | 10 | START | 10 | 569 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 10 | START | 10 | 379 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 10 | START | 10 | 569 |
| ✅ EXACT | `Action_DownBlock` | WR1 | `1` | `1` | 371 | START | 371 | 404 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `20` | `20` | 371 | START | 371 | 379 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `21` | `21` | 371 | START | 371 | 381 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `23` | `22` | 371 | START | 371 | 404 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 569 | 560 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–543
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 379 | 370 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 543 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 370 | 361 | inferred_complete_timeline |
| `Action_DownBlock` | 371 | 404 | 34 | inferred_complete_timeline |
| `Action_None` | 405 | 569 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 551 | 542 | inferred_complete_timeline |
| `Action_PreSnap` | 553 | 569 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 569 | 560 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–482
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 376 | 367 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 472 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 478 | 482 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–370
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 43 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 203 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 370 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 45 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 139 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 370 | 226 | inferred_complete_timeline |
| `Action_DownBlock` | 371 | 379 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 381 | 404 | 24 | inferred_complete_timeline |
| `Action_None` | 405 | 415 | 11 | inferred_complete_timeline |
| `Action_None` | 417 | 569 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 10–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 45 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 499 | 450 | inferred_complete_timeline |
| `Action_PreSnap` | 502 | 569 | 68 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–396
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 33 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 152 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 159 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 224 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 375 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 396 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 391 | 382 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 395 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 402 | 569 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 533

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 367 | 358 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 414 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 419 | 452 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 458 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 466 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 470 | 503 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 510 | 512 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 517 | 569 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 378 | 369 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 461 | 81 | inferred_complete_timeline |
| `Action_PreSnap` | 475 | 569 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 482 | 473 | inferred_complete_timeline |
| `Action_PreSnap` | 488 | 512 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 514 | 569 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 493 | 484 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 498 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 515 | 569 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 569 | 560 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 499 | 490 | inferred_complete_timeline |
| `Action_PreSnap` | 505 | 507 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 521 | 526 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 528 | 569 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 569 | 560 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `8` | Position_Unknown | Team_Unknown | 10–25 | 16 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 10–569 | 560 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 10–569 | 538 | 6 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 147–569 | 212 | 9 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 368–569 | 202 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 376–569 | 178 | 6 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 428–429 | 2 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 442–443 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 452–569 | 118 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 466–569 | 104 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 557–569 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 67 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [10-551] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-499] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [505-507] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [521-526] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-379] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-543] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-569] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-25] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-45] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-499] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-376] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-472] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [478-482] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-378] for track '12' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-461] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-493] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [497-498] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-569] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-482] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [488-512] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-391] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-395] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-414] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-452] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-458] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-466] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [470-503] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [510-512] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-41] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-152] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-375] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-396] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-451] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [455-457] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-469] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [471-569] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-43] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-203] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-370] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-45] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [371-379] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-415] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-314] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [371-381] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-498] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-507] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-459] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-512] for track '23' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [517-522] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [525-526] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [533-569] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-429] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-443] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [466-569] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>