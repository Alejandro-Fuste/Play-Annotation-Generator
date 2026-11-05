# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_68`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 213
- **Validation Warnings:** 260
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
- **Inferred Coverage Segments (Action_None):** 198
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `13` | `13` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `40` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 23 | START | 23 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `7` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 23 | START | 23 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `9` | `Group` | 23 | START | 23 | 92 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `7` | `7` | 93 | START | 93 | 136 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 116 | END | 116 | 116 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 140 | START | 140 | 155 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `13` | `13` | 254 | START | 254 | 273 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `13` | `13` | 274 | START | 274 | 277 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `49` | `40` | 606 | START | 606 | 611 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 23–350
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 153 | 61 | inferred_complete_timeline |
| `Action_None` | 156 | 340 | 185 | inferred_complete_timeline |
| `Action_None` | 342 | 350 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 23–578
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_LongSnap` | 93 | 136 | 44 | inferred_complete_timeline |
| `Action_None` | 143 | 160 | 18 | inferred_complete_timeline |
| `Action_None` | 163 | 175 | 13 | inferred_complete_timeline |
| `Action_None` | 182 | 360 | 179 | inferred_complete_timeline |
| `Action_None` | 371 | 575 | 205 | inferred_complete_timeline |
| `Action_None` | 577 | 578 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–268
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 155 | 63 | inferred_complete_timeline |
| `Action_None` | 185 | 268 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 23–216
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 216 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 23–560
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 130 | 38 | inferred_complete_timeline |
| `Action_None` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 270 | 125 | inferred_complete_timeline |
| `Action_None` | 273 | 287 | 15 | inferred_complete_timeline |
| `Action_None` | 289 | 395 | 107 | inferred_complete_timeline |
| `Action_None` | 398 | 432 | 35 | inferred_complete_timeline |
| `Action_None` | 434 | 560 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–456
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 115 | 93 | inferred_complete_timeline |
| `Action_SnapReceive` | 116 | 116 | 1 | inferred_complete_timeline |
| `Action_None` | 117 | 139 | 23 | inferred_complete_timeline |
| `Action_PuntBall` | 140 | 155 | 16 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 169 | 200 | 32 | inferred_complete_timeline |
| `Action_None` | 202 | 221 | 20 | inferred_complete_timeline |
| `Action_None` | 231 | 307 | 77 | inferred_complete_timeline |
| `Action_None` | 311 | 321 | 11 | inferred_complete_timeline |
| `Action_None` | 324 | 398 | 75 | inferred_complete_timeline |
| `Action_None` | 400 | 450 | 51 | inferred_complete_timeline |
| `Action_None` | 454 | 456 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 23–113
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 113 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 23–629
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 256 | 164 | inferred_complete_timeline |
| `Action_None` | 282 | 391 | 110 | inferred_complete_timeline |
| `Action_None` | 398 | 544 | 147 | inferred_complete_timeline |
| `Action_None` | 554 | 629 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 23–132
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 132 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 23–575
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 168 | 76 | inferred_complete_timeline |
| `Action_None` | 174 | 387 | 214 | inferred_complete_timeline |
| `Action_None` | 389 | 395 | 7 | inferred_complete_timeline |
| `Action_None` | 397 | 483 | 87 | inferred_complete_timeline |
| `Action_None` | 506 | 511 | 6 | inferred_complete_timeline |
| `Action_None` | 515 | 518 | 4 | inferred_complete_timeline |
| `Action_None` | 522 | 533 | 12 | inferred_complete_timeline |
| `Action_None` | 548 | 553 | 6 | inferred_complete_timeline |
| `Action_None` | 555 | 560 | 6 | inferred_complete_timeline |
| `Action_None` | 567 | 568 | 2 | inferred_complete_timeline |
| `Action_None` | 574 | 575 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–629
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 136 | 44 | inferred_complete_timeline |
| `Action_None` | 139 | 180 | 42 | inferred_complete_timeline |
| `Action_None` | 195 | 223 | 29 | inferred_complete_timeline |
| `Action_None` | 229 | 250 | 22 | inferred_complete_timeline |
| `Action_None` | 275 | 538 | 264 | inferred_complete_timeline |
| `Action_None` | 543 | 629 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 23–119
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 119 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 23–240
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 240 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 23–189
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 189 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 23–580
- **Visible Samples:** 545

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 506 | 414 | inferred_complete_timeline |
| `Action_None` | 516 | 518 | 3 | inferred_complete_timeline |
| `Action_None` | 521 | 533 | 13 | inferred_complete_timeline |
| `Action_None` | 535 | 569 | 35 | inferred_complete_timeline |
| `Action_None` | 571 | 580 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–204
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 92 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 204 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 23–438 | 391 | 10 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 51–450 | 345 | 12 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 117–404 | 272 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 125–495 | 360 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 135–230 | 96 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 156–240 | 82 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 174–177 | 4 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 186–629 | 396 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 231–629 | 310 | 10 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 260–416 | 157 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 275–416 | 132 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 278–464 | 175 | 6 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 328–384 | 46 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 334–629 | 234 | 7 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 355–397 | 43 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 364–494 | 100 | 4 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 374–592 | 205 | 7 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 397–498 | 100 | 2 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 420–629 | 210 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 422–629 | 202 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 434–629 | 193 | 2 | Undefined position; Undefined team |
| `37` | `45` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `38` | `46` | Position_Unknown | Team_Unknown | 446–468 | 19 | 2 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 450–629 | 180 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 451–629 | 179 | 3 | Undefined position; Undefined team |
| `41` | `51` | Position_Unknown | Team_Unknown | 465–467 | 3 | 1 | Undefined position; Undefined team |
| `42` | `52` | Position_Unknown | Team_Unknown | 467–629 | 153 | 3 | Undefined position; Undefined team |
| `43` | `53` | Position_Unknown | Team_Unknown | 469–598 | 72 | 13 | Undefined position; Undefined team |
| `44` | `55` | Position_Unknown | Team_Unknown | 473–474 | 2 | 1 | Undefined position; Undefined team |
| `45` | `56` | Position_Unknown | Team_Unknown | 488–491 | 4 | 1 | Undefined position; Undefined team |
| `46` | `58` | Position_Unknown | Team_Unknown | 499–584 | 69 | 7 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 504–509 | 6 | 1 | Undefined position; Undefined team |
| `48` | `61` | Position_Unknown | Team_Unknown | 516–551 | 19 | 4 | Undefined position; Undefined team |
| `49` | `62` | Position_Unknown | Team_Unknown | 519–628 | 109 | 2 | Undefined position; Undefined team |
| `50` | `63` | Position_Unknown | Team_Unknown | 536–543 | 8 | 1 | Undefined position; Undefined team |
| `51` | `66` | Position_Unknown | Team_Unknown | 554–594 | 37 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punt_Support1` position mapped to `defense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 185 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [93-155] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-307] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-321] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-398] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-450] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-216] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-132] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-130] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-270] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-395] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-432] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-560] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-189] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-340] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-350] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [93-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-175] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-360] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-575] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-113] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-391] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-544] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-204] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-136] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-223] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-538] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-629] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-240] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-40] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-83] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-95] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-253] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [274-277] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [287-438] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-168] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-387] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-395] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-483] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-511] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-518] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-533] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-553] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-560] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-119] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-506] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-518] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-533] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-569] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [571-580] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-92] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-131] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-398] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-424] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-450] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-352] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-387] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-264] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-270] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-483] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-495] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-304] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-313] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-412] for track '23' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-629] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-349] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-358] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-427] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-548] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-554] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-601] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [605-621] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-416] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-340] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-396] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-416] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-424] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-442] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-464] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-356] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-384] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-383] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-418] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-432] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-457] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-629] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-397] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-449] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-457] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-488] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-494] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-375] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-527] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-534] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-560] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-575] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-583] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-592] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-485] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-498] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-629] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-487] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-454] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-458] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-468] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [451-605] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-467] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-532] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-489] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-502] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-525] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-528] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-541] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-579] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-595] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-598] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-474] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-506] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-534] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-541] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-553] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-584] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-509] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-529] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-551] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-572] for track '49' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-628] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-543] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-569] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-579] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-588] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-594] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>