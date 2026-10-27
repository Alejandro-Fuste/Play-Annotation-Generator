# Play-Annotation-Generator Annotation Review — Counter_116

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_116`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 25
- **Ball Tracks:** 1
- **Action Segments:** 64
- **Validation Warnings:** 68
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 47
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ✅ EXACT | `Action_DownBlock` | DT1 | defense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 118 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 118 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 119 | START | 119 | 132 |
| ✅ EXACT | `Action_DownBlock` | DT1 | `14` | `13` | 119 | START | 119 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `5` | `4` | 119 | START | 119 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `9` | `8` | 119 | START | 119 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `10` | `9` | 119 | START | 119 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `13` | `12` | 119 | START | 119 | 157 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `5` | 133 | END | 119 | 133 |
| ✅ EXACT | `Action_BallCarry` | QB | `6` | `5` | 165 | START | 165 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 211 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 119 | 133 | 15 | inferred_complete_timeline |
| `Action_None` | 134 | 164 | 31 | inferred_complete_timeline |
| `Action_BallCarry` | 165 | 299 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 119 | 157 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 163 | 202 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 215 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_PullBlock` | 119 | 136 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 138 | 146 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 151 | 156 | 6 | inferred_complete_timeline |
| `Action_PullBlock` | 159 | 211 | 53 | inferred_complete_timeline |
| `Action_None` | 212 | 226 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 119 | 132 | 14 | inferred_complete_timeline |
| `Action_None` | 165 | 169 | 5 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_None` | 200 | 213 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 153 | 35 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 162 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 211 | 48 | inferred_complete_timeline |
| `Action_None` | 212 | 217 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 196 | 78 | inferred_complete_timeline |
| `Action_DownBlock` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_None` | 213 | 227 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 188 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_DownBlock` | 119 | 211 | 93 | inferred_complete_timeline |
| `Action_None` | 212 | 214 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 199 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 299 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 118 | 119 | inferred_complete_timeline |
| `Action_None` | 119 | 237 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 75 | 76 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 118 | 23 | inferred_complete_timeline |
| `Action_None` | 119 | 177 | 59 | inferred_complete_timeline |
| `Action_None` | 183 | 299 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–212 | 212 | 3 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 44–229 | 186 | 2 | Undefined position; Undefined team |
| `16` | `20` | Position_Unknown | Team_Unknown | 179–183 | 5 | 1 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 179–180 | 2 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 182–233 | 52 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 202–230 | 24 | 2 | Undefined position; Undefined team |
| `20` | `29` | Position_Unknown | Team_Unknown | 213–254 | 42 | 1 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 251–299 | 38 | 2 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 253–269 | 8 | 3 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 260–299 | 40 | 1 | Undefined position; Undefined team |
| `24` | `35` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | 48 | 70 | 16 | 69.6% | 49, 51–55, 65 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 38 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 234: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '4' (RG) duration 93 frames exceeds threshold 90 frames [start=119, end=211].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (RT) duration 93 frames exceeds threshold 90 frames [start=119, end=211].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (LG) duration 93 frames exceeds threshold 90 frames [start=119, end=211].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '13' (DT1) duration 93 frames exceeds threshold 90 frames [start=119, end=211].
- ⚠️ Action 'Action_None' range [119-205] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-237] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-75] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-177] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-153] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-162] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [119-132] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-198] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-213] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-215] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [119-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [205-207] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-227] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [119-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [138-146] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [151-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-188] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [119-157] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [163-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-214] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-229] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-233] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-254] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-286] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-262] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>