# Play-Annotation-Generator Annotation Review — Counter_105

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_105`
- **Frame Range:** 0 to 509 (510 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 509
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 128
- **Validation Warnings:** 127
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 100
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `16` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `18` | `17` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `15` | `14` |
| ✅ EXACT | `Action_PullLeadBlock` | WR4 | offense | `5` | `4` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `2` | `1` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 9 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 9 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 9 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 9 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 9 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 9 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 9 | 242 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 9 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 9 | 234 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 9 | 236 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 9 | 234 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `16` | 235 | START | 235 | 248 |
| ✅ EXACT | `Action_DownBlock` | LT | `13` | `12` | 237 | START | 237 | 274 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `17` | `16` | 237 | START | 249 | 255 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `18` | `17` | 237 | START | 237 | 257 |
| ✅ EXACT | `Action_PullBlock` | RG | `15` | `14` | 237 | START | 237 | 377 |
| ✅ EXACT | `Action_PullLeadBlock` | WR4 | `5` | `4` | 237 | START | 237 | 377 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `2` | `1` | 243 | START | 243 | 281 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 248 | END | 235 | 248 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `7` | 259 | START | 259 | 281 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `2` | `1` | 282 | START | 282 | 315 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 377 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 9–437
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_SnapReceive` | 235 | 248 | 14 | inferred_complete_timeline |
| `Action_None` | 249 | 258 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 259 | 281 | 23 | inferred_complete_timeline |
| `Action_None` | 282 | 437 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 9–509
- **Visible Samples:** 495

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 242 | 234 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 243 | 281 | 39 | inferred_complete_timeline |
| `Action_BallCarry` | 282 | 315 | 34 | inferred_complete_timeline |
| `Action_BallCarry` | 319 | 320 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 324 | 509 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 9–404
- **Visible Samples:** 385

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 391 | 157 | inferred_complete_timeline |
| `Action_None` | 403 | 404 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 9–507
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 507 | 273 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 9–509
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 509 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 9–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 236 | 228 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 237 | 377 | 141 | inferred_complete_timeline |
| `Action_None` | 378 | 501 | 124 | inferred_complete_timeline |
| `Action_None` | 503 | 509 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 9–274
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 236 | 228 | inferred_complete_timeline |
| `Action_DownBlock` | 237 | 274 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 9–277
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 12 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 16 | 17 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 67 | 236 | 170 | inferred_complete_timeline |
| `Action_DownBlock` | 237 | 257 | 21 | inferred_complete_timeline |
| `Action_DownBlock` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 276 | 277 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 9–509
- **Visible Samples:** 491

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_BallSnap` | 235 | 248 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 249 | 255 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 258 | 264 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 272 | 319 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 321 | 377 | 57 | inferred_complete_timeline |
| `Action_None` | 378 | 509 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 9–462
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 236 | 228 | inferred_complete_timeline |
| `Action_PullBlock` | 237 | 377 | 141 | inferred_complete_timeline |
| `Action_None` | 378 | 382 | 5 | inferred_complete_timeline |
| `Action_None` | 386 | 438 | 53 | inferred_complete_timeline |
| `Action_None` | 440 | 462 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 9–305
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 305 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 489

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 290 | 56 | inferred_complete_timeline |
| `Action_None` | 303 | 509 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 9–493
- **Visible Samples:** 471

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 274 | 40 | inferred_complete_timeline |
| `Action_None` | 282 | 471 | 190 | inferred_complete_timeline |
| `Action_None` | 474 | 482 | 9 | inferred_complete_timeline |
| `Action_None` | 488 | 493 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 11–293
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 32 | 22 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 63 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 234 | 169 | inferred_complete_timeline |
| `Action_None` | 235 | 293 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 9–321
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 321 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 500

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 358 | 124 | inferred_complete_timeline |
| `Action_None` | 360 | 509 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 9–285
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 270 | 36 | inferred_complete_timeline |
| `Action_None` | 275 | 280 | 6 | inferred_complete_timeline |
| `Action_None` | 284 | 285 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 509 | 275 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 492

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 402 | 168 | inferred_complete_timeline |
| `Action_None` | 411 | 507 | 97 | inferred_complete_timeline |
| `Action_None` | 509 | 509 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 9–494
- **Visible Samples:** 477

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 316 | 82 | inferred_complete_timeline |
| `Action_None` | 318 | 320 | 3 | inferred_complete_timeline |
| `Action_None` | 322 | 325 | 4 | inferred_complete_timeline |
| `Action_None` | 331 | 335 | 5 | inferred_complete_timeline |
| `Action_None` | 337 | 491 | 155 | inferred_complete_timeline |
| `Action_None` | 493 | 494 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 9–509
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 490 | 256 | inferred_complete_timeline |
| `Action_None` | 493 | 504 | 12 | inferred_complete_timeline |
| `Action_None` | 506 | 509 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 9–507
- **Visible Samples:** 499

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 9 | 234 | 226 | inferred_complete_timeline |
| `Action_None` | 235 | 507 | 273 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 107–200 | 20 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 247–509 | 233 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 278–506 | 197 | 7 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 283–343 | 54 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 289–503 | 195 | 2 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 290–318 | 12 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 305–509 | 186 | 6 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 351–509 | 155 | 4 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 374–392 | 18 | 2 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 382–509 | 121 | 3 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 385–509 | 124 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 429–430 | 2 | 1 | Undefined position; Undefined team |
| `35` | `54` | Position_Unknown | Team_Unknown | 450–470 | 9 | 2 | Undefined position; Undefined team |
| `36` | `56` | Position_Unknown | Team_Unknown | 461–482 | 11 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (7 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 93 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '14' (RG) duration 141 frames exceeds threshold 90 frames [start=237, end=377].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 141 frames exceeds threshold 90 frames [start=237, end=377].
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [235–248], lower_priority='Action_DownBlock' annotated_start=237, effective_Action_DownBlock_start=249.
- ⚠️ Action 'Action_None' range [235-507] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [282-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [319-320] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [324-509] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-391] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-404] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-501] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-509] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-402] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [411-507] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [259-281] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-437] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-490] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-504] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-509] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-507] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-316] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-320] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-335] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-491] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-494] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-321] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [237-274] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-358] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-509] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-382] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-438] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-462] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-270] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-285] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [235-248] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [249-255] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [258-264] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [272-319] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [67-236] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [237-257] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [259-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [276-277] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-305] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-274] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-471] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [474-482] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-493] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-290] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-509] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-32] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-63] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-293] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-124] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-200] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-248] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-273] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-501] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-274] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-313] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-341] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-484] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-490] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [500-506] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-291] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-343] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [289-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-503] for track '27' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-292] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [310-313] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [305-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-320] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-344] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-474] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-495] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [498-509] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-362] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-484] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-501] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-376] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [378-392] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-383] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-467] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [385-465] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [429-430] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-454] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [467-470] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [461-467] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-478] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [481-482] for track '36' has 1 frames without a visible bounding box.
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