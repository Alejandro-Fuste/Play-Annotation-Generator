# Play-Annotation-Generator Annotation Review — OutsideZoneRead_128

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_128`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 64
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `6` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `3` | `2` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `4` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `2` | `1` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | offense | `4` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `4` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `12` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `6` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `6` | `5` | 7 | START | 7 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `14` | `13` | 10 | START | 10 | 29 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `15` | `14` | 10 | START | 10 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 10 | START | 10 | 25 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `3` | `2` | 10 | START | 10 | 74 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `6` | `5` | 10 | START | 24 | 90 |
| ✅ EXACT | `Action_SnapReceive` | QB | `4` | `3` | 23 | END | 7 | 23 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `2` | `1` | 26 | START | 26 | 90 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `4` | `3` | 29 | START | 29 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_Keep` | QB | `4` | `3` | 34 | START | 34 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `4` | `3` | 54 | START | 54 | 276 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 90 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_None` | 24 | 28 | 5 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 29 | 33 | 5 | inferred_complete_timeline |
| `Action_Keep` | 34 | 44 | 11 | inferred_complete_timeline |
| `Action_Keep` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 54 | 276 | 223 | inferred_complete_timeline |
| `Action_BallCarry` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 94

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 46 | 40 | inferred_complete_timeline |
| `Action_None` | 50 | 96 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 296

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 21 | 15 | inferred_complete_timeline |
| `Action_None` | 23 | 48 | 26 | inferred_complete_timeline |
| `Action_None` | 50 | 209 | 160 | inferred_complete_timeline |
| `Action_None` | 211 | 298 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 74 | 65 | inferred_complete_timeline |
| `Action_ZoneBlock` | 77 | 89 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–43
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 29 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 42 | 43 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 24 | 90 | 67 | inferred_complete_timeline |
| `Action_None` | 91 | 103 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 90 | 81 | inferred_complete_timeline |
| `Action_None` | 91 | 110 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 25 | 16 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 26 | 90 | 65 | inferred_complete_timeline |
| `Action_None` | 91 | 171 | 81 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 94 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 276 | 270 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_None` | 7 | 98 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 81 | 75 | inferred_complete_timeline |
| `Action_None` | 84 | 121 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 282 | 276 | inferred_complete_timeline |
| `Action_None` | 285 | 286 | 2 | inferred_complete_timeline |
| `Action_None` | 288 | 299 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 108 | 102 | inferred_complete_timeline |
| `Action_None` | 115 | 180 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 92 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 299 | 293 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `21` | Position_Unknown | Team_Unknown | 56–88 | 33 | 1 | Undefined position; Undefined team |
| `17` | `24` | Position_Unknown | Team_Unknown | 69–86 | 18 | 1 | Undefined position; Undefined team |
| `18` | `26` | Position_Unknown | Team_Unknown | 73–77 | 5 | 1 | Undefined position; Undefined team |
| `19` | `28` | Position_Unknown | Team_Unknown | 79–82 | 4 | 1 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 87–90 | 4 | 1 | Undefined position; Undefined team |
| `21` | `33` | Position_Unknown | Team_Unknown | 166–167 | 2 | 1 | Undefined position; Undefined team |
| `22` | `34` | Position_Unknown | Team_Unknown | 185–188 | 4 | 1 | Undefined position; Undefined team |
| `23` | `37` | Position_Unknown | Team_Unknown | 228–233 | 6 | 1 | Undefined position; Undefined team |
| `24` | `38` | Position_Unknown | Team_Unknown | 239–299 | 61 | 1 | Undefined position; Undefined team |
| `25` | `39` | Position_Unknown | Team_Unknown | 242–282 | 41 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `3` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `6` (C): Annotated start 10 != Inferred start 24
- ⚠️ Ambiguous match for action `Action_Keep` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `4` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [7–23], lower_priority='Action_ZoneBlock' annotated_start=10, effective_Action_ZoneBlock_start=24.
- ⚠️ Action 'Action_None' range [7-92] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-171] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-74] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [77-89] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Keep' range [34-44] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [54-276] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-103] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-276] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-282] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-299] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-96] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-21] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-48] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-209] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-298] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-81] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-121] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-29] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [42-43] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [10-90] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-98] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-88] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-77] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-90] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-282] for track '25' has 1 frames without a visible bounding box.
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

</details>