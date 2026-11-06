# Play-Annotation-Generator Annotation Review — PuntCoverage_18

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_18`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 40
- **Ball Tracks:** 0
- **Action Segments:** 112
- **Validation Warnings:** 133
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
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 98
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `24` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `24` | `23` |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | Team_Unknown | `32` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `13` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 14 | START | 14 | 52 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 42 | END | 42 | 42 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 69 | START | 69 | 86 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `24` | `23` | 195 | START | 195 | 201 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `24` | `23` | 230 | START | 230 | 286 |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | `32` | `29` | 281 | START | 281 | 285 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–323
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 30 | 17 | inferred_complete_timeline |
| `Action_None` | 74 | 323 | 250 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_LongSnap` | 14 | 52 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 329 | 316 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 74 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 68 | 26 | inferred_complete_timeline |
| `Action_PuntBall` | 69 | 86 | 18 | inferred_complete_timeline |
| `Action_None` | 87 | 329 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 23 | 10 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–50
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 50 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |
| `Action_None` | 46 | 213 | 168 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 153 | 140 | inferred_complete_timeline |
| `Action_None` | 156 | 170 | 15 | inferred_complete_timeline |
| `Action_None` | 174 | 225 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 110 | 97 | inferred_complete_timeline |
| `Action_None` | 113 | 169 | 57 | inferred_complete_timeline |
| `Action_None` | 173 | 267 | 95 | inferred_complete_timeline |
| `Action_None` | 270 | 273 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 118 | 105 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 148 | 135 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |
| `Action_None` | 160 | 161 | 2 | inferred_complete_timeline |
| `Action_None` | 164 | 171 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 238 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 181 | 168 | inferred_complete_timeline |
| `Action_None` | 190 | 287 | 98 | inferred_complete_timeline |
| `Action_None` | 291 | 306 | 16 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–322
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 322 | 309 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 329 | 316 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–329 | 303 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 34–38 | 5 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 51–307 | 239 | 5 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 56–79 | 19 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 59–329 | 270 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 60–155 | 91 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 63–329 | 249 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 84–255 | 172 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 99–314 | 215 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 107–272 | 161 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 116–322 | 201 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 127–238 | 112 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 139–255 | 116 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 147–329 | 167 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 157–285 | 121 | 5 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 207–255 | 4 | 2 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 234–312 | 75 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 248–284 | 26 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 264–329 | 66 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 290–295 | 6 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 295–329 | 27 | 2 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 300–306 | 7 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 319–328 | 10 | 1 | Undefined position; Undefined team |
| `38` | `55` | Position_Unknown | Team_Unknown | 322–329 | 8 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 323–329 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `24` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 81 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [14-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-287] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-306] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-329] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-74] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-171] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-238] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [14-52] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-322] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-153] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-170] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-225] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-169] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-267] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-273] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-30] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-323] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-36] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-241] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-301] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-213] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-23] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-129] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-174] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-289] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-307] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-279] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-126] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-155] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-65] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-255] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [230-286] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [288-314] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-169] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-272] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-126] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-322] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-238] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-252] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-279] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-312] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-158] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-183] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-277] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [281-285] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-282] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-312] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-269] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-284] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-295] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-303] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-328] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>