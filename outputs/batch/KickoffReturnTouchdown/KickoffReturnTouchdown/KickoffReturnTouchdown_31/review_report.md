# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_31`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 62
- **Ball Tracks:** 0
- **Action Segments:** 217
- **Validation Warnings:** 291
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 2
- **Group Expanded Events:** 4
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 208
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `39` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `39` | `31` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `39` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage5 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `5` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `8` | `Group` | 0 | START | 0 | 14 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `5` | `5` | 15 | START | 15 | 38 |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `5` | `5` | 66 | START | N/A | N/A |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `39` | `31` | 184 | START | 184 | 192 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `39` | `31` | 210 | START | 210 | 584 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrossGoalLine` | Position_Unknown | `39` | `31` | 585 | START | 585 | 593 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_KickApproach` | 15 | 38 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage5 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–8
- **Visible Samples:** 4

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 8 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 107 | 93 | inferred_complete_timeline |
| `Action_None` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 310 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–458
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 458 | 444 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 75 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–531
- **Visible Samples:** 494

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 82 | 68 | inferred_complete_timeline |
| `Action_None` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_None` | 90 | 391 | 302 | inferred_complete_timeline |
| `Action_None` | 401 | 464 | 64 | inferred_complete_timeline |
| `Action_None` | 476 | 498 | 23 | inferred_complete_timeline |
| `Action_None` | 503 | 511 | 9 | inferred_complete_timeline |
| `Action_None` | 521 | 528 | 8 | inferred_complete_timeline |
| `Action_None` | 530 | 531 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 48

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 45 | 31 | inferred_complete_timeline |
| `Action_None` | 81 | 82 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–593
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 80 | 66 | inferred_complete_timeline |
| `Action_None` | 83 | 111 | 29 | inferred_complete_timeline |
| `Action_None` | 113 | 581 | 469 | inferred_complete_timeline |
| `Action_None` | 583 | 593 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 464 | 450 | inferred_complete_timeline |
| `Action_None` | 466 | 532 | 67 | inferred_complete_timeline |
| `Action_None` | 534 | 535 | 2 | inferred_complete_timeline |
| `Action_None` | 543 | 544 | 2 | inferred_complete_timeline |
| `Action_None` | 562 | 563 | 2 | inferred_complete_timeline |
| `Action_None` | 569 | 575 | 7 | inferred_complete_timeline |
| `Action_None` | 579 | 581 | 3 | inferred_complete_timeline |
| `Action_None` | 588 | 591 | 4 | inferred_complete_timeline |
| `Action_None` | 593 | 599 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Kick_Returner2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–598
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 250 | 236 | inferred_complete_timeline |
| `Action_None` | 253 | 598 | 346 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 52 | 53 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 62 | 3 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 107 | 111 | 5 | inferred_complete_timeline |
| `Action_None` | 116 | 120 | 5 | inferred_complete_timeline |
| `Action_None` | 124 | 207 | 84 | inferred_complete_timeline |
| `Action_None` | 209 | 220 | 12 | inferred_complete_timeline |
| `Action_None` | 242 | 599 | 358 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–232
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 212 | 198 | inferred_complete_timeline |
| `Action_None` | 216 | 232 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–87
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 72 | 58 | inferred_complete_timeline |
| `Action_None` | 81 | 87 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_None` | 15 | 84 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–305 | 296 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 10–48 | 20 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 12–13 | 2 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 29–59 | 21 | 3 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 58–599 | 435 | 7 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 71–72 | 2 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 87–599 | 462 | 11 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 95–599 | 499 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 98–101 | 4 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 101–599 | 496 | 3 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 105–599 | 494 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 106–208 | 102 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 122–382 | 257 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 122–124 | 3 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 127–271 | 143 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 129–599 | 450 | 7 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 129–555 | 418 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 133–599 | 466 | 7 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 136–467 | 320 | 6 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 186–188 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 194–464 | 264 | 3 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 222–511 | 274 | 4 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 243–599 | 356 | 2 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 261–532 | 223 | 9 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 311–599 | 287 | 2 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 317–599 | 281 | 3 | Undefined position; Undefined team |
| `41` | `58` | Position_Unknown | Team_Unknown | 356–399 | 30 | 7 | Undefined position; Undefined team |
| `42` | `59` | Position_Unknown | Team_Unknown | 369–372 | 4 | 1 | Undefined position; Undefined team |
| `43` | `60` | Position_Unknown | Team_Unknown | 389–390 | 2 | 1 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 394–531 | 133 | 3 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 400–401 | 2 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 408–517 | 66 | 6 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 421–423 | 3 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 421–586 | 86 | 16 | Undefined position; Undefined team |
| `49` | `74` | Position_Unknown | Team_Unknown | 443–487 | 7 | 3 | Undefined position; Undefined team |
| `50` | `78` | Position_Unknown | Team_Unknown | 456–599 | 140 | 5 | Undefined position; Undefined team |
| `51` | `84` | Position_Unknown | Team_Unknown | 494–515 | 5 | 2 | Undefined position; Undefined team |
| `52` | `85` | Position_Unknown | Team_Unknown | 505–599 | 95 | 1 | Undefined position; Undefined team |
| `53` | `90` | Position_Unknown | Team_Unknown | 538–546 | 5 | 2 | Undefined position; Undefined team |
| `54` | `92` | Position_Unknown | Team_Unknown | 541–568 | 28 | 1 | Undefined position; Undefined team |
| `55` | `95` | Position_Unknown | Team_Unknown | 565–566 | 2 | 1 | Undefined position; Undefined team |
| `56` | `96` | Position_Unknown | Team_Unknown | 570–589 | 12 | 4 | Undefined position; Undefined team |
| `57` | `97` | Position_Unknown | Team_Unknown | 574–575 | 2 | 1 | Undefined position; Undefined team |
| `58` | `98` | Position_Unknown | Team_Unknown | 577–590 | 9 | 2 | Undefined position; Undefined team |
| `59` | `100` | Position_Unknown | Team_Unknown | 588–599 | 12 | 1 | Undefined position; Undefined team |
| `60` | `103` | Position_Unknown | Team_Unknown | 597–599 | 3 | 1 | Undefined position; Undefined team |
| `61` | `104` | Position_Unknown | Team_Unknown | 598–599 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `5` (Kicker)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `39` (2 segments found)
- ⚠️ Ambiguous match for action `Action_CrossGoalLine` and target `39` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kick_Returner2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Second_Level_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Second_Level_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Second_Level_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage5` position mapped to `offense` team
- ⚠️ 48 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 48 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 96 |
| Missing visible bounding boxes during action | 192 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 64: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '5' has invalid range: start=66, end=38. Clamping end to start.
- ⚠️ Action 'Action_None' range [15-260] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-305] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-598] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-464] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-532] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-535] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-575] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-581] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-591] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-599] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-107] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-116] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-310] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickApproach' range [15-38] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-82] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-391] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-464] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-498] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-511] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-528] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-111] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-581] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [583-593] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-458] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-75] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-84] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-72] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-87] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-62] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-207] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-45] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-13] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-22] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-30] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-45] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-85] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-116] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-399] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-599] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-124] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-549] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-563] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-572] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-581] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-592] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [595-599] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-381] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-391] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-397] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-255] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-294] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-599] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-599] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-382] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-242] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-271] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-266] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-281] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-383] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-207] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-450] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-555] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [585-593] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-163] for track '32' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-217] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-467] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-464] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-448] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-498] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-502] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-258] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-378] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-386] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-443] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [449-451] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [455-457] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-500] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-517] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-532] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-391] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-599] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-577] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [579-581] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-363] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-377] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-383] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-390] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-454] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-531] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-424] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-440] for track '46' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-473] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [475-491] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-507] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-517] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-427] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-431] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-438] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-446] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-467] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-470] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-477] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-487] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-511] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [551-557] for track '48' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-577] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-586] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-459] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-477] for track '50' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-480] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-493] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-599] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-515] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-599] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-540] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-568] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-566] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-575] for track '56' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-578] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [580-581] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-575] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-582] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-590] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [598-599] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.

</details>