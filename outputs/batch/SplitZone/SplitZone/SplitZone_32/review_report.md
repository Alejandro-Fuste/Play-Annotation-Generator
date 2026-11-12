# Play-Annotation-Generator Annotation Review — SplitZone_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_32`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 449
- **Player Tracks:** 65
- **Ball Tracks:** 1
- **Action Segments:** 135
- **Validation Warnings:** 197
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_SplitBlock` | TE2 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `10` | `10` |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | defense | `11` | `11` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `16` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 13 | START | 13 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 13 | START | 13 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 13 | START | 13 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 13 | START | 13 | 108 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 13 | START | 13 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 13 | START | 13 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 13 | START | 13 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `8` | `Group` | 13 | START | 13 | 226 |
| ✅ EXACT | `Action_BallSnap` | C | `0` | `0` | 215 | START | 215 | 229 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `0` | `0` | 218 | START | 230 | 280 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `2` | 218 | START | 218 | 289 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `6` | 218 | START | 218 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `7` | `7` | 218 | START | 218 | 232 |
| ✅ EXACT | `Action_SplitBlock` | TE2 | `8` | `8` | 227 | START | 227 | 261 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `10` | 229 | END | 215 | 229 |
| ✅ EXACT | `Action_Handoff` | QB | `10` | `10` | 242 | START | 242 | 267 |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF1 | `11` | `11` | 244 | START | 244 | 300 |
| ✅ EXACT | `Action_BallCarry` | RB | `16` | `16` | 268 | START | 268 | 297 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 300 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 13–449
- **Visible Samples:** 426

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_SnapReceive` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 241 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 242 | 267 | 26 | inferred_complete_timeline |
| `Action_None` | 268 | 291 | 24 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 298 | 429 | 132 | inferred_complete_timeline |
| `Action_None` | 435 | 438 | 4 | inferred_complete_timeline |
| `Action_None` | 441 | 449 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 13–297
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 108 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 175 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 267 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 268 | 297 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–306
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 276 | 62 | inferred_complete_timeline |
| `Action_None` | 289 | 306 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–261
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 226 | 214 | inferred_complete_timeline |
| `Action_SplitBlock` | 227 | 261 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 13–300
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 217 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 293 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 298 | 300 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–310
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_BallSnap` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 230 | 280 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 286 | 300 | 15 | inferred_complete_timeline |
| `Action_None` | 301 | 310 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–336
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 217 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 232 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 236 | 300 | 65 | inferred_complete_timeline |
| `Action_None` | 301 | 336 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–331
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 217 | 205 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 289 | 72 | inferred_complete_timeline |
| `Action_ZoneBlock` | 296 | 300 | 5 | inferred_complete_timeline |
| `Action_None` | 301 | 331 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 13–298
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 298 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 13–265
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 265 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–355
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 355 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 13–357
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 357 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 13–284
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 284 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–354
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 255 | 41 | inferred_complete_timeline |
| `Action_None` | 257 | 275 | 19 | inferred_complete_timeline |
| `Action_None` | 277 | 354 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–303
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 243 | 231 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 244 | 300 | 57 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–308
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 214 | 202 | inferred_complete_timeline |
| `Action_None` | 215 | 308 | 94 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 13–354 | 338 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 258–302 | 45 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 263–449 | 187 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 263–302 | 40 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 268–305 | 37 | 2 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 279–285 | 7 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 285–301 | 16 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 301–304 | 4 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 310–344 | 35 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 348–349 | 2 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 363–449 | 87 | 1 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 364–368 | 5 | 1 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 365–368 | 4 | 1 | Undefined position; Undefined team |
| `30` | `45` | Position_Unknown | Team_Unknown | 366–409 | 15 | 3 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 366–378 | 5 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 369–449 | 56 | 7 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 371–377 | 4 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 373–449 | 77 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 374–376 | 3 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 378–381 | 4 | 1 | Undefined position; Undefined team |
| `37` | `57` | Position_Unknown | Team_Unknown | 378–443 | 62 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 380–382 | 3 | 1 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 380–410 | 9 | 2 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 380–383 | 4 | 1 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 381–449 | 37 | 6 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 384–409 | 26 | 1 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 384–449 | 66 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 388–400 | 9 | 2 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 389–449 | 61 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 393–449 | 57 | 1 | Undefined position; Undefined team |
| `47` | `72` | Position_Unknown | Team_Unknown | 394–397 | 4 | 1 | Undefined position; Undefined team |
| `48` | `73` | Position_Unknown | Team_Unknown | 395–401 | 7 | 1 | Undefined position; Undefined team |
| `49` | `77` | Position_Unknown | Team_Unknown | 403–449 | 11 | 4 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 404–420 | 9 | 2 | Undefined position; Undefined team |
| `51` | `79` | Position_Unknown | Team_Unknown | 407–449 | 26 | 5 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 407–409 | 3 | 1 | Undefined position; Undefined team |
| `53` | `82` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `54` | `85` | Position_Unknown | Team_Unknown | 410–449 | 39 | 2 | Undefined position; Undefined team |
| `55` | `86` | Position_Unknown | Team_Unknown | 416–449 | 34 | 1 | Undefined position; Undefined team |
| `56` | `88` | Position_Unknown | Team_Unknown | 419–429 | 11 | 1 | Undefined position; Undefined team |
| `57` | `89` | Position_Unknown | Team_Unknown | 432–449 | 18 | 1 | Undefined position; Undefined team |
| `58` | `90` | Position_Unknown | Team_Unknown | 433–449 | 17 | 1 | Undefined position; Undefined team |
| `59` | `92` | Position_Unknown | Team_Unknown | 435–443 | 9 | 1 | Undefined position; Undefined team |
| `60` | `93` | Position_Unknown | Team_Unknown | 439–449 | 11 | 1 | Undefined position; Undefined team |
| `61` | `94` | Position_Unknown | Team_Unknown | 439–440 | 2 | 1 | Undefined position; Undefined team |
| `62` | `96` | Position_Unknown | Team_Unknown | 442–449 | 8 | 1 | Undefined position; Undefined team |
| `63` | `98` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |
| `64` | `99` | Position_Unknown | Team_Unknown | 448–449 | 2 | 1 | Undefined position; Undefined team |
| `65` | `100` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 28 | 215 | 172 | 91.5% | 50–65 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 49 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 49 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 98 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 66: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [215–229], lower_priority='Action_ZoneBlock' annotated_start=218, effective_Action_ZoneBlock_start=230.
- ⚠️ Action 'Action_ZoneBlock' range [230-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-335] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-354] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-284] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-265] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-308] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-293] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [295-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [298-300] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-232] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-336] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [227-261] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-298] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [242-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-291] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-429] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-438] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-355] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-275] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-354] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-276] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-306] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-357] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [268-297] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-302] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-302] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-285] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-301] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-344] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-384] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-371] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-377] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-394] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-427] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-444] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-381] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-443] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-410] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-395] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-404] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-407] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-420] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-409] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-393] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-400] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-397] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-401] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-410] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-416] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-421] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-438] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-416] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-429] for track '56' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-449] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-443] for track '59' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-440] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-449] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.

</details>