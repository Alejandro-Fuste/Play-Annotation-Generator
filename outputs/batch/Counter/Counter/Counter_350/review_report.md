# Play-Annotation-Generator Annotation Review — Counter_350

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_350`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 33
- **Ball Tracks:** 2
- **Action Segments:** 101
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | DE2 | defense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `13` | `12` |
| ✅ EXACT | `Action_PullLeadBlock` | DT1 | defense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `11` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `13` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 164 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `7` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `8` | `Group` | 0 | START | 0 | 160 |
| ✅ EXACT | `Action_BallSnap` | C | `7` | `6` | 161 | START | 161 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `11` | `10` | 164 | START | 164 | 178 |
| ✅ EXACT | `Action_DownBlock` | DE2 | `5` | `4` | 164 | START | 164 | 244 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `7` | `6` | 164 | START | 175 | 242 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `13` | `12` | 164 | START | 164 | 205 |
| ✅ EXACT | `Action_PullLeadBlock` | DT1 | `16` | `14` | 164 | START | 164 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_PlaySideFakeStep` | RB | `4` | `3` | 165 | START | 165 | 197 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `11` | 174 | END | 161 | 174 |
| ✅ EXACT | `Action_Handoff` | QB | `12` | `11` | 184 | START | 184 | 203 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `4` | `3` | 204 | START | 204 | 300 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 244 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_SnapReceive` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_None` | 175 | 183 | 9 | inferred_complete_timeline |
| `Action_Handoff` | 184 | 203 | 20 | inferred_complete_timeline |
| `Action_None` | 204 | 419 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 347

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 164 | 165 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 165 | 197 | 33 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 200 | 203 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 300 | 97 | inferred_complete_timeline |
| `Action_BallCarry` | 303 | 323 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 330 | 356 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–342
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PullBlock` | 164 | 205 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 211 | 244 | 34 | inferred_complete_timeline |
| `Action_None` | 245 | 342 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_BallSnap` | 161 | 174 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 242 | 68 | inferred_complete_timeline |
| `Action_DownBlock` | 244 | 244 | 1 | inferred_complete_timeline |
| `Action_None` | 245 | 336 | 92 | inferred_complete_timeline |
| `Action_None` | 338 | 395 | 58 | inferred_complete_timeline |
| `Action_None` | 398 | 419 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 193 | 33 | inferred_complete_timeline |
| `Action_None` | 196 | 229 | 34 | inferred_complete_timeline |
| `Action_None` | 231 | 339 | 109 | inferred_complete_timeline |
| `Action_None` | 342 | 343 | 2 | inferred_complete_timeline |
| `Action_None` | 345 | 356 | 12 | inferred_complete_timeline |
| `Action_None` | 359 | 419 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–419
- **Visible Samples:** 417

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 180 | 208 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 211 | 244 | 34 | inferred_complete_timeline |
| `Action_None` | 245 | 419 | 175 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 419 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 398

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_DownBlock` | 164 | 244 | 81 | inferred_complete_timeline |
| `Action_None` | 245 | 326 | 82 | inferred_complete_timeline |
| `Action_None` | 349 | 419 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 68–419
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 68 | 163 | 96 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 164 | 224 | 61 | inferred_complete_timeline |
| `Action_None` | 247 | 419 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 420

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 419 | 259 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–419
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 278 | 118 | inferred_complete_timeline |
| `Action_None` | 280 | 330 | 51 | inferred_complete_timeline |
| `Action_None` | 332 | 344 | 13 | inferred_complete_timeline |
| `Action_None` | 346 | 407 | 62 | inferred_complete_timeline |
| `Action_None` | 413 | 419 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 280 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_None` | 161 | 237 | 77 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–419 | 418 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 116–373 | 248 | 5 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 204–206 | 3 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 208–419 | 210 | 3 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 215–321 | 101 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 235–238 | 4 | 1 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 237–249 | 4 | 2 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 239–411 | 164 | 4 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 239–419 | 181 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 284–366 | 75 | 2 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 284–288 | 5 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 285–334 | 25 | 5 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 291–397 | 106 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 292–419 | 128 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 355–419 | 65 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 356–419 | 32 | 7 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 366–383 | 15 | 2 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 396–419 | 24 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 398–418 | 21 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 403–404 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | 0 | 74 | 69 | 92.0% | 29, 60–61, 63–64, 67 |
| `16` | `19` | 127 | 157 | 30 | 96.8% | 131 |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PlaySideFakeStep` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 702: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [161–174], lower_priority='Action_DownBlock' annotated_start=164, effective_Action_DownBlock_start=175.
- ⚠️ Action 'Action_None' range [161-237] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-419] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-228] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-419] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [165-197] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-300] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [303-323] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [330-356] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-326] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-278] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-330] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [332-344] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-407] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-242] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-395] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-193] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-229] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-339] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-343] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-356] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-419] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-280] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [164-178] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [180-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [164-205] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-342] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [164-224] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-261] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-274] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-373] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-325] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-407] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-313] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-321] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-387] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-411] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-353] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-366] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-288] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-289] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-306] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-313] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-382] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-397] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-361] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-366] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-370] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [377-378] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [380-382] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-407] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-378] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-418] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.

</details>