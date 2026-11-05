# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_51`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `12` | `12` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `0` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `12` | `Group` | 0 | START | 0 | 90 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `14` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `19` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `3` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `8` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `9` | `Group` | 0 | START | 0 | 61 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 62 | START | 62 | 111 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `12` | `12` | 91 | END | 91 | 91 |
| ✅ EXACT | `Action_PuntBall` | Punter | `12` | `12` | 112 | START | 112 | 124 |

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
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 180 | 119 | inferred_complete_timeline |
| `Action_None` | 182 | 300 | 119 | inferred_complete_timeline |
| `Action_None` | 305 | 307 | 3 | inferred_complete_timeline |
| `Action_None` | 309 | 312 | 4 | inferred_complete_timeline |
| `Action_None` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 214 | 153 | inferred_complete_timeline |
| `Action_None` | 216 | 329 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 212 | 151 | inferred_complete_timeline |
| `Action_None` | 220 | 250 | 31 | inferred_complete_timeline |
| `Action_None` | 252 | 257 | 6 | inferred_complete_timeline |
| `Action_None` | 259 | 262 | 4 | inferred_complete_timeline |
| `Action_None` | 264 | 266 | 3 | inferred_complete_timeline |
| `Action_None` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 287 | 4 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–320
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_LongSnap` | 62 | 111 | 50 | inferred_complete_timeline |
| `Action_None` | 112 | 320 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 181 | 120 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 91 | 91 | 1 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 125 | 171 | 47 | inferred_complete_timeline |
| `Action_None` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 292 | 231 | inferred_complete_timeline |
| `Action_None` | 296 | 299 | 4 | inferred_complete_timeline |
| `Action_None` | 305 | 329 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 122 | 61 | inferred_complete_timeline |
| `Action_None` | 127 | 329 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 259 | 198 | inferred_complete_timeline |
| `Action_None` | 261 | 287 | 27 | inferred_complete_timeline |
| `Action_None` | 289 | 294 | 6 | inferred_complete_timeline |
| `Action_None` | 297 | 329 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 121 | 60 | inferred_complete_timeline |
| `Action_None` | 124 | 329 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 114 | 53 | inferred_complete_timeline |
| `Action_None` | 119 | 329 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 94 | 33 | inferred_complete_timeline |
| `Action_None` | 98 | 119 | 22 | inferred_complete_timeline |
| `Action_None` | 171 | 173 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 93 | 32 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 329 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 147 | 86 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 202 | 46 | inferred_complete_timeline |
| `Action_None` | 206 | 213 | 8 | inferred_complete_timeline |
| `Action_None` | 216 | 248 | 33 | inferred_complete_timeline |
| `Action_None` | 250 | 298 | 49 | inferred_complete_timeline |
| `Action_None` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_None` | 62 | 329 | 268 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 38–329 | 289 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 113–124 | 12 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 117–329 | 213 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 131–139 | 9 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 151–152 | 2 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 206–329 | 109 | 3 | Undefined position; Undefined team |
| `27` | `42` | Position_Unknown | Team_Unknown | 212–329 | 115 | 3 | Undefined position; Undefined team |
| `28` | `46` | Position_Unknown | Team_Unknown | 252–262 | 8 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 56 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 104: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [62-122] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-329] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-259] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-287] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-294] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-320] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-94] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-300] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-312] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-147] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-202] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-213] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-248] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-212] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-262] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-266] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-287] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-114] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-291] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-152] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-274] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-329] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '28' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>