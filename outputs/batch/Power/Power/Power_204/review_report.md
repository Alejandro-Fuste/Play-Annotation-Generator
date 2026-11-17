# Play-Annotation-Generator Annotation Review — Power_204

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_204`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Touchdown`
- **Result Frame:** 569
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 147
- **Validation Warnings:** 223
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 0
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `26` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `31` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `34` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `26` | `22` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 4 | START | 4 | 374 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 4 | START | 4 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 4 | START | 4 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `21` | `Group` | 4 | START | 122 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `26` | `Group` | 4 | START | 164 | 297 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 4 | START | 4 | 133 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `31` | `26` | 298 | START | 298 | 317 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `34` | `29` | 298 | START | 298 | 323 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `26` | `22` | 298 | START | 298 | 308 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 4–316
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 150 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 316 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `21`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 122–569
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 122 | 123 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 151 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 183 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 194 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 211 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 281 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 283 | 366 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 377 | 455 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 463 | 469 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 482 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 484 | 488 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 491 | 494 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 497 | 569 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 4–452
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 169 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 323 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 392 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 396 | 452 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 4–316
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 133 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 159 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 316 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 4–381
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 374 | 371 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 381 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `26`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `26`
- **team_side:** `offense`
- **Visible Frames:** 164–402
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 164 | 297 | 134 | inferred_complete_timeline |
| `Action_PullBlock` | 298 | 308 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 320 | 346 | 27 | inferred_complete_timeline |
| `Action_PullBlock` | 351 | 354 | 4 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 358 | 362 | 5 | inferred_complete_timeline |
| `Action_None` | 371 | 402 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 4–386
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 173 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 292 | 109 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 386 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 4–447
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 146 | 143 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 192 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 198 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 200 | 223 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 280 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 286 | 320 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 447 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 4–417
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 417 | 414 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 4–318
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 4 | 318 | 315 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 4–267 | 176 | 4 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 4–172 | 166 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 4–509 | 506 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 4–149 | 101 | 4 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 6–168 | 144 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 9–17 | 9 | 1 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 15–390 | 376 | 1 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 32–251 | 220 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 39–125 | 13 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 97–106 | 9 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 108–138 | 31 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 136–278 | 65 | 9 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 146–209 | 11 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 169–380 | 112 | 8 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 177–224 | 47 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 178–183 | 6 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 274–378 | 89 | 9 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 284–317 | 34 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 291–404 | 82 | 5 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 296–329 | 33 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 322–569 | 233 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 336–398 | 62 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 339–347 | 9 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 355–473 | 109 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 365–453 | 76 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 369–479 | 111 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 372–569 | 182 | 4 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 374–379 | 6 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 375–406 | 28 | 4 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 386–457 | 54 | 2 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 398–399 | 2 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 408–411 | 4 | 1 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 412–569 | 158 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 415–417 | 3 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 418–495 | 78 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 450–569 | 117 | 2 | Undefined position; Undefined team |
| `46` | `63` | Position_Unknown | Team_Unknown | 464–569 | 93 | 2 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 489–569 | 81 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 515–569 | 55 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 528–569 | 42 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 541–569 | 29 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 560–569 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `31` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `34` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `26` (3 segments found)

### Track Identity Issues

- ⚠️ 42 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 42 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 84 |
| Missing visible bounding boxes during action | 136 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 410: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 410: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [4-374] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-386] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-169] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-323] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-392] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-452] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-417] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-192] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-223] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-280] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-320] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-447] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-173] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-156] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-133] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-159] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-316] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-509] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-79] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-125] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-316] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-10] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-168] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-390] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-125] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-151] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-194] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-211] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-281] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-366] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-455] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-469] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-482] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-488] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [491-494] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-176] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-234] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-259] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-278] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-149] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-209] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [298-308] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [320-346] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [351-354] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-171] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-232] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-240] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-321] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-334] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-341] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-376] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-221] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-224] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-183] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [298-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [323-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [330-335] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [337-354] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-369] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-317] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-295] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-391] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-398] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-404] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [298-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [325-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-351] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-521] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-342] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-398] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-347] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-452] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-473] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-404] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-453] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-479] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-417] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-434] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [437-454] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [374-379] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-395] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-398] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-402] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-406] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-433] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [452-457] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-399] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-411] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-569] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [415-417] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-495] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-453] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [464-477] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-569] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-569] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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

</details>