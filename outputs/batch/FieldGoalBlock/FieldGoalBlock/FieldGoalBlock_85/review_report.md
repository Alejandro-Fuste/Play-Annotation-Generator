# Play-Annotation-Generator Annotation Review — FieldGoalBlock_85

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_85`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 174
- **Validation Warnings:** 214
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 158
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `11` | `11` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockKick` | Left_Tackle | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `17` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `19` | `Group` | 0 | START | 0 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 5 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `4` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `6` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `7` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `11` | `11` | 17 | START | 17 | 29 |
| ✅ EXACT | `Action_KickBall` | Kicker | `6` | `6` | 38 | START | 38 | 48 |
| ✅ EXACT | `Action_BlockKick` | Left_Tackle | `17` | `17` | 45 | START | 45 | 60 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–353
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PlaceBall` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_None` | 30 | 245 | 216 | inferred_complete_timeline |
| `Action_None` | 247 | 276 | 30 | inferred_complete_timeline |
| `Action_None` | 281 | 285 | 5 | inferred_complete_timeline |
| `Action_None` | 291 | 296 | 6 | inferred_complete_timeline |
| `Action_None` | 300 | 304 | 5 | inferred_complete_timeline |
| `Action_None` | 309 | 310 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 327 | 11 | inferred_complete_timeline |
| `Action_None` | 341 | 353 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–302
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_KickBall` | 38 | 48 | 11 | inferred_complete_timeline |
| `Action_None` | 49 | 284 | 236 | inferred_complete_timeline |
| `Action_None` | 292 | 298 | 7 | inferred_complete_timeline |
| `Action_None` | 301 | 302 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_None` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_None` | 59 | 67 | 9 | inferred_complete_timeline |
| `Action_None` | 70 | 73 | 4 | inferred_complete_timeline |
| `Action_None` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_None` | 79 | 102 | 24 | inferred_complete_timeline |
| `Action_None` | 105 | 137 | 33 | inferred_complete_timeline |
| `Action_None` | 141 | 289 | 149 | inferred_complete_timeline |
| `Action_None` | 292 | 293 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 39 | 41 | 3 | inferred_complete_timeline |
| `Action_None` | 43 | 129 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BlockKick` | 45 | 60 | 16 | inferred_complete_timeline |
| `Action_None` | 61 | 81 | 21 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |
| `Action_None` | 99 | 177 | 79 | inferred_complete_timeline |
| `Action_None` | 181 | 237 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 51 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 137 | 61 | inferred_complete_timeline |
| `Action_None` | 141 | 389 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–224
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 37 | 21 | inferred_complete_timeline |
| `Action_None` | 38 | 224 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 88 | 51 | inferred_complete_timeline |
| `Action_None` | 91 | 159 | 69 | inferred_complete_timeline |
| `Action_None` | 161 | 178 | 18 | inferred_complete_timeline |
| `Action_None` | 180 | 295 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–361
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 71 | 12 | inferred_complete_timeline |
| `Action_None` | 87 | 361 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 65 | 28 | inferred_complete_timeline |
| `Action_None` | 67 | 69 | 3 | inferred_complete_timeline |
| `Action_None` | 71 | 367 | 297 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 56 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 333

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 37 | 18 | inferred_complete_timeline |
| `Action_None` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 41 | 341 | 301 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–20
- **Visible Samples:** 21

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 48 | 49 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–89
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 77 | 28 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 60 | 23 | inferred_complete_timeline |
| `Action_None` | 71 | 312 | 242 | inferred_complete_timeline |
| `Action_None` | 314 | 328 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 38 | 90 | 53 | inferred_complete_timeline |
| `Action_None` | 93 | 123 | 31 | inferred_complete_timeline |
| `Action_None` | 128 | 389 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 383

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 137 | 100 | inferred_complete_timeline |
| `Action_None` | 145 | 389 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–341
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 202 | 165 | inferred_complete_timeline |
| `Action_None` | 204 | 341 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 255 | 218 | inferred_complete_timeline |
| `Action_None` | 262 | 263 | 2 | inferred_complete_timeline |
| `Action_None` | 265 | 280 | 16 | inferred_complete_timeline |
| `Action_None` | 282 | 287 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–367 | 365 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 23–358 | 336 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 48–389 | 335 | 5 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 57–59 | 3 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 59–376 | 316 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 61–131 | 71 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 82–389 | 308 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 101–184 | 13 | 3 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 108–352 | 209 | 10 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 110–307 | 101 | 11 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 121–327 | 195 | 3 | Undefined position; Undefined team |
| `31` | `49` | Position_Unknown | Team_Unknown | 186–339 | 147 | 5 | Undefined position; Undefined team |
| `32` | `50` | Position_Unknown | Team_Unknown | 193–194 | 2 | 1 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 206–207 | 2 | 1 | Undefined position; Undefined team |
| `34` | `56` | Position_Unknown | Team_Unknown | 225–276 | 32 | 6 | Undefined position; Undefined team |
| `35` | `58` | Position_Unknown | Team_Unknown | 266–274 | 9 | 1 | Undefined position; Undefined team |
| `36` | `61` | Position_Unknown | Team_Unknown | 288–291 | 4 | 1 | Undefined position; Undefined team |
| `37` | `62` | Position_Unknown | Team_Unknown | 290–324 | 24 | 5 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 300–319 | 18 | 3 | Undefined position; Undefined team |
| `39` | `65` | Position_Unknown | Team_Unknown | 312–318 | 7 | 1 | Undefined position; Undefined team |
| `40` | `67` | Position_Unknown | Team_Unknown | 332–383 | 23 | 6 | Undefined position; Undefined team |
| `41` | `69` | Position_Unknown | Team_Unknown | 336–345 | 10 | 1 | Undefined position; Undefined team |
| `42` | `72` | Position_Unknown | Team_Unknown | 342–351 | 9 | 2 | Undefined position; Undefined team |
| `43` | `73` | Position_Unknown | Team_Unknown | 342–351 | 10 | 1 | Undefined position; Undefined team |
| `44` | `74` | Position_Unknown | Team_Unknown | 342–343 | 2 | 1 | Undefined position; Undefined team |
| `45` | `75` | Position_Unknown | Team_Unknown | 346–348 | 3 | 1 | Undefined position; Undefined team |
| `46` | `76` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `47` | `77` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `48` | `78` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 154 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 172: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_None' range [38-255] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-280] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-287] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-51] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-304] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-367] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-77] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-67] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-289] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-60] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-312] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-328] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-284] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-88] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-159] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-295] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-137] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-90] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-389] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-245] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-276] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-285] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-304] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-310] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-327] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-353] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-56] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-65] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-367] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-11] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-341] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-341] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [45-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-81] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-177] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-237] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-71] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-361] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-13] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-224] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-358] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-49] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-179] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-97] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-376] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-131] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-158] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-112] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-285] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-304] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-327] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-352] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-134] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-228] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-254] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-299] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-128] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-306] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-327] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-196] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-249] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-339] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-207] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-256] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-274] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-291] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-315] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-310] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-319] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-318] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-336] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-347] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-373] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-345] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-348] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-351] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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