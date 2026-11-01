# Play-Annotation-Generator Annotation Review — InsideZoneRead_115

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_115`
- **Frame Range:** 0 to 689 (690 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 689
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 80
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `7` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `15` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `17` | `16` |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 570 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 570 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 590 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 0 | START | 0 | 570 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 408 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 228 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `6` | `Group` | 0 | START | 0 | 567 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `7` | `Group` | 0 | START | 0 | 567 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | C | `22` | `21` | 568 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `10` | `9` | 571 | START | 571 | 612 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `12` | `11` | 571 | START | 571 | 634 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `15` | 571 | START | 571 | 615 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `17` | `16` | 571 | START | 571 | 640 |
| ❌ MISSING SEGMENT | `Action_ZoneBlock` | C | `22` | `21` | 571 | START | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 579 | END | 568 | 579 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `17` | 588 | START | 588 | 594 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 595 | START | 595 | 601 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `14` | `13` | 602 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 640 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_SnapReceive` | 568 | 579 | 12 | inferred_complete_timeline |
| `Action_None` | 580 | 587 | 8 | inferred_complete_timeline |
| `Action_ReadDefender` | 588 | 594 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 595 | 601 | 7 | inferred_complete_timeline |
| `Action_None` | 602 | 689 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–590
- **Visible Samples:** 591

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 590 | 591 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 688

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 680 | 113 | inferred_complete_timeline |
| `Action_None` | 683 | 689 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 683 | 116 | inferred_complete_timeline |
| `Action_None` | 688 | 689 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 685

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 570 | 571 | inferred_complete_timeline |
| `Action_ZoneBlock` | 571 | 612 | 42 | inferred_complete_timeline |
| `Action_ZoneBlock` | 618 | 640 | 23 | inferred_complete_timeline |
| `Action_None` | 641 | 689 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 677

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 408 | 409 | inferred_complete_timeline |
| `Action_PreSnap` | 411 | 413 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 425 | 570 | 146 | inferred_complete_timeline |
| `Action_ZoneBlock` | 571 | 640 | 70 | inferred_complete_timeline |
| `Action_None` | 641 | 689 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 228 | 229 | inferred_complete_timeline |
| `Action_PreSnap` | 230 | 231 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–689
- **Visible Samples:** 680

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 570 | 571 | inferred_complete_timeline |
| `Action_ZoneBlock` | 571 | 615 | 45 | inferred_complete_timeline |
| `Action_ZoneBlock` | 623 | 626 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 630 | 640 | 11 | inferred_complete_timeline |
| `Action_None` | 641 | 689 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–634
- **Visible Samples:** 635

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 570 | 571 | inferred_complete_timeline |
| `Action_ZoneBlock` | 571 | 634 | 64 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 689

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 637 | 70 | inferred_complete_timeline |
| `Action_None` | 639 | 689 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 686

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 6 | 567 | 562 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–243
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 55 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 60 | 243 | 184 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–642
- **Visible Samples:** 595

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 474 | 475 | inferred_complete_timeline |
| `Action_PreSnap` | 513 | 567 | 55 | inferred_complete_timeline |
| `Action_None` | 568 | 588 | 21 | inferred_complete_timeline |
| `Action_None` | 593 | 632 | 40 | inferred_complete_timeline |
| `Action_None` | 635 | 636 | 2 | inferred_complete_timeline |
| `Action_None` | 641 | 642 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–255
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |
| `Action_PreSnap` | 239 | 244 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 246 | 255 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–689
- **Visible Samples:** 690

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 567 | 568 | inferred_complete_timeline |
| `Action_None` | 568 | 689 | 122 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–427 | 428 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 227–689 | 430 | 6 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 308–613 | 227 | 10 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 363–618 | 252 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 469–689 | 221 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 595–689 | 95 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 597–605 | 9 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 636–683 | 48 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 642–684 | 39 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 652–677 | 16 | 3 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 671–689 | 7 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `22` (C)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (4 segments found)
- ❌ Missing segment for action `Action_ZoneBlock` on target `22` (C)
- ❌ Missing segment for action `Action_BallCarry` on target `14` (RB)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 53 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 232: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '13' has invalid range: start=602, end=590. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '21' has invalid range: start=568, end=231. Clamping end to start.
- ⚠️ Segment 'Action_ZoneBlock' for track '21' has invalid range: start=571, end=231. Clamping end to start.
- ⚠️ Action 'Action_None' range [568-683] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-689] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-680] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [571-612] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [239-244] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [246-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [571-634] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-637] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [639-689] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-590] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-427] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [571-615] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [623-626] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-408] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [411-413] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-474] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-588] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [593-632] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [635-636] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [641-642] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-55] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-243] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-228] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [230-231] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-243] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [253-254] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-652] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [659-661] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-689] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [308-311] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [314-317] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [339-343] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [354-364] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [375-380] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [382-393] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [400-401] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [421-429] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [440-567] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-613] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [568-598] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [603-618] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [597-605] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [636-683] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [642-664] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [669-684] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [652-659] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [662-667] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [676-677] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [671-673] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [684-685] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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

</details>