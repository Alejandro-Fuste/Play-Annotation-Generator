# Play-Annotation-Generator Annotation Review — Power_361

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_361`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 60
- **Validation Warnings:** 61
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
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `18` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `21` | `21` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 19 | START | 19 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 19 | START | 19 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `14` | `Group` | 19 | START | 19 | 269 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 19 | START | 19 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 19 | START | 19 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 19 | START | 19 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 19 | START | 19 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `11` | `11` | 154 | START | 154 | 159 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `18` | 154 | START | 154 | 180 |
| ✅ EXACT | `Action_PullBlock` | LG | `21` | `21` | 154 | START | 154 | 206 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 49 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 52 | 269 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 26 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 269 | 242 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 210 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 269 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 19–269
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 153 | 135 | inferred_complete_timeline |
| `Action_PullBlock` | 154 | 206 | 53 | inferred_complete_timeline |
| `Action_None` | 207 | 259 | 53 | inferred_complete_timeline |
| `Action_None` | 261 | 269 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 19–203
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 153 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 172 | 10 | inferred_complete_timeline |
| `Action_DownBlock` | 202 | 203 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 19–242
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 153 | 135 | inferred_complete_timeline |
| `Action_DownBlock` | 154 | 180 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 206 | 24 | inferred_complete_timeline |
| `Action_None` | 207 | 218 | 12 | inferred_complete_timeline |
| `Action_None` | 221 | 242 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 200 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 217 | 15 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 225 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 228 | 233 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 269 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 215 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 229 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 236 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 249 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 269 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 220 | 202 | inferred_complete_timeline |
| `Action_PreSnap` | 241 | 269 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–268
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 203 | 185 | inferred_complete_timeline |
| `Action_PreSnap` | 208 | 268 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 243 | 225 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 249 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 255 | 257 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 269 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 269 | 251 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 19–269 | 251 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 19–269 | 251 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 19–269 | 251 | 1 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 19–254 | 221 | 5 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 23–33 | 11 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 168–173 | 6 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 189–269 | 76 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 226–228 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 722: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [19-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-249] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-252] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-257] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [265-266] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-159] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-172] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [202-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-26] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-269] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-269] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-200] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-217] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-233] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-220] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-215] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-229] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-249] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [154-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-206] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-218] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-242] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-163] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-222] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-242] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-254] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-269] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-259] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-269] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-33] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-173] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-233] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-240] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-228] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>