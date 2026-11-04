# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_57

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_57`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 149
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 133
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `27` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `27` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `23` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `0` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `13` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `15` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `16` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `4` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `5` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `8` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `9` | `Group` | 0 | START | 0 | 3 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `14` | `14` | 4 | START | 4 | 59 |
| ✅ EXACT | `Action_KickBall` | Kicker | `14` | `14` | 60 | START | 60 | 63 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `27` | `23` | 167 | START | 167 | 178 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `27` | `23` | 194 | START | 194 | 583 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `23` | 584 | START | 584 | 591 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–510
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_KickApproach` | 4 | 59 | 56 | inferred_complete_timeline |
| `Action_KickBall` | 60 | 63 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 146 | 83 | inferred_complete_timeline |
| `Action_None` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 163 | 7 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 178 | 179 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 182 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 208 | 18 | inferred_complete_timeline |
| `Action_None` | 214 | 363 | 150 | inferred_complete_timeline |
| `Action_None` | 366 | 370 | 5 | inferred_complete_timeline |
| `Action_None` | 380 | 395 | 16 | inferred_complete_timeline |
| `Action_None` | 399 | 406 | 8 | inferred_complete_timeline |
| `Action_None` | 409 | 510 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 576

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 545 | 542 | inferred_complete_timeline |
| `Action_None` | 549 | 556 | 8 | inferred_complete_timeline |
| `Action_None` | 566 | 581 | 16 | inferred_complete_timeline |
| `Action_None` | 590 | 591 | 2 | inferred_complete_timeline |
| `Action_None` | 594 | 596 | 3 | inferred_complete_timeline |
| `Action_None` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 208 | 205 | inferred_complete_timeline |
| `Action_None` | 210 | 592 | 383 | inferred_complete_timeline |
| `Action_None` | 595 | 599 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 457 | 454 | inferred_complete_timeline |
| `Action_None` | 459 | 599 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 187 | 184 | inferred_complete_timeline |
| `Action_None` | 193 | 371 | 179 | inferred_complete_timeline |
| `Action_None` | 373 | 599 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 147 | 144 | inferred_complete_timeline |
| `Action_None` | 149 | 233 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–477
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 261 | 258 | inferred_complete_timeline |
| `Action_None` | 272 | 323 | 52 | inferred_complete_timeline |
| `Action_None` | 332 | 337 | 6 | inferred_complete_timeline |
| `Action_None` | 361 | 450 | 90 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–597
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 135 | 132 | inferred_complete_timeline |
| `Action_None` | 137 | 431 | 295 | inferred_complete_timeline |
| `Action_None` | 437 | 549 | 113 | inferred_complete_timeline |
| `Action_None` | 551 | 562 | 12 | inferred_complete_timeline |
| `Action_None` | 574 | 580 | 7 | inferred_complete_timeline |
| `Action_None` | 586 | 588 | 3 | inferred_complete_timeline |
| `Action_None` | 593 | 597 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 163 | 160 | inferred_complete_timeline |
| `Action_None` | 165 | 173 | 9 | inferred_complete_timeline |
| `Action_None` | 175 | 486 | 312 | inferred_complete_timeline |
| `Action_None` | 488 | 578 | 91 | inferred_complete_timeline |
| `Action_None` | 581 | 599 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 56 | 53 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_None` | 75 | 82 | 8 | inferred_complete_timeline |
| `Action_None` | 84 | 599 | 516 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 216 | 213 | inferred_complete_timeline |
| `Action_None` | 218 | 222 | 5 | inferred_complete_timeline |
| `Action_None` | 224 | 266 | 43 | inferred_complete_timeline |
| `Action_None` | 272 | 599 | 328 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 289 | 286 | inferred_complete_timeline |
| `Action_None` | 291 | 599 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–578
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 254 | 251 | inferred_complete_timeline |
| `Action_None` | 257 | 284 | 28 | inferred_complete_timeline |
| `Action_None` | 286 | 287 | 2 | inferred_complete_timeline |
| `Action_None` | 289 | 295 | 7 | inferred_complete_timeline |
| `Action_None` | 299 | 307 | 9 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 314 | 315 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 578 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–532
- **Visible Samples:** 523

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 211 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 524 | 308 | inferred_complete_timeline |
| `Action_None` | 530 | 532 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 318 | 315 | inferred_complete_timeline |
| `Action_None` | 321 | 599 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 599 | 596 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `21` | Position_Unknown | Team_Unknown | 63–75 | 6 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 89–533 | 431 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 105–599 | 495 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 110–599 | 490 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 115–116 | 2 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 122–599 | 478 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 136–599 | 464 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 251–599 | 349 | 1 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 339–362 | 12 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 347–368 | 8 | 3 | Undefined position; Undefined team |
| `28` | `42` | Position_Unknown | Team_Unknown | 356–369 | 9 | 2 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 364–368 | 5 | 1 | Undefined position; Undefined team |
| `30` | `47` | Position_Unknown | Team_Unknown | 393–400 | 8 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 405–406 | 2 | 1 | Undefined position; Undefined team |
| `32` | `49` | Position_Unknown | Team_Unknown | 405–459 | 42 | 7 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 447–500 | 19 | 4 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 462–581 | 61 | 14 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 474–599 | 126 | 1 | Undefined position; Undefined team |
| `36` | `62` | Position_Unknown | Team_Unknown | 517–526 | 10 | 1 | Undefined position; Undefined team |
| `37` | `64` | Position_Unknown | Team_Unknown | 523–599 | 77 | 1 | Undefined position; Undefined team |
| `38` | `65` | Position_Unknown | Team_Unknown | 547–599 | 53 | 1 | Undefined position; Undefined team |
| `39` | `68` | Position_Unknown | Team_Unknown | 576–599 | 24 | 1 | Undefined position; Undefined team |
| `40` | `69` | Position_Unknown | Team_Unknown | 576–580 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `27` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 109 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [4-457] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-187] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-371] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-289] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-216] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-222] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-545] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-556] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-581] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-596] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-233] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-318] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-592] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-599] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-254] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-284] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-287] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-295] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-307] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-578] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-524] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-532] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-337] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-450] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-56] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-163] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-208] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-363] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-370] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-395] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-406] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-510] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-431] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-549] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-562] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-580] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-588] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-597] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-163] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-173] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-486] for track '16' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-578] for track '16' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-255] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-524] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [194-583] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-343] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-362] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-368] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-368] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-400] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-406] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-413] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-419] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-430] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-445] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-449] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-459] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-451] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-484] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-500] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-466] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-478] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-489] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-501] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-505] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-517] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-524] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [537-541] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-551] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-558] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-568] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-581] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-599] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-526] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-580] for track '40' has 1 frames without a visible bounding box.
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

</details>