# Play-Annotation-Generator Annotation Review — FieldGoalBlock_98

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_98`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 103
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
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `7` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `2` | `2` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockKick` | Kicker | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `0` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `1` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `13` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `14` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `2` | `Group` | 0 | START | 0 | 70 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `3` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `5` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `7` | `Group` | 0 | START | 0 | 95 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `2` | `2` | 71 | START | 71 | 87 |
| ✅ EXACT | `Action_KickBall` | Kicker | `0` | `0` | 96 | START | 96 | 100 |
| ✅ EXACT | `Action_BlockKick` | Kicker | `0` | `0` | 101 | START | 101 | 110 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_PlaceBall` | 71 | 87 | 17 | inferred_complete_timeline |
| `Action_None` | 88 | 188 | 101 | inferred_complete_timeline |
| `Action_None` | 194 | 197 | 4 | inferred_complete_timeline |
| `Action_None` | 207 | 210 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_KickBall` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_BlockKick` | 101 | 110 | 10 | inferred_complete_timeline |
| `Action_None` | 111 | 181 | 71 | inferred_complete_timeline |
| `Action_None` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 140 | 45 | inferred_complete_timeline |
| `Action_None` | 195 | 200 | 6 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 100 | 5 | inferred_complete_timeline |
| `Action_None` | 103 | 131 | 29 | inferred_complete_timeline |
| `Action_None` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 169 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 9 | 73 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 96 | 107 | 12 | inferred_complete_timeline |
| `Action_None` | 109 | 121 | 13 | inferred_complete_timeline |
| `Action_None` | 126 | 205 | 80 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 109 | 14 | inferred_complete_timeline |
| `Action_None` | 112 | 133 | 22 | inferred_complete_timeline |
| `Action_None` | 148 | 168 | 21 | inferred_complete_timeline |
| `Action_None` | 174 | 176 | 3 | inferred_complete_timeline |
| `Action_None` | 187 | 195 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 178 | 83 | inferred_complete_timeline |
| `Action_None` | 189 | 210 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 141 | 46 | inferred_complete_timeline |
| `Action_None` | 148 | 177 | 30 | inferred_complete_timeline |
| `Action_None` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_None` | 190 | 210 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 95 | 7 | inferred_complete_timeline |
| `Action_None` | 96 | 188 | 93 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_None` | 98 | 99 | 2 | inferred_complete_timeline |
| `Action_None` | 103 | 210 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 164 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 210 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_None` | 96 | 191 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–116 | 94 | 4 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 3–201 | 32 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 5–210 | 162 | 8 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 5–139 | 133 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 75–204 | 113 | 5 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 93–103 | 11 | 2 | Undefined position; Undefined team |
| `21` | `30` | Position_Unknown | Team_Unknown | 125–210 | 53 | 4 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 127–130 | 4 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 192–210 | 17 | 3 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 192–210 | 14 | 3 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |
| `26` | `36` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Long_Snapper` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 78 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [111-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-195] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-140] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-188] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-178] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-86] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-188] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-146] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-141] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-177] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-164] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-73] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-99] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-109] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-133] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-168] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-176] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-195] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-91] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-107] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-121] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-205] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-92] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-10] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-10] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-139] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-196] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-6] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-95] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-95] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-160] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-204] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-103] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-194] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-210] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
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

</details>