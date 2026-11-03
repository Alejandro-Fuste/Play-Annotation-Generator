# Play-Annotation-Generator Annotation Review — PuntBlock_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_76`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 91
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 12
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Left_Edge_Rusher1 | defense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Interior_Rusher4 | defense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `0` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `15` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `2` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `4` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `9` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `6` | `6` | 22 | START | 22 | 75 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `4` | `4` | 53 | END | 53 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PuntBall` | Punter | `4` | `4` | 76 | START | 76 | 82 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockPunt` | Left_Edge_Rusher1 | `14` | `14` | 84 | START | 84 | 85 |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Interior_Rusher4 | `5` | `5` | 202 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_LongSnap` | 22 | 75 | 54 | inferred_complete_timeline |
| `Action_None` | 76 | 239 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 70 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 53 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 52 | 5 | inferred_complete_timeline |
| `Action_SnapReceive` | 53 | 53 | 1 | inferred_complete_timeline |
| `Action_None` | 54 | 75 | 22 | inferred_complete_timeline |
| `Action_PuntBall` | 76 | 82 | 7 | inferred_complete_timeline |
| `Action_PuntBall` | 109 | 239 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 47 | 26 | inferred_complete_timeline |
| `Action_None` | 78 | 86 | 9 | inferred_complete_timeline |
| `Action_None` | 93 | 95 | 3 | inferred_complete_timeline |
| `Action_None` | 103 | 237 | 135 | inferred_complete_timeline |
| `Action_None` | 239 | 239 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 239 | 218 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 130 | 109 | inferred_complete_timeline |
| `Action_None` | 132 | 239 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 51 | 30 | inferred_complete_timeline |
| `Action_None` | 54 | 131 | 78 | inferred_complete_timeline |
| `Action_None` | 136 | 213 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 71 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 173 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 109 | 88 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 136 | 19 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 201 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 116 | 95 | inferred_complete_timeline |
| `Action_None` | 118 | 233 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Edge_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 83 | 6 | inferred_complete_timeline |
| `Action_BlockPunt` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_BlockPunt` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 239 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_None` | 22 | 57 | 36 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–142 | 138 | 3 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 32–205 | 166 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–164 | 105 | 2 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 35–79 | 34 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 73–239 | 161 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 79–239 | 161 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 82–94 | 13 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 83–207 | 115 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 96–239 | 140 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 96–109 | 9 | 3 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 97–239 | 143 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 106–239 | 134 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 120–239 | 118 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 122–239 | 118 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 154–239 | 84 | 2 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 202–225 | 24 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 224–239 | 16 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PuntBall` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockPunt` and target `14` (2 segments found)
- ❌ Missing segment for action `Action_SecureRecovery` on target `5` (Interior_Rusher4)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Right_Guard` position mapped to `offense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 154: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureRecovery' for track '5' has invalid range: start=202, end=173. Clamping end to start.
- ⚠️ Action 'Action_None' range [22-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-130] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PuntBall' range [76-82] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-201] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-116] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-233] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-53] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-57] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-51] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-131] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-213] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [84-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockPunt' range [90-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-47] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-86] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-237] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-36] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-205] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-42] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-164] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-45] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-79] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-88] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-94] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-147] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-178] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-207] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-121] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-100] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-217] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-239] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-161] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-225] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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