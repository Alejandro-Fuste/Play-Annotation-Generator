# Play-Annotation-Generator Annotation Review — OutsideZoneRead_130

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutsideZoneRead_130`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_OutsideZoneRead`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 93
- **Validation Warnings:** 114
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 72
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `7` | `6` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | offense | `3` | `2` |
| ✅ EXACT | `Action_Keep` | QB | offense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `3` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `3` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `11` | 4 | START | 4 | 19 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `12` | `11` | 7 | START | 20 | 27 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `5` | `4` | 7 | START | 7 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `6` | `5` | 7 | START | 7 | 97 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `7` | `6` | 7 | START | 7 | 62 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `8` | `7` | 7 | START | 7 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `3` | `2` | 19 | END | 4 | 19 |
| ✅ EXACT | `Action_ReadEdgeDefender` | QB | `3` | `2` | 23 | START | 23 | 29 |
| ✅ EXACT | `Action_Keep` | QB | `3` | `2` | 30 | START | 30 | 54 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `3` | `2` | 55 | START | 55 | 171 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 97 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_SnapReceive` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_None` | 20 | 22 | 3 | inferred_complete_timeline |
| `Action_ReadEdgeDefender` | 23 | 29 | 7 | inferred_complete_timeline |
| `Action_Keep` | 30 | 54 | 25 | inferred_complete_timeline |
| `Action_BallCarry` | 55 | 171 | 117 | inferred_complete_timeline |
| `Action_BallCarry` | 180 | 181 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 38 | 35 | inferred_complete_timeline |
| `Action_None` | 45 | 97 | 53 | inferred_complete_timeline |
| `Action_None` | 102 | 119 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 111 | 108 | inferred_complete_timeline |
| `Action_None` | 114 | 127 | 14 | inferred_complete_timeline |
| `Action_None` | 130 | 150 | 21 | inferred_complete_timeline |
| `Action_None` | 156 | 181 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 97 | 91 | inferred_complete_timeline |
| `Action_None` | 98 | 200 | 103 | inferred_complete_timeline |
| `Action_None` | 202 | 210 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 62 | 56 | inferred_complete_timeline |
| `Action_ZoneBlock` | 65 | 66 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_BallSnap` | 4 | 19 | 16 | inferred_complete_timeline |
| `Action_ZoneBlock` | 20 | 27 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 30 | 31 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 35 | 42 | 8 | inferred_complete_timeline |
| `Action_ZoneBlock` | 47 | 75 | 29 | inferred_complete_timeline |
| `Action_ZoneBlock` | 80 | 97 | 18 | inferred_complete_timeline |
| `Action_None` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 183 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 166

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 50 | 44 | inferred_complete_timeline |
| `Action_ZoneBlock` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 70 | 97 | 28 | inferred_complete_timeline |
| `Action_None` | 98 | 148 | 51 | inferred_complete_timeline |
| `Action_None` | 152 | 185 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 7 | 48 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_None` | 14 | 98 | 85 | inferred_complete_timeline |
| `Action_None` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 5 | 2 | inferred_complete_timeline |
| `Action_None` | 12 | 13 | 2 | inferred_complete_timeline |
| `Action_None` | 48 | 50 | 3 | inferred_complete_timeline |
| `Action_None` | 53 | 74 | 22 | inferred_complete_timeline |
| `Action_None` | 76 | 210 | 135 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 210 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 71 | 68 | inferred_complete_timeline |
| `Action_None` | 74 | 114 | 41 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 84 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_None` | 4 | 139 | 136 | inferred_complete_timeline |
| `Action_None` | 141 | 210 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 21–29 | 8 | 2 | Undefined position; Undefined team |
| `15` | `16` | Position_Unknown | Team_Unknown | 22–196 | 164 | 4 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 50–201 | 143 | 5 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 56–207 | 152 | 1 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 79–210 | 129 | 2 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 80–210 | 131 | 1 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 82–91 | 10 | 1 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 92–122 | 30 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 104–107 | 4 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 125–129 | 5 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 127–210 | 84 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 128–210 | 9 | 2 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 140–148 | 7 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 140–142 | 3 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 142–210 | 63 | 2 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 186–187 | 2 | 1 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 203–207 | 5 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 203–204 | 2 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 205–210 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 71 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '4' (RG) duration 91 frames exceeds threshold 90 frames [start=7, end=97].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 91 frames exceeds threshold 90 frames [start=7, end=97].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 91 frames exceeds threshold 90 frames [start=7, end=97].
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [4–19], lower_priority='Action_ZoneBlock' annotated_start=7, effective_Action_ZoneBlock_start=20.
- ⚠️ Action 'Action_None' range [4-38] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-111] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-150] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [55-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [180-181] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-84] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-50] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [67-68] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-148] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-185] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-200] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-62] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [65-66] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [7-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-114] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [20-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [30-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [35-42] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [47-75] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-183] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-13] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-50] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-210] for track '12' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [4-9] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-98] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [21-25] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-24] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-48] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-68] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-196] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-201] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-207] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-210] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-122] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-143] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-145] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-207] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-210] for track '32' has 2 frames without a visible bounding box.
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

</details>