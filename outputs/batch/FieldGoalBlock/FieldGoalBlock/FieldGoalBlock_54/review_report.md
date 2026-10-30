# Play-Annotation-Generator Annotation Review — FieldGoalBlock_54

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `FieldGoalBlock_54`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_FieldGoalBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 118
- **Validation Warnings:** 127
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
- **Inferred Coverage Segments (Action_None):** 101
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `8` | `Group` |
| ✅ EXACT | `Action_PlaceBall` | Holder | offense | `3` | `3` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Left_Tackle | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `10` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `11` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `12` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `13` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_End | `15` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Holder | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `7` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `8` | `Group` | 0 | START | 0 | 45 |
| ✅ EXACT | `Action_PlaceBall` | Holder | `3` | `3` | 36 | START | 36 | 56 |
| ✅ EXACT | `Action_KickBall` | Kicker | `1` | `1` | 64 | START | 64 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockKick` | Left_Tackle | `8` | `8` | 67 | START | 67 | 71 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Holder — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PlaceBall` | 36 | 56 | 21 | inferred_complete_timeline |
| `Action_None` | 57 | 143 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>Kicker — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_KickBall` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 68 | 163 | 96 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 182 | 204 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Guard — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 63 | 13 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 70 | 72 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 61 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 66 | 4 | inferred_complete_timeline |
| `Action_BlockKick` | 67 | 71 | 5 | inferred_complete_timeline |
| `Action_BlockKick` | 73 | 74 | 2 | inferred_complete_timeline |
| `Action_None` | 89 | 106 | 18 | inferred_complete_timeline |
| `Action_None` | 110 | 112 | 3 | inferred_complete_timeline |
| `Action_None` | 115 | 130 | 16 | inferred_complete_timeline |
| `Action_None` | 133 | 134 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 67 | 4 | inferred_complete_timeline |
| `Action_None` | 83 | 85 | 3 | inferred_complete_timeline |
| `Action_None` | 87 | 95 | 9 | inferred_complete_timeline |
| `Action_None` | 97 | 123 | 27 | inferred_complete_timeline |
| `Action_None` | 129 | 210 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 74 | 11 | inferred_complete_timeline |
| `Action_None` | 92 | 104 | 13 | inferred_complete_timeline |
| `Action_None` | 112 | 139 | 28 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 159 | 4 | inferred_complete_timeline |
| `Action_None` | 170 | 180 | 11 | inferred_complete_timeline |
| `Action_None` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 210 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>Right_End — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 89 | 26 | inferred_complete_timeline |
| `Action_None` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 91 | 28 | inferred_complete_timeline |
| `Action_None` | 95 | 201 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 56 | 18 | inferred_complete_timeline |
| `Action_None` | 74 | 166 | 93 | inferred_complete_timeline |
| `Action_None` | 174 | 191 | 18 | inferred_complete_timeline |
| `Action_None` | 201 | 202 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>FG_Block_Support — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 118 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_None` | 120 | 123 | 4 | inferred_complete_timeline |
| `Action_None` | 126 | 127 | 2 | inferred_complete_timeline |
| `Action_None` | 140 | 143 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 55 | 63 | 9 | inferred_complete_timeline |
| `Action_None` | 64 | 182 | 119 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 210 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–175
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 85 | 22 | inferred_complete_timeline |
| `Action_None` | 110 | 151 | 42 | inferred_complete_timeline |
| `Action_None` | 156 | 167 | 12 | inferred_complete_timeline |
| `Action_None` | 171 | 175 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 98 | 210 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 19–174 | 121 | 7 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 19–79 | 48 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 24–81 | 36 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 24–210 | 145 | 8 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 29–204 | 161 | 4 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 32–184 | 114 | 7 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 98–210 | 111 | 3 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 113–210 | 96 | 2 | Undefined position; Undefined team |
| `24` | `24` | Position_Unknown | Team_Unknown | 121–210 | 74 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 140–210 | 71 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 167–210 | 44 | 1 | Undefined position; Undefined team |
| `27` | `28` | Position_Unknown | Team_Unknown | 182–201 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BlockKick` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `FG_Block_Support` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Holder` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Edge_Rusher` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_End` position mapped to `offense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 102 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [64-118] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-163] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-31] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '7' starts at frame 64, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [64-67] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-61] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [67-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockKick' range [73-74] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-106] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-112] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-85] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-151] for track '9' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-167] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-175] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-67] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-72] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-104] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-191] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-210] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-91] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-191] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-182] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-210] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-28] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-44] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-79] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-88] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-29] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [31-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-63] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 64, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [64-67] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-40] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-81] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-53] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-60] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-184] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-95] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-184] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-132] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-141] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-163] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '27' has 1 frames without a visible bounding box.
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

</details>