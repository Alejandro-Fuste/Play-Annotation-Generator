# Play-Annotation-Generator Annotation Review — Duo_42

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `Duo_42`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 268
- **Player Tracks:** 20
- **Ball Tracks:** 2
- **Action Segments:** 51
- **Validation Warnings:** 63
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 23
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | offense | `13` | `13` |
| ✅ EXACT | `Action_ComboBlock` | QB | offense | `13` | `13` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `18` | N/A |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `4` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 190 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 159 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `16` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 174 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 268 |
| ✅ EXACT | `Action_BlockSecondLevel` | QB | `13` | `13` | 160 | START | 160 | 174 |
| ✅ EXACT | `Action_ComboBlock` | QB | `13` | `13` | 175 | START | 175 | 193 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | Position_Unknown | `18` | N/A | 175 | START | N/A | N/A |
| ✅ EXACT | `Action_ComboBlock` | RG | `4` | `4` | 175 | START | 175 | 193 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 193 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 160 | 174 | 15 | inferred_complete_timeline |
| `Action_ComboBlock` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 194 | 259 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 8 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 62 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 123 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 149 | 166 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 268 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 261

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 237 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 244 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 248 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 268 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 63 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 92 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 256 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 268 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_ComboBlock` | 175 | 193 | 19 | inferred_complete_timeline |
| `Action_None` | 194 | 206 | 13 | inferred_complete_timeline |
| `Action_None` | 210 | 220 | 11 | inferred_complete_timeline |
| `Action_None` | 248 | 268 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 43 | 99 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 268 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–268 | 269 | 1 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–268 | 269 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–268 | 269 | 1 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–268 | 243 | 3 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–253 | 254 | 1 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–240 | 241 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–218 | 218 | 2 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–260 | 224 | 3 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 157–183 | 13 | 3 | Undefined position; Undefined team |
| `20` | `31` | Position_Unknown | Team_Unknown | 224–268 | 44 | 2 | Undefined position; Undefined team |
| `21` | `36` | Position_Unknown | Team_Unknown | 255–260 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `17` | `17` | 13 | 41 | 29 | 100.0% | None |
| `18` | `20` | 113 | 171 | 44 | 74.6% | 148, 155–168 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `18` (Position_Unknown)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_ComboBlock' at frame 175 targets track ID '24', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 40 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [175-193] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-220] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-268] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-260] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [264-268] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-218] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-99] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-195] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-237] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-244] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-248] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-259] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-203] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-260] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-63] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-92] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-256] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-8] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [149-166] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-164] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-183] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-246] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-260] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.

</details>