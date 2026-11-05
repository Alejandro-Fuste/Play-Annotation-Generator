# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_24`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 539
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 213
- **Validation Warnings:** 256
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 200
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `14` | `14` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `33` | `26` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `26` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `61` | `42` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `13` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `14` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `2` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `9` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `9` | `9` | 8 | START | 8 | 65 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `14` | `14` | 40 | END | 40 | 40 |
| ✅ EXACT | `Action_PuntBall` | Punter | `14` | `14` | 66 | START | 66 | 80 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `33` | `26` | 203 | START | 203 | 212 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `33` | `26` | 226 | START | 226 | 348 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `61` | `42` | 520 | START | 520 | 532 |

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
- **Visible Frames:** 0–135
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 66 | 59 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |
| `Action_None` | 74 | 76 | 3 | inferred_complete_timeline |
| `Action_None` | 78 | 91 | 14 | inferred_complete_timeline |
| `Action_None` | 95 | 99 | 5 | inferred_complete_timeline |
| `Action_None` | 101 | 135 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 138 | 131 | inferred_complete_timeline |
| `Action_None` | 143 | 244 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 65 | 58 | inferred_complete_timeline |
| `Action_None` | 66 | 84 | 19 | inferred_complete_timeline |
| `Action_None` | 86 | 92 | 7 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |
| `Action_None` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 117 | 147 | 31 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 192 | 193 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 201 | 3 | inferred_complete_timeline |
| `Action_None` | 204 | 206 | 3 | inferred_complete_timeline |
| `Action_None` | 208 | 221 | 14 | inferred_complete_timeline |
| `Action_None` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 256 | 14 | inferred_complete_timeline |
| `Action_None` | 259 | 319 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–233
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 101 | 94 | inferred_complete_timeline |
| `Action_None` | 105 | 233 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 136 | 129 | inferred_complete_timeline |
| `Action_None` | 139 | 160 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 106 | 99 | inferred_complete_timeline |
| `Action_None` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_None` | 132 | 145 | 14 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_None` | 177 | 195 | 19 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 218 | 227 | 10 | inferred_complete_timeline |
| `Action_None` | 238 | 248 | 11 | inferred_complete_timeline |
| `Action_None` | 251 | 265 | 15 | inferred_complete_timeline |
| `Action_None` | 270 | 272 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 40 | 1 | inferred_complete_timeline |
| `Action_None` | 41 | 65 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 66 | 80 | 15 | inferred_complete_timeline |
| `Action_None` | 81 | 137 | 57 | inferred_complete_timeline |
| `Action_None` | 142 | 145 | 4 | inferred_complete_timeline |
| `Action_None` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_None` | 161 | 168 | 8 | inferred_complete_timeline |
| `Action_None` | 173 | 176 | 4 | inferred_complete_timeline |
| `Action_None` | 178 | 193 | 16 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 209 | 210 | 2 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |
| `Action_None` | 220 | 240 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_None` | 154 | 173 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 69 | 62 | inferred_complete_timeline |
| `Action_None` | 71 | 81 | 11 | inferred_complete_timeline |
| `Action_None` | 86 | 133 | 48 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 528

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 353 | 346 | inferred_complete_timeline |
| `Action_None` | 366 | 539 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–248
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 248 | 241 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–474
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 134 | 127 | inferred_complete_timeline |
| `Action_None` | 136 | 187 | 52 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_None` | 210 | 223 | 14 | inferred_complete_timeline |
| `Action_None` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_None` | 235 | 310 | 76 | inferred_complete_timeline |
| `Action_None` | 313 | 365 | 53 | inferred_complete_timeline |
| `Action_None` | 367 | 465 | 99 | inferred_complete_timeline |
| `Action_None` | 468 | 474 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–510
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 144 | 137 | inferred_complete_timeline |
| `Action_None` | 146 | 510 | 365 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 537

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 410 | 403 | inferred_complete_timeline |
| `Action_None` | 413 | 422 | 10 | inferred_complete_timeline |
| `Action_None` | 424 | 539 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 44 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 9–14 | 6 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 24–83 | 60 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 34–429 | 330 | 11 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 47–105 | 55 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 89–539 | 417 | 8 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 104–151 | 48 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 107–390 | 267 | 6 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 114–534 | 361 | 15 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 124–211 | 88 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 126–252 | 127 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 129–530 | 385 | 6 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 155–348 | 194 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 181–539 | 342 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 202–290 | 71 | 4 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 202–539 | 304 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 221–455 | 228 | 2 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 243–539 | 292 | 4 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 244–255 | 12 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 246–249 | 4 | 1 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 248–539 | 290 | 2 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 257–259 | 3 | 1 | Undefined position; Undefined team |
| `36` | `49` | Position_Unknown | Team_Unknown | 270–539 | 238 | 6 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 314–355 | 16 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 323–539 | 211 | 3 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 336–357 | 22 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 342–423 | 69 | 7 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 353–514 | 162 | 1 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 355–539 | 181 | 4 | Undefined position; Undefined team |
| `43` | `62` | Position_Unknown | Team_Unknown | 360–539 | 179 | 2 | Undefined position; Undefined team |
| `44` | `63` | Position_Unknown | Team_Unknown | 370–371 | 2 | 1 | Undefined position; Undefined team |
| `45` | `64` | Position_Unknown | Team_Unknown | 381–539 | 159 | 1 | Undefined position; Undefined team |
| `46` | `65` | Position_Unknown | Team_Unknown | 402–539 | 138 | 1 | Undefined position; Undefined team |
| `47` | `66` | Position_Unknown | Team_Unknown | 417–460 | 44 | 1 | Undefined position; Undefined team |
| `48` | `71` | Position_Unknown | Team_Unknown | 434–440 | 7 | 1 | Undefined position; Undefined team |
| `49` | `73` | Position_Unknown | Team_Unknown | 442–539 | 77 | 3 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 448–539 | 92 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 465–539 | 75 | 1 | Undefined position; Undefined team |
| `52` | `78` | Position_Unknown | Team_Unknown | 526–528 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punter` position mapped to `offense` team
- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 176 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [8-353] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-134] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-187] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-223] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-231] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-310] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-365] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-465] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-474] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-233] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-151] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-173] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-248] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-410] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-422] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-144] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-510] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-81] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-133] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-84] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-92] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-102] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-115] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-147] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-319] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-44] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-66] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-91] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-99] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-136] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-160] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-106] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-145] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-248] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-137] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-168] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-193] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-240] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [9-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-43] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-216] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-251] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-425] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-429] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-84] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-105] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-161] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-222] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-267] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-375] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-151] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-185] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-251] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-327] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-347] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-390] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-119] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-132] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-196] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-298] for track '22' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-424] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-480] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-506] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [516-534] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-211] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-252] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-160] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-396] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-404] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-423] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-490] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-530] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [226-348] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-195] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-288] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-220] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-286] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-259] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-491] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-372] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-455] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-308] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-329] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-411] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-255] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-383] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-259] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-347] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-479] for track '36' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-493] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-497] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [508-511] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-324] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-430] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-495] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-357] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-352] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-362] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-409] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-420] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-423] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-514] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [355-364] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-462] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [417-460] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-440] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [442-461] for track '49' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-479] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-539] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [465-539] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-528] for track '52' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>