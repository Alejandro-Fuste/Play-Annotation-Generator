# Play-Annotation-Generator Annotation Review — Counter_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_58`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 76
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
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 150 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 152 |
| ✅ EXACT | `Action_BallSnap` | LB2 | `11` | `10` | 151 | START | 151 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB2 | `11` | `10` | 153 | START | 153 | 167 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `6` | `5` | 153 | START | 153 | 227 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 153 | START | 153 | 172 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `9` | 153 | START | 153 | 181 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `9` | `8` | 153 | START | 153 | 232 |
| ✅ EXACT | `Action_SnapReceive` | RB | `3` | `2` | 170 | END | 151 | 170 |
| ✅ EXACT | `Action_BallCarry` | RB | `3` | `2` | 192 | START | 192 | 221 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 232 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 231 | 81 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_SnapReceive` | 151 | 170 | 20 | inferred_complete_timeline |
| `Action_None` | 171 | 183 | 13 | inferred_complete_timeline |
| `Action_None` | 187 | 191 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 221 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 153 | 232 | 80 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–238
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 227 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 232 | 3 | inferred_complete_timeline |
| `Action_None` | 233 | 238 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 172 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 183 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 191 | 209 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 220 | 225 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PullBlock` | 153 | 181 | 29 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 189 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 198 | 204 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 217 | 232 | 16 | inferred_complete_timeline |
| `Action_None` | 233 | 247 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–252
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 252 | 102 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 219 | 69 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 229 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 242 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–201
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_BallSnap` | 151 | 152 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 153 | 167 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 169 | 178 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 181 | 189 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 191 | 201 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 185 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–241
- **Visible Samples:** 242

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 150 | 151 | inferred_complete_timeline |
| `Action_None` | 151 | 241 | 91 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–279 | 280 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 170–175 | 6 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 190–250 | 43 | 6 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 212–299 | 72 | 3 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 220–299 | 69 | 5 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 248–299 | 52 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 249–299 | 51 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 253–299 | 44 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 265–267 | 3 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 273–277 | 5 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 282–299 | 18 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 284–299 | 16 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 46 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 118: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_None' range [151-279] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-231] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-227] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-229] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-172] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-183] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [191-209] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [220-225] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [153-232] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [153-181] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [187-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [194-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [198-204] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [217-232] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-247] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [153-167] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [169-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [181-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [191-201] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-252] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-185] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-299] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-241] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-222] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-232] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-250] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-261] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-272] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-288] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-290] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-267] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>