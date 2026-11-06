# Play-Annotation-Generator Annotation Review — PuntCoverage_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_12`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 51
- **Ball Tracks:** 0
- **Action Segments:** 220
- **Validation Warnings:** 258
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
- **Inferred Coverage Segments (Action_None):** 206
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | Team_Unknown | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `7` | `7` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `33` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `28` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | Team_Unknown | `49` | `37` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `14` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `18` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `6` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `7` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_LongSnap` | Position_Unknown | `1` | `1` | 41 | START | 41 | 106 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `7` | `7` | 62 | END | 62 | 62 |
| ✅ EXACT | `Action_PuntBall` | Punter | `7` | `7` | 107 | START | 107 | 118 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `33` | `28` | 243 | START | 243 | 251 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `33` | `28` | 252 | START | 252 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Position_Unknown | `49` | `37` | 357 | START | 357 | 378 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 51 | 11 | inferred_complete_timeline |
| `Action_None` | 55 | 86 | 32 | inferred_complete_timeline |
| `Action_None` | 92 | 181 | 90 | inferred_complete_timeline |
| `Action_None` | 191 | 201 | 11 | inferred_complete_timeline |
| `Action_None` | 204 | 237 | 34 | inferred_complete_timeline |
| `Action_None` | 239 | 245 | 7 | inferred_complete_timeline |
| `Action_None` | 248 | 261 | 14 | inferred_complete_timeline |
| `Action_None` | 265 | 312 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–308
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 130 | 90 | inferred_complete_timeline |
| `Action_None` | 140 | 263 | 124 | inferred_complete_timeline |
| `Action_None` | 267 | 308 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 419 | 379 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–179
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 167 | 127 | inferred_complete_timeline |
| `Action_None` | 172 | 179 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 172 | 132 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 220 | 9 | inferred_complete_timeline |
| `Action_None` | 226 | 227 | 2 | inferred_complete_timeline |
| `Action_None` | 318 | 319 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 400

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_SnapReceive` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_None` | 63 | 106 | 44 | inferred_complete_timeline |
| `Action_PuntBall` | 107 | 118 | 12 | inferred_complete_timeline |
| `Action_None` | 119 | 139 | 21 | inferred_complete_timeline |
| `Action_None` | 141 | 170 | 30 | inferred_complete_timeline |
| `Action_None` | 173 | 182 | 10 | inferred_complete_timeline |
| `Action_None` | 200 | 419 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 141 | 101 | inferred_complete_timeline |
| `Action_None` | 148 | 168 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 80 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 123 | 83 | inferred_complete_timeline |
| `Action_None` | 128 | 144 | 17 | inferred_complete_timeline |
| `Action_None` | 146 | 151 | 6 | inferred_complete_timeline |
| `Action_None` | 162 | 170 | 9 | inferred_complete_timeline |
| `Action_None` | 173 | 174 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 99 | 59 | inferred_complete_timeline |
| `Action_None` | 109 | 129 | 21 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 162 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–347
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 151 | 111 | inferred_complete_timeline |
| `Action_None` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 162 | 5 | inferred_complete_timeline |
| `Action_None` | 165 | 168 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 207 | 227 | 21 | inferred_complete_timeline |
| `Action_None` | 239 | 288 | 50 | inferred_complete_timeline |
| `Action_None` | 290 | 297 | 8 | inferred_complete_timeline |
| `Action_None` | 304 | 311 | 8 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 321 | 323 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 347 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 150 | 110 | inferred_complete_timeline |
| `Action_None` | 158 | 212 | 55 | inferred_complete_timeline |
| `Action_None` | 233 | 293 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 106 | 66 | inferred_complete_timeline |
| `Action_None` | 112 | 124 | 13 | inferred_complete_timeline |
| `Action_None` | 137 | 178 | 42 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–102
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 94 | 54 | inferred_complete_timeline |
| `Action_None` | 100 | 102 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 69 | 29 | inferred_complete_timeline |
| `Action_None` | 75 | 84 | 10 | inferred_complete_timeline |
| `Action_None` | 87 | 88 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 96 | 3 | inferred_complete_timeline |
| `Action_None` | 146 | 209 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 134 | 94 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |
| `Action_None` | 152 | 163 | 12 | inferred_complete_timeline |
| `Action_None` | 165 | 182 | 18 | inferred_complete_timeline |
| `Action_None` | 192 | 216 | 25 | inferred_complete_timeline |
| `Action_None` | 219 | 229 | 11 | inferred_complete_timeline |
| `Action_None` | 242 | 245 | 4 | inferred_complete_timeline |
| `Action_None` | 248 | 253 | 6 | inferred_complete_timeline |
| `Action_None` | 255 | 301 | 47 | inferred_complete_timeline |
| `Action_None` | 304 | 321 | 18 | inferred_complete_timeline |
| `Action_None` | 326 | 336 | 11 | inferred_complete_timeline |
| `Action_None` | 338 | 355 | 18 | inferred_complete_timeline |
| `Action_None` | 357 | 361 | 5 | inferred_complete_timeline |
| `Action_None` | 365 | 378 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 153 | 113 | inferred_complete_timeline |
| `Action_None` | 164 | 179 | 16 | inferred_complete_timeline |
| `Action_None` | 188 | 201 | 14 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–419 | 419 | 4 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–128 | 129 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–131 | 90 | 7 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–121 | 50 | 5 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 84–419 | 304 | 8 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 136–227 | 80 | 3 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 146–376 | 214 | 7 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 153–202 | 50 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 158–394 | 209 | 10 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 158–161 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 167–218 | 50 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 168–369 | 195 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 189–419 | 227 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 194–331 | 125 | 4 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 220–320 | 88 | 3 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 220–276 | 49 | 2 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 224–413 | 180 | 6 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 248–357 | 100 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 250–314 | 62 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 258–419 | 139 | 8 | Undefined position; Undefined team |
| `37` | `49` | Position_Unknown | Team_Unknown | 281–387 | 97 | 4 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 287–404 | 99 | 3 | Undefined position; Undefined team |
| `39` | `52` | Position_Unknown | Team_Unknown | 297–419 | 113 | 4 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 301–308 | 8 | 1 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 302–369 | 60 | 4 | Undefined position; Undefined team |
| `42` | `56` | Position_Unknown | Team_Unknown | 305–416 | 105 | 4 | Undefined position; Undefined team |
| `43` | `57` | Position_Unknown | Team_Unknown | 314–363 | 38 | 3 | Undefined position; Undefined team |
| `44` | `61` | Position_Unknown | Team_Unknown | 339–352 | 14 | 1 | Undefined position; Undefined team |
| `45` | `66` | Position_Unknown | Team_Unknown | 368–369 | 2 | 1 | Undefined position; Undefined team |
| `46` | `67` | Position_Unknown | Team_Unknown | 377–410 | 27 | 3 | Undefined position; Undefined team |
| `47` | `68` | Position_Unknown | Team_Unknown | 380–381 | 2 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 392–397 | 6 | 1 | Undefined position; Undefined team |
| `49` | `71` | Position_Unknown | Team_Unknown | 395–416 | 20 | 2 | Undefined position; Undefined team |
| `50` | `72` | Position_Unknown | Team_Unknown | 403–404 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `33` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `49` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Guard` position mapped to `offense` team
- ⚠️ 34 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 34 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 68 |
| Missing visible bounding boxes during action | 187 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [41-130] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-308] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-352] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-123] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-144] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-151] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-128] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-153] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-179] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-201] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-139] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-419] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-182] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-216] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-245] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-301] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-321] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-336] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-355] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-361] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-80] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-102] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-106] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-124] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-69] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-84] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-209] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-172] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-319] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-168] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-227] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-288] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-311] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-347] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-150] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-212] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-293] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-129] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-162] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-181] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-237] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-245] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-312] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-103] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-122] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-294] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-322] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-392] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-407] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [412-419] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-170] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-227] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-203] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-256] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-317] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-336] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-376] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-318] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-342] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-345] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-374] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-385] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-218] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [252-290] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [293-361] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [367-369] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-323] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-350] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-298] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-320] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-245] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-276] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-247] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-311] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-317] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-325] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-408] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-302] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-357] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-309] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-288] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-317] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-335] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-345] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-357] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-413] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-337] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [357-378] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [386-387] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-318] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-361] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-404] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-350] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-387] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-308] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-320] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-330] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-361] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-336] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-389] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-399] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-416] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-342] for track '43' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-355] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-352] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-379] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-402] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-410] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-381] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-397] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-410] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-416] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
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