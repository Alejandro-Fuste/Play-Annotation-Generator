# Play-Annotation-Generator Annotation Review — PuntBlock_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PuntBlock_60`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_PuntBlock`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 40
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | offense | `9` | `Group` |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_PuntBall` | Punter | offense | `0` | `0` |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | defense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Punter | `0` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Tackle | `1` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Wing | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Guard | `11` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Long_Snapper | `2` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector2 | `3` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector1 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Wing | `5` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Guard | `6` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Personal_Protector3 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Tackle | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_LongSnap` | Long_Snapper | `2` | `2` | 2 | START | 2 | 59 |
| ✅ EXACT | `Action_SnapReceive` | Punter | `0` | `0` | 30 | END | 30 | 30 |
| ✅ EXACT | `Action_PuntBall` | Punter | `0` | `0` | 60 | START | 60 | 150 |
| ✅ EXACT | `Action_BlockPunt` | Interior_Rusher5 | `16` | `16` | 71 | START | 71 | 76 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Left_Guard — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Tackle — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 142 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Wing — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Long_Snapper — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_LongSnap` | 2 | 59 | 58 | inferred_complete_timeline |
| `Action_None` | 60 | 125 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Personal_Protector3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 119 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>Punter — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 30 | 1 | inferred_complete_timeline |
| `Action_None` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_PuntBall` | 60 | 150 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Guard — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Tackle — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Wing — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Interior_Rusher1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 132 | 131 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher4 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–60
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 60 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher5 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 70 | 71 | inferred_complete_timeline |
| `Action_BlockPunt` | 71 | 76 | 6 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher6 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher7 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Interior_Rusher8 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Edge_Rusher1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 150 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 0–138 | 139 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 62–64 | 3 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 73–140 | 68 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 110–111 | 2 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 120–127 | 8 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 121–150 | 30 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 128–150 | 16 | 4 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Punter` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Right_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Long_Snapper` position mapped to `offense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Personal_Protector2` position mapped to `offense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Personal_Protector1` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Right_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Right_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Personal_Protector3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Interior_Rusher3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Left_Tackle` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Left_Wing` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Left_Guard` position mapped to `offense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Interior_Rusher8` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Interior_Rusher7` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Right_Edge_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Interior_Rusher6` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Interior_Rusher5` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Interior_Rusher1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Interior_Rusher2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Interior_Rusher4` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 122: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PuntBall' range [60-150] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-142] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-150] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-132] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-60] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-64] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-140] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-130] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-142] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
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