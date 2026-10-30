# Play-Annotation-Generator Annotation Review — FieldGoalBlock_90

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_90`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 269
- **Player Tracks:** 41
- **Ball Tracks:** 1
- **Action Segments:** 160
- **Validation Warnings:** 175
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 144
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `4` | `4` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | Team_Unknown | `20` | `19` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `14` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `15` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `17` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `4` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `8` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `4` | `4` | 15 | START | 15 | 28 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 40 | START | 40 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Position_Unknown | `20` | `19` | 44 | START | 44 | 52 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–91
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PlaceBall` | 15 | 28 | 14 | inferred_complete_timeline |
| `Action_None` | 29 | 91 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_KickBall` | 40 | 44 | 5 | inferred_complete_timeline |
| `Action_None` | 45 | 86 | 42 | inferred_complete_timeline |
| `Action_None` | 91 | 165 | 75 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–58
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 57 | 58 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 54 | 55 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 72 | 33 | inferred_complete_timeline |
| `Action_None` | 99 | 187 | 89 | inferred_complete_timeline |
| `Action_None` | 194 | 269 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_None` | 56 | 269 | 214 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–65
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 39 | 3 | inferred_complete_timeline |
| `Action_None` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_None` | 57 | 60 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 39 | 10 | inferred_complete_timeline |
| `Action_None` | 40 | 114 | 75 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |
| `Action_None` | 137 | 269 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–264
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 39 | 7 | inferred_complete_timeline |
| `Action_None` | 40 | 49 | 10 | inferred_complete_timeline |
| `Action_None` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_None` | 60 | 70 | 11 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |
| `Action_None` | 116 | 127 | 12 | inferred_complete_timeline |
| `Action_None` | 130 | 227 | 98 | inferred_complete_timeline |
| `Action_None` | 229 | 264 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 115 | 76 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 125 | 147 | 23 | inferred_complete_timeline |
| `Action_None` | 150 | 175 | 26 | inferred_complete_timeline |
| `Action_None` | 177 | 183 | 7 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 147 | 108 | inferred_complete_timeline |
| `Action_None` | 150 | 193 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 168 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–166
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 37 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 39 | 1 | inferred_complete_timeline |
| `Action_None` | 40 | 54 | 15 | inferred_complete_timeline |
| `Action_None` | 56 | 161 | 106 | inferred_complete_timeline |
| `Action_None` | 163 | 166 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 7 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 12 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_None` | 42 | 52 | 11 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 39 | 8 | inferred_complete_timeline |
| `Action_None` | 40 | 117 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 113 | 74 | inferred_complete_timeline |
| `Action_None` | 120 | 174 | 55 | inferred_complete_timeline |
| `Action_None` | 193 | 227 | 35 | inferred_complete_timeline |
| `Action_None` | 242 | 260 | 19 | inferred_complete_timeline |
| `Action_None` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_None` | 266 | 269 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 124 | 85 | inferred_complete_timeline |
| `Action_None` | 129 | 190 | 62 | inferred_complete_timeline |
| `Action_None` | 193 | 254 | 62 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–155 | 148 | 5 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–269 | 225 | 9 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 8–74 | 45 | 5 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 28–269 | 233 | 6 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 46–269 | 176 | 7 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 48–129 | 30 | 5 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 52–89 | 25 | 6 | Undefined position; Undefined team |
| `25` | `38` | Position_Unknown | Team_Unknown | 87–269 | 183 | 1 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 99–240 | 141 | 2 | Undefined position; Undefined team |
| `27` | `41` | Position_Unknown | Team_Unknown | 104–269 | 152 | 5 | Undefined position; Undefined team |
| `28` | `43` | Position_Unknown | Team_Unknown | 108–269 | 162 | 1 | Undefined position; Undefined team |
| `29` | `44` | Position_Unknown | Team_Unknown | 110–269 | 143 | 6 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 129–130 | 2 | 1 | Undefined position; Undefined team |
| `31` | `48` | Position_Unknown | Team_Unknown | 140–269 | 113 | 4 | Undefined position; Undefined team |
| `32` | `51` | Position_Unknown | Team_Unknown | 165–174 | 9 | 2 | Undefined position; Undefined team |
| `33` | `54` | Position_Unknown | Team_Unknown | 174–184 | 11 | 1 | Undefined position; Undefined team |
| `34` | `55` | Position_Unknown | Team_Unknown | 184–269 | 84 | 2 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 192–199 | 8 | 1 | Undefined position; Undefined team |
| `36` | `57` | Position_Unknown | Team_Unknown | 196–269 | 74 | 1 | Undefined position; Undefined team |
| `37` | `58` | Position_Unknown | Team_Unknown | 201–269 | 66 | 2 | Undefined position; Undefined team |
| `38` | `59` | Position_Unknown | Team_Unknown | 202–260 | 28 | 3 | Undefined position; Undefined team |
| `39` | `61` | Position_Unknown | Team_Unknown | 205–206 | 2 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 252–269 | 3 | 2 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 260–269 | 9 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `20` | `23` | 24 | 24 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `20` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 125 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 182: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [45-86] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-165] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-49] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-146] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-124] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-254] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-147] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-193] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-91] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-115] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-147] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-175] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-183] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-191] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-113] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-174] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-227] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-260] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-264] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-37] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-54] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-161] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-166] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-60] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-72] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-187] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-48] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-269] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-168] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-117] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-28] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-114] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-49] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-20] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-32] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-39] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-153] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-224] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-31] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-49] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-227] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-52] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-17] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-43] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [44-52] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [54-59] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-74] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-37] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-60] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-95] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-188] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-203] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-218] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-61] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-84] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-107] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-54] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-59] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-64] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-74] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-78] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-135] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-146] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-163] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-263] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-128] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-144] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-170] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-243] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-199] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-244] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-211] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-251] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-260] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-206] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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

</details>