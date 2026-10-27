# Play-Annotation-Generator Annotation Review — Counter_383

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_383`
- **Frame Range:** 0 to 449 (450 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 449
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 116
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 84
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `25` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `15` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 213 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 253 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 211 | START | 211 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 214 | START | 227 | 231 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `17` | `16` | 214 | START | 214 | 241 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `25` | `23` | 214 | START | 224 | 230 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `22` | `21` | 214 | START | 214 | 255 |
| ✅ EXACT | `Action_PullLeadBlock` | WR2 | `3` | `2` | 214 | START | 214 | 272 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 226 | END | 211 | 226 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `13` | `12` | 240 | START | 240 | 245 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 254 | START | 254 | 297 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 296 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–332
- **Visible Samples:** 332

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_SnapReceive` | 211 | 226 | 16 | inferred_complete_timeline |
| `Action_None` | 227 | 239 | 13 | inferred_complete_timeline |
| `Action_Handoff` | 240 | 245 | 6 | inferred_complete_timeline |
| `Action_Handoff` | 247 | 253 | 7 | inferred_complete_timeline |
| `Action_None` | 254 | 332 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–297
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 253 | 254 | inferred_complete_timeline |
| `Action_BallCarry` | 254 | 297 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–449
- **Visible Samples:** 447

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 332 | 122 | inferred_complete_timeline |
| `Action_None` | 336 | 449 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 214 | 272 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–291
- **Visible Samples:** 284

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 242 | 32 | inferred_complete_timeline |
| `Action_None` | 247 | 280 | 34 | inferred_complete_timeline |
| `Action_None` | 285 | 291 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–429
- **Visible Samples:** 414

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PullBlock` | 214 | 255 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 263 | 264 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 266 | 274 | 9 | inferred_complete_timeline |
| `Action_PullBlock` | 283 | 296 | 14 | inferred_complete_timeline |
| `Action_None` | 297 | 429 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–242
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_BallSnap` | 211 | 226 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 227 | 231 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 241 | 242 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_DownBlock` | 214 | 241 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 256 | 277 | 22 | inferred_complete_timeline |
| `Action_DownBlock` | 282 | 285 | 4 | inferred_complete_timeline |
| `Action_None` | 304 | 356 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 46 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–370
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 243 | 33 | inferred_complete_timeline |
| `Action_None` | 245 | 322 | 78 | inferred_complete_timeline |
| `Action_None` | 327 | 329 | 3 | inferred_complete_timeline |
| `Action_None` | 334 | 355 | 22 | inferred_complete_timeline |
| `Action_None` | 361 | 370 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–367
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 241 | 31 | inferred_complete_timeline |
| `Action_None` | 270 | 281 | 12 | inferred_complete_timeline |
| `Action_None` | 318 | 341 | 24 | inferred_complete_timeline |
| `Action_None` | 360 | 367 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–374
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 237 | 27 | inferred_complete_timeline |
| `Action_None` | 257 | 271 | 15 | inferred_complete_timeline |
| `Action_None` | 297 | 374 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 264

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 242 | 32 | inferred_complete_timeline |
| `Action_None` | 246 | 266 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 284 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–245
- **Visible Samples:** 246

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 245 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 449 | 239 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 340 | 130 | inferred_complete_timeline |
| `Action_None` | 343 | 449 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 321 | 111 | inferred_complete_timeline |
| `Action_None` | 323 | 428 | 106 | inferred_complete_timeline |
| `Action_None` | 430 | 437 | 8 | inferred_complete_timeline |
| `Action_None` | 440 | 449 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–314
- **Visible Samples:** 315

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 314 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–449
- **Visible Samples:** 450

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |
| `Action_None` | 211 | 449 | 239 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–342 | 340 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 21–230 | 205 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 224–243 | 9 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 246–449 | 203 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 248–449 | 195 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 265–361 | 94 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 265–316 | 45 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 287–305 | 19 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 288–393 | 101 | 2 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 298–449 | 143 | 3 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 313–377 | 53 | 3 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 315–449 | 135 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 321–449 | 129 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 322–399 | 33 | 4 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 334–449 | 111 | 3 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 360–381 | 22 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 446–449 | 4 | 1 | Undefined position; Undefined team |
| `38` | `53` | Position_Unknown | Team_Unknown | 449–449 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `25` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `13` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 77 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 768: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [211–226], lower_priority='Action_DownBlock' annotated_start=214, effective_Action_DownBlock_start=227.
- ⚠️ Action 'Action_None' range [211-243] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-322] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-355] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-370] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-332] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [214-272] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-340] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-321] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-428] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-437] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-449] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [254-297] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-245] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-293] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-342] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-242] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-266] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-271] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-374] for track '10' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-314] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [240-245] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-332] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [227-231] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [241-242] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-242] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-280] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-291] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-241] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-281] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [318-341] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-367] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [214-241] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [256-277] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [282-285] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [304-356] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-284] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-46] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-449] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [214-255] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [263-264] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [266-274] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-429] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-230] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [224-230] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [242-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-317] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [319-449] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-250] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-257] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-321] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-346] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-361] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-274] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-309] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [312-316] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-305] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-344] for track '29' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [350-393] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-351] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-426] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-325] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-335] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-377] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [321-449] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-345] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-388] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-391] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-399] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-382] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [386-419] for track '35' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-449] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [360-381] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.

</details>