# Play-Annotation-Generator Annotation Review — Power_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_134`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `6` | `6` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `0` | `Group` | 19 | START | 19 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 19 | START | 19 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 19 | START | 19 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 19 | START | 19 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 19 | START | 19 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `9` | `Group` | 19 | START | 19 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `17` | `17` | 182 | START | 182 | 235 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `5` | `5` | 182 | START | 182 | 187 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `6` | `6` | 182 | START | 182 | 202 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `1` | `1` | 182 | START | 182 | 202 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 19–255
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 210 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 255 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 19–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 214 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 221 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 389 | 167 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 19–223
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 210 | 192 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 218 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 220 | 223 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 19–389
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 181 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 235 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_None` | 241 | 389 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 19–332
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 247 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 268 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 332 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 19–299
- **Visible Samples:** 272

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 181 | 163 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 240 | 48 | inferred_complete_timeline |
| `Action_None` | 241 | 270 | 30 | inferred_complete_timeline |
| `Action_None` | 272 | 273 | 2 | inferred_complete_timeline |
| `Action_None` | 277 | 299 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 19–251
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 183 | 165 | inferred_complete_timeline |
| `Action_PreSnap` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 199 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 244 | 251 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 19–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 389 | 371 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 19–389
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 178 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 328 | 75 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 389 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 19–323
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 179 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 236 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 238 | 323 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 19–292
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 238 | 220 | inferred_complete_timeline |
| `Action_PreSnap` | 245 | 266 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 292 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 19–304
- **Visible Samples:** 277

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 212 | 194 | inferred_complete_timeline |
| `Action_PreSnap` | 214 | 215 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 300 | 79 | inferred_complete_timeline |
| `Action_PreSnap` | 303 | 304 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 19–240
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 240 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 19–339
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 245 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 289 | 339 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 19–389
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 19 | 304 | 286 | inferred_complete_timeline |
| `Action_PreSnap` | 308 | 389 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 19–202 | 184 | 2 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 19–389 | 371 | 1 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 19–389 | 367 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 213–263 | 6 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 262–389 | 128 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 268–284 | 17 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 277–389 | 111 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 290–388 | 88 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 304–389 | 86 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 311–389 | 79 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 312–389 | 72 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 313–318 | 5 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 362–389 | 28 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 363–389 | 27 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 270: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ Row 270: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
- ⚠️ Row 270: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [19-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-268] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-332] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [182-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-255] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-214] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-221] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-389] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-187] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-240] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-270] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-273] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-240] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-300] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [303-304] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-218] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [220-223] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-179] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [188-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-323] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [289-339] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-188] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-251] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-238] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-266] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-328] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-389] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-235] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-214] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-263] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-284] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-306] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [290-370] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [372-373] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [384-388] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-374] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [380-381] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-315] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-318] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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