# Play-Annotation-Generator Annotation Review — FieldGoalBlock_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_80`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 139
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 123
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `6` | `6` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | defense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `11` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `13` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `16` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `18` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `19` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `20` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `6` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `7` | `Group` | 0 | START | 0 | 30 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `6` | `6` | 14 | START | 14 | 27 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 37 | START | 37 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher5 | `15` | `15` | 44 | START | 44 | 46 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–106
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PlaceBall` | 14 | 27 | 14 | inferred_complete_timeline |
| `Action_None` | 28 | 44 | 17 | inferred_complete_timeline |
| `Action_None` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_None` | 54 | 67 | 14 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |
| `Action_None` | 77 | 98 | 22 | inferred_complete_timeline |
| `Action_None` | 104 | 106 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_KickBall` | 37 | 44 | 8 | inferred_complete_timeline |
| `Action_None` | 45 | 137 | 93 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 147 | 344 | 198 | inferred_complete_timeline |
| `Action_None` | 347 | 359 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 37 | 218 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |
| `Action_None` | 46 | 48 | 3 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_None` | 77 | 107 | 31 | inferred_complete_timeline |
| `Action_None` | 109 | 337 | 229 | inferred_complete_timeline |
| `Action_None` | 347 | 355 | 9 | inferred_complete_timeline |
| `Action_None` | 358 | 359 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_None` | 37 | 59 | 23 | inferred_complete_timeline |
| `Action_None` | 68 | 127 | 60 | inferred_complete_timeline |
| `Action_None` | 129 | 359 | 231 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 21 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_None` | 37 | 133 | 97 | inferred_complete_timeline |
| `Action_None` | 135 | 359 | 225 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–4
- **Visible Samples:** 5

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 55 | 140 | 86 | inferred_complete_timeline |
| `Action_None` | 142 | 359 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 92 | 56 | inferred_complete_timeline |
| `Action_None` | 97 | 110 | 14 | inferred_complete_timeline |
| `Action_None` | 117 | 238 | 122 | inferred_complete_timeline |
| `Action_None` | 241 | 359 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–148
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 136 | 100 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 143 | 148 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 220 | 184 | inferred_complete_timeline |
| `Action_None` | 228 | 239 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 40 | 4 | inferred_complete_timeline |
| `Action_None` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_None` | 77 | 359 | 283 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 38 | 2 | inferred_complete_timeline |
| `Action_None` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 113 | 359 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 44 | 46 | 3 | inferred_complete_timeline |
| `Action_BlockKick` | 49 | 57 | 9 | inferred_complete_timeline |
| `Action_None` | 58 | 72 | 15 | inferred_complete_timeline |
| `Action_None` | 78 | 80 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 90 | 9 | inferred_complete_timeline |
| `Action_None` | 93 | 94 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 101 | 155 | 55 | inferred_complete_timeline |
| `Action_None` | 159 | 160 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–37
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 37 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–311
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 311 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 239 | 203 | inferred_complete_timeline |
| `Action_None` | 245 | 359 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 359 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 279 | 243 | inferred_complete_timeline |
| `Action_None` | 281 | 359 | 79 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `21` | Position_Unknown | Team_Unknown | 5–6 | 2 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 13–228 | 140 | 5 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 14–359 | 343 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 32–121 | 5 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 32–359 | 295 | 14 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 69–359 | 284 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 95–342 | 248 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 99–325 | 217 | 5 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 144–359 | 213 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 182–359 | 143 | 4 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 221–223 | 3 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 238–248 | 8 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 248–359 | 103 | 4 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 274–316 | 35 | 2 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 290–359 | 56 | 4 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 310–359 | 50 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 113 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [45-137] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-344] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-92] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-110] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-238] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-359] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 37, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [37-37] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-311] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-136] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [28-44] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-52] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-67] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-98] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-106] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-220] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-239] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-75] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 37, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [37-37] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-72] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-337] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-355] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-21] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [44-46] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [49-57] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-80] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-90] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-218] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-59] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-127] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-96] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-156] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-228] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-35] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-117] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-359] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-34] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-121] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-52] for track '25' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-75] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-90] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-102] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-123] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-154] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-222] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-318] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-338] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-350] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-131] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-170] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-342] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-187] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-315] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-237] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-213] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-227] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-223] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-248] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-257] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-359] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-304] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-298] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [307-319] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-359] for track '35' has 3 frames without a visible bounding box.
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

</details>