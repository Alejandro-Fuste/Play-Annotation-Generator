# Play-Annotation-Generator Annotation Review — PinAndPull_12

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_12`
- **Frame Range:** 0 to 479 (480 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 479
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 127
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 3
- **Inferred Coverage Segments (Action_None):** 109
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `21` |
| ℹ️ GLOBAL EVENT | `Action_DownBlock` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | Team_Unknown | `9` | `9` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `20` | `20` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `14` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 208 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `20` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 20 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `8` | 21 | START | 21 | 224 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `21` | 201 | START | 201 | 214 |
| ℹ️ GLOBAL EVENT | `Action_DownBlock` | N/A | N/A | N/A | 209 | START | N/A | N/A |
| ✅ EXACT | `Action_PullBlock` | RG | `17` | `17` | 209 | START | 209 | 282 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `14` | `14` | 209 | START | 209 | 255 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `9` | `9` | 214 | END | 201 | 214 |
| ✅ EXACT | `Action_Handoff` | Position_Unknown | `9` | `9` | 224 | START | 224 | 237 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `20` | `20` | 238 | START | 238 | 295 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 282 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 479 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 474

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 286 | 86 | inferred_complete_timeline |
| `Action_None` | 293 | 479 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–295
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 64 | 237 | 174 | inferred_complete_timeline |
| `Action_BallCarry` | 238 | 295 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 427

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 209 | 255 | 47 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 262 | 282 | 21 | inferred_complete_timeline |
| `Action_None` | 283 | 287 | 5 | inferred_complete_timeline |
| `Action_None` | 321 | 407 | 87 | inferred_complete_timeline |
| `Action_None` | 421 | 423 | 3 | inferred_complete_timeline |
| `Action_None` | 425 | 479 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 301 | 101 | inferred_complete_timeline |
| `Action_None` | 303 | 331 | 29 | inferred_complete_timeline |
| `Action_None` | 333 | 479 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–249
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 20 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 21 | 224 | 204 | inferred_complete_timeline |
| `Action_DownBlock` | 228 | 235 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 238 | 240 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 248 | 249 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 200 | 167 | inferred_complete_timeline |
| `Action_BallSnap` | 201 | 214 | 14 | inferred_complete_timeline |
| `Action_None` | 215 | 222 | 8 | inferred_complete_timeline |
| `Action_None` | 224 | 228 | 5 | inferred_complete_timeline |
| `Action_None` | 234 | 341 | 108 | inferred_complete_timeline |
| `Action_None` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_None` | 355 | 360 | 6 | inferred_complete_timeline |
| `Action_None` | 368 | 479 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–288
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 208 | 209 | inferred_complete_timeline |
| `Action_PullBlock` | 209 | 282 | 74 | inferred_complete_timeline |
| `Action_None` | 283 | 288 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–479
- **Visible Samples:** 461

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 341 | 141 | inferred_complete_timeline |
| `Action_None` | 343 | 345 | 3 | inferred_complete_timeline |
| `Action_None` | 349 | 360 | 12 | inferred_complete_timeline |
| `Action_None` | 373 | 392 | 20 | inferred_complete_timeline |
| `Action_None` | 396 | 479 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 472

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 336 | 136 | inferred_complete_timeline |
| `Action_None` | 339 | 340 | 2 | inferred_complete_timeline |
| `Action_None` | 346 | 365 | 20 | inferred_complete_timeline |
| `Action_None` | 367 | 479 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 479 | 279 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 234 | 34 | inferred_complete_timeline |
| `Action_None` | 294 | 297 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–336
- **Visible Samples:** 337

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 336 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 282 | 82 | inferred_complete_timeline |
| `Action_None` | 285 | 389 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 454

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 284 | 84 | inferred_complete_timeline |
| `Action_None` | 288 | 347 | 60 | inferred_complete_timeline |
| `Action_None` | 355 | 356 | 2 | inferred_complete_timeline |
| `Action_None` | 373 | 479 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 362 | 162 | inferred_complete_timeline |
| `Action_None` | 365 | 479 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 315 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 369 | 169 | inferred_complete_timeline |
| `Action_None` | 371 | 373 | 3 | inferred_complete_timeline |
| `Action_None` | 396 | 479 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–479
- **Visible Samples:** 480

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 479 | 279 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–479 | 470 | 7 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–251 | 252 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–479 | 476 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 52–53 | 2 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 83–85 | 3 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 251–260 | 10 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 260–360 | 101 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 267–479 | 187 | 9 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 290–477 | 169 | 6 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 292–479 | 177 | 5 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 304–467 | 157 | 4 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 321–479 | 157 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 371–479 | 102 | 3 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 372–479 | 108 | 1 | Undefined position; Undefined team |
| `33` | `39` | Position_Unknown | Team_Unknown | 372–479 | 108 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 408–409 | 2 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 432–433 | 2 | 1 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 448–473 | 9 | 3 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 464–479 | 15 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 26: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ Row 26: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LG) duration 229 frames exceeds threshold 90 frames [start=21, end=249].
- ⚠️ Action 'Action_None' range [201-362] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-301] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-331] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-286] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-479] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-284] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-347] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-356] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-336] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-369] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-373] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [21-224] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [228-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [238-240] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [248-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-362] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [370-406] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-297] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-282] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-389] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-251] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [209-255] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-407] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-423] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-336] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-340] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [346-365] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-479] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-367] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [209-282] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-288] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-341] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-360] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [373-392] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-479] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-315] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [238-295] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-222] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-228] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-341] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-345] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-360] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-479] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [52-53] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-85] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-260] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-360] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-296] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [301-303] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-307] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-315] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-341] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-358] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-422] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-362] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-381] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-394] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-398] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-403] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [415-477] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-388] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-394] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-407] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-413] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-330] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-365] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-409] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-467] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-388] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-407] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [410-425] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [372-479] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-409] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-433] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-450] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [453-454] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-473] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-477] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.

</details>