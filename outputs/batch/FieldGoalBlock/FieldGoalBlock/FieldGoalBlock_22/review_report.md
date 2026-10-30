# Play-Annotation-Generator Annotation Review — FieldGoalBlock_22

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_22`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 146
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 122
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `5` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher6 | defense | `17` | `17` |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher3 | defense | `8` | `8` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | Team_Unknown | `30` | `26` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `10` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `18` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `2` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `20` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `3` | `Group` | 0 | START | 0 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `5` | `Group` | 0 | START | 0 | 7 |
| ✅ EXACT | `Action_LongSnap` | Interior_Rusher6 | `17` | `17` | 8 | START | 8 | 23 |
| ✅ EXACT | `Action_PlaceBall` | Interior_Rusher3 | `8` | `8` | 24 | START | 24 | 41 |
| ✅ EXACT | `Action_KickBall` | Kicker | `2` | `2` | 47 | START | 47 | 54 |
| ✅ EXACT | `Action_BlockKick` | Position_Unknown | `30` | `26` | 52 | START | 52 | 57 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_KickBall` | 47 | 54 | 8 | inferred_complete_timeline |
| `Action_None` | 55 | 185 | 131 | inferred_complete_timeline |
| `Action_None` | 187 | 269 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 119 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 269 | 262 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 108 | 123 | 16 | inferred_complete_timeline |
| `Action_None` | 127 | 269 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 24

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 19 | 12 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 154 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 56 | 49 | inferred_complete_timeline |
| `Action_None` | 65 | 269 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 35 | 28 | inferred_complete_timeline |
| `Action_None` | 37 | 53 | 17 | inferred_complete_timeline |
| `Action_None` | 58 | 269 | 212 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 49 | 21 | inferred_complete_timeline |
| `Action_None` | 58 | 59 | 2 | inferred_complete_timeline |
| `Action_None` | 65 | 269 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PlaceBall` | 24 | 41 | 18 | inferred_complete_timeline |
| `Action_None` | 42 | 200 | 159 | inferred_complete_timeline |
| `Action_None` | 206 | 224 | 19 | inferred_complete_timeline |
| `Action_None` | 227 | 228 | 2 | inferred_complete_timeline |
| `Action_None` | 239 | 269 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 262

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 77 | 70 | inferred_complete_timeline |
| `Action_None` | 84 | 117 | 34 | inferred_complete_timeline |
| `Action_None` | 119 | 263 | 145 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 25 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 8 | 23 | 16 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_None` | 35 | 68 | 34 | inferred_complete_timeline |
| `Action_None` | 72 | 73 | 2 | inferred_complete_timeline |
| `Action_None` | 77 | 87 | 11 | inferred_complete_timeline |
| `Action_None` | 89 | 208 | 120 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 243 | 245 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 85 | 78 | inferred_complete_timeline |
| `Action_None` | 88 | 133 | 46 | inferred_complete_timeline |
| `Action_None` | 137 | 269 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–28
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_None` | 8 | 21 | 14 | inferred_complete_timeline |
| `Action_None` | 26 | 28 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–269 | 262 | 4 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–269 | 257 | 4 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–239 | 239 | 3 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–269 | 270 | 2 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–269 | 241 | 7 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–223 | 216 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–269 | 182 | 7 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 3–34 | 25 | 4 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 22–269 | 167 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 29–40 | 9 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 40–95 | 37 | 7 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 43–64 | 20 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 69–208 | 92 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 69–269 | 194 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 85–269 | 168 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 102–141 | 21 | 3 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 113–269 | 80 | 5 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 173–177 | 5 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 176–179 | 4 | 1 | Undefined position; Undefined team |
| `35` | `52` | Position_Unknown | Team_Unknown | 198–200 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Right_Guard` position mapped to `offense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 98 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 46: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
- ⚠️ Row 46: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [8-244] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-252] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-64] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-94] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-185] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-85] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-133] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-119] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-158] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-56] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-224] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-269] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-154] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-186] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-224] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-251] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-269] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-117] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-263] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-21] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-28] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-269] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-25] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-21] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-59] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-68] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-87] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-208] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-245] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-35] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-123] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-269] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-217] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-223] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-19] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-41] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [8-44] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-177] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 8, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [8-10] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-34] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-27] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-38] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-163] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-177] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-40] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-56] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-84] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-51] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [52-57] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-64] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-269] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-137] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-118] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-138] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-120] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-165] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-269] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-177] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>