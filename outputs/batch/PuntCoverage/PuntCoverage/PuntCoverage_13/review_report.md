# Play-Annotation-Generator Annotation Review — PuntCoverage_13

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntCoverage_13`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntCoverage`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 52
- **Ball Tracks:** 0
- **Action Segments:** 172
- **Validation Warnings:** 199
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 155
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `3` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `16` | `16` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `33` | `29` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `33` | `29` |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | Team_Unknown | `22` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Gunner | `0` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `10` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `14` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `16` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `3` | `Group` | 0 | START | 0 | 17 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `18` | `18` | 18 | START | 18 | 75 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `16` | `16` | 45 | END | 45 | 45 |
| ✅ EXACT | `Action_PuntBall` | Punter | `16` | `16` | 76 | START | 76 | 88 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `33` | `29` | 214 | START | 214 | 220 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `33` | `29` | 320 | START | 320 | 346 |
| ✅ EXACT | `Action_Tackle` | Position_Unknown | `22` | `21` | 342 | START | 342 | 369 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 77 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Gunner — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 150 | 133 | inferred_complete_timeline |
| `Action_None` | 152 | 355 | 204 | inferred_complete_timeline |
| `Action_None` | 359 | 372 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 90 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_LongSnap` | 18 | 75 | 58 | inferred_complete_timeline |
| `Action_None` | 76 | 165 | 90 | inferred_complete_timeline |
| `Action_None` | 167 | 354 | 188 | inferred_complete_timeline |
| `Action_None` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 249 | 232 | inferred_complete_timeline |
| `Action_None` | 256 | 389 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 170 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–161
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 45 | 45 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 75 | 30 | inferred_complete_timeline |
| `Action_PuntBall` | 76 | 88 | 13 | inferred_complete_timeline |
| `Action_None` | 89 | 161 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 186 | 169 | inferred_complete_timeline |
| `Action_None` | 189 | 191 | 3 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_None` | 210 | 324 | 115 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 161 | 144 | inferred_complete_timeline |
| `Action_None` | 163 | 167 | 5 | inferred_complete_timeline |
| `Action_None` | 172 | 176 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 208 | 191 | inferred_complete_timeline |
| `Action_None` | 210 | 353 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 352 | 335 | inferred_complete_timeline |
| `Action_None` | 360 | 389 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 141 | 124 | inferred_complete_timeline |
| `Action_None` | 143 | 215 | 73 | inferred_complete_timeline |
| `Action_None` | 218 | 249 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 353 | 336 | inferred_complete_timeline |
| `Action_None` | 359 | 389 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 174 | 157 | inferred_complete_timeline |
| `Action_None` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_None` | 181 | 201 | 21 | inferred_complete_timeline |
| `Action_None` | 206 | 389 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 389 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Jammer — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 172 | 155 | inferred_complete_timeline |
| `Action_None` | 176 | 205 | 30 | inferred_complete_timeline |
| `Action_None` | 208 | 389 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 98 | 81 | inferred_complete_timeline |
| `Action_None` | 100 | 101 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 389 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 389 | 372 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_None` | 18 | 389 | 372 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–362 | 361 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 90–369 | 273 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 90–97 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 102–104 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 105–194 | 63 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 111–389 | 263 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 136–203 | 44 | 7 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 142–389 | 212 | 10 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 149–150 | 2 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 159–389 | 230 | 5 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 161–246 | 78 | 7 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 164–167 | 4 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 175–177 | 3 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 180–231 | 39 | 4 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 184–222 | 38 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 221–263 | 17 | 6 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 221–376 | 128 | 6 | Undefined position; Undefined team |
| `38` | `56` | Position_Unknown | Team_Unknown | 227–236 | 9 | 2 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 240–273 | 29 | 2 | Undefined position; Undefined team |
| `40` | `63` | Position_Unknown | Team_Unknown | 247–256 | 10 | 1 | Undefined position; Undefined team |
| `41` | `64` | Position_Unknown | Team_Unknown | 250–389 | 120 | 6 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 250–298 | 25 | 7 | Undefined position; Undefined team |
| `43` | `69` | Position_Unknown | Team_Unknown | 269–270 | 2 | 1 | Undefined position; Undefined team |
| `44` | `70` | Position_Unknown | Team_Unknown | 276–323 | 38 | 3 | Undefined position; Undefined team |
| `45` | `71` | Position_Unknown | Team_Unknown | 277–319 | 21 | 7 | Undefined position; Undefined team |
| `46` | `72` | Position_Unknown | Team_Unknown | 295–296 | 2 | 1 | Undefined position; Undefined team |
| `47` | `76` | Position_Unknown | Team_Unknown | 323–325 | 3 | 1 | Undefined position; Undefined team |
| `48` | `77` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `49` | `78` | Position_Unknown | Team_Unknown | 339–366 | 27 | 2 | Undefined position; Undefined team |
| `50` | `79` | Position_Unknown | Team_Unknown | 360–386 | 27 | 1 | Undefined position; Undefined team |
| `51` | `80` | Position_Unknown | Team_Unknown | 361–389 | 29 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `33` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Jammer` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Tackle` position mapped to `offense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 133 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [18-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-355] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-372] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-341] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-362] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-98] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-101] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-161] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-141] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-249] for track '5' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-174] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-179] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-201] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-353] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-205] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-170] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-249] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-352] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-161] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-186] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-324] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-354] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-77] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-353] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-194] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-211] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-221] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Tackle' range [342-369] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-97] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-115] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-215] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-160] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-179] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-203] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-165] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-177] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-189] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-206] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-224] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-319] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-346] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [348-389] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-189] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-220] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-228] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-236] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-246] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-201] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-218] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-231] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-187] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-222] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-226] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-251] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-228] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-331] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-352] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-372] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-236] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-249] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-273] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-256] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-260] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-268] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-278] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-349] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-256] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-270] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-291] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-311] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-323] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-284] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-313] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-363] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [365-366] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-386] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>