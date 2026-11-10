# Play-Annotation-Generator Annotation Review — Sack_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Sack_6`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Defense_Sack`
- **Result:** `Result_Unknown`
- **Result Frame:** 329
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 37
- **Validation Warnings:** 44
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 10
- **Exact Matches:** 3
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 24
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB1 | defense | `8` | `8` |
| ✅ EXACT | `Action_WrapQuarterback` | LB1 | defense | `8` | `8` |
| ✅ EXACT | `Action_SackQuarterback` | LB1 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 7 | START | 7 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 7 | START | 7 | 287 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 7 | START | 7 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 7 | START | 7 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 7 | START | 7 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 7 | START | 7 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 7 | START | 7 | 253 |
| ✅ EXACT | `Action_CloseOnQuarterback` | LB1 | `8` | `8` | 252 | START | 252 | 267 |
| ✅ EXACT | `Action_WrapQuarterback` | LB1 | `8` | `8` | 268 | START | 268 | 274 |
| ✅ EXACT | `Action_SackQuarterback` | LB1 | `8` | `8` | 275 | START | 275 | 293 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 287 | 281 | inferred_complete_timeline |
| `Action_PreSnap` | 292 | 329 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 7–192
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 192 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 329 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 253 | 247 | inferred_complete_timeline |
| `Action_PreSnap` | 257 | 266 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 268 | 329 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 329 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 329 | 323 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 329 | 323 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 7–297
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 282 | 276 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 297 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 7–243
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 243 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 7–329
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 242 | 236 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 294 | 41 | inferred_complete_timeline |
| `Action_PreSnap` | 296 | 313 | 18 | inferred_complete_timeline |
| `Action_PreSnap` | 316 | 329 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 7–212
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 75 | 69 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 212 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 7–293
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 251 | 245 | inferred_complete_timeline |
| `Action_CloseOnQuarterback` | 252 | 267 | 16 | inferred_complete_timeline |
| `Action_WrapQuarterback` | 268 | 274 | 7 | inferred_complete_timeline |
| `Action_SackQuarterback` | 275 | 293 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 7–255
- **Visible Samples:** 249

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 255 | 249 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 7–46
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 46 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 7–329
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 329 | 323 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 218–226 | 9 | 1 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 252–322 | 71 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 254–282 | 19 | 2 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 290–329 | 40 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 295–329 | 35 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 295–329 | 35 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 297–329 | 33 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 307–329 | 23 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 312–329 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 25 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [7-243] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-46] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-255] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-329] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SackQuarterback' range [275-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-253] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [257-266] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-329] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-282] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-287] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-294] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [296-313] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-212] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-226] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-322] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-270] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [307-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [312-323] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [327-329] for track '23' has 1 frames without a visible bounding box.
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

</details>