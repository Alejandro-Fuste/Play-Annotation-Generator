# Play-Annotation-Generator Annotation Review — Counter_385

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_385`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 389
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 63
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | TE1 | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | offense | `4` | `3` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `15` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `20` | `Group` | 0 | START | 0 | 217 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 2 | 7 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 247 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 214 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 253 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 215 | START | 215 | 229 |
| ✅ EXACT | `Action_DownBlock` | LT | `11` | `10` | 218 | START | 218 | 296 |
| ✅ EXACT | `Action_DownBlock` | TE1 | `20` | `19` | 218 | START | 218 | 309 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `22` | `21` | 218 | START | 218 | 272 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 229 | END | 215 | 229 |
| ✅ EXACT | `Action_Handoff` | QB | `13` | `12` | 243 | START | 243 | 264 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `16` | `15` | 248 | START | 248 | 292 |
| ✅ EXACT | `Action_PullLeadBlock` | TE2 | `4` | `3` | 248 | START | 248 | 309 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 265 | START | 265 | 330 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 309 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–377
- **Visible Samples:** 377

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_SnapReceive` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 242 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 243 | 264 | 22 | inferred_complete_timeline |
| `Action_None` | 265 | 306 | 42 | inferred_complete_timeline |
| `Action_None` | 308 | 377 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_PreSnap` | 258 | 264 | 7 | inferred_complete_timeline |
| `Action_BallCarry` | 265 | 330 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 382

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 355 | 141 | inferred_complete_timeline |
| `Action_None` | 364 | 389 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 323 | 109 | inferred_complete_timeline |
| `Action_None` | 326 | 333 | 8 | inferred_complete_timeline |
| `Action_None` | 336 | 389 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 217 | 218 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 309 | 92 | inferred_complete_timeline |
| `Action_None` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–372
- **Visible Samples:** 373

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 248 | 309 | 62 | inferred_complete_timeline |
| `Action_None` | 310 | 372 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–296
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 217 | 124 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 296 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–389
- **Visible Samples:** 362

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 7 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 217 | 207 | inferred_complete_timeline |
| `Action_DownBlock` | 218 | 272 | 55 | inferred_complete_timeline |
| `Action_DownBlock` | 274 | 309 | 36 | inferred_complete_timeline |
| `Action_None` | 310 | 315 | 6 | inferred_complete_timeline |
| `Action_None` | 318 | 327 | 10 | inferred_complete_timeline |
| `Action_None` | 347 | 353 | 7 | inferred_complete_timeline |
| `Action_None` | 355 | 389 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 371

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_BallSnap` | 215 | 229 | 15 | inferred_complete_timeline |
| `Action_None` | 230 | 247 | 18 | inferred_complete_timeline |
| `Action_None` | 253 | 257 | 5 | inferred_complete_timeline |
| `Action_None` | 260 | 261 | 2 | inferred_complete_timeline |
| `Action_None` | 272 | 344 | 73 | inferred_complete_timeline |
| `Action_None` | 347 | 389 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 247 | 248 | inferred_complete_timeline |
| `Action_PullBlock` | 248 | 292 | 45 | inferred_complete_timeline |
| `Action_PullBlock` | 296 | 309 | 14 | inferred_complete_timeline |
| `Action_None` | 310 | 389 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 354 | 140 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–273
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 253 | 39 | inferred_complete_timeline |
| `Action_None` | 271 | 273 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–285
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 254 | 40 | inferred_complete_timeline |
| `Action_None` | 258 | 285 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 243 | 29 | inferred_complete_timeline |
| `Action_None` | 271 | 272 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–361
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 239 | 25 | inferred_complete_timeline |
| `Action_None` | 241 | 242 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 307 | 64 | inferred_complete_timeline |
| `Action_None` | 309 | 321 | 13 | inferred_complete_timeline |
| `Action_None` | 326 | 361 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–280
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 280 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–387
- **Visible Samples:** 388

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 387 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 387

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 358 | 144 | inferred_complete_timeline |
| `Action_None` | 362 | 389 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 389 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 389 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 390

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 389 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–381
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 214 | 215 | inferred_complete_timeline |
| `Action_None` | 215 | 359 | 145 | inferred_complete_timeline |
| `Action_None` | 367 | 381 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 74–76 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 148–389 | 162 | 6 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 274–389 | 116 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 295–357 | 59 | 2 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 295–389 | 95 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 306–345 | 40 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 319–330 | 12 | 1 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 328–329 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 378–387 | 10 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 58 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (TE1) duration 92 frames exceeds threshold 90 frames [start=218, end=309].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '21' (LG) duration 92 frames exceeds threshold 90 frames [start=218, end=309].
- ⚠️ Action 'Action_None' range [215-253] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-273] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-243] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-372] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-355] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-253] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [265-330] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-387] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-280] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-296] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-307] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [309-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-361] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-306] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [308-377] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-254] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-285] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-323] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-333] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-389] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [248-292] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [296-309] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-359] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-381] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-358] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-354] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-309] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-247] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-344] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-7] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-217] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [218-272] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-315] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-327] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-353] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-389] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-76] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-240] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-296] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-389] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-389] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-306] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-357] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-389] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [306-345] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-330] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-387] for track '30' has 1 frames without a visible bounding box.
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