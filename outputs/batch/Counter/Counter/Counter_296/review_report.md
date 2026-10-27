# Play-Annotation-Generator Annotation Review — Counter_296

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_296`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | defense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 182 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 183 | START | 183 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `10` | 186 | START | 200 | 200 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `2` | `1` | 186 | START | 186 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `3` | `2` | 186 | START | 186 | 234 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `1` | `0` | 186 | START | 186 | 223 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 199 | END | 183 | 199 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 209 | START | 209 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | DT2 | `7` | `6` | 230 | START | 230 | 249 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 279 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–348
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_SnapReceive` | 183 | 199 | 17 | inferred_complete_timeline |
| `Action_None` | 200 | 208 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 209 | 229 | 21 | inferred_complete_timeline |
| `Action_None` | 230 | 344 | 115 | inferred_complete_timeline |
| `Action_None` | 346 | 348 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 186 | 223 | 38 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 225 | 276 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–335
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 215 | 33 | inferred_complete_timeline |
| `Action_None` | 219 | 249 | 31 | inferred_complete_timeline |
| `Action_None` | 251 | 282 | 32 | inferred_complete_timeline |
| `Action_None` | 289 | 335 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_BallSnap` | 183 | 199 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 200 | 200 | 1 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 216 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 241 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 243 | 257 | 15 | inferred_complete_timeline |
| `Action_None` | 312 | 407 | 96 | inferred_complete_timeline |
| `Action_None` | 414 | 419 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 234 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 276 | 279 | 4 | inferred_complete_timeline |
| `Action_None` | 280 | 419 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–347
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 243 | 61 | inferred_complete_timeline |
| `Action_None` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_None` | 253 | 255 | 3 | inferred_complete_timeline |
| `Action_None` | 276 | 280 | 5 | inferred_complete_timeline |
| `Action_None` | 286 | 291 | 6 | inferred_complete_timeline |
| `Action_None` | 306 | 307 | 2 | inferred_complete_timeline |
| `Action_None` | 310 | 313 | 4 | inferred_complete_timeline |
| `Action_None` | 315 | 316 | 2 | inferred_complete_timeline |
| `Action_None` | 323 | 347 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–333
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 230 | 48 | inferred_complete_timeline |
| `Action_None` | 235 | 251 | 17 | inferred_complete_timeline |
| `Action_None` | 264 | 333 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 36–318
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 182 | 147 | inferred_complete_timeline |
| `Action_None` | 183 | 218 | 36 | inferred_complete_timeline |
| `Action_None` | 268 | 269 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 318 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–400
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |
| `Action_BallCarry` | 230 | 249 | 20 | inferred_complete_timeline |
| `Action_BallCarry` | 251 | 326 | 76 | inferred_complete_timeline |
| `Action_BallCarry` | 328 | 400 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–263
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 218 | 36 | inferred_complete_timeline |
| `Action_None` | 220 | 263 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 236 | 54 | inferred_complete_timeline |
| `Action_None` | 241 | 311 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 182 | 183 | inferred_complete_timeline |
| `Action_None` | 183 | 245 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–419 | 408 | 8 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 5–403 | 261 | 18 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 11–32 | 6 | 2 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 220–419 | 200 | 1 | Undefined position; Undefined team |
| `16` | `24` | Position_Unknown | Team_Unknown | 248–419 | 172 | 1 | Undefined position; Undefined team |
| `17` | `26` | Position_Unknown | Team_Unknown | 251–332 | 79 | 2 | Undefined position; Undefined team |
| `18` | `28` | Position_Unknown | Team_Unknown | 257–299 | 43 | 1 | Undefined position; Undefined team |
| `19` | `29` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 281–374 | 89 | 3 | Undefined position; Undefined team |
| `21` | `32` | Position_Unknown | Team_Unknown | 290–311 | 18 | 2 | Undefined position; Undefined team |
| `22` | `33` | Position_Unknown | Team_Unknown | 291–419 | 127 | 2 | Undefined position; Undefined team |
| `23` | `35` | Position_Unknown | Team_Unknown | 297–419 | 78 | 6 | Undefined position; Undefined team |
| `24` | `40` | Position_Unknown | Team_Unknown | 308–331 | 24 | 1 | Undefined position; Undefined team |
| `25` | `42` | Position_Unknown | Team_Unknown | 310–395 | 19 | 3 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 329–419 | 91 | 1 | Undefined position; Undefined team |
| `27` | `47` | Position_Unknown | Team_Unknown | 330–419 | 90 | 1 | Undefined position; Undefined team |
| `28` | `48` | Position_Unknown | Team_Unknown | 330–335 | 5 | 2 | Undefined position; Undefined team |
| `29` | `49` | Position_Unknown | Team_Unknown | 330–406 | 77 | 1 | Undefined position; Undefined team |
| `30` | `51` | Position_Unknown | Team_Unknown | 353–419 | 56 | 2 | Undefined position; Undefined team |
| `31` | `53` | Position_Unknown | Team_Unknown | 391–400 | 9 | 2 | Undefined position; Undefined team |
| `32` | `54` | Position_Unknown | Team_Unknown | 404–419 | 16 | 1 | Undefined position; Undefined team |
| `33` | `55` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `3` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 90 |
| Track-related warning | 7 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 593: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 594: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '1' (Unknown) duration 94 frames exceeds threshold 90 frames [start=186, end=279].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '2' (RG) duration 94 frames exceeds threshold 90 frames [start=186, end=279].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '10' (C) duration 94 frames exceeds threshold 90 frames [start=186, end=279].
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [183–199], lower_priority='Action_DownBlock' annotated_start=186, effective_Action_DownBlock_start=200.
- ⚠️ Action 'Action_PullLeadBlock' range [186-223] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [225-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [223-233] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-363] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-403] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-234] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-251] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-333] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-243] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-291] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-263] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-249] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-326] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [328-400] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-249] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-282] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-335] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-344] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' for track '10' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_DownBlock' range [200-200] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-241] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [243-257] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-407] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-23] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-59] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-65] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-97] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-253] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-266] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-344] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-403] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-32] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-318] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-318] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-332] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-301] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-321] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-374] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-304] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-311] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-390] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-348] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-375] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-331] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-395] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-419] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-419] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-331] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-406] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-377] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-400] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>