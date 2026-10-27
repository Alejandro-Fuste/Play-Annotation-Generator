# Play-Annotation-Generator Annotation Review — Counter_177

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_177`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 329
- **Player Tracks:** 24
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 7
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 67
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `19` | `18` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `21` | `20` |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | Team_Unknown | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | OLB2 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | DE2 | defense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_BallCarry` | DE2 | defense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 184 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `19` | `18` | 185 | START | 185 | 188 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `19` | `18` | 189 | START | 189 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `21` | `20` | 189 | START | 189 | 258 |
| ✅ EXACT | `Action_PullBlock` | Position_Unknown | `1` | `0` | 189 | START | 189 | 271 |
| ✅ EXACT | `Action_PullLeadBlock` | OLB2 | `2` | `1` | 189 | START | 189 | 271 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | DE2 | `11` | `10` | 194 | START | 194 | 213 |
| ✅ EXACT | `Action_SnapReceive` | C | `15` | `14` | 198 | END | 185 | 198 |
| ✅ EXACT | `Action_Handoff` | C | `15` | `14` | 207 | START | 207 | 222 |
| ✅ EXACT | `Action_BallCarry` | DE2 | `11` | `10` | 223 | START | 223 | 329 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 271 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 210 | 26 | inferred_complete_timeline |
| `Action_None` | 212 | 329 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 321 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_SnapReceive` | 185 | 198 | 14 | inferred_complete_timeline |
| `Action_None` | 199 | 206 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 222 | 16 | inferred_complete_timeline |
| `Action_None` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 225 | 41 | inferred_complete_timeline |
| `Action_None` | 229 | 277 | 49 | inferred_complete_timeline |
| `Action_None` | 293 | 329 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–327
- **Visible Samples:** 325

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 258 | 74 | inferred_complete_timeline |
| `Action_None` | 262 | 327 | 66 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 194 | 213 | 20 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 219 | 222 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 228 | 44 | inferred_complete_timeline |
| `Action_None` | 233 | 236 | 4 | inferred_complete_timeline |
| `Action_None` | 243 | 329 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 220 | 36 | inferred_complete_timeline |
| `Action_None` | 223 | 263 | 41 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |
| `Action_None` | 275 | 276 | 2 | inferred_complete_timeline |
| `Action_None` | 281 | 282 | 2 | inferred_complete_timeline |
| `Action_None` | 292 | 304 | 13 | inferred_complete_timeline |
| `Action_None` | 306 | 329 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 189 | 271 | 83 | inferred_complete_timeline |
| `Action_None` | 272 | 295 | 24 | inferred_complete_timeline |
| `Action_None` | 299 | 309 | 11 | inferred_complete_timeline |
| `Action_None` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 184 | 185 | inferred_complete_timeline |
| `Action_None` | 185 | 247 | 63 | inferred_complete_timeline |
| `Action_None` | 249 | 283 | 35 | inferred_complete_timeline |
| `Action_None` | 285 | 309 | 25 | inferred_complete_timeline |
| `Action_None` | 311 | 329 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–329 | 323 | 6 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–329 | 321 | 5 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 0–306 | 295 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 0–329 | 330 | 4 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–329 | 310 | 3 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–329 | 329 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–329 | 329 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 4–19 | 11 | 2 | Undefined position; Undefined team |
| `23` | `37` | Position_Unknown | Team_Unknown | 324–329 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `11` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 46 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [272-276] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-300] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [302-303] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [189-271] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-309] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-329] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-258] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-327] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-225] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-277] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-329] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-247] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-283] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-309] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-321] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [194-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [216-217] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-329] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-228] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-236] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-329] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-263] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-276] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-304] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-329] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-329] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-247] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-260] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-274] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-242] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-257] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-306] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-271] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-184] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-261] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [189-258] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-253] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-12] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-19] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-329] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
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