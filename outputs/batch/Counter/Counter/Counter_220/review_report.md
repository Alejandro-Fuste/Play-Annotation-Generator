# Play-Annotation-Generator Annotation Review — Counter_220

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_220`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 57
- **Validation Warnings:** 60
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 38
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | defense | `11` | `10` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `5` | `4` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 149 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 147 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 148 | START | 148 | 161 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | `11` | `10` | 150 | START | 150 | 183 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `12` | `11` | 150 | START | 162 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `3` | `2` | 150 | START | 150 | 176 |
| ✅ EXACT | `Action_PullBlock` | LG | `5` | `4` | 150 | START | 150 | 200 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `2` | `1` | 150 | START | 150 | 189 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 161 | END | 148 | 161 |
| ✅ EXACT | `Action_BallCarry` | QB | `9` | `8` | 191 | START | 191 | 303 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–303
- **Visible Samples:** 304

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_SnapReceive` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_None` | 162 | 190 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 191 | 303 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 150 | 189 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 200 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BallSnap` | 148 | 161 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 233 | 72 | inferred_complete_timeline |
| `Action_None` | 234 | 258 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 176 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 185 | 233 | 49 | inferred_complete_timeline |
| `Action_None` | 234 | 329 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 329 | 182 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 222 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 171 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–256
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 174 | 27 | inferred_complete_timeline |
| `Action_None` | 176 | 183 | 8 | inferred_complete_timeline |
| `Action_None` | 194 | 256 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 171 | 24 | inferred_complete_timeline |
| `Action_None` | 174 | 329 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 149 | 150 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 183 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 188 | 233 | 46 | inferred_complete_timeline |
| `Action_None` | 234 | 321 | 88 | inferred_complete_timeline |
| `Action_None` | 323 | 326 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–223
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_None` | 148 | 223 | 76 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `13` | Position_Unknown | Team_Unknown | 78–329 | 245 | 4 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 156–329 | 173 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 163–263 | 95 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 169–329 | 161 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 190–229 | 38 | 2 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 230–254 | 25 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 234–284 | 51 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 235–277 | 43 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 237–317 | 81 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 258–329 | 62 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 271–277 | 7 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 275–329 | 55 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 312–327 | 16 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `12` (C): Annotated start 150 != Inferred start 162
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 13 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 13 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 26 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [148–161], lower_priority='Action_DownBlock' annotated_start=150, effective_Action_DownBlock_start=162.
- ⚠️ Action 'Action_None' range [148-223] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [150-189] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-176] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [185-233] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-222] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [150-200] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-171] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [191-303] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-183] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-256] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [150-183] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-321] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-326] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-258] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-312] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-321] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-254] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-284] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-277] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-317] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-296] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-327] for track '24' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>