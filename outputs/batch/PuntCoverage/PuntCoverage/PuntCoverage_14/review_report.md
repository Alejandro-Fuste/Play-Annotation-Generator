# Play-Annotation-Generator Annotation Review — PuntCoverage_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_14`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 121
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 103
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_Tackle` | Left_Guard | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `3` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `5` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `8` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 328 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `3` | `3` | 6 | START | 6 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 34 | END | 34 | 34 |
| ✅ EXACT | `Action_PuntBall` | Punter | `4` | `4` | 60 | START | 60 | 76 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `21` | `21` | 205 | START | 205 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `21` | `21` | 239 | START | 239 | 342 |
| ✅ EXACT | `Action_Tackle` | Left_Guard | `9` | `9` | 329 | START | 329 | 336 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 328 | 329 | inferred_complete_timeline |
| `Action_Tackle` | 329 | 336 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 281 | 276 | inferred_complete_timeline |
| `Action_None` | 288 | 425 | 138 | inferred_complete_timeline |
| `Action_None` | 432 | 433 | 2 | inferred_complete_timeline |
| `Action_None` | 437 | 438 | 2 | inferred_complete_timeline |
| `Action_None` | 446 | 449 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–360
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_LongSnap` | 6 | 59 | 54 | inferred_complete_timeline |
| `Action_None` | 60 | 360 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 155 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 433

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 371 | 366 | inferred_complete_timeline |
| `Action_None` | 381 | 384 | 4 | inferred_complete_timeline |
| `Action_None` | 386 | 387 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 426 | 37 | inferred_complete_timeline |
| `Action_None` | 431 | 435 | 5 | inferred_complete_timeline |
| `Action_None` | 437 | 449 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 34 | 1 | inferred_complete_timeline |
| `Action_None` | 35 | 59 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 77 | 242 | 166 | inferred_complete_timeline |
| `Action_None` | 253 | 254 | 2 | inferred_complete_timeline |
| `Action_None` | 256 | 449 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–365
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 305 | 300 | inferred_complete_timeline |
| `Action_None` | 308 | 326 | 19 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 333 | 342 | 10 | inferred_complete_timeline |
| `Action_None` | 363 | 365 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–443
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 352 | 347 | inferred_complete_timeline |
| `Action_None` | 355 | 384 | 30 | inferred_complete_timeline |
| `Action_None` | 386 | 390 | 5 | inferred_complete_timeline |
| `Action_None` | 402 | 403 | 2 | inferred_complete_timeline |
| `Action_None` | 407 | 415 | 9 | inferred_complete_timeline |
| `Action_None` | 433 | 443 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–413
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 244 | 239 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 249 | 413 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 110 | 105 | inferred_complete_timeline |
| `Action_None` | 114 | 449 | 336 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 53 | 48 | inferred_complete_timeline |
| `Action_None` | 56 | 449 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 39 | 34 | inferred_complete_timeline |
| `Action_None` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_None` | 48 | 51 | 4 | inferred_complete_timeline |
| `Action_None` | 57 | 78 | 22 | inferred_complete_timeline |
| `Action_None` | 80 | 449 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 167 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–443
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 310 | 305 | inferred_complete_timeline |
| `Action_None` | 317 | 358 | 42 | inferred_complete_timeline |
| `Action_None` | 365 | 438 | 74 | inferred_complete_timeline |
| `Action_None` | 442 | 443 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 449 | 444 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 449 | 444 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 6 | 88 | 83 | inferred_complete_timeline |
| `Action_None` | 91 | 449 | 359 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 79–293 | 213 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 93–449 | 354 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 109–449 | 341 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 117–402 | 234 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 127–449 | 292 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 133–136 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 159–174 | 7 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 207–245 | 12 | 3 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 233–449 | 206 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 271–449 | 179 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 300–361 | 62 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 319–373 | 45 | 4 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 334–336 | 3 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 347–366 | 19 | 2 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 355–449 | 49 | 6 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 357–449 | 72 | 4 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 424–448 | 25 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 429–442 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 81 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [6-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-360] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-242] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-305] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-326] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-310] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-358] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-438] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-443] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-413] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-371] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-384] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-387] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-426] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-435] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-449] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [329-336] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-281] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-425] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-110] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-53] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-352] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-384] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-415] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-443] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [6-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-51] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-78] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-274] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-293] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-160] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-437] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [239-342] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [395-402] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-366] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-383] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-398] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-312] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-449] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-323] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-334] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-373] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-336] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-354] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-366] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-387] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-423] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-361] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-416] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-433] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-448] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-432] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-442] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>