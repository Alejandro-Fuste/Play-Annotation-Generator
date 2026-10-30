# Play-Annotation-Generator Annotation Review — FieldGoalBlock_43

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_43`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 122
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | offense | `19` | `19` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher4 | defense | `14` | `14` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 53 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_End | `11` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `16` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `17` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `18` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `19` | `Group` | 0 | START | 0 | 8 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `7` | `Group` | 0 | START | 0 | 30 |
| ⚠️ AMBIGUOUS MATCH | `Action_LongSnap` | Long_Snapper | `19` | `19` | 17 | START | 17 | 24 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `7` | `7` | 31 | START | 31 | 45 |
| ⚠️ START CHANGED | `Action_KickBall` | Kicker | `1` | `1` | 54 | START | 59 | 59 |
| ✅ EXACT | `Action_BlockKick` | Interior_Rusher4 | `14` | `14` | 58 | START | 58 | 73 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PlaceBall` | 31 | 45 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_KickBall` | 59 | 59 | 1 | inferred_complete_timeline |
| `Action_None` | 60 | 210 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>Left_End — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 54 | 38 | inferred_complete_timeline |
| `Action_None` | 56 | 140 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 194 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 16 | 7 | inferred_complete_timeline |
| `Action_LongSnap` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_LongSnap` | 27 | 30 | 4 | inferred_complete_timeline |
| `Action_None` | 31 | 48 | 18 | inferred_complete_timeline |
| `Action_None` | 50 | 79 | 30 | inferred_complete_timeline |
| `Action_None` | 82 | 84 | 3 | inferred_complete_timeline |
| `Action_None` | 86 | 98 | 13 | inferred_complete_timeline |
| `Action_None` | 110 | 114 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 183 | 5 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 196 | 180 | inferred_complete_timeline |
| `Action_None` | 201 | 207 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 24 | 8 | inferred_complete_timeline |
| `Action_None` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 65 | 9 | inferred_complete_timeline |
| `Action_None` | 76 | 78 | 3 | inferred_complete_timeline |
| `Action_None` | 82 | 167 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 110 | 94 | inferred_complete_timeline |
| `Action_None` | 115 | 147 | 33 | inferred_complete_timeline |
| `Action_None` | 150 | 173 | 24 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–184
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 74 | 58 | inferred_complete_timeline |
| `Action_None` | 79 | 172 | 94 | inferred_complete_timeline |
| `Action_None` | 182 | 184 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 95 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>FG_Block_Support3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–187
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 59 | 43 | inferred_complete_timeline |
| `Action_None` | 78 | 102 | 25 | inferred_complete_timeline |
| `Action_None` | 105 | 171 | 67 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 56 | 40 | inferred_complete_timeline |
| `Action_None` | 59 | 92 | 34 | inferred_complete_timeline |
| `Action_None` | 98 | 178 | 81 | inferred_complete_timeline |
| `Action_None` | 186 | 210 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–134
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 41 | 25 | inferred_complete_timeline |
| `Action_None` | 52 | 67 | 16 | inferred_complete_timeline |
| `Action_None` | 69 | 86 | 18 | inferred_complete_timeline |
| `Action_None` | 88 | 99 | 12 | inferred_complete_timeline |
| `Action_None` | 101 | 111 | 11 | inferred_complete_timeline |
| `Action_None` | 118 | 134 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 29 | 13 | inferred_complete_timeline |
| `Action_None` | 41 | 43 | 3 | inferred_complete_timeline |
| `Action_None` | 54 | 61 | 8 | inferred_complete_timeline |
| `Action_None` | 63 | 78 | 16 | inferred_complete_timeline |
| `Action_None` | 80 | 91 | 12 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 162 | 65 | inferred_complete_timeline |
| `Action_None` | 166 | 174 | 9 | inferred_complete_timeline |
| `Action_None` | 178 | 191 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–204
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_BlockKick` | 58 | 73 | 16 | inferred_complete_timeline |
| `Action_None` | 74 | 89 | 16 | inferred_complete_timeline |
| `Action_None` | 92 | 100 | 9 | inferred_complete_timeline |
| `Action_None` | 102 | 114 | 13 | inferred_complete_timeline |
| `Action_None` | 116 | 176 | 61 | inferred_complete_timeline |
| `Action_None` | 180 | 183 | 4 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 202 | 204 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–38
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 38 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 31 | 15 | inferred_complete_timeline |
| `Action_None` | 34 | 35 | 2 | inferred_complete_timeline |
| `Action_None` | 38 | 169 | 132 | inferred_complete_timeline |
| `Action_None` | 177 | 195 | 19 | inferred_complete_timeline |
| `Action_None` | 197 | 201 | 5 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 163 | 147 | inferred_complete_timeline |
| `Action_None` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_None` | 205 | 210 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_None` | 17 | 95 | 79 | inferred_complete_timeline |
| `Action_None` | 100 | 116 | 17 | inferred_complete_timeline |
| `Action_None` | 118 | 123 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–210 | 211 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 22–44 | 23 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 49–52 | 4 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 63–173 | 111 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–88 | 9 | 4 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 106–146 | 31 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 106–142 | 37 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 108–116 | 9 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 111–120 | 8 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 111–210 | 71 | 6 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 131–191 | 35 | 6 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 132–210 | 79 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_LongSnap` and target `19` (2 segments found)
- ⚠️ `Action_KickBall` for actor_track_id `1` (Kicker): Annotated start 54 != Inferred start 59

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `FG_Block_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `FG_Block_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `FG_Block_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_End` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_End` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 101 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 88: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [17-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-53] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-59] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-171] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-95] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-74] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-172] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-184] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-163] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-116] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-41] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-67] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-86] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-99] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-134] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-29] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-61] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-78] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-91] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-162] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-54] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-140] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-38] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-92] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-178] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-89] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-100] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-176] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-31] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-35] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-169] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-201] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-24] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-55] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-78] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-167] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-196] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [17-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-147] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-173] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [17-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LongSnap' range [27-30] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-48] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-79] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-98] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-114] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-44] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-52] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-71] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-88] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-134] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-142] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-116] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-116] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-184] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
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

</details>