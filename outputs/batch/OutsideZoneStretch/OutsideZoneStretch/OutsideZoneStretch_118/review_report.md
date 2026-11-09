# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_118`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 36
- **Ball Tracks:** 1
- **Action Segments:** 118
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 102
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | Team_Unknown | `21` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 251 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `15` | `Group` | 0 | START | 0 | 345 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 229 | START | 229 | 251 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `12` | `12` | 229 | START | 229 | 239 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `5` | `5` | 229 | START | 229 | 281 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `7` | 229 | START | 229 | 281 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 229 | START | 229 | 239 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | Position_Unknown | `21` | `19` | 239 | START | 258 | 274 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 255 | START | 255 | 266 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 254 | 202 | inferred_complete_timeline |
| `Action_Handoff` | 255 | 266 | 12 | inferred_complete_timeline |
| `Action_None` | 267 | 539 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 251 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–345
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 345 | 346 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 469

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 239 | 11 | inferred_complete_timeline |
| `Action_None` | 310 | 533 | 224 | inferred_complete_timeline |
| `Action_None` | 535 | 539 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 530

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 281 | 53 | inferred_complete_timeline |
| `Action_None` | 282 | 295 | 14 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 308 | 539 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 251 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 257 | 281 | 25 | inferred_complete_timeline |
| `Action_None` | 282 | 296 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 239 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 241 | 281 | 41 | inferred_complete_timeline |
| `Action_None` | 282 | 539 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_ZoneBlock` | 229 | 281 | 53 | inferred_complete_timeline |
| `Action_None` | 282 | 539 | 258 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 520

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 165 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 226 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 343 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 345 | 380 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 386 | 497 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 499 | 539 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–466
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 54 | 259 | 206 | inferred_complete_timeline |
| `Action_PreSnap` | 327 | 451 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 454 | 456 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 465 | 466 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–327
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 327 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 524

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 349 | 350 | inferred_complete_timeline |
| `Action_PreSnap` | 361 | 362 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 365 | 379 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 530 | 150 | inferred_complete_timeline |
| `Action_PreSnap` | 533 | 539 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–515
- **Visible Samples:** 497

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 300 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 503 | 190 | inferred_complete_timeline |
| `Action_PreSnap` | 507 | 515 | 9 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–539 | 539 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 64–525 | 383 | 8 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 181–255 | 75 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 258–539 | 261 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 260–500 | 235 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 263–534 | 139 | 8 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 284–326 | 43 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 285–351 | 63 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 295–305 | 11 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 295–539 | 235 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 319–539 | 219 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 327–525 | 187 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 330–539 | 206 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 337–504 | 166 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 352–539 | 178 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 356–539 | 183 | 2 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 395–539 | 142 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 453–539 | 70 | 6 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 477–539 | 63 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 481–489 | 9 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 514–520 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | 146 | 169 | 8 | 33.3% | 152–155, 157–168 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PressEdge` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 238: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-300] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-503] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-515] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-349] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-379] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-530] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-165] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-226] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-380] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-497] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-327] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-533] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-451] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [454-456] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [465-466] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [257-281] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-296] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [229-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-265] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-345] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-342] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [345-362] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-369] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-386] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-398] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-409] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-525] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-255] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [258-274] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-453] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-462] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-525] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-531] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-264] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [269-359] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [362-500] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-273] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-343] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-416] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-420] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-429] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-459] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-472] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [532-534] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-326] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-351] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-373] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-378] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-384] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-331] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-424] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-330] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-344] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-525] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-339] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-504] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [352-371] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-400] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [404-438] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-364] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-539] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [395-423] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-539] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [453-454] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-459] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [461-463] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-476] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-529] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [531-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-489] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [514-515] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-520] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>