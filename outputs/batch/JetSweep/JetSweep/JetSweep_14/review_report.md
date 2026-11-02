# Play-Annotation-Generator Annotation Review — JetSweep_14

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `JetSweep_14`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 73
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 26
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 5
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 45
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `16` | `14` |
| ⚠️ START CHANGED | `Action_BallSnap` | C | offense | `17` | `15` |
| ✅ EXACT | `Action_LeadBlock` | TE | offense | `5` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `10` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `17` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `6` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `13` | `12` |
| ✅ EXACT | `Action_Toss` | QB | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | offense | `16` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `10` | `9` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | offense | `17` | `15` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `6` | `5` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `7` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `10` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 41 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `16` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 57 |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `16` | `14` | 43 | START | 43 | 60 |
| ⚠️ START CHANGED | `Action_BallSnap` | C | `17` | `15` | 55 | START | 59 | 68 |
| ✅ EXACT | `Action_LeadBlock` | TE | `5` | `4` | 58 | START | 58 | 86 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `10` | `9` | 58 | START | 58 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 58 | START | 58 | 74 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `17` | `15` | 58 | START | 69 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `6` | `5` | 58 | START | 58 | 107 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `7` | `6` | 58 | START | 58 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `13` | `12` | 68 | END | 60 | 68 |
| ✅ EXACT | `Action_Toss` | QB | `13` | `12` | 73 | START | 73 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR | `16` | `14` | 76 | START | 76 | 76 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | RT | `12` | `11` | 85 | START | 85 | 97 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `10` | `9` | 107 | BOUNDARY | N/A | 107 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `12` | `11` | 107 | BOUNDARY | 99 | 107 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | C | `17` | `15` | 107 | BOUNDARY | N/A | 107 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `6` | `5` | 107 | BOUNDARY | 58 | 107 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `7` | `6` | 107 | BOUNDARY | N/A | 107 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–107
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 41 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 45 | 46 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 53 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 68 | 9 | inferred_complete_timeline |
| `Action_None` | 69 | 72 | 4 | inferred_complete_timeline |
| `Action_Toss` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_None` | 76 | 97 | 22 | inferred_complete_timeline |
| `Action_None` | 100 | 103 | 4 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `16`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 43–201
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 43 | 60 | 18 | inferred_complete_timeline |
| `Action_JetMotion` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 76 | 76 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 82 | 96 | 15 | inferred_complete_timeline |
| `Action_BallCarry` | 100 | 201 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_LeadBlock` | 58 | 86 | 29 | inferred_complete_timeline |
| `Action_None` | 119 | 239 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–81
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 81 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 97 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 59–106
- **Visible Samples:** 23

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_BallSnap` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_ZoneBlock` | 69 | 71 | 3 | inferred_complete_timeline |
| `Action_ZoneBlock` | 97 | 106 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 107 | 50 | inferred_complete_timeline |
| `Action_None` | 108 | 110 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 58 | 74 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 85 | 97 | 13 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 99 | 107 | 9 | inferred_complete_timeline |
| `Action_None` | 108 | 108 | 1 | inferred_complete_timeline |
| `Action_None` | 110 | 154 | 45 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 121 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–94
- **Visible Samples:** 95

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 94 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–105
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 105 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 124 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 142 | 88 | inferred_complete_timeline |
| `Action_None` | 144 | 160 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_None` | 55 | 121 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>SS — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–30
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `15`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 29–239
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 29 | 54 | 26 | inferred_complete_timeline |
| `Action_None` | 55 | 239 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `18` | Position_Unknown | Team_Unknown | 74–114 | 41 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 83–104 | 15 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 101–156 | 54 | 2 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 106–239 | 127 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 108–239 | 132 | 1 | Undefined position; Undefined team |
| `21` | `29` | Position_Unknown | Team_Unknown | 134–236 | 103 | 1 | Undefined position; Undefined team |
| `22` | `30` | Position_Unknown | Team_Unknown | 153–155 | 3 | 1 | Undefined position; Undefined team |
| `23` | `32` | Position_Unknown | Team_Unknown | 174–175 | 2 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 209–238 | 16 | 4 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 209–215 | 6 | 2 | Undefined position; Undefined team |
| `26` | `39` | Position_Unknown | Team_Unknown | 229–239 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `16` (2 segments found)
- ⚠️ `Action_BallSnap` for actor_track_id `17` (C): Annotated start 55 != Inferred start 59
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [59–68], lower_priority='Action_ZoneBlock' annotated_start=59, effective_Action_ZoneBlock_start=69.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-121] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-142] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-160] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-121] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [58-86] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-97] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-105] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-124] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-81] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [58-74] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [76-84] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [85-97] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '11' starts at frame 108, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [108-108] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-154] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-41] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [45-46] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-97] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [43-60] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [63-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '14' starts at frame 76, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [76-76] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [82-96] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [100-201] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [69-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [97-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-114] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-139] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-156] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-123] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-236] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-225] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
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