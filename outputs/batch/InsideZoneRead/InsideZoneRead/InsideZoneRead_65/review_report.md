# Play-Annotation-Generator Annotation Review — InsideZoneRead_65

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_65`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 103
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 191 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 156 |
| ✅ EXACT | `Action_BallSnap` | C | `20` | `19` | 157 | START | 157 | 166 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 159 | START | 159 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `16` | `15` | 159 | START | 159 | 224 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `18` | `17` | 159 | START | 159 | 224 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `20` | `19` | 159 | START | 167 | 171 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `21` | `20` | 159 | START | 159 | 173 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 166 | END | 157 | 166 |
| ✅ EXACT | `Action_ReadDefender` | QB | `14` | `13` | 173 | START | 173 | 185 |
| ✅ EXACT | `Action_Handoff` | QB | `14` | `13` | 186 | START | 186 | 191 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `9` | 192 | START | 192 | 406 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 224 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–392
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_SnapReceive` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_None` | 167 | 172 | 6 | inferred_complete_timeline |
| `Action_ReadDefender` | 173 | 185 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 186 | 191 | 6 | inferred_complete_timeline |
| `Action_None` | 192 | 392 | 201 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–445
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 191 | 192 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 406 | 215 | inferred_complete_timeline |
| `Action_BallCarry` | 410 | 411 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 415 | 416 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 418 | 430 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 434 | 445 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 354 | 198 | inferred_complete_timeline |
| `Action_None` | 372 | 374 | 3 | inferred_complete_timeline |
| `Action_None` | 383 | 392 | 10 | inferred_complete_timeline |
| `Action_None` | 399 | 449 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–434
- **Visible Samples:** 435

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 434 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–393
- **Visible Samples:** 394

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 393 | 237 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 224 | 66 | inferred_complete_timeline |
| `Action_None` | 225 | 225 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–442
- **Visible Samples:** 443

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 224 | 66 | inferred_complete_timeline |
| `Action_None` | 225 | 442 | 218 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_BallSnap` | 157 | 166 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 167 | 171 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–369
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 173 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 184 | 211 | 28 | inferred_complete_timeline |
| `Action_ZoneBlock` | 213 | 224 | 12 | inferred_complete_timeline |
| `Action_None` | 225 | 369 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–350
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_ZoneBlock` | 159 | 224 | 66 | inferred_complete_timeline |
| `Action_None` | 225 | 232 | 8 | inferred_complete_timeline |
| `Action_None` | 234 | 350 | 117 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 185 | 29 | inferred_complete_timeline |
| `Action_None` | 194 | 218 | 25 | inferred_complete_timeline |
| `Action_None` | 220 | 447 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 449 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–440
- **Visible Samples:** 441

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 440 | 284 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 215 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–440
- **Visible Samples:** 439

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 424 | 268 | inferred_complete_timeline |
| `Action_None` | 427 | 440 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–447
- **Visible Samples:** 437

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 201 | 45 | inferred_complete_timeline |
| `Action_None` | 211 | 214 | 4 | inferred_complete_timeline |
| `Action_None` | 216 | 291 | 76 | inferred_complete_timeline |
| `Action_None` | 293 | 447 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 449 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–384
- **Visible Samples:** 384

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 349 | 193 | inferred_complete_timeline |
| `Action_None` | 351 | 384 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 449 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 449 | 293 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–417
- **Visible Samples:** 416

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 156 | 157 | inferred_complete_timeline |
| `Action_None` | 157 | 302 | 146 | inferred_complete_timeline |
| `Action_None` | 305 | 417 | 113 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–449 | 450 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 182–186 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 202–406 | 190 | 6 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 229–449 | 221 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 237–399 | 142 | 5 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 252–277 | 14 | 4 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 292–359 | 64 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 320–323 | 4 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 323–329 | 4 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 355–384 | 30 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 371–372 | 2 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 387–449 | 59 | 4 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 398–402 | 5 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 401–403 | 3 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 411–439 | 29 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 447–449 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (5 segments found)

### Track Identity Issues

- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 65 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 132: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [157–166], lower_priority='Action_ZoneBlock' annotated_start=159, effective_Action_ZoneBlock_start=167.
- ⚠️ Action 'Action_None' range [157-393] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-374] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-392] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-434] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-349] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-384] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-417] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-406] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [410-411] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [415-416] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [418-430] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [434-445] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-224] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-350] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-214] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [216-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-447] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-392] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-185] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-218] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-447] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-442] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-440] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '17' starts at frame 225, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [225-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-424] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-440] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [167-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [159-173] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [184-211] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-369] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-215] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-406] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-312] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-316] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-399] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-259] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [276-277] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-301] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-359] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-323] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-384] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-372] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-404] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-413] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-437] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-402] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-403] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-439] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>