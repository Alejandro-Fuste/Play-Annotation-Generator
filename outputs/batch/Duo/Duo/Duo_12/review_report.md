# Play-Annotation-Generator Annotation Review — Duo_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_12`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 31
- **Ball Tracks:** 1
- **Action Segments:** 72
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 49
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | offense | `12` | `12` |
| ✅ EXACT | `Action_ComboBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | offense | `2` | `2` |
| ✅ EXACT | `Action_ComboBlock` | DE1 | defense | `8` | `8` |
| ✅ EXACT | `Action_BlockSecondLevel` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | defense | `0` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 253 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 275 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 358 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `17` | `Group` | 0 | START | 0 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `18` | `Group` | 0 | START | 0 | 313 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 358 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LT | `12` | `12` | 247 | START | 247 | 250 |
| ✅ EXACT | `Action_ComboBlock` | C | `14` | `14` | 247 | START | 247 | 259 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | LG | `2` | `2` | 247 | START | 247 | 279 |
| ✅ EXACT | `Action_ComboBlock` | DE1 | `8` | `8` | 247 | START | 247 | 305 |
| ✅ EXACT | `Action_BlockSecondLevel` | C | `14` | `14` | 260 | START | 260 | 305 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | LB2 | `0` | `0` | 270 | START | 270 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 305 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 275 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 310 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 315 | 318 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 338 | 342 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 170 | 71 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 286 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 297 | 358 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 356 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 313 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ComboBlock` | 247 | 250 | 4 | inferred_complete_timeline |
| `Action_ComboBlock` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_ComboBlock` | 256 | 300 | 45 | inferred_complete_timeline |
| `Action_None` | 307 | 312 | 6 | inferred_complete_timeline |
| `Action_None` | 316 | 323 | 8 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 358 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ComboBlock` | 247 | 279 | 33 | inferred_complete_timeline |
| `Action_ComboBlock` | 281 | 305 | 25 | inferred_complete_timeline |
| `Action_None` | 306 | 336 | 31 | inferred_complete_timeline |
| `Action_None` | 338 | 342 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 246 | 247 | inferred_complete_timeline |
| `Action_ComboBlock` | 247 | 259 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 260 | 305 | 46 | inferred_complete_timeline |
| `Action_None` | 306 | 358 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 246 | 62 | inferred_complete_timeline |
| `Action_ComboBlock` | 247 | 305 | 59 | inferred_complete_timeline |
| `Action_None` | 306 | 334 | 29 | inferred_complete_timeline |
| `Action_None` | 336 | 358 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 173 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 301 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 304 | 328 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PreSnap` | 322 | 332 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 336 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–308
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |
| `Action_BallCarry` | 270 | 302 | 33 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 308 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 319 | 320 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 158 | 186 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 337 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 341 | 354 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 356 | 358 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 358 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `25` | Position_Unknown | Team_Unknown | 164–300 | 137 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 186–192 | 7 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 234–236 | 3 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 237–243 | 7 | 1 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 277–297 | 20 | 2 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 287–292 | 6 | 1 | Undefined position; Undefined team |
| `26` | `42` | Position_Unknown | Team_Unknown | 319–358 | 40 | 1 | Undefined position; Undefined team |
| `27` | `44` | Position_Unknown | Team_Unknown | 326–358 | 13 | 4 | Undefined position; Undefined team |
| `28` | `45` | Position_Unknown | Team_Unknown | 327–358 | 15 | 3 | Undefined position; Undefined team |
| `29` | `46` | Position_Unknown | Team_Unknown | 337–358 | 22 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 342–346 | 5 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `19` | `21` | 35 | 229 | 181 | 92.8% | 112–114, 116, 125–126, 139–140, 145, 155–159 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 55 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Action 'Action_BallCarry' range [270-302] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-356] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-246] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [247-279] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [281-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-336] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-342] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-173] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [304-328] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-312] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-332] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-186] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-337] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-354] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-182] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-334] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-358] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-319] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-275] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-310] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-318] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-342] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [247-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [252-253] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [256-300] for track '12' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-323] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-358] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-170] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-313] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-300] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-236] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-297] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-330] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-335] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-355] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-328] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-346] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-350] for track '31' has 1 frames without a visible bounding box.
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