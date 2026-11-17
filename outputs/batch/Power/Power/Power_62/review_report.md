# Play-Annotation-Generator Annotation Review — Power_62

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_62`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 65
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 2
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 28 | START | 28 | 274 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 28 | START | 28 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 28 | START | 28 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 28 | START | 28 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 28 | START | 28 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 28 | START | 28 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 28 | START | 28 | 248 |
| ✅ EXACT | `Action_DownBlock` | RG | `1` | `1` | 222 | START | 222 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `13` | 222 | START | 222 | 240 |
| ✅ EXACT | `Action_PullBlock` | LG | `6` | `6` | 222 | START | 222 | 290 |

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
- **Visible Frames:** 28–291
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 291 | 264 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 28–281
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 248 | 221 | inferred_complete_timeline |
| `Action_PreSnap` | 270 | 271 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 277 | 281 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 28–327
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 274 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 284 | 286 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 290 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 294 | 327 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 28–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 329 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 28–319
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 221 | 194 | inferred_complete_timeline |
| `Action_PullBlock` | 222 | 290 | 69 | inferred_complete_timeline |
| `Action_None` | 291 | 292 | 2 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |
| `Action_None` | 303 | 304 | 2 | inferred_complete_timeline |
| `Action_None` | 309 | 313 | 5 | inferred_complete_timeline |
| `Action_None` | 315 | 319 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 28–311
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 221 | 194 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 240 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 257 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 261 | 264 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 266 | 267 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 270 | 290 | 21 | inferred_complete_timeline |
| `Action_None` | 291 | 311 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 28–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 221 | 194 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 290 | 69 | inferred_complete_timeline |
| `Action_None` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 329 | 302 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 215 | 188 | inferred_complete_timeline |
| `Action_PreSnap` | 301 | 329 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 231 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 234 | 246 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 249 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 329 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 28–236
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 38 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 214 | 174 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 306 | 279 | inferred_complete_timeline |
| `Action_PreSnap` | 309 | 311 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 314 | 329 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 28–279
- **Visible Samples:** 247

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 254 | 227 | inferred_complete_timeline |
| `Action_PreSnap` | 260 | 279 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 288 | 261 | inferred_complete_timeline |
| `Action_PreSnap` | 291 | 329 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 28–249
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 249 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 28–329
- **Visible Samples:** 302

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 28 | 329 | 302 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `4` | `4` | Position_Unknown | Team_Unknown | 28–329 | 298 | 3 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 28–203 | 173 | 3 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 28–34 | 7 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 237–329 | 64 | 2 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 255–329 | 75 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 275–295 | 10 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 276–294 | 19 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 295–329 | 35 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 306–329 | 24 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 314–329 | 16 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 316–329 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 126: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [28-274] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [284-286] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-290] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [294-327] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-306] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [309-311] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-141] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-250] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-288] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-292] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-304] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-319] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-254] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-279] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-248] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [270-271] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [277-281] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-249] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-154] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-203] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [222-240] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [244-257] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [261-264] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [266-267] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [270-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-311] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-231] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [234-246] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-249] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-291] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-215] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-38] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-214] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-227] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [235-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-34] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-245] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [275-276] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-281] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-288] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [292-295] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-294] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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

</details>