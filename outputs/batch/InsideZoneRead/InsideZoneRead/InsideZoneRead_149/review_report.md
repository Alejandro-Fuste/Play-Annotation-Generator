# Play-Annotation-Generator Annotation Review — InsideZoneRead_149

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_149`
- **Frame Range:** 0 to 539 (540 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 539
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 128
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `11` | `10` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `7` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `11` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 315 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 315 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `12` | `11` | 316 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `1` | `0` | 318 | START | 318 | 383 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `11` | `10` | 318 | START | 318 | 340 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `12` | `11` | 318 | START | N/A | N/A |
| ✅ EXACT | `Action_ZoneBlock` | RT | `2` | `1` | 318 | START | 318 | 356 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 318 | START | 318 | 383 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `7` | 325 | END | 316 | 325 |
| ✅ EXACT | `Action_ReadDefender` | QB | `8` | `7` | 330 | START | 330 | 359 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `8` | `7` | 360 | START | 360 | 434 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 383 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–488
- **Visible Samples:** 463

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_SnapReceive` | 316 | 325 | 10 | inferred_complete_timeline |
| `Action_None` | 326 | 329 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 330 | 359 | 30 | inferred_complete_timeline |
| `Action_BallCarry` | 360 | 434 | 75 | inferred_complete_timeline |
| `Action_BallCarry` | 461 | 488 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–365
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 348 | 33 | inferred_complete_timeline |
| `Action_None` | 352 | 354 | 3 | inferred_complete_timeline |
| `Action_None` | 361 | 365 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–395
- **Visible Samples:** 396

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 383 | 66 | inferred_complete_timeline |
| `Action_None` | 384 | 395 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–490
- **Visible Samples:** 458

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 383 | 66 | inferred_complete_timeline |
| `Action_None` | 384 | 384 | 1 | inferred_complete_timeline |
| `Action_None` | 387 | 457 | 71 | inferred_complete_timeline |
| `Action_None` | 489 | 490 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–133
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 106 | 133 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–509
- **Visible Samples:** 478

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 234 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 242 | 317 | 76 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 340 | 23 | inferred_complete_timeline |
| `Action_ZoneBlock` | 358 | 362 | 5 | inferred_complete_timeline |
| `Action_ZoneBlock` | 365 | 383 | 19 | inferred_complete_timeline |
| `Action_None` | 384 | 509 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–356
- **Visible Samples:** 357

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 317 | 318 | inferred_complete_timeline |
| `Action_ZoneBlock` | 318 | 356 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–414
- **Visible Samples:** 415

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 414 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–508
- **Visible Samples:** 467

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 362 | 47 | inferred_complete_timeline |
| `Action_None` | 388 | 401 | 14 | inferred_complete_timeline |
| `Action_None` | 405 | 452 | 48 | inferred_complete_timeline |
| `Action_None` | 454 | 482 | 29 | inferred_complete_timeline |
| `Action_None` | 488 | 489 | 2 | inferred_complete_timeline |
| `Action_None` | 493 | 495 | 3 | inferred_complete_timeline |
| `Action_None` | 501 | 508 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–378
- **Visible Samples:** 329

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 324 | 9 | inferred_complete_timeline |
| `Action_None` | 375 | 378 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–385
- **Visible Samples:** 386

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 385 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–335
- **Visible Samples:** 335

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 315 | 316 | inferred_complete_timeline |
| `Action_None` | 316 | 332 | 17 | inferred_complete_timeline |
| `Action_None` | 334 | 335 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `14` | Position_Unknown | Team_Unknown | 49–61 | 10 | 2 | Undefined position; Undefined team |
| `13` | `15` | Position_Unknown | Team_Unknown | 226–482 | 231 | 4 | Undefined position; Undefined team |
| `14` | `18` | Position_Unknown | Team_Unknown | 341–449 | 100 | 2 | Undefined position; Undefined team |
| `15` | `20` | Position_Unknown | Team_Unknown | 349–494 | 139 | 2 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 357–511 | 155 | 1 | Undefined position; Undefined team |
| `17` | `22` | Position_Unknown | Team_Unknown | 358–402 | 9 | 2 | Undefined position; Undefined team |
| `18` | `23` | Position_Unknown | Team_Unknown | 367–369 | 3 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 371–457 | 68 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 375–539 | 128 | 4 | Undefined position; Undefined team |
| `21` | `28` | Position_Unknown | Team_Unknown | 402–403 | 2 | 1 | Undefined position; Undefined team |
| `22` | `29` | Position_Unknown | Team_Unknown | 403–539 | 137 | 1 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 406–411 | 6 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 407–409 | 3 | 1 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 414–430 | 17 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 423–528 | 74 | 3 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 428–539 | 112 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 429–539 | 111 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 460–497 | 38 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 462–463 | 2 | 1 | Undefined position; Undefined team |
| `31` | `43` | Position_Unknown | Team_Unknown | 469–529 | 59 | 2 | Undefined position; Undefined team |
| `32` | `44` | Position_Unknown | Team_Unknown | 469–539 | 71 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 470–539 | 64 | 6 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 483–534 | 36 | 5 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 494–500 | 7 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 528–539 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `1` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (3 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `12` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 25 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 25 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 50 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 539 as fallback play end.
- ⚠️ Segment 'Action_BallSnap' for track '11' has invalid range: start=316, end=133. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '11' has invalid range: start=318, end=133. Clamping end to start.
- ⚠️ Action 'Action_None' range [384-395] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [318-356] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-362] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [388-401] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [405-452] for track '2' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-482] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [488-489] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-495] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [501-508] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-348] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [352-354] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [361-365] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-385] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-414] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '6' starts at frame 384, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [384-384] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [387-457] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-490] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-315] for track '7' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [360-434] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [461-488] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-324] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-378] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-332] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [334-335] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-234] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [318-340] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [358-362] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [384-509] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [106-133] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-61] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-249] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [260-315] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [316-378] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-482] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [341-425] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-449] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [349-374] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [382-494] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [357-511] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [358-364] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [401-402] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [367-369] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [371-428] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [439-446] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-457] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [375-424] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [434-450] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-487] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-403] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-411] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-409] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [414-430] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-454] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-460] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [489-528] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-497] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-463] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-500] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [503-529] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-485] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-507] for track '33' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-510] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-520] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [522-528] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [530-539] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-485] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-490] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-508] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-524] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-534] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-500] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>