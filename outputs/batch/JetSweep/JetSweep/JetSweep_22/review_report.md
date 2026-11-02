# Play-Annotation-Generator Annotation Review — JetSweep_22

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `JetSweep_22`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_JetSweep`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 88
- **Validation Warnings:** 115
- **Validation Errors:** 1
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 4
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | offense | `11` | `10` |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `12` | `11` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `3` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | Team_Unknown | `15` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `10` | `9` |
| ✅ EXACT | `Action_Toss` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `16` | `14` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `6` | `5` |
| ✅ EXACT | `Action_SealBlock` | LT | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | offense | `1` | `0` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | offense | `12` | `11` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | offense | `4` | `3` |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | offense | `6` | `5` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ⚠️ AMBIGUOUS MATCH | `Action_JetMotion` | WR | `11` | `10` | 0 | START | 0 | 35 |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `10` | `Group` | 0 | START | 0 | 25 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 21 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `1` | `0` | 22 | START | 22 | 68 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `12` | `11` | 22 | START | 22 | 23 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `3` | 22 | START | 22 | 68 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `6` | `5` | 22 | START | 22 | 56 |
| ✅ EXACT | `Action_LeadBlock` | Position_Unknown | `15` | `13` | 24 | START | 24 | 67 |
| ✅ EXACT | `Action_SnapReceive` | QB | `10` | `9` | 26 | END | 26 | 26 |
| ✅ EXACT | `Action_Toss` | Position_Unknown | `16` | `14` | 34 | START | 34 | 43 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `16` | `14` | 44 | START | 44 | 45 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `6` | `5` | 57 | START | 57 | 70 |
| ✅ EXACT | `Action_SealBlock` | LT | `4` | `3` | 69 | START | 69 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RG | `1` | `0` | 70 | BOUNDARY | N/A | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | RT | `12` | `11` | 70 | BOUNDARY | N/A | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LT | `4` | `3` | 70 | BOUNDARY | 69 | 70 |
| ✅ BOUNDARY_TERMINATED | `End of OL Block` | LG | `6` | `5` | 70 | BOUNDARY | 57 | 70 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 84

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_SnapReceive` | 26 | 26 | 1 | inferred_complete_timeline |
| `Action_None` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_None` | 48 | 84 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 73 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 161 | 87 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 236 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–60
- **Visible Samples:** 60

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_JetMotion` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_JetMotion` | 37 | 60 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 68 | 47 | inferred_complete_timeline |
| `Action_SealBlock` | 69 | 70 | 2 | inferred_complete_timeline |
| `Action_None` | 71 | 96 | 26 | inferred_complete_timeline |
| `Action_None` | 108 | 239 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 56 | 35 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 57 | 70 | 14 | inferred_complete_timeline |
| `Action_None` | 71 | 193 | 123 | inferred_complete_timeline |
| `Action_None` | 201 | 206 | 6 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 212 | 218 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 68 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–27
- **Visible Samples:** 27

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_ZoneBlock` | 22 | 23 | 2 | inferred_complete_timeline |
| `Action_ZoneBlock` | 25 | 27 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–229
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 229 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>DE — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 50

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 5 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 10 | 15 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 65 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–78
- **Visible Samples:** 77

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 54 | 55 | inferred_complete_timeline |
| `Action_PreSnap` | 57 | 78 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–56
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 239 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>LB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–100
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 94 | 95 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `15` | Position_Unknown | Team_Unknown | 24–67 | 44 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 31–45 | 15 | 3 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 36–85 | 33 | 6 | Undefined position; Undefined team |
| `16` | `21` | Position_Unknown | Team_Unknown | 51–57 | 7 | 1 | Undefined position; Undefined team |
| `17` | `23` | Position_Unknown | Team_Unknown | 54–218 | 157 | 4 | Undefined position; Undefined team |
| `18` | `24` | Position_Unknown | Team_Unknown | 55–78 | 19 | 2 | Undefined position; Undefined team |
| `19` | `25` | Position_Unknown | Team_Unknown | 62–209 | 145 | 3 | Undefined position; Undefined team |
| `20` | `30` | Position_Unknown | Team_Unknown | 74–239 | 165 | 2 | Undefined position; Undefined team |
| `21` | `31` | Position_Unknown | Team_Unknown | 78–144 | 44 | 2 | Undefined position; Undefined team |
| `22` | `32` | Position_Unknown | Team_Unknown | 112–239 | 122 | 3 | Undefined position; Undefined team |
| `23` | `33` | Position_Unknown | Team_Unknown | 114–222 | 82 | 3 | Undefined position; Undefined team |
| `24` | `34` | Position_Unknown | Team_Unknown | 121–205 | 74 | 2 | Undefined position; Undefined team |
| `25` | `35` | Position_Unknown | Team_Unknown | 124–239 | 102 | 2 | Undefined position; Undefined team |
| `26` | `37` | Position_Unknown | Team_Unknown | 132–239 | 108 | 1 | Undefined position; Undefined team |
| `27` | `38` | Position_Unknown | Team_Unknown | 143–171 | 29 | 1 | Undefined position; Undefined team |
| `28` | `39` | Position_Unknown | Team_Unknown | 146–177 | 27 | 5 | Undefined position; Undefined team |
| `29` | `41` | Position_Unknown | Team_Unknown | 147–169 | 23 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 154–163 | 10 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 156–239 | 84 | 1 | Undefined position; Undefined team |
| `32` | `46` | Position_Unknown | Team_Unknown | 170–239 | 70 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 218–239 | 22 | 1 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 236–239 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_JetMotion` and target `11` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ 24 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 24 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Event 'Action_BallSnap' at frame 15 targets track ID '[?]', but it is not found in XML.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 48 |
| Missing visible bounding boxes during action | 65 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_ZoneBlock' range [22-68] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [168-169] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-96] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-73] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-161] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-193] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-206] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-218] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-100] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-229] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-54] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [57-78] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-46] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-84] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [0-35] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_JetMotion' range [37-60] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [22-23] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [25-27] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-15] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_LeadBlock' range [24-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Toss' range [34-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-38] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-58] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-62] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-72] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-85] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-57] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-106] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-124] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-159] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-218] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-71] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-168] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-209] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-79] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-144] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-125] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-177] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-174] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-207] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-222] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-191] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-205] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-184] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-171] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-153] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-169] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-163] for track '30' has 1 frames without a visible bounding box.
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