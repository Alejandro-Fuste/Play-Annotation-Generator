# Play-Annotation-Generator Annotation Review — KickoffReturnTouchdown_92

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `KickoffReturnTouchdown_92`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_KickoffReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 163
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 147
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | Team_Unknown | `28` | `24` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `28` | `24` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `28` | `24` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `0` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `10` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `11` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `13` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `15` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `16` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `3` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `4` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `7` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `8` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 33 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 34 | START | 34 | 114 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 115 | START | 115 | 120 |
| ✅ EXACT | `Action_CatchKick` | Position_Unknown | `28` | `24` | 224 | START | 224 | 231 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `28` | `24` | 243 | START | 243 | 593 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `28` | `24` | 594 | START | 594 | 599 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_KickApproach` | 34 | 114 | 81 | inferred_complete_timeline |
| `Action_KickBall` | 115 | 120 | 6 | inferred_complete_timeline |
| `Action_None` | 121 | 230 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–98
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 39 | 6 | inferred_complete_timeline |
| `Action_None` | 42 | 51 | 10 | inferred_complete_timeline |
| `Action_None` | 55 | 56 | 2 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 86 | 98 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 39 | 42 | 4 | inferred_complete_timeline |
| `Action_None` | 45 | 49 | 5 | inferred_complete_timeline |
| `Action_None` | 82 | 87 | 6 | inferred_complete_timeline |
| `Action_None` | 92 | 98 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 117 | 131 | 15 | inferred_complete_timeline |
| `Action_None` | 133 | 135 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 578 | 438 | inferred_complete_timeline |
| `Action_None` | 581 | 599 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 599 | 566 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 337 | 304 | inferred_complete_timeline |
| `Action_None` | 339 | 569 | 231 | inferred_complete_timeline |
| `Action_None` | 577 | 587 | 11 | inferred_complete_timeline |
| `Action_None` | 589 | 599 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 506 | 473 | inferred_complete_timeline |
| `Action_None` | 508 | 599 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 486 | 453 | inferred_complete_timeline |
| `Action_None` | 489 | 546 | 58 | inferred_complete_timeline |
| `Action_None` | 554 | 599 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 241 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 572

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 485 | 452 | inferred_complete_timeline |
| `Action_None` | 506 | 508 | 3 | inferred_complete_timeline |
| `Action_None` | 517 | 599 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 599 | 566 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 599 | 566 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Front_Blocker1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 583

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 273 | 240 | inferred_complete_timeline |
| `Action_None` | 277 | 281 | 5 | inferred_complete_timeline |
| `Action_None` | 294 | 339 | 46 | inferred_complete_timeline |
| `Action_None` | 341 | 349 | 9 | inferred_complete_timeline |
| `Action_None` | 351 | 599 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 257 | 224 | inferred_complete_timeline |
| `Action_None` | 268 | 561 | 294 | inferred_complete_timeline |
| `Action_None` | 563 | 599 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–436
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 56 | 23 | inferred_complete_timeline |
| `Action_None` | 61 | 224 | 164 | inferred_complete_timeline |
| `Action_None` | 229 | 250 | 22 | inferred_complete_timeline |
| `Action_None` | 253 | 436 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 230 | 197 | inferred_complete_timeline |
| `Action_None` | 242 | 244 | 3 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 509 | 248 | inferred_complete_timeline |
| `Action_None` | 513 | 599 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Front_Blocker5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 588

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 246 | 213 | inferred_complete_timeline |
| `Action_None` | 248 | 256 | 9 | inferred_complete_timeline |
| `Action_None` | 259 | 437 | 179 | inferred_complete_timeline |
| `Action_None` | 440 | 490 | 51 | inferred_complete_timeline |
| `Action_None` | 492 | 505 | 14 | inferred_complete_timeline |
| `Action_None` | 507 | 549 | 43 | inferred_complete_timeline |
| `Action_None` | 555 | 599 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Second_Level_Blocker1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 34 | 563 | 530 | inferred_complete_timeline |
| `Action_None` | 566 | 599 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 104–181 | 67 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 124–599 | 476 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 173–214 | 38 | 3 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 179–599 | 418 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 182–599 | 395 | 6 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 185–349 | 165 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 186–207 | 19 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 208–599 | 392 | 5 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 214–599 | 361 | 14 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 251–463 | 213 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 252–494 | 235 | 5 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 268–301 | 34 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 333–385 | 45 | 5 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 365–599 | 228 | 2 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 388–599 | 177 | 13 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 408–530 | 44 | 11 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 456–587 | 131 | 2 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 479–498 | 20 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 514–516 | 3 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 522–525 | 4 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 553–555 | 3 | 1 | Undefined position; Undefined team |
| `38` | `50` | Position_Unknown | Team_Unknown | 581–586 | 6 | 1 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 584–586 | 3 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 596–599 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Second_Level_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Front_Blocker4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Front_Blocker5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Front_Blocker1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Front_Blocker3` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Front_Blocker2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 125 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [34-485] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-508] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-563] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-244] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-509] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-246] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-437] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-490] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-505] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-549] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-273] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-281] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-339] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-349] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-241] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-506] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-230] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-337] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [577-587] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-486] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-546] for track '11' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-224] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-436] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-599] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-257] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-561] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-98] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-42] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-87] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-131] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-135] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-578] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-599] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-209] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-506] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-528] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-566] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-589] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [592-597] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-349] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-200] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-207] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-265] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-298] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-435] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-450] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-457] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-491] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-496] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-505] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-517] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-525] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-539] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [541-546] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [549-599] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-463] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-273] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-487] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-494] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-301] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-372] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-382] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-371] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-599] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-397] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-408] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-430] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-465] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-492] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-498] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-519] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-541] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-594] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-413] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-427] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-451] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-455] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-504] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-513] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-517] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-530] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-584] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [586-587] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-498] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-516] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-525] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-555] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-586] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [584-586] for track '39' has 1 frames without a visible bounding box.
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