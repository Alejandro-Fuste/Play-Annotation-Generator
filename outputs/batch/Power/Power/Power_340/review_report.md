# Play-Annotation-Generator Annotation Review — Power_340

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_340`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `5` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 19 | START | 19 | 117 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 19 | START | 22 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 19 | START | 19 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 19 | START | 19 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 19 | START | 19 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 19 | START | 19 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 19 | START | 19 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `4` | `4` | 103 | START | 103 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `9` | `9` | 103 | START | 103 | 132 |
| ✅ EXACT | `Action_PullBlock` | RG | `5` | `5` | 103 | START | 103 | 170 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 180 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 211 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 213 | 269 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 22–150
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 150 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 19–135
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 135 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–239
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 102 | 84 | inferred_complete_timeline |
| `Action_DownBlock` | 103 | 122 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 170 | 22 | inferred_complete_timeline |
| `Action_None` | 171 | 239 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 19–149
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 117 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 131 | 149 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 102 | 84 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 170 | 68 | inferred_complete_timeline |
| `Action_None` | 171 | 269 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 150 | 132 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 213 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 269 | 55 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 23–259
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 23 | 41 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 259 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 22–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 22 | 26 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 75 | 46 | inferred_complete_timeline |
| `Action_PreSnap` | 83 | 269 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 197 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 202 | 269 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 134 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 141 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 152 | 183 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 257 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 269 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 158 | 140 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 174 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 269 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 171 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 174 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 269 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 19–269 | 244 | 6 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 121–269 | 146 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 133–269 | 128 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 146–269 | 124 | 1 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 151–215 | 65 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 173–176 | 4 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 187–265 | 79 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 199–269 | 71 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 202–220 | 19 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 203–269 | 60 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 207–242 | 31 | 3 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 219–263 | 45 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 222–269 | 48 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 246–269 | 23 | 2 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 246–259 | 14 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 249–269 | 19 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 680: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [19-158] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-174] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-174] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-135] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-211] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-239] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-134] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-141] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-183] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-257] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-269] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [103-132] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [135-152] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [155-170] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-222] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-117] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-26] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [30-75] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-41] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-259] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-221] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-152] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-252] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-176] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-265] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-231] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-242] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-263] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-252] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-259] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [249-255] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>