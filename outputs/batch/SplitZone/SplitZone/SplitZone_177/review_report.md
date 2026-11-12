# Play-Annotation-Generator Annotation Review — SplitZone_177

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_177`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 419
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 116
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 95
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SplitBlock` | HB | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `13` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `1` | `Group` | 12 | START | 14 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 12 | START | 14 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 12 | START | 14 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 12 | START | 14 | 230 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 12 | START | 14 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 12 | START | 14 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 12 | START | 14 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 12 | START | 37 | 202 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 12 | START | 14 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 12 | START | 14 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 12 | START | 14 | 199 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 200 | START | 200 | 208 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `10` | 203 | START | 268 | 269 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `15` | `15` | 203 | START | 203 | 236 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `16` | 203 | START | 203 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `18` | `18` | 203 | START | 203 | 225 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `21` | 203 | START | 203 | 235 |
| ✅ EXACT | `Action_SplitBlock` | HB | `1` | `1` | 209 | START | 209 | 295 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 213 | END | 200 | 213 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `12` | 217 | START | 217 | 230 |
| ✅ EXACT | `Action_BallCarry` | RB | `13` | `13` | 231 | START | 231 | 369 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 295 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 14–419
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_SnapReceive` | 200 | 213 | 14 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |
| `Action_Handoff` | 217 | 230 | 14 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 259 | 21 | inferred_complete_timeline |
| `Action_None` | 262 | 379 | 118 | inferred_complete_timeline |
| `Action_None` | 387 | 419 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 14–369
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 230 | 217 | inferred_complete_timeline |
| `Action_BallCarry` | 231 | 369 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 14–419
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 208 | 195 | inferred_complete_timeline |
| `Action_SplitBlock` | 209 | 295 | 87 | inferred_complete_timeline |
| `Action_None` | 296 | 347 | 52 | inferred_complete_timeline |
| `Action_None` | 355 | 419 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 14–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 419 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 14–419
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 336 | 137 | inferred_complete_timeline |
| `Action_None` | 340 | 419 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 14–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 419 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 14–260
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 202 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 236 | 34 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 260 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 14–221
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 202 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 221 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 14–269
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_BallSnap` | 200 | 208 | 9 | inferred_complete_timeline |
| `Action_ZoneBlock` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 37–385
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 37 | 202 | 166 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 235 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 240 | 295 | 56 | inferred_complete_timeline |
| `Action_None` | 296 | 385 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 14–258
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 202 | 189 | inferred_complete_timeline |
| `Action_ZoneBlock` | 203 | 225 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 227 | 240 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 253 | 258 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 14–221
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 221 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 14–342
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 230 | 31 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 250 | 263 | 14 | inferred_complete_timeline |
| `Action_None` | 270 | 283 | 14 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 342 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 14–301
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 221 | 22 | inferred_complete_timeline |
| `Action_None` | 240 | 301 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 14–419
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 225 | 26 | inferred_complete_timeline |
| `Action_None` | 227 | 272 | 46 | inferred_complete_timeline |
| `Action_None` | 278 | 319 | 42 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 348 | 3 | inferred_complete_timeline |
| `Action_None` | 353 | 419 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 14–335
- **Visible Samples:** 317

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 325 | 126 | inferred_complete_timeline |
| `Action_None` | 331 | 335 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 14–248
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 248 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 14–417
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 370 | 171 | inferred_complete_timeline |
| `Action_None` | 372 | 373 | 2 | inferred_complete_timeline |
| `Action_None` | 380 | 401 | 22 | inferred_complete_timeline |
| `Action_None` | 404 | 408 | 5 | inferred_complete_timeline |
| `Action_None` | 412 | 417 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 14–301
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 301 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 14–419
- **Visible Samples:** 406

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 419 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 14–419
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 345 | 146 | inferred_complete_timeline |
| `Action_None` | 347 | 356 | 10 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 375 | 419 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 14–419
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 14 | 199 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 371 | 172 | inferred_complete_timeline |
| `Action_None` | 376 | 419 | 44 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 250–419 | 163 | 5 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 256–419 | 125 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 271–356 | 86 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 271–310 | 5 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 284–419 | 136 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 299–419 | 108 | 6 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 303–308 | 4 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 309–419 | 52 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 339–416 | 75 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 343–348 | 6 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 373–419 | 11 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 377–419 | 36 | 4 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 392–419 | 28 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 403–406 | 4 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 412–419 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 203 != Inferred start 268
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 76 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [200–213], lower_priority='Action_ZoneBlock' annotated_start=203, effective_Action_ZoneBlock_start=214.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '21' (RG) duration 93 frames exceeds threshold 90 frames [start=203, end=295].
- ⚠️ Action 'Action_None' range [200-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-342] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [209-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-347] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-345] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-356] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-248] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-371] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-370] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-401] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-408] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-417] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [200-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [268-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-301] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-259] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-379] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [231-369] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-325] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-335] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-236] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-221] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-272] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-319] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-225] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [227-240] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [253-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-221] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-301] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-221] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [203-235] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-385] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-257] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-321] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-358] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-419] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-287] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-356] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-382] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-392] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-408] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-308] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-322] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-393] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-416] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-374] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-413] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-385] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-413] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-419] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '35' has 1 frames without a visible bounding box.
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