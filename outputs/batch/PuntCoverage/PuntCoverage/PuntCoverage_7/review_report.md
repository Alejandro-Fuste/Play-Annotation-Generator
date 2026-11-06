# Play-Annotation-Generator Annotation Review — PuntCoverage_7

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_7`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 35
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `9` | `9` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `34` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `26` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Left_Wing | offense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `14` | `Group` | 0 | START | 0 | 231 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `15` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `19` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `20` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `9` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 1 | START | 1 | 64 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `9` | `9` | 27 | END | 27 | 27 |
| ✅ EXACT | `Action_PuntBall` | Punter | `9` | `9` | 65 | START | 65 | 79 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `34` | `26` | 184 | START | 184 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `26` | 204 | START | 204 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Left_Wing | `14` | `14` | 232 | START | 232 | 248 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 31 | 31 | inferred_complete_timeline |
| `Action_None` | 33 | 329 | 297 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 174 | 174 | inferred_complete_timeline |
| `Action_None` | 176 | 198 | 23 | inferred_complete_timeline |
| `Action_None` | 205 | 329 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 231 | 232 | inferred_complete_timeline |
| `Action_Tackle` | 232 | 248 | 17 | inferred_complete_timeline |
| `Action_Tackle` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 255 | 276 | 22 | inferred_complete_timeline |
| `Action_None` | 283 | 329 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–275
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 64 | 64 | inferred_complete_timeline |
| `Action_None` | 65 | 275 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 189 | 189 | inferred_complete_timeline |
| `Action_None` | 193 | 198 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 146 | 146 | inferred_complete_timeline |
| `Action_None` | 150 | 329 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 27 | 1 | inferred_complete_timeline |
| `Action_None` | 28 | 64 | 37 | inferred_complete_timeline |
| `Action_PuntBall` | 65 | 79 | 15 | inferred_complete_timeline |
| `Action_None` | 80 | 148 | 69 | inferred_complete_timeline |
| `Action_None` | 152 | 329 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 251 | 251 | inferred_complete_timeline |
| `Action_None` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 263 | 263 | inferred_complete_timeline |
| `Action_None` | 265 | 329 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 203 | 203 | inferred_complete_timeline |
| `Action_None` | 205 | 329 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 173 | 173 | inferred_complete_timeline |
| `Action_None` | 176 | 179 | 4 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 329 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 188 | 188 | inferred_complete_timeline |
| `Action_None` | 190 | 329 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 190 | 190 | inferred_complete_timeline |
| `Action_None` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 206 | 270 | 65 | inferred_complete_timeline |
| `Action_None` | 272 | 328 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 18 | 18 | inferred_complete_timeline |
| `Action_None` | 20 | 26 | 7 | inferred_complete_timeline |
| `Action_None` | 28 | 73 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 15 | 15 | inferred_complete_timeline |
| `Action_None` | 17 | 329 | 313 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 196 | 196 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 329 | 329 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–70
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 50 | 50 | inferred_complete_timeline |
| `Action_None` | 55 | 70 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 51 | 51 | inferred_complete_timeline |
| `Action_None` | 53 | 329 | 277 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 47–56 | 10 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 70–329 | 256 | 3 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 81–329 | 235 | 6 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 148–179 | 13 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 154–155 | 2 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 161–329 | 122 | 5 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 190–297 | 101 | 3 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 204–209 | 6 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 224–329 | 94 | 5 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 224–237 | 14 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 300–329 | 30 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 313–326 | 4 | 2 | Undefined position; Undefined team |
| `33` | `51` | Position_Unknown | Team_Unknown | 327–329 | 3 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 329–329 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 68 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [1-329] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-51] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-173] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-263] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-329] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-70] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [1-64] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-275] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-196] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-188] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-329] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-190] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-270] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-328] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-203] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-31] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-329] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [232-248] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-276] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-329] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-251] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-260] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-18] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [20-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-73] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-15] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-329] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-189] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-198] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-56] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-181] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-205] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-181] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-298] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-153] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-264] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-199] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-293] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-209] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-227] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-269] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-303] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-329] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-326] for track '32' has 1 frames without a visible bounding box.
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

</details>