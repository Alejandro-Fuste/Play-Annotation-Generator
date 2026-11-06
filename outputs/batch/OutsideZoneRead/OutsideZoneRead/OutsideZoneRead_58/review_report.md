# Play-Annotation-Generator Annotation Review — OutsideZoneRead_58

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_58`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 91
- **Validation Warnings:** 103
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 73
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `10` | `10` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 133 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 145 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `10` | `10` | 134 | START | 134 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `12` | `12` | 134 | START | 134 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 134 | START | 134 | 174 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `5` | `5` | 134 | START | 134 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_PressEdge` | RB | `8` | `8` | 135 | START | 135 | 157 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `9` | `9` | 146 | START | 146 | 154 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 155 | START | 155 | 165 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–319
- **Visible Samples:** 318

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 145 | 146 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 146 | 154 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 155 | 165 | 11 | inferred_complete_timeline |
| `Action_None` | 166 | 197 | 32 | inferred_complete_timeline |
| `Action_None` | 200 | 319 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PressEdge` | 135 | 157 | 23 | inferred_complete_timeline |
| `Action_PressEdge` | 161 | 191 | 31 | inferred_complete_timeline |
| `Action_None` | 192 | 305 | 114 | inferred_complete_timeline |
| `Action_None` | 307 | 329 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_PreSnap` | 221 | 329 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 174 | 41 | inferred_complete_timeline |
| `Action_None` | 175 | 182 | 8 | inferred_complete_timeline |
| `Action_None` | 185 | 200 | 16 | inferred_complete_timeline |
| `Action_None` | 208 | 329 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 12 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 18 | 45 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 133 | 68 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 174 | 41 | inferred_complete_timeline |
| `Action_None` | 175 | 329 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–279
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 174 | 41 | inferred_complete_timeline |
| `Action_None` | 175 | 185 | 11 | inferred_complete_timeline |
| `Action_None` | 191 | 239 | 49 | inferred_complete_timeline |
| `Action_None` | 269 | 276 | 8 | inferred_complete_timeline |
| `Action_None` | 278 | 279 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 133 | 134 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 174 | 41 | inferred_complete_timeline |
| `Action_None` | 175 | 189 | 15 | inferred_complete_timeline |
| `Action_None` | 201 | 329 | 129 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 190 | 191 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 255 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 315 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 323 | 324 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–189
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 189 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 210 | 214 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 240 | 268 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 329 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 165 | 180 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 251 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–274
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 219 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 226 | 274 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 240 | 241 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 329 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 2–329 | 307 | 4 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 4–50 | 27 | 4 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 160–329 | 122 | 4 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 177–188 | 12 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 185–327 | 88 | 8 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 219–329 | 100 | 4 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 228–329 | 94 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 232–329 | 98 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 240–329 | 90 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 252–255 | 4 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 262–323 | 62 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 263–329 | 51 | 4 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 267–329 | 63 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 291–310 | 20 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 306–329 | 24 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 313–315 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PressEdge` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 67 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 118: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-274] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-214] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-268] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-329] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-185] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-279] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-182] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-200] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-255] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-315] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-217] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PressEdge' range [135-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-305] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-197] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-319] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-12] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-45] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-17] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [26-75] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-329] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-5] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-11] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-33] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-50] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-196] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-204] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-188] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-233] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-304] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [306-313] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [315-327] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-283] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [286-288] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-298] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-296] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [240-329] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [262-323] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-271] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [279-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [323-324] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [291-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '29' has 1 frames without a visible bounding box.
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