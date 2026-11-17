# Play-Annotation-Generator Annotation Review — Power_138

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_138`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 42
- **Ball Tracks:** 2
- **Action Segments:** 97
- **Validation Warnings:** 144
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `18` |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `22` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 4 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 4 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 23 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 56 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 4 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 4 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 4 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 4 | 80 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `20` | `18` | 172 | START | 172 | 214 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `20` | `18` | 172 | START | 172 | 214 |
| ❌ MISSING SEGMENT | `Action_PullBlock` | Position_Unknown | `22` | `19` | 172 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 4–373
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 107 | 104 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 298 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 373 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–286
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 80 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 123 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 286 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 4–79
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 6 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 25 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 79 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 4–358
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 358 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 56–107
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 56 | 103 | 48 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 4–467
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 31 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 355 | 318 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 388 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 405 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 410 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 418 | 434 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 439 | 442 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 449 | 467 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 23–103
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 103 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 4–446
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 29 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 74 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 330 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 344 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 347 | 446 | 100 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 4–284
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 284 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 4–439
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 422 | 419 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 439 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 4–435
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 329 | 326 | inferred_complete_timeline |
| `Action_PreSnap` | 332 | 353 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 402 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 422 | 424 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 432 | 435 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 4–309
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 68 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 309 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 4–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 429 | 426 | inferred_complete_timeline |
| `Action_PreSnap` | 434 | 479 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–476
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 459 | 456 | inferred_complete_timeline |
| `Action_PreSnap` | 464 | 469 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 473 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 475 | 476 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 4–34 | 31 | 1 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 4–25 | 22 | 1 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 21–51 | 31 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 82–479 | 387 | 4 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 116–273 | 145 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 123–479 | 356 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 135–357 | 189 | 6 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 253–479 | 225 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 285–385 | 96 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 287–305 | 19 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 293–479 | 185 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 302–340 | 38 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 316–479 | 161 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 327–479 | 152 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 347–479 | 118 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 355–461 | 107 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 359–479 | 109 | 3 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 366–436 | 60 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 376–479 | 103 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 393–410 | 18 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 401–464 | 60 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 414–479 | 66 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 420–446 | 27 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 425–479 | 54 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 426–479 | 54 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 457–462 | 6 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 473–479 | 7 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 476–479 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | 72 | 216 | 62 | 42.8% | 73–113, 119–122, 125–127, 137–149, 177–198 |
| `22` | `26` | 184 | 265 | 23 | 28.0% | 189–226, 229, 231–232, 234–242, 256–264 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_PullBlock` on target `19` (Position_Unknown)

### Track Identity Issues

- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 86 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Deduplicated duplicate event 'Action_DownBlock' at frame 172 for track '18'.
- ⚠️ Action 'Action_PreSnap' range [4-284] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-459] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-469] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-473] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [475-476] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-68] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-309] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-29] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-74] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-330] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-446] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-358] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-373] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-329] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-353] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-402] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [422-424] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [432-435] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-429] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-286] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-422] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [424-439] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-25] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-31] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-388] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-405] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-410] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-434] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-442] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [449-467] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-6] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-25] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-51] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-171] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-427] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-138] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-464] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-285] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-321] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-344] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-347] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-351] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-387] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [390-479] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-364] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-385] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-305] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-299] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-479] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-309] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-340] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-349] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-331] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-479] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-386] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-414] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-461] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-387] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-401] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-479] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-385] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-400] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-411] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-436] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-410] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-427] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-446] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-464] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-446] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-433] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [457-462] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-479] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>