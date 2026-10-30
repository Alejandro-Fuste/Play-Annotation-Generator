# Play-Annotation-Generator Annotation Review — FieldGoalBlock_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_112`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 389
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 146
- **Validation Warnings:** 187
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 6
- **Exact Matches:** 1
- **Group Expanded Events:** 3
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 141
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `6` | `6` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher4 | defense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ EXACT | `Action_PlaceBall` | Holder | `6` | `6` | 18 | START | 18 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `13` | `Group` | 18 | START | 18 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 18 | START | 18 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `6` | `Group` | 18 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_KickBall` | Kicker | `2` | `2` | 41 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Interior_Rusher4 | `9` | `9` | 47 | START | 47 | 48 |

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
- **Visible Frames:** 18–389
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PlaceBall` | 18 | 29 | 12 | inferred_complete_timeline |
| `Action_None` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_None` | 47 | 105 | 59 | inferred_complete_timeline |
| `Action_None` | 116 | 187 | 72 | inferred_complete_timeline |
| `Action_None` | 190 | 360 | 171 | inferred_complete_timeline |
| `Action_None` | 368 | 373 | 6 | inferred_complete_timeline |
| `Action_None` | 375 | 389 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 18–25
- **Visible Samples:** 8

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 25 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 18–307
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 29 | 4 | inferred_complete_timeline |
| `Action_None` | 62 | 87 | 26 | inferred_complete_timeline |
| `Action_None` | 129 | 187 | 59 | inferred_complete_timeline |
| `Action_None` | 190 | 307 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 18–222
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 222 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 18–389
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 159 | 119 | inferred_complete_timeline |
| `Action_None` | 164 | 180 | 17 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 389 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 18–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 154 | 114 | inferred_complete_timeline |
| `Action_None` | 156 | 389 | 234 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 18–78
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 46 | 29 | inferred_complete_timeline |
| `Action_BlockKick` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_BlockKick` | 52 | 57 | 6 | inferred_complete_timeline |
| `Action_None` | 62 | 67 | 6 | inferred_complete_timeline |
| `Action_None` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 72 | 78 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 18–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 102 | 62 | inferred_complete_timeline |
| `Action_None` | 104 | 389 | 286 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 18–389
- **Visible Samples:** 372

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 389 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 18–33
- **Visible Samples:** 16

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 33 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 18–72
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 72 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 18–204
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 40 | 23 | inferred_complete_timeline |
| `Action_None` | 41 | 104 | 64 | inferred_complete_timeline |
| `Action_None` | 106 | 184 | 79 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 18–35
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 35 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 18–182 | 144 | 7 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 19–31 | 13 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 20–155 | 103 | 7 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 22–357 | 270 | 6 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 26–30 | 5 | 1 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 36–67 | 32 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 41–306 | 211 | 4 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 45–389 | 328 | 8 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 50–82 | 33 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 51–389 | 338 | 2 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 66–87 | 22 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 69–354 | 258 | 9 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 78–301 | 223 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 79–373 | 266 | 6 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 79–85 | 7 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 84–353 | 262 | 7 | Undefined position; Undefined team |
| `29` | `42` | Position_Unknown | Team_Unknown | 101–389 | 145 | 13 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 103–389 | 279 | 5 | Undefined position; Undefined team |
| `31` | `45` | Position_Unknown | Team_Unknown | 120–297 | 178 | 1 | Undefined position; Undefined team |
| `32` | `47` | Position_Unknown | Team_Unknown | 122–140 | 18 | 2 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 137–389 | 237 | 3 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 178–387 | 210 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 212–369 | 146 | 6 | Undefined position; Undefined team |
| `36` | `53` | Position_Unknown | Team_Unknown | 214–389 | 155 | 2 | Undefined position; Undefined team |
| `37` | `54` | Position_Unknown | Team_Unknown | 224–294 | 71 | 1 | Undefined position; Undefined team |
| `38` | `63` | Position_Unknown | Team_Unknown | 347–363 | 15 | 2 | Undefined position; Undefined team |
| `39` | `64` | Position_Unknown | Team_Unknown | 348–359 | 7 | 2 | Undefined position; Undefined team |
| `40` | `65` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_KickBall` on target `2` (Kicker)
- ⚠️ Ambiguous match for action `Action_BlockKick` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Left_Guard` position mapped to `offense` team
- ⚠️ 28 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 28 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 56 |
| Missing visible bounding boxes during action | 128 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 226: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Segment 'Action_KickBall' for track '2' has invalid range: start=41, end=25. Clamping end to start.
- ⚠️ Action 'Action_None' range [41-222] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-51] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-69] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-79] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-167] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-25] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-35] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-154] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-159] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-389] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-42] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-105] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-187] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-360] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-373] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-389] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-389] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-104] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-184] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [47-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [52-57] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-67] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-78] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-33] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-29] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-187] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-307] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-31] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [20-25] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 41, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [41-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-55] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-73] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-155] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-47] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-282] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-319] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-357] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-30] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-186] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-271] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-306] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-105] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-190] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-376] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-82] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-312] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-87] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-206] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-298] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-307] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-342] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-354] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-127] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-301] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-80] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-96] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-314] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-362] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-373] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-127] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-214] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-286] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-318] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-353] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-127] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-145] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-202] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-298] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-312] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-356] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-377] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-111] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-117] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-223] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-389] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-297] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-124] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-140] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-387] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-322] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-331] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-366] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-369] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-365] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-294] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-357] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-363] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [348-352] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>