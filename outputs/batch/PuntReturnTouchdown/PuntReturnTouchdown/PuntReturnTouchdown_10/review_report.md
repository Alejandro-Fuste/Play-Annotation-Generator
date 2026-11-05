# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_10

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_10`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 599
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 119
- **Validation Warnings:** 174
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 107
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `49` | `33` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `49` | `33` |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `49` | `33` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `11` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `3` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `5` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 66 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 38 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `8` | `8` | 39 | START | 39 | 93 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 67 | END | 67 | 67 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 94 | START | 94 | 104 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `49` | `33` | 214 | START | 214 | 220 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `49` | `33` | 233 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_CrossGoalLine` | Position_Unknown | `49` | `33` | 590 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–447
- **Visible Samples:** 430

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 162 | 124 | inferred_complete_timeline |
| `Action_None` | 181 | 447 | 267 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–407
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 403 | 365 | inferred_complete_timeline |
| `Action_None` | 405 | 407 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_LongSnap` | 39 | 93 | 55 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 99 | 161 | 63 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–271
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 271 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 409

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 408 | 370 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–362
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 156 | 118 | inferred_complete_timeline |
| `Action_None` | 158 | 321 | 164 | inferred_complete_timeline |
| `Action_None` | 326 | 362 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_SnapReceive` | 67 | 67 | 1 | inferred_complete_timeline |
| `Action_None` | 68 | 93 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 94 | 104 | 11 | inferred_complete_timeline |
| `Action_None` | 105 | 112 | 8 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–409
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 189 | 151 | inferred_complete_timeline |
| `Action_None` | 207 | 224 | 18 | inferred_complete_timeline |
| `Action_None` | 226 | 335 | 110 | inferred_complete_timeline |
| `Action_None` | 338 | 409 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–446
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 80 | 42 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 88 | 446 | 359 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–396
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 66 | 28 | inferred_complete_timeline |
| `Action_None` | 68 | 396 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 198 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 91 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–421
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 117 | 79 | inferred_complete_timeline |
| `Action_None` | 121 | 421 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 147 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 403 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_None` | 39 | 60 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 51–78 | 28 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 88–599 | 510 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 98–148 | 51 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 101–447 | 347 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 116–180 | 65 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 125–245 | 117 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 141–197 | 57 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 144–162 | 19 | 1 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 155–156 | 2 | 1 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 158–599 | 435 | 3 | Undefined position; Undefined team |
| `29` | `45` | Position_Unknown | Team_Unknown | 163–596 | 429 | 4 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 163–227 | 59 | 4 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 164–528 | 359 | 4 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 164–399 | 226 | 7 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 169–231 | 58 | 5 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 175–200 | 7 | 3 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 179–454 | 270 | 2 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 194–195 | 2 | 1 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 205–275 | 71 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 221–404 | 184 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 244–422 | 148 | 3 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 258–444 | 183 | 2 | Undefined position; Undefined team |
| `41` | `61` | Position_Unknown | Team_Unknown | 352–490 | 139 | 1 | Undefined position; Undefined team |
| `42` | `62` | Position_Unknown | Team_Unknown | 356–493 | 138 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 371–377 | 7 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 371–566 | 196 | 1 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 380–395 | 16 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 396–599 | 204 | 1 | Undefined position; Undefined team |
| `47` | `73` | Position_Unknown | Team_Unknown | 552–599 | 48 | 1 | Undefined position; Undefined team |
| `48` | `75` | Position_Unknown | Team_Unknown | 572–579 | 8 | 1 | Undefined position; Undefined team |
| `49` | `76` | Position_Unknown | Team_Unknown | 585–594 | 10 | 1 | Undefined position; Undefined team |
| `50` | `77` | Position_Unknown | Team_Unknown | 585–586 | 2 | 1 | Undefined position; Undefined team |
| `51` | `78` | Position_Unknown | Team_Unknown | 590–591 | 2 | 1 | Undefined position; Undefined team |
| `52` | `80` | Position_Unknown | Team_Unknown | 593–596 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallCarry` on target `49` (Position_Unknown)
- ❌ Missing segment for action `Action_CrossGoalLine` on target `49` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Jammer1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Jammer2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Jammer` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 95 |
| Track-related warning | 2 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_BallCarry' for track '33' has invalid range: start=233, end=231. Clamping end to start.
- ⚠️ Segment 'Action_CrossGoalLine' for track '33' has invalid range: start=590, end=231. Clamping end to start.
- ⚠️ Action 'Action_None' range [39-271] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-147] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-162] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-447] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-321] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-362] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-408] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-403] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-407] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-421] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-161] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-80] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-446] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-66] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-396] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-189] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-224] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-335] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-409] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-403] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-198] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-60] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-91] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-224] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-599] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-447] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-179] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-194] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-240] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-197] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-162] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-233] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-594] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [596-599] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-272] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-572] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [574-576] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-596] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-186] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-207] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-227] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-200] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-411] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-528] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-169] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-178] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-299] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-310] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-399] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-182] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-231] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-345] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-454] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-404] for track '38' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-334] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-391] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-311] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-444] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-490] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-493] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-377] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-566] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-395] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [572-579] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-594] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [585-586] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [590-591] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-596] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>