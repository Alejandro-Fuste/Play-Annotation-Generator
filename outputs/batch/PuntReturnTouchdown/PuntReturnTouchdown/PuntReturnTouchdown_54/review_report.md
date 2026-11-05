# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_54`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 45
- **Ball Tracks:** 1
- **Action Segments:** 160
- **Validation Warnings:** 178
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `16` | `16` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `1` | `1` |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | defense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | defense | `19` | `19` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `27` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `1` | `Group` | 23 | START | 23 | 67 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `16` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `17` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `18` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `21` | `Group` | 23 | START | 23 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 23 | START | 23 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `6` | `Group` | 23 | START | 23 | 45 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `16` | `16` | 46 | START | 46 | 64 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `1` | `1` | 68 | END | 68 | 68 |
| ✅ EXACT | `Action_PuntBall` | Punter | `1` | `1` | 94 | START | 94 | 109 |
| ✅ EXACT | `Action_CatchPunt` | Punt_Returner | `19` | `19` | 167 | START | 167 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Punt_Returner | `19` | `19` | 203 | START | 203 | 257 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `27` | `26` | 360 | START | 360 | 365 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 129 | 84 | inferred_complete_timeline |
| `Action_None` | 131 | 389 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 23–304
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 83 | 38 | inferred_complete_timeline |
| `Action_None` | 86 | 107 | 22 | inferred_complete_timeline |
| `Action_None` | 120 | 151 | 32 | inferred_complete_timeline |
| `Action_None` | 154 | 304 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 23–111
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 96 | 51 | inferred_complete_timeline |
| `Action_None` | 99 | 111 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_LongSnap` | 46 | 64 | 19 | inferred_complete_timeline |
| `Action_LongSnap` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 85 | 93 | 9 | inferred_complete_timeline |
| `Action_None` | 94 | 214 | 121 | inferred_complete_timeline |
| `Action_None` | 219 | 249 | 31 | inferred_complete_timeline |
| `Action_None` | 255 | 389 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 23–228
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_None` | 94 | 114 | 21 | inferred_complete_timeline |
| `Action_None` | 116 | 133 | 18 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 228 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 23–216
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 142 | 97 | inferred_complete_timeline |
| `Action_None` | 144 | 192 | 49 | inferred_complete_timeline |
| `Action_None` | 195 | 216 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 67 | 45 | inferred_complete_timeline |
| `Action_SnapReceive` | 68 | 68 | 1 | inferred_complete_timeline |
| `Action_None` | 69 | 93 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 357 | 248 | inferred_complete_timeline |
| `Action_None` | 366 | 367 | 2 | inferred_complete_timeline |
| `Action_None` | 370 | 389 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_None` | 83 | 109 | 27 | inferred_complete_timeline |
| `Action_None` | 112 | 155 | 44 | inferred_complete_timeline |
| `Action_None` | 159 | 257 | 99 | inferred_complete_timeline |
| `Action_None` | 261 | 389 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 23–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 131 | 86 | inferred_complete_timeline |
| `Action_None` | 133 | 166 | 34 | inferred_complete_timeline |
| `Action_None` | 171 | 389 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 23–34
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 34 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 23–389
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 44 | 22 | inferred_complete_timeline |
| `Action_None` | 47 | 53 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 143 | 29 | inferred_complete_timeline |
| `Action_None` | 147 | 219 | 73 | inferred_complete_timeline |
| `Action_None` | 228 | 342 | 115 | inferred_complete_timeline |
| `Action_None` | 351 | 389 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 23–62
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 62 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 23–335
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 60 | 15 | inferred_complete_timeline |
| `Action_None` | 88 | 104 | 17 | inferred_complete_timeline |
| `Action_None` | 107 | 284 | 178 | inferred_complete_timeline |
| `Action_None` | 286 | 296 | 11 | inferred_complete_timeline |
| `Action_None` | 299 | 335 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 23–100
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 88 | 43 | inferred_complete_timeline |
| `Action_None` | 94 | 100 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Returner — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 23–328
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 96 | 74 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 166 | 50 | inferred_complete_timeline |
| `Action_CatchPunt` | 167 | 174 | 8 | inferred_complete_timeline |
| `Action_None` | 175 | 202 | 28 | inferred_complete_timeline |
| `Action_BallCarry` | 203 | 257 | 55 | inferred_complete_timeline |
| `Action_BallCarry` | 260 | 301 | 42 | inferred_complete_timeline |
| `Action_BallCarry` | 305 | 328 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 23–389
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 115 | 70 | inferred_complete_timeline |
| `Action_None` | 117 | 214 | 98 | inferred_complete_timeline |
| `Action_None` | 232 | 285 | 54 | inferred_complete_timeline |
| `Action_None` | 294 | 371 | 78 | inferred_complete_timeline |
| `Action_None` | 373 | 389 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 23–307
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 164 | 119 | inferred_complete_timeline |
| `Action_None` | 169 | 255 | 87 | inferred_complete_timeline |
| `Action_None` | 258 | 286 | 29 | inferred_complete_timeline |
| `Action_None` | 288 | 295 | 8 | inferred_complete_timeline |
| `Action_None` | 301 | 307 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 23–295
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 204 | 159 | inferred_complete_timeline |
| `Action_None` | 206 | 295 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 23–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 92 | 47 | inferred_complete_timeline |
| `Action_None` | 101 | 175 | 75 | inferred_complete_timeline |
| `Action_None` | 178 | 283 | 106 | inferred_complete_timeline |
| `Action_None` | 286 | 289 | 4 | inferred_complete_timeline |
| `Action_None` | 293 | 389 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 23–389
- **Visible Samples:** 354

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 45 | 23 | inferred_complete_timeline |
| `Action_None` | 46 | 66 | 21 | inferred_complete_timeline |
| `Action_None` | 69 | 122 | 54 | inferred_complete_timeline |
| `Action_None` | 126 | 151 | 26 | inferred_complete_timeline |
| `Action_None` | 159 | 336 | 178 | inferred_complete_timeline |
| `Action_None` | 338 | 389 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 23–101 | 79 | 2 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 23–272 | 242 | 4 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 26–63 | 20 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 77–79 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 82–351 | 243 | 8 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 97–98 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 101–389 | 286 | 4 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 105–112 | 8 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 129–318 | 187 | 3 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 161–182 | 15 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 181–186 | 6 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 202–389 | 185 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 210–389 | 180 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 227–228 | 2 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 235–389 | 151 | 3 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 244–245 | 2 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 269–389 | 108 | 3 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 272–303 | 6 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 279–288 | 6 | 3 | Undefined position; Undefined team |
| `39` | `48` | Position_Unknown | Team_Unknown | 313–389 | 77 | 1 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 335–380 | 37 | 4 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 337–389 | 53 | 1 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 350–389 | 40 | 1 | Undefined position; Undefined team |
| `43` | `55` | Position_Unknown | Team_Unknown | 353–389 | 37 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 385–389 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `44` | `56` | 353 | 355 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punt_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Punt_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Punt_Returner` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Right_Wing` position mapped to `offense` team
- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 125 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [46-96] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-357] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-367] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-204] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-295] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-192] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-216] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-164] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-255] for track '4' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-307] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-129] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-389] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-115] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-214] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-285] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-371] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-389] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-66] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-336] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-389] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-159] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-104] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-284] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-296] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-335] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-92] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-289] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-131] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-166] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-83] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-107] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-151] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-304] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [46-64] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [85-93] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 94, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [94-214] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-249] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-109] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-155] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-92] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-114] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-133] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-228] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-96] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-107] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [109-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-115] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [203-257] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [260-301] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [305-328] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-53] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-143] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-219] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-342] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-34] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-28] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-44] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-164] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-183] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-203] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-279] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-306] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-351] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-359] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' for track '26' starts at frame 360, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_CrossGoalLine' range [360-365] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-382] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-112] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-318] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-256] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-371] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-250] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-294] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-389] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-289] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-323] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-274] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-280] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-340] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-363] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-380] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-389] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>