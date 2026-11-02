# Play-Annotation-Generator Annotation Review — PinAndPull_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_9`
- **Frame Range:** 0 to 358 (359 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Tackle`
- **Result Frame:** 358
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | Team_Unknown | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `16` | `15` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `22` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 200 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 233 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 201 | START | 201 | 211 |
| ✅ EXACT | `Action_DownBlock` | Position_Unknown | `20` | `19` | 203 | START | 203 | 299 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | C | `21` | `20` | 203 | START | 212 | 265 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `15` | 211 | END | 201 | 211 |
| ✅ EXACT | `Action_Handoff` | QB | `16` | `15` | 222 | START | 222 | 233 |
| ✅ EXACT | `Action_BallCarry` | RB | `7` | `6` | 234 | START | 234 | 352 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 299 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–349
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_SnapReceive` | 201 | 211 | 11 | inferred_complete_timeline |
| `Action_None` | 212 | 221 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 222 | 233 | 12 | inferred_complete_timeline |
| `Action_None` | 234 | 349 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–352
- **Visible Samples:** 353

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 233 | 234 | inferred_complete_timeline |
| `Action_BallCarry` | 234 | 352 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–310
- **Visible Samples:** 309

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 200 | 40 | inferred_complete_timeline |
| `Action_None` | 201 | 310 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–330
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 325 | 125 | inferred_complete_timeline |
| `Action_None` | 327 | 330 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–312
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 312 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 327

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 297 | 97 | inferred_complete_timeline |
| `Action_None` | 303 | 326 | 24 | inferred_complete_timeline |
| `Action_None` | 347 | 348 | 2 | inferred_complete_timeline |
| `Action_None` | 356 | 358 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 343

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_BallSnap` | 201 | 211 | 11 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 212 | 265 | 54 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 277 | 278 | 2 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 280 | 299 | 20 | inferred_complete_timeline |
| `Action_None` | 300 | 307 | 8 | inferred_complete_timeline |
| `Action_None` | 311 | 324 | 14 | inferred_complete_timeline |
| `Action_None` | 326 | 358 | 33 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 351

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 221 | 21 | inferred_complete_timeline |
| `Action_None` | 224 | 288 | 65 | inferred_complete_timeline |
| `Action_None` | 291 | 340 | 50 | inferred_complete_timeline |
| `Action_None` | 345 | 358 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 323 | 123 | inferred_complete_timeline |
| `Action_None` | 325 | 358 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 359

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 358 | 158 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 259 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–324
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 264 | 64 | inferred_complete_timeline |
| `Action_None` | 266 | 283 | 18 | inferred_complete_timeline |
| `Action_None` | 286 | 324 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 358

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 291 | 91 | inferred_complete_timeline |
| `Action_None` | 293 | 358 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 350

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 255 | 55 | inferred_complete_timeline |
| `Action_None` | 262 | 314 | 53 | inferred_complete_timeline |
| `Action_None` | 318 | 358 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 249 | 49 | inferred_complete_timeline |
| `Action_None` | 252 | 278 | 27 | inferred_complete_timeline |
| `Action_None` | 290 | 291 | 2 | inferred_complete_timeline |
| `Action_None` | 293 | 299 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 323 | 123 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–323
- **Visible Samples:** 324

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 323 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–358
- **Visible Samples:** 338

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 286 | 86 | inferred_complete_timeline |
| `Action_None` | 295 | 308 | 14 | inferred_complete_timeline |
| `Action_None` | 322 | 358 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–354
- **Visible Samples:** 355

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 200 | 201 | inferred_complete_timeline |
| `Action_None` | 201 | 354 | 154 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–358 | 359 | 2 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–352 | 353 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 0–358 | 359 | 3 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 303–324 | 12 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 322–325 | 4 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 337–358 | 21 | 2 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 342–358 | 17 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `21` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 7 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 7 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 14 |
| Missing visible bounding boxes during action | 42 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 20: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ Track ID '26' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 97 frames exceeds threshold 90 frames [start=203, end=299].
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [201–211], lower_priority='Action_PullLeadBlock' annotated_start=203, effective_Action_PullLeadBlock_start=212.
- ⚠️ Action 'Action_None' range [201-325] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-330] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-249] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-278] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-299] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-323] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-312] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-323] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-329] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-310] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [234-352] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-264] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [266-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-324] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-221] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-288] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-340] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-259] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-352] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-255] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-314] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-286] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-308] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-349] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-291] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-354] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-297] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-326] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [347-348] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [212-265] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [277-278] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-307] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [311-324] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [326-358] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-323] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [325-358] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [303-312] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-324] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [322-325] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [337-339] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>