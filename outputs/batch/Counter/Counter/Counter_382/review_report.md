# Play-Annotation-Generator Annotation Review — Counter_382

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_382`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 78
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
- **Inferred Coverage Segments (Action_None):** 65
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | defense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | SAF1 | defense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 221 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | FB | `9` | `Group` | 0 | START | 0 | 169 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 170 | START | 170 | 182 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 173 | START | 183 | 189 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LB1 | `2` | `1` | 173 | START | 173 | 211 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | SAF1 | `11` | `10` | 173 | START | 173 | 180 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `18` | `16` | 173 | START | 173 | 260 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 182 | END | 170 | 182 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 203 | START | 203 | 221 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 222 | START | 222 | 320 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 260 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_SnapReceive` | 170 | 182 | 13 | inferred_complete_timeline |
| `Action_None` | 183 | 202 | 20 | inferred_complete_timeline |
| `Action_Handoff` | 203 | 221 | 19 | inferred_complete_timeline |
| `Action_None` | 222 | 270 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 221 | 222 | inferred_complete_timeline |
| `Action_BallCarry` | 222 | 320 | 99 | inferred_complete_timeline |
| `Action_BallCarry` | 323 | 389 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>FB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 389 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 325 | 156 | inferred_complete_timeline |
| `Action_None` | 334 | 389 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_BallSnap` | 170 | 182 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 183 | 189 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 191 | 216 | 26 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 254 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 257 | 260 | 4 | inferred_complete_timeline |
| `Action_None` | 261 | 389 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–366
- **Visible Samples:** 364

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 203 | 34 | inferred_complete_timeline |
| `Action_None` | 205 | 214 | 10 | inferred_complete_timeline |
| `Action_None` | 216 | 230 | 15 | inferred_complete_timeline |
| `Action_None` | 232 | 366 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 228 | 59 | inferred_complete_timeline |
| `Action_None` | 233 | 389 | 157 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 389 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 245 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–363
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 288 | 119 | inferred_complete_timeline |
| `Action_None` | 300 | 363 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 208 | 39 | inferred_complete_timeline |
| `Action_None` | 210 | 215 | 6 | inferred_complete_timeline |
| `Action_None` | 219 | 220 | 2 | inferred_complete_timeline |
| `Action_None` | 228 | 234 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_DownBlock` | 173 | 211 | 39 | inferred_complete_timeline |
| `Action_DownBlock` | 215 | 260 | 46 | inferred_complete_timeline |
| `Action_None` | 261 | 389 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 215 | 46 | inferred_complete_timeline |
| `Action_None` | 221 | 232 | 12 | inferred_complete_timeline |
| `Action_None` | 234 | 238 | 5 | inferred_complete_timeline |
| `Action_None` | 240 | 326 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 123 | 124 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 136 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 172 | 35 | inferred_complete_timeline |
| `Action_PullBlock` | 173 | 180 | 8 | inferred_complete_timeline |
| `Action_PullBlock` | 186 | 241 | 56 | inferred_complete_timeline |
| `Action_PullBlock` | 252 | 253 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 169 | 170 | inferred_complete_timeline |
| `Action_None` | 170 | 294 | 125 | inferred_complete_timeline |
| `Action_None` | 297 | 360 | 64 | inferred_complete_timeline |
| `Action_None` | 369 | 389 | 21 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–366 | 366 | 3 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 125–330 | 206 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 153–389 | 237 | 2 | Undefined position; Undefined team |
| `18` | `25` | Position_Unknown | Team_Unknown | 261–347 | 87 | 1 | Undefined position; Undefined team |
| `19` | `26` | Position_Unknown | Team_Unknown | 270–306 | 35 | 3 | Undefined position; Undefined team |
| `20` | `28` | Position_Unknown | Team_Unknown | 288–328 | 41 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 300–389 | 89 | 2 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 310–361 | 52 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 327–389 | 63 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 331–389 | 59 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 356–389 | 34 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 372–389 | 18 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 380–389 | 10 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 383–389 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 387–389 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 766: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [170–182], lower_priority='Action_DownBlock' annotated_start=173, effective_Action_DownBlock_start=183.
- ⚠️ Action 'Action_None' range [170-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-366] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [173-211] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-389] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-228] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [222-320] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-215] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-232] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-238] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-326] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-294] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-360] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [173-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [186-241] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [252-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-230] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-366] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [183-189] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [191-216] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [222-254] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-270] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-288] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-363] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-215] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-220] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-234] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-330] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-347] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-298] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-306] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-328] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-375] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-361] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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