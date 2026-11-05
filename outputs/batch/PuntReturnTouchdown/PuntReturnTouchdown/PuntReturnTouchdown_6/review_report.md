# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_6`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `22` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `22` | `19` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `22` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `2` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `7` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_LongSnap` | Right_Guard | `8` | `8` | 41 | START | 41 | 94 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `3` | `3` | 67 | END | 67 | 67 |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 95 | START | 95 | 110 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `22` | `19` | 178 | START | 178 | 186 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `22` | `19` | 193 | START | 193 | 228 |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `22` | `19` | 532 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 539 | 499 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 123 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–501
- **Visible Samples:** 475

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 303 | 263 | inferred_complete_timeline |
| `Action_None` | 331 | 501 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–459
- **Visible Samples:** 456

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 136 | 96 | inferred_complete_timeline |
| `Action_None` | 138 | 310 | 173 | inferred_complete_timeline |
| `Action_None` | 314 | 459 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 286 | 246 | inferred_complete_timeline |
| `Action_None` | 290 | 372 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 539 | 499 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–409
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SnapReceive` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_None` | 68 | 94 | 27 | inferred_complete_timeline |
| `Action_PuntBall` | 95 | 110 | 16 | inferred_complete_timeline |
| `Action_None` | 111 | 356 | 246 | inferred_complete_timeline |
| `Action_None` | 363 | 368 | 6 | inferred_complete_timeline |
| `Action_None` | 370 | 409 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_LongSnap` | 41 | 94 | 54 | inferred_complete_timeline |
| `Action_None` | 95 | 258 | 164 | inferred_complete_timeline |
| `Action_None` | 260 | 350 | 91 | inferred_complete_timeline |
| `Action_None` | 355 | 372 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–273
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 273 | 233 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 82 | 4 | inferred_complete_timeline |
| `Action_None` | 86 | 89 | 4 | inferred_complete_timeline |
| `Action_None` | 91 | 131 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_None` | 68 | 103 | 36 | inferred_complete_timeline |
| `Action_None` | 108 | 274 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 42 | 2 | inferred_complete_timeline |
| `Action_None` | 44 | 187 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–281
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 72 | 190 | 119 | inferred_complete_timeline |
| `Action_None` | 192 | 281 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 527

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 225 | 185 | inferred_complete_timeline |
| `Action_None` | 232 | 300 | 69 | inferred_complete_timeline |
| `Action_None` | 304 | 342 | 39 | inferred_complete_timeline |
| `Action_None` | 345 | 363 | 19 | inferred_complete_timeline |
| `Action_None` | 365 | 404 | 40 | inferred_complete_timeline |
| `Action_None` | 406 | 539 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 347 | 307 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 6–97 | 90 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 81–390 | 303 | 5 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 88–483 | 385 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 128–441 | 311 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 142–243 | 99 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 153–370 | 218 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 156–432 | 173 | 7 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 207–222 | 16 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 209–538 | 279 | 13 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 236–259 | 23 | 2 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 245–330 | 85 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 249–314 | 66 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 264–359 | 76 | 5 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 284–539 | 253 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 299–361 | 63 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 307–340 | 34 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 319–402 | 84 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 334–339 | 6 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 352–401 | 50 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 353–390 | 38 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 378–426 | 47 | 2 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 450–460 | 11 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 526–539 | 14 | 1 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 536–537 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `22` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 94 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CrossGoalLine' for track '19' has invalid range: start=532, end=243. Clamping end to start.
- ⚠️ Action 'Action_None' range [41-123] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-310] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-459] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-356] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-368] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-409] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-347] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-303] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-501] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-286] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-372] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-273] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-258] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-350] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-372] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-539] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-225] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-300] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-342] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-363] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-404] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-103] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-274] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-190] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-281] for track '14' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-304] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-309] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-312] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-337] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-390] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-357] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-483] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-425] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-435] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-441] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [232-243] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-370] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-165] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-338] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-432] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-316] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-381] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-395] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-399] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-435] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-443] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-450] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-487] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-494] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-517] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [520-538] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-286] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-330] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-314] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-289] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-307] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-338] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-374] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-539] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-361] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-340] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-402] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-339] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-401] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-390] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-419] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-426] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-460] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '38' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>