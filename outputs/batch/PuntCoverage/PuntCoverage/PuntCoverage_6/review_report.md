# Play-Annotation-Generator Annotation Review — PuntCoverage_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_6`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 201
- **Validation Warnings:** 249
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 187
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `6` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `12` | `12` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner | defense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `14` | `14` |
| ⚠️ START CHANGED | `Action_Tackle` | Position_Unknown | Team_Unknown | `31` | `29` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `5` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `6` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `12` | `12` | 16 | START | 16 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 42 | END | 42 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `4` | `4` | 77 | START | 77 | 87 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Punt_Returner | `14` | `14` | 191 | START | 192 | 198 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `14` | `14` | 207 | START | 207 | 215 |
| ⚠️ START CHANGED | `Action_Tackle` | Position_Unknown | `31` | `29` | 309 | START | 318 | 321 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 114 | 99 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_None` | 159 | 207 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 59 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 37 | 22 | inferred_complete_timeline |
| `Action_None` | 39 | 74 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–404
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 100 | 85 | inferred_complete_timeline |
| `Action_None` | 105 | 404 | 300 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 78 | 63 | inferred_complete_timeline |
| `Action_None` | 80 | 104 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_SnapReceive` | 42 | 42 | 1 | inferred_complete_timeline |
| `Action_None` | 43 | 62 | 20 | inferred_complete_timeline |
| `Action_None` | 67 | 76 | 10 | inferred_complete_timeline |
| `Action_PuntBall` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_PuntBall` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 191 | 46 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 203 | 205 | 3 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 237 | 246 | 10 | inferred_complete_timeline |
| `Action_None` | 256 | 272 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 52 | 37 | inferred_complete_timeline |
| `Action_None` | 55 | 225 | 171 | inferred_complete_timeline |
| `Action_None` | 227 | 270 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 142 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 405

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 50 | 35 | inferred_complete_timeline |
| `Action_None` | 55 | 57 | 3 | inferred_complete_timeline |
| `Action_None` | 67 | 386 | 320 | inferred_complete_timeline |
| `Action_None` | 388 | 390 | 3 | inferred_complete_timeline |
| `Action_None` | 392 | 419 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 346

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 59 | 44 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 195 | 129 | inferred_complete_timeline |
| `Action_None` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 208 | 6 | inferred_complete_timeline |
| `Action_None` | 210 | 225 | 16 | inferred_complete_timeline |
| `Action_None` | 233 | 332 | 100 | inferred_complete_timeline |
| `Action_None` | 340 | 342 | 3 | inferred_complete_timeline |
| `Action_None` | 344 | 350 | 7 | inferred_complete_timeline |
| `Action_None` | 356 | 361 | 6 | inferred_complete_timeline |
| `Action_None` | 369 | 370 | 2 | inferred_complete_timeline |
| `Action_None` | 372 | 384 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 122 | 107 | inferred_complete_timeline |
| `Action_None` | 129 | 225 | 97 | inferred_complete_timeline |
| `Action_None` | 227 | 266 | 40 | inferred_complete_timeline |
| `Action_None` | 268 | 419 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 206 | 191 | inferred_complete_timeline |
| `Action_None` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_None` | 223 | 238 | 16 | inferred_complete_timeline |
| `Action_None` | 242 | 243 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 173 | 158 | inferred_complete_timeline |
| `Action_None` | 178 | 337 | 160 | inferred_complete_timeline |
| `Action_None` | 340 | 376 | 37 | inferred_complete_timeline |
| `Action_None` | 379 | 419 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–250
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 189 | 190 | inferred_complete_timeline |
| `Action_CatchPunt` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 199 | 206 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 207 | 215 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 217 | 250 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–231
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 53 | 38 | inferred_complete_timeline |
| `Action_None` | 55 | 124 | 70 | inferred_complete_timeline |
| `Action_None` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 152 | 153 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 160 | 231 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 54 | 39 | inferred_complete_timeline |
| `Action_None` | 57 | 80 | 24 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–48 | 46 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 7–55 | 40 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 22–126 | 105 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 27–69 | 8 | 4 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 46–365 | 286 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 50–240 | 155 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 54–416 | 226 | 12 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 71–192 | 122 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 95–111 | 17 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 99–104 | 6 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 107–301 | 177 | 3 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 108–419 | 312 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 118–344 | 216 | 4 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 136–321 | 159 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 140–352 | 197 | 6 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 159–419 | 244 | 6 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 162–174 | 11 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 162–163 | 2 | 1 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 176–196 | 16 | 2 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 180–340 | 153 | 4 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 220–398 | 164 | 5 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 240–324 | 71 | 5 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 254–373 | 88 | 4 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 269–396 | 40 | 4 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 281–320 | 12 | 2 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 282–372 | 23 | 3 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 289–291 | 3 | 1 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 296–298 | 3 | 1 | Undefined position; Undefined team |
| `44` | `58` | Position_Unknown | Team_Unknown | 303–324 | 17 | 3 | Undefined position; Undefined team |
| `45` | `59` | Position_Unknown | Team_Unknown | 305–306 | 2 | 1 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 319–340 | 4 | 2 | Undefined position; Undefined team |
| `47` | `61` | Position_Unknown | Team_Unknown | 333–419 | 52 | 6 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 387–412 | 20 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (2 segments found)
- ⚠️ `Action_CatchPunt` for actor_track_id `14` (Punt_Returner): Annotated start 191 != Inferred start 192
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)
- ⚠️ `Action_Tackle` for actor_track_id `31` (Position_Unknown): Annotated start 309 != Inferred start 318

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ 33 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 33 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 66 |
| Missing visible bounding boxes during action | 181 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-54] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-80] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-206] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-225] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-266] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-419] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-62] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-76] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [77-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [92-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-246] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-272] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-114] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-156] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-207] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-37] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-53] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-153] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-50] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-386] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-419] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-59] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-195] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-208] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-332] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-342] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-350] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-370] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-384] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-104] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-404] for track '11' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-59] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-52] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-225] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-270] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-189] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CatchPunt' range [192-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [207-215] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [217-250] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 16, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [16-173] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-337] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-376] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-48] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-48] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-174] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-297] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-325] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-335] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-343] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-205] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-212] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-240] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-214] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-255] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-263] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-278] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-283] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-380] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-402] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-416] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-192] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-111] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-104] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-264] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-301] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-131] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-255] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-344] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-187] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-205] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-295] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [318-321] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-188] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-306] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-320] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-345] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-352] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-175] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-264] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-354] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-419] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-168] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-174] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-207] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-297] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-330] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-340] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-229] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-373] for track '36' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-389] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-260] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-295] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-305] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-320] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-324] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-324] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-332] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-350] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-281] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-298] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-330] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-396] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-290] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-292] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-372] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-291] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-320] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-320] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-370] for track '47' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-396] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-412] for track '48' has 2 frames without a visible bounding box.
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

</details>