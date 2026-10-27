# Play-Annotation-Generator Annotation Review — Counter_133

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_133`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 81
- **Validation Warnings:** 70
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `25` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `24` | `23` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullLeadBlock` | WR1 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `25` | `24` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `24` | `Group` | 0 | START | 15 | 161 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `25` | `Group` | 0 | START | 43 | 192 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 161 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 159 | START | 159 | 174 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 162 | START | 162 | 266 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 162 | START | 175 | 180 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `24` | `23` | 162 | START | 162 | 195 |
| ✅ EXACT | `Action_PullBlock` | RG | `18` | `17` | 162 | START | 162 | 222 |
| ✅ EXACT | `Action_PullLeadBlock` | WR1 | `4` | `3` | 162 | START | 162 | 266 |
| ✅ EXACT | `Action_SnapReceive` | QB | `20` | `19` | 174 | END | 159 | 174 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `25` | `24` | 193 | START | 193 | 265 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 266 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_SnapReceive` | 159 | 174 | 16 | inferred_complete_timeline |
| `Action_None` | 175 | 329 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `offense`
- **Visible Frames:** 43–318
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 43 | 192 | 150 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 265 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 271 | 305 | 35 | inferred_complete_timeline |
| `Action_BallCarry` | 310 | 318 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 162 | 266 | 105 | inferred_complete_timeline |
| `Action_None` | 267 | 314 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 314 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–325
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 206 | 48 | inferred_complete_timeline |
| `Action_None` | 212 | 215 | 4 | inferred_complete_timeline |
| `Action_None` | 219 | 316 | 98 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 266 | 105 | inferred_complete_timeline |
| `Action_None` | 267 | 267 | 1 | inferred_complete_timeline |
| `Action_None` | 272 | 321 | 50 | inferred_complete_timeline |
| `Action_None` | 323 | 328 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 15–327
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 15 | 161 | 147 | inferred_complete_timeline |
| `Action_DownBlock` | 162 | 195 | 34 | inferred_complete_timeline |
| `Action_DownBlock` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 221 | 266 | 46 | inferred_complete_timeline |
| `Action_None` | 267 | 327 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–209
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_BallSnap` | 159 | 174 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 175 | 180 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 198 | 201 | 4 | inferred_complete_timeline |
| `Action_DownBlock` | 206 | 209 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PullBlock` | 162 | 222 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–321
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 321 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–325
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 321 | 163 | inferred_complete_timeline |
| `Action_None` | 324 | 325 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 292 | 134 | inferred_complete_timeline |
| `Action_None` | 294 | 329 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–318
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 318 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–326
- **Visible Samples:** 323

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 319 | 161 | inferred_complete_timeline |
| `Action_None` | 324 | 326 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_None` | 159 | 329 | 171 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 0–32 | 32 | 2 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 0–20 | 21 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–37 | 28 | 5 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 131–133 | 3 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 211–329 | 108 | 3 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 232–234 | 3 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 244–319 | 74 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 257–258 | 2 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 304–305 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `24` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `25` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (LT) duration 105 frames exceeds threshold 90 frames [start=162, end=266].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [159–174], lower_priority='Action_DownBlock' annotated_start=162, effective_Action_DownBlock_start=175.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '23' (LG) duration 105 frames exceeds threshold 90 frames [start=162, end=266].
- ⚠️ Action 'Action_None' range [159-329] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-314] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-314] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-325] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-329] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-321] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-319] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '12' starts at frame 267, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [267-267] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-321] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-328] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-206] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-215] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-316] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-318] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [175-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [193-194] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [198-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [206-209] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [162-222] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-329] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-32] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-20] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-10] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-31] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-37] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [162-195] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [197-198] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-327] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [271-305] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [310-318] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [131-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-320] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-234] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-253] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-319] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-258] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-305] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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