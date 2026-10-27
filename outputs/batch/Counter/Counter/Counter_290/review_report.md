# Play-Annotation-Generator Annotation Review — Counter_290

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_290`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 21
- **Ball Tracks:** 1
- **Action Segments:** 61
- **Validation Warnings:** 48
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `7` | `6` |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 138 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 135 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `4` | 136 | START | 136 | 151 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `11` | `10` | 139 | START | 139 | 157 |
| ✅ EXACT | `Action_DownBlock` | LT | `3` | `2` | 139 | START | 139 | 181 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `5` | `4` | 139 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `7` | `6` | 139 | START | 139 | 184 |
| ⚠️ START CHANGED | `Action_PullLeadBlock` | C | `5` | `4` | 139 | START | 152 | 226 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 151 | END | 136 | 151 |
| ✅ EXACT | `Action_Handoff` | QB | `9` | `8` | 165 | START | 165 | 196 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `6` | `5` | 197 | START | 197 | 246 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 226 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–283
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_SnapReceive` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_None` | 152 | 164 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 165 | 196 | 32 | inferred_complete_timeline |
| `Action_None` | 197 | 271 | 75 | inferred_complete_timeline |
| `Action_None` | 278 | 283 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 196 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 197 | 246 | 50 | inferred_complete_timeline |
| `Action_BallCarry` | 251 | 255 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 258 | 276 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 278 | 299 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 181 | 43 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 234 | 99 | inferred_complete_timeline |
| `Action_None` | 239 | 250 | 12 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BallSnap` | 136 | 151 | 16 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 152 | 226 | 75 | inferred_complete_timeline |
| `Action_None` | 227 | 251 | 25 | inferred_complete_timeline |
| `Action_None` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PullBlock` | 139 | 184 | 46 | inferred_complete_timeline |
| `Action_PullBlock` | 187 | 194 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–267
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_DownBlock` | 139 | 157 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 163 | 174 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 226 | 40 | inferred_complete_timeline |
| `Action_None` | 227 | 264 | 38 | inferred_complete_timeline |
| `Action_None` | 266 | 267 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 283 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 299 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 222 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 205 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–287
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 251 | 116 | inferred_complete_timeline |
| `Action_None` | 263 | 277 | 15 | inferred_complete_timeline |
| `Action_None` | 280 | 283 | 4 | inferred_complete_timeline |
| `Action_None` | 285 | 287 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_None` | 136 | 258 | 123 | inferred_complete_timeline |
| `Action_None` | 261 | 287 | 27 | inferred_complete_timeline |
| `Action_None` | 290 | 299 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 69–299 | 231 | 2 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 73–299 | 226 | 3 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 194–290 | 96 | 2 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 216–299 | 84 | 1 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 227–299 | 73 | 1 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 238–299 | 62 | 1 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 252–299 | 48 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 274–299 | 26 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | 99 | 134 | 36 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `5` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `7` (2 segments found)
- ⚠️ `Action_PullLeadBlock` for actor_track_id `5` (C): Annotated start 139 != Inferred start 152
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `6` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 29 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Overlapping action conflict at frame 139 for track '4': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [136–151], lower_priority='Action_PullLeadBlock' annotated_start=139, effective_Action_PullLeadBlock_start=152.
- ⚠️ Action 'Action_None' range [136-283] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-181] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-251] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-277] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-283] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-287] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-251] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [197-246] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [251-255] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [258-276] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [139-184] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [187-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-222] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [165-196] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-271] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-283] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-205] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [139-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [163-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-264] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-267] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-234] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-250] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-258] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-287] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-164] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-290] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>