# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_37

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_37`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 40
- **Ball Tracks:** 1
- **Action Segments:** 147
- **Validation Warnings:** 163
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 134
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `28` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `28` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `28` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 57 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 26 | START | 26 | 83 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 58 | END | 58 | 58 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 84 | START | 84 | 97 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `28` | `23` | 206 | START | 206 | 214 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `28` | `23` | 285 | START | 285 | 453 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `28` | `23` | 588 | START | 588 | 596 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 82 | 57 | inferred_complete_timeline |
| `Action_None` | 128 | 137 | 10 | inferred_complete_timeline |
| `Action_None` | 140 | 165 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 54 | 29 | inferred_complete_timeline |
| `Action_None` | 58 | 234 | 177 | inferred_complete_timeline |
| `Action_None` | 236 | 242 | 7 | inferred_complete_timeline |
| `Action_None` | 244 | 246 | 3 | inferred_complete_timeline |
| `Action_None` | 251 | 316 | 66 | inferred_complete_timeline |
| `Action_None` | 319 | 342 | 24 | inferred_complete_timeline |
| `Action_None` | 344 | 599 | 256 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_LongSnap` | 26 | 83 | 58 | inferred_complete_timeline |
| `Action_None` | 84 | 453 | 370 | inferred_complete_timeline |
| `Action_None` | 455 | 460 | 6 | inferred_complete_timeline |
| `Action_None` | 465 | 599 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 172 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 167 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_SnapReceive` | 58 | 58 | 1 | inferred_complete_timeline |
| `Action_None` | 59 | 83 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 84 | 97 | 14 | inferred_complete_timeline |
| `Action_None` | 98 | 155 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–500
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 182 | 157 | inferred_complete_timeline |
| `Action_None` | 190 | 199 | 10 | inferred_complete_timeline |
| `Action_None` | 204 | 405 | 202 | inferred_complete_timeline |
| `Action_None` | 409 | 416 | 8 | inferred_complete_timeline |
| `Action_None` | 418 | 433 | 16 | inferred_complete_timeline |
| `Action_None` | 438 | 440 | 3 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |
| `Action_None` | 474 | 476 | 3 | inferred_complete_timeline |
| `Action_None` | 482 | 487 | 6 | inferred_complete_timeline |
| `Action_None` | 491 | 492 | 2 | inferred_complete_timeline |
| `Action_None` | 497 | 500 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 582

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 311 | 286 | inferred_complete_timeline |
| `Action_None` | 313 | 455 | 143 | inferred_complete_timeline |
| `Action_None` | 460 | 465 | 6 | inferred_complete_timeline |
| `Action_None` | 467 | 468 | 2 | inferred_complete_timeline |
| `Action_None` | 473 | 506 | 34 | inferred_complete_timeline |
| `Action_None` | 509 | 510 | 2 | inferred_complete_timeline |
| `Action_None` | 513 | 548 | 36 | inferred_complete_timeline |
| `Action_None` | 552 | 580 | 29 | inferred_complete_timeline |
| `Action_None` | 582 | 599 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–490
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 340 | 315 | inferred_complete_timeline |
| `Action_None` | 351 | 490 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–165
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 58 | 33 | inferred_complete_timeline |
| `Action_None` | 68 | 165 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 586

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 152 | 127 | inferred_complete_timeline |
| `Action_None` | 154 | 337 | 184 | inferred_complete_timeline |
| `Action_None` | 351 | 599 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 40 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–571
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 571 | 546 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 198 | 173 | inferred_complete_timeline |
| `Action_None` | 200 | 205 | 6 | inferred_complete_timeline |
| `Action_None` | 213 | 342 | 130 | inferred_complete_timeline |
| `Action_None` | 345 | 569 | 225 | inferred_complete_timeline |
| `Action_None` | 572 | 599 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 152 | 127 | inferred_complete_timeline |
| `Action_None` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–549
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_None` | 26 | 533 | 508 | inferred_complete_timeline |
| `Action_None` | 535 | 545 | 11 | inferred_complete_timeline |
| `Action_None` | 547 | 549 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–442 | 441 | 3 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–176 | 175 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–169 | 170 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–128 | 124 | 5 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 43–599 | 536 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 46–599 | 533 | 9 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 82–599 | 518 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 157–599 | 439 | 8 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 181–599 | 408 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 256–599 | 337 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 265–453 | 187 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 266–468 | 195 | 5 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 283–285 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 291–599 | 309 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 306–556 | 251 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 320–504 | 185 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 369–528 | 152 | 4 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 441–449 | 7 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 521–532 | 10 | 3 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 527–599 | 71 | 2 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 556–560 | 5 | 1 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 562–563 | 2 | 1 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 569–599 | 31 | 1 | Undefined position; Undefined team |
| `40` | `54` | Position_Unknown | Team_Unknown | 590–592 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `35` | `48` | 522 | 525 | 4 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `28` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 76: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ Row 76: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 76: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [26-533] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [535-545] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-549] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-192] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-442] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-50] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-342] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-569] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-340] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-490] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-152] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-337] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-169] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-155] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-40] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-311] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-455] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-465] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-506] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-548] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-580] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-571] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-453] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-460] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-182] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-405] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-416] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-433] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-487] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-500] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-82] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-137] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-165] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-103] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-119] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-234] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-316] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-342] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-599] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-77] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-345] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-381] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-513] for track '20' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-530] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-90] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-125] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-271] for track '21' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-348] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-524] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [285-453] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [455-587] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-295] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-462] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-583] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-544] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-593] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-334] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-453] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-409] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-433] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-442] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-457] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-468] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-599] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-556] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-504] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-431] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-436] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-482] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-528] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-523] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-532] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-530] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-599] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-560] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-599] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-592] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>