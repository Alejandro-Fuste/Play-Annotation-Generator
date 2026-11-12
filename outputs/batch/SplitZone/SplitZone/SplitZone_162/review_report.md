# Play-Annotation-Generator Annotation Review — SplitZone_162

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_162`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 509
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 8 | START | 9 | 280 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 8 | START | 9 | 280 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 8 | START | 9 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 8 | START | 9 | 280 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 8 | START | 9 | 280 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 8 | START | 9 | 277 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 8 | START | 9 | 280 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 8 | START | 9 | 277 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 278 | START | 278 | 288 |
| ✅ EXACT | `Action_SplitBlock` | TE | `0` | `0` | 281 | START | 281 | 316 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 281 | START | 281 | 322 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 281 | START | 289 | 325 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `4` | `4` | 281 | START | 281 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `5` | `5` | 281 | START | 281 | 304 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `7` | 281 | START | 281 | 332 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 288 | END | 278 | 288 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `8` | 316 | START | 316 | 492 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 384 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–497
- **Visible Samples:** 487

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_SnapReceive` | 278 | 288 | 11 | inferred_complete_timeline |
| `Action_None` | 289 | 315 | 27 | inferred_complete_timeline |
| `Action_BallCarry` | 316 | 492 | 177 | inferred_complete_timeline |
| `Action_BallCarry` | 495 | 497 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–325
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 313 | 36 | inferred_complete_timeline |
| `Action_None` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 325 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 9–316
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 280 | 272 | inferred_complete_timeline |
| `Action_SplitBlock` | 281 | 316 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 280 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 293 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 297 | 359 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–351
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 280 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 304 | 24 | inferred_complete_timeline |
| `Action_ZoneBlock` | 306 | 330 | 25 | inferred_complete_timeline |
| `Action_ZoneBlock` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 9–424
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_BallSnap` | 278 | 288 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 289 | 325 | 37 | inferred_complete_timeline |
| `Action_ZoneBlock` | 328 | 372 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 374 | 384 | 11 | inferred_complete_timeline |
| `Action_None` | 385 | 424 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 280 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 322 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 324 | 384 | 61 | inferred_complete_timeline |
| `Action_None` | 385 | 509 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–332
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 280 | 272 | inferred_complete_timeline |
| `Action_ZoneBlock` | 281 | 332 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–354
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |
| `Action_None` | 305 | 354 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–279
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 189 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 224 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 247 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 277 | 19 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 9–506
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 231 | 223 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 277 | 44 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |
| `Action_None` | 322 | 506 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 9–310
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 310 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–354
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 294 | 17 | inferred_complete_timeline |
| `Action_None` | 298 | 354 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 344 | 67 | inferred_complete_timeline |
| `Action_None` | 347 | 509 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–38
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 38 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 277 | 269 | inferred_complete_timeline |
| `Action_None` | 278 | 398 | 121 | inferred_complete_timeline |
| `Action_None` | 400 | 408 | 9 | inferred_complete_timeline |
| `Action_None` | 410 | 442 | 33 | inferred_complete_timeline |
| `Action_None` | 447 | 509 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 91–100 | 9 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 133–509 | 284 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 209–264 | 13 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 305–315 | 9 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 320–356 | 37 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 342–369 | 28 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 356–509 | 146 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 366–509 | 144 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 371–509 | 115 | 4 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 374–390 | 17 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 389–447 | 34 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 392–414 | 23 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 392–465 | 69 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 396–509 | 109 | 4 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 399–400 | 2 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 405–509 | 102 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 420–509 | 83 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 422–509 | 83 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 424–507 | 71 | 4 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 438–509 | 69 | 2 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 442–450 | 9 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 447–509 | 63 | 1 | Undefined position; Undefined team |
| `38` | `43` | Position_Unknown | Team_Unknown | 453–509 | 57 | 1 | Undefined position; Undefined team |
| `39` | `44` | Position_Unknown | Team_Unknown | 506–509 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (RG) duration 104 frames exceeds threshold 90 frames [start=281, end=384].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (C) duration 104 frames exceeds threshold 90 frames [start=281, end=384].
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [278–288], lower_priority='Action_ZoneBlock' annotated_start=281, effective_Action_ZoneBlock_start=289.
- ⚠️ Action 'Action_SplitBlock' range [281-316] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-398] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-408] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-442] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-344] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-310] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [297-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-304] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [306-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [350-351] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-313] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-332] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [316-492] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [495-497] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-38] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-277] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-354] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-247] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-277] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-294] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [281-322] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [289-325] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [328-372] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-424] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-231] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-506] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-97] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-509] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-264] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-356] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-369] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-500] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-442] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-475] for track '24' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-390] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-417] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-447] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-414] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-449] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-465] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-405] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-411] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-507] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-400] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-509] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-486] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-466] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-465] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-507] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-443] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-450] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-507] for track '39' has 1 frames without a visible bounding box.
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

</details>