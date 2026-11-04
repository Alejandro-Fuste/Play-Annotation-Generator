# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_84

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_84`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 192
- **Validation Warnings:** 220
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 1
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 179
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `35` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `35` | `25` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `35` | `25` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `1` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `16` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `9` | `Group` | 0 | START | 0 | 7 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `8` | `8` | 8 | START | 8 | 24 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `8` | `8` | 59 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `35` | `25` | 182 | START | 182 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `35` | `25` | 209 | START | 209 | 252 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `35` | `25` | 553 | START | 553 | 557 |

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
- **Visible Frames:** 0–541
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_KickApproach` | 8 | 24 | 17 | inferred_complete_timeline |
| `Action_KickApproach` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 46 | 54 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_None` | 117 | 497 | 381 | inferred_complete_timeline |
| `Action_None` | 499 | 520 | 22 | inferred_complete_timeline |
| `Action_None` | 522 | 541 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 16 | 9 | inferred_complete_timeline |
| `Action_None` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_None` | 32 | 35 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–94
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 43 | 72 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 27 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 37 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 516

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 469 | 462 | inferred_complete_timeline |
| `Action_None` | 471 | 480 | 10 | inferred_complete_timeline |
| `Action_None` | 505 | 511 | 7 | inferred_complete_timeline |
| `Action_None` | 513 | 515 | 3 | inferred_complete_timeline |
| `Action_None` | 518 | 521 | 4 | inferred_complete_timeline |
| `Action_None` | 523 | 531 | 9 | inferred_complete_timeline |
| `Action_None` | 533 | 535 | 3 | inferred_complete_timeline |
| `Action_None` | 560 | 569 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–556
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 442 | 435 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |
| `Action_None` | 451 | 480 | 30 | inferred_complete_timeline |
| `Action_None` | 483 | 488 | 6 | inferred_complete_timeline |
| `Action_None` | 491 | 506 | 16 | inferred_complete_timeline |
| `Action_None` | 509 | 523 | 15 | inferred_complete_timeline |
| `Action_None` | 527 | 537 | 11 | inferred_complete_timeline |
| `Action_None` | 539 | 547 | 9 | inferred_complete_timeline |
| `Action_None` | 553 | 556 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–480
- **Visible Samples:** 481

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 480 | 473 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 73 | 81 | 9 | inferred_complete_timeline |
| `Action_None` | 83 | 87 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 73 | 88 | 16 | inferred_complete_timeline |
| `Action_None` | 93 | 126 | 34 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 552

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 73 | 89 | 17 | inferred_complete_timeline |
| `Action_None` | 91 | 183 | 93 | inferred_complete_timeline |
| `Action_None` | 185 | 206 | 22 | inferred_complete_timeline |
| `Action_None` | 218 | 495 | 278 | inferred_complete_timeline |
| `Action_None` | 497 | 545 | 49 | inferred_complete_timeline |
| `Action_None` | 547 | 557 | 11 | inferred_complete_timeline |
| `Action_None` | 560 | 569 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 558

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 204 | 197 | inferred_complete_timeline |
| `Action_None` | 206 | 211 | 6 | inferred_complete_timeline |
| `Action_None` | 217 | 279 | 63 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |
| `Action_None` | 289 | 569 | 281 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 560

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 125 | 118 | inferred_complete_timeline |
| `Action_None` | 129 | 148 | 20 | inferred_complete_timeline |
| `Action_None` | 156 | 569 | 414 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker6 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–418
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 409 | 402 | inferred_complete_timeline |
| `Action_None` | 411 | 418 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_None` | 105 | 276 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 534

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 523 | 516 | inferred_complete_timeline |
| `Action_None` | 560 | 569 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 36–37 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 78–569 | 449 | 12 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 80–569 | 454 | 10 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 83–569 | 467 | 4 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 101–569 | 458 | 5 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 103–569 | 424 | 4 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 108–569 | 437 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 111–569 | 451 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 112–569 | 452 | 8 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 113–306 | 177 | 3 | Undefined position; Undefined team |
| `27` | `40` | Position_Unknown | Team_Unknown | 131–160 | 20 | 4 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 137–569 | 422 | 2 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 137–241 | 92 | 5 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 158–285 | 113 | 5 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 164–177 | 10 | 3 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 242–476 | 221 | 5 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 273–525 | 241 | 6 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 297–568 | 264 | 2 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 310–467 | 157 | 2 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 422–569 | 118 | 5 | Undefined position; Undefined team |
| `37` | `51` | Position_Unknown | Team_Unknown | 423–425 | 3 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 514–516 | 3 | 1 | Undefined position; Undefined team |
| `39` | `57` | Position_Unknown | Team_Unknown | 514–537 | 22 | 2 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 521–535 | 8 | 2 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 523–525 | 3 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 524–567 | 4 | 2 | Undefined position; Undefined team |
| `43` | `61` | Position_Unknown | Team_Unknown | 551–552 | 2 | 1 | Undefined position; Undefined team |
| `44` | `62` | Position_Unknown | Team_Unknown | 556–569 | 14 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 561–569 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `8` (3 segments found)
- ❌ Missing segment for action `Action_KickBall` on target `8` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `35` (3 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `35` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker6` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 161 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [8-523] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-569] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-480] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-409] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-418] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-442] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-449] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-480] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-506] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-523] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-537] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-547] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-556] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-279] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-469] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-480] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-511] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [518-521] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-531] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-569] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-102] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-276] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-148] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [8-24] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [32-33] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [46-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-115] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-497] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-520] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-541] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-40] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-89] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-495] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-545] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-557] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-37] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-72] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-81] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-35] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-108] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-140] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-544] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [554-569] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-266] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-417] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-420] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-435] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-451] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-460] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-94] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-241] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-413] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-422] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-544] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-553] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-303] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-497] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-500] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-244] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-526] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [547-556] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-490] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [209-252] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-495] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [497-552] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [553-557] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-122] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-140] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-160] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-144] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-569] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-238] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-258] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-272] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-285] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-177] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-292] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-449] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-460] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-464] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-476] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-433] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-447] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-499] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-512] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-519] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-324] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-568] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-453] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-467] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-503] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-526] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-541] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-425] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-525] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-537] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-525] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-535] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-525] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-525] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [566-567] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-552] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-567] for track '45' has 1 frames without a visible bounding box.
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

</details>