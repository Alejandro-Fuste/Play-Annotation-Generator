# Play-Annotation-Generator Annotation Review — PuntCoverage_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_49`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 154
- **Validation Warnings:** 198
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 141
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Left_Guard | offense | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `3` | `3` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `30` | `28` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `30` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | Team_Unknown | `28` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `15` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `17` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `3` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `6` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `0` | `0` | 8 | START | 8 | 57 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | Left_Guard | `13` | `13` | 36 | END | N/A | N/A |
| ✅ EXACT | `Action_PuntBall` | Punter | `3` | `3` | 58 | START | 58 | 74 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `30` | `28` | 183 | START | 183 | 192 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `30` | `28` | 212 | START | 212 | 291 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | `28` | `26` | 254 | START | 254 | 254 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 30 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_None` | 58 | 152 | 95 | inferred_complete_timeline |
| `Action_None` | 154 | 329 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 87 | 80 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 161 | 66 | inferred_complete_timeline |
| `Action_None` | 166 | 180 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 239 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PuntBall` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_None` | 75 | 143 | 69 | inferred_complete_timeline |
| `Action_None` | 151 | 329 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–35
- **Visible Samples:** 35

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 32 | 25 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 30 | 23 | inferred_complete_timeline |
| `Action_None` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 291 | 244 | inferred_complete_timeline |
| `Action_None` | 298 | 329 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 57 | 50 | inferred_complete_timeline |
| `Action_None` | 61 | 95 | 35 | inferred_complete_timeline |
| `Action_None` | 97 | 329 | 233 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 40 | 33 | inferred_complete_timeline |
| `Action_None` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 132 | 63 | inferred_complete_timeline |
| `Action_None` | 134 | 136 | 3 | inferred_complete_timeline |
| `Action_None` | 154 | 288 | 135 | inferred_complete_timeline |
| `Action_None` | 290 | 329 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 36 | 29 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 61 | 54 | inferred_complete_timeline |
| `Action_None` | 68 | 73 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 80 | 4 | inferred_complete_timeline |
| `Action_None` | 87 | 129 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 71 | 64 | inferred_complete_timeline |
| `Action_None` | 73 | 129 | 57 | inferred_complete_timeline |
| `Action_None` | 137 | 142 | 6 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 154 | 248 | 95 | inferred_complete_timeline |
| `Action_None` | 252 | 253 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 329 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 80 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–101 | 73 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–45 | 43 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–44 | 33 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 3–329 | 322 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 13–329 | 316 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 13–83 | 14 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 18–44 | 27 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 28–80 | 53 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 37–70 | 32 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 39–40 | 2 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 44–328 | 260 | 7 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 49–50 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 53–291 | 238 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 79–127 | 6 | 3 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 89–154 | 63 | 4 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 98–329 | 224 | 3 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 104–202 | 41 | 8 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 105–329 | 225 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 119–329 | 211 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 132–138 | 7 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 139–329 | 184 | 6 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 155–329 | 175 | 1 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 165–329 | 157 | 4 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 175–267 | 83 | 3 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 187–210 | 11 | 2 | Undefined position; Undefined team |
| `42` | `58` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `43` | `59` | Position_Unknown | Team_Unknown | 207–208 | 2 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 210–211 | 2 | 1 | Undefined position; Undefined team |
| `45` | `63` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `46` | `64` | Position_Unknown | Team_Unknown | 242–263 | 22 | 1 | Undefined position; Undefined team |
| `47` | `65` | Position_Unknown | Team_Unknown | 242–279 | 35 | 3 | Undefined position; Undefined team |
| `48` | `67` | Position_Unknown | Team_Unknown | 250–252 | 3 | 1 | Undefined position; Undefined team |
| `49` | `69` | Position_Unknown | Team_Unknown | 262–317 | 11 | 4 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 318–329 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_SnapReceive` on target `13` (Left_Guard)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `28` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Gunner` position mapped to `offense` team
- ⚠️ 36 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 36 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 72 |
| Missing visible bounding boxes during action | 120 |
| Track-related warning | 4 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 99: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ Row 100: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SnapReceive' for track '13' has invalid range: start=36, end=30. Clamping end to start.
- ⚠️ Action 'Action_None' range [58-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-329] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-36] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-30] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-35] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-291] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-40] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-68] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-288] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-57] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-62] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-61] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-80] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-129] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-329] for track '12' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-129] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-142] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-161] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-239] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-45] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-13] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-329] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-29] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-17] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-51] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-44] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-80] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-51] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-40] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-253] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' for track '26' starts at frame 254, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_Tackle' range [254-254] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [263-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [268-275] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [286-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-328] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [212-291] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-97] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-124] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-154] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-271] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-117] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-137] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-138] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-283] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-312] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-325] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-175] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-232] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-329] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-267] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-192] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-263] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-246] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-275] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-252] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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