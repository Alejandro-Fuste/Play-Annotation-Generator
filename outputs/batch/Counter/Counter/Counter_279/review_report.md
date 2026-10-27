# Play-Annotation-Generator Annotation Review — Counter_279

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_279`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 94
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 69
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `15` | `14` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `19` | `18` |
| ⚠️ START CHANGED | `Action_PullBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_PullLeadBlock` | LT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BallCarry` | CB3 | defense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `1` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 99 | START | 99 | 114 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `15` | `14` | 102 | START | 102 | 125 |
| ✅ EXACT | `Action_DownBlock` | LG | `17` | `16` | 102 | START | 102 | 149 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `19` | `18` | 102 | START | 102 | 132 |
| ⚠️ START CHANGED | `Action_PullBlock` | C | `12` | `11` | 102 | START | 115 | 149 |
| ✅ EXACT | `Action_PullLeadBlock` | LT | `8` | `7` | 102 | START | 102 | 149 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 114 | END | 99 | 114 |
| ✅ EXACT | `Action_Handoff` | QB | `5` | `4` | 133 | START | 133 | 148 |
| ✅ EXACT | `Action_BallCarry` | CB3 | `4` | `3` | 149 | START | 149 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 149 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_None` | 115 | 132 | 18 | inferred_complete_timeline |
| `Action_Handoff` | 133 | 148 | 16 | inferred_complete_timeline |
| `Action_None` | 149 | 219 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 224 | 126 | inferred_complete_timeline |
| `Action_None` | 227 | 299 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 102 | 149 | 48 | inferred_complete_timeline |
| `Action_None` | 150 | 299 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 149 | 48 | inferred_complete_timeline |
| `Action_None` | 150 | 156 | 7 | inferred_complete_timeline |
| `Action_None` | 159 | 183 | 25 | inferred_complete_timeline |
| `Action_None` | 187 | 299 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_PullBlock` | 115 | 149 | 35 | inferred_complete_timeline |
| `Action_None` | 150 | 154 | 5 | inferred_complete_timeline |
| `Action_None` | 157 | 162 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 132 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 137 | 138 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 101 | 102 | inferred_complete_timeline |
| `Action_DownBlock` | 102 | 125 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 135 | 149 | 15 | inferred_complete_timeline |
| `Action_None` | 150 | 181 | 32 | inferred_complete_timeline |
| `Action_None` | 187 | 213 | 27 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 154 | 56 | inferred_complete_timeline |
| `Action_None` | 157 | 160 | 4 | inferred_complete_timeline |
| `Action_None` | 169 | 180 | 12 | inferred_complete_timeline |
| `Action_None` | 186 | 209 | 24 | inferred_complete_timeline |
| `Action_None` | 211 | 276 | 66 | inferred_complete_timeline |
| `Action_None` | 279 | 288 | 10 | inferred_complete_timeline |
| `Action_None` | 295 | 299 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 164 | 66 | inferred_complete_timeline |
| `Action_None` | 166 | 168 | 3 | inferred_complete_timeline |
| `Action_None` | 170 | 299 | 130 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 299 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 132 | 34 | inferred_complete_timeline |
| `Action_None` | 137 | 140 | 4 | inferred_complete_timeline |
| `Action_None` | 145 | 228 | 84 | inferred_complete_timeline |
| `Action_None` | 237 | 274 | 38 | inferred_complete_timeline |
| `Action_None` | 280 | 299 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_BallCarry` | 149 | 299 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 98 | 99 | inferred_complete_timeline |
| `Action_None` | 99 | 232 | 134 | inferred_complete_timeline |
| `Action_None` | 245 | 252 | 8 | inferred_complete_timeline |
| `Action_None` | 257 | 270 | 14 | inferred_complete_timeline |
| `Action_None` | 276 | 277 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–299 | 291 | 3 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–286 | 286 | 3 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 13–285 | 258 | 6 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 152–299 | 148 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 176–299 | 124 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 220–299 | 78 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 222–299 | 72 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 263–267 | 5 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 264–267 | 4 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 271–295 | 17 | 3 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 287–299 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `19` (2 segments found)
- ⚠️ `Action_PullBlock` for actor_track_id `12` (C): Annotated start 102 != Inferred start 115

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 560: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ Row 560: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [99–114], lower_priority='Action_PullBlock' annotated_start=102, effective_Action_PullBlock_start=115.
- ⚠️ Action 'Action_None' range [99-224] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-299] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-239] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-219] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-132] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-228] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-274] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-154] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-164] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-283] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-125] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-213] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-156] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-232] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-252] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-270] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [102-132] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [137-138] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-154] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-180] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-209] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-288] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-26] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-46] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-52] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-98] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-285] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-295] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-256] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-267] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-277] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-295] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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

</details>