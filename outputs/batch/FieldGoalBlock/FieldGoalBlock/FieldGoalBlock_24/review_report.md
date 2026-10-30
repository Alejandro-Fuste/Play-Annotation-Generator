# Play-Annotation-Generator Annotation Review — FieldGoalBlock_24

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_24`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 419
- **Player Tracks:** 69
- **Ball Tracks:** 0
- **Action Segments:** 230
- **Validation Warnings:** 320
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 4
- **Group Expanded Events:** 5
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 221
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_PlaceBall` | FG_Block_Support3 | defense | `1` | `1` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | defense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `16` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `3` | `Group` | 0 | START | 0 | 0 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `9` | `Group` | 0 | START | 0 | 0 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 1 | START | 1 | 17 |
| ✅ EXACT | `Action_PlaceBall` | FG_Block_Support3 | `1` | `1` | 18 | START | 18 | 29 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 40 | START | 40 | 44 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher3 | `10` | `10` | 45 | START | 45 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 45 | 144 | 100 | inferred_complete_timeline |
| `Action_None` | 146 | 348 | 203 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 108 | 108 | inferred_complete_timeline |
| `Action_None` | 120 | 121 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 182 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_LongSnap` | 1 | 17 | 17 | inferred_complete_timeline |
| `Action_None` | 18 | 97 | 80 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 52 | 52 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |
| `Action_None` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_None` | 83 | 86 | 4 | inferred_complete_timeline |
| `Action_None` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_None` | 111 | 141 | 31 | inferred_complete_timeline |
| `Action_None` | 143 | 159 | 17 | inferred_complete_timeline |
| `Action_None` | 163 | 189 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 347 | 347 | inferred_complete_timeline |
| `Action_None` | 350 | 419 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–195
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 57 | 57 | inferred_complete_timeline |
| `Action_None` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_None` | 73 | 191 | 119 | inferred_complete_timeline |
| `Action_None` | 194 | 195 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 100 | 100 | inferred_complete_timeline |
| `Action_None` | 102 | 135 | 34 | inferred_complete_timeline |
| `Action_None` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_None` | 146 | 147 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 169 | 172 | 4 | inferred_complete_timeline |
| `Action_None` | 174 | 187 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PlaceBall` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_None` | 30 | 419 | 390 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–23
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 23 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–19
- **Visible Samples:** 20

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 19 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_BlockKick` | 45 | 57 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 20 | 20 | inferred_complete_timeline |
| `Action_None` | 22 | 144 | 123 | inferred_complete_timeline |
| `Action_None` | 160 | 167 | 8 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |
| `Action_None` | 174 | 258 | 85 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 264 | 265 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 84 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–393
- **Visible Samples:** 370

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 113 | 113 | inferred_complete_timeline |
| `Action_None` | 116 | 142 | 27 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 196 | 50 | inferred_complete_timeline |
| `Action_None` | 201 | 216 | 16 | inferred_complete_timeline |
| `Action_None` | 218 | 271 | 54 | inferred_complete_timeline |
| `Action_None` | 273 | 276 | 4 | inferred_complete_timeline |
| `Action_None` | 278 | 348 | 71 | inferred_complete_timeline |
| `Action_None` | 353 | 370 | 18 | inferred_complete_timeline |
| `Action_None` | 377 | 388 | 12 | inferred_complete_timeline |
| `Action_None` | 392 | 393 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 0 | 1 | inferred_complete_timeline |
| `Action_None` | 1 | 419 | 419 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–138 | 83 | 4 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–239 | 237 | 5 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–419 | 394 | 14 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–256 | 200 | 15 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 14–47 | 28 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 16–161 | 68 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 42–44 | 3 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 45–50 | 6 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 48–52 | 5 | 1 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 48–52 | 5 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 51–197 | 103 | 9 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 51–52 | 2 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 59–156 | 98 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 75–181 | 105 | 3 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 94–232 | 74 | 14 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 97–129 | 20 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 98–127 | 22 | 4 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 99–205 | 91 | 5 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 107–184 | 61 | 3 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 118–178 | 61 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 125–188 | 62 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 131–147 | 10 | 2 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 141–144 | 4 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 155–185 | 30 | 2 | Undefined position; Undefined team |
| `39` | `51` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `40` | `52` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `41` | `53` | Position_Unknown | Team_Unknown | 189–207 | 18 | 2 | Undefined position; Undefined team |
| `42` | `54` | Position_Unknown | Team_Unknown | 191–216 | 11 | 3 | Undefined position; Undefined team |
| `43` | `56` | Position_Unknown | Team_Unknown | 197–198 | 2 | 1 | Undefined position; Undefined team |
| `44` | `60` | Position_Unknown | Team_Unknown | 272–417 | 136 | 6 | Undefined position; Undefined team |
| `45` | `62` | Position_Unknown | Team_Unknown | 276–280 | 5 | 1 | Undefined position; Undefined team |
| `46` | `66` | Position_Unknown | Team_Unknown | 287–419 | 120 | 3 | Undefined position; Undefined team |
| `47` | `67` | Position_Unknown | Team_Unknown | 288–289 | 2 | 1 | Undefined position; Undefined team |
| `48` | `72` | Position_Unknown | Team_Unknown | 295–317 | 5 | 2 | Undefined position; Undefined team |
| `49` | `79` | Position_Unknown | Team_Unknown | 301–302 | 2 | 1 | Undefined position; Undefined team |
| `50` | `80` | Position_Unknown | Team_Unknown | 303–359 | 49 | 5 | Undefined position; Undefined team |
| `51` | `81` | Position_Unknown | Team_Unknown | 303–320 | 8 | 2 | Undefined position; Undefined team |
| `52` | `86` | Position_Unknown | Team_Unknown | 312–392 | 81 | 1 | Undefined position; Undefined team |
| `53` | `90` | Position_Unknown | Team_Unknown | 327–330 | 4 | 1 | Undefined position; Undefined team |
| `54` | `91` | Position_Unknown | Team_Unknown | 328–330 | 3 | 1 | Undefined position; Undefined team |
| `55` | `96` | Position_Unknown | Team_Unknown | 332–352 | 21 | 1 | Undefined position; Undefined team |
| `56` | `97` | Position_Unknown | Team_Unknown | 335–336 | 2 | 1 | Undefined position; Undefined team |
| `57` | `103` | Position_Unknown | Team_Unknown | 341–357 | 17 | 1 | Undefined position; Undefined team |
| `58` | `108` | Position_Unknown | Team_Unknown | 348–414 | 49 | 9 | Undefined position; Undefined team |
| `59` | `113` | Position_Unknown | Team_Unknown | 350–353 | 4 | 1 | Undefined position; Undefined team |
| `60` | `115` | Position_Unknown | Team_Unknown | 352–416 | 64 | 2 | Undefined position; Undefined team |
| `61` | `117` | Position_Unknown | Team_Unknown | 354–357 | 4 | 1 | Undefined position; Undefined team |
| `62` | `120` | Position_Unknown | Team_Unknown | 357–358 | 2 | 1 | Undefined position; Undefined team |
| `63` | `124` | Position_Unknown | Team_Unknown | 363–398 | 14 | 2 | Undefined position; Undefined team |
| `64` | `125` | Position_Unknown | Team_Unknown | 374–396 | 14 | 2 | Undefined position; Undefined team |
| `65` | `126` | Position_Unknown | Team_Unknown | 378–383 | 6 | 1 | Undefined position; Undefined team |
| `66` | `131` | Position_Unknown | Team_Unknown | 382–391 | 10 | 1 | Undefined position; Undefined team |
| `67` | `134` | Position_Unknown | Team_Unknown | 407–409 | 3 | 1 | Undefined position; Undefined team |
| `68` | `135` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 54 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 54 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 108 |
| Missing visible bounding boxes during action | 206 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 50: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ Row 50: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Action 'Action_None' range [45-144] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-348] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-419] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [18-97] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-52] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-141] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-189] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-419] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-57] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-191] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-195] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-55] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-100] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-149] for track '8' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-167] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-347] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-419] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [45-57] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-113] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-196] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-271] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-276] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-348] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-370] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-388] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-393] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-121] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-174] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-213] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-282] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-310] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-327] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-337] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-355] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-372] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-384] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-84] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-23] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-19] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-20] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-144] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-258] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [1-27] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-36] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-144] for track '18' has 10 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-154] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-172] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-179] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-187] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-199] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-247] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-19] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-40] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-47] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-31] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-117] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-156] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-44] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-50] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-52] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-55] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-64] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-73] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-120] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-197] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-156] for track '27' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-82] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-87] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-181] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-107] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-133] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-197] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-220] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-125] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-108] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-120] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-101] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-138] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-205] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-109] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-128] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-184] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-178] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-184] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-138] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-182] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-192] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-207] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-195] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-200] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-216] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-376] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-384] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-396] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-406] for track '44' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-412] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [416-417] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-280] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-365] for track '46' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-289] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-296] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-317] for track '48' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-313] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-322] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-337] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-344] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-359] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-306] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-392] for track '52' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '53' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-330] for track '54' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-352] for track '55' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [335-336] for track '56' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-357] for track '57' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-350] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-355] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-374] for track '58' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [376-379] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-395] for track '58' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-401] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [404-409] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-414] for track '58' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-353] for track '59' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-405] for track '60' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-416] for track '60' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-357] for track '61' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-358] for track '62' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-366] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-398] for track '63' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '64' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-396] for track '64' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-383] for track '65' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-391] for track '66' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '67' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '68' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '54' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '54' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '55' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '55' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '56' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '56' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '57' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '57' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '58' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '58' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '59' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '59' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '60' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '60' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '61' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '61' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '62' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '62' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '63' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '63' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '64' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '64' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '65' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '65' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '66' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '66' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '67' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '67' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '68' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '68' has undefined team_side. Will map to Team_Unknown.

</details>