# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_48

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_48`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 136
- **Validation Warnings:** 167
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 5
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Position_Unknown | Team_Unknown | `12` | `11` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `23` | `19` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `23` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `10` | `Group` | 2 | START | 2 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `5` | `Group` | 2 | START | 2 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 2 | START | 2 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 2 | START | 2 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 2 | START | 2 | 32 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `8` | `8` | 33 | START | 33 | 91 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `12` | `11` | 68 | END | 68 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Position_Unknown | `12` | `11` | 92 | START | 92 | 96 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `23` | `19` | 223 | START | 223 | 232 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `23` | `19` | 245 | START | 245 | 529 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `23` | `19` | 530 | START | 530 | 539 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 2–206
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 77 | 45 | inferred_complete_timeline |
| `Action_None` | 79 | 196 | 118 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 2–236
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_LongSnap` | 33 | 91 | 59 | inferred_complete_timeline |
| `Action_None` | 92 | 197 | 106 | inferred_complete_timeline |
| `Action_None` | 216 | 221 | 6 | inferred_complete_timeline |
| `Action_None` | 223 | 224 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 236 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 235 | 203 | inferred_complete_timeline |
| `Action_None` | 237 | 482 | 246 | inferred_complete_timeline |
| `Action_None` | 486 | 487 | 2 | inferred_complete_timeline |
| `Action_None` | 489 | 503 | 15 | inferred_complete_timeline |
| `Action_None` | 505 | 506 | 2 | inferred_complete_timeline |
| `Action_None` | 510 | 511 | 2 | inferred_complete_timeline |
| `Action_None` | 513 | 518 | 6 | inferred_complete_timeline |
| `Action_None` | 521 | 527 | 7 | inferred_complete_timeline |
| `Action_None` | 533 | 539 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 370 | 338 | inferred_complete_timeline |
| `Action_None` | 379 | 465 | 87 | inferred_complete_timeline |
| `Action_None` | 468 | 539 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 2–539
- **Visible Samples:** 518

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 5 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 32 | 25 | inferred_complete_timeline |
| `Action_None` | 33 | 245 | 213 | inferred_complete_timeline |
| `Action_None` | 250 | 251 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 262 | 5 | inferred_complete_timeline |
| `Action_None` | 264 | 378 | 115 | inferred_complete_timeline |
| `Action_None` | 382 | 384 | 3 | inferred_complete_timeline |
| `Action_None` | 386 | 388 | 3 | inferred_complete_timeline |
| `Action_None` | 392 | 539 | 148 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 2–488
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 147 | 115 | inferred_complete_timeline |
| `Action_None` | 167 | 417 | 251 | inferred_complete_timeline |
| `Action_None` | 423 | 468 | 46 | inferred_complete_timeline |
| `Action_None` | 470 | 479 | 10 | inferred_complete_timeline |
| `Action_None` | 483 | 488 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 535

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 103 | 71 | inferred_complete_timeline |
| `Action_None` | 107 | 539 | 433 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 2–400
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 247 | 215 | inferred_complete_timeline |
| `Action_None` | 250 | 282 | 33 | inferred_complete_timeline |
| `Action_None` | 284 | 344 | 61 | inferred_complete_timeline |
| `Action_None` | 348 | 400 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 2–448
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 448 | 416 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 539 | 507 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 2–539
- **Visible Samples:** 538

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 32 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 539 | 507 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 28–402 | 322 | 13 | Undefined position; Undefined team |
| `12` | `13` | Position_Unknown | Team_Unknown | 54–114 | 31 | 2 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 113–539 | 426 | 2 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 132–269 | 133 | 3 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 134–326 | 192 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 138–319 | 155 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 139–539 | 399 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 157–539 | 383 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 159–539 | 381 | 5 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 170–539 | 352 | 6 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 173–539 | 367 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 193–539 | 337 | 7 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 224–235 | 8 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 238–405 | 167 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 265–266 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 279–539 | 260 | 2 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 281–290 | 8 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 292–347 | 46 | 4 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 312–322 | 8 | 2 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 328–539 | 192 | 4 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 341–380 | 40 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 409–539 | 113 | 2 | Undefined position; Undefined team |
| `34` | `52` | Position_Unknown | Team_Unknown | 491–506 | 16 | 1 | Undefined position; Undefined team |
| `35` | `55` | Position_Unknown | Team_Unknown | 498–539 | 42 | 1 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 504–539 | 31 | 4 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 506–534 | 24 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 521–539 | 13 | 3 | Undefined position; Undefined team |
| `39` | `60` | Position_Unknown | Team_Unknown | 523–539 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Guard` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 106 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [33-147] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-417] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-468] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-479] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-488] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-282] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-400] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-448] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-235] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-482] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-503] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-506] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-511] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-518] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-527] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-77] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-539] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-197] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-236] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-370] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-465] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-539] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-5] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-245] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-378] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-388] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [92-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-114] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-125] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-287] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-402] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-418] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-539] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-264] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-293] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-326] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-282] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-292] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-246] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-539] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-539] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-355] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-369] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-375] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-443] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-539] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-298] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-539] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-314] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-405] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-320] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-347] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-353] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-496] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-380] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-428] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-506] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [504-505] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [507-509] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [511-512] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-539] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-525] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-523] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-532] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-533] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-539] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>