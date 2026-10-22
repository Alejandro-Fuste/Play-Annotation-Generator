# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_2`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 71
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Left_Edge_Rusher | defense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `20` | `18` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `20` | `18` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `20` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `3` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 54 |
| ✅ EXACT | `Action_LongSnap` | Left_Edge_Rusher | `10` | `10` | 55 | START | 55 | 112 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 85 | END | 85 | 85 |
| ✅ EXACT | `Action_PuntBall` | Punter | `5` | `5` | 113 | START | 113 | 123 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `20` | `18` | 247 | START | 247 | 258 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `20` | `18` | 262 | START | 262 | 599 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `20` | `18` | 605 | START | N/A | N/A |

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
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 599 | 545 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 342 | 288 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–387
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 387 | 333 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 580

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 240 | 186 | inferred_complete_timeline |
| `Action_None` | 247 | 276 | 30 | inferred_complete_timeline |
| `Action_None` | 278 | 579 | 302 | inferred_complete_timeline |
| `Action_None` | 590 | 595 | 6 | inferred_complete_timeline |
| `Action_None` | 599 | 599 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–531
- **Visible Samples:** 515

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 381 | 327 | inferred_complete_timeline |
| `Action_None` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_None` | 393 | 396 | 4 | inferred_complete_timeline |
| `Action_None` | 399 | 401 | 3 | inferred_complete_timeline |
| `Action_None` | 406 | 435 | 30 | inferred_complete_timeline |
| `Action_None` | 439 | 531 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 85 | 1 | inferred_complete_timeline |
| `Action_None` | 86 | 112 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 113 | 123 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 599 | 476 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 472 | 418 | inferred_complete_timeline |
| `Action_None` | 474 | 599 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–344
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 344 | 290 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 597

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 95 | 41 | inferred_complete_timeline |
| `Action_None` | 99 | 599 | 501 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 599 | 545 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 600

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 599 | 545 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 376 | 322 | inferred_complete_timeline |
| `Action_None` | 378 | 599 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 590

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_LongSnap` | 55 | 112 | 58 | inferred_complete_timeline |
| `Action_None` | 113 | 565 | 453 | inferred_complete_timeline |
| `Action_None` | 576 | 599 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 599

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 497 | 443 | inferred_complete_timeline |
| `Action_None` | 499 | 599 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 108 | 54 | inferred_complete_timeline |
| `Action_None` | 112 | 556 | 445 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 111–470 | 360 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 123–599 | 474 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 160–599 | 440 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 165–599 | 435 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 166–599 | 395 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 174–592 | 412 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 180–599 | 420 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 347–599 | 253 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 354–599 | 245 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 354–374 | 5 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 366–367 | 2 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 427–599 | 172 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 467–489 | 22 | 2 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 473–489 | 17 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 476–477 | 2 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 498–500 | 3 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 591–599 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_CrossGoalLine` on target `20` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 4 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '18' has invalid range: start=605, end=599. Clamping end to start.
- ⚠️ Action 'Action_None' range [55-387] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-344] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-240] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-579] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-595] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-381] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-396] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-401] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-435] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-531] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-599] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-472] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-342] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-565] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-497] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-108] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-556] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-95] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-376] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-470] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [262-599] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-544] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [559-571] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-597] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-203] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-592] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-599] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-525] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-595] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-468] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-489] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-489] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-500] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [591-595] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Action event 'Action_CrossGoalLine' has invalid start frame 605. Video range is [0, 599].
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>