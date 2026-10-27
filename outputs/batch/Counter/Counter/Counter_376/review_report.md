# Play-Annotation-Generator Annotation Review — Counter_376

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_376`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `6` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `1` | `0` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `6` | `5` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 402 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 153 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 88 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 201 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 402 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 399 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `6` | `Group` | 0 | START | 0 | 172 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `11` | `10` | 400 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `1` | `0` | 403 | START | 403 | 429 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | C | `11` | `10` | 403 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `17` | `16` | 403 | START | 403 | 414 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `14` | `13` | 403 | START | 403 | 430 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `4` | `3` | 403 | START | 403 | 452 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 415 | END | 400 | 415 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `10` | `9` | 423 | START | 423 | 434 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `6` | `5` | 446 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 491 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–441
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 153 | 154 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 241 | 85 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 399 | 154 | inferred_complete_timeline |
| `Action_SnapReceive` | 400 | 415 | 16 | inferred_complete_timeline |
| `Action_None` | 416 | 422 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 423 | 434 | 12 | inferred_complete_timeline |
| `Action_Handoff` | 438 | 441 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–172
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 594

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 402 | 403 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 403 | 452 | 50 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 457 | 469 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 472 | 491 | 20 | inferred_complete_timeline |
| `Action_None` | 492 | 599 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–434
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 428 | 29 | inferred_complete_timeline |
| `Action_None` | 432 | 434 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 88 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 201 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–432
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 402 | 403 | inferred_complete_timeline |
| `Action_DownBlock` | 403 | 429 | 27 | inferred_complete_timeline |
| `Action_DownBlock` | 431 | 432 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–445
- **Visible Samples:** 446

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 445 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–514
- **Visible Samples:** 431

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 93 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 126 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 138 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 141 | 248 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 252 | 255 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 262 | 399 | 138 | inferred_complete_timeline |
| `Action_None` | 400 | 406 | 7 | inferred_complete_timeline |
| `Action_None` | 451 | 452 | 2 | inferred_complete_timeline |
| `Action_None` | 454 | 514 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–284
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 266 | 170 | inferred_complete_timeline |
| `Action_PreSnap` | 281 | 284 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 589

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 497 | 98 | inferred_complete_timeline |
| `Action_None` | 509 | 599 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–265
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 259 | 260 | inferred_complete_timeline |
| `Action_PreSnap` | 261 | 265 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 596

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 399 | 400 | inferred_complete_timeline |
| `Action_None` | 400 | 539 | 140 | inferred_complete_timeline |
| `Action_None` | 544 | 599 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `14` | Position_Unknown | Team_Unknown | 101–576 | 442 | 8 | Undefined position; Undefined team |
| `14` | `15` | Position_Unknown | Team_Unknown | 182–580 | 398 | 3 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 206–414 | 209 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 216–528 | 302 | 7 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 244–303 | 57 | 2 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 312–423 | 112 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 349–599 | 141 | 7 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 408–493 | 86 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 422–501 | 75 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 430–494 | 65 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 441–442 | 2 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 485–599 | 110 | 3 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 490–599 | 107 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 506–576 | 63 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 510–586 | 75 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 522–558 | 31 | 2 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 531–599 | 66 | 3 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 531–599 | 69 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 538–599 | 62 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 545–553 | 9 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 552–556 | 5 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 556–599 | 44 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 569–587 | 19 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `1` (2 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `11` (C)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `4` (3 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `6` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 78 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=446, end=172. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '10' has invalid range: start=400, end=88. Clamping end to start.
- ⚠️ Segment 'Action_DownBlock' for track '10' has invalid range: start=403, end=88. Clamping end to start.
- ⚠️ Action 'Action_DownBlock' range [403-429] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [431-432] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-539] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [544-599] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-201] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [403-452] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [457-469] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-428] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-434] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-497] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-259] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [261-265] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-266] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-153] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-241] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [423-434] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [438-441] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-126] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-138] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-248] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-406] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-452] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-514] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-399] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-445] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [403-430] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [442-474] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [492-531] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [533-540] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [553-561] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-576] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-437] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-580] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-414] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [403-414] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [416-419] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [421-427] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [430-445] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [448-487] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-528] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [244-297] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-303] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-423] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [349-354] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [370-371] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [373-376] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [379-397] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-486] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-499] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [408-493] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [422-429] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-501] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [430-494] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-442] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-513] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-569] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-499] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-571] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-543] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-572] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [575-576] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [510-519] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-586] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-548] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [555-558] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-554] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [538-599] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-553] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [552-556] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [569-587] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
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

</details>