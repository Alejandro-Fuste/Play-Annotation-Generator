# Play-Annotation-Generator Annotation Review — Power_363

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_363`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 52
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `13` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `15` | `15` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `21` | `21` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 20 | START | 20 | 437 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 20 | START | 20 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 20 | START | 20 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 20 | START | 20 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 20 | START | 20 | 332 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 20 | START | 20 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 20 | START | 28 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 20 | START | 20 | 442 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 20 | START | 20 | 310 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 20 | START | 20 | 449 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 20 | START | 20 | 420 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `13` | 311 | START | 311 | 378 |
| ✅ EXACT | `Action_DownBlock` | C | `15` | `15` | 311 | START | 311 | 378 |
| ✅ EXACT | `Action_DownBlock` | LG | `21` | `21` | 311 | START | 311 | 323 |
| ✅ EXACT | `Action_PullBlock` | RG | `6` | `6` | 311 | START | 311 | 378 |

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
- **Visible Frames:** 20–435
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 74 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 426 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 428 | 435 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 449 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 20–420
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 420 | 401 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 449 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–437
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 437 | 418 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 20–442
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 442 | 423 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 310 | 291 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 378 | 68 | inferred_complete_timeline |
| `Action_None` | 379 | 449 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 28–323
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 310 | 283 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 323 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 310 | 291 | inferred_complete_timeline |
| `Action_DownBlock` | 311 | 378 | 68 | inferred_complete_timeline |
| `Action_None` | 379 | 449 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 310 | 291 | inferred_complete_timeline |
| `Action_PullBlock` | 311 | 378 | 68 | inferred_complete_timeline |
| `Action_None` | 379 | 449 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 20–332
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 332 | 313 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 422 | 403 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 428 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 449 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 20–335
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 312 | 293 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 323 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 335 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–363
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 363 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 391 | 372 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 449 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–418
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 418 | 399 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 424

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 318 | 299 | inferred_complete_timeline |
| `Action_PreSnap` | 320 | 323 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 443 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 385 | 366 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 419 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 449 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 449 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 449 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–441
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 441 | 422 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–449
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 449 | 430 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 331–443 | 113 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 337–346 | 9 | 2 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 344–449 | 95 | 4 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 360–449 | 84 | 2 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 376–449 | 74 | 1 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 436–448 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 35 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [20-437] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-422] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-428] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-332] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-449] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-442] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-420] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-418] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-363] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-441] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-426] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-435] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-391] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-385] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-419] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-312] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-323] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-335] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-318] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-323] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-443] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-310] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [311-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-443] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-342] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-346] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-350] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-375] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-449] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-448] for track '27' has 1 frames without a visible bounding box.
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

</details>