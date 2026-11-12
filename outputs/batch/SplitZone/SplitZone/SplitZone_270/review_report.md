# Play-Annotation-Generator Annotation Review — SplitZone_270

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_270`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 60
- **Validation Warnings:** 71
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `1` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `0` | `0` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 11 | 220 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 11 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 11 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 11 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 11 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 11 | 246 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 11 | 220 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `1` | `1` | 218 | START | 218 | 279 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `13` | `13` | 218 | START | 218 | 268 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `2` | `2` | 218 | START | 218 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `5` | 218 | START | 218 | 258 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `9` | 221 | END | 221 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `0` | `0` | 221 | START | 221 | 253 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `9` | 228 | START | 228 | 252 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `6` | 253 | START | 256 | 318 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 283 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 11–319
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 220 | 210 | inferred_complete_timeline |
| `Action_SnapReceive` | 221 | 221 | 1 | inferred_complete_timeline |
| `Action_None` | 222 | 227 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 228 | 252 | 25 | inferred_complete_timeline |
| `Action_None` | 253 | 319 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 11–353
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 246 | 236 | inferred_complete_timeline |
| `Action_BallCarry` | 256 | 318 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 320 | 344 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 346 | 353 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 11–291
- **Visible Samples:** 280

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 220 | 210 | inferred_complete_timeline |
| `Action_SplitBlock` | 221 | 253 | 33 | inferred_complete_timeline |
| `Action_SplitBlock` | 255 | 283 | 29 | inferred_complete_timeline |
| `Action_None` | 284 | 291 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 11–305
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 217 | 207 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 274 | 57 | inferred_complete_timeline |
| `Action_None` | 284 | 293 | 10 | inferred_complete_timeline |
| `Action_None` | 304 | 305 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 217 | 207 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 268 | 51 | inferred_complete_timeline |
| `Action_ZoneBlock` | 270 | 283 | 14 | inferred_complete_timeline |
| `Action_None` | 284 | 359 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 11–359
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 217 | 207 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 258 | 41 | inferred_complete_timeline |
| `Action_ZoneBlock` | 260 | 283 | 24 | inferred_complete_timeline |
| `Action_None` | 284 | 359 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 11–339
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 217 | 207 | inferred_complete_timeline |
| `Action_ZoneBlock` | 218 | 279 | 62 | inferred_complete_timeline |
| `Action_None` | 288 | 339 | 52 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 11–246
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 246 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 11–356
- **Visible Samples:** 344

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 214 | 204 | inferred_complete_timeline |
| `Action_PreSnap` | 217 | 356 | 140 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 15–86
- **Visible Samples:** 11

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 16 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 45 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 359 | 349 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 29 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 33 | 332 | 300 | inferred_complete_timeline |
| `Action_PreSnap` | 335 | 343 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 348 | 359 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 11–242
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 242 | 232 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 11–359
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 359 | 349 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 11–359 | 347 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 23–38 | 16 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 197–227 | 15 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 238–263 | 26 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 241–359 | 119 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 263–359 | 97 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 269–359 | 91 | 1 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 290–359 | 70 | 1 | Undefined position; Undefined team |
| `22` | `31` | Position_Unknown | Team_Unknown | 322–348 | 26 | 2 | Undefined position; Undefined team |
| `23` | `34` | Position_Unknown | Team_Unknown | 333–359 | 26 | 2 | Undefined position; Undefined team |
| `24` | `37` | Position_Unknown | Team_Unknown | 337–359 | 23 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 341–342 | 2 | 1 | Undefined position; Undefined team |
| `26` | `40` | Position_Unknown | Team_Unknown | 346–349 | 4 | 1 | Undefined position; Undefined team |
| `27` | `45` | Position_Unknown | Team_Unknown | 355–359 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `0` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 542: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_SplitBlock' range [221-253] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [255-283] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-291] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-279] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-339] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-274] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-293] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-258] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-246] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [256-318] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [320-344] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [346-353] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-242] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-359] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-319] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-29] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-332] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [335-343] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [348-359] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-314] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-359] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-356] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [218-268] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-359] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-16] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-45] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-227] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-263] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-344] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-348] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [333-335] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [341-342] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [346-349] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
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

</details>