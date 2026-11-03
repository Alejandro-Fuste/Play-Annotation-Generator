# Play-Annotation-Generator Annotation Review — PuntBlock_82

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_82`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 120
- **Validation Warnings:** 166
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `5` | `Group` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `5` | `5` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `1` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `10` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `12` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `13` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `14` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `5` | `5` | 24 | END | 24 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `5` | `5` | 50 | START | 50 | 81 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `2` | `2` | 57 | START | 57 | 63 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 243 | 210 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 248 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 318 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 389 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–294
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 294 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 350 | 307 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–381
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 232 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 328 | 77 | inferred_complete_timeline |
| `Action_PreSnap` | 360 | 365 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 369 | 381 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 55 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 152 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 189 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 331 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 357 | 385 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 389 | 389 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 80 | 83 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 24 | 1 | inferred_complete_timeline |
| `Action_None` | 25 | 49 | 25 | inferred_complete_timeline |
| `Action_PuntBall` | 50 | 81 | 32 | inferred_complete_timeline |
| `Action_PuntBall` | 84 | 93 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 112 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 119 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 200 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 242 | 243 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 320 | 64 | inferred_complete_timeline |
| `Action_PreSnap` | 370 | 389 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–77
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 71 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 124 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 126 | 158 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–48
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 48 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PreSnap` | 190 | 207 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 253 | 280 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 321 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_BlockPunt` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_None` | 64 | 86 | 23 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 107 | 8 | inferred_complete_timeline |
| `Action_None` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 128 | 186 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 5–67 | 45 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 30–369 | 340 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 54–55 | 2 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 77–78 | 2 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 77–292 | 216 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 81–388 | 308 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 86–389 | 298 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 90–269 | 180 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 92–211 | 110 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 92–226 | 114 | 5 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 99–389 | 264 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 127–389 | 250 | 4 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 131–187 | 40 | 3 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 195–234 | 39 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 267–389 | 106 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 268–342 | 14 | 2 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 270–299 | 25 | 3 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 271–287 | 8 | 2 | Undefined position; Undefined team |
| `34` | `40` | Position_Unknown | Team_Unknown | 279–342 | 59 | 3 | Undefined position; Undefined team |
| `35` | `41` | Position_Unknown | Team_Unknown | 279–284 | 5 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 291–295 | 5 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 294–389 | 95 | 2 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 298–378 | 70 | 2 | Undefined position; Undefined team |
| `39` | `47` | Position_Unknown | Team_Unknown | 310–389 | 71 | 5 | Undefined position; Undefined team |
| `40` | `49` | Position_Unknown | Team_Unknown | 356–389 | 27 | 3 | Undefined position; Undefined team |
| `41` | `50` | Position_Unknown | Team_Unknown | 367–389 | 23 | 1 | Undefined position; Undefined team |
| `42` | `51` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 108 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-280] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-321] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-350] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-86] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-107] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-186] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-294] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-243] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-248] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-318] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-389] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [50-81] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [84-93] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [190-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-242] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-254] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-320] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-389] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [80-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-77] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-328] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-365] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-381] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-55] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-152] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-189] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-331] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [357-385] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-112] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-119] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-124] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-158] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-67] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-369] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-292] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-388] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [86-134] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-375] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-269] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-171] for track '24' has 9 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [174-179] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-211] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-193] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-226] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-195] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-335] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-351] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-175] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-183] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-318] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [330-389] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-187] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-228] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-234] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [267-305] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-382] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [387-389] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [332-342] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-289] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [293-294] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [271-274] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-287] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-329] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [331-334] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-342] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-281] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-284] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-295] for track '36' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-384] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-363] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-378] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [310-339] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-343] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [347-365] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [369-372] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-389] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [356-358] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [360-365] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [383-389] for track '43' has 2 frames without a visible bounding box.
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

</details>