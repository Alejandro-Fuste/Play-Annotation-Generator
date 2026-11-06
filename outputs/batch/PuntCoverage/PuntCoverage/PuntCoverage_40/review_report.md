# Play-Annotation-Generator Annotation Review — PuntCoverage_40

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_40`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 137
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 5
- **Group Expanded Events:** 9
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `6` | `6` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `19` | `19` |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | Team_Unknown | `28` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `4` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `6` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `5` | `5` | 8 | START | 8 | 67 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `6` | `6` | 36 | END | 36 | 36 |
| ✅ EXACT | `Action_PuntBall` | Punter | `6` | `6` | 68 | START | 68 | 83 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `19` | `19` | 193 | START | 193 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `19` | `19` | 204 | START | 204 | 257 |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | `28` | `26` | 246 | START | 246 | 272 |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 23 | 58 | 36 | inferred_complete_timeline |
| `Action_None` | 68 | 88 | 21 | inferred_complete_timeline |
| `Action_None` | 90 | 299 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_None` | 184 | 187 | 4 | inferred_complete_timeline |
| `Action_None` | 189 | 196 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 208 | 213 | 6 | inferred_complete_timeline |
| `Action_None` | 216 | 277 | 62 | inferred_complete_timeline |
| `Action_None` | 287 | 299 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 67 | 60 | inferred_complete_timeline |
| `Action_None` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 86 | 299 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 299 | 292 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 81 | 74 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |
| `Action_None` | 107 | 167 | 61 | inferred_complete_timeline |
| `Action_None` | 169 | 182 | 14 | inferred_complete_timeline |
| `Action_None` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_None` | 204 | 216 | 13 | inferred_complete_timeline |
| `Action_None` | 224 | 232 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 297 | 290 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_SnapReceive` | 36 | 36 | 1 | inferred_complete_timeline |
| `Action_None` | 37 | 67 | 31 | inferred_complete_timeline |
| `Action_PuntBall` | 68 | 83 | 16 | inferred_complete_timeline |
| `Action_None` | 84 | 99 | 16 | inferred_complete_timeline |
| `Action_None` | 102 | 103 | 2 | inferred_complete_timeline |
| `Action_None` | 109 | 111 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 204 | 92 | inferred_complete_timeline |
| `Action_None` | 206 | 278 | 73 | inferred_complete_timeline |
| `Action_None` | 280 | 294 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 70 | 63 | inferred_complete_timeline |
| `Action_None` | 73 | 299 | 227 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 59 | 52 | inferred_complete_timeline |
| `Action_None` | 71 | 160 | 90 | inferred_complete_timeline |
| `Action_None` | 166 | 224 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 164 | 157 | inferred_complete_timeline |
| `Action_None` | 179 | 242 | 64 | inferred_complete_timeline |
| `Action_None` | 247 | 248 | 2 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_None` | 86 | 173 | 88 | inferred_complete_timeline |
| `Action_None` | 180 | 283 | 104 | inferred_complete_timeline |
| `Action_None` | 285 | 299 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–16
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 16 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 34 | 27 | inferred_complete_timeline |
| `Action_None` | 64 | 272 | 209 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–276
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 79 | 72 | inferred_complete_timeline |
| `Action_None` | 84 | 155 | 72 | inferred_complete_timeline |
| `Action_None` | 157 | 167 | 11 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 210 | 212 | 3 | inferred_complete_timeline |
| `Action_None` | 221 | 228 | 8 | inferred_complete_timeline |
| `Action_None` | 238 | 242 | 5 | inferred_complete_timeline |
| `Action_None` | 244 | 245 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 276 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 120 | 113 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |
| `Action_None` | 127 | 278 | 152 | inferred_complete_timeline |
| `Action_None` | 281 | 299 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 59 | 52 | inferred_complete_timeline |
| `Action_None` | 69 | 80 | 12 | inferred_complete_timeline |
| `Action_None` | 83 | 84 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 26–299 | 273 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 35–38 | 4 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 46–286 | 233 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 47–299 | 242 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 49–184 | 93 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 71–299 | 223 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 81–86 | 6 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 83–91 | 9 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 87–299 | 208 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 90–118 | 29 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 97–272 | 164 | 8 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 137–299 | 162 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 202–245 | 43 | 2 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 235–299 | 57 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 244–299 | 52 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 293–299 | 7 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 298–299 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 101 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-155] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-167] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-192] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-242] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-276] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-80] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-120] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-278] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-297] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-99] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-204] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-278] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-294] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-70] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-151] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-213] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-277] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-160] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-224] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-272] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-167] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-216] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-164] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-242] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-21] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-58] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-19] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-173] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-283] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-16] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-81] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-286] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [261-263] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-107] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-140] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-186] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-229] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-86] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-91] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-228] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-118] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-173] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-198] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-219] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-234] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-238] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [246-272] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-221] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-245] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-269] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-299] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-252] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-271] for track '30' has 1 frames without a visible bounding box.
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

</details>