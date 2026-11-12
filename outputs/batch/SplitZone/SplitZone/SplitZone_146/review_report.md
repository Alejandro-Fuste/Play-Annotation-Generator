# Play-Annotation-Generator Annotation Review — SplitZone_146

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_146`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 359
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 74
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 55
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | offense | `0` | `0` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `6` | `6` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `0` | `Group` | 19 | START | 20 | 142 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 19 | START | 20 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 19 | START | 20 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 19 | START | 20 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 19 | START | 20 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 19 | START | 20 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 19 | START | 20 | 141 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 19 | START | 20 | 138 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 139 | START | 139 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `13` | `13` | 142 | START | 142 | 233 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `14` | `14` | 142 | START | 142 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `15` | `15` | 142 | START | 142 | 171 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `17` | `17` | 142 | START | 152 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 142 | START | 142 | 163 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE1 | `0` | `0` | 143 | START | 143 | 159 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `2` | `2` | 148 | START | 148 | 359 |
| ✅ EXACT | `Action_SnapReceive` | QB | `6` | `6` | 151 | END | 139 | 151 |
| ✅ EXACT | `Action_Handoff` | QB | `6` | `6` | 157 | START | 157 | 277 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `3` | `3` | 164 | START | 164 | 233 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 233 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 20–277
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_SnapReceive` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_None` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 157 | 277 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 20–220
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 142 | 123 | inferred_complete_timeline |
| `Action_SplitBlock` | 143 | 159 | 17 | inferred_complete_timeline |
| `Action_SplitBlock` | 214 | 220 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 20–254
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 221 | 83 | inferred_complete_timeline |
| `Action_None` | 233 | 254 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 20–235
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 141 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 233 | 92 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 20–241
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 141 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 163 | 22 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 164 | 233 | 70 | inferred_complete_timeline |
| `Action_None` | 234 | 241 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 20–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_BallSnap` | 139 | 151 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 152 | 233 | 82 | inferred_complete_timeline |
| `Action_None` | 234 | 239 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 20–245
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 141 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 171 | 30 | inferred_complete_timeline |
| `Action_ZoneBlock` | 177 | 182 | 6 | inferred_complete_timeline |
| `Action_ZoneBlock` | 188 | 233 | 46 | inferred_complete_timeline |
| `Action_None` | 234 | 245 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 20–274
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 141 | 122 | inferred_complete_timeline |
| `Action_ZoneBlock` | 142 | 174 | 33 | inferred_complete_timeline |
| `Action_ZoneBlock` | 176 | 182 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 208 | 217 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 223 | 233 | 11 | inferred_complete_timeline |
| `Action_None` | 234 | 274 | 41 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 20–264
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 264 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 20–211
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 206 | 68 | inferred_complete_timeline |
| `Action_None` | 210 | 211 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 20–238
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 238 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 20–274
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 274 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 20–248
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 248 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 20–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 359 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 20–288
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 288 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 20–229
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 229 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 20–355
- **Visible Samples:** 336

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 20 | 138 | 119 | inferred_complete_timeline |
| `Action_None` | 139 | 355 | 217 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `2` | Position_Unknown | Team_Unknown | 20–359 | 340 | 2 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 155–250 | 96 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 217–256 | 40 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 223–277 | 55 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 225–359 | 135 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 226–227 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 245–251 | 7 | 1 | Undefined position; Undefined team |
| `25` | `37` | Position_Unknown | Team_Unknown | 329–359 | 31 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 329–359 | 31 | 1 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 330–359 | 30 | 1 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 333–355 | 21 | 2 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 333–359 | 19 | 3 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 336–342 | 7 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 336–340 | 5 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 336–351 | 16 | 1 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 341–346 | 6 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 350–359 | 10 | 1 | Undefined position; Undefined team |
| `35` | `53` | Position_Unknown | Team_Unknown | 358–359 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (3 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `17` (C): Annotated start 142 != Inferred start 152
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF3` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 6 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 294: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '14' (RT) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '17' (C) duration 92 frames exceeds threshold 90 frames [start=142, end=233].
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [139–151], lower_priority='Action_ZoneBlock' annotated_start=142, effective_Action_ZoneBlock_start=152.
- ⚠️ Action 'Action_SplitBlock' range [143-159] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [214-220] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-229] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-241] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-206] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-211] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [157-277] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-248] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-264] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-355] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-274] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-174] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [176-182] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [208-217] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-274] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [142-171] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [177-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-245] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-221] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-254] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-250] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-256] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-277] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-227] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-251] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-359] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-359] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-351] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-355] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-342] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-351] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-342] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-340] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-351] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-346] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-359] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.

</details>