# Play-Annotation-Generator Annotation Review — Duo_3

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_3`
- **Frame Range:** 0 to 388 (389 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 388
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ComboBlock` | TE1 | offense | `7` | `7` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `11` | `11` |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 388 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 384 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 362 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 377 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 279 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 233 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `3` | `Group` | 0 | START | 0 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 235 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 229 |
| ✅ EXACT | `Action_ComboBlock` | RG | `14` | `14` | 236 | START | 236 | 264 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | RT | `21` | `21` | 236 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | TE1 | `7` | `7` | 236 | START | 236 | 305 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | C | `9` | `9` | 236 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `11` | `11` | 260 | START | 260 | 320 |
| ✅ EXACT | `Action_BlockSecondLevel` | RG | `14` | `14` | 265 | START | 265 | 305 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–377
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 377 | 378 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 320 | 61 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 333 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 337 | 388 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–384
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 384 | 385 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ComboBlock` | 236 | 305 | 70 | inferred_complete_timeline |
| `Action_None` | 306 | 315 | 10 | inferred_complete_timeline |
| `Action_None` | 320 | 371 | 52 | inferred_complete_timeline |
| `Action_None` | 373 | 388 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 323 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 363

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 362 | 363 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 279 | 280 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 388 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 235 | 236 | inferred_complete_timeline |
| `Action_ComboBlock` | 236 | 264 | 29 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 265 | 305 | 41 | inferred_complete_timeline |
| `Action_None` | 306 | 362 | 57 | inferred_complete_timeline |
| `Action_None` | 365 | 371 | 7 | inferred_complete_timeline |
| `Action_None` | 373 | 388 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 367 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 371 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 388 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 323 | 324 | inferred_complete_timeline |
| `Action_PreSnap` | 325 | 388 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |
| `Action_PreSnap` | 269 | 270 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 303 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 312 | 325 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 388 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 337 | 338 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 280 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 294 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 301 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 310 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 378 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 384 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 300 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 306 | 388 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 255 | 256 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 362 | 105 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 371 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 373 | 388 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 381 | 382 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–386
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 370 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 386 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 388 | 389 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 252–316 | 59 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 274–301 | 25 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 274–285 | 11 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 305–388 | 76 | 3 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 314–387 | 46 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 320–338 | 19 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 330–345 | 7 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 334–337 | 4 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 342–388 | 47 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 346–348 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 374–388 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `21` (RT)
- ❌ Missing segment for action `Action_ComboBlock` on target `9` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '9' has invalid range: start=236, end=229. Clamping end to start.
- ⚠️ Segment 'Action_ComboBlock' for track '21' has invalid range: start=236, end=233. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-384] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-388] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-388] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-381] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-362] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-371] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [236-305] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-315] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-371] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-370] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-386] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-367] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [323-333] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [337-388] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-303] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-325] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-362] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-371] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-337] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-294] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-301] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-310] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-378] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-384] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-291] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-300] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-388] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-362] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-377] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-279] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-308] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-316] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-281] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-289] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-301] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-285] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-332] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-371] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-320] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-387] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-338] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-333] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-345] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-337] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '31' has 1 frames without a visible bounding box.
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

</details>