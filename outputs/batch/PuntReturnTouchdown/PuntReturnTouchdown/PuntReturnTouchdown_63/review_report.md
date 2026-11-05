# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_63`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 173
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 117
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `17` | `17` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `17` | `17` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `31` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `31` | `25` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `52` | `39` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner2 | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `17` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `18` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `20` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `8` | `Group` | 0 | START | 0 | 35 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 36 | START | 36 | 90 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `17` | `17` | 64 | END | 64 | 64 |
| ✅ EXACT | `Action_PuntBall` | Punter | `17` | `17` | 91 | START | 91 | 106 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `31` | `25` | 221 | START | 221 | 228 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `31` | `25` | 258 | START | 258 | 358 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `52` | `39` | 578 | START | 578 | 583 |

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
- **Visible Frames:** 0–429
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 429 | 394 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–486
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 105 | 70 | inferred_complete_timeline |
| `Action_None` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 486 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 64 | 29 | inferred_complete_timeline |
| `Action_None` | 79 | 83 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–442
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_LongSnap` | 36 | 90 | 55 | inferred_complete_timeline |
| `Action_None` | 91 | 442 | 352 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–380
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 380 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 185 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 165 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 64 | 1 | inferred_complete_timeline |
| `Action_None` | 65 | 90 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 91 | 106 | 16 | inferred_complete_timeline |
| `Action_None` | 107 | 133 | 27 | inferred_complete_timeline |
| `Action_None` | 136 | 138 | 3 | inferred_complete_timeline |
| `Action_None` | 140 | 147 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 150 | 115 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 584

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 311 | 276 | inferred_complete_timeline |
| `Action_None` | 313 | 316 | 4 | inferred_complete_timeline |
| `Action_None` | 327 | 561 | 235 | inferred_complete_timeline |
| `Action_None` | 566 | 569 | 4 | inferred_complete_timeline |
| `Action_None` | 571 | 599 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 254 | 219 | inferred_complete_timeline |
| `Action_None` | 256 | 262 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–545
- **Visible Samples:** 546

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 545 | 510 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 328 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 101 | 66 | inferred_complete_timeline |
| `Action_None` | 104 | 599 | 496 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 592

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 100 | 65 | inferred_complete_timeline |
| `Action_None` | 102 | 486 | 385 | inferred_complete_timeline |
| `Action_None` | 492 | 497 | 6 | inferred_complete_timeline |
| `Action_None` | 499 | 512 | 14 | inferred_complete_timeline |
| `Action_None` | 514 | 599 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–422
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 422 | 387 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 199 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 99 | 64 | inferred_complete_timeline |
| `Action_None` | 102 | 599 | 498 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–318 | 319 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–599 | 590 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–45 | 46 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 19–370 | 331 | 8 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 74–540 | 467 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 98–100 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 136–161 | 26 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 166–411 | 234 | 6 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 167–599 | 430 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 167–170 | 4 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 219–220 | 2 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 220–221 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 226–230 | 5 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 243–248 | 6 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 248–546 | 210 | 7 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 258–259 | 2 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 260–338 | 79 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 289–405 | 101 | 3 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 291–324 | 19 | 3 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 300–301 | 2 | 1 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 300–303 | 4 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 323–599 | 275 | 4 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 335–599 | 247 | 7 | Undefined position; Undefined team |
| `41` | `55` | Position_Unknown | Team_Unknown | 339–586 | 245 | 3 | Undefined position; Undefined team |
| `42` | `57` | Position_Unknown | Team_Unknown | 344–385 | 15 | 3 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 347–348 | 2 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 351–430 | 80 | 1 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 398–401 | 4 | 1 | Undefined position; Undefined team |
| `46` | `61` | Position_Unknown | Team_Unknown | 421–422 | 2 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 423–482 | 60 | 1 | Undefined position; Undefined team |
| `48` | `63` | Position_Unknown | Team_Unknown | 444–599 | 156 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 483–497 | 15 | 1 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 509–514 | 6 | 1 | Undefined position; Undefined team |
| `51` | `69` | Position_Unknown | Team_Unknown | 515–521 | 7 | 1 | Undefined position; Undefined team |
| `52` | `70` | Position_Unknown | Team_Unknown | 525–526 | 2 | 1 | Undefined position; Undefined team |
| `53` | `77` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `31` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner2` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 128: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [36-254] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-561] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-569] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-185] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-599] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-486] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-497] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-512] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-328] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-422] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-105] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-486] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-318] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-545] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-442] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-60] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-264] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-599] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-101] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-380] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-199] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-133] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-138] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-147] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-429] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-83] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-251] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-354] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-361] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-540] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-358] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [362-380] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [390-411] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-486] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-599] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-343] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-431] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-438] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-480] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-546] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-338] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-367] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-377] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-405] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-310] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-437] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-401] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-531] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-599] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-486] for track '41' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-508] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-586] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-377] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-430] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-401] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-422] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-482] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-497] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-514] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-526] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>