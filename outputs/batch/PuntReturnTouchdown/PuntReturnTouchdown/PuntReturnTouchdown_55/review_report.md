# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_55

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_55`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 479
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 168
- **Validation Warnings:** 186
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 151
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `18` | `18` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `56` | `39` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `27` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `34` | `27` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner | `12` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `14` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `18` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `19` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `3` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `8` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `9` | `Group` | 0 | START | 0 | 48 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `18` | `18` | 49 | START | 49 | 123 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 73 | END | 73 | 73 |
| ✅ EXACT | `Action_PuntBall` | Punter | `4` | `4` | 124 | START | 124 | 138 |
| ⚠️ START CHANGED | `Action_CatchPunt` | Position_Unknown | `56` | `39` | 220 | START | 346 | 346 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `27` | 245 | START | 245 | 445 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `34` | `27` | 446 | START | 446 | 476 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–262
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 262 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 269 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 296 | 248 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 306 | 312 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_LongSnap` | 49 | 123 | 75 | inferred_complete_timeline |
| `Action_None` | 124 | 264 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–324
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 293 | 245 | inferred_complete_timeline |
| `Action_None` | 295 | 296 | 2 | inferred_complete_timeline |
| `Action_None` | 301 | 303 | 3 | inferred_complete_timeline |
| `Action_None` | 305 | 311 | 7 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |
| `Action_None` | 321 | 324 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 219 | 171 | inferred_complete_timeline |
| `Action_None` | 240 | 254 | 15 | inferred_complete_timeline |
| `Action_None` | 258 | 382 | 125 | inferred_complete_timeline |
| `Action_None` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_SnapReceive` | 73 | 73 | 1 | inferred_complete_timeline |
| `Action_None` | 74 | 123 | 50 | inferred_complete_timeline |
| `Action_PuntBall` | 124 | 138 | 15 | inferred_complete_timeline |
| `Action_None` | 139 | 292 | 154 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–428
- **Visible Samples:** 401

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 374 | 326 | inferred_complete_timeline |
| `Action_None` | 376 | 383 | 8 | inferred_complete_timeline |
| `Action_None` | 411 | 428 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 141 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 131 | 83 | inferred_complete_timeline |
| `Action_None` | 217 | 218 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 220 | 172 | inferred_complete_timeline |
| `Action_None` | 222 | 245 | 24 | inferred_complete_timeline |
| `Action_None` | 247 | 451 | 205 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 479 | 431 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 192 | 144 | inferred_complete_timeline |
| `Action_None` | 194 | 373 | 180 | inferred_complete_timeline |
| `Action_None` | 376 | 383 | 8 | inferred_complete_timeline |
| `Action_None` | 404 | 417 | 14 | inferred_complete_timeline |
| `Action_None` | 421 | 479 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 250 | 202 | inferred_complete_timeline |
| `Action_None` | 257 | 298 | 42 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 304 | 309 | 6 | inferred_complete_timeline |
| `Action_None` | 313 | 314 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–397
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 268 | 220 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |
| `Action_None` | 274 | 383 | 110 | inferred_complete_timeline |
| `Action_None` | 385 | 386 | 2 | inferred_complete_timeline |
| `Action_None` | 390 | 397 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 171 | 123 | inferred_complete_timeline |
| `Action_None` | 173 | 192 | 20 | inferred_complete_timeline |
| `Action_None` | 194 | 479 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 222 | 174 | inferred_complete_timeline |
| `Action_None` | 226 | 229 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 237 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 228 | 180 | inferred_complete_timeline |
| `Action_None` | 230 | 235 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 217 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 49 | 225 | 177 | inferred_complete_timeline |
| `Action_None` | 227 | 253 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 103–104 | 2 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 124–125 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 127–129 | 3 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 130–479 | 334 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 131–465 | 330 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 131–136 | 5 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 213–479 | 246 | 5 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 214–479 | 266 | 4 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 260–468 | 204 | 3 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 266–479 | 213 | 2 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 276–479 | 190 | 6 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 277–479 | 175 | 8 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 286–479 | 188 | 6 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 292–468 | 170 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 299–322 | 22 | 2 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 302–318 | 16 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 319–321 | 3 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 326–479 | 154 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 332–479 | 124 | 8 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 346–479 | 113 | 8 | Undefined position; Undefined team |
| `40` | `58` | Position_Unknown | Team_Unknown | 351–479 | 86 | 11 | Undefined position; Undefined team |
| `41` | `59` | Position_Unknown | Team_Unknown | 355–356 | 2 | 1 | Undefined position; Undefined team |
| `42` | `60` | Position_Unknown | Team_Unknown | 362–479 | 109 | 3 | Undefined position; Undefined team |
| `43` | `65` | Position_Unknown | Team_Unknown | 403–479 | 77 | 1 | Undefined position; Undefined team |
| `44` | `68` | Position_Unknown | Team_Unknown | 436–479 | 44 | 1 | Undefined position; Undefined team |
| `45` | `70` | Position_Unknown | Team_Unknown | 479–479 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_CatchPunt` for actor_track_id `56` (Position_Unknown): Annotated start 220 != Inferred start 346
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Gunner` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punt_Support5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 130 |
| Track-related warning | 1 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_CatchPunt' for track '39' has invalid range: start=346, end=233. Clamping end to start.
- ⚠️ Action 'Action_None' range [49-192] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-373] for track '0' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-383] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-417] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-479] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-250] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-298] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-309] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-225] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-253] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-262] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-292] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-228] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-235] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-222] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-268] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-383] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-397] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-296] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-312] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-220] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-245] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-451] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-269] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-131] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-218] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-171] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-192] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-479] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-293] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-311] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-324] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-217] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-374] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-383] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-428] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-479] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-264] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-219] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-254] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-382] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-129] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-402] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-409] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-417] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-439] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-448] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-465] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-136] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-268] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-317] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-479] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [245-445] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-389] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [393-394] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-468] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-479] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-296] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-312] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-358] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-439] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-445] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-278] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-295] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-303] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-309] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-321] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-346] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-297] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-376] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-413] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-479] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-308] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-468] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-318] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-322] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-313] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-318] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-321] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-373] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-390] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-400] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-407] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-434] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-441] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-448] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-479] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-351] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-356] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-363] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-376] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-441] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-448] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-353] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-357] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-361] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-373] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-382] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-396] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-419] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-439] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-445] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-403] for track '42' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-438] for track '42' has 3 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>