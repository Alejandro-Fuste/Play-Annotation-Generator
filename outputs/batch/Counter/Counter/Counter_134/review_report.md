# Play-Annotation-Generator Annotation Review — Counter_134

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_134`
- **Frame Range:** 0 to 463 (464 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 463
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DE1 | defense | `11` | `10` |
| ✅ EXACT | `Action_PullLeadBlock` | TE | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 107 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 199 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 203 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 199 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 200 | START | 200 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `10` | `9` | 204 | START | 213 | 254 |
| ✅ EXACT | `Action_DownBlock` | LT | `5` | `4` | 204 | START | 204 | 290 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | DE1 | `11` | `10` | 204 | START | 204 | 253 |
| ✅ EXACT | `Action_PullLeadBlock` | TE | `7` | `6` | 204 | START | 204 | 218 |
| ✅ EXACT | `Action_SnapReceive` | RB | `3` | `2` | 212 | END | 200 | 212 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `3` | `2` | 223 | START | 223 | 366 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 290 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 311

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 310 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–376
- **Visible Samples:** 369

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_SnapReceive` | 200 | 212 | 13 | inferred_complete_timeline |
| `Action_None` | 213 | 222 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 223 | 366 | 144 | inferred_complete_timeline |
| `Action_BallCarry` | 375 | 376 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 204 | 218 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–391
- **Visible Samples:** 392

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_DownBlock` | 204 | 290 | 87 | inferred_complete_timeline |
| `Action_None` | 291 | 391 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–268
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 237 | 38 | inferred_complete_timeline |
| `Action_None` | 266 | 268 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–368
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 115 | 199 | 85 | inferred_complete_timeline |
| `Action_BallSnap` | 200 | 212 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 213 | 254 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 259 | 266 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 268 | 290 | 23 | inferred_complete_timeline |
| `Action_None` | 291 | 368 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–313
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 313 | 114 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–463
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 203 | 204 | inferred_complete_timeline |
| `Action_PullBlock` | 204 | 253 | 50 | inferred_complete_timeline |
| `Action_PullBlock` | 260 | 290 | 31 | inferred_complete_timeline |
| `Action_None` | 291 | 463 | 173 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 259 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 108 | 94 | inferred_complete_timeline |
| `Action_PreSnap` | 110 | 115 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 128 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 140 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 143 | 149 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 199 | 46 | inferred_complete_timeline |
| `Action_None` | 200 | 202 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–463
- **Visible Samples:** 436

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 199 | 77 | inferred_complete_timeline |
| `Action_None` | 200 | 209 | 10 | inferred_complete_timeline |
| `Action_None` | 212 | 233 | 22 | inferred_complete_timeline |
| `Action_None` | 235 | 259 | 25 | inferred_complete_timeline |
| `Action_None` | 265 | 463 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–315
- **Visible Samples:** 314

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 290 | 91 | inferred_complete_timeline |
| `Action_None` | 292 | 295 | 4 | inferred_complete_timeline |
| `Action_None` | 297 | 315 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–463
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 263 | 64 | inferred_complete_timeline |
| `Action_None` | 266 | 349 | 84 | inferred_complete_timeline |
| `Action_None` | 355 | 366 | 12 | inferred_complete_timeline |
| `Action_None` | 368 | 377 | 10 | inferred_complete_timeline |
| `Action_None` | 379 | 387 | 9 | inferred_complete_timeline |
| `Action_None` | 400 | 407 | 8 | inferred_complete_timeline |
| `Action_None` | 409 | 410 | 2 | inferred_complete_timeline |
| `Action_None` | 445 | 447 | 3 | inferred_complete_timeline |
| `Action_None` | 460 | 463 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–272
- **Visible Samples:** 273

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 199 | 200 | inferred_complete_timeline |
| `Action_None` | 200 | 272 | 73 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–463 | 458 | 4 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 16–17 | 2 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 104–275 | 15 | 7 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 200–264 | 59 | 4 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 225–463 | 208 | 3 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 231–463 | 137 | 3 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 236–351 | 115 | 2 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 251–463 | 213 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 277–463 | 187 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 281–310 | 30 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 290–463 | 159 | 3 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 298–430 | 102 | 2 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 298–463 | 128 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 299–349 | 51 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 334–372 | 28 | 2 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 358–463 | 106 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 374–463 | 85 | 3 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 421–463 | 34 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 427–463 | 35 | 2 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 448–463 | 16 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 452–463 | 12 | 1 | Undefined position; Undefined team |
| `35` | `46` | Position_Unknown | Team_Unknown | 453–463 | 11 | 1 | Undefined position; Undefined team |
| `36` | `47` | Position_Unknown | Team_Unknown | 453–463 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 270: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 463 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [200–212], lower_priority='Action_DownBlock' annotated_start=204, effective_Action_DownBlock_start=213.
- ⚠️ Action 'Action_None' range [200-258] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-455] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-463] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-290] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-295] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-315] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [223-366] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [375-376] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-310] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-391] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-259] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [204-218] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-263] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-349] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [355-366] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [368-377] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-387] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [400-407] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [409-410] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-447] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-237] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-268] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [213-254] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [259-266] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-368] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [204-253] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [260-290] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-102] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-233] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-259] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-313] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-108] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-115] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-140] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-149] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 200, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [200-202] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-272] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-17] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-108] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-118] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-199] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-246] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-253] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-260] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-264] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-319] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-463] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-346] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-340] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [342-351] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-463] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-310] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-334] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-395] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [397-463] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-351] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [383-430] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-305] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [299-349] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-350] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [362-372] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [374-385] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-398] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-425] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [431-445] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [427-432] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>