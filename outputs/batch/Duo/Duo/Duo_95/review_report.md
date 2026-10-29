# Play-Annotation-Generator Annotation Review — Duo_95

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_95`
- **Frame Range:** 0 to 418 (419 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 418
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 130
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `0` | `Group` | 0 | START | 0 | 300 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 418 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | `17` | `17` | 18 | START | 18 | 77 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | C | `19` | `19` | 18 | START | 18 | 193 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | WR1 | `3` | `3` | 18 | START | 18 | 240 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `19` | `19` | 219 | START | 219 | 334 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `7` | `7` | 219 | START | 219 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 334 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 369 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 295 | 296 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 331 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 349 | 410 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 418 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ComboBlock` | 18 | 240 | 223 | inferred_complete_timeline |
| `Action_ComboBlock` | 243 | 334 | 92 | inferred_complete_timeline |
| `Action_None` | 335 | 418 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–409
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 300 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 302 | 409 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ComboBlock` | 18 | 77 | 60 | inferred_complete_timeline |
| `Action_ComboBlock` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_ComboBlock` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_ComboBlock` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 144 | 165 | 22 | inferred_complete_timeline |
| `Action_ComboBlock` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 208 | 240 | 33 | inferred_complete_timeline |
| `Action_ComboBlock` | 244 | 259 | 16 | inferred_complete_timeline |
| `Action_ComboBlock` | 261 | 330 | 70 | inferred_complete_timeline |
| `Action_None` | 335 | 347 | 13 | inferred_complete_timeline |
| `Action_None` | 350 | 418 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_ComboBlock` | 18 | 193 | 176 | inferred_complete_timeline |
| `Action_ComboBlock` | 196 | 218 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 219 | 334 | 116 | inferred_complete_timeline |
| `Action_None` | 335 | 388 | 54 | inferred_complete_timeline |
| `Action_None` | 402 | 418 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–418
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 86 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 141 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 161 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 237 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 357 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 418 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 73 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 141 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 218 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 219 | 233 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 236 | 237 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 254 | 283 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 286 | 288 | 3 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 292 | 333 | 42 | inferred_complete_timeline |
| `Action_None` | 335 | 359 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 169 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 240 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 287 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 290 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 295 | 418 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 161 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 169 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 280 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 282 | 340 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 343 | 418 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 129 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 161 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 237 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 259 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 295 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 300 | 418 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 45 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 49 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 73 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 121 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 129 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 237 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 259 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 295 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 392 | 393 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 405 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 418 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–380
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 372 | 373 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 376 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 402 | 403 | inferred_complete_timeline |
| `Action_PreSnap` | 406 | 418 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 410 | 411 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 418 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 418 | 419 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 381 | 382 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–418 | 418 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 57–418 | 264 | 8 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 323–418 | 89 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 354–358 | 5 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 358–407 | 49 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 389–418 | 16 | 3 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 400–418 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `17` (10 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (6 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 192: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '7' (RT) duration 116 frames exceeds threshold 90 frames [start=219, end=334].
- ⚠️ Validation warning: Action 'Action_BlockSecondLevel' for track '19' (C) duration 116 frames exceeds threshold 90 frames [start=219, end=334].
- ⚠️ Action 'Action_PreSnap' range [0-300] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-409] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-141] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-161] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-169] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-181] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-280] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-340] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-418] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [18-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-372] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-376] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-381] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-73] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-141] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [219-233] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [236-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [248-251] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [254-283] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [286-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [292-333] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-359] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-410] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-402] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-295] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-331] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-410] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-45] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-49] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-73] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-121] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-237] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-245] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-259] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-295] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-392] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-405] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-129] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-161] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-259] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-295] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-129] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-169] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-240] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-287] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-290] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [18-77] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [83-85] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [110-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [132-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [144-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [184-185] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [208-240] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [244-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [261-330] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-347] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-86] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-141] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-161] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-237] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-247] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-357] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [18-193] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [219-334] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-388] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-418] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-121] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-369] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-81] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-129] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-147] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-259] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-325] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-418] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-358] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-403] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-407] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-391] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-407] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-418] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-418] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>