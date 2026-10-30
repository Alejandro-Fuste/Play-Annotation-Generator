# Play-Annotation-Generator Annotation Review — FieldGoalBlock_137

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_137`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 132
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 108
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BlockKick` | Interior_Rusher2 | defense | `13` | `13` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `0` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `1` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `11` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `15` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `9` | `Group` | 0 | START | 0 | 23 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `9` | `9` | 24 | START | 24 | 34 |
| ✅ EXACT | `Action_KickBall` | Kicker | `8` | `8` | 46 | START | 46 | 51 |
| ❌ MISSING SEGMENT | `Action_BlockKick` | Interior_Rusher2 | `13` | `13` | 81 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_PlaceBall` | 24 | 34 | 11 | inferred_complete_timeline |
| `Action_None` | 35 | 239 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_KickBall` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_None` | 52 | 239 | 188 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 148 | 103 | inferred_complete_timeline |
| `Action_None` | 150 | 236 | 87 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 28 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 36 | 6 | inferred_complete_timeline |
| `Action_None` | 50 | 54 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 163 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 68 | 23 | inferred_complete_timeline |
| `Action_None` | 70 | 79 | 10 | inferred_complete_timeline |
| `Action_None` | 85 | 88 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 158 | 113 | inferred_complete_timeline |
| `Action_None` | 172 | 174 | 3 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 218 | 37 | inferred_complete_timeline |
| `Action_None` | 225 | 230 | 6 | inferred_complete_timeline |
| `Action_None` | 234 | 237 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 156 | 111 | inferred_complete_timeline |
| `Action_None` | 159 | 165 | 7 | inferred_complete_timeline |
| `Action_None` | 167 | 168 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 172 | 2 | inferred_complete_timeline |
| `Action_None` | 186 | 207 | 22 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 220 | 175 | inferred_complete_timeline |
| `Action_None` | 224 | 226 | 3 | inferred_complete_timeline |
| `Action_None` | 228 | 236 | 9 | inferred_complete_timeline |
| `Action_None` | 238 | 239 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 156 | 111 | inferred_complete_timeline |
| `Action_None` | 164 | 176 | 13 | inferred_complete_timeline |
| `Action_None` | 178 | 239 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–59
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 59 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–34
- **Visible Samples:** 33

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 34 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 136 | 91 | inferred_complete_timeline |
| `Action_None` | 162 | 165 | 4 | inferred_complete_timeline |
| `Action_None` | 167 | 239 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 239 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_None` | 46 | 154 | 109 | inferred_complete_timeline |
| `Action_None` | 161 | 165 | 5 | inferred_complete_timeline |
| `Action_None` | 170 | 186 | 17 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |
| `Action_None` | 205 | 206 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 15–181 | 161 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 27–53 | 22 | 4 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 38–64 | 17 | 5 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 55–227 | 109 | 5 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 69–89 | 19 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 74–132 | 58 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 86–188 | 71 | 5 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 91–239 | 95 | 4 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 92–122 | 17 | 4 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 92–150 | 47 | 4 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 111–239 | 126 | 2 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 122–234 | 107 | 4 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 142–181 | 37 | 3 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 166–239 | 72 | 3 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 172–239 | 65 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 202–203 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BlockKick` on target `13` (Interior_Rusher2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Tackle` position mapped to `offense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 96 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_BlockKick' for track '13' has invalid range: start=81, end=59. Clamping end to start.
- ⚠️ Action 'Action_None' range [46-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-236] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-163] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-156] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-156] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-207] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-220] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-136] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-165] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-239] for track '6' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-186] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-31] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-34] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-68] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-88] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-218] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-230] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-237] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-59] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-14] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-28] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-54] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-34] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-45] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-181] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-48] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-53] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-51] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-61] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-96] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-162] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-227] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-74] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-89] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-128] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-110] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-128] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-158] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-98] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-143] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-217] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-122] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-128] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-181] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-223] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-239] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-182] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '32' has 1 frames without a visible bounding box.
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

</details>