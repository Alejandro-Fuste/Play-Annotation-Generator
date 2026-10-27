# Play-Annotation-Generator Annotation Review — Counter_154

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_154`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 123
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DE2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB2 | defense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | defense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_Handoff` | LG | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | LB1 | defense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 293 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 134 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 18 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 51 | 54 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `21` | `Group` | 0 | START | 150 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `22` | `Group` | 0 | START | 177 | 184 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `7` | `Group` | 0 | START | 0 | 291 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 291 |
| ✅ EXACT | `Action_BallSnap` | DE2 | `13` | `12` | 292 | START | 292 | 293 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | WR1 | `1` | `0` | 294 | START | 294 | 346 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `13` | `12` | 294 | START | 294 | 311 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `14` | `13` | 294 | START | 294 | 318 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | CB2 | `4` | `3` | 294 | START | 294 | 315 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | DE1 | `6` | `5` | 294 | START | 294 | 332 |
| ✅ EXACT | `Action_SnapReceive` | LG | `22` | `21` | 306 | END | 292 | 306 |
| ✅ EXACT | `Action_Handoff` | LG | `22` | `21` | 317 | START | 317 | 335 |
| ✅ EXACT | `Action_BallCarry` | LB1 | `5` | `4` | 336 | START | 336 | 563 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 393 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 51–79
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 51 | 54 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 77 | 79 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–394
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |
| `Action_None` | 361 | 367 | 7 | inferred_complete_timeline |
| `Action_None` | 369 | 394 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 554

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |
| `Action_DownBlock` | 294 | 346 | 53 | inferred_complete_timeline |
| `Action_DownBlock` | 363 | 393 | 31 | inferred_complete_timeline |
| `Action_None` | 394 | 569 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–420
- **Visible Samples:** 356

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 342 | 51 | inferred_complete_timeline |
| `Action_None` | 344 | 353 | 10 | inferred_complete_timeline |
| `Action_None` | 418 | 420 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 150–564
- **Visible Samples:** 411

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 150 | 291 | 142 | inferred_complete_timeline |
| `Action_None` | 292 | 476 | 185 | inferred_complete_timeline |
| `Action_None` | 480 | 482 | 3 | inferred_complete_timeline |
| `Action_None` | 484 | 564 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–341
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 319 | 28 | inferred_complete_timeline |
| `Action_None` | 327 | 332 | 6 | inferred_complete_timeline |
| `Action_None` | 339 | 341 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 177–376
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 177 | 184 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 188 | 291 | 104 | inferred_complete_timeline |
| `Action_SnapReceive` | 292 | 306 | 15 | inferred_complete_timeline |
| `Action_None` | 307 | 316 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 317 | 335 | 19 | inferred_complete_timeline |
| `Action_None` | 336 | 376 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–219
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 134 | 135 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 150 | 180 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 185 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 198 | 219 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 18–44
- **Visible Samples:** 13

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 37 | 44 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–367
- **Visible Samples:** 352

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |
| `Action_DownBlock` | 294 | 318 | 25 | inferred_complete_timeline |
| `Action_DownBlock` | 321 | 336 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 347 | 353 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 358 | 367 | 10 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 561

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 294 | 332 | 39 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 342 | 393 | 52 | inferred_complete_timeline |
| `Action_None` | 394 | 569 | 176 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–556
- **Visible Samples:** 548

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 101 | 291 | 191 | inferred_complete_timeline |
| `Action_BallSnap` | 292 | 293 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 294 | 311 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 315 | 393 | 79 | inferred_complete_timeline |
| `Action_None` | 394 | 556 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–350
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 350 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 70–108
- **Visible Samples:** 39

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 70 | 108 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–563
- **Visible Samples:** 564

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 335 | 336 | inferred_complete_timeline |
| `Action_BallCarry` | 336 | 563 | 228 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 43 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 49 | 53 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 569 | 278 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–343
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 293 | 294 | inferred_complete_timeline |
| `Action_PullBlock` | 294 | 315 | 22 | inferred_complete_timeline |
| `Action_PullBlock` | 338 | 343 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 567

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 291 | 292 | inferred_complete_timeline |
| `Action_None` | 292 | 359 | 68 | inferred_complete_timeline |
| `Action_None` | 363 | 569 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–49
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 62–569
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 62 | 98 | 37 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 291 | 186 | inferred_complete_timeline |
| `Action_None` | 292 | 569 | 278 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 303–413 | 80 | 7 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 313–361 | 19 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 336–569 | 234 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 351–526 | 172 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 371–568 | 157 | 11 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 371–569 | 195 | 4 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 375–435 | 61 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 381–569 | 183 | 2 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 387–569 | 175 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 388–480 | 90 | 2 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 436–569 | 134 | 1 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 444–447 | 4 | 1 | Undefined position; Undefined team |
| `34` | `42` | Position_Unknown | Team_Unknown | 449–569 | 121 | 1 | Undefined position; Undefined team |
| `35` | `43` | Position_Unknown | Team_Unknown | 464–472 | 8 | 2 | Undefined position; Undefined team |
| `36` | `45` | Position_Unknown | Team_Unknown | 510–512 | 3 | 1 | Undefined position; Undefined team |
| `37` | `46` | Position_Unknown | Team_Unknown | 524–569 | 34 | 6 | Undefined position; Undefined team |
| `38` | `47` | Position_Unknown | Team_Unknown | 536–547 | 6 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (6 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '0' (WR1) duration 100 frames exceeds threshold 90 frames [start=294, end=393].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (DE2) duration 100 frames exceeds threshold 90 frames [start=294, end=393].
- ⚠️ Action 'Action_DownBlock' range [294-346] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [294-315] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [338-343] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [336-563] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [294-332] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-342] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [344-353] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [418-420] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-319] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-332] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [339-341] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-367] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [369-394] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-350] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-359] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [101-291] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [294-311] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-556] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [294-318] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [321-336] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [347-353] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [358-367] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-53] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-134] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-142] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-180] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-219] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-22] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [37-44] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-54] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-79] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-98] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-476] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [480-482] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-564] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-184] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-376] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-310] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-324] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [329-333] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-338] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [343-344] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-359] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [363-413] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-314] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-326] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-348] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [359-361] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [336-569] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-377] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-526] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-381] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [389-439] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [447-461] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-466] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-473] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-477] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [479-488] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-538] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-553] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-556] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-568] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-404] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-416] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [419-441] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-435] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-539] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-445] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-390] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [394-480] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [444-447] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [464-466] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-472] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-512] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-529] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [532-533] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-541] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [543-544] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [548-553] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [536-537] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [539-540] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [546-547] for track '38' has 1 frames without a visible bounding box.
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