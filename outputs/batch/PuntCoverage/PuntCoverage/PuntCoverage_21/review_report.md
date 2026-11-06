# Play-Annotation-Generator Annotation Review — PuntCoverage_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_21`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 149
- **Validation Warnings:** 163
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
- **Inferred Coverage Segments (Action_None):** 126
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `13` | `13` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `36` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `36` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Right_Gunner | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `1` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `13` | `Group` | 0 | START | 0 | 38 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `14` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `19` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `11` | `11` | 16 | START | 16 | 63 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `13` | `13` | 39 | END | 39 | 39 |
| ✅ EXACT | `Action_PuntBall` | Punter | `13` | `13` | 64 | START | 64 | 81 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `36` | `27` | 192 | START | 192 | 206 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `36` | `27` | 252 | START | 252 | 286 |
| ⚠️ AMBIGUOUS MATCH | `Action_Tackle` | Right_Gunner | `1` | `1` | 263 | START | 263 | 277 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 140 | 125 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 174 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 154 | 139 | inferred_complete_timeline |
| `Action_None` | 157 | 254 | 98 | inferred_complete_timeline |
| `Action_None` | 256 | 359 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–307
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 154 | 139 | inferred_complete_timeline |
| `Action_None` | 156 | 180 | 25 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |
| `Action_None` | 193 | 307 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–74
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 63 | 48 | inferred_complete_timeline |
| `Action_None` | 64 | 70 | 7 | inferred_complete_timeline |
| `Action_None` | 73 | 74 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_SnapReceive` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_None` | 40 | 63 | 24 | inferred_complete_timeline |
| `Action_PuntBall` | 64 | 81 | 18 | inferred_complete_timeline |
| `Action_None` | 82 | 168 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 29 | 14 | inferred_complete_timeline |
| `Action_None` | 33 | 35 | 3 | inferred_complete_timeline |
| `Action_None` | 38 | 359 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 162 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 188 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 239 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 246 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 249 | 262 | 14 | inferred_complete_timeline |
| `Action_Tackle` | 263 | 277 | 15 | inferred_complete_timeline |
| `Action_Tackle` | 279 | 289 | 11 | inferred_complete_timeline |
| `Action_None` | 290 | 292 | 3 | inferred_complete_timeline |
| `Action_None` | 299 | 301 | 3 | inferred_complete_timeline |
| `Action_None` | 303 | 359 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 178 | 163 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 197 | 13 | inferred_complete_timeline |
| `Action_None` | 203 | 206 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 328 | 313 | inferred_complete_timeline |
| `Action_None` | 330 | 359 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 195 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 184 | 169 | inferred_complete_timeline |
| `Action_None` | 188 | 189 | 2 | inferred_complete_timeline |
| `Action_None` | 191 | 276 | 86 | inferred_complete_timeline |
| `Action_None` | 278 | 359 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 51 | 164 | 114 | inferred_complete_timeline |
| `Action_None` | 174 | 319 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 285 | 270 | inferred_complete_timeline |
| `Action_None` | 294 | 359 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 71 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 326 | 311 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 133 | 118 | inferred_complete_timeline |
| `Action_None` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |
| `Action_None` | 156 | 267 | 112 | inferred_complete_timeline |
| `Action_None` | 285 | 358 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 182 | 167 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 193 | 359 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–331
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 200 | 185 | inferred_complete_timeline |
| `Action_None` | 202 | 331 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Jammer — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–96
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 85 | 70 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 95 | 96 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `24` | Position_Unknown | Team_Unknown | 85–359 | 258 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 100–359 | 255 | 3 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 110–112 | 3 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 114–115 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 116–233 | 107 | 5 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 144–191 | 32 | 6 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 164–359 | 171 | 10 | Undefined position; Undefined team |
| `28` | `41` | Position_Unknown | Team_Unknown | 194–282 | 81 | 2 | Undefined position; Undefined team |
| `29` | `43` | Position_Unknown | Team_Unknown | 205–322 | 84 | 5 | Undefined position; Undefined team |
| `30` | `44` | Position_Unknown | Team_Unknown | 206–294 | 88 | 2 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 206–227 | 8 | 3 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 214–216 | 3 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 221–262 | 42 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 224–359 | 133 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 225–226 | 2 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 237–309 | 67 | 3 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 238–240 | 3 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 246–267 | 22 | 1 | Undefined position; Undefined team |
| `40` | `60` | Position_Unknown | Team_Unknown | 256–359 | 72 | 4 | Undefined position; Undefined team |
| `41` | `62` | Position_Unknown | Team_Unknown | 270–271 | 2 | 1 | Undefined position; Undefined team |
| `42` | `64` | Position_Unknown | Team_Unknown | 275–277 | 3 | 1 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 284–292 | 9 | 1 | Undefined position; Undefined team |
| `44` | `66` | Position_Unknown | Team_Unknown | 321–323 | 3 | 1 | Undefined position; Undefined team |
| `45` | `69` | Position_Unknown | Team_Unknown | 356–359 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `36` (6 segments found)
- ⚠️ Ambiguous match for action `Action_Tackle` and target `1` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 111 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [16-326] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-188] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-239] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-246] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-262] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [263-277] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [279-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-154] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-254] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-285] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-331] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-85] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-328] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [16-63] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-140] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-174] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-133] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-149] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-267] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-358] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-319] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-35] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-178] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-197] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-154] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-180] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-307] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-184] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-175] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-280] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-292] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-204] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-339] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-233] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-154] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-191] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [252-286] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-304] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [309-313] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [327-332] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [335-347] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-282] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-208] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-216] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-252] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-322] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-294] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-208] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-217] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-262] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-359] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-241] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-248] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-309] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-240] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-267] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-265] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-335] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-271] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '44' has 1 frames without a visible bounding box.
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

</details>