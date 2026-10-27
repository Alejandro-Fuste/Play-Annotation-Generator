# Play-Annotation-Generator Annotation Review — Counter_126

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_126`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 1
- **Action Segments:** 72
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `5` | `4` |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | RB | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `10` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 139 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 140 | START | 140 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 143 | START | 151 | 160 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `5` | `4` | 143 | START | 143 | 213 |
| ❌ MISSING SEGMENT | `Action_PlaySideFakeStep` | RB | `6` | `5` | 143 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `11` | 143 | START | 143 | 230 |
| ✅ EXACT | `Action_PullLeadBlock` | RB | `6` | `5` | 143 | START | 143 | 230 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `10` | 150 | END | 140 | 150 |
| ✅ EXACT | `Action_BallCarry` | QB | `11` | `10` | 181 | START | 181 | 289 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 230 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–289
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_SnapReceive` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_None` | 151 | 180 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 181 | 289 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 143 | 230 | 88 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_DownBlock` | 143 | 213 | 71 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 230 | 16 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_BallSnap` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 186 | 187 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 142 | 143 | inferred_complete_timeline |
| `Action_PullBlock` | 143 | 230 | 88 | inferred_complete_timeline |
| `Action_None` | 231 | 299 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 299 | 160 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 226 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–235
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 199 | 60 | inferred_complete_timeline |
| `Action_None` | 224 | 235 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 150 | 11 | inferred_complete_timeline |
| `Action_None` | 156 | 206 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–158
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 152 | 13 | inferred_complete_timeline |
| `Action_None` | 156 | 158 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 226 | 87 | inferred_complete_timeline |
| `Action_None` | 234 | 299 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 251 | 112 | inferred_complete_timeline |
| `Action_None` | 255 | 256 | 2 | inferred_complete_timeline |
| `Action_None` | 258 | 259 | 2 | inferred_complete_timeline |
| `Action_None` | 261 | 296 | 36 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 258 | 119 | inferred_complete_timeline |
| `Action_None` | 261 | 299 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_None` | 140 | 229 | 90 | inferred_complete_timeline |
| `Action_None` | 233 | 299 | 67 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `19` | Position_Unknown | Team_Unknown | 164–299 | 133 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 165–214 | 45 | 4 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 211–299 | 72 | 4 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 215–233 | 19 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 231–299 | 65 | 3 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 238–299 | 62 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 255–299 | 45 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 256–299 | 44 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 258–299 | 42 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 262–299 | 34 | 2 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 295–299 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 153 | 153 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_PlaySideFakeStep` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 33 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 143 for track '5': 'Action_PlaySideFakeStep' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [140–150], lower_priority='Action_DownBlock' annotated_start=143, effective_Action_DownBlock_start=151.
- ⚠️ Action 'Action_None' range [140-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-226] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-152] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-158] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [143-213] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-199] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-229] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-251] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-296] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [181-289] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [151-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [186-187] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-226] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-206] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-198] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-199] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-225] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-233] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-289] for track '27' has 1 frames without a visible bounding box.
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