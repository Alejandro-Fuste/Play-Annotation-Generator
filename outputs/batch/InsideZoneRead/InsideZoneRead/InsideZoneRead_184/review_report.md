# Play-Annotation-Generator Annotation Review — InsideZoneRead_184

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_184`
- **Frame Range:** 0 to 569 (570 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 569
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 67
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
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | CB2 | defense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `19` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `20` | `19` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `6` | `5` |
| ✅ EXACT | `Action_ReadDefender` | DE2 | defense | `6` | `5` |
| ✅ EXACT | `Action_Handoff` | DE2 | defense | `6` | `5` |
| ✅ EXACT | `Action_BallCarry` | DE1 | defense | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 413 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 421 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 185 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 422 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 425 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 425 |
| ✅ EXACT | `Action_BallSnap` | CB2 | `12` | `11` | 423 | START | 423 | 437 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `19` | `18` | 426 | START | 426 | 508 |
| ✅ EXACT | `Action_ZoneBlock` | C | `20` | `19` | 426 | START | 426 | 508 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | RG | `22` | `21` | 426 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `7` | `6` | 426 | START | 426 | 508 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 426 | START | 426 | 508 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `6` | `5` | 437 | END | 423 | 437 |
| ✅ EXACT | `Action_ReadDefender` | DE2 | `6` | `5` | 443 | START | 443 | 463 |
| ✅ EXACT | `Action_Handoff` | DE2 | `6` | `5` | 464 | START | 464 | 477 |
| ✅ EXACT | `Action_BallCarry` | DE1 | `2` | `1` | 478 | START | 478 | 569 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 508 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 569

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 413 | 414 | inferred_complete_timeline |
| `Action_PreSnap` | 415 | 422 | 8 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 508 | 83 | inferred_complete_timeline |
| `Action_None` | 509 | 515 | 7 | inferred_complete_timeline |
| `Action_None` | 518 | 569 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 508 | 83 | inferred_complete_timeline |
| `Action_None` | 509 | 569 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 421 | 422 | inferred_complete_timeline |
| `Action_PreSnap` | 424 | 425 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 508 | 83 | inferred_complete_timeline |
| `Action_None` | 509 | 569 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 193 | 234 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 425 | 426 | inferred_complete_timeline |
| `Action_ZoneBlock` | 426 | 508 | 83 | inferred_complete_timeline |
| `Action_None` | 509 | 569 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 477 | 478 | inferred_complete_timeline |
| `Action_BallCarry` | 478 | 569 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_SnapReceive` | 423 | 437 | 15 | inferred_complete_timeline |
| `Action_None` | 438 | 442 | 5 | inferred_complete_timeline |
| `Action_ReadDefender` | 443 | 463 | 21 | inferred_complete_timeline |
| `Action_Handoff` | 464 | 477 | 14 | inferred_complete_timeline |
| `Action_None` | 478 | 569 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 559

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 408 | 409 | inferred_complete_timeline |
| `Action_PreSnap` | 420 | 422 | 3 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–518
- **Visible Samples:** 501

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 450 | 28 | inferred_complete_timeline |
| `Action_None` | 469 | 518 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_BallSnap` | 423 | 437 | 15 | inferred_complete_timeline |
| `Action_None` | 438 | 569 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 570

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 569 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–569
- **Visible Samples:** 568

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 565 | 143 | inferred_complete_timeline |
| `Action_None` | 568 | 569 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB6 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–441
- **Visible Samples:** 442

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 422 | 423 | inferred_complete_timeline |
| `Action_None` | 423 | 441 | 19 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `27` | Position_Unknown | Team_Unknown | 181–473 | 255 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 414–416 | 3 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 421–426 | 6 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 423–424 | 2 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 454–569 | 116 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 460–565 | 70 | 9 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 486–487 | 2 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 494–569 | 69 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 525–527 | 3 | 1 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 527–569 | 43 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 528–564 | 15 | 3 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 540–548 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (2 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (RG)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=426, end=234. Clamping end to start.
- ⚠️ Action 'Action_BallCarry' range [478-569] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-515] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-565] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-569] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-413] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-450] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [469-518] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-422] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-569] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-441] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-421] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-408] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-569] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-196] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-470] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [472-473] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [414-416] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-426] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [423-424] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [460-466] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [470-477] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [485-487] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [490-494] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [502-503] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [509-513] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [524-555] for track '27' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [557-562] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [564-565] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [486-487] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [494-495] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [497-522] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-542] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [525-527] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [527-569] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [528-531] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [550-551] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [556-564] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [540-548] for track '33' has 1 frames without a visible bounding box.
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
- ⚠️ Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_184'; source metadata written as null.

</details>