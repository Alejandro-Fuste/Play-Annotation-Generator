# Play-Annotation-Generator Annotation Review — CrackToss_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_62`
- **Frame Range:** 0 to 399 (400 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 399
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 77
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | CB3 | defense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `17` | `16` |
| ✅ EXACT | `Action_Toss` | RB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `19` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 303 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 303 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 304 | START | 304 | 315 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `3` | `2` | 307 | START | 307 | 323 |
| ✅ EXACT | `Action_PullBlock` | CB3 | `2` | `1` | 307 | START | 307 | 364 |
| ✅ EXACT | `Action_SnapReceive` | RB | `17` | `16` | 315 | END | 304 | 315 |
| ✅ EXACT | `Action_Toss` | RB | `17` | `16` | 319 | START | 319 | 339 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `22` | `21` | 340 | START | 340 | 369 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 364 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 339 | 289 | inferred_complete_timeline |
| `Action_BallCarry` | 340 | 369 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 373 | 374 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_SnapReceive` | 304 | 315 | 12 | inferred_complete_timeline |
| `Action_None` | 316 | 318 | 3 | inferred_complete_timeline |
| `Action_Toss` | 319 | 339 | 21 | inferred_complete_timeline |
| `Action_None` | 340 | 383 | 44 | inferred_complete_timeline |
| `Action_None` | 387 | 395 | 9 | inferred_complete_timeline |
| `Action_None` | 398 | 399 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 388 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 399 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 367 | 64 | inferred_complete_timeline |
| `Action_None` | 373 | 376 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–392
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 376 | 73 | inferred_complete_timeline |
| `Action_None` | 378 | 379 | 2 | inferred_complete_timeline |
| `Action_None` | 391 | 392 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–398
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_BallSnap` | 304 | 315 | 12 | inferred_complete_timeline |
| `Action_None` | 316 | 378 | 63 | inferred_complete_timeline |
| `Action_None` | 384 | 385 | 2 | inferred_complete_timeline |
| `Action_None` | 389 | 398 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 315 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 379 | 76 | inferred_complete_timeline |
| `Action_None` | 388 | 395 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 322 | 19 | inferred_complete_timeline |
| `Action_None` | 325 | 379 | 55 | inferred_complete_timeline |
| `Action_None` | 388 | 395 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 328 | 25 | inferred_complete_timeline |
| `Action_None` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_None` | 342 | 379 | 38 | inferred_complete_timeline |
| `Action_None` | 383 | 385 | 3 | inferred_complete_timeline |
| `Action_None` | 388 | 394 | 7 | inferred_complete_timeline |
| `Action_None` | 396 | 397 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 381 | 78 | inferred_complete_timeline |
| `Action_None` | 383 | 399 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–386
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 356 | 53 | inferred_complete_timeline |
| `Action_None` | 358 | 372 | 15 | inferred_complete_timeline |
| `Action_None` | 375 | 379 | 5 | inferred_complete_timeline |
| `Action_None` | 384 | 386 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 347 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 379 | 76 | inferred_complete_timeline |
| `Action_None` | 383 | 384 | 2 | inferred_complete_timeline |
| `Action_None` | 388 | 399 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 399 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 306 | 307 | inferred_complete_timeline |
| `Action_PullBlock` | 307 | 364 | 58 | inferred_complete_timeline |
| `Action_None` | 365 | 399 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–399
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 303 | 304 | inferred_complete_timeline |
| `Action_None` | 304 | 399 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–399 | 398 | 4 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–399 | 399 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–395 | 391 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–385 | 382 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 319–399 | 9 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 344–396 | 40 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 350–351 | 2 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 351–399 | 45 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 393–399 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 57 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '24' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 399 as fallback play end.
- ⚠️ Action 'Action_CrackBlock' range [307-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [326-364] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-399] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-388] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-399] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-347] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-380] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-315] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-379] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-395] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-303] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-322] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-379] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-395] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-379] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-381] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-399] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-377] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-395] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-328] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-379] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-385] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-394] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-397] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-378] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-398] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-383] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-395] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-399] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-356] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-372] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-379] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-367] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-376] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-376] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-379] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-363] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-381] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-339] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [340-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [373-374] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-399] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-379] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-368] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-399] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>