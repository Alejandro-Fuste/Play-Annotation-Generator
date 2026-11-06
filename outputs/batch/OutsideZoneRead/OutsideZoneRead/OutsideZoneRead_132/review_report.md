# Play-Annotation-Generator Annotation Review — OutsideZoneRead_132

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_132`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 66
- **Validation Warnings:** 66
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 44
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `10` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_Keep` | QB | offense | `5` | `4` |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `9` | 7 | START | 7 | 20 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `10` | `9` | 10 | START | 21 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `14` | `13` | 10 | START | 10 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `2` | 10 | START | 10 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `6` | `5` | 10 | START | 10 | 75 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `7` | `6` | 10 | START | 10 | 39 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 20 | END | 7 | 20 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `5` | `4` | 25 | START | 25 | 29 |
| ✅ EXACT | `Action_Keep` | QB | `5` | `4` | 30 | START | 30 | 51 |
| ✅ EXACT | `Action_BlockSecondLevel` | RT | `7` | `6` | 40 | START | 40 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 52 | START | 52 | 161 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 75 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_None` | 21 | 24 | 4 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 25 | 29 | 5 | inferred_complete_timeline |
| `Action_Keep` | 30 | 51 | 22 | inferred_complete_timeline |
| `Action_BallCarry` | 52 | 161 | 110 | inferred_complete_timeline |
| `Action_BallCarry` | 164 | 173 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 90 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 84 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 75 | 66 | inferred_complete_timeline |
| `Action_None` | 76 | 88 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 75 | 66 | inferred_complete_timeline |
| `Action_None` | 76 | 97 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 20 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 21 | 75 | 55 | inferred_complete_timeline |
| `Action_None` | 76 | 86 | 11 | inferred_complete_timeline |
| `Action_None` | 88 | 102 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 75 | 66 | inferred_complete_timeline |
| `Action_None` | 76 | 113 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 10 | 39 | 30 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 40 | 75 | 36 | inferred_complete_timeline |
| `Action_None` | 76 | 118 | 43 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–31
- **Visible Samples:** 32

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 31 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 180 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 15 | 9 | inferred_complete_timeline |
| `Action_None` | 51 | 101 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 27 | 21 | inferred_complete_timeline |
| `Action_None` | 29 | 104 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–97
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 64 | 58 | inferred_complete_timeline |
| `Action_None` | 69 | 83 | 15 | inferred_complete_timeline |
| `Action_None` | 86 | 97 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 123 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–35
- **Visible Samples:** 36

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 35 | 29 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 39–41 | 3 | 1 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 42–86 | 40 | 2 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 44–86 | 40 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 53–178 | 126 | 1 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 56–82 | 27 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 65–78 | 14 | 1 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 102–154 | 52 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 104–180 | 75 | 2 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 107–155 | 17 | 4 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 165–180 | 16 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 170–174 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_ZoneBlock` for actor_track_id `10` (C): Annotated start 10 != Inferred start 21
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

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
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [7–20], lower_priority='Action_ZoneBlock' annotated_start=10, effective_Action_ZoneBlock_start=21.
- ⚠️ Action 'Action_None' range [7-123] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-64] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-83] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-97] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-113] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-90] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [52-161] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [164-173] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-97] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-118] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-84] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-180] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-86] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-31] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-15] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-101] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-27] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-88] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-35] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-86] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-86] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-82] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-78] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-137] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-154] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-139] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-180] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-112] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-180] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-174] for track '26' has 1 frames without a visible bounding box.
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

</details>