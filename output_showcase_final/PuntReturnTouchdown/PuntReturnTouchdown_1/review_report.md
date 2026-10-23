# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_1

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_1`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 106
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `20` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `10` | `10` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `27` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner1 | `0` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `10` | `Group` | 0 | START | 0 | 78 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner2 | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `17` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `2` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `20` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `14` | `14` | 49 | START | 49 | 103 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `10` | `10` | 79 | END | 79 | 79 |
| ✅ EXACT | `Action_PuntBall` | Punter | `10` | `10` | 104 | START | 104 | 113 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `27` | `26` | 231 | START | 231 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `26` | 253 | START | 253 | 258 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `26` | 591 | START | 591 | 597 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 212 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–548
- **Visible Samples:** 541

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 261 | 213 | inferred_complete_timeline |
| `Action_None` | 263 | 280 | 18 | inferred_complete_timeline |
| `Action_None` | 288 | 548 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–588
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 313 | 265 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_None` | 328 | 588 | 261 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–514
- **Visible Samples:** 509

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 179 | 131 | inferred_complete_timeline |
| `Action_None` | 181 | 185 | 5 | inferred_complete_timeline |
| `Action_None` | 188 | 251 | 64 | inferred_complete_timeline |
| `Action_None` | 254 | 296 | 43 | inferred_complete_timeline |
| `Action_None` | 298 | 514 | 217 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–487
- **Visible Samples:** 486

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_LongSnap` | 49 | 103 | 55 | inferred_complete_timeline |
| `Action_None` | 104 | 252 | 149 | inferred_complete_timeline |
| `Action_None` | 255 | 487 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–579
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 288 | 240 | inferred_complete_timeline |
| `Action_None` | 291 | 540 | 250 | inferred_complete_timeline |
| `Action_None` | 549 | 550 | 2 | inferred_complete_timeline |
| `Action_None` | 552 | 565 | 14 | inferred_complete_timeline |
| `Action_None` | 567 | 579 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–533
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_None` | 80 | 103 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 104 | 113 | 10 | inferred_complete_timeline |
| `Action_None` | 114 | 533 | 420 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–556
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 157 | 109 | inferred_complete_timeline |
| `Action_None` | 161 | 162 | 2 | inferred_complete_timeline |
| `Action_None` | 247 | 288 | 42 | inferred_complete_timeline |
| `Action_None` | 292 | 556 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 138 | 90 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 281 | 233 | inferred_complete_timeline |
| `Action_None` | 283 | 286 | 4 | inferred_complete_timeline |
| `Action_None` | 288 | 357 | 70 | inferred_complete_timeline |
| `Action_None` | 361 | 599 | 239 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 599 | 551 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 241 | 193 | inferred_complete_timeline |
| `Action_None` | 243 | 258 | 16 | inferred_complete_timeline |
| `Action_None` | 260 | 286 | 27 | inferred_complete_timeline |
| `Action_None` | 289 | 292 | 4 | inferred_complete_timeline |
| `Action_None` | 295 | 300 | 6 | inferred_complete_timeline |
| `Action_None` | 307 | 569 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–594
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 241 | 193 | inferred_complete_timeline |
| `Action_None` | 244 | 594 | 351 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher4 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 599 | 551 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–450
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 280 | 232 | inferred_complete_timeline |
| `Action_None` | 282 | 284 | 3 | inferred_complete_timeline |
| `Action_None` | 286 | 450 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 543 | 495 | inferred_complete_timeline |
| `Action_None` | 545 | 599 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–402
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 402 | 354 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–522
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 522 | 474 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 599 | 551 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 234 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–580 | 581 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 57–62 | 5 | 2 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 61–62 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 170–594 | 417 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 177–181 | 5 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 183–547 | 350 | 7 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 204–599 | 385 | 8 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 221–243 | 22 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 228–568 | 338 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 330–332 | 3 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 458–459 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 474–475 | 2 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 532–569 | 35 | 3 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 532–588 | 46 | 3 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 533–536 | 4 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 557–599 | 29 | 6 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 559–586 | 21 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Edge_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 89 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 4: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [49-261] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-548] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-138] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-599] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-543] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-599] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-241] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-594] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-402] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-522] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-234] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-286] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-292] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-300] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-569] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-533] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-251] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-296] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-514] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-313] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-588] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-599] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-252] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-487] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-288] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-556] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-280] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-450] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-281] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-286] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-357] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-580] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-212] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-540] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-565] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-579] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-594] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-181] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-251] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-269] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-292] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-547] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [253-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-243] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-250] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-451] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-568] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-459] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-475] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-543] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-564] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-569] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-543] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-574] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-588] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-536] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-571] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-578] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-587] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-599] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-571] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-580] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>