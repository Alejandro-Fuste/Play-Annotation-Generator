# Play-Annotation-Generator Annotation Review — OutsideZoneStretch_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneStretch_107`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_OutsideZoneStretch`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 78
- **Validation Warnings:** 100
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 13
- **Exact Matches:** 5
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ EXACT | `Action_PressEdge` | RB | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `1` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `10` | `10` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 380 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 160 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 370 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 312 |
| ✅ EXACT | `Action_PressEdge` | RB | `4` | `4` | 313 | START | 313 | 423 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 371 | START | 371 | 440 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `1` | `1` | 371 | START | 371 | 440 |
| ✅ EXACT | `Action_ZoneBlock` | C | `12` | `12` | 371 | START | 371 | 440 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `3` | `3` | 371 | START | 371 | 392 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `10` | `10` | 381 | START | 381 | 565 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–595
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 380 | 381 | inferred_complete_timeline |
| `Action_Handoff` | 381 | 565 | 185 | inferred_complete_timeline |
| `Action_Handoff` | 569 | 595 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–592
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 312 | 313 | inferred_complete_timeline |
| `Action_PressEdge` | 313 | 423 | 111 | inferred_complete_timeline |
| `Action_None` | 424 | 474 | 51 | inferred_complete_timeline |
| `Action_None` | 477 | 592 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–520
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 440 | 70 | inferred_complete_timeline |
| `Action_None` | 441 | 520 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–392
- **Visible Samples:** 393

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 392 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–508
- **Visible Samples:** 476

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 160 | 161 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 201 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 246 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 248 | 251 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 260 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 266 | 270 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 274 | 370 | 97 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 440 | 70 | inferred_complete_timeline |
| `Action_None` | 441 | 448 | 8 | inferred_complete_timeline |
| `Action_None` | 450 | 470 | 21 | inferred_complete_timeline |
| `Action_None` | 473 | 508 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–456
- **Visible Samples:** 457

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 370 | 371 | inferred_complete_timeline |
| `Action_ZoneBlock` | 371 | 440 | 70 | inferred_complete_timeline |
| `Action_None` | 441 | 456 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–533
- **Visible Samples:** 526

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 491 | 492 | inferred_complete_timeline |
| `Action_PreSnap` | 500 | 533 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–469
- **Visible Samples:** 470

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 469 | 470 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–487
- **Visible Samples:** 488

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 487 | 488 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–483
- **Visible Samples:** 479

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 272 | 273 | inferred_complete_timeline |
| `Action_PreSnap` | 276 | 478 | 203 | inferred_complete_timeline |
| `Action_PreSnap` | 481 | 483 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–482
- **Visible Samples:** 448

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 181 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 266 | 84 | inferred_complete_timeline |
| `Action_PreSnap` | 288 | 316 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 318 | 319 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 329 | 475 | 147 | inferred_complete_timeline |
| `Action_PreSnap` | 477 | 482 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–428
- **Visible Samples:** 429

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 428 | 429 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–395
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 141 | 142 | inferred_complete_timeline |
| `Action_PreSnap` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 154 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 283 | 117 | inferred_complete_timeline |
| `Action_PreSnap` | 287 | 322 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 326 | 395 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–454 | 455 | 1 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–470 | 471 | 1 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 402–434 | 4 | 2 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 411–576 | 165 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 415–599 | 185 | 1 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 420–437 | 16 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 424–599 | 176 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 427–431 | 4 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 428–449 | 21 | 2 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 448–552 | 97 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 463–598 | 134 | 2 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 474–497 | 24 | 1 | Undefined position; Undefined team |
| `25` | `36` | Position_Unknown | Team_Unknown | 479–599 | 121 | 1 | Undefined position; Undefined team |
| `26` | `38` | Position_Unknown | Team_Unknown | 482–501 | 10 | 2 | Undefined position; Undefined team |
| `27` | `39` | Position_Unknown | Team_Unknown | 484–599 | 109 | 5 | Undefined position; Undefined team |
| `28` | `40` | Position_Unknown | Team_Unknown | 536–599 | 64 | 1 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 572–599 | 28 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 586–599 | 14 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_Handoff` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 62 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 216: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [441-456] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-520] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-491] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-533] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [371-392] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [424-474] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-592] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-181] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-266] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [288-316] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [318-319] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [329-475] for track '5' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [477-482] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-469] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-454] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-470] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-272] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [276-478] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [481-483] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [381-565] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [569-595] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-487] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-160] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-201] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-246] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-251] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [259-260] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [266-270] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [441-448] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-470] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [473-508] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-428] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-141] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-151] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-154] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-283] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [287-322] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [326-395] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [402-403] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [433-434] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-526] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [528-576] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [420-431] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-437] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [427-428] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [430-431] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [428-432] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [434-449] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [448-468] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [476-477] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-552] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [463-544] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [547-598] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [474-497] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [479-599] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [482-489] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [500-501] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [484-505] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [507-511] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [515-517] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [519-560] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
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

</details>