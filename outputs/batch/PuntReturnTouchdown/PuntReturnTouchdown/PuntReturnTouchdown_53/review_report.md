# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_53

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_53`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 85
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `2` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `2` | `2` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `23` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `23` | `23` |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Wing | offense | `19` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `17` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `18` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `19` | `Group` | 0 | START | 0 | 368 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `2` | `Group` | 0 | START | 0 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 58 | START | 58 | 76 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `2` | `2` | 79 | END | 79 | 79 |
| ✅ EXACT | `Action_PuntBall` | Punter | `2` | `2` | 106 | START | 106 | 117 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `23` | `23` | 174 | START | 174 | 185 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `23` | `23` | 205 | START | 205 | 253 |
| ✅ EXACT | `Action_CrossGoalLine` | Right_Wing | `19` | `19` | 369 | START | 369 | 378 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 79 | 22 | inferred_complete_timeline |
| `Action_None` | 90 | 201 | 112 | inferred_complete_timeline |
| `Action_None` | 207 | 389 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_LongSnap` | 58 | 76 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 81 | 87 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_LongSnap` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 98 | 105 | 8 | inferred_complete_timeline |
| `Action_None` | 106 | 389 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 78 | 79 | inferred_complete_timeline |
| `Action_SnapReceive` | 79 | 79 | 1 | inferred_complete_timeline |
| `Action_None` | 80 | 105 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 106 | 117 | 12 | inferred_complete_timeline |
| `Action_None` | 118 | 154 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 75 | 389 | 315 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 389

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 368 | 369 | inferred_complete_timeline |
| `Action_CrossGoalLine` | 369 | 378 | 10 | inferred_complete_timeline |
| `Action_None` | 379 | 383 | 5 | inferred_complete_timeline |
| `Action_None` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 168 | 111 | inferred_complete_timeline |
| `Action_None` | 171 | 186 | 16 | inferred_complete_timeline |
| `Action_None` | 190 | 198 | 9 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_None` | 211 | 389 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–221
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 207 | 150 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 216 | 221 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 287 | 230 | inferred_complete_timeline |
| `Action_None` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 177 | 120 | inferred_complete_timeline |
| `Action_None` | 182 | 389 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 311 | 254 | inferred_complete_timeline |
| `Action_None` | 337 | 389 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 389 | 332 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_None` | 58 | 155 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–389 | 390 | 2 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–204 | 190 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 67–389 | 282 | 7 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 83–85 | 3 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 92–95 | 4 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 170–359 | 187 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 184–186 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 188–389 | 191 | 5 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 191–389 | 192 | 3 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 223–389 | 165 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 231–389 | 159 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 352–353 | 2 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 363–365 | 3 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 370–389 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `23` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Wing` position mapped to `offense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 107: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [58-177] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-154] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-186] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-389] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-207] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-221] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-311] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-287] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-389] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-155] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-187] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [58-76] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [81-87] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [90-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-368] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-383] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-75] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [205-253] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [255-279] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-359] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-273] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-197] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-376] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-353] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-365] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-377] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-389] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>