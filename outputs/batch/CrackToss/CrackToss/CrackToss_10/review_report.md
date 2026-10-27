# Play-Annotation-Generator Annotation Review — CrackToss_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_10`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 34
- **Ball Tracks:** 2
- **Action Segments:** 95
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_PullBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Toss` | QB | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 254 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 216 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `17` | 217 | START | 217 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR2 | `17` | `16` | 220 | START | 220 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | WR1 | `7` | `6` | 220 | START | 220 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LT | `2` | `1` | 220 | START | 220 | 305 |
| ✅ EXACT | `Action_PullBlock` | TE | `6` | `5` | 220 | START | 220 | 324 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 221 | END | 217 | 221 |
| ✅ EXACT | `Action_Toss` | QB | `16` | `15` | 227 | START | 227 | 254 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 255 | START | 255 | 272 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 324 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–277
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_SnapReceive` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 222 | 226 | 5 | inferred_complete_timeline |
| `Action_Toss` | 227 | 254 | 28 | inferred_complete_timeline |
| `Action_None` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_None` | 274 | 277 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 254 | 255 | inferred_complete_timeline |
| `Action_BallCarry` | 255 | 272 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 274 | 389 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_CrackBlock` | 220 | 271 | 52 | inferred_complete_timeline |
| `Action_CrackBlock` | 277 | 324 | 48 | inferred_complete_timeline |
| `Action_None` | 325 | 335 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_CrackBlock` | 220 | 268 | 49 | inferred_complete_timeline |
| `Action_CrackBlock` | 274 | 282 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 285 | 324 | 40 | inferred_complete_timeline |
| `Action_None` | 325 | 389 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 324 | 105 | inferred_complete_timeline |
| `Action_None` | 325 | 389 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PullBlock` | 220 | 305 | 86 | inferred_complete_timeline |
| `Action_PullBlock` | 307 | 324 | 18 | inferred_complete_timeline |
| `Action_None` | 325 | 389 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 287 | 71 | inferred_complete_timeline |
| `Action_None` | 289 | 346 | 58 | inferred_complete_timeline |
| `Action_None` | 348 | 389 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 216 | 198 | inferred_complete_timeline |
| `Action_BallSnap` | 217 | 221 | 5 | inferred_complete_timeline |
| `Action_None` | 222 | 389 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–317
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 216 | 92 | inferred_complete_timeline |
| `Action_None` | 217 | 264 | 48 | inferred_complete_timeline |
| `Action_None` | 270 | 292 | 23 | inferred_complete_timeline |
| `Action_None` | 298 | 317 | 20 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 259 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–383
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 300 | 84 | inferred_complete_timeline |
| `Action_None` | 306 | 322 | 17 | inferred_complete_timeline |
| `Action_None` | 329 | 333 | 5 | inferred_complete_timeline |
| `Action_None` | 335 | 336 | 2 | inferred_complete_timeline |
| `Action_None` | 357 | 383 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 259 | 43 | inferred_complete_timeline |
| `Action_None` | 261 | 279 | 19 | inferred_complete_timeline |
| `Action_None` | 282 | 318 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–295
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 283 | 67 | inferred_complete_timeline |
| `Action_None` | 294 | 295 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 389 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–337
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 337 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 306 | 90 | inferred_complete_timeline |
| `Action_None` | 310 | 312 | 3 | inferred_complete_timeline |
| `Action_None` | 314 | 316 | 3 | inferred_complete_timeline |
| `Action_None` | 318 | 389 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_None` | 217 | 246 | 30 | inferred_complete_timeline |
| `Action_None` | 250 | 389 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–298 | 288 | 5 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 82–135 | 54 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 89–287 | 192 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 168–389 | 221 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 286–353 | 66 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 290–306 | 4 | 2 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 294–295 | 2 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 306–314 | 8 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 308–389 | 82 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 315–389 | 75 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 331–351 | 21 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 333–389 | 57 | 1 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 345–389 | 45 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 346–389 | 44 | 1 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 355–389 | 35 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 362–376 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | 63 | 63 | 1 | 100.0% | None |
| `35` | `57` | 367 | 367 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 22: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '1' (LT) duration 105 frames exceeds threshold 90 frames [start=220, end=324].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (TE) duration 105 frames exceeds threshold 90 frames [start=220, end=324].
- ⚠️ Action 'Action_None' range [217-300] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-322] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-383] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-305] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-246] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [220-324] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [220-271] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [277-324] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-335] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-287] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-346] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-259] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-306] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-316] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-264] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-292] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-317] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-283] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-337] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-259] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-279] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-318] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [227-254] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-272] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-277] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [220-268] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [274-282] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-99] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-216] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-287] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-216] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-276] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-306] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-319] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-353] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-311] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-389] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-351] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-389] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-376] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>