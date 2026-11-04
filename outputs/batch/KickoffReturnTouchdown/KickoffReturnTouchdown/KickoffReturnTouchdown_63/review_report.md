# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_63

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_63`
- **Frame Range:** 0 to 629 (630 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 629
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 133
- **Validation Warnings:** 170
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `39` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `39` | `28` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `39` | `28` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `13` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `2` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `7` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `8` | `8` | 18 | START | 18 | 92 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 93 | START | 93 | 97 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `39` | `28` | 205 | START | 205 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `39` | `28` | 233 | START | 233 | 302 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `39` | `28` | 630 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_KickApproach` | 18 | 92 | 75 | inferred_complete_timeline |
| `Action_KickBall` | 93 | 97 | 5 | inferred_complete_timeline |
| `Action_None` | 98 | 445 | 348 | inferred_complete_timeline |
| `Action_None` | 448 | 454 | 7 | inferred_complete_timeline |
| `Action_None` | 456 | 459 | 4 | inferred_complete_timeline |
| `Action_None` | 478 | 481 | 4 | inferred_complete_timeline |
| `Action_None` | 530 | 531 | 2 | inferred_complete_timeline |
| `Action_None` | 554 | 562 | 9 | inferred_complete_timeline |
| `Action_None` | 564 | 568 | 5 | inferred_complete_timeline |
| `Action_None` | 573 | 629 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–571
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 571 | 554 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–627
- **Visible Samples:** 627

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 497 | 480 | inferred_complete_timeline |
| `Action_None` | 499 | 627 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–379
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 379 | 362 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–465
- **Visible Samples:** 410

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 391 | 374 | inferred_complete_timeline |
| `Action_None` | 448 | 465 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 399

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 277 | 260 | inferred_complete_timeline |
| `Action_None` | 288 | 408 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 128 | 111 | inferred_complete_timeline |
| `Action_None` | 130 | 629 | 500 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 46

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_None` | 35 | 45 | 11 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 73 | 20 | inferred_complete_timeline |
| `Action_None` | 77 | 81 | 5 | inferred_complete_timeline |
| `Action_None` | 99 | 103 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–436
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 21 | 27 | 7 | inferred_complete_timeline |
| `Action_None` | 29 | 100 | 72 | inferred_complete_timeline |
| `Action_None` | 103 | 421 | 319 | inferred_complete_timeline |
| `Action_None` | 425 | 436 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–574
- **Visible Samples:** 571

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 369 | 352 | inferred_complete_timeline |
| `Action_None` | 371 | 374 | 4 | inferred_complete_timeline |
| `Action_None` | 378 | 574 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 243 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 630

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 629 | 612 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 629

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 298 | 281 | inferred_complete_timeline |
| `Action_None` | 300 | 629 | 330 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–600
- **Visible Samples:** 575

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 253 | 236 | inferred_complete_timeline |
| `Action_None` | 266 | 326 | 61 | inferred_complete_timeline |
| `Action_None` | 340 | 597 | 258 | inferred_complete_timeline |
| `Action_None` | 599 | 600 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–373
- **Visible Samples:** 361

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 214 | 197 | inferred_complete_timeline |
| `Action_None` | 217 | 241 | 25 | inferred_complete_timeline |
| `Action_None` | 245 | 271 | 27 | inferred_complete_timeline |
| `Action_None` | 280 | 373 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–629
- **Visible Samples:** 625

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 230 | 213 | inferred_complete_timeline |
| `Action_None` | 233 | 481 | 249 | inferred_complete_timeline |
| `Action_None` | 485 | 629 | 145 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–469 | 418 | 6 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 41–52 | 10 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 44–53 | 10 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 80–629 | 531 | 6 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 107–108 | 2 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 133–262 | 130 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 142–236 | 95 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 158–629 | 440 | 9 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 168–290 | 123 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 194–629 | 426 | 8 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 257–629 | 371 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 258–598 | 281 | 4 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 282–461 | 180 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 295–405 | 111 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 370–448 | 79 | 1 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 383–556 | 174 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 392–629 | 225 | 4 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 420–421 | 2 | 1 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 483–486 | 4 | 1 | Undefined position; Undefined team |
| `38` | `62` | Position_Unknown | Team_Unknown | 484–521 | 20 | 2 | Undefined position; Undefined team |
| `39` | `63` | Position_Unknown | Team_Unknown | 490–491 | 2 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 496–565 | 22 | 5 | Undefined position; Undefined team |
| `41` | `65` | Position_Unknown | Team_Unknown | 530–531 | 2 | 1 | Undefined position; Undefined team |
| `42` | `71` | Position_Unknown | Team_Unknown | 549–550 | 2 | 1 | Undefined position; Undefined team |
| `43` | `72` | Position_Unknown | Team_Unknown | 561–562 | 2 | 1 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 593–629 | 10 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `39` (5 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `39` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 109 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
- ⚠️ Segment 'Action_CrossGoalLine' for track '28' has invalid range: start=630, end=629. Clamping end to start.
- ⚠️ Action 'Action_None' range [18-571] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-243] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-497] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-627] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-408] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-298] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-629] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-326] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-597] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [599-600] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-391] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-465] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-445] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-454] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-562] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-568] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-214] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-373] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-379] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-230] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-481] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-629] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-369] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-374] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-574] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-128] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-629] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-27] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-100] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-421] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-436] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-45] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-73] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 18, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [18-22] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-312] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-469] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-53] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-485] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-556] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-562] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-568] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-629] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-236] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-320] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-421] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-448] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-456] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-557] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-613] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-290] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchKick' range [205-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [233-302] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [308-338] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [340-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [364-492] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [494-629] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-284] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-385] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-545] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-565] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-598] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-461] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-405] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-448] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-556] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-427] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-433] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-494] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-421] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-486] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-496] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-491] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-497] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-504] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-523] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-552] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [563-565] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-550] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-562] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-594] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [604-605] for track '44' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 630. Video range is [0, 629].

</details>