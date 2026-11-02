# Play-Annotation-Generator Annotation Review — JetSweep_212

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_212`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 629
- **Player Tracks:** 50
- **Ball Tracks:** 0
- **Action Segments:** 129
- **Validation Warnings:** 178
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `0` | `0` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_LeadBlock` | RB | offense | `9` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 2 | START | 2 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 2 | START | 2 | 42 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 2 | START | 2 | 93 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 2 | START | 2 | 119 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 2 | START | 2 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 2 | START | 2 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 2 | START | 2 | 241 |
| ✅ EXACT | `Action_JetMotion` | Position_Unknown | `15` | `15` | 212 | START | 212 | 239 |
| ✅ EXACT | `Action_BallSnap` | C | `0` | `0` | 213 | START | 213 | 227 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `0` | `0` | 216 | START | 228 | 275 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 216 | START | 216 | 275 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 216 | START | 216 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `8` | `8` | 216 | START | 216 | 243 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 227 | END | 213 | 227 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `14` | 231 | START | 231 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `15` | `15` | 242 | START | 242 | 402 |
| ✅ EXACT | `Action_LeadBlock` | RB | `9` | `9` | 242 | START | 242 | 275 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 275 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 2–275
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 42 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 212 | 169 | inferred_complete_timeline |
| `Action_SnapReceive` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_None` | 228 | 230 | 3 | inferred_complete_timeline |
| `Action_Toss` | 231 | 241 | 11 | inferred_complete_timeline |
| `Action_None` | 242 | 275 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–629
- **Visible Samples:** 619

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 241 | 240 | inferred_complete_timeline |
| `Action_LeadBlock` | 242 | 275 | 34 | inferred_complete_timeline |
| `Action_None` | 276 | 385 | 110 | inferred_complete_timeline |
| `Action_None` | 388 | 534 | 147 | inferred_complete_timeline |
| `Action_None` | 537 | 539 | 3 | inferred_complete_timeline |
| `Action_None` | 541 | 600 | 60 | inferred_complete_timeline |
| `Action_None` | 605 | 629 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–277
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 244 | 32 | inferred_complete_timeline |
| `Action_None` | 246 | 277 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 2–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 119 | 118 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 215 | 95 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 259 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 261 | 266 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 2–501
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_BallSnap` | 213 | 227 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 228 | 275 | 48 | inferred_complete_timeline |
| `Action_None` | 276 | 501 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 2–296
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 215 | 214 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 243 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 246 | 275 | 30 | inferred_complete_timeline |
| `Action_None` | 276 | 296 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 2–284
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 93 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 215 | 120 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 275 | 60 | inferred_complete_timeline |
| `Action_None` | 276 | 284 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–469
- **Visible Samples:** 468

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 469 | 257 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 2–290
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 173 | 172 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 212 | 36 | inferred_complete_timeline |
| `Action_None` | 213 | 218 | 6 | inferred_complete_timeline |
| `Action_None` | 224 | 259 | 36 | inferred_complete_timeline |
| `Action_None` | 261 | 290 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 2–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 226 | 14 | inferred_complete_timeline |
| `Action_None` | 229 | 437 | 209 | inferred_complete_timeline |
| `Action_None` | 439 | 629 | 191 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 2–229
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 229 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–490
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 490 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 2–283
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 283 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 2–629
- **Visible Samples:** 605

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 212 | 211 | inferred_complete_timeline |
| `Action_None` | 213 | 355 | 143 | inferred_complete_timeline |
| `Action_None` | 367 | 495 | 129 | inferred_complete_timeline |
| `Action_None` | 501 | 518 | 18 | inferred_complete_timeline |
| `Action_None` | 520 | 542 | 23 | inferred_complete_timeline |
| `Action_None` | 545 | 546 | 2 | inferred_complete_timeline |
| `Action_None` | 551 | 629 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 2–260 | 257 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 212–629 | 413 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 267–293 | 27 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 279–305 | 27 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 291–564 | 265 | 5 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 305–367 | 63 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 310–464 | 155 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 311–384 | 72 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 317–512 | 182 | 8 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 317–486 | 170 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 349–351 | 3 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 362–414 | 19 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 363–364 | 2 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 387–396 | 10 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 390–613 | 202 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 403–629 | 212 | 3 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 425–483 | 54 | 3 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 429–605 | 171 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 429–441 | 10 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 431–438 | 8 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 433–554 | 97 | 2 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 440–493 | 53 | 2 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 442–605 | 159 | 3 | Undefined position; Undefined team |
| `37` | `55` | Position_Unknown | Team_Unknown | 445–500 | 56 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 454–610 | 157 | 1 | Undefined position; Undefined team |
| `39` | `58` | Position_Unknown | Team_Unknown | 460–620 | 154 | 4 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 468–629 | 162 | 1 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 489–595 | 107 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 527–579 | 53 | 1 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 594–629 | 36 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 602–629 | 26 | 3 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 611–612 | 2 | 1 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 614–629 | 16 | 1 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 619–623 | 5 | 1 | Undefined position; Undefined team |
| `48` | `74` | Position_Unknown | Team_Unknown | 619–629 | 11 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 625–628 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `0` (C): Annotated start 216 != Inferred start 228
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 103 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 426: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [213–227], lower_priority='Action_ZoneBlock' annotated_start=216, effective_Action_ZoneBlock_start=228.
- ⚠️ Action 'Action_ZoneBlock' range [228-275] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-501] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-251] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-260] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-93] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-284] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-490] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-119] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-259] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [261-266] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-283] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-212] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-244] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-469] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-243] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-385] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-534] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-539] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-600] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-226] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-437] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-629] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-218] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-355] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-495] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-518] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-542] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-42] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [212-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [242-402] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-293] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-305] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-472] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-491] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-564] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-367] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-464] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-378] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-396] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-415] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-486] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-501] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-504] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-486] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-414] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-364] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-396] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-520] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-531] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-576] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-613] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-506] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-529] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-443] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-483] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-443] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-605] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-434] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-438] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-456] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-554] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-472] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-493] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-453] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-497] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-605] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-500] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-610] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-505] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-534] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-547] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-620] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-595] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-579] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-604] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-620] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [622-629] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [611-612] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-623] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [619-629] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [625-628] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>