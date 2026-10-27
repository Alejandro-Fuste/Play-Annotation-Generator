# Play-Annotation-Generator Annotation Review — Counter_174

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_174`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 46
- **Ball Tracks:** 0
- **Action Segments:** 105
- **Validation Warnings:** 131
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | WR1 | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR2 | offense | `1` | `0` |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | Team_Unknown | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | CB1 | defense | `17` | `16` |
| ✅ EXACT | `Action_PlaySideFakeStep` | SAF1 | defense | `8` | `7` |
| ✅ EXACT | `Action_Handoff` | CB1 | defense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF1 | defense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 100 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `16` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 36 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 58 | 229 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 213 | 225 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 32 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `22` | `21` | 226 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `20` | `19` | 230 | START | 230 | 261 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `22` | `21` | 230 | START | 230 | 245 |
| ✅ EXACT | `Action_DownBlock` | WR1 | `6` | `5` | 230 | START | 230 | 322 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | WR2 | `1` | `0` | 230 | START | 230 | 243 |
| ✅ EXACT | `Action_PullLeadBlock` | Position_Unknown | `4` | `3` | 230 | START | 230 | 322 |
| ✅ EXACT | `Action_SnapReceive` | CB1 | `17` | `16` | 231 | END | 226 | 231 |
| ✅ EXACT | `Action_PlaySideFakeStep` | SAF1 | `8` | `7` | 235 | START | 235 | 279 |
| ✅ EXACT | `Action_Handoff` | CB1 | `17` | `16` | 264 | START | 264 | 279 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | SAF1 | `8` | `7` | 280 | START | 280 | 424 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 322 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 100 | 101 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 225 | 121 | inferred_complete_timeline |
| `Action_None` | 226 | 255 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–357
- **Visible Samples:** 348

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 43 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 229 | 183 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 322 | 93 | inferred_complete_timeline |
| `Action_None` | 323 | 335 | 13 | inferred_complete_timeline |
| `Action_None` | 338 | 357 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–375
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 72 | 229 | 158 | inferred_complete_timeline |
| `Action_PullBlock` | 230 | 243 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 248 | 305 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 307 | 322 | 16 | inferred_complete_timeline |
| `Action_None` | 323 | 375 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–539
- **Visible Samples:** 540

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 539 | 314 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 213–230
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 213 | 225 | 13 | inferred_complete_timeline |
| `Action_None` | 226 | 230 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 58–395
- **Visible Samples:** 334

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 58 | 229 | 172 | inferred_complete_timeline |
| `Action_DownBlock` | 230 | 261 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 264 | 275 | 12 | inferred_complete_timeline |
| `Action_DownBlock` | 278 | 322 | 45 | inferred_complete_timeline |
| `Action_None` | 323 | 395 | 73 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 36–338
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 36 | 225 | 190 | inferred_complete_timeline |
| `Action_None` | 226 | 338 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–287
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 287 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 250 | 25 | inferred_complete_timeline |
| `Action_None` | 258 | 260 | 3 | inferred_complete_timeline |
| `Action_None` | 262 | 280 | 19 | inferred_complete_timeline |
| `Action_None` | 282 | 298 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–351
- **Visible Samples:** 349

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |
| `Action_None` | 243 | 351 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 532

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 503 | 278 | inferred_complete_timeline |
| `Action_None` | 512 | 539 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–334
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_PreSnap` | 48 | 67 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 99 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 102 | 225 | 124 | inferred_complete_timeline |
| `Action_None` | 226 | 242 | 17 | inferred_complete_timeline |
| `Action_None` | 245 | 327 | 83 | inferred_complete_timeline |
| `Action_None` | 333 | 334 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 119 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 293 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–539
- **Visible Samples:** 539

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 59 | 225 | 167 | inferred_complete_timeline |
| `Action_SnapReceive` | 226 | 231 | 6 | inferred_complete_timeline |
| `Action_None` | 232 | 263 | 32 | inferred_complete_timeline |
| `Action_Handoff` | 264 | 279 | 16 | inferred_complete_timeline |
| `Action_None` | 280 | 539 | 260 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–348
- **Visible Samples:** 340

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 86 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 225 | 137 | inferred_complete_timeline |
| `Action_None` | 226 | 260 | 35 | inferred_complete_timeline |
| `Action_None` | 264 | 348 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–21
- **Visible Samples:** 22

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–514
- **Visible Samples:** 512

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 234 | 235 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 235 | 279 | 45 | inferred_complete_timeline |
| `Action_BallCarry` | 280 | 424 | 145 | inferred_complete_timeline |
| `Action_BallCarry` | 428 | 514 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–366
- **Visible Samples:** 367

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 225 | 226 | inferred_complete_timeline |
| `Action_None` | 226 | 366 | 141 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `3` | `4` | Position_Unknown | Team_Unknown | 0–350 | 351 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 230–279 | 46 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 234–270 | 37 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 288–354 | 63 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 294–310 | 17 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 322–393 | 72 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 323–387 | 58 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 327–346 | 20 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 331–415 | 85 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 337–421 | 85 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 345–358 | 14 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 351–392 | 41 | 2 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 362–539 | 178 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 392–426 | 35 | 1 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 403–466 | 64 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 410–539 | 130 | 1 | Undefined position; Undefined team |
| `36` | `43` | Position_Unknown | Team_Unknown | 427–428 | 2 | 1 | Undefined position; Undefined team |
| `37` | `44` | Position_Unknown | Team_Unknown | 432–517 | 85 | 2 | Undefined position; Undefined team |
| `38` | `45` | Position_Unknown | Team_Unknown | 443–539 | 94 | 3 | Undefined position; Undefined team |
| `39` | `46` | Position_Unknown | Team_Unknown | 459–539 | 80 | 2 | Undefined position; Undefined team |
| `40` | `48` | Position_Unknown | Team_Unknown | 472–539 | 68 | 1 | Undefined position; Undefined team |
| `41` | `49` | Position_Unknown | Team_Unknown | 484–539 | 54 | 2 | Undefined position; Undefined team |
| `42` | `50` | Position_Unknown | Team_Unknown | 487–539 | 53 | 1 | Undefined position; Undefined team |
| `43` | `51` | Position_Unknown | Team_Unknown | 494–539 | 46 | 1 | Undefined position; Undefined team |
| `44` | `52` | Position_Unknown | Team_Unknown | 494–518 | 25 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 527–539 | 13 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `1` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 26 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 26 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 52 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (WR2) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '5' (WR1) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (LG) duration 93 frames exceeds threshold 90 frames [start=230, end=322].
- ⚠️ Action 'Action_PreSnap' range [0-69] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [230-243] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [248-305] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-375] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-44] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-67] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-99] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-242] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-327] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-334] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-350] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-260] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-348] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-32] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-43] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-229] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-335] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [338-357] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-293] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [280-424] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [428-514] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-366] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-503] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-539] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-239] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-351] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-250] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-280] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [282-298] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-100] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-255] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-225] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-263] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-287] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-338] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-261] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [264-275] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [278-322] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-395] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-225] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-230] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [230-245] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [250-279] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-270] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-294] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-354] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-310] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-393] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-329] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-387] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-346] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [331-415] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-421] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [345-358] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-389] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [391-392] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-539] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [392-426] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [403-466] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-428] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-512] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [514-517] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [443-444] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [446-474] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-500] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-499] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-518] for track '44' has 2 frames without a visible bounding box.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.

</details>