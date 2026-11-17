# Play-Annotation-Generator Annotation Review — Power_149

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_149`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PullBlock` | RT | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 22 | START | 22 | 343 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 22 | START | 22 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 22 | START | 22 | 443 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `17` | `Group` | 22 | START | 22 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 22 | START | 22 | 305 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 22 | START | 22 | 305 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 22 | START | 22 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 22 | START | 22 | 357 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 22 | START | 22 | 352 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `11` | `11` | 306 | START | 306 | 368 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `20` | `20` | 306 | START | 306 | 329 |
| ✅ EXACT | `Action_PullBlock` | RT | `19` | `19` | 306 | START | 306 | 380 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 22–421
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 95 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 129 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 421 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 247 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 384 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 449 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 22–443
- **Visible Samples:** 422

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 443 | 422 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 343 | 322 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 383 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 395 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 411 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 449 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 22–394
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 317 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 326 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 388 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 393 | 394 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 22–430
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 352 | 331 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 430 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 357 | 336 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 449 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 305 | 284 | inferred_complete_timeline |
| `Action_DownBlock` | 306 | 329 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 332 | 333 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 335 | 380 | 46 | inferred_complete_timeline |
| `Action_None` | 381 | 449 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 305 | 284 | inferred_complete_timeline |
| `Action_PullBlock` | 306 | 380 | 75 | inferred_complete_timeline |
| `Action_None` | 381 | 449 | 69 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 22–368
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 305 | 284 | inferred_complete_timeline |
| `Action_DownBlock` | 306 | 368 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 22–322
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 322 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 22–448
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 365 | 344 | inferred_complete_timeline |
| `Action_PreSnap` | 368 | 448 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 22–448
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 437 | 416 | inferred_complete_timeline |
| `Action_PreSnap` | 447 | 448 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 22–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 449 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 22–435
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 435 | 414 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 22–449 | 401 | 4 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 22–449 | 428 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 116–449 | 242 | 10 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 353–449 | 94 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 379–449 | 71 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 408–449 | 39 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 438–441 | 4 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 442–445 | 4 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 444–449 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 300: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 300: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [22-323] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-364] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-449] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-449] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-384] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-322] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-435] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-430] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-343] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-383] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-395] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-411] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [306-368] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-129] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-421] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-443] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-317] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-326] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-388] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-394] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-437] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [306-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [332-333] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [335-380] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-449] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-365] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-448] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-196] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-345] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-367] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-389] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-446] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-435] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-433] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [438-441] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [442-445] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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