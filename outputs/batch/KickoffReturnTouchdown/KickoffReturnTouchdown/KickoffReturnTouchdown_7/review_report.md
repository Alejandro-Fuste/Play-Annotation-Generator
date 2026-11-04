# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_7`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 199
- **Validation Warnings:** 253
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 187
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `12` | `12` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `33` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `26` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `33` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `10` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `13` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `8` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `12` | `12` | 22 | START | 22 | 82 |
| ✅ EXACT | `Action_KickBall` | Kicker | `12` | `12` | 83 | START | 83 | 88 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `33` | `26` | 201 | START | 201 | 205 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `33` | `26` | 216 | START | 216 | 456 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `33` | `26` | 618 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_KickApproach` | 22 | 82 | 61 | inferred_complete_timeline |
| `Action_KickBall` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 89 | 89 | 1 | inferred_complete_timeline |
| `Action_None` | 95 | 169 | 75 | inferred_complete_timeline |
| `Action_None` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_None` | 177 | 327 | 151 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |
| `Action_None` | 340 | 346 | 7 | inferred_complete_timeline |
| `Action_None` | 353 | 354 | 2 | inferred_complete_timeline |
| `Action_None` | 362 | 363 | 2 | inferred_complete_timeline |
| `Action_None` | 365 | 369 | 5 | inferred_complete_timeline |
| `Action_None` | 372 | 629 | 258 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 71 | 50 | inferred_complete_timeline |
| `Action_None` | 73 | 79 | 7 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 102 | 9 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 129 | 133 | 5 | inferred_complete_timeline |
| `Action_None` | 184 | 209 | 26 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 304 | 283 | inferred_complete_timeline |
| `Action_None` | 307 | 537 | 231 | inferred_complete_timeline |
| `Action_None` | 539 | 629 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–540
- **Visible Samples:** 536

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 153 | 132 | inferred_complete_timeline |
| `Action_None` | 156 | 525 | 370 | inferred_complete_timeline |
| `Action_None` | 527 | 532 | 6 | inferred_complete_timeline |
| `Action_None` | 534 | 537 | 4 | inferred_complete_timeline |
| `Action_None` | 539 | 540 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 624

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 106 | 85 | inferred_complete_timeline |
| `Action_None` | 108 | 261 | 154 | inferred_complete_timeline |
| `Action_None` | 265 | 282 | 18 | inferred_complete_timeline |
| `Action_None` | 285 | 629 | 345 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–416
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 177 | 156 | inferred_complete_timeline |
| `Action_None` | 180 | 381 | 202 | inferred_complete_timeline |
| `Action_None` | 384 | 388 | 5 | inferred_complete_timeline |
| `Action_None` | 390 | 393 | 4 | inferred_complete_timeline |
| `Action_None` | 397 | 400 | 4 | inferred_complete_timeline |
| `Action_None` | 405 | 408 | 4 | inferred_complete_timeline |
| `Action_None` | 411 | 416 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 65 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–623
- **Visible Samples:** 617

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 605 | 584 | inferred_complete_timeline |
| `Action_None` | 608 | 610 | 3 | inferred_complete_timeline |
| `Action_None` | 616 | 623 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–580
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 315 | 294 | inferred_complete_timeline |
| `Action_None` | 318 | 406 | 89 | inferred_complete_timeline |
| `Action_None` | 408 | 422 | 15 | inferred_complete_timeline |
| `Action_None` | 424 | 549 | 126 | inferred_complete_timeline |
| `Action_None` | 553 | 563 | 11 | inferred_complete_timeline |
| `Action_None` | 565 | 574 | 10 | inferred_complete_timeline |
| `Action_None` | 576 | 580 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–349
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 274 | 253 | inferred_complete_timeline |
| `Action_None` | 278 | 343 | 66 | inferred_complete_timeline |
| `Action_None` | 345 | 349 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 188 | 167 | inferred_complete_timeline |
| `Action_None` | 192 | 629 | 438 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–574
- **Visible Samples:** 550

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 501 | 480 | inferred_complete_timeline |
| `Action_None` | 504 | 516 | 13 | inferred_complete_timeline |
| `Action_None` | 519 | 531 | 13 | inferred_complete_timeline |
| `Action_None` | 534 | 548 | 15 | inferred_complete_timeline |
| `Action_None` | 558 | 559 | 2 | inferred_complete_timeline |
| `Action_None` | 561 | 563 | 3 | inferred_complete_timeline |
| `Action_None` | 573 | 574 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 179 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 442 | 421 | inferred_complete_timeline |
| `Action_None` | 444 | 629 | 186 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 3–243 | 233 | 6 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 4–77 | 38 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 8–72 | 28 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 78–629 | 517 | 12 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 99–100 | 2 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 100–101 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 107–622 | 499 | 7 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 114–577 | 464 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 116–315 | 200 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 117–624 | 456 | 9 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 121–248 | 120 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 133–614 | 474 | 5 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 139–576 | 428 | 7 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 144–307 | 161 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 215–629 | 399 | 7 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 242–573 | 329 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 267–563 | 283 | 5 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 294–629 | 281 | 10 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 315–629 | 293 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 329–341 | 13 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 329–629 | 301 | 1 | Undefined position; Undefined team |
| `36` | `54` | Position_Unknown | Team_Unknown | 427–430 | 4 | 1 | Undefined position; Undefined team |
| `37` | `56` | Position_Unknown | Team_Unknown | 448–450 | 3 | 1 | Undefined position; Undefined team |
| `38` | `57` | Position_Unknown | Team_Unknown | 456–563 | 106 | 2 | Undefined position; Undefined team |
| `39` | `59` | Position_Unknown | Team_Unknown | 468–480 | 7 | 3 | Undefined position; Undefined team |
| `40` | `61` | Position_Unknown | Team_Unknown | 507–511 | 5 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 570–595 | 26 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 570–629 | 35 | 5 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 572–629 | 7 | 2 | Undefined position; Undefined team |
| `44` | `69` | Position_Unknown | Team_Unknown | 597–628 | 32 | 1 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 598–618 | 9 | 2 | Undefined position; Undefined team |
| `46` | `74` | Position_Unknown | Team_Unknown | 604–624 | 21 | 1 | Undefined position; Undefined team |
| `47` | `75` | Position_Unknown | Team_Unknown | 606–616 | 7 | 2 | Undefined position; Undefined team |
| `48` | `79` | Position_Unknown | Team_Unknown | 618–619 | 2 | 1 | Undefined position; Undefined team |
| `49` | `80` | Position_Unknown | Team_Unknown | 621–629 | 9 | 1 | Undefined position; Undefined team |
| `50` | `81` | Position_Unknown | Team_Unknown | 623–629 | 7 | 1 | Undefined position; Undefined team |
| `51` | `82` | Position_Unknown | Team_Unknown | 623–625 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `33` (4 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `33` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 175 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '26' has invalid range: start=618, end=576. Clamping end to start.
- ⚠️ Action 'Action_None' range [22-304] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-537] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-629] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-274] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-343] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-349] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-501] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-516] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-531] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-548] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [558-559] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-563] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-153] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-525] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-532] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-188] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-629] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-442] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-315] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-406] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-422] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-549] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-563] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-574] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [576-580] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-605] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [608-610] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [616-623] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-106] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-261] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-282] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-629] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-177] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-381] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-388] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-393] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-408] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-416] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [22-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 89, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [89-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-327] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-346] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-363] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-369] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-71] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-79] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-102] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-123] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-209] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-18] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-92] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-12] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-29] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-91] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-488] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-525] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-532] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-537] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-573] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-580] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-599] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-629] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-123] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-136] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-144] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-281] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-468] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-486] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-622] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-577] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-315] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-532] for track '23' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-540] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-548] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-560] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-574] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [607-610] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [612-624] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-200] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-306] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-606] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [609-610] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-614] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [216-456] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [458-562] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [571-572] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [574-576] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-302] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-306] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-335] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-366] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-382] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-565] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-573] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-277] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-283] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-304] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-563] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-309] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-337] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-594] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-600] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-604] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-629] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-341] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-550] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-563] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-469] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-472] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-480] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-595] for track '41' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-574] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [594-595] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [602-614] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [617-629] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-574] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [626-629] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-628] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-600] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [613-618] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-624] for track '46' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [606-610] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [615-616] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [618-619] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [623-625] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>