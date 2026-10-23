# Play-Annotation-Generator Annotation Review — OutsideZoneRead_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_1`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 419
- **Player Tracks:** 42
- **Ball Tracks:** 0
- **Action Segments:** 144
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_PressEdge` | WR3 | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `20` | `20` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 3 | START | 3 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 3 | START | 3 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 3 | START | 3 | 248 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `18` | `Group` | 3 | START | 3 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 3 | START | 3 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 3 | START | 3 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 3 | START | 3 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 3 | START | 3 | 193 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 3 | START | 3 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `11` | `11` | 194 | START | 194 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `19` | `19` | 194 | START | 194 | 197 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `21` | 194 | START | 194 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `5` | `5` | 194 | START | 194 | 203 |
| ✅ EXACT | `Action_PressEdge` | WR3 | `8` | `8` | 206 | START | 206 | 260 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `20` | `20` | 206 | START | 206 | 220 |
| ✅ EXACT | `Action_Handoff` | CB1 | `7` | `7` | 222 | START | 222 | 237 |

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
- **Visible Frames:** 3–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 205 | 203 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 206 | 220 | 15 | inferred_complete_timeline |
| `Action_None` | 221 | 419 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 3–258
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 248 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 258 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 368 | 366 | inferred_complete_timeline |
| `Action_PreSnap` | 371 | 377 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 380 | 410 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 419 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 205 | 203 | inferred_complete_timeline |
| `Action_PressEdge` | 206 | 260 | 55 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |
| `Action_None` | 279 | 282 | 4 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 391 | 104 | inferred_complete_timeline |
| `Action_None` | 393 | 407 | 15 | inferred_complete_timeline |
| `Action_None` | 409 | 419 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 3–198
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 198 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 3–284
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 193 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 216 | 238 | 23 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |
| `Action_None` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_None` | 274 | 284 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 3–242
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 193 | 191 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 203 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 227 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 238 | 9 | inferred_complete_timeline |
| `Action_None` | 239 | 242 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 3–196
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 94 | 92 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 193 | 74 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 196 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 3–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 101 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 103 | 193 | 91 | inferred_complete_timeline |
| `Action_ZoneBlock` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 215 | 238 | 24 | inferred_complete_timeline |
| `Action_None` | 239 | 419 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 3–257
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 242 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 257 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 3–306
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 242 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 306 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 110 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 195 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 199 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 248 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 257 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 273 | 275 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 325 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 419 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 90 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 99 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 195 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 218 | 419 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 3–419
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 257 | 255 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 389 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 3–328
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 281 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 316 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 328 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 3–335
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 221 | 219 | inferred_complete_timeline |
| `Action_Handoff` | 222 | 237 | 16 | inferred_complete_timeline |
| `Action_None` | 238 | 335 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 3–417
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 247 | 245 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 377 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 381 | 396 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 406 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 412 | 417 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 3–418
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 340 | 338 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 356 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 370 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 376 | 377 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 384 | 385 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 417 | 418 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 3–407
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 407 | 405 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 3–409
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 3 | 393 | 391 | inferred_complete_timeline |
| `Action_PreSnap` | 399 | 401 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 409 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 3–358 | 351 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 3–277 | 253 | 6 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 221–419 | 192 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 222–335 | 111 | 3 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 261–419 | 157 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 294–419 | 123 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 295–298 | 4 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 305–419 | 115 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 310–419 | 60 | 7 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 321–419 | 99 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 328–366 | 35 | 4 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 344–419 | 68 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 360–418 | 49 | 5 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 361–383 | 13 | 3 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 364–366 | 3 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 366–419 | 54 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 381–419 | 39 | 1 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 385–419 | 17 | 5 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 389–393 | 5 | 1 | Undefined position; Undefined team |
| `39` | `53` | Position_Unknown | Team_Unknown | 393–411 | 14 | 2 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 393–419 | 25 | 2 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 409–419 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 3: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 3: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [3-368] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [371-377] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-410] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-419] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-334] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [337-340] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-353] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-257] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-212] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-242] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-257] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-267] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-272] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-407] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-203] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-247] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-377] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [381-396] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-406] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-417] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-335] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-282] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-391] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-407] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-257] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-389] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-356] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-370] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-377] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-385] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [417-418] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-197] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [199-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [208-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [216-238] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-284] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-281] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-316] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-393] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-401] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-409] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-110] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-248] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-257] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-275] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-325] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-248] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-258] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-90] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-113] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [256-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-306] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-198] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-193] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-197] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [194-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-242] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-419] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-319] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-335] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-297] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [299-326] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-370] for track '25' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-377] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-298] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-338] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-383] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-395] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-405] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-419] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [328-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-355] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-362] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [365-366] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [344-379] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [388-419] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-362] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-365] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-391] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-399] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [405-418] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-363] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [376-383] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [364-366] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-393] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-403] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [407-410] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [418-419] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [389-393] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-404] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [410-411] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-396] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [399-419] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>