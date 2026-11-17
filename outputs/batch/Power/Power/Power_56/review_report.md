# Play-Annotation-Generator Annotation Review — Power_56

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_56`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 23
- **Ball Tracks:** 0
- **Action Segments:** 44
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 9
- **Exact Matches:** 3
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 28
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `12` | `12` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 25 | START | 25 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 25 | START | 25 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `2` | `Group` | 25 | START | 25 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `3` | `Group` | 25 | START | 25 | 182 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 25 | START | 25 | 162 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 25 | START | 25 | 269 |
| ✅ EXACT | `Action_DownBlock` | LG | `10` | `10` | 106 | START | 106 | 142 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `12` | `12` | 106 | START | 106 | 142 |
| ✅ EXACT | `Action_PullBlock` | RG | `2` | `2` | 106 | START | 106 | 117 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 25–242
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 242 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 25–269
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 162 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 218 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 264 | 43 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 25–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 182 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 212 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 224 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 269 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 25–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 105 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 106 | 142 | 37 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 25–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 269 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 25–117
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 105 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 106 | 117 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 25–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 241 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 25–269
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 172 | 148 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 269 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 25–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 205 | 181 | inferred_complete_timeline |
| `Action_PreSnap` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 25–269
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 269 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 25–269
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 25 | 114 | 90 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 129 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 171 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 178 | 182 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 269 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 25–254 | 230 | 1 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 25–189 | 165 | 3 | Undefined position; Undefined team |
| `13` | `16` | Position_Unknown | Team_Unknown | 119–269 | 151 | 1 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 132–269 | 138 | 1 | Undefined position; Undefined team |
| `15` | `19` | Position_Unknown | Team_Unknown | 133–269 | 137 | 1 | Undefined position; Undefined team |
| `16` | `22` | Position_Unknown | Team_Unknown | 170–269 | 100 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 175–181 | 7 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `20` | `27` | Position_Unknown | Team_Unknown | 210–269 | 60 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 214–233 | 14 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 231–233 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 114: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ Row 114: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [25-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [106-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-182] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-212] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-224] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-114] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-171] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-182] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-241] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-162] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-264] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-269] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-269] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-223] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-233] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>