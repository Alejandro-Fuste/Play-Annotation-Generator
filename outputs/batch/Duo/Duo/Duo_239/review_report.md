# Play-Annotation-Generator Annotation Review — Duo_239

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_239`
- **Frame Range:** 0 to 388 (389 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 388
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `4` | `4` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 324 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 351 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 0 | 131 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `12` | `12` | 275 | START | 275 | 331 |
| ✅ EXACT | `Action_ComboBlock` | QB | `15` | `15` | 275 | START | 275 | 340 |
| ✅ EXACT | `Action_ComboBlock` | RG | `4` | `4` | 275 | START | 275 | 300 |
| ✅ EXACT | `Action_ComboBlock` | LG | `9` | `9` | 275 | START | 275 | 340 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RG | `4` | `4` | 301 | START | 301 | 315 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 340 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–388
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 274 | 275 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 340 | 66 | inferred_complete_timeline |
| `Action_None` | 341 | 388 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 351 | 352 | inferred_complete_timeline |
| `Action_PreSnap` | 354 | 367 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 371 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 375 | 382 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 388 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 388 | 272 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 324 | 325 | inferred_complete_timeline |
| `Action_PreSnap` | 331 | 388 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–388
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 274 | 112 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 340 | 66 | inferred_complete_timeline |
| `Action_None` | 341 | 388 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 274 | 130 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 300 | 26 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 301 | 315 | 15 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 317 | 326 | 10 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 333 | 337 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 344 | 349 | 6 | inferred_complete_timeline |
| `Action_None` | 357 | 366 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–355
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 274 | 140 | inferred_complete_timeline |
| `Action_ComboBlock` | 275 | 331 | 57 | inferred_complete_timeline |
| `Action_ComboBlock` | 333 | 340 | 8 | inferred_complete_timeline |
| `Action_None` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_None` | 354 | 355 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 388 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 326 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 330 | 331 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 334 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 270 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 324 | 326 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 333 | 388 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 265 | 266 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 349 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 376 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 379 | 380 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 383 | 388 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 297 | 298 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 315 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 323 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 334 | 335 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 273 | 274 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 279 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 285 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 24 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 35 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 388 | 319 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 222 | 223 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–388
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 341 | 342 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 351 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 370 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 372 | 388 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `19` | `20` | Position_Unknown | Team_Unknown | 42–153 | 30 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 116–268 | 149 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 131–206 | 76 | 1 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 271–272 | 2 | 1 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 274–388 | 115 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 283–388 | 99 | 2 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 316–351 | 36 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 340–388 | 47 | 2 | Undefined position; Undefined team |
| `27` | `43` | Position_Unknown | Team_Unknown | 342–345 | 4 | 1 | Undefined position; Undefined team |
| `28` | `44` | Position_Unknown | Team_Unknown | 344–388 | 44 | 2 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 354–366 | 11 | 3 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 361–388 | 28 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 365–388 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 74 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-273] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-279] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-285] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-297] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-307] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-315] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-323] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-324] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-351] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-367] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-371] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-382] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [301-315] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [317-326] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [333-337] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [339-340] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-349] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-366] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-326] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-331] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-334] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-222] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-341] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-351] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-370] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-388] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-133] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [275-331] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [333-340] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-349] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-376] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-380] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-388] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-274] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-24] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-206] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-272] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [274-388] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-325] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [340-341] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-388] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-345] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-365] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-361] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-366] for track '29' has 1 frames without a visible bounding box.
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

</details>