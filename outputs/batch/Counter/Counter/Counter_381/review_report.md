# Play-Annotation-Generator Annotation Review — Counter_381

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_381`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 479
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 72
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `23` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | LG | offense | `23` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `11` | `Group` | 6 | START | 6 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 6 | START | 6 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 6 | START | 6 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 6 | START | 6 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 6 | START | 6 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `23` | `Group` | 6 | START | 29 | 271 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 6 | START | 6 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `4` | `Group` | 6 | START | 6 | 323 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 6 | START | 6 | 268 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 6 | START | 6 | 268 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `15` | 269 | START | 269 | 283 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `16` | `15` | 272 | START | 284 | 296 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `18` | `17` | 272 | START | 272 | 316 |
| ✅ EXACT | `Action_PullBlock` | LG | `23` | `21` | 272 | START | 272 | 336 |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | `2` | `1` | 272 | START | 272 | 360 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 283 | END | 269 | 283 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 301 | START | 301 | 323 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `4` | `3` | 324 | START | 324 | 344 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 360 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_SnapReceive` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_None` | 284 | 300 | 17 | inferred_complete_timeline |
| `Action_Handoff` | 301 | 323 | 23 | inferred_complete_timeline |
| `Action_None` | 324 | 479 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 323 | 318 | inferred_complete_timeline |
| `Action_BallCarry` | 324 | 344 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 347 | 354 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 358 | 389 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 396 | 479 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 271 | 266 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 272 | 360 | 89 | inferred_complete_timeline |
| `Action_None` | 361 | 479 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `23`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `23`
- **team_side:** `offense`
- **Visible Frames:** 29–336
- **Visible Samples:** 308

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 271 | 243 | inferred_complete_timeline |
| `Action_PullBlock` | 272 | 336 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_BallSnap` | 269 | 283 | 15 | inferred_complete_timeline |
| `Action_DownBlock` | 284 | 296 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 305 | 306 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 312 | 314 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 317 | 345 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 360 | 360 | 1 | inferred_complete_timeline |
| `Action_None` | 361 | 479 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–479
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 271 | 266 | inferred_complete_timeline |
| `Action_DownBlock` | 272 | 316 | 45 | inferred_complete_timeline |
| `Action_DownBlock` | 322 | 360 | 39 | inferred_complete_timeline |
| `Action_None` | 361 | 444 | 84 | inferred_complete_timeline |
| `Action_None` | 447 | 479 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 6–331
- **Visible Samples:** 326

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 331 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 306 | 38 | inferred_complete_timeline |
| `Action_None` | 314 | 317 | 4 | inferred_complete_timeline |
| `Action_None` | 333 | 372 | 40 | inferred_complete_timeline |
| `Action_None` | 374 | 420 | 47 | inferred_complete_timeline |
| `Action_None` | 424 | 479 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 6–315
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 315 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–298
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 298 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 466

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 304 | 36 | inferred_complete_timeline |
| `Action_None` | 308 | 352 | 45 | inferred_complete_timeline |
| `Action_None` | 358 | 479 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 6–476
- **Visible Samples:** 462

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 332 | 64 | inferred_complete_timeline |
| `Action_None` | 334 | 348 | 15 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 359 | 476 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 479 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 6–315
- **Visible Samples:** 310

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 315 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–371
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 268 | 263 | inferred_complete_timeline |
| `Action_None` | 269 | 352 | 84 | inferred_complete_timeline |
| `Action_None` | 354 | 358 | 5 | inferred_complete_timeline |
| `Action_None` | 362 | 371 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 6–479 | 472 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 316–479 | 144 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 329–479 | 148 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 353–479 | 123 | 3 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 383–479 | 97 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 397–439 | 12 | 4 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 398–479 | 80 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 400–448 | 49 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 426–428 | 3 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 432–433 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 764: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [269–283], lower_priority='Action_DownBlock' annotated_start=272, effective_Action_DownBlock_start=284.
- ⚠️ Action 'Action_None' range [269-315] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [272-360] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-479] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-344] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [347-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [358-389] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-479] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-352] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [354-358] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-371] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-306] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [314-317] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-372] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-420] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-304] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-352] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-331] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [284-296] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [305-306] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [312-314] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [317-345] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-298] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [272-316] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [322-360] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-444] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-268] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-315] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-332] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-348] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-476] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-475] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [29-271] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [272-336] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-322] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-479] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-332] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [353-354] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [356-360] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-479] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-401] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-427] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [438-439] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [398-465] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-479] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-448] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [426-428] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '30' has 1 frames without a visible bounding box.
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

</details>