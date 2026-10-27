# Play-Annotation-Generator Annotation Review — Counter_45

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_45`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 79
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 3
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `17` | `16` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `18` | `17` |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB1 | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB1 | offense | `12` | `11` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `22` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `10` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `18` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 35 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `2` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 35 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 35 | 51 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 0 | START | N/A | N/A |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `18` | `17` | 17 | START | 35 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `16` | `15` | 28 | START | 35 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `17` | `16` | 28 | START | 35 | 235 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `18` | `17` | 28 | START | 36 | 235 |
| ⚠️ END CHANGED | `Action_SnapReceive` | QB1 | `12` | `11` | 32 | END | 35 | 35 |
| ✅ EXACT | `Action_Handoff` | QB1 | `12` | `11` | 42 | START | 42 | 55 |
| ✅ EXACT | `Action_PullBlock` | RG | `22` | `21` | 52 | START | 52 | 235 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `20` | `19` | 52 | START | 52 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `22` | 56 | START | 204 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 235 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 35–244
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_SnapReceive` | 35 | 35 | 1 | inferred_complete_timeline |
| `Action_None` | 36 | 41 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 42 | 55 | 14 | inferred_complete_timeline |
| `Action_None` | 56 | 244 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>QB2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 266 | 232 | inferred_complete_timeline |
| `Action_None` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_None` | 295 | 298 | 4 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |
| `Action_None` | 328 | 332 | 5 | inferred_complete_timeline |
| `Action_None` | 334 | 389 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 251 | 217 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 268 | 272 | 5 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 303 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 389 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 35 | 235 | 201 | inferred_complete_timeline |
| `Action_None` | 236 | 257 | 22 | inferred_complete_timeline |
| `Action_None` | 264 | 306 | 43 | inferred_complete_timeline |
| `Action_None` | 315 | 389 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_DownBlock` | 35 | 235 | 201 | inferred_complete_timeline |
| `Action_None` | 236 | 389 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 35–290
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 35 | 35 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 36 | 235 | 200 | inferred_complete_timeline |
| `Action_None` | 236 | 276 | 41 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 35–389
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_PullBlock` | 52 | 235 | 184 | inferred_complete_timeline |
| `Action_None` | 236 | 260 | 25 | inferred_complete_timeline |
| `Action_None` | 263 | 266 | 4 | inferred_complete_timeline |
| `Action_None` | 269 | 276 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |
| `Action_None` | 315 | 326 | 12 | inferred_complete_timeline |
| `Action_None` | 330 | 389 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 35–291
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 35 | 51 | 17 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 52 | 235 | 184 | inferred_complete_timeline |
| `Action_None` | 236 | 291 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 35–283
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 253 | 219 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 280 | 283 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 382 | 348 | inferred_complete_timeline |
| `Action_None` | 384 | 385 | 2 | inferred_complete_timeline |
| `Action_None` | 387 | 389 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 35–274
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 274 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 35–319
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 319 | 285 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 389 | 355 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 35–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 292 | 258 | inferred_complete_timeline |
| `Action_None` | 296 | 389 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 35–308
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 35 | 308 | 274 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 35–284 | 246 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 204–243 | 39 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 315–389 | 75 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 317–321 | 5 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 318–389 | 66 | 4 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 320–389 | 68 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 324–379 | 56 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 338–389 | 48 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 339–389 | 49 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 343–344 | 2 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 350–389 | 40 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 370–389 | 16 | 2 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 378–380 | 3 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (C): Annotated start 17 != Inferred start 35
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `18` (C): Annotated start 28 != Inferred start 36
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 8 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '11' has invalid range: start=35, end=32. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (LG) duration 201 frames exceeds threshold 90 frames [start=35, end=235].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (LT) duration 201 frames exceeds threshold 90 frames [start=35, end=235].
- ⚠️ Segment 'Action_BallSnap' for track '17' has invalid range: start=35, end=32. Clamping end to start.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '17' (C) duration 201 frames exceeds threshold 90 frames [start=35, end=235].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [35–35], lower_priority='Action_DownBlock' annotated_start=35, effective_Action_DownBlock_start=36.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 184 frames exceeds threshold 90 frames [start=52, end=235].
- ⚠️ Action 'Action_None' range [35-292] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-308] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-319] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-382] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-244] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-257] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-306] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-276] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-266] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-274] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-332] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-389] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-291] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-260] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-266] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-389] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-233] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-326] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-331] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-346] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-324] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-379] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-344] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-389] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-372] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-380] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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