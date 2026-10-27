# Play-Annotation-Generator Annotation Review — Counter_118

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_118`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 96
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB | defense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 215 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 90 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `16` | `14` | 214 | START | 214 | 218 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB | `1` | `0` | 216 | START | 216 | 251 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `6` | `5` | 216 | START | 216 | 232 |
| ✅ EXACT | `Action_PullBlock` | LG | `7` | `6` | 216 | START | 216 | 316 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `17` | `15` | 216 | START | 216 | 316 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | Position_Unknown | `16` | `14` | 219 | START | 219 | 403 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 229 | END | 214 | 229 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 246 | START | 246 | 256 |
| ✅ EXACT | `Action_BallCarry` | C | `6` | `5` | 257 | START | 257 | 408 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 316 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 368

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 90 | 91 | inferred_complete_timeline |
| `Action_PreSnap` | 93 | 213 | 121 | inferred_complete_timeline |
| `Action_SnapReceive` | 214 | 229 | 16 | inferred_complete_timeline |
| `Action_None` | 230 | 245 | 16 | inferred_complete_timeline |
| `Action_Handoff` | 246 | 256 | 11 | inferred_complete_timeline |
| `Action_None` | 257 | 369 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 419 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PullBlock` | 216 | 316 | 101 | inferred_complete_timeline |
| `Action_None` | 317 | 340 | 24 | inferred_complete_timeline |
| `Action_None` | 349 | 419 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–408
- **Visible Samples:** 404

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 232 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 238 | 256 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 257 | 408 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–413
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 243 | 30 | inferred_complete_timeline |
| `Action_None` | 246 | 413 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 418

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 252 | 39 | inferred_complete_timeline |
| `Action_None` | 255 | 419 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–353
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 233 | 20 | inferred_complete_timeline |
| `Action_None` | 241 | 353 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 419 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–302
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 302 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–300
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_None` | 214 | 229 | 16 | inferred_complete_timeline |
| `Action_None` | 257 | 258 | 2 | inferred_complete_timeline |
| `Action_None` | 299 | 300 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_DownBlock` | 216 | 251 | 36 | inferred_complete_timeline |
| `Action_DownBlock` | 253 | 264 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `12` | Position_Unknown | Team_Unknown | 12–333 | 320 | 4 | Undefined position; Undefined team |
| `12` | `14` | Position_Unknown | Team_Unknown | 36–340 | 303 | 3 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 53–119 | 67 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 54–419 | 361 | 5 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 67–384 | 318 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 142–419 | 247 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 246–419 | 173 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 273–290 | 18 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 289–391 | 103 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 295–419 | 124 | 2 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 295–320 | 26 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 296–411 | 116 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 305–419 | 115 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 310–419 | 106 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 333–419 | 80 | 3 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 338–419 | 82 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 343–415 | 73 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 371–415 | 27 | 6 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 403–406 | 4 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 410–419 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `16` (3 segments found)

### Track Identity Issues

- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '6' (LG) duration 101 frames exceeds threshold 90 frames [start=216, end=316].
- ⚠️ Action 'Action_DownBlock' range [216-251] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [253-264] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-252] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-419] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-243] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-413] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-233] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-353] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [216-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [238-256] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [257-408] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [216-316] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-340] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-419] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-369] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-229] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-300] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-302] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-307] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-313] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-333] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-231] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-340] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [219-403] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [406-412] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-384] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-190] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-321] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-314] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-419] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-290] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-391] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-370] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-320] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-411] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-419] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-419] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-336] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-415] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-396] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-406] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-415] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-406] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>