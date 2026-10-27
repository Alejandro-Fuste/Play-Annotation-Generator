# Play-Annotation-Generator Annotation Review — Counter_38

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_38`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 30
- **Ball Tracks:** 1
- **Action Segments:** 73
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `16` |
| ✅ EXACT | `Action_DownBlock` | RT | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `7` | `6` |
| ✅ EXACT | `Action_DownBlock` | C | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 171 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 0 | START | 0 | 160 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `18` | `16` | 159 | START | 193 | 193 |
| ✅ EXACT | `Action_DownBlock` | RT | `11` | `10` | 161 | START | 161 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `7` | `6` | 161 | START | 161 | 245 |
| ✅ EXACT | `Action_DownBlock` | C | `8` | `7` | 161 | START | 161 | 245 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `12` | `11` | 161 | START | 161 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `5` | `4` | 161 | START | 161 | 183 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 171 | END | 159 | 171 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `14` | `13` | 172 | START | 172 | 210 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 194 | START | 194 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `14` | `13` | 211 | START | 211 | 278 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 245 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 159 | 171 | 13 | inferred_complete_timeline |
| `Action_None` | 172 | 178 | 7 | inferred_complete_timeline |
| `Action_None` | 180 | 193 | 14 | inferred_complete_timeline |
| `Action_Handoff` | 194 | 210 | 17 | inferred_complete_timeline |
| `Action_None` | 211 | 270 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–292
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 171 | 172 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 172 | 210 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 211 | 278 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 281 | 292 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 161 | 183 | 23 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 185 | 245 | 61 | inferred_complete_timeline |
| `Action_None` | 246 | 269 | 24 | inferred_complete_timeline |
| `Action_None` | 272 | 290 | 19 | inferred_complete_timeline |
| `Action_None` | 297 | 299 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 236 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PullBlock` | 161 | 171 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 173 | 181 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 184 | 194 | 11 | inferred_complete_timeline |
| `Action_PullBlock` | 197 | 245 | 49 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 245 | 85 | inferred_complete_timeline |
| `Action_None` | 282 | 283 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 245 | 85 | inferred_complete_timeline |
| `Action_None` | 246 | 256 | 11 | inferred_complete_timeline |
| `Action_None` | 258 | 299 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_DownBlock` | 161 | 245 | 85 | inferred_complete_timeline |
| `Action_None` | 246 | 299 | 54 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 230 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 158 | 81 | inferred_complete_timeline |
| `Action_None` | 159 | 243 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 190 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 213 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 193–299 | 105 | 3 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 202–299 | 98 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 210–212 | 3 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 216–299 | 82 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 217–280 | 21 | 3 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 221–222 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 222–299 | 73 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 240–299 | 60 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 242–299 | 58 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 244–299 | 56 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 251–299 | 43 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 277–283 | 7 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 291–299 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | 0 | 100 | 75 | 74.3% | 48–52, 69, 76–77, 79–94, 98–99 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `18` (Position_Unknown): Annotated start 159 != Inferred start 193
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 37 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=193, end=171. Clamping end to start.
- ⚠️ Action 'Action_None' range [159-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-236] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [161-183] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-269] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-290] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-299] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-256] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [161-245] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-213] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-299] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [161-171] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [173-181] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [184-194] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-178] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-270] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [172-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [211-278] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [281-292] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-243] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-296] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-212] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-231] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-276] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-280] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-281] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-292] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-283] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-294] for track '30' has 1 frames without a visible bounding box.
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