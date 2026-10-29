# Play-Annotation-Generator Annotation Review — Duo_198

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_198`
- **Frame Range:** 0 to 374 (375 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 374
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 93
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_ComboBlock` | SAF | defense | `21` | `21` |
| ⚠️ START CHANGED | `Action_ComboBlock` | LG | offense | `25` | `22` |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | WR1 | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 85 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `16` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `20` | `Group` | 0 | START | 96 | 295 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `25` | `Group` | 0 | START | 139 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 76 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 53 |
| ✅ EXACT | `Action_ComboBlock` | C | `10` | `10` | 279 | START | 279 | 327 |
| ✅ EXACT | `Action_ComboBlock` | SAF | `21` | `21` | 279 | START | 279 | 327 |
| ⚠️ START CHANGED | `Action_ComboBlock` | LG | `25` | `22` | 279 | START | 308 | 309 |
| ⚠️ START CHANGED | `Action_BlockSecondLevel` | WR1 | `20` | `20` | 299 | START | 300 | 327 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 327 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–374
- **Visible Samples:** 374

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 374 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 316 | 258 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 365 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 374 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 96–374
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 96 | 295 | 200 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 300 | 327 | 28 | inferred_complete_timeline |
| `Action_None` | 328 | 370 | 43 | inferred_complete_timeline |
| `Action_None` | 372 | 374 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 93 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 215 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 228 | 54 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 284 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 305 | 350 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 353 | 358 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 345 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 355 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 359 | 371 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 374 | 374 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `25`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 139–309
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 139 | 275 | 137 | inferred_complete_timeline |
| `Action_ComboBlock` | 308 | 309 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 85 | 86 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 97 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 278 | 177 | inferred_complete_timeline |
| `Action_ComboBlock` | 279 | 327 | 49 | inferred_complete_timeline |
| `Action_None` | 328 | 355 | 28 | inferred_complete_timeline |
| `Action_None` | 358 | 374 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–339
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 76 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 92 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 334 | 239 | inferred_complete_timeline |
| `Action_PreSnap` | 336 | 339 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–374
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 337 | 270 | inferred_complete_timeline |
| `Action_PreSnap` | 339 | 345 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 374 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 374 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 47 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 374 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 82 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 307 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 325 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 330 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 339 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 351 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 361 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 374 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 81 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 336 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 363 | 365 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 374 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–332
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 91 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 332 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 319 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 328 | 374 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 102–374
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 102 | 278 | 177 | inferred_complete_timeline |
| `Action_ComboBlock` | 279 | 327 | 49 | inferred_complete_timeline |
| `Action_None` | 328 | 374 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–374 | 374 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–116 | 116 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–76 | 76 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–45 | 46 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 35–54 | 17 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 218–279 | 62 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 283–289 | 7 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 286–374 | 89 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 301–336 | 23 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 343–360 | 18 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 353–369 | 14 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 362–374 | 13 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 369–374 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `26` | 165 | 170 | 6 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ComboBlock` for actor_track_id `25` (LG): Annotated start 279 != Inferred start 308
- ⚠️ `Action_BlockSecondLevel` for actor_track_id `20` (WR1): Annotated start 299 != Inferred start 300

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF` position mapped to `defense` team
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

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 374 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-345] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-371] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-81] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-336] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [363-365] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-319] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-332] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-92] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-334] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [336-339] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-316] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-365] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-374] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-116] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-97] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-355] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-228] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-284] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [305-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-358] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-76] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-337] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-345] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-374] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-93] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-82] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-121] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-307] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-325] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-339] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-351] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-361] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-275] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [308-309] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-279] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-289] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-318] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-336] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [343-360] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [353-355] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [359-369] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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