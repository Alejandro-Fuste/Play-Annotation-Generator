# Play-Annotation-Generator Annotation Review — PuntBlock_66

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_66`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 104
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 80
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | defense | `10` | `10` |
| ✅ EXACT | `Action_SecureRecovery` | Right_Edge_Rusher1 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `0` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `1` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `3` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 15 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `9` | `Group` | 0 | START | 0 | 15 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 16 | START | 16 | 66 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 44 | END | 44 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `4` | `4` | 67 | START | 67 | 95 |
| ✅ EXACT | `Action_BlockPunt` | Right_Edge_Rusher1 | `10` | `10` | 80 | START | 80 | 86 |
| ✅ EXACT | `Action_SecureRecovery` | Right_Edge_Rusher1 | `10` | `10` | 143 | START | 143 | 159 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 180 | 165 | inferred_complete_timeline |
| `Action_None` | 182 | 274 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 73 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–282
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_LongSnap` | 16 | 66 | 51 | inferred_complete_timeline |
| `Action_None` | 67 | 282 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 359 | 344 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 107

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_SnapReceive` | 44 | 44 | 1 | inferred_complete_timeline |
| `Action_None` | 45 | 66 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 67 | 95 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 97 | 107 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–274
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 274 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 170 | 155 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 33 | 18 | inferred_complete_timeline |
| `Action_None` | 39 | 43 | 5 | inferred_complete_timeline |
| `Action_None` | 46 | 201 | 156 | inferred_complete_timeline |
| `Action_None` | 203 | 359 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 40 | 25 | inferred_complete_timeline |
| `Action_None` | 68 | 90 | 23 | inferred_complete_timeline |
| `Action_None` | 93 | 292 | 200 | inferred_complete_timeline |
| `Action_None` | 294 | 301 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 229 | 214 | inferred_complete_timeline |
| `Action_None` | 231 | 324 | 94 | inferred_complete_timeline |
| `Action_None` | 342 | 359 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 27 | 12 | inferred_complete_timeline |
| `Action_None` | 45 | 114 | 70 | inferred_complete_timeline |
| `Action_None` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_None` | 121 | 259 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>Punt_Support1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 16 | 137 | 122 | inferred_complete_timeline |
| `Action_None` | 142 | 212 | 71 | inferred_complete_timeline |
| `Action_None` | 214 | 359 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 43 | 44 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 79 | 35 | inferred_complete_timeline |
| `Action_BlockPunt` | 80 | 86 | 7 | inferred_complete_timeline |
| `Action_None` | 87 | 142 | 56 | inferred_complete_timeline |
| `Action_SecureRecovery` | 143 | 159 | 17 | inferred_complete_timeline |
| `Action_None` | 160 | 359 | 200 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | Position_Unknown | Team_Unknown | 2–29 | 26 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 55–117 | 60 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 56–57 | 2 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 88–243 | 156 | 1 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 88–359 | 244 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 98–153 | 56 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 101–119 | 16 | 3 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 102–103 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 114–232 | 119 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 115–359 | 244 | 2 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 118–248 | 115 | 8 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 119–232 | 112 | 2 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 162–236 | 74 | 2 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 236–257 | 16 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 262–263 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 302–359 | 57 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 330–333 | 4 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 339–359 | 21 | 1 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 343–359 | 5 | 2 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 349–359 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Punt_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 62 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_None' range [67-282] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-170] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [67-95] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [97-107] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-40] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-90] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-292] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-301] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-33] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-201] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-73] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-229] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-274] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-359] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-137] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-212] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-180] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-274] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-27] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-22] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-71] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-243] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-196] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-359] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-153] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-103] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-232] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-340] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-199] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-221] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-244] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-213] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-232] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-233] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-317] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-333] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-346] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>