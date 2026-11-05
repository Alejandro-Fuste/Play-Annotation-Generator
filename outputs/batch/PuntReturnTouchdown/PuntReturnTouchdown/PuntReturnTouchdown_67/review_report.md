# Play-Annotation-Generator Annotation Review — PuntReturnTouchdown_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntReturnTouchdown_67`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_SpecialTeams_PuntReturnTouchdown`
- **Result:** `Result_Unknown`
- **Result Frame:** 569
- **Player Tracks:** 56
- **Ball Tracks:** 0
- **Action Segments:** 262
- **Validation Warnings:** 317
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
- **Inferred Coverage Segments (Action_None):** 247
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `13` | `13` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `15` | `15` |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | Team_Unknown | `34` | `30` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `34` | `30` |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | Team_Unknown | `34` | `30` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner1 | `0` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `13` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `15` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `4` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Gunner3 | `6` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `8` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `9` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `13` | `13` | 50 | START | 50 | 98 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `15` | `15` | 78 | END | 78 | 78 |
| ✅ EXACT | `Action_PuntBall` | Punter | `15` | `15` | 99 | START | 99 | 115 |
| ✅ EXACT | `Action_CatchPunt` | Position_Unknown | `34` | `30` | 218 | START | 218 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `34` | `30` | 241 | START | 241 | 241 |
| ✅ EXACT | `Action_CrossGoalLine` | Position_Unknown | `34` | `30` | 565 | START | 565 | 568 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 565

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 286 | 237 | inferred_complete_timeline |
| `Action_None` | 288 | 368 | 81 | inferred_complete_timeline |
| `Action_None` | 370 | 388 | 19 | inferred_complete_timeline |
| `Action_None` | 391 | 395 | 5 | inferred_complete_timeline |
| `Action_None` | 397 | 569 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_LongSnap` | 50 | 98 | 49 | inferred_complete_timeline |
| `Action_None` | 99 | 294 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 139 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–115
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 115 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–452
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 208 | 159 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 322 | 86 | inferred_complete_timeline |
| `Action_None` | 327 | 356 | 30 | inferred_complete_timeline |
| `Action_None` | 359 | 437 | 79 | inferred_complete_timeline |
| `Action_None` | 445 | 452 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 78 | 1 | inferred_complete_timeline |
| `Action_None` | 79 | 98 | 20 | inferred_complete_timeline |
| `Action_PuntBall` | 99 | 115 | 17 | inferred_complete_timeline |
| `Action_None` | 116 | 124 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–430
- **Visible Samples:** 402

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 86 | 37 | inferred_complete_timeline |
| `Action_None` | 94 | 280 | 187 | inferred_complete_timeline |
| `Action_None` | 283 | 314 | 32 | inferred_complete_timeline |
| `Action_None` | 317 | 318 | 2 | inferred_complete_timeline |
| `Action_None` | 320 | 323 | 4 | inferred_complete_timeline |
| `Action_None` | 335 | 401 | 67 | inferred_complete_timeline |
| `Action_None` | 408 | 430 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 236 | 187 | inferred_complete_timeline |
| `Action_None` | 238 | 278 | 41 | inferred_complete_timeline |
| `Action_None` | 327 | 330 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Gunner3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 327 | 278 | inferred_complete_timeline |
| `Action_None` | 335 | 366 | 32 | inferred_complete_timeline |
| `Action_None` | 370 | 371 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 569 | 197 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 63 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 105 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_None` | 81 | 101 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–83
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 80 | 31 | inferred_complete_timeline |
| `Action_None` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–466
- **Visible Samples:** 428

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 115 | 66 | inferred_complete_timeline |
| `Action_None` | 120 | 225 | 106 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 231 | 257 | 27 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 278 | 386 | 109 | inferred_complete_timeline |
| `Action_None` | 390 | 391 | 2 | inferred_complete_timeline |
| `Action_None` | 403 | 466 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 74 | 25 | inferred_complete_timeline |
| `Action_None` | 82 | 92 | 11 | inferred_complete_timeline |
| `Action_None` | 94 | 98 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 104 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–80
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 80 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–565 | 546 | 7 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–84 | 85 | 2 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–81 | 82 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–330 | 317 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–499 | 372 | 22 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 70–107 | 36 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 89–131 | 39 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 97–187 | 90 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 106–197 | 89 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 121–169 | 46 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 122–262 | 141 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 122–135 | 14 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 126–206 | 81 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 135–146 | 7 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 141–568 | 398 | 16 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 161–465 | 296 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 184–370 | 153 | 10 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 209–521 | 288 | 15 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 222–569 | 308 | 4 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 226–469 | 227 | 9 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 231–246 | 8 | 2 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 245–332 | 87 | 2 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 259–295 | 37 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 262–390 | 61 | 10 | Undefined position; Undefined team |
| `40` | `53` | Position_Unknown | Team_Unknown | 274–565 | 268 | 12 | Undefined position; Undefined team |
| `41` | `54` | Position_Unknown | Team_Unknown | 276–531 | 231 | 9 | Undefined position; Undefined team |
| `42` | `55` | Position_Unknown | Team_Unknown | 278–280 | 3 | 1 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 282–511 | 230 | 1 | Undefined position; Undefined team |
| `44` | `57` | Position_Unknown | Team_Unknown | 293–485 | 192 | 2 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 303–569 | 245 | 9 | Undefined position; Undefined team |
| `46` | `60` | Position_Unknown | Team_Unknown | 319–428 | 110 | 1 | Undefined position; Undefined team |
| `47` | `62` | Position_Unknown | Team_Unknown | 324–325 | 2 | 1 | Undefined position; Undefined team |
| `48` | `64` | Position_Unknown | Team_Unknown | 332–335 | 4 | 1 | Undefined position; Undefined team |
| `49` | `66` | Position_Unknown | Team_Unknown | 352–569 | 217 | 2 | Undefined position; Undefined team |
| `50` | `68` | Position_Unknown | Team_Unknown | 372–497 | 106 | 6 | Undefined position; Undefined team |
| `51` | `70` | Position_Unknown | Team_Unknown | 380–569 | 186 | 3 | Undefined position; Undefined team |
| `52` | `71` | Position_Unknown | Team_Unknown | 393–569 | 177 | 1 | Undefined position; Undefined team |
| `53` | `72` | Position_Unknown | Team_Unknown | 414–490 | 48 | 6 | Undefined position; Undefined team |
| `54` | `75` | Position_Unknown | Team_Unknown | 485–548 | 46 | 8 | Undefined position; Undefined team |
| `55` | `82` | Position_Unknown | Team_Unknown | 530–563 | 9 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `34` (10 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Gunner1` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Gunner3` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Edge_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Left_Edge_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Edge_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ 40 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 40 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 80 |
| Missing visible bounding boxes during action | 231 |
| Track-related warning | 3 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 135: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 136: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [50-236] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-278] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-296] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-306] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-548] for track '1' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-558] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-565] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-84] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-327] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-366] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-371] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-80] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-83] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-208] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-322] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-356] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-437] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-452] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-286] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-368] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-388] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-395] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-569] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-92] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-280] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-314] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-401] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-430] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [50-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-225] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-257] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-386] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-466] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-124] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-81] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-170] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-325] for track '16' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-105] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-73] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-101] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-63] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-11] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-39] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-65] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-141] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-189] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-366] for track '20' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-486] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-494] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [496-499] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-104] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-131] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-187] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-113] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-197] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-262] for track '26' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-135] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-212] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-237] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '30' starts at frame 241, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [241-241] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [244-296] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [301-302] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-314] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [319-322] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-346] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-420] for track '30' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [422-551] for track '30' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_CrossGoalLine' range [565-568] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-282] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-465] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-206] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-261] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-268] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-333] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-344] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-348] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-355] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-370] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-333] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-345] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-362] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-365] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-396] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-407] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-423] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-432] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-435] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-450] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-513] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-521] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-232] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-325] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-350] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-569] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-299] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-305] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-406] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-416] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-431] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-451] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-463] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-469] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-246] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-248] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-332] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-295] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-293] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-300] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-363] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-381] for track '39' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-386] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-296] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-335] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-368] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-497] for track '40' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [499-502] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [505-519] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-535] for track '40' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-543] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-546] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-559] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [561-565] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-344] for track '41' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-347] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-374] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-384] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-462] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-526] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-511] for track '43' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-448] for track '44' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-485] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-305] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-343] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-356] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-521] for track '45' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [529-548] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-555] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-558] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [560-565] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-428] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-335] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-377] for track '49' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-417] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-426] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-466] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-485] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-497] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-393] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-398] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-569] for track '51' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-415] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-425] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [428-455] for track '53' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-486] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-491] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-499] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-505] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [515-531] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-537] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-548] for track '54' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-531] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [534-536] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-539] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [562-563] for track '55' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

</details>