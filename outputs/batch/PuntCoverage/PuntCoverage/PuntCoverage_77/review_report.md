# Play-Annotation-Generator Annotation Review — PuntCoverage_77

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_77`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 449
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 142
- **Validation Warnings:** 206
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 1
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 112
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `40` | `32` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `40` | `32` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Right_Guard | offense | `7` | `7` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 129 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `1` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `2` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_PuntBall` | Punter | `4` | `4` | 71 | START | 71 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_CatchPunt` | Position_Unknown | `40` | `32` | 207 | START | 207 | 207 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `40` | `32` | 225 | START | 225 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Right_Guard | `7` | `7` | 400 | START | 400 | 415 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–276
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 32 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 41 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 146 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 162 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 276 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–412
- **Visible Samples:** 403

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 224 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 412 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 129 | 130 | inferred_complete_timeline |
| `Action_PreSnap` | 133 | 161 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 449 | 287 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 397 | 367 | inferred_complete_timeline |
| `Action_PreSnap` | 400 | 449 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PuntBall` | 71 | 86 | 16 | inferred_complete_timeline |
| `Action_None` | 87 | 233 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–425
- **Visible Samples:** 408

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 265 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 267 | 399 | 133 | inferred_complete_timeline |
| `Action_Tackle` | 400 | 415 | 16 | inferred_complete_timeline |
| `Action_Tackle` | 420 | 425 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–435
- **Visible Samples:** 425

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 171 | 145 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 418 | 246 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 425 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 431 | 435 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–41
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 38 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 41 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 449 | 415 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 374 | 375 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–403
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 403 | 404 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 113 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 391 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 394 | 449 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–397 | 388 | 3 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 5–38 | 24 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 12–449 | 419 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 36–76 | 39 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 47–449 | 394 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 49–234 | 178 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 52–449 | 374 | 5 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 52–419 | 363 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 60–70 | 10 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 69–189 | 120 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 70–312 | 235 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 75–200 | 126 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 92–291 | 166 | 5 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 104–110 | 7 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 130–175 | 16 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 144–158 | 9 | 2 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 204–449 | 232 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 206–244 | 35 | 6 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 216–220 | 5 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 242–449 | 198 | 4 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 249–449 | 190 | 3 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 251–252 | 2 | 1 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 261–387 | 124 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 287–449 | 162 | 2 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 301–380 | 71 | 4 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 303–361 | 55 | 3 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 321–449 | 124 | 2 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 377–449 | 71 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 393–449 | 55 | 2 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 397–447 | 46 | 2 | Undefined position; Undefined team |
| `45` | `60` | Position_Unknown | Team_Unknown | 398–400 | 3 | 1 | Undefined position; Undefined team |
| `46` | `62` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `47` | `63` | Position_Unknown | Team_Unknown | 411–422 | 12 | 1 | Undefined position; Undefined team |
| `48` | `65` | Position_Unknown | Team_Unknown | 412–449 | 37 | 2 | Undefined position; Undefined team |
| `49` | `67` | Position_Unknown | Team_Unknown | 429–449 | 16 | 4 | Undefined position; Undefined team |
| `50` | `70` | Position_Unknown | Team_Unknown | 440–448 | 5 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CatchPunt` and target `40` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `40` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ 37 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 37 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 74 |
| Missing visible bounding boxes during action | 131 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-161] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-449] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-171] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-418] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-425] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [431-435] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-397] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-449] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-250] for track '3' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-397] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-233] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-374] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-247] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [400-415] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [420-425] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-227] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-412] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-113] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-391] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [394-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-41] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-146] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-276] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-449] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-403] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-38] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-25] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-230] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-235] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [250-252] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-67] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-76] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-289] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-370] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-381] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-388] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-135] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-228] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-250] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [334-361] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-449] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-208] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-231] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-275] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-419] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-70] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-163] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-189] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-187] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-203] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-312] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-200] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-250] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-110] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-134] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-160] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-158] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-244] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-297] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-304] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' for track '32' starts at frame 207, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_CatchPunt' range [207-207] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [209-213] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [225-226] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [229-244] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-411] for track '34' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-417] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [419-421] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-394] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-420] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-367] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-383] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [385-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-375] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-449] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-351] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [358-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [361-365] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [368-380] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-347] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [350-354] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [321-329] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-449] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [377-411] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-449] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [393-403] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [397-407] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [413-447] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [398-400] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [408-409] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-422] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [412-418] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-449] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [429-433] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [436-437] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [439-445] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-442] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [447-448] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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

</details>