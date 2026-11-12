# Play-Annotation-Generator Annotation Review — SplitZone_228

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_228`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 27
- **Ball Tracks:** 1
- **Action Segments:** 67
- **Validation Warnings:** 55
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `13` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `5` | `5` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `12` | `Group` | 8 | START | 9 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 8 | START | 9 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 8 | START | 9 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 8 | START | 9 | 219 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 8 | START | 9 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 8 | START | 9 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 8 | START | 9 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 8 | START | 9 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `8` | `8` | 217 | START | 220 | 351 |
| ✅ EXACT | `Action_BallSnap` | C | `5` | `5` | 217 | START | 217 | 231 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `12` | `12` | 220 | START | 220 | 297 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `13` | `13` | 220 | START | 220 | 233 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `2` | 220 | START | 220 | 249 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `3` | `3` | 220 | START | 220 | 281 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `5` | `5` | 220 | START | 232 | 297 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `18` | `17` | 223 | START | 223 | 297 |
| ❌ MISSING SEGMENT | `Action_Handoff` | QB | `7` | `7` | 227 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 231 | END | 217 | 231 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `2` | `2` | 250 | START | 250 | 297 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 297 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 9–342
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_SnapReceive` | 217 | 231 | 15 | inferred_complete_timeline |
| `Action_None` | 232 | 342 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 203 | 195 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 208 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 220 | 351 | 132 | inferred_complete_timeline |
| `Action_BallCarry` | 358 | 383 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 385 | 389 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 9–248
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 248 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 219 | 211 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 297 | 78 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |
| `Action_None` | 322 | 389 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 219 | 211 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 281 | 62 | inferred_complete_timeline |
| `Action_ZoneBlock` | 283 | 297 | 15 | inferred_complete_timeline |
| `Action_None` | 298 | 389 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_BallSnap` | 217 | 231 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 232 | 297 | 66 | inferred_complete_timeline |
| `Action_None` | 298 | 389 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 219 | 211 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 233 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 238 | 297 | 60 | inferred_complete_timeline |
| `Action_None` | 298 | 350 | 53 | inferred_complete_timeline |
| `Action_None` | 355 | 379 | 25 | inferred_complete_timeline |
| `Action_None` | 382 | 389 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–389
- **Visible Samples:** 381

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 219 | 211 | inferred_complete_timeline |
| `Action_ZoneBlock` | 220 | 249 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 250 | 297 | 48 | inferred_complete_timeline |
| `Action_None` | 298 | 389 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 380

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 272 | 56 | inferred_complete_timeline |
| `Action_None` | 274 | 389 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 9–373
- **Visible Samples:** 365

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 373 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–301
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 290 | 74 | inferred_complete_timeline |
| `Action_None` | 300 | 301 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–310
- **Visible Samples:** 301

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 216 | 207 | inferred_complete_timeline |
| `Action_None` | 217 | 310 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 379 | 163 | inferred_complete_timeline |
| `Action_None` | 386 | 389 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 291 | 75 | inferred_complete_timeline |
| `Action_None` | 321 | 389 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–389
- **Visible Samples:** 379

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 216 | 208 | inferred_complete_timeline |
| `Action_None` | 217 | 278 | 62 | inferred_complete_timeline |
| `Action_None` | 281 | 389 | 109 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 81–83 | 3 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 187–389 | 203 | 3 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 256–285 | 28 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 280–389 | 110 | 1 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 299–389 | 91 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 300–389 | 90 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 309–389 | 81 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 313–370 | 58 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 317–389 | 73 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 321–389 | 69 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 369–389 | 20 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 382–384 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `14` | `14` | 9 | 217 | 70 | 33.5% | 32–39, 42, 44–79, 118–131, 134–145, 148–155, 157–216 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `5` (C): Annotated start 220 != Inferred start 232
- ❌ Missing segment for action `Action_Handoff` on target `7` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 28 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [217–231], lower_priority='Action_ZoneBlock' annotated_start=220, effective_Action_ZoneBlock_start=232.
- ⚠️ Segment 'Action_Handoff' for track '7' has invalid range: start=227, end=216. Clamping end to start.
- ⚠️ Action 'Action_None' range [217-272] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-379] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-281] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-373] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-342] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-203] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-208] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [220-351] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [358-383] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-291] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-290] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-301] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-278] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [220-233] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [238-297] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-350] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-379] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-310] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-83] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [223-297] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-258] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-285] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-389] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-370] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-377] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-384] for track '27' has 1 frames without a visible bounding box.
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