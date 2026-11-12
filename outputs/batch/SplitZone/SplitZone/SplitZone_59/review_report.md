# Play-Annotation-Generator Annotation Review — SplitZone_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_59`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `0` | `0` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_SplitBlock` | WR3 | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | WR3 | offense | `8` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `0` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `12` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 244 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `8` | `Group` | 0 | START | 0 | 253 |
| ✅ EXACT | `Action_BallSnap` | C | `0` | `0` | 245 | START | 245 | 258 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `0` | `0` | 248 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 248 | START | 248 | 360 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `18` | `18` | 248 | START | 248 | 360 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `19` | `19` | 248 | START | 248 | 360 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `20` | `20` | 248 | START | 248 | 360 |
| ✅ EXACT | `Action_SplitBlock` | WR3 | `8` | `8` | 254 | START | 254 | 276 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 260 | END | 245 | 260 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `15` | 263 | START | 263 | 268 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `5` | `5` | 269 | START | 269 | 341 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | WR3 | `8` | `8` | 277 | START | 277 | 292 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 360 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–439
- **Visible Samples:** 440

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_SnapReceive` | 245 | 260 | 16 | inferred_complete_timeline |
| `Action_None` | 261 | 262 | 2 | inferred_complete_timeline |
| `Action_Handoff` | 263 | 268 | 6 | inferred_complete_timeline |
| `Action_None` | 269 | 439 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–451
- **Visible Samples:** 449

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 268 | 269 | inferred_complete_timeline |
| `Action_BallCarry` | 269 | 341 | 73 | inferred_complete_timeline |
| `Action_BallCarry` | 343 | 347 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 350 | 451 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–491
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 491 | 247 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–464
- **Visible Samples:** 465

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 464 | 220 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 452

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_SplitBlock` | 254 | 276 | 23 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 277 | 292 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 294 | 302 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 305 | 308 | 4 | inferred_complete_timeline |
| `Action_None` | 362 | 454 | 93 | inferred_complete_timeline |
| `Action_None` | 457 | 509 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 508

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 485 | 241 | inferred_complete_timeline |
| `Action_None` | 488 | 509 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 360 | 113 | inferred_complete_timeline |
| `Action_None` | 361 | 509 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 360 | 113 | inferred_complete_timeline |
| `Action_None` | 361 | 509 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–258
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_BallSnap` | 245 | 258 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 360 | 113 | inferred_complete_timeline |
| `Action_None` | 361 | 509 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_ZoneBlock` | 248 | 360 | 113 | inferred_complete_timeline |
| `Action_None` | 361 | 509 | 149 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 509 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–316
- **Visible Samples:** 312

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 286 | 42 | inferred_complete_timeline |
| `Action_None` | 292 | 316 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 509 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 509 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 350 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–476
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 468 | 224 | inferred_complete_timeline |
| `Action_None` | 470 | 476 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–509
- **Visible Samples:** 510

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 509 | 265 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–398
- **Visible Samples:** 391

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 381 | 137 | inferred_complete_timeline |
| `Action_None` | 388 | 389 | 2 | inferred_complete_timeline |
| `Action_None` | 392 | 398 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 328 | 84 | inferred_complete_timeline |
| `Action_None` | 341 | 343 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–482
- **Visible Samples:** 482

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 439 | 195 | inferred_complete_timeline |
| `Action_None` | 441 | 482 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–490
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 244 | 245 | inferred_complete_timeline |
| `Action_None` | 245 | 465 | 221 | inferred_complete_timeline |
| `Action_None` | 468 | 470 | 3 | inferred_complete_timeline |
| `Action_None` | 476 | 477 | 2 | inferred_complete_timeline |
| `Action_None` | 488 | 490 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–24 | 6 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 253–262 | 7 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 283–509 | 216 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 313–334 | 18 | 3 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 337–509 | 173 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 349–350 | 2 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 360–371 | 12 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 375–376 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 382–509 | 128 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 389–509 | 114 | 4 | Undefined position; Undefined team |
| `32` | `40` | Position_Unknown | Team_Unknown | 409–509 | 101 | 1 | Undefined position; Undefined team |
| `33` | `47` | Position_Unknown | Team_Unknown | 458–468 | 10 | 2 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 463–466 | 4 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 467–487 | 6 | 2 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 471–509 | 27 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ZoneBlock` on target `0` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `8` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Resolved action overlap for track '0' (C): higher_priority='Action_BallSnap' [245–258], lower_priority='Action_ZoneBlock' annotated_start=248, effective_Action_ZoneBlock_start=259.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 113 frames exceeds threshold 90 frames [start=248, end=360].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (LG) duration 113 frames exceeds threshold 90 frames [start=248, end=360].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 113 frames exceeds threshold 90 frames [start=248, end=360].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 113 frames exceeds threshold 90 frames [start=248, end=360].
- ⚠️ Action 'Action_BallSnap' range [245-258] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-381] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-389] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-398] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-491] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [269-341] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [343-347] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [350-451] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-328] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-464] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [277-292] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [294-302] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [305-308] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-454] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-468] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-476] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-439] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-482] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-485] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-286] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-316] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-509] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-439] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-350] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-509] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-465] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-470] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-262] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-357] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [366-368] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-326] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-334] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-350] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-371] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-376] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-509] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-390] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-464] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-487] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [458-464] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [466-468] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-469] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [471-474] for track '36' has 1 frames without a visible bounding box.
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