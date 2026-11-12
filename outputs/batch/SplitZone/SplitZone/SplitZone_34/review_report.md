# Play-Annotation-Generator Annotation Review — SplitZone_34

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_34`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 34
- **Ball Tracks:** 1
- **Action Segments:** 88
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `7` | `7` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | WR1 | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | offense | `7` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 6 | START | 6 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 6 | START | 6 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `13` | `Group` | 6 | START | 6 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 6 | START | 6 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `18` | `Group` | 6 | START | 6 | 238 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 6 | START | 6 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 6 | START | 6 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 6 | START | 6 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 6 | START | 6 | 237 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 6 | START | 6 | 237 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `7` | 235 | START | 235 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `10` | `10` | 238 | START | 238 | 243 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `5` | `5` | 238 | START | 238 | 298 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `7` | `7` | 238 | START | 250 | 274 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `8` | `8` | 238 | START | 238 | 298 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `9` | `9` | 238 | START | 238 | 268 |
| ✅ EXACT | `Action_SplitBlock` | WR1 | `18` | `18` | 239 | START | 239 | 331 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 249 | END | 235 | 249 |
| ✅ EXACT | `Action_Handoff` | QB | `11` | `11` | 263 | START | 263 | 274 |
| ✅ EXACT | `Action_BallCarry` | RB | `19` | `19` | 275 | START | 275 | 326 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | C | `7` | `7` | 275 | START | 275 | 302 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 331 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_SnapReceive` | 235 | 249 | 15 | inferred_complete_timeline |
| `Action_None` | 250 | 262 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 263 | 274 | 12 | inferred_complete_timeline |
| `Action_None` | 275 | 419 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–326
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 274 | 269 | inferred_complete_timeline |
| `Action_BallCarry` | 275 | 326 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–415
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 238 | 233 | inferred_complete_timeline |
| `Action_SplitBlock` | 239 | 331 | 93 | inferred_complete_timeline |
| `Action_None` | 332 | 405 | 74 | inferred_complete_timeline |
| `Action_None` | 407 | 415 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–259
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 251 | 17 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 6–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 237 | 232 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 298 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–271
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 237 | 232 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 268 | 31 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 271 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 395

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_BallSnap` | 235 | 249 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 250 | 274 | 25 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 275 | 302 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 316 | 317 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 320 | 321 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 328 | 331 | 4 | inferred_complete_timeline |
| `Action_None` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 6–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 237 | 232 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 243 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 249 | 254 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 256 | 257 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 260 | 331 | 72 | inferred_complete_timeline |
| `Action_None` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–341
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 237 | 232 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 298 | 61 | inferred_complete_timeline |
| `Action_ZoneBlock` | 302 | 331 | 30 | inferred_complete_timeline |
| `Action_None` | 332 | 341 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 410 | 176 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 335 | 101 | inferred_complete_timeline |
| `Action_None` | 337 | 419 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–350
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 275 | 41 | inferred_complete_timeline |
| `Action_None` | 277 | 327 | 51 | inferred_complete_timeline |
| `Action_None` | 349 | 350 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–311
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 306 | 72 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 328 | 94 | inferred_complete_timeline |
| `Action_None` | 332 | 419 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–32
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 32 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 413

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 348 | 114 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–416
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 416 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 6–419
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 234 | 229 | inferred_complete_timeline |
| `Action_None` | 235 | 419 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `23` | Position_Unknown | Team_Unknown | 265–274 | 10 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 269–419 | 147 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 276–328 | 53 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 286–419 | 134 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 290–376 | 87 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 305–419 | 115 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 310–419 | 110 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 318–419 | 102 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 327–419 | 93 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 335–338 | 4 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 340–412 | 66 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 373–412 | 17 | 4 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 377–413 | 24 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | 6 | 235 | 184 | 80.0% | 67, 69–112, 139 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `7` (C): Annotated start 238 != Inferred start 250
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `7` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (RT) duration 94 frames exceeds threshold 90 frames [start=238, end=331].
- ⚠️ Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [235–249], lower_priority='Action_ZoneBlock' annotated_start=238, effective_Action_ZoneBlock_start=250.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '10' (RG) duration 94 frames exceeds threshold 90 frames [start=238, end=331].
- ⚠️ Action 'Action_None' range [235-348] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-419] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-328] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-416] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-298] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-341] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-32] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [275-302] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [316-317] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [320-321] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [323-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-298] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-268] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [270-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-243] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [249-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [256-257] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [260-331] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-275] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-327] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-306] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-410] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-335] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [239-331] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-405] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-415] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [275-326] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-410] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-328] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-376] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-338] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-372] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-412] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-382] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-386] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-412] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-392] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '34' has 1 frames without a visible bounding box.
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