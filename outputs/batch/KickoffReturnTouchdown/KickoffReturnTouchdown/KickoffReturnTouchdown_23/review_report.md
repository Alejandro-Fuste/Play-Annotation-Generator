# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_23

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_23`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 145
- **Validation Warnings:** 159
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 121
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `6` | `Group` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `21` | `21` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `10` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `11` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `14` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `16` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `17` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `18` | `Group` | 0 | START | 0 | 10 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `5` | `Group` | 0 | START | 0 | 109 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `6` | `Group` | 0 | START | 0 | 109 |
| ✅ EXACT | `Action_KickBall` | Kicker | `16` | `16` | 75 | START | 75 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_KickApproach` | Kicker | `16` | `16` | 110 | START | 110 | 411 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `21` | `21` | 174 | START | 174 | 189 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `21` | `21` | 199 | START | 199 | 556 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `21` | `21` | 557 | START | 557 | 569 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 549

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 74 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 75 | 78 | 4 | inferred_complete_timeline |
| `Action_None` | 79 | 88 | 10 | inferred_complete_timeline |
| `Action_None` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_KickApproach` | 110 | 411 | 302 | inferred_complete_timeline |
| `Action_KickApproach` | 413 | 569 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–10
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 58 | 85 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 121 | 6 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |
| `Action_None` | 128 | 143 | 16 | inferred_complete_timeline |
| `Action_None` | 145 | 411 | 267 | inferred_complete_timeline |
| `Action_None` | 413 | 504 | 92 | inferred_complete_timeline |
| `Action_None` | 506 | 569 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 63

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 16 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 50 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 83 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 220 | 111 | inferred_complete_timeline |
| `Action_None` | 246 | 329 | 84 | inferred_complete_timeline |
| `Action_None` | 331 | 334 | 4 | inferred_complete_timeline |
| `Action_None` | 340 | 569 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 553

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 540 | 431 | inferred_complete_timeline |
| `Action_None` | 542 | 543 | 2 | inferred_complete_timeline |
| `Action_None` | 560 | 569 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 125 | 16 | inferred_complete_timeline |
| `Action_None` | 127 | 138 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 569 | 430 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–424
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 424 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–465
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 450 | 341 | inferred_complete_timeline |
| `Action_None` | 452 | 465 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 199 | 90 | inferred_complete_timeline |
| `Action_None` | 223 | 230 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 336 | 227 | inferred_complete_timeline |
| `Action_None` | 350 | 351 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–537
- **Visible Samples:** 531

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 105 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 537 | 428 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 569 | 460 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 569 | 460 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 272 | 163 | inferred_complete_timeline |
| `Action_None` | 275 | 569 | 295 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 333 | 224 | inferred_complete_timeline |
| `Action_None` | 335 | 569 | 235 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 224 | 115 | inferred_complete_timeline |
| `Action_None` | 229 | 332 | 104 | inferred_complete_timeline |
| `Action_None` | 340 | 345 | 6 | inferred_complete_timeline |
| `Action_None` | 351 | 354 | 4 | inferred_complete_timeline |
| `Action_None` | 372 | 446 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 569 | 460 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 109 | 110 | inferred_complete_timeline |
| `Action_None` | 110 | 509 | 400 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 5–8 | 4 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 84–569 | 485 | 6 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 105–569 | 460 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 106–249 | 142 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 108–317 | 179 | 9 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 119–123 | 5 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 129–169 | 37 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 149–214 | 59 | 4 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 217–569 | 350 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 252–569 | 314 | 5 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 256–498 | 242 | 2 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 364–461 | 73 | 6 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 369–512 | 144 | 1 | Undefined position; Undefined team |
| `33` | `53` | Position_Unknown | Team_Unknown | 396–521 | 66 | 14 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 429–430 | 2 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 438–447 | 10 | 1 | Undefined position; Undefined team |
| `36` | `59` | Position_Unknown | Team_Unknown | 482–483 | 2 | 1 | Undefined position; Undefined team |
| `37` | `61` | Position_Unknown | Team_Unknown | 488–491 | 4 | 1 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 543–545 | 3 | 1 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 559–569 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_KickApproach` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 118 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action 'Action_None' range [110-333] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-509] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-569] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-332] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-345] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-354] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-446] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-336] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-138] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-569] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-220] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-334] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-569] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-569] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-199] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-109] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-272] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-450] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-465] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-424] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-537] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-143] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-411] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-504] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-569] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [110-411] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [413-569] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-540] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [542-543] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-16] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-50] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-83] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-305] for track '22' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-478] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-569] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-242] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-153] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-288] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-300] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-136] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-153] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-264] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-563] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-467] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-476] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-481] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-484] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-569] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-498] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-396] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-409] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-428] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-439] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-461] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-512] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-407] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-411] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-422] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-425] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-436] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-440] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-451] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-465] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [478-487] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-496] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-515] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [519-521] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-447] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-491] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-545] for track '38' has 1 frames without a visible bounding box.
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

</details>