# Play-Annotation-Generator Annotation Review — FieldGoalBlock_79

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_79`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 359
- **Player Tracks:** 49
- **Ball Tracks:** 0
- **Action Segments:** 212
- **Validation Warnings:** 255
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 11
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 201
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `5` | `5` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | Left_Tackle | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `12` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `15` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `5` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `6` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `5` | `5` | 14 | START | 14 | 28 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 36 | START | 36 | 40 |
| ✅ EXACT | `Action_BlockKick` | Left_Tackle | `9` | `9` | 40 | START | 40 | 49 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PlaceBall` | 14 | 28 | 15 | inferred_complete_timeline |
| `Action_None` | 29 | 63 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_KickBall` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_None` | 41 | 67 | 27 | inferred_complete_timeline |
| `Action_None` | 87 | 91 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 105 | 3 | inferred_complete_timeline |
| `Action_None` | 109 | 128 | 20 | inferred_complete_timeline |
| `Action_None` | 130 | 138 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 58 | 23 | inferred_complete_timeline |
| `Action_None` | 65 | 94 | 30 | inferred_complete_timeline |
| `Action_None` | 96 | 247 | 152 | inferred_complete_timeline |
| `Action_None` | 249 | 359 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BlockKick` | 40 | 49 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 308 | 273 | inferred_complete_timeline |
| `Action_None` | 312 | 325 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 62 | 27 | inferred_complete_timeline |
| `Action_None` | 64 | 206 | 143 | inferred_complete_timeline |
| `Action_None` | 210 | 237 | 28 | inferred_complete_timeline |
| `Action_None` | 243 | 250 | 8 | inferred_complete_timeline |
| `Action_None` | 252 | 259 | 8 | inferred_complete_timeline |
| `Action_None` | 262 | 270 | 9 | inferred_complete_timeline |
| `Action_None` | 275 | 298 | 24 | inferred_complete_timeline |
| `Action_None` | 300 | 302 | 3 | inferred_complete_timeline |
| `Action_None` | 310 | 311 | 2 | inferred_complete_timeline |
| `Action_None` | 317 | 330 | 14 | inferred_complete_timeline |
| `Action_None` | 350 | 359 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 28

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 240 | 205 | inferred_complete_timeline |
| `Action_None` | 243 | 247 | 5 | inferred_complete_timeline |
| `Action_None` | 250 | 254 | 5 | inferred_complete_timeline |
| `Action_None` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_None` | 263 | 270 | 8 | inferred_complete_timeline |
| `Action_None` | 274 | 276 | 3 | inferred_complete_timeline |
| `Action_None` | 278 | 320 | 43 | inferred_complete_timeline |
| `Action_None` | 323 | 325 | 3 | inferred_complete_timeline |
| `Action_None` | 328 | 329 | 2 | inferred_complete_timeline |
| `Action_None` | 338 | 340 | 3 | inferred_complete_timeline |
| `Action_None` | 343 | 359 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–301
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 142 | 107 | inferred_complete_timeline |
| `Action_None` | 148 | 279 | 132 | inferred_complete_timeline |
| `Action_None` | 299 | 301 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 59 | 24 | inferred_complete_timeline |
| `Action_None` | 67 | 73 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 342

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 55 | 20 | inferred_complete_timeline |
| `Action_None` | 64 | 240 | 177 | inferred_complete_timeline |
| `Action_None` | 246 | 247 | 2 | inferred_complete_timeline |
| `Action_None` | 252 | 254 | 3 | inferred_complete_timeline |
| `Action_None` | 256 | 359 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 307

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 22 | 2 | inferred_complete_timeline |
| `Action_None` | 39 | 54 | 16 | inferred_complete_timeline |
| `Action_None` | 68 | 114 | 47 | inferred_complete_timeline |
| `Action_None` | 123 | 183 | 61 | inferred_complete_timeline |
| `Action_None` | 186 | 195 | 10 | inferred_complete_timeline |
| `Action_None` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_None` | 204 | 235 | 32 | inferred_complete_timeline |
| `Action_None` | 239 | 359 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 35 | 19 | inferred_complete_timeline |
| `Action_None` | 36 | 37 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 58 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 107 | 45 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 59 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 36 | 268 | 233 | inferred_complete_timeline |
| `Action_None` | 270 | 300 | 31 | inferred_complete_timeline |
| `Action_None` | 303 | 307 | 5 | inferred_complete_timeline |
| `Action_None` | 313 | 316 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 25 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 28 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_None` | 36 | 48 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 100 | 37 | inferred_complete_timeline |
| `Action_None` | 102 | 104 | 3 | inferred_complete_timeline |
| `Action_None` | 120 | 265 | 146 | inferred_complete_timeline |
| `Action_None` | 268 | 286 | 19 | inferred_complete_timeline |
| `Action_None` | 289 | 299 | 11 | inferred_complete_timeline |
| `Action_None` | 301 | 359 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | Position_Unknown | Team_Unknown | 14–95 | 82 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 17–232 | 216 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 28–42 | 15 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 32–359 | 317 | 8 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 36–314 | 256 | 6 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 70–139 | 69 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 72–239 | 145 | 4 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 77–242 | 163 | 3 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 77–205 | 96 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 87–355 | 215 | 12 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 94–359 | 200 | 10 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 99–359 | 253 | 4 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 106–359 | 254 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 108–359 | 234 | 6 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 109–359 | 217 | 12 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 140–308 | 153 | 7 | Undefined position; Undefined team |
| `33` | `52` | Position_Unknown | Team_Unknown | 174–178 | 5 | 1 | Undefined position; Undefined team |
| `34` | `53` | Position_Unknown | Team_Unknown | 174–202 | 29 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 182–183 | 2 | 1 | Undefined position; Undefined team |
| `36` | `55` | Position_Unknown | Team_Unknown | 186–220 | 35 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 222–223 | 2 | 1 | Undefined position; Undefined team |
| `38` | `60` | Position_Unknown | Team_Unknown | 230–359 | 115 | 6 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 233–243 | 11 | 1 | Undefined position; Undefined team |
| `40` | `62` | Position_Unknown | Team_Unknown | 236–237 | 2 | 1 | Undefined position; Undefined team |
| `41` | `63` | Position_Unknown | Team_Unknown | 240–359 | 98 | 6 | Undefined position; Undefined team |
| `42` | `65` | Position_Unknown | Team_Unknown | 252–293 | 28 | 5 | Undefined position; Undefined team |
| `43` | `66` | Position_Unknown | Team_Unknown | 253–254 | 2 | 1 | Undefined position; Undefined team |
| `44` | `67` | Position_Unknown | Team_Unknown | 258–355 | 82 | 5 | Undefined position; Undefined team |
| `45` | `68` | Position_Unknown | Team_Unknown | 264–265 | 2 | 1 | Undefined position; Undefined team |
| `46` | `70` | Position_Unknown | Team_Unknown | 279–353 | 75 | 1 | Undefined position; Undefined team |
| `47` | `71` | Position_Unknown | Team_Unknown | 281–359 | 79 | 1 | Undefined position; Undefined team |
| `48` | `76` | Position_Unknown | Team_Unknown | 308–359 | 51 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 189 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 160: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action 'Action_None' range [41-67] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-91] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-128] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-308] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-325] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-240] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-247] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-260] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-320] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-340] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-142] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-301] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-55] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-240] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-359] for track '4' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-63] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-27] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-59] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-59] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-73] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [40-49] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-16] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-54] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-195] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-235] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-25] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-28] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-247] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-359] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-48] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-100] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-104] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-265] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-268] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-300] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-307] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-316] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-62] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-206] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-298] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-302] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-311] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-330] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-35] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-58] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-107] for track '16' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-35] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-232] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '19' starts at frame 36, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [36-42] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-54] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-63] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-237] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-265] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-351] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-42] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-61] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-232] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-307] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-131] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-139] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-166] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-239] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-213] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-218] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-242] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-97] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-113] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-240] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-249] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-261] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-273] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-323] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-339] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-355] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-240] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-244] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-247] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-291] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-302] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-316] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-242] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-261] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-359] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-359] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-241] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-256] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-320] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-116] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-237] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-264] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-305] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-356] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-155] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-244] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-262] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-289] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-298] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-308] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-202] for track '34' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-183] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-220] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-241] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '38' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-258] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-279] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-243] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-237] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-250] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-275] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-281] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-254] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-278] for track '42' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-293] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-324] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-337] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-346] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-355] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-265] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-353] for track '46' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-311] for track '48' has 1 frames without a visible bounding box.
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