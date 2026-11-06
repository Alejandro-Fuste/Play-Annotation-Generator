# Play-Annotation-Generator Annotation Review — PuntCoverage_58

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_58`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 195
- **Validation Warnings:** 246
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 169
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `36` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `16` | `Group` | 0 | START | 0 | 458 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 539 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `4` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 417 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 57 | START | 57 | 70 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `36` | `31` | 167 | START | 167 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `36` | `31` | 230 | START | 230 | 384 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 539 | 540 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 237 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 422 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 426 | 443 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 446 | 447 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 450 | 451 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 458 | 459 | inferred_complete_timeline |
| `Action_PreSnap` | 462 | 483 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 485 | 539 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–47
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 415 | 395 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 539 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PuntBall` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 157 | 87 | inferred_complete_timeline |
| `Action_None` | 159 | 302 | 144 | inferred_complete_timeline |
| `Action_None` | 308 | 327 | 20 | inferred_complete_timeline |
| `Action_None` | 331 | 539 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–505
- **Visible Samples:** 503

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 417 | 418 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 505 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 149 | 129 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 252 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 82 | 103 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–474
- **Visible Samples:** 455

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 19 | 248 | 230 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 337 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 342 | 460 | 119 | inferred_complete_timeline |
| `Action_PreSnap` | 468 | 469 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 472 | 474 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–510
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 172 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 174 | 399 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 409 | 412 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 421 | 425 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 430 | 442 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 445 | 478 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 480 | 484 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 486 | 510 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–478
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 241 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 250 | 460 | 211 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 478 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 24 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 180 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–523
- **Visible Samples:** 513

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_PreSnap` | 401 | 478 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 489 | 523 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 109 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 115 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 123 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 529

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 120 | 100 | inferred_complete_timeline |
| `Action_PreSnap` | 122 | 380 | 259 | inferred_complete_timeline |
| `Action_PreSnap` | 382 | 383 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 385 | 400 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 403 | 539 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 23 | 115 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 118 | 123 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 179 | 51 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 255 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 305 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 307 | 347 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 358 | 361 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–82 | 70 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–539 | 518 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–12 | 13 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 29–539 | 470 | 12 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 43–44 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 57–61 | 5 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 73–425 | 340 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 102–163 | 62 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 106–134 | 24 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 114–276 | 61 | 11 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 143–305 | 105 | 15 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 153–169 | 7 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 155–158 | 4 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 156–423 | 256 | 6 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 196–474 | 245 | 9 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 205–539 | 274 | 12 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 214–217 | 4 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 232–539 | 305 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 265–539 | 241 | 4 | Undefined position; Undefined team |
| `38` | `48` | Position_Unknown | Team_Unknown | 272–273 | 2 | 1 | Undefined position; Undefined team |
| `39` | `49` | Position_Unknown | Team_Unknown | 277–278 | 2 | 1 | Undefined position; Undefined team |
| `40` | `50` | Position_Unknown | Team_Unknown | 284–432 | 75 | 15 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 285–287 | 3 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 290–539 | 250 | 1 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 295–422 | 124 | 2 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 386–526 | 141 | 1 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 400–403 | 4 | 1 | Undefined position; Undefined team |
| `46` | `57` | Position_Unknown | Team_Unknown | 445–455 | 11 | 1 | Undefined position; Undefined team |
| `47` | `58` | Position_Unknown | Team_Unknown | 507–537 | 9 | 2 | Undefined position; Undefined team |
| `48` | `59` | Position_Unknown | Team_Unknown | 519–523 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `36` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Row 60, Column 'Tackle': Unknown actor track ID '?' in entry '468,515,?'.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 183 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action 'Action_None' range [71-157] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-302] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-327] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-120] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-380] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-383] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-400] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [403-539] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-539] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-415] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-417] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-505] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-460] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-478] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-109] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-115] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-123] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-248] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-337] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [342-460] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-469] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [472-474] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-115] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-123] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-179] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-255] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-305] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-347] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-361] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-47] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-149] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-252] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-172] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-399] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-412] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-425] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-442] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-478] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [480-484] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-510] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-399] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [401-478] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [489-523] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-458] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [462-483] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [485-539] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-237] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-422] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [426-443] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [446-447] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [450-451] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-82] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-419] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [425-456] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-185] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-188] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-345] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-349] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-352] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-479] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-500] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-61] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-336] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-343] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [351-416] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-425] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-117] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-129] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-134] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-123] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-146] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-160] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-166] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-228] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-171] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-182] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-194] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-203] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-215] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-226] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-243] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-248] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-267] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [282-287] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-384] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [386-409] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [421-423] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-223] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-360] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [366-384] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-407] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [409-411] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [423-425] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-455] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [458-474] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-209] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-229] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-234] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-335] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-399] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-416] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-425] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-483] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [486-539] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-217] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-277] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-466] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [468-471] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-503] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-278] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-294] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-311] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-321] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [338-341] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-363] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [367-368] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-376] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [378-379] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-387] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [392-393] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [396-410] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-413] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-432] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [285-287] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-416] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-422] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [386-526] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-403] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [445-455] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-512] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [535-537] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-523] for track '48' has 1 frames without a visible bounding box.
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

</details>