# Play-Annotation-Generator Annotation Review — InsideZoneRead_171

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_171`
- **Frame Range:** 0 to 599 (600 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 599
- **Player Tracks:** 43
- **Ball Tracks:** 0
- **Action Segments:** 132
- **Validation Warnings:** 158
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 114
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LB1 | defense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `9` |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | Team_Unknown | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | Team_Unknown | `10` | `9` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `11` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `5` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 31 |
| ✅ EXACT | `Action_BallSnap` | LB1 | `14` | `13` | 32 | START | 32 | 48 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `11` | `10` | 35 | START | 35 | 120 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 35 | START | 35 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 35 | START | 35 | 120 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `5` | 35 | START | 35 | 120 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `9` | 48 | END | 32 | 48 |
| ✅ EXACT | `Action_ReadDefender` | Position_Unknown | `10` | `9` | 50 | START | 50 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | Position_Unknown | `10` | `9` | 73 | START | 73 | 454 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 593

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 215 | 184 | inferred_complete_timeline |
| `Action_None` | 223 | 599 | 377 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 240 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 222 | 191 | inferred_complete_timeline |
| `Action_None` | 224 | 255 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–444
- **Visible Samples:** 445

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_None` | 121 | 444 | 324 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–434
- **Visible Samples:** 432

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_None` | 121 | 263 | 143 | inferred_complete_timeline |
| `Action_None` | 265 | 266 | 2 | inferred_complete_timeline |
| `Action_None` | 269 | 434 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–599
- **Visible Samples:** 521

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_None` | 121 | 168 | 48 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 420 | 240 | inferred_complete_timeline |
| `Action_None` | 477 | 479 | 3 | inferred_complete_timeline |
| `Action_None` | 493 | 599 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–588
- **Visible Samples:** 498

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 120 | 86 | inferred_complete_timeline |
| `Action_None` | 121 | 411 | 291 | inferred_complete_timeline |
| `Action_None` | 413 | 430 | 18 | inferred_complete_timeline |
| `Action_None` | 435 | 444 | 10 | inferred_complete_timeline |
| `Action_None` | 523 | 573 | 51 | inferred_complete_timeline |
| `Action_None` | 582 | 588 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 598

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 405 | 374 | inferred_complete_timeline |
| `Action_None` | 407 | 514 | 108 | inferred_complete_timeline |
| `Action_None` | 516 | 599 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–319
- **Visible Samples:** 306

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 289 | 258 | inferred_complete_timeline |
| `Action_None` | 297 | 305 | 9 | inferred_complete_timeline |
| `Action_None` | 313 | 319 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–495
- **Visible Samples:** 484

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 266 | 235 | inferred_complete_timeline |
| `Action_None` | 268 | 410 | 143 | inferred_complete_timeline |
| `Action_None` | 421 | 492 | 72 | inferred_complete_timeline |
| `Action_None` | 494 | 495 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–469
- **Visible Samples:** 459

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_BallSnap` | 32 | 48 | 17 | inferred_complete_timeline |
| `Action_None` | 49 | 436 | 388 | inferred_complete_timeline |
| `Action_None` | 440 | 443 | 4 | inferred_complete_timeline |
| `Action_None` | 452 | 469 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 577

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 433 | 402 | inferred_complete_timeline |
| `Action_None` | 437 | 439 | 3 | inferred_complete_timeline |
| `Action_None` | 459 | 461 | 3 | inferred_complete_timeline |
| `Action_None` | 463 | 599 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–377
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_None` | 32 | 168 | 137 | inferred_complete_timeline |
| `Action_None` | 184 | 189 | 6 | inferred_complete_timeline |
| `Action_None` | 193 | 377 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–599
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 3 | 7 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 31 | 19 | inferred_complete_timeline |
| `Action_None` | 32 | 540 | 509 | inferred_complete_timeline |
| `Action_None` | 570 | 581 | 12 | inferred_complete_timeline |
| `Action_None` | 588 | 599 | 12 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–599 | 565 | 7 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 155–297 | 80 | 6 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 250–599 | 256 | 4 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 320–396 | 77 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 395–500 | 102 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 402–548 | 128 | 3 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 425–568 | 143 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 432–599 | 83 | 4 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 440–460 | 17 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 442–599 | 158 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 445–571 | 127 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 450–599 | 120 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 451–485 | 30 | 2 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 456–599 | 118 | 8 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 484–596 | 111 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 491–582 | 69 | 5 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 507–599 | 93 | 1 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 509–559 | 51 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 512–520 | 9 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 517–576 | 60 | 1 | Undefined position; Undefined team |
| `34` | `37` | Position_Unknown | Team_Unknown | 524–599 | 74 | 2 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 565–599 | 35 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 567–568 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 573–581 | 9 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 578–590 | 6 | 2 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 581–599 | 19 | 1 | Undefined position; Undefined team |
| `40` | `47` | Position_Unknown | Team_Unknown | 592–599 | 8 | 1 | Undefined position; Undefined team |
| `41` | `48` | Position_Unknown | Team_Unknown | 593–599 | 7 | 1 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 597–599 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `8`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 29 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 29 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 58 |
| Missing visible bounding boxes during action | 97 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
- ⚠️ Action 'Action_None' range [32-240] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-411] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [413-430] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-444] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [523-573] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [582-588] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-168] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-420] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [477-479] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [493-599] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-433] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [437-439] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [459-461] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-222] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-255] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-444] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-215] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-168] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-189] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-377] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-266] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-410] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [421-492] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [73-454] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [458-468] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [501-599] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-263] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-434] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-289] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-305] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [313-319] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-405] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [407-514] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-436] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-443] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [452-469] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [3-7] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [32-540] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [570-581] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-212] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-223] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-273] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [278-297] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-424] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [454-466] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [468-483] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [320-396] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [395-445] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-500] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-455] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [463-470] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [483-548] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [425-433] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [435-568] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [432-436] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-446] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [448-470] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [440-452] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [457-460] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [445-571] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [450-498] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [513-529] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [531-533] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [451-456] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [462-485] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [456-461] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [476-479] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [482-483] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [487-489] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-492] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [495-537] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-542] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [545-599] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [484-585] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [588-596] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [491-494] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [506-518] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [521-522] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [526-573] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-582] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-559] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [512-520] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [517-576] for track '33' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-534] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [565-599] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [567-568] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [573-581] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [578-581] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [589-590] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [581-599] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-599] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_171'; source metadata written as null.

</details>