# Play-Annotation-Generator Annotation Review — SplitZone_223

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_223`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 449
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `10` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `15` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_SplitBlock` | WR2 | offense | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `6` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 26 | START | 27 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 26 | START | 27 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `14` | `Group` | 26 | START | 27 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `15` | `Group` | 26 | START | 27 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 26 | START | 27 | 205 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 26 | START | 27 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 26 | START | 27 | 311 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 26 | START | 27 | 349 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 26 | START | 27 | 314 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `9` | `Group` | 26 | START | 27 | 317 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 312 | START | 312 | 315 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 315 | END | 312 | 315 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `10` | 315 | START | 315 | 340 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `11` | `11` | 315 | START | 316 | 320 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `15` | `15` | 315 | START | 315 | 328 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `18` | `18` | 315 | START | 315 | 348 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `8` | `8` | 315 | START | 315 | 327 |
| ✅ EXACT | `Action_SplitBlock` | WR2 | `9` | `9` | 318 | START | 318 | 389 |
| ✅ EXACT | `Action_Handoff` | QB | `2` | `2` | 344 | START | 344 | 349 |
| ✅ EXACT | `Action_BlockSecondLevel` | LT | `10` | `10` | 348 | START | 348 | 389 |
| ✅ EXACT | `Action_BallCarry` | RB | `6` | `6` | 350 | START | 350 | 449 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 389 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 27–438
- **Visible Samples:** 412

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_SnapReceive` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_None` | 316 | 343 | 28 | inferred_complete_timeline |
| `Action_Handoff` | 344 | 349 | 6 | inferred_complete_timeline |
| `Action_None` | 350 | 438 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 349 | 323 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 449 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 317 | 291 | inferred_complete_timeline |
| `Action_SplitBlock` | 318 | 389 | 72 | inferred_complete_timeline |
| `Action_None` | 390 | 449 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 421

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 314 | 288 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 340 | 26 | inferred_complete_timeline |
| `Action_ZoneBlock` | 343 | 347 | 5 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 348 | 389 | 42 | inferred_complete_timeline |
| `Action_None` | 390 | 449 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 36 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 79 | 314 | 236 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 328 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 333 | 389 | 57 | inferred_complete_timeline |
| `Action_None` | 390 | 449 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 27–320
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_BallSnap` | 312 | 315 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 316 | 320 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 27–348
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 205 | 179 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 314 | 106 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 348 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 27–449
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 314 | 288 | inferred_complete_timeline |
| `Action_ZoneBlock` | 315 | 327 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 339 | 341 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 368 | 389 | 22 | inferred_complete_timeline |
| `Action_None` | 390 | 449 | 60 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 380 | 69 | inferred_complete_timeline |
| `Action_None` | 385 | 449 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 378

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 115 | 89 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 311 | 151 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 27–365
- **Visible Samples:** 339

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 365 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 419

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 340 | 29 | inferred_complete_timeline |
| `Action_None` | 345 | 449 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 362 | 51 | inferred_complete_timeline |
| `Action_None` | 369 | 388 | 20 | inferred_complete_timeline |
| `Action_None` | 391 | 449 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 407

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 397 | 86 | inferred_complete_timeline |
| `Action_None` | 399 | 425 | 27 | inferred_complete_timeline |
| `Action_None` | 427 | 430 | 4 | inferred_complete_timeline |
| `Action_None` | 445 | 449 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 27–449
- **Visible Samples:** 423

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 27 | 311 | 285 | inferred_complete_timeline |
| `Action_None` | 312 | 449 | 138 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `20` | Position_Unknown | Team_Unknown | 27–94 | 68 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 111–162 | 51 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 161–449 | 289 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 331–333 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 340–449 | 110 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 349–449 | 101 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 352–449 | 98 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 397–402 | 6 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 419–443 | 14 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 420–449 | 9 | 3 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 433–435 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `11` (C): Annotated start 315 != Inferred start 316
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [312–315], lower_priority='Action_ZoneBlock' annotated_start=315, effective_Action_ZoneBlock_start=316.
- ⚠️ Action 'Action_None' range [350-438] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-397] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [399-425] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-430] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-380] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-327] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [339-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [348-389] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-449] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [316-320] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-449] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-449] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-77] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-328] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [333-389] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-115] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-449] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-362] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-388] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [315-348] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-365] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-94] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-340] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-449] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-112] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-162] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-333] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [340-449] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-402] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-424] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [436-443] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [420-422] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-427] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-449] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [433-435] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>