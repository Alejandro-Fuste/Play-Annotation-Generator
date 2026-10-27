# Play-Annotation-Generator Annotation Review — Counter_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_32`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 359
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 70
- **Validation Warnings:** 62
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 52
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `7` | `6` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | HB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `13` | `12` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 223 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | HB | `16` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 181 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 179 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `6` | `5` | 180 | START | 180 | 263 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `7` | `6` | 180 | START | 180 | 219 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `9` | `8` | 180 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `15` | `14` | 180 | START | 180 | 202 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | HB | `16` | `15` | 180 | START | 180 | 227 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 182 | START | 182 | 199 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 199 | END | 182 | 199 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 207 | START | 207 | 223 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `13` | `12` | 224 | START | 224 | 236 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 263 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_SnapReceive` | 182 | 199 | 18 | inferred_complete_timeline |
| `Action_None` | 200 | 206 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 207 | 223 | 17 | inferred_complete_timeline |
| `Action_None` | 224 | 359 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 223 | 224 | inferred_complete_timeline |
| `Action_BallCarry` | 224 | 236 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 359 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>HB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 180 | 227 | 48 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 233 | 263 | 31 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 345

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 202 | 21 | inferred_complete_timeline |
| `Action_None` | 216 | 223 | 8 | inferred_complete_timeline |
| `Action_None` | 226 | 359 | 134 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PullBlock` | 180 | 202 | 23 | inferred_complete_timeline |
| `Action_PullBlock` | 204 | 210 | 7 | inferred_complete_timeline |
| `Action_PullBlock` | 212 | 263 | 52 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–266
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_None` | 180 | 181 | 2 | inferred_complete_timeline |
| `Action_BallSnap` | 182 | 199 | 18 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 210 | 223 | 14 | inferred_complete_timeline |
| `Action_None` | 225 | 233 | 9 | inferred_complete_timeline |
| `Action_None` | 241 | 246 | 6 | inferred_complete_timeline |
| `Action_None` | 257 | 266 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 263 | 84 | inferred_complete_timeline |
| `Action_None` | 264 | 359 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 219 | 40 | inferred_complete_timeline |
| `Action_DownBlock` | 222 | 263 | 42 | inferred_complete_timeline |
| `Action_None` | 264 | 296 | 33 | inferred_complete_timeline |
| `Action_None` | 299 | 359 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–253
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 235 | 54 | inferred_complete_timeline |
| `Action_None` | 239 | 253 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 359 | 178 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–264
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 264 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 181 | 182 | inferred_complete_timeline |
| `Action_None` | 182 | 192 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–359 | 360 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 105–201 | 96 | 3 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 114–202 | 89 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 243–359 | 117 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 267–359 | 92 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 272–359 | 88 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 274–359 | 86 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 278–285 | 8 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 287–359 | 73 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 288–290 | 3 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 295–359 | 65 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 312–321 | 10 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 316–359 | 44 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 326–331 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | 59 | 67 | 9 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `9` (C)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 66: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [182–199], lower_priority='Action_DownBlock' annotated_start=180, effective_Action_DownBlock_start=200.
- ⚠️ Action 'Action_None' range [182-264] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-359] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [180-219] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-296] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-223] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-233] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-246] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-223] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [224-236] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-359] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-235] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-253] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [180-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [212-263] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [180-227] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-359] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-161] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-202] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-275] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-321] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-331] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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

</details>