# Play-Annotation-Generator Annotation Review — Duo_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_112`
- **Frame Range:** 0 to 268 (269 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 268
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 98
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `16` | `16` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | Team_Unknown | `20` | `20` |
| ✅ EXACT | `Action_ComboBlock` | SAF1 | defense | `8` | `8` |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | Team_Unknown | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 122 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `14` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `16` | `16` | 140 | START | 140 | 200 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `17` | `17` | 140 | START | 140 | 159 |
| ✅ EXACT | `Action_ComboBlock` | Position_Unknown | `20` | `20` | 140 | START | 140 | 200 |
| ✅ EXACT | `Action_ComboBlock` | SAF1 | `8` | `8` | 140 | START | 140 | 200 |
| ❌ MISSING SEGMENT | `Action_BlockSecondLevel` | Position_Unknown | `21` | `21` | 156 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 200 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–243
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 45 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 88 | 94 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 111 | 112 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 243 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 172 | 173 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 190 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 201 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_PreSnap` | 147 | 156 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 167 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–244
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 122 | 123 | inferred_complete_timeline |
| `Action_PreSnap` | 160 | 195 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 240 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 245 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 247 | 251 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 268 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 268 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–25
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–267
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 243 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 267 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–169
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 157 | 158 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_ComboBlock` | 140 | 200 | 61 | inferred_complete_timeline |
| `Action_None` | 201 | 268 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–268
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 167 | 168 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 268 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–231 | 215 | 8 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 10–159 | 148 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 34–268 | 224 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 46–76 | 31 | 1 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 69–268 | 200 | 3 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 105–127 | 21 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 115–268 | 133 | 8 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 142–258 | 34 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 151–232 | 82 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 169–268 | 87 | 6 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 197–268 | 58 | 5 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 261–268 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BlockSecondLevel` on target `21` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 226: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
- ⚠️ Segment 'Action_BlockSecondLevel' for track '21' has invalid range: start=156, end=127. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-244] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-243] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-267] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [247-251] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-156] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-122] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-195] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-268] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-173] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-190] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-268] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-94] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-243] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-18] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [140-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-215] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-221] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-231] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-89] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-139] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [140-159] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-53] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-251] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-259] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-76] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-268] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-123] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [126-127] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [133-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-258] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-232] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-221] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-236] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-258] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-268] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-221] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-237] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-241] for track '26' has 1 frames without a visible bounding box.
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

</details>